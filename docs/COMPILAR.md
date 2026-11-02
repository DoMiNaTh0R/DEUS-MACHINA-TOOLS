# Compilar DEUS MACHINA | TOOLS desde el código fuente

Qué instalar, dónde va cada cosa y cómo generar el ejecutable.
Todo está pensado para **Windows 10/11 de 64 bits**.

---

## 1. Lo que necesitas antes de empezar

| Requisito | Detalle |
|---|---|
| **Python 3.13** (64 bits) | 3.13.17 o posterior, instalado con el lanzador `py`. Comprueba con `py -3.13 --version`. Python 3.14 todavía no sirve: PaddlePaddle no publica versión para 3.14 en Windows |
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
2. instala el stack de GPU (PaddlePaddle GPU + PyTorch, este último solo por sus DLL de CUDA);
3. instala todo lo de `requirements.txt` con las **versiones exactas** que ahí aparecen, respetando `constraints.txt`;
4. deja un registro de pip en `instalacion_venv_dmt.log`.

Si ya existe el entorno, pregunta si lo reutiliza y repara lo que falte. Si está roto (por ejemplo, porque se desinstaló el Python con el que se creó) o es de otra versión de Python, ofrece borrarlo y crearlo de nuevo. Con `crear_venv_dmt.bat /auto` no pregunta nada.

---

## 3. Descargar FFmpeg y Ghostscript

Estos dos programas **no se incluyen en el repositorio** (son proyectos externos con sus
propias licencias GPL/AGPL). Descárgalos y colócalos con estos nombres exactos:

### FFmpeg

- Descarga: <https://www.gyan.dev/ffmpeg/builds/> (paquete *full*; la v3.1 se distribuye con la 9.0.2)
- Copia el contenido de su carpeta `bin` de forma que quede:

```
tools\ffmpeg\bin\ffmpeg.exe
tools\ffmpeg\bin\ffprobe.exe
tools\ffmpeg\LICENSE          <- el archivo de licencia del propio FFmpeg
```

### Ghostscript

- Descarga: <https://github.com/ArtifexSoftware/ghostpdl-downloads/releases> (instalador `gsXXXXXw64.exe`, Windows 64 bits, AGPL; la v3.1 se distribuye con la 10.08.0, que corrige CVE-2026-39919)
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

La forma más sencilla es el compilador todo en uno:

```bat
compilar_dmt.bat
```

Hace, en orden:

1. crea el entorno con `crear_venv_dmt.bat` si no existe o está roto;
2. regenera `imgtype\THIRD_PARTY_NOTICES.txt` si tienes `generar_licencias.py` (herramienta del autor, no viene en el repositorio); si no, usa el que ya trae `imgtype`;
3. compila con `build_pyinstaller.py`;
4. arma `Instalador\DEUS_MACHINA_TOOLS\` con el ejecutable, la carpeta `tools` y los documentos (`CHANGELOG.md`, `EULA.txt`, `LICENSE.txt`, `LICENSE-EXCEPTION.txt`, `README.md`, `THIRD_PARTY_NOTICES.txt`);
5. copia `README.txt` y `EULA.txt` a `Instalador\` (los muestra el asistente de instalación).

No firma nada ni ejecuta Inno Setup (ver el paso 6).

También se puede compilar solo el ejecutable:

```bat
build_env_DMT\Scripts\python.exe build_pyinstaller.py
```

El script se encarga de:

- empaquetar la app **sin PyTorch** (solo copia las DLL de NVIDIA que la app usa, según `cuda_necesarias.txt`);
- incluir PaddlePaddle, PaddleX, PaddleOCR, RapidOCR, rembg, faster-whisper, spotDL y yt-dlp;
- copiar `imgtype` y `tools` junto al ejecutable;
- limpiar restos (`_internal\torch`, duplicados de CUDA) al final.

> **La versión se escribe en un solo lugar:** la línea `version = "…"` de
> `Deus_machina_tools.py`. Con ella el script genera `version_info.txt` (metadatos del
> .exe: versión, nombre del producto, copyright…) y avisa si `README` o `CHANGELOG` no
> la mencionan. `build_pyinstaller.py --version` solo la imprime.

**Al distribuir el resultado** hay que incluir `LICENSE` (AGPL-3.0),
`LICENSE-EXCEPTION.txt`, `THIRD_PARTY_NOTICES.txt` y las licencias de FFmpeg y
Ghostscript que vienen dentro de `tools`, y ofrecer el código fuente correspondiente
(este repositorio cumple esa función).

---

## 6. Instalador (Inno Setup) y firma

El instalador oficial se arma con **Inno Setup 7** y el script `Instalador\innoF.iss`
(no forma parte de este repositorio). Después de `compilar_dmt.bat`:

1. firmar `Instalador\DEUS_MACHINA_TOOLS\DEUS_MACHINA_TOOLS.exe`;
2. compilar `innoF.iss`: toma la versión del `.exe`, así que no hay que tocar el script;
3. firmar el `Instalador\Output\DeusMachinaTools_Setup_vX.Y.exe` resultante.

El instalador acepta `/SILENT` y `/VERYSILENT`; con `/RELANZAR=1` vuelve a abrir la app
al terminar (lo usa el actualizador de la propia app).

> **El buscador de actualizaciones de la app solo instala instaladores firmados con el
> mismo certificado que el programa** (además de comprobar la huella SHA-256 que publica
> GitHub). Un instalador sin firmar, o firmado con otro certificado, se rechaza. Si
> compilas tu propia versión, cambia `_DMT_REPO_GITHUB` y `_DMT_FIRMAS_CONFIABLES` en
> `Deus_machina_tools.py` para que apunten a tu repositorio y a tu certificado.
