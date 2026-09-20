"""
Compila DEUS MACHINA | TOOLS con PyInstaller (carpeta, sin consola).

Uso (en la carpeta del proyecto, con el venv de la app activado):
    pip install -U pyinstaller pyinstaller-hooks-contrib
    python build_pyinstaller.py

Versión CON consola (para diagnosticar; muestra todo lo que imprime la app):
    set DMT_CONSOLA=1
    python build_pyinstaller.py

Resultado:
    dist\\DEUS_MACHINA_TOOLS\\DEUS_MACHINA_TOOLS.exe
Después copia la carpeta 'tools' (ffmpeg, ghostscript, modelos...) junto al .exe.

Registros de la app compilada (sin consola):
    %LOCALAPPDATA%\\DeusMachinaTools\\logs\\ultima_sesion.log   (app)
    %LOCALAPPDATA%\\DeusMachinaTools\\logs\\motor_ocr.log       (motor OCR)

CUDA sin PyTorch:
  La app ya no importa PyTorch: solo necesita las DLL de NVIDIA (CUDA 12.9 /
  cuDNN 9.10) que vienen dentro de torch\\lib. Este script NO empaqueta torch
  y copia esas DLL a dist\\DEUS_MACHINA_TOOLS\\_internal\\cuda.
  Si existe 'cuda_necesarias.txt' (lo genera diagnostico_cuda.py después de
  probar Whisper y PaddleOCR en tu GPU), se copian solo esas.

Qué hace además de compilar:
  1. Durante la compilación quita del PATH las carpetas con DLLs de CUDA o del
     runtime de Visual C++ (CUDA Toolkit, Anaconda, etc.). Si no, PyInstaller
     puede empaquetar copias de otra versión que chocan con las de la app
     (la app usa SOLO las de su carpeta cuda) y se cierra al transcribir o
     al cargar el OCR.
  2. Al terminar revisa las DLLs empaquetadas:
     · runtime de Visual C++ (msvcp140, vcruntime140...): si alguna es más vieja
       que la de Windows se reemplaza. Con una versión vieja, ONNX Runtime
       (RapidOCR, Quitar fondo) y CTranslate2 (Whisper) se cierran de golpe.
     · CUDA/cuDNN duplicadas fuera de _internal\\cuda: se eliminan de la raíz
       de _internal (y los restos de torch) y se avisa de cualquier otra copia.
"""
import ctypes
import importlib.metadata
import importlib.util
import os
import shutil
import subprocess
import sys

APP = "Deus_machina_tools.py"
NOMBRE = "DEUS_MACHINA_TOOLS"
CONSOLA = os.environ.get("DMT_CONSOLA", "").strip() == "1"

# Librerías que no usa la app (reducen tamaño y tiempo de análisis)
EXCLUIR = [
    "PyQt5", "PyQt6", "PySide2", "PySide6",
    "matplotlib", "mpl_toolkits", "astropy",
    "IPython", "jupyter", "notebook", "pytest",
    # PyTorch no se empaqueta: la app solo usa sus DLL de NVIDIA (se copian aparte)
    "torch", "torchvision", "torchaudio", "tensorboard", "triton",
]

# Paquetes con datos, DLLs o importaciones dinámicas: se incluyen completos
COLECTAR_TODO = [
    "faster_whisper",   # modelo VAD (silero .onnx)
    "ctranslate2",      # DLLs del motor de Whisper
    "paddle",           # PaddlePaddle GPU (DLLs en paddle\\libs)
    "paddlex",          # configuraciones YAML de los pipelines
    "paddleocr",
    "rapidocr",         # modelos ONNX y config YAML incluidos
    "rembg",
    "pymupdf",
    "curl_cffi",        # libcurl-impersonate + certificados
    "spotdl",           # se ejecuta con el propio .exe (--dmt-run-module)
    "yt_dlp_ejs",       # scripts JS que usa Deno para YouTube
]

# Solo datos
COLECTAR_DATOS = [
    "ytmusicapi",       # traducciones (spotDL)
    "pykakasi",         # diccionarios (spotDL)
]

# Metadatos (dist-info) que las librerías consultan al ejecutarse.
# PaddleX revisa 'opencv-contrib-python', 'shapely', 'pyclipper'... y si faltan
# deja de importar cv2; pymatting (rembg) y ytmusicapi leen su propia versión.
METADATOS_RECURSIVOS = [
    "paddlex", "paddleocr", "rapidocr", "rembg", "spotdl", "faster-whisper", "yt-dlp",
]
METADATOS = [
    "opencv-contrib-python", "opencv-python", "paddlepaddle-gpu",
    "imagesize", "pyclipper", "pypdfium2", "python-bidi", "shapely",
    "PyMatting", "ytmusicapi", "yt-dlp-ejs", "huggingface_hub", "tqdm",
    "requests", "numpy", "pillow", "tokenizers", "safetensors",
]

# Importaciones que la app hace con importlib (carga en segundo plano) y que
# el análisis estático no ve; PIL._tkinter_finder lo necesita ImageTk.
IMPORTS_OCULTOS = [
    "numpy", "cv2", "pymupdf", "PyPDF2", "yt_dlp",
    "faster_whisper", "pyaudio", "piexif", "mutagen", "docx", "openpyxl", "pptx",
    "PIL._tkinter_finder",
]

# DLLs del runtime de Visual C++
DLL_RUNTIME_VC = {
    "msvcp140.dll", "msvcp140_1.dll", "msvcp140_2.dll", "msvcp140_atomic_wait.dll",
    "msvcp140_codecvt_ids.dll", "vcruntime140.dll", "vcruntime140_1.dll",
    "concrt140.dll", "vccorlib140.dll", "vcomp140.dll",
}
# DLLs de CUDA / cuDNN (la app usa SOLO las de la carpeta cuda)
PREFIJOS_CUDA = (
    "cublas", "cudnn", "cudart", "cufft", "curand", "cusolver", "cusparse",
    "nvrtc", "nvjitlink", "nvtoolsext", "cupti", "zlibwapi",
)
# DLLs de torch\lib que la app NO usa (mismo criterio que _cuda_dll_util en la app)
CUDA_NO_COPIAR_PREFIJOS = ("torch", "c10", "caffe2", "fbgemm", "asmjit", "shm", "uv",
                           "libiomp", "cupti", "cufftw", "cusolvermg")
CUDA_NO_COPIAR_EXACTOS = {"nvrtc64_120_0.alt.dll"}


# ----------------------------------------------------------------------------
#  Utilidades
# ----------------------------------------------------------------------------
def _paquete_instalado(nombre):
    try:
        return importlib.util.find_spec(nombre) is not None
    except Exception:
        return False


def _distribucion_instalada(nombre):
    try:
        importlib.metadata.distribution(nombre)
        return True
    except importlib.metadata.PackageNotFoundError:
        return False


def _filtrar(lista, existe, tipo):
    ok = [x for x in lista if existe(x)]
    for x in lista:
        if x not in ok:
            print(f"  [aviso] {tipo} '{x}' no está instalado en este entorno: se omite")
    return ok


def _version_dll(ruta):
    """Versión de archivo como tupla (14, 44, 35211, 0); () si no se puede leer."""
    if os.name != "nt" or not os.path.isfile(ruta):
        return ()
    try:
        from ctypes import wintypes
        ver = ctypes.WinDLL("version")
        ver.GetFileVersionInfoSizeW.argtypes = [wintypes.LPCWSTR, ctypes.POINTER(wintypes.DWORD)]
        ver.GetFileVersionInfoSizeW.restype = wintypes.DWORD
        ver.GetFileVersionInfoW.argtypes = [wintypes.LPCWSTR, wintypes.DWORD, wintypes.DWORD, ctypes.c_void_p]
        ver.GetFileVersionInfoW.restype = wintypes.BOOL
        ver.VerQueryValueW.argtypes = [ctypes.c_void_p, wintypes.LPCWSTR,
                                       ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(wintypes.UINT)]
        ver.VerQueryValueW.restype = wintypes.BOOL
        tam = ver.GetFileVersionInfoSizeW(ruta, None)
        if not tam:
            return ()
        buf = ctypes.create_string_buffer(tam)
        if not ver.GetFileVersionInfoW(ruta, 0, tam, buf):
            return ()
        ptr, largo = ctypes.c_void_p(), wintypes.UINT()
        if not ver.VerQueryValueW(buf, "\\", ctypes.byref(ptr), ctypes.byref(largo)) or not ptr.value:
            return ()
        campos = ctypes.cast(ptr, ctypes.POINTER(wintypes.DWORD * 4)).contents
        ms, ls = campos[2], campos[3]
        return (ms >> 16, ms & 0xFFFF, ls >> 16, ls & 0xFFFF)
    except Exception:
        return ()


def _txt_version(v):
    return ".".join(str(x) for x in v) if v else "?"


def _path_de_compilacion():
    """PATH sin carpetas que aporten DLLs de CUDA o del runtime de VC++ ajenas a la app."""
    if os.name != "nt":
        return os.environ.get("PATH", "")
    sistema = os.path.normcase(os.environ.get("SystemRoot", r"C:\Windows"))
    # Las carpetas del propio Python y del venv nunca se quitan
    propias = {os.path.normcase(os.path.abspath(p)) for p in (
        sys.base_prefix, sys.prefix, os.path.join(sys.prefix, "Scripts"),
        os.path.join(sys.base_prefix, "Scripts"))}
    limpias, quitadas = [], []
    for carpeta in os.environ.get("PATH", "").split(os.pathsep):
        if not carpeta.strip():
            continue
        norm = os.path.normcase(os.path.abspath(carpeta))
        if norm.startswith(sistema) or norm.rstrip("\\/") in propias:
            limpias.append(carpeta)
            continue
        try:
            nombres = [n.lower() for n in os.listdir(carpeta)]
        except OSError:
            limpias.append(carpeta)
            continue
        choca = any(n.endswith(".dll") and (n.startswith(PREFIJOS_CUDA) or n in DLL_RUNTIME_VC)
                    for n in nombres)
        (quitadas if choca else limpias).append(carpeta)
    for q in quitadas:
        print(f"  [PATH] Se ignora durante la compilación (trae DLLs de CUDA/VC++): {q}")
    return os.pathsep.join(limpias)


def _mb(n):
    return f"{n / (1024 ** 2):,.0f} MB"


def _carpeta_dlls_torch():
    """torch\\lib del entorno (solo se ubica, NO se importa torch)."""
    try:
        spec = importlib.util.find_spec("torch")
        if spec is not None and spec.origin:
            carpeta = os.path.join(os.path.dirname(spec.origin), "lib")
            if os.path.isdir(carpeta):
                return carpeta
    except Exception:
        pass
    return None


def copiar_dlls_cuda(destino, base):
    """Copia las DLL de NVIDIA que usa la app (desde torch\\lib) a 'destino'."""
    origen = _carpeta_dlls_torch()
    if not origen:
        print("  [CUDA] torch no está instalado en este entorno: el build quedará SIN GPU.")
        return
    todas = [n for n in os.listdir(origen) if n.lower().endswith(".dll")]
    lista = os.path.join(base, "cuda_necesarias.txt")
    if os.path.isfile(lista):
        with open(lista, encoding="utf-8") as fh:
            pedidas = {l.strip().lower() for l in fh if l.strip() and not l.startswith("#")}
        elegidas = [n for n in todas if n.lower() in pedidas]
        modo = "solo las verificadas en cuda_necesarias.txt"
    else:
        elegidas = [n for n in todas
                    if not n.lower().startswith(CUDA_NO_COPIAR_PREFIJOS)
                    and n.lower() not in CUDA_NO_COPIAR_EXACTOS]
        modo = "todas las de NVIDIA (sin las propias de PyTorch)"
    if not any(n.lower() == "cudart64_12.dll" for n in elegidas):
        print("  [CUDA] ¡Falta cudart64_12.dll! Revisa cuda_necesarias.txt; el build quedará SIN GPU.")
    if os.path.isdir(destino):
        shutil.rmtree(destino)
    os.makedirs(destino)
    copiado = omitido = 0
    for n in todas:
        tam = os.path.getsize(os.path.join(origen, n))
        if n in elegidas:
            shutil.copy2(os.path.join(origen, n), os.path.join(destino, n))
            copiado += tam
        else:
            omitido += tam
    print(f"\n=== DLLs de CUDA ({modo}) ===")
    print(f"  Copiadas: {len(elegidas)} DLLs, {_mb(copiado)}  ->  {destino}")
    print(f"  No incluidas (PyTorch y extras): {_mb(omitido)}")


def revisar_dlls(dist):
    """Revisión posterior de las DLLs empaquetadas (solo Windows)."""
    if os.name != "nt" or not os.path.isdir(dist):
        return
    print("\n=== Revisión de DLLs empaquetadas ===")
    interno = os.path.join(dist, "_internal")
    system32 = os.path.join(os.environ.get("SystemRoot", r"C:\Windows"), "System32")

    # 1) Runtime de Visual C++: nunca más viejo que el de Windows
    for raiz, _, archivos in os.walk(dist):
        for nombre in archivos:
            if nombre.lower() not in DLL_RUNTIME_VC:
                continue
            ruta = os.path.join(raiz, nombre)
            del_sistema = os.path.join(system32, nombre)
            v_emp, v_sis = _version_dll(ruta), _version_dll(del_sistema)
            rel = os.path.relpath(ruta, dist)
            if v_emp and v_sis and v_emp < v_sis:
                shutil.copy2(del_sistema, ruta)
                print(f"  [VC++] {rel}: {_txt_version(v_emp)} -> reemplazada por la de Windows {_txt_version(v_sis)}")
            else:
                print(f"  [VC++] {rel}: {_txt_version(v_emp)} (Windows: {_txt_version(v_sis)}) OK")

    # 2) Restos de PyTorch (no se empaqueta; solo sus DLL de NVIDIA en _internal\cuda)
    restos_torch = os.path.join(interno, "torch")
    if os.path.isdir(restos_torch):
        tam = sum(os.path.getsize(os.path.join(r, f)) for r, _, fs in os.walk(restos_torch) for f in fs)
        shutil.rmtree(restos_torch, ignore_errors=True)
        print(f"  [CUDA] _internal\\torch (restos, {_mb(tam)}) -> eliminado")

    # 3) CUDA / cuDNN fuera de la carpeta cuda
    torch_lib = os.path.join(interno, "cuda")
    en_torch = {n.lower() for n in os.listdir(torch_lib)} if os.path.isdir(torch_lib) else set()
    for raiz, _, archivos in os.walk(interno):
        if os.path.normcase(raiz) == os.path.normcase(torch_lib):
            continue
        for nombre in archivos:
            baja = nombre.lower()
            if not (baja.endswith(".dll") and baja.startswith(PREFIJOS_CUDA)):
                continue
            ruta = os.path.join(raiz, nombre)
            rel = os.path.relpath(ruta, dist)
            if os.path.normcase(raiz) == os.path.normcase(interno) and baja in en_torch:
                os.remove(ruta)
                print(f"  [CUDA] {rel}: duplicado de _internal\\cuda -> eliminado")
            else:
                print(f"  [CUDA] Aviso: {rel} ({_txt_version(_version_dll(ruta))}) fuera de _internal\\cuda")

    # 4) Otras copias que conviene conocer
    for nombre_buscado in ("onnxruntime.dll", "libiomp5md.dll"):
        copias = [os.path.relpath(os.path.join(r, n), dist)
                  for r, _, fs in os.walk(interno) for n in fs if n.lower() == nombre_buscado]
        if len(copias) > 1:
            print(f"  [Info] {nombre_buscado} aparece {len(copias)} veces: " + ", ".join(copias))
    print("=== Fin de la revisión ===\n")


# ----------------------------------------------------------------------------
def main():
    base = os.path.dirname(os.path.abspath(__file__))
    os.chdir(base)
    for requerido in (APP, os.path.join("imgtype", "1.ico")):
        if not os.path.exists(requerido):
            sys.exit(f"Falta '{requerido}' en {base}")
    # version_info.txt es OPCIONAL: son los metadatos de versión del .exe
    # (nombre del producto, copyright...). Si no está, se compila sin ellos.
    hay_version = os.path.exists("version_info.txt")
    if not hay_version:
        print("  [AVISO] Sin 'version_info.txt': el .exe se compilará sin metadatos de versión.")

    colectar_todo = _filtrar(COLECTAR_TODO, _paquete_instalado, "paquete")
    colectar_datos = _filtrar(COLECTAR_DATOS, _paquete_instalado, "paquete")
    meta_rec = _filtrar(METADATOS_RECURSIVOS, _distribucion_instalada, "distribución")
    meta = _filtrar(METADATOS, _distribucion_instalada, "distribución")
    ocultos = _filtrar(IMPORTS_OCULTOS, _paquete_instalado, "módulo")

    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--noconfirm", "--clean", "--onedir",
        "--console" if CONSOLA else "--windowed",
        "--name", NOMBRE,
        "--icon", os.path.join("imgtype", "1.ico"),
        "--add-data", f"imgtype{os.pathsep}imgtype",
    ]
    if hay_version:
        cmd += ["--version-file", "version_info.txt"]
    for m in EXCLUIR:
        cmd += ["--exclude-module", m]
    for p in colectar_todo:
        cmd += ["--collect-all", p]
    for p in colectar_datos:
        cmd += ["--collect-data", p]
    for d in meta_rec:
        cmd += ["--recursive-copy-metadata", d]
    for d in meta:
        cmd += ["--copy-metadata", d]
    for h in ocultos:
        cmd += ["--hidden-import", h]
    cmd.append(APP)

    print(" ".join(f'"{c}"' if " " in c else c for c in cmd))
    if CONSOLA:
        print("  [modo] Compilación CON consola (diagnóstico)")

    entorno = os.environ.copy()
    entorno["PATH"] = _path_de_compilacion()
    codigo = subprocess.call(cmd, env=entorno)
    if codigo != 0:
        sys.exit(codigo)

    dist = os.path.join(base, "dist", NOMBRE)
    copiar_dlls_cuda(os.path.join(dist, "_internal", "cuda"), base)
    revisar_dlls(dist)
    total = sum(os.path.getsize(os.path.join(r, f)) for r, _, fs in os.walk(dist) for f in fs)
    print(f"Tamaño total de la carpeta: {total / (1024 ** 3):.2f} GB")
    print("Listo: dist\\" + NOMBRE + "\\" + NOMBRE + ".exe")
    print("Recuerda copiar la carpeta 'tools' junto al .exe.")


if __name__ == "__main__":
    main()
