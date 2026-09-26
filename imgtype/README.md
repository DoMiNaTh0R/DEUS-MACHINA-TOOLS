# DEUS MACHINA | TOOLS — Versión 3.0

---

## Descripción

DEUS MACHINA | TOOLS es una aplicación de escritorio para el procesamiento local de medios y tareas automatizadas. Incluye herramientas para conversión de video y audio, transcripción con IA, extracción de texto con OCR, descarga de contenido de YouTube y Spotify, edición de PDF, conversión de imágenes, eliminación de fondos, renombrado en lote y edición y limpieza de metadatos.

La aplicación funciona completamente de forma local. No recopila datos personales ni telemetría de ningún tipo.

Para conocer los cambios incluidos en esta versión, consulta el archivo `CHANGELOG.md`.

---

## Descarga

El instalador (~1.7 GB) está en dos lugares; es el mismo archivo en ambos:

- **[Descargar desde GitHub Releases](https://github.com/DoMiNaTh0R/DEUS-MACHINA-TOOLS/releases/latest)**
- **[Descargar desde Google Drive](https://drive.google.com/drive/folders/1Vr5GbW31KSOUGScupc5S8DhU_w5zGrFb)** (espejo)

**Código fuente:** https://github.com/DoMiNaTh0R/DEUS-MACHINA-TOOLS

---

## Novedades principales de la versión 3.0

- **Varios módulos a la vez:** puedes convertir un video mientras comprimes imágenes y descargas de YouTube. Los módulos que cargan modelos de IA (OCR, Transcripción y Quitar fondo) se turnan automáticamente para no saturar la memoria.
- **OCR nuevo:** PaddleOCR (GPU/CPU) y RapidOCR en lugar de EasyOCR, con el motor en un proceso aparte, decisión página por página en PDF mixtos y lectura a 200 DPI.
- **Metadata Lab:** lectura, edición, limpieza y verificación de metadatos en imágenes, audio, video, PDF y documentos de Office, sin recomprimir el archivo.
- **Video:** detección real de lo que soporta tu GPU (NVENC H.264/H.265/AV1, 10 bits, NVDEC, ruta completa en GPU) niveles de calidad calibrados por códec y soporte de archivos con varias pistas de audio y subtítulos (eliges cuáles conservar).
- **Descargas:** soporte de Spotify (vía spotDL, sin esperar en la cola), cola de 3 descargas simultáneas para YouTube y demás sitios, ⚙️ configuración (códec preferido, pista de audio de videos doblados, subtítulos dentro del video y letra de canciones de YouTube Music) y actualizador de yt-dlp con verificación SHA-256.
- **Transcripción:** selector de idioma (incluido modo multilingüe), traducción al inglés, modo en vivo que ya no pierde audio, enlaces de Spotify en YouTube → Texto y una pestaña nueva para bajar **subtítulos** de videos y **letras de canciones** (solas o con tiempos) sin usar IA.
- **Botón "🧹 Liberar modelo IA"** en el menú, Transcripción, OCR y Quitar fondo: saca de la memoria el modelo de IA cargado.
- **Renombrador:** deshacer el último renombrado completo, incluso después de cerrar la app.
- **Arranque más rápido y ejecutable más ligero:** la app ya no carga PyTorch; usa solo las librerías de NVIDIA necesarias.

---

## Requisitos del sistema

| Componente        | Mínimo                                   | Recomendado                                          |
| ----------------- | ---------------------------------------- | ---------------------------------------------------- |
| Sistema operativo | Windows 10 64-bit                        | Windows 11 64-bit                                    |
| Procesador        | Intel i3 (8ª Gen) / Ryzen 3 (Serie 3000) | Intel i5 (10ª Gen) / Ryzen 5 (Serie 5000) o superior |
| RAM               | 8 GB                                     | 16 GB                                                |
| Espacio en disco  | 12 GB                                    | 20 GB                                                |
| GPU               | Cualquier GPU NVIDIA                     | NVIDIA con 6 GB VRAM o más                           |
| Drivers NVIDIA    | Actualizados a la versión más reciente   | —                                                    |

> Windows 7 / Vista / 8 / 8.1 no han sido probados y no se garantiza compatibilidad.

La aplicación funciona sin GPU: en ese caso usa la CPU, con las limitaciones indicadas más abajo.

---

## Aceleración por GPU y modelos de IA

La app detecta automáticamente GPUs NVIDIA compatibles y usa aceleración por hardware cuando está disponible. No es necesario instalar el CUDA Toolkit por separado, siempre que los drivers oficiales de NVIDIA estén actualizados.

Si no hay GPU compatible, la aplicación opera automáticamente en modo CPU, con algunas limitaciones en los modelos de transcripción más pesados.

### Referencia de modelos de transcripción en vivo (faster-whisper)

| Modelo | CPU | GPU mínima | Notas |
|---|---|---|---|
| 🟢 TINY | ✅ Funciona bien | GTX 1650 / 2–4 GB VRAM | Para PCs básicas |
| 🟡 SMALL | ✅ Funciona | GTX 1650 / 2–4 GB VRAM | Recomendado para la mayoría |
| 🟠 MEDIUM | ⚠️ Muy lento | RTX 2060 / 3060 — 6 GB VRAM | Solo con GPU decente |
| 🔴 LARGE | ❌ Extremadamente lento | RTX 3080 / 4060+ — 8 GB VRAM | Solo gama alta |

### Motores de OCR

| Motor | Requisitos | Notas |
|---|---|---|
| 🚀 PaddleOCR · GPU | NVIDIA **Turing (RTX 20xx) o posterior** con driver compatible con CUDA 12.9 | Máxima precisión y el más rápido |
| 🎯 PaddleOCR · CPU | Cualquier equipo | Misma precisión, bastante más lento |
| ⚡ RapidOCR · CPU | Cualquier equipo | Rápido y ligero, precisión algo menor |

La app comprueba tu tarjeta antes de ofrecer el modo GPU; si no es compatible o falla, cambia sola a CPU o a RapidOCR y lo indica en pantalla.

Para la codificación de video en formato **AV1** se requiere una GPU con soporte de codificación AV1 por hardware (NVIDIA RTX 40xx o superior); en equipos sin ese soporte se usa el codificador por CPU (SVT-AV1).

---

## Descarga de modelos y componentes

Los siguientes componentes **no están incluidos** en el instalador y se descargan automáticamente la primera vez que hacen falta:

| Componente | Cuándo se descarga | Tamaño aprox. | Dónde queda |
|---|---|---|---|
| Modelos faster-whisper | Al usar transcripción con ese modelo | 150 MB – 3 GB según el modelo | Caché de Hugging Face (`~/.cache/huggingface/hub/`) |
| Modelo u2net (quitar fondo) | Al usar "Remover Fondo" por primera vez | ~170 MB | `%LOCALAPPDATA%\DeusMachinaTools\rembg_models\` |
| Deno (runtime de JavaScript) | Antes de una descarga que lo necesite | ~40 MB | `%LOCALAPPDATA%\DeusMachinaTools\tools\deno\` |
| spotDL | Al pegar el primer enlace de Spotify | ~50 MB | Entorno de la aplicación |

Los modelos de OCR (PP-OCRv6 de PaddleOCR y los de RapidOCR) **sí vienen incluidos** con la aplicación, en `tools\paddleocr`.

Las ejecuciones posteriores no requieren descarga.

---

## Conexión a internet

La app no requiere conexión permanente a internet. Las únicas situaciones en las que se realiza una conexión son:

- Descarga de un modelo o componente por primera vez (ver la tabla anterior).
- Descarga de contenido desde YouTube, Spotify u otras plataformas compatibles (incluidos subtítulos).
- Búsqueda de letras de canciones (LRCLIB, YouTube Music y otros proveedores), solo cuando usas esa opción.
- Actualización de yt-dlp desde el botón integrado en la app (con verificación de firma SHA-256).

---

## Privacidad

- No se recopilan datos personales del usuario.
- No se envía información a servidores externos propios del software.
- No se utiliza telemetría ni sistemas de seguimiento.
- Todo el procesamiento de archivos se realiza localmente en el equipo del usuario.

---

## Licencia

DEUS MACHINA | TOOLS es **software libre** y se distribuye bajo la **GNU Affero General Public License v3 (AGPL-3.0) o posterior**. El texto completo está en el archivo `LICENSE` (también incluido con la aplicación como `LICENSE.txt`), el permiso adicional de la sección 7 para las bibliotecas de NVIDIA está en `LICENSE-EXCEPTION.txt`, y el resumen en lenguaje claro de tus derechos y obligaciones está en `EULA.txt`.

Puedes usar el programa para cualquier fin (incluido el comercial), estudiarlo, modificarlo y redistribuirlo. Si distribuyes el programa o una versión modificada —o si ofreces su funcionalidad a través de una red— debes entregar el código fuente correspondiente bajo esta misma licencia.

**Código fuente:** https://github.com/DoMiNaTh0R/DEUS-MACHINA-TOOLS
También se envía por correo a quien lo solicite: DoMiNaTh0RRoyale@gmail.com

### Por qué AGPL

La aplicación enlaza directamente **PyMuPDF (fitz)**, publicado bajo AGPL-3.0. Al ser una librería enlazada dentro del mismo proceso (y no un programa externo), el conjunto se publica bajo la misma licencia.

### Nombre y logotipo

Conforme a la sección 7(e) de la AGPL, el nombre "DEUS MACHINA | TOOLS", su logotipo y sus imágenes propias no se pueden usar para promocionar versiones modificadas ni dar a entender el respaldo del autor: publica tus versiones con un nombre propio. Esto no limita ningún derecho de la AGPL sobre el código.

---

## Componentes de terceros

### Programas externos (mera agregación)

Se distribuyen junto al software como programas independientes y se invocan como procesos externos. Cada uno se rige por su propia licencia y no forma una obra derivada del ejecutable principal.

**FFmpeg — GPL v3**
Utilizado para conversión y procesamiento de video y audio. Se ejecuta como proceso externo independiente (CLI), sin vinculación estática ni dinámica con el ejecutable principal.
Código fuente: https://ffmpeg.org/download.html

**Ghostscript — AGPL v3**
Utilizado para el procesamiento de archivos PDF. Se invoca exclusivamente mediante llamadas al ejecutable `gswin64c.exe`, sin vinculación directa con el código principal.
Código fuente: https://ghostscript.com/

### Componentes enlazados

**PyMuPDF (fitz) — AGPL v3**
Motor PDF para extracción de texto, renderizado de páginas y manipulación de archivos PDF. Se enlaza **directamente** como librería Python dentro del proceso principal: no es mera agregación, y por eso toda la aplicación se publica bajo AGPL-3.0.
Documentación y licencia: https://pymupdf.readthedocs.io/

### Otros componentes

**PaddleOCR / PaddlePaddle / PaddleX — Apache 2.0**
Motor de OCR principal (modelos PP-OCRv6) y su framework. Se ejecuta en un proceso independiente de la aplicación.
Proyecto: https://github.com/PaddlePaddle/PaddleOCR

**RapidOCR + ONNX Runtime — Apache 2.0 / MIT**
Motor de OCR ligero para CPU.
Proyecto: https://github.com/RapidAI/RapidOCR

**faster-whisper / CTranslate2 — MIT**
Motor de transcripción (implementación optimizada de Whisper, de OpenAI, también MIT).
Proyecto: https://github.com/SYSTRAN/faster-whisper

**rembg + u2net — MIT**
Eliminación de fondos en imágenes.
Proyecto: https://github.com/danielgatis/rembg

**yt-dlp — Unlicense · spotDL — MIT · Deno — MIT**
Descarga de contenido multimedia y runtime de JavaScript necesario para resolver los retos de YouTube. Se ejecutan como procesos externos.

**NVIDIA CUDA Runtime y cuDNN**
Este software incluye librerías dinámicas redistribuibles de NVIDIA, utilizadas únicamente para acelerar la transcripción y el OCR en GPUs NVIDIA. Versiones exactas distribuidas:

| Componente | Versión | Archivos |
|---|---|---|
| CUDA | 12.9.79 | `cublas64_12.dll`, `cublasLt64_12.dll`, `cudart64_12.dll` |
| cuDNN | 9.10.2.21 | `cudnn64_9.dll`, `cudnn_adv64_9.dll`, `cudnn_cnn64_9.dll`, `cudnn_engines_precompiled64_9.dll`, `cudnn_engines_runtime_compiled64_9.dll`, `cudnn_graph64_9.dll`, `cudnn_heuristic64_9.dll`, `cudnn_ops64_9.dll` |

> "La distribución de estas bibliotecas se realiza exclusivamente en calidad de componentes redistribuibles autorizados por los términos de licencia de NVIDIA aplicables a la versión correspondiente de CUDA/cuDNN. Dichos componentes permanecen sujetos a sus respectivas licencias de NVIDIA y no forman parte de la licencia AGPLv3 aplicable al código original de DEUS MACHINA | TOOLS."

El archivo `LICENSE-EXCEPTION.txt` recoge el **permiso adicional conforme a la sección 7 de la AGPL v3** que autoriza combinar y distribuir el programa junto a esas bibliotecas, reconociendo expresamente que NVIDIA conserva el control de la licencia de CUDA y cuDNN.

© NVIDIA Corporation — https://docs.nvidia.com/cuda/eula/index.html · https://docs.nvidia.com/deeplearning/cudnn/sla/index.html

Para la lista completa de librerías y sus licencias, consulta el archivo `THIRD_PARTY_NOTICES.txt`.

---

## Créditos

**Imagen artística**
"La Novena Ola" (1850) — Iván Aivazovski. Obra en dominio público.
Fuente: https://commons.wikimedia.org/wiki/File:Aivazovsky,_Ivan_-_The_Ninth_Wave.jpg

**Tipografía**
JetBrains Mono — desarrollada por JetBrains, distribuida bajo la SIL Open Font License v1.1.
© 2020 The JetBrains Mono Project Authors — https://scripts.sil.org/OFL

---

## Soporte

Para soporte técnico, consultas o reporte de errores:
**DoMiNaTh0RRoyale@gmail.com**

---

## Autor

Kevin González (DoMiNaTh0R)

---
---
---

# DEUS MACHINA | TOOLS — Version 3.0

---

## Description

DEUS MACHINA | TOOLS is a desktop application for local media processing and automated tasks. It includes tools for video and audio conversion, AI-powered transcription, OCR text extraction, YouTube and Spotify content downloading, PDF editing, image conversion, background removal, batch renaming, and metadata editing and cleaning.

The application runs entirely locally. It does not collect personal data or telemetry of any kind.

For a list of changes included in this version, refer to the `CHANGELOG.md` file.

---

## Download

The installer (~1.7 GB) is available in two places; it is the same file in both:

- **[Download from GitHub Releases](https://github.com/DoMiNaTh0R/DEUS-MACHINA-TOOLS/releases/latest)**
- **[Download from Google Drive](https://drive.google.com/drive/folders/1Vr5GbW31KSOUGScupc5S8DhU_w5zGrFb)** (mirror)

**Source code:** https://github.com/DoMiNaTh0R/DEUS-MACHINA-TOOLS

---

## Highlights of Version 3.0

- **Several modules at once:** convert a video while compressing images and downloading from YouTube. Modules that load AI models (OCR, Transcription and Background Removal) take turns automatically so memory never saturates.
- **New OCR:** PaddleOCR (GPU/CPU) and RapidOCR instead of EasyOCR, with the engine in a separate process, page-by-page decisions in mixed PDFs and reading at 200 DPI.
- **Metadata Lab:** read, edit, clean and verify metadata in images, audio, video, PDF and Office documents, without recompressing the file.
- **Video:** real detection of what your GPU supports (NVENC H.264/H.265/AV1, 10-bit, NVDEC, full-GPU pipeline) quality levels calibrated per codec and support for files with several audio tracks and subtitles (you choose which ones to keep).
- **Downloads:** Spotify support (via spotDL, without waiting in the queue), a 3-download queue for YouTube and other sites, ⚙️ settings (preferred codec, audio track for dubbed videos, subtitles inside the video and YouTube Music song lyrics) and a yt-dlp updater with SHA-256 verification.
- **Transcription:** language selector (including multilingual mode), translation to English, a live mode that no longer drops audio, Spotify links in YouTube → Text and a new tab to download video **subtitles** and **song lyrics** (plain or timed) without AI.
- **"🧹 Free AI model" button** in the menu, Transcription, OCR and Background Removal: unloads the AI model from memory.
- **Renamer:** undo the last full rename, even after closing the app.
- **Faster startup, lighter executable:** the app no longer loads PyTorch; it only uses the required NVIDIA libraries.

---

## System Requirements

| Component         | Minimum                                      | Recommended                                              |
| ----------------- | -------------------------------------------- | -------------------------------------------------------- |
| Operating System  | Windows 10 64-bit                            | Windows 11 64-bit                                        |
| Processor         | Intel i3 (8th Gen) / Ryzen 3 (3000 Series)  | Intel i5 (10th Gen) / Ryzen 5 (5000 Series) or higher   |
| RAM               | 8 GB                                         | 16 GB                                                    |
| Disk Space        | 12 GB                                        | 20 GB                                                    |
| GPU               | Any NVIDIA GPU                               | NVIDIA with 6 GB VRAM or more                            |
| NVIDIA Drivers    | Updated to the latest version                | —                                                        |

> Windows 7 / Vista / 8 / 8.1 have not been tested and compatibility is not guaranteed.

The application works without a GPU: in that case it uses the CPU, with the limitations noted below.

---

## GPU Acceleration and AI Models

The app automatically detects compatible NVIDIA GPUs and uses hardware acceleration when available. There is no need to install the CUDA Toolkit separately, as long as the official NVIDIA drivers are up to date.

If no compatible GPU is found, the application automatically operates in CPU mode, with some limitations on the heavier transcription models.

### Live Transcription Model Reference (faster-whisper)

| Model | CPU | Minimum GPU | Notes |
|---|---|---|---|
| 🟢 TINY | ✅ Works well | GTX 1650 / 2–4 GB VRAM | For basic PCs |
| 🟡 SMALL | ✅ Works | GTX 1650 / 2–4 GB VRAM | Recommended for most users |
| 🟠 MEDIUM | ⚠️ Very slow | RTX 2060 / 3060 — 6 GB VRAM | Only with a decent GPU |
| 🔴 LARGE | ❌ Extremely slow | RTX 3080 / 4060+ — 8 GB VRAM | High-end only |

### OCR Engines

| Engine | Requirements | Notes |
|---|---|---|
| 🚀 PaddleOCR · GPU | NVIDIA **Turing (RTX 20xx) or newer** with a CUDA 12.9 capable driver | Maximum accuracy and fastest |
| 🎯 PaddleOCR · CPU | Any machine | Same accuracy, considerably slower |
| ⚡ RapidOCR · CPU | Any machine | Fast and light, slightly lower accuracy |

The app checks your card before offering GPU mode; if it is not supported or fails, it switches to CPU or RapidOCR on its own and says so on screen.

For video encoding in **AV1** format, a GPU with hardware AV1 encoding support is required (NVIDIA RTX 40xx or higher); on machines without it, the CPU encoder (SVT-AV1) is used.

---

## Model and Component Downloads

The following components are **not included** in the installer and are downloaded automatically the first time they are needed:

| Component | When it is downloaded | Approx. size | Where it is stored |
|---|---|---|---|
| faster-whisper models | When transcribing with that model | 150 MB – 3 GB depending on the model | Hugging Face cache (`~/.cache/huggingface/hub/`) |
| u2net model (background removal) | First time you use "Remove Background" | ~170 MB | `%LOCALAPPDATA%\DeusMachinaTools\rembg_models\` |
| Deno (JavaScript runtime) | Before a download that needs it | ~40 MB | `%LOCALAPPDATA%\DeusMachinaTools\tools\deno\` |
| spotDL | When you paste your first Spotify link | ~50 MB | Application environment |

The OCR models (PaddleOCR's PP-OCRv6 and RapidOCR's own) **are included** with the application, under `tools\paddleocr`.

Subsequent runs do not require a download.

---

## Internet Connection

The app does not require a permanent internet connection. The only situations in which a connection is made are:

- Downloading a model or component for the first time (see the table above).
- Downloading content from YouTube, Spotify or other supported platforms (subtitles included).
- Looking up song lyrics (LRCLIB, YouTube Music and other providers), only when you use that option.
- Updating yt-dlp via the built-in button in the app (with SHA-256 signature verification).

---

## Privacy

- No personal user data is collected.
- No information is sent to external servers owned by this software.
- No telemetry or tracking systems are used.
- All file processing is performed locally on the user's machine.

---

## License

DEUS MACHINA | TOOLS is **free software**, distributed under the **GNU Affero General Public License v3 (AGPL-3.0) or later**. The full text is in the `LICENSE` file (also shipped with the application as `LICENSE.txt`), the section 7 additional permission for the NVIDIA libraries is in `LICENSE-EXCEPTION.txt`, and a plain-language summary of your rights and obligations is in `EULA.txt`.

You may use the program for any purpose (including commercial use), study it, modify it and redistribute it. If you distribute the program or a modified version — or offer its functionality over a network — you must provide the corresponding source code under this same license.

**Source code:** https://github.com/DoMiNaTh0R/DEUS-MACHINA-TOOLS
It is also emailed to anyone who requests it: DoMiNaTh0RRoyale@gmail.com

### Why AGPL

The application links **PyMuPDF (fitz)** directly, which is published under AGPL-3.0. Since it is a library linked inside the same process (not an external program), the whole work is released under the same license.

### Name and logo

Pursuant to AGPL section 7(e), the name "DEUS MACHINA | TOOLS", its logo and its own artwork may not be used to promote modified versions or imply the author's endorsement: publish your versions under your own name. This does not limit any AGPL right over the code.

---

## Third-Party Components

### External programs (mere aggregation)

Distributed alongside the software as independent programs and invoked as external processes. Each is governed by its own license and does not form a derivative work of the main executable.

**FFmpeg — GPL v3**
Used for video and audio conversion and processing. Runs as an independent external process (CLI), with no static or dynamic linking to the main executable.
Source code: https://ffmpeg.org/download.html

**Ghostscript — AGPL v3**
Used for PDF file processing. Invoked exclusively through calls to the `gswin64c.exe` executable, with no direct linking to the main code.
Source code: https://ghostscript.com/

### Linked components

**PyMuPDF (fitz) — AGPL v3**
PDF engine for text extraction, page rendering, and PDF file manipulation. It is linked **directly** as a Python library within the main process: this is not mere aggregation, and it is why the whole application is released under AGPL-3.0.
Documentation and license: https://pymupdf.readthedocs.io/

### Other components

**PaddleOCR / PaddlePaddle / PaddleX — Apache 2.0**
Main OCR engine (PP-OCRv6 models) and its framework. Runs in a process separate from the application.
Project: https://github.com/PaddlePaddle/PaddleOCR

**RapidOCR + ONNX Runtime — Apache 2.0 / MIT**
Lightweight CPU OCR engine.
Project: https://github.com/RapidAI/RapidOCR

**faster-whisper / CTranslate2 — MIT**
Transcription engine (optimized implementation of OpenAI's Whisper, also MIT).
Project: https://github.com/SYSTRAN/faster-whisper

**rembg + u2net — MIT**
Background removal for images.
Project: https://github.com/danielgatis/rembg

**yt-dlp — Unlicense · spotDL — MIT · Deno — MIT**
Media downloading and the JavaScript runtime required to solve YouTube's challenges. They run as external processes.

**NVIDIA CUDA Runtime and cuDNN**
This software includes NVIDIA redistributable dynamic libraries, used only to accelerate transcription and OCR on NVIDIA GPUs. Exact versions distributed:

| Component | Version | Files |
|---|---|---|
| CUDA | 12.9.79 | `cublas64_12.dll`, `cublasLt64_12.dll`, `cudart64_12.dll` |
| cuDNN | 9.10.2.21 | `cudnn64_9.dll`, `cudnn_adv64_9.dll`, `cudnn_cnn64_9.dll`, `cudnn_engines_precompiled64_9.dll`, `cudnn_engines_runtime_compiled64_9.dll`, `cudnn_graph64_9.dll`, `cudnn_heuristic64_9.dll`, `cudnn_ops64_9.dll` |

> "These libraries are distributed solely as redistributable components authorized by the NVIDIA license terms applicable to the corresponding CUDA/cuDNN version. Such components remain subject to their respective NVIDIA licenses and are not part of the AGPLv3 license applicable to the original DEUS MACHINA | TOOLS code."

The `LICENSE-EXCEPTION.txt` file contains the **additional permission under section 7 of the AGPL v3** allowing the program to be combined and distributed together with those libraries, while expressly acknowledging that NVIDIA retains control of the CUDA and cuDNN licensing.

© NVIDIA Corporation — https://docs.nvidia.com/cuda/eula/index.html · https://docs.nvidia.com/deeplearning/cudnn/sla/index.html

For the full list of libraries and their licenses, refer to the `THIRD_PARTY_NOTICES.txt` file.

---

## Credits

**Artwork**
"The Ninth Wave" (1850) — Ivan Aivazovsky. Public domain work.
Source: https://commons.wikimedia.org/wiki/File:Aivazovsky,_Ivan_-_The_Ninth_Wave.jpg

**Typography**
JetBrains Mono — developed by JetBrains, distributed under the SIL Open Font License v1.1.
© 2020 The JetBrains Mono Project Authors — https://scripts.sil.org/OFL

---

## Support

For technical support, inquiries, or bug reports:
**DoMiNaTh0RRoyale@gmail.com**

---

## Author

Kevin González (DoMiNaTh0R)

---
---
---
