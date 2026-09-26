<p align="center">
  <img src="imgtype/logo.png" alt="DEUS MACHINA | TOOLS" width="420">
</p>

<h1 align="center">DEUS MACHINA | TOOLS v3.0</h1>

<p align="center">
  Aplicación de escritorio (Windows) para procesar medios en local: video, audio, imágenes,
  PDF, OCR, transcripción con IA, descargas y metadatos.<br>
  <b>Software libre bajo licencia GNU AGPL-3.0</b>
</p>

---

## Descarga / Download

**Código fuente / Source code:** este repositorio

**Instalador / Installer (~1.7 GB):**

- **[GitHub Releases](https://github.com/DoMiNaTh0R/DEUS-MACHINA-TOOLS/releases/latest)**
- **[Google Drive](https://drive.google.com/drive/folders/1Vr5GbW31KSOUGScupc5S8DhU_w5zGrFb)** (espejo / mirror)

> Es el mismo instalador en los dos sitios.
> It is the same installer in both places.

---

## Qué hace

| Módulo | Para qué sirve |
|---|---|
| **Video** | Convertir y comprimir con detección real de NVENC/NVDEC (H.264, H.265, AV1, 10 bits), niveles de calidad por códec, extracción de audio, varias pistas de audio y subtítulos (eliges cuáles conservar) |
| **Audio** | Conversión entre MP3, M4A, OPUS, WAV, FLAC… con perfiles de calidad |
| **Imágenes** | Convertir, comprimir y quitar fondo (rembg/u2net). SVG, HEIC, PSD e ICO multiescala |
| **PDF** | Comprimir (Ghostscript), unir, dividir, PDF ⇄ imágenes con control de DPI |
| **OCR** | Extraer texto con PaddleOCR (GPU/CPU) o RapidOCR; decide página por página si el texto se extrae directo o se lee con IA |
| **Transcripción** | faster-whisper: archivos, YouTube / Spotify → texto y en vivo, con selector de idioma y modo multilingüe; subtítulos de videos y letras de canciones (solas o con tiempos) sin IA |
| **Descargas** | YouTube y Spotify (yt-dlp / spotDL), cola de 3 a la vez para YouTube (Spotify va aparte), metadatos, carátulas, códec preferido, pista de audio (doblajes), subtítulos dentro del video y letras de YouTube Music |
| **Renombrador** | Renombrado masivo con vista previa y deshacer del último lote |
| **Metadata Lab** | Leer, editar, limpiar y verificar metadatos de imágenes, audio, video, PDF y Office |

Varios módulos pueden trabajar **a la vez**; los que cargan modelos de IA se turnan solos para no saturar la memoria, y un botón (en el menú, Transcripción, OCR y Quitar fondo) libera el modelo cargado cuando termina lo que está en curso.

Detalle completo de cambios: **[CHANGELOG](imgtype/CHANGELOG.md)** · Documentación de usuario: **[README de la app](imgtype/README.md)**

---

## Requisitos

- Windows 10/11 de 64 bits
- Python **3.13** (solo para compilar desde el código fuente)
- GPU NVIDIA opcional: acelera transcripción y OCR (para OCR en GPU se necesita **Turing / RTX 20xx o posterior** y driver compatible con CUDA 12.9)
- FFmpeg y Ghostscript (se descargan aparte, ver abajo)

---

## Compilar desde el código fuente

Guía paso a paso: **[docs/COMPILAR.md](docs/COMPILAR.md)**

Resumen rápido:

```bat
:: 1) Crear el entorno con todas las dependencias (Python 3.13)
crear_venv_dmt.bat

:: 2) Descargar FFmpeg y Ghostscript y dejarlos en:
::    tools\ffmpeg\bin\ffmpeg.exe   y   tools\ghostscript\bin\gswin64c.exe

:: 3) Ejecutar desde el código fuente
build_env_DMT\Scripts\python.exe Deus_machina_tools.py

:: 4) O compilar el ejecutable
build_env_DMT\Scripts\python.exe build_pyinstaller.py
```

---

## Qué hay en este repositorio

| Archivo / carpeta | Para qué es |
|---|---|
| `Deus_machina_tools.py` | Todo el programa (interfaz + módulos + motores) |
| `crear_venv_dmt.bat` | Crea el entorno virtual `build_env_DMT` con el stack CUDA 12.9 |
| `requirements.txt` · `constraints.txt` | Dependencias exactas y versiones fijadas |
| `cuda_necesarias.txt` | Lista de DLL de NVIDIA que la app necesita y que se empaquetan |
| `build_pyinstaller.py` | Compila el ejecutable con PyInstaller |
| `imgtype/` | Recursos de la app (icono, logo, fuentes) y documentación que la app muestra: README, CHANGELOG, LICENSE, LICENSE-EXCEPTION, EULA y THIRD_PARTY_NOTICES |
| `docs/COMPILAR.md` | Guía de compilación |
| `LICENSE` | Texto completo de la GNU AGPL-3.0 |
| `LICENSE-EXCEPTION.txt` | Permiso adicional (sección 7) para combinar el programa con CUDA/cuDNN |

No se incluyen en el repositorio (se obtienen aparte): el entorno `build_env_DMT`, la carpeta `tools` (FFmpeg, Ghostscript, modelos de OCR) ni los modelos de IA, que se descargan solos la primera vez que se usan.

---

## Licencia

DEUS MACHINA | TOOLS es **software libre** bajo la **GNU Affero General Public License v3 (AGPL-3.0) o posterior**. Ver [LICENSE](LICENSE), el permiso adicional en [LICENSE-EXCEPTION.txt](LICENSE-EXCEPTION.txt) y el resumen en [imgtype/EULA.txt](imgtype/EULA.txt).

La aplicación enlaza **PyMuPDF (fitz)**, publicado bajo AGPL-3.0, dentro de su propio proceso: por eso todo el programa se publica bajo la misma licencia. **FFmpeg** (GPL v3) y **Ghostscript** (AGPL v3) se usan como programas externos independientes (mera agregación).

Los textos completos de todas las licencias de terceros están en [imgtype/THIRD_PARTY_NOTICES.txt](imgtype/THIRD_PARTY_NOTICES.txt).

### Componentes de NVIDIA

Versiones exactas que se distribuyen con la aplicación:

| Componente | Versión | Archivos |
|---|---|---|
| CUDA | 12.9.79 | `cublas64_12.dll`, `cublasLt64_12.dll`, `cudart64_12.dll` |
| cuDNN | 9.10.2.21 | `cudnn64_9.dll`, `cudnn_adv64_9.dll`, `cudnn_cnn64_9.dll`, `cudnn_engines_precompiled64_9.dll`, `cudnn_engines_runtime_compiled64_9.dll`, `cudnn_graph64_9.dll`, `cudnn_heuristic64_9.dll`, `cudnn_ops64_9.dll` |

> "La distribución de estas bibliotecas se realiza exclusivamente en calidad de componentes redistribuibles autorizados por los términos de licencia de NVIDIA aplicables a la versión correspondiente de CUDA/cuDNN. Dichos componentes permanecen sujetos a sus respectivas licencias de NVIDIA y no forman parte de la licencia AGPLv3 aplicable al código original de DEUS MACHINA | TOOLS."

> "These libraries are distributed solely as redistributable components authorized by the NVIDIA license terms applicable to the corresponding CUDA/cuDNN version. Such components remain subject to their respective NVIDIA licenses and are not part of the AGPLv3 license applicable to the original DEUS MACHINA | TOOLS code."

El archivo [LICENSE-EXCEPTION.txt](LICENSE-EXCEPTION.txt) recoge el **permiso adicional conforme a la sección 7 de la AGPL v3**: autoriza enlazar, combinar y distribuir el programa junto a esas bibliotecas y, a la vez, reconoce expresamente que **NVIDIA Corporation conserva el control y la titularidad de la licencia de CUDA y cuDNN**.

---

## In English

**DEUS MACHINA | TOOLS v3.0** is a Windows desktop app for local media processing: video and audio conversion, image tools (including background removal), PDF utilities, OCR (PaddleOCR / RapidOCR), AI transcription (faster-whisper), YouTube/Spotify downloading, batch renaming and a metadata lab. Everything runs locally; no telemetry.

- **Source code:** this repository
- **Installer (~1.7 GB):** [GitHub Releases](https://github.com/DoMiNaTh0R/DEUS-MACHINA-TOOLS/releases/latest) or [Google Drive](https://drive.google.com/drive/folders/1Vr5GbW31KSOUGScupc5S8DhU_w5zGrFb) *(mirror, same file)*
- **Build from source:** see [docs/COMPILAR.md](docs/COMPILAR.md)
- **License:** GNU AGPL-3.0 or later — the app links PyMuPDF (AGPL-3.0) in-process, so the whole work is AGPL. An [additional permission under section 7](LICENSE-EXCEPTION.txt) covers combining the program with NVIDIA's CUDA/cuDNN runtimes, which remain under NVIDIA's own licenses. Full third-party license texts in [imgtype/THIRD_PARTY_NOTICES.txt](imgtype/THIRD_PARTY_NOTICES.txt).

---

## Autor

**Kevin González (DoMiNaTh0R)** — DoMiNaTh0RRoyale@gmail.com

© 2026 Kevin González. Publicado bajo GNU AGPL-3.0.
