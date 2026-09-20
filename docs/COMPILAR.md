# Compilar DEUS MACHINA | TOOLS desde el código fuente

Qué instalar, dónde va cada cosa y cómo generar el ejecutable.
Todo está pensado para **Windows 10/11 de 64 bits**.

---

## 1. Lo que necesitas antes de empezar

| Requisito | Detalle |
|---|---|
| **Python 3.13** (64 bits) | Instalado con el lanzador `py`. Comprueba con `py -3.13 --version` |
| **Espacio en disco** | ~12 GB para el entorno + ~7 GB para la compilación |
| **GPU NVIDIA** (opcional) | Driver compatible con CUDA 12.9. Para OCR en GPU: Turing (RTX 20xx) o posterior |
| **FFmpeg** | Build "full" de Windows (ver paso 3) |
| **Ghostscript** | Versión de consola para Windows 64 bits (ver paso 3) |

No hace falta instalar el CUDA Toolkit: las DLL necesarias vienen dentro del paquete de PyTorch que instala el script del entorno, y el compilador copia solo las que la app usa (las listadas en `cuda_necesarias.txt`).

---

## 2. Crear el entorno virtual

Con el repositorio descargado, desde su carpeta:

```bat
crear_venv_dmt.bat
```

El script:

1. crea el entorno `build_env_DMT` **junto al propio .bat**;
2. instala todo lo de `requirements.txt` respetando `constraints.txt`;
3. instala el stack de GPU (PaddlePaddle GPU + PyTorch, este último solo por sus DLL de CUDA);
4. deja un registro de pip en `instalacion_venv_dmt.log`.

Si ya existe el entorno, pregunta si lo reutiliza y repara lo que falte.

---

## 3. Descargar FFmpeg y Ghostscript

Estos dos programas **no se incluyen en el repositorio** (son proyectos externos con sus
propias licencias GPL/AGPL). Descárgalos y colócalos con estos nombres exactos:

### FFmpeg

- Descarga: <https://www.gyan.dev/ffmpeg/builds/> (paquete *full*, versión 7.x o superior)
- Copia el contenido de su carpeta `bin` de forma que quede:

```
tools\ffmpeg\bin\ffmpeg.exe
tools\ffmpeg\bin\ffprobe.exe
tools\ffmpeg\LICENSE          <- el archivo de licencia del propio FFmpeg
```

### Ghostscript

- Descarga: <https://ghostscript.com/releases/gsdnld.html> (Windows 64 bits, AGPL)
- Instálalo (o extrae el instalador) y copia lo necesario de forma que quede:

```
tools\ghostscript\bin\gswin64c.exe
tools\ghostscript\bin\*.dll
tools\ghostscript\lib\...      <- carpeta 'lib' completa del programa
tools\ghostscript\COPYING      <- el archivo de licencia de Ghostscript
```

> Si prefieres usar el FFmpeg o el Ghostscript que ya tengas instalados en el PATH del
> sistema, la app también los encuentra; la carpeta `tools` solo sirve para llevarlos
> junto al ejecutable.

### Modelos de OCR (opcional)

La primera vez que uses el OCR, PaddleX descarga los modelos PP-OCRv6 (~133 MB) a
`tools\paddleocr\official_models`. Si quieres que el ejecutable ya los lleve, ejecuta el
OCR una vez antes de compilar: quedarán en esa carpeta y el compilador los incluirá.

---

## 4. Ejecutar desde el código fuente

```bat
build_env_DMT\Scripts\python.exe Deus_machina_tools.py
```

Estructura mínima para que funcione así:

```
<carpeta del proyecto>\
├── Deus_machina_tools.py
├── imgtype\            (icono, logo, fuentes y documentación)
├── tools\              (ffmpeg, ghostscript y, con el uso, paddleocr)
└── build_env_DMT\      (entorno virtual)
```

---

## 5. Compilar el ejecutable

```bat
build_env_DMT\Scripts\python.exe build_pyinstaller.py
```

El script se encarga de:

- empaquetar la app **sin PyTorch** (solo copia las DLL de NVIDIA que la app usa, según `cuda_necesarias.txt`);
- incluir PaddlePaddle, PaddleX, PaddleOCR, RapidOCR, rembg, faster-whisper, spotDL y yt-dlp;
- copiar `imgtype` y `tools` junto al ejecutable;
- limpiar restos (`_internal\torch`, duplicados de CUDA) al final.

> Los metadatos de versión del .exe (nombre del producto, copyright…) se toman de un
> archivo `version_info.txt` opcional junto al script. Si no existe, el ejecutable se
> compila igual, solo que sin esos metadatos.

**Al distribuir el resultado** hay que incluir `LICENSE` (AGPL-3.0),
`LICENSE-EXCEPTION.txt`, `THIRD_PARTY_NOTICES.txt` y las licencias de FFmpeg y
Ghostscript que vienen dentro de `tools`, y ofrecer el código fuente correspondiente
(este repositorio cumple esa función).
