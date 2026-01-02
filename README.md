# DEUS-MACHINA-TOOLS
Private-use multitools suite. Work in progress.


============= DEUS MACHINA | TOOLS =============
=============

DESCRIPCIÓN
-----------
DEUS MACHINA | TOOLS es una aplicación de escritorio diseñada para el
procesamiento local de medios y tareas automatizadas.

La aplicación funciona completamente de forma local y no requiere
conexión permanente a internet. No recopila datos personales ni
telemetría de ningún tipo.


REQUISITOS DEL SISTEMA
---------------------
- Sistema operativo:
  Windows 10 o Windows 11 (64 bits).
  Windows 7/vista/8/8.1/ no ha sido probado y no se garantiza compatibilidad.

- Procesador:
  Arquitectura x64 compatible.
  Intel Core i5 o AMD Ryzen 5 (o superior) recomendado.

- Memoria RAM:
  8 GB mínimo.
  16 GB recomendado para un mejor rendimiento.

- Espacio en disco:
  Mínimo 15 GB de espacio libre disponible.

- GPU (opcional, recomendada):
  Tarjeta gráfica NVIDIA RTX series 30xx o 40xx.
  Drivers NVIDIA oficiales actualizados.



USO GENERAL
-----------
- La aplicación se ejecuta como una aplicación de escritorio estándar.
- Todo el procesamiento se realiza localmente.
- La aplicación prioriza el funcionamiento OFFLINE. Los modelos de
  IA (Whisper) ya están incluidos y no requieren internet.
- En caso de no detectarse una GPU compatible, el sistema utilizará CPU.
- Funciones externas: Herramientas específicas como la descarga de videos
  (YouTube/Redes) requieren conexión activa durante su ejecución.




ACELERACIÓN POR GPU
------------------
DEUS MACHINA | TOOLS detecta automáticamente GPUs NVIDIA compatibles
y utiliza aceleración por hardware cuando está disponible.

No es necesario instalar CUDA Toolkit por separado, siempre que los
drivers oficiales de NVIDIA estén actualizados.

Si no hay una GPU compatible disponible, la aplicación funcionará
automáticamente en modo CPU.


PRIVACIDAD
----------
- No se recopilan datos personales del usuario.
- No se envía información a servidores externos propios del software.
- No se utiliza telemetría ni sistemas de seguimiento.
- Todo el procesamiento de archivos y datos se realiza localmente en el
  equipo del usuario.
- Las conexiones a internet se realizan exclusivamente cuando el usuario
  solicita explícitamente funciones que dependen de servicios externos
  (por ejemplo, descarga de contenido desde YouTube).
- Descargas Automáticas de Modelos: Si el usuario solicita un modelo de IA no
  presente en el disco, el software descargará los archivos necesarios (aprox. 
  500MB - 3GB) directamente desde servidores públicos confiables (Hugging Face).
  Una vez descargado, el modelo queda guardado y no requiere internet futuro.

LICENCIA
--------
Este software es de LICENCIA PRIVADA y PROPIETARIA.

Todos los derechos están reservados.
El uso, copia, modificación o redistribución del software está sujeto
a los términos establecidos en el EULA incluido con el producto.


NVIDIA
------
Este software incluye librerías dinámicas del NVIDIA CUDA Toolkit, tales como:

cublas64_12.dll

cublasLt64_12.dll

Estas librerías se redistribuyen conforme al NVIDIA CUDA Toolkit End User License Agreement.

© NVIDIA Corporation
Licencia disponible en:
https://docs.nvidia.com/cuda/eula/index.html


Componentes de terceros (Mera agregación)
-----------------------------------------
El software utiliza diversos componentes de terceros que se distribuyen como programas independientes
(mera agregación). Cada uno se rige por su propia licencia y no forma una obra derivada del ejecutable principal.

FFmpeg — GPL v3

Utilizado para tareas de conversión y procesamiento de video.

Se ejecuta como proceso externo independiente (CLI).
No existe vinculación estática ni dinámica con el ejecutable principal.

FFmpeg es software libre bajo la GNU General Public License v3.
Código fuente disponible en:
https://ffmpeg.org/download.html


Ghostscript — AGPL v3

Utilizado para el procesamiento de archivos PDF.

Se ejecuta exclusivamente mediante llamadas al sistema al ejecutable
gswin64c.exe.
No existe vinculación directa con el código del programa principal.

Ghostscript se distribuye bajo la GNU Affero General Public License v3.
Código fuente disponible en:
https://ghostscript.com/



NOTA SOBRE LICENCIAS DE TERCEROS
-------------------------------
Los componentes de terceros se incluyen como mera agregación y/o
herramientas externas independientes.

Cada componente mantiene su propia licencia y condiciones de uso.
El usuario es responsable de cumplir con los términos de dichas
licencias.


CRÉDITOS
--------
Imagen artística mostrada en el programa:

“La Novena Ola” (1850)
Autor: Iván Aivazovski
Obra en dominio público.

Imagen obtenida desde Wikimedia Commons:
https://commons.wikimedia.org/wiki/File:Aivazovsky,_Ivan_-_The_Ninth_Wave.jpg

Tipografía:

Esta aplicación utiliza la fuente JetBrains Mono.

JetBrains Mono fue desarrollada por JetBrains y se distribuye bajo la
SIL Open Font License, Version 1.1.

© 2020 The JetBrains Mono Project Authors
Texto completo de la licencia disponible en:
https://scripts.sil.org/OFL

SOPORTE
-------
Para soporte técnico, consultas o reportes de errores, utilice los
canales indicados en el EULA del producto.


AUTOR
-----
Kevin González (DoMiNaTh0R)

==================================================


ENGLISH VERSION:


=============DEUS MACHINA | TOOLS=============
=============

DESCRIPTION
-----------
DEUS MACHINA | TOOLS is a desktop application designed for
local media processing and automated tasks.

The application operates entirely locally and does not require
a permanent internet connection. It does not collect personal data
or telemetry of any kind.


SYSTEM REQUIREMENTS
-------------------
- Operating system:
  Windows 10 or Windows 11 (64-bit).
  Windows 7/Vista/8/8.1 has not been tested and compatibility is not guaranteed.

- Processor:
  Compatible x64 architecture.
  Intel Core i5 or AMD Ryzen 5 (or higher) recommended.

- RAM:
  8 GB minimum.
  16 GB recommended for better performance.

- Disk space:
  Minimum 15 GB of available free space.

- GPU (optional, recommended):
  NVIDIA RTX series 30xx or 40xx graphics card.
  Official NVIDIA drivers up to date.


GENERAL USAGE
-------------
- The application runs as a standard desktop application.
- All processing is performed locally.
- The application prioritizes OFFLINE operation. AI models (Whisper)
  are already included and do not require an internet connection.
- If a compatible GPU is not detected, the system will automatically
  fall back to CPU processing.
- External features: Specific tools such as video downloading
  (YouTube / social platforms) require an active internet connection
  only during their execution.


GPU ACCELERATION
----------------
DEUS MACHINA | TOOLS automatically detects compatible NVIDIA GPUs
and uses hardware acceleration when available.

It is not necessary to install the CUDA Toolkit separately, as long as
the official NVIDIA drivers are up to date.

If no compatible GPU is available, the application will automatically
operate in CPU mode.


PRIVACY
-------
- No personal user data is collected.
- No information is sent to external servers owned by the software.
- No telemetry or tracking systems are used.
- Internet connections are made exclusively when the user explicitly
  requests functions that depend on external services
  (for example, downloading content from YouTube).
- All file and data processing is performed locally on the user’s machine.


LICENSE
-------
This software is PRIVATE AND PROPRIETARY LICENSED.

All rights are reserved.
The use, copying, modification, or redistribution of the software is subject
to the terms established in the EULA included with the product.


NVIDIA
------
This software includes dynamic libraries from the NVIDIA CUDA Toolkit, such as:

cublas64_12.dll

cublasLt64_12.dll

These libraries are redistributed in accordance with the NVIDIA CUDA Toolkit
End User License Agreement.

© NVIDIA Corporation
License available at:
https://docs.nvidia.com/cuda/eula/index.html


Third-party components (Mere aggregation)
-----------------------------------------
The software uses various third-party components that are distributed as
independent programs (mere aggregation). Each is governed by its own license
and does not form a derivative work of the main executable.

FFmpeg — GPL v3

Used for video conversion and processing tasks.

Runs as an independent external process (CLI).
There is no static or dynamic linking with the main executable.

FFmpeg is free software under the GNU General Public License v3.
Source code available at:
https://ffmpeg.org/download.html


Ghostscript — AGPL v3

Used for PDF file processing.

Executed exclusively through system calls to the executable
gswin64c.exe.
There is no direct linkage with the main program code.

Ghostscript is distributed under the GNU Affero General Public License v3.
Source code available at:
https://ghostscript.com/



THIRD-PARTY LICENSE NOTICE
-------------------------
Third-party components are included as mere aggregation and/or
independent external tools.

Each component maintains its own license and terms of use.
The user is responsible for complying with the terms of those
licenses.


CREDITS
-------
Artistic image displayed in the program:

“The Ninth Wave” (1850)
Author: Ivan Aivazovsky
Public domain artwork.

Image obtained from Wikimedia Commons:
https://commons.wikimedia.org/wiki/File:Aivazovsky,_Ivan_-_The_Ninth_Wave.jpg

Typeface:

This application uses the JetBrains Mono font.

JetBrains Mono was developed by JetBrains and is distributed under the
SIL Open Font License, Version 1.1.

© 2020 The JetBrains Mono Project Authors
Full license text available at:
https://scripts.sil.org/OFL

SUPPORT
-------
For technical support, inquiries, or bug reports, use the channels
indicated in the product EULA.


AUTHOR
------
Kevin González (DoMiNaTh0R)

==================================================


