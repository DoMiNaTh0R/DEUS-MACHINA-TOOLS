# CHANGELOG — Deus Machina Tools

# —— Novedades v3.0 ——

---
---

# 🇲🇽 ESPAÑOL

---

## 📋 Resumen para el usuario

La 3.0 es un salto grande: el **OCR se rehízo desde cero** (ahora PaddleOCR/RapidOCR en vez de EasyOCR, con motor en un proceso aparte, decisión página por página y lectura a 200 DPI), el **editor de metadatos** pasó de "borrar etiquetas" a un laboratorio completo que lee, edita, limpia y **verifica** imágenes, audio, video, PDF y documentos de Office sin recomprimir nada, y el **convertidor de video** ahora prueba de verdad qué puede hacer tu tarjeta (NVENC H.264/H.265/AV1, 10 bits, NVDEC, ruta 100 % en GPU) en vez de asumirlo.

Además la app ya **no carga PyTorch** (solo usa las DLL de NVIDIA): arranca más rápido y el ejecutable pesa muchísimo menos. Ahora puedes **usar varios módulos a la vez** —convertir un video mientras comprimes imágenes y bajas de YouTube— y lo que usa modelos de IA se turna solo para no saturar la memoria. Se suman **descargas de Spotify**, **cola de 3 descargas**, **subtítulos y letras de canciones**, **deshacer el último renombrado**, **idioma y modo multilingüe en transcripción**, y una regla que ahora vale para toda la app: **nada sobrescribe tus archivos** (si el nombre existe, se guarda como `archivo (1)`).

Además, **el programa pasa a ser software libre bajo licencia AGPL-3.0**: su código fuente está publicado en https://github.com/DoMiNaTh0R/DEUS-MACHINA-TOOLS.

---

## 📜 Cambio de licencia: ahora es software libre (AGPL-3.0)

A partir de la 3.0, **DEUS MACHINA | TOOLS se publica bajo la GNU Affero General Public License v3** (AGPL-3.0) o posterior, en lugar de una licencia privativa.

- **Qué significa para ti:** puedes usar el programa para lo que quieras (incluido uso comercial), estudiar cómo está hecho, modificarlo y redistribuirlo. Si distribuyes el programa o una versión tuya —o si ofreces su funcionalidad a través de una red— tienes que entregar el código fuente correspondiente bajo esta misma licencia.
- **Por qué:** la app enlaza **PyMuPDF (fitz)** directamente como librería dentro de su propio proceso; PyMuPDF es AGPL-3.0, así que el conjunto tiene que serlo también. FFmpeg y Ghostscript siguen siendo programas externos independientes (mera agregación).
- **Código fuente:** https://github.com/DoMiNaTh0R/DEUS-MACHINA-TOOLS (también se envía por correo a quien lo pida).
- **Qué NO cambia:** las bibliotecas de NVIDIA (CUDA 12.9.79 y cuDNN 9.10.2.21) que acompañan a la app se distribuyen como componentes redistribuibles autorizados por NVIDIA, siguen sujetas a sus propias licencias y **no forman parte de la AGPLv3** aplicable al código original. Se añadió un **permiso adicional conforme a la sección 7 de la AGPL** (`LICENSE-EXCEPTION.txt`) que autoriza combinar y distribuir el programa junto a esas bibliotecas, reconociendo que NVIDIA conserva el control de su licencia; los archivos exactos que se distribuyen están listados ahí y en el EULA.
- La app incluye ahora el texto completo de la licencia (`LICENSE.txt`), visible desde *Acerca de… → Ver Documentación y Legal → Licencia (AGPL)*, y el documento de términos (`EULA.txt`) se reescribió para explicar tus derechos bajo la AGPL.

---

## 🚀 Nuevas Funciones

### 1.- Varios módulos trabajando a la vez

Antes la app hacía **una sola cosa a la vez**. Ahora **video, audio, imágenes, PDF, descargas y metadatos trabajan en paralelo**: cada módulo tiene su propia barra de progreso, su botón de cancelar y su propio resumen al terminar (con el nombre del módulo en el título, para distinguirlos si terminan dos a la vez). Cancelar uno no toca a los demás.

Lo que carga modelos de IA (**OCR, Transcripción y Quitar fondo**) va de uno en uno a propósito: dos modelos grandes a la vez saturan la RAM o la VRAM. El que llega segundo muestra **"⏳ Esperando a que termine …"** y arranca solo en cuanto el otro libera la memoria.

### 2.- OCR completamente nuevo

- **Motores nuevos:** se reemplazó EasyOCR por **PaddleOCR (GPU y CPU)** y **RapidOCR (CPU)**, con modelos PP-OCRv6. Se elige con tres tarjetas que muestran el estado real de cada motor (tu GPU detectada, "En memoria ✓", "Cargando…", o el motivo por el que no está disponible).
- **El motor corre en un proceso aparte:** si PaddlePaddle falla o se queda sin VRAM, la app **no se cae**: avisa, lo reinicia o cambia solo a CPU/RapidOCR.
- **Decisión página por página:** en un PDF mixto, las páginas que ya traen texto real se extraen exactas y sin IA, y solo las escaneadas pasan por el OCR. El .txt indica cuántas páginas fueron de cada tipo.
- **200 DPI:** la resolución de lectura se eligió midiendo (páginas A4 escaneadas a 200 y 300 DPI, texto de 6 a 12 pt): a 200 DPI no se pierde ninguna letra y es ~45 % más rápido que 300.
- **Pantalla rediseñada:** zona de arrastre igual que la de Transcripción, barra ancha, reloj que cambia de color por fase (preparando, cargando, escaneando, guardando) y **SALTAR** que termina la página en curso antes de pasar al siguiente archivo.
- **Chequeo de GPU real:** verifica que la tarjeta sea compatible (Turing o posterior) antes de ofrecer el modo GPU, y si falla ofrece reintentar con un clic.

### 3.- Metadata Lab: motor nuevo de metadatos

El módulo pasó de "borrar etiquetas" a un laboratorio completo:

- **Lee, edita y guarda** metadatos de JPEG, PNG, TIFF, WebP (lectura), RAW/HEIC (lectura), audio (MP3, FLAC, M4A, OGG, OPUS, WAV), video (MP4, MKV, MOV…), **PDF** y documentos de **Office** (docx, xlsx, pptx).
- **Limpieza real sin recomprimir:** el JPEG se limpia a nivel de segmentos y el PNG/WebP a nivel de bloques, conservando lo que afecta a cómo se ve la imagen (JFIF, **perfil de color ICC**, Adobe APP14) y borrando lo que es dato personal (EXIF, XMP, IPTC, GPS, miniaturas).
- **Verificación posterior:** tras limpiar, la app comprueba que el archivo resultante sigue siendo válido y que el contenido no cambió (mismas dimensiones y modo de color, mismas pistas y duración en audio/video, mismas páginas en PDF). Si algo no cuadra, descarta el resultado y conserva el original.
- **Escritura atómica:** nunca se toca el archivo original; la copia limpia se escribe aparte y solo se entrega si pasó la verificación.
- **Carátulas:** ver, cambiar o quitar la portada incrustada en archivos de audio.

### 4.- Convertidor de video: motor nuevo

- **Detección real de capacidades:** la app prueba de verdad qué acepta tu FFmpeg y tu tarjeta — **NVENC H.264 / H.265 / AV1**, **10 bits**, **NVDEC** (decodificar en GPU) y la ruta **100 % en GPU** (decodificar, escalar y codificar sin bajar a la RAM) — y elige las mejores opciones que tu equipo soporta, en vez de asumir que existen.
- **Niveles de calidad calibrados** por códec (5 niveles en "Reducir tamaño") y modo "visualmente idéntico" en "Convertir formato", cada uno con su CRF/CQ ajustado por encoder (incluido **SVT-AV1** en CPU).
- **Selector de resolución** (Original, 1440p, 1080p, 720p, 480p) con escalado en GPU cuando se puede.
- **Pistas de audio y subtítulos:** **Convertir** y **Reducir tamaño** preguntan qué pistas de audio y qué subtítulos conservar cuando hay algo que elegir (varias pistas, o subtítulos que caben en el formato de salida). Convertir marca todo de entrada (antes quedaba una sola pista y los subtítulos se perdían salvo el primero en MKV); Reducir tamaño marca solo el audio principal y ningún subtítulo, para que pese menos, pero siempre deja marcar más, con botones **Todas / Principal** y **Todos / Ninguno**. En MP4 y MOV los subtítulos de texto quedan como pistas que se activan en el reproductor, con su nombre (los de imagen, PGS/DVD, solo caben en MKV); en MKV pasan tal cual, con las fuentes que usan los ASS. **Extraer audio** deja elegir una o varias pistas (un archivo por pista, con el idioma en el nombre). Con «Usar la misma elección en los demás archivos» no vuelve a preguntar en esa lista.
- **Audio inteligente por contenedor:** si la pista ya es compatible se copia tal cual en vez de recodificarla.
- **Errores legibles:** si FFmpeg falla, el resumen muestra la línea útil del error, no el volcado completo.

### 5.- Descargas: Spotify, cola de 3, configuración y actualizador verificado

- **Spotify:** pegar un enlace de canción, álbum, playlist o artista descarga el audio vía **spotDL**, con el mismo flujo que YouTube (aviso de lista, subcarpeta, progreso por canción y preguntas cada 50). Va **por fuera de la cola** (no espera ni frena a las de YouTube), baja **hasta 3 canciones a la vez** y el paso "Analizando" es mucho más rápido. En modo Video guarda el audio en **M4A original** (la mejor calidad, sin recomprimir) en vez de MP3; en modo Audio usa el formato elegido.
- **Cola de 3 descargas:** bajan tres a la vez y las demás esperan mostrando **"⏳ En cola (#2)"**, en orden de llegada. En cuanto una termina de bajar y pasa a convertir o empaquetar, **arranca la siguiente**. Cancelar o pausar **libera su lugar al instante**, aunque esté en "Analizando…".
- **⚙️ Configuración del descargador** (se guarda sola): **códec preferido** H.264 (por defecto) o H.265 — VP9.2, AV1 y VP9 siguen primero cuando el video los tiene; la opción solo decide el orden entre H.264 y H.265, sin retrasar la descarga ni bajar nunca la resolución —; **pista de audio** para videos doblados: original (por defecto), inglés, español, ambas o **Preguntarme** (al descargar se abre una ventana con los idiomas del video —muchos traen decenas de doblajes—, con botones **Todas / Original**; si el elegido no está, queda el original; cada pista lleva su idioma y nombre para elegirla en el reproductor; en modo Audio se guarda una sola); **subtítulos dentro del video**: no (por defecto), español, inglés, ambos o **Preguntarme** (al descargar se abre una ventana con todos los idiomas que subió el autor para marcar los que quieras, con **Todos / Ninguno**; nunca los automáticos; quedan como pista seleccionable, no pegados a la imagen; en una playlist se pregunta una sola vez), **letra de la canción** (solo enlaces de YouTube Music, nunca Spotify, y solo en modo Video; apagada por defecto: busca la letra en LRCLIB, YouTube Music y otros y la incrusta como pista «Letra» si tiene tiempos y en la etiqueta de letra del video; si no aparece, se descarga igual, sin letra) y el aviso de Spotify. La **carátula** ahora también se incrusta en **MKV** (como adjunto `cover.jpg`) y en MP4 las pistas de subtítulos muestran su nombre (Español, Letra…) en el reproductor; si alguna vez no se puede incrustar, el estado final lo dice («sin carátula») y la consola muestra el motivo. El resumen de lo elegido se ve al pie de esa ventana, y **«Incluir Metadatos»** también se recuerda.
- **TikTok:** se baja siempre el video **con su audio real**, también en modo Audio (antes podía salir la pista de música del video en vez de lo que se escucha).
- **YouTube más rápido:** cada video se analiza **una sola vez** (antes dos, o tres con subtítulos): la descarga reutiliza ese análisis y ahorra 1–2 s por video.
- **Videos con dos ediciones:** algunos videos editados después de subirse tienen dos versiones (por ejemplo 964 s y 947 s) y, según la sesión, YouTube entrega de la anterior todo (video, audio y doblajes) o una parte (solo los formatos DASH, o solo los HLS con sus doblajes), aunque la página y los subtítulos sean de la actual. La app lo detecta por la duración que declara cada formato (la del audio HLS no es confiable: se toma la de los videos de su misma lista) y vuelve a pedir el video con una sesión nueva (~1 s cada vez, hasta 8 veces) hasta recibir completa la edición actual, la que se ve en YouTube. Si nunca llega, baja una sola edición —nunca el video de una con el audio o los doblajes de la otra— y lo avisa («⚠️ dura 947 s (YouTube dice 964 s)»). Además, si YouTube corta una descarga a mitad (error 403), se baja desde cero en vez de retomar lo bajado a medias con enlaces nuevos. Con un enlace de YouTube, la letra con tiempos sale primero de YouTube Music, que está sincronizada con ese mismo video (la de LRCLIB es la del álbum y podía correrse).
- **"🧹 Limpiar terminadas":** quita de la cola las descargas terminadas, con error o canceladas. Las canceladas ahora se borran de verdad (antes solo se ocultaban y seguían ocupando memoria).
- **Deno automático:** la app descarga el runtime de JavaScript que yt-dlp necesita para resolver los retos de YouTube (una sola vez, del release oficial), lo que evita muchos fallos de descarga.
- **Actualizador de yt-dlp verificado:** comprueba la **firma SHA-256** que publica PyPI antes de instalar; si no coincide, no instala nada y conserva la versión que funcionaba. Además la versión actualizada se carga sin reinstalar la app.

### 6.- Transcripción: idioma a tu gusto y en vivo sin perder audio

- **Selector de idioma** en las tres pestañas: *Automático (detectar)*, *Multilingüe (mezcla)* o uno de 17 idiomas. El selector es un botón compacto que abre una lista con scroll (antes un desplegable ocupaba media pantalla).
- **Multilingüe** para material que mezcla idiomas (una canción en japonés e inglés, una entrevista bilingüe): detecta el idioma en cada segmento.
- **Traducir al inglés** con una casilla, en Archivos y en YouTube → Texto.
- **En vivo:** ya no se pierde audio mientras el modelo transcribe (se graba en paralelo), el idioma se fija tras la primera detección confiable y, al detener, el modelo **queda en memoria** para volver a grabar al instante.
- **Sin WAV intermedios:** el audio se decodifica directo a memoria a 16 kHz, así que transcribir es más rápido y no deja archivos sueltos.
- **YouTube → Texto acepta enlaces de Spotify** (spotDL busca la canción en YouTube) y descarga Deno si hace falta. En TikTok transcribe el audio real del video.
- **"⚡ Modo rápido"** (Archivos y YouTube → Texto, se guarda): transcribe varios trozos de voz a la vez. Con GPU, 6 minutos de voz pasaron de 21 s a ~4 s con el mismo texto; en CPU, casi el doble de rápido. Los subtítulos siguen saliendo en renglones normales. En YouTube → Texto el registro dice si está activado.
- **Nueva pestaña "Subtítulos y Letras":** baja los **subtítulos** de un video (YouTube y otros sitios) sin descargar el audio ni usar IA, en **.srt, .vtt o .txt**, y la **letra de una canción** (YouTube, YouTube Music o Spotify, incluso álbumes y playlists) **sola (.txt) o con tiempos (.lrc)**, buscando en **LRCLIB**, **YouTube Music** y otros proveedores. Un solo botón, **🔍 Buscar y descargar**: en Subtítulos abre una ventana para marcar uno o varios idiomas (un archivo por idioma; los automáticos de YouTube salen limpios, sin líneas repetidas) y en Letra baja directo. Los subtítulos que pintan a cada persona de un color se guardan como **solo texto** (por defecto), con **"Persona 1:", "Persona 2:"…** u **originales** (siempre con sus tiempos; la elección se recuerda). Las letras en .txt salen **con las estrofas separadas** (si una fuente las da todas juntas, se busca en otra). **Acepta listas**: playlists y álbumes de YouTube y YouTube Music (y de otros sitios), además de los de Spotify. Como en YouTube Downloader, pregunta si se descarga la lista (si el enlace es de un video dentro de una lista, se puede bajar solo ese video); las de más de 25 van **de 25 en 25** y al terminar cada tanda pregunta si sigue; y entre un elemento y otro hay una **pausa** (2 a 5 s entre videos, 1 a 2,5 s entre letras) para no saturar al sitio. En subtítulos, los idiomas se eligen en el primer video y se usan en todos (cada lista va en su propia carpeta). Al empezar, el enlace se borra del campo. El registro va con colores y termina con un resumen tipo **"Terminado: 10/10 letras guardadas con éxito"**. Si algo falla, lo dice en pantalla y en el registro, sin cerrarse.
- **Archivos con varias pistas de audio** (películas, videos doblados): si el archivo trae más de una, la transcripción pregunta cuál transcribir; si trae una sola, ni pregunta.

### 7.- Renombrador: deshacer el último renombrado

Nuevo botón **"↩ Deshacer último (N)"**: devuelve su nombre original a **todos** los archivos del último lote, aunque hayas cerrado y vuelto a abrir la app. Pide confirmación y omite los que se movieron o borraron. Además **avisa antes de renombrar** si dos archivos van a quedar con el mismo nombre (se marcan en rojo) y ahora se pueden **intercambiar nombres** (A ↔ B) sin perder ninguno.

### 8.- Imágenes: más formatos y control

- **SVG, HEIC/HEIF y PSD** se abren de forma fiable (cada uno por la vía que mejor lo lee: FFmpeg o Pillow), con transparencia compuesta sobre blanco cuando el destino no la admite.
- **ICO multiescala** con tamaños estándar (256 → 16 px) en un solo archivo.
- **CANCELAR** en Convertir y en Comprimir: termina la imagen en curso y corta el resto de la cola.

### 9.- PDF: resolución al crear PDF desde imágenes

Con **"Forzar A4"** se elige **150 o 300 DPI**. Ese valor es un **techo, no una meta**: si una foto trae menos resolución, se deja tal cual (nunca se amplía). Al terminar, el mensaje dice cuántas se redujeron y cuántas ya estaban por debajo.

### 10.- Aviso al cerrar con trabajo en curso

Si cierras la app mientras algo trabaja, se listan los trabajos en marcha y se pide confirmación. Al aceptar, se cierran de verdad los procesos externos (FFmpeg, Ghostscript, yt-dlp, spotDL) y los motores de IA.

### 11.- Botón "🧹 Liberar modelo IA"

En el menú principal, Transcripción, OCR y Quitar fondo: saca de la memoria el modelo de IA que esté cargado (Whisper, OCR o el de quitar fondo). Si algo lo está usando (o espera turno), lo libera en cuanto termina el último trabajo.

---

## 🛠️ Mejoras

### 1.- Arranque y peso de la app

- **Sin PyTorch:** la app ya no importa PyTorch para detectar la GPU ni para CUDA; usa solo las DLL de NVIDIA (CUDA 12.9 / cuDNN 9.10) y consultas ligeras a la tarjeta (NVML). **El ejecutable pesa muchísimo menos y arranca más rápido.**
- **La detección de NVENC/GPU ya no se repite en cada arranque:** se mide la primera vez que entras al módulo de video y queda guardada en disco, con la firma de FFmpeg + GPU + driver. Si cambia cualquiera de los tres, se vuelve a medir sola; y hay un botón **"↻ Re-detectar"** para forzarlo a mano.
- **Quitar fondo precarga sus librerías** al abrir su pestaña, así al pulsar el botón ya no hay espera. Si falta el modelo (176 MB), empieza a bajarlo **en paralelo** y muestra el avance real.
- **Arranque más fluido:** las librerías pesadas empiezan a cargar mientras se arma la ventana, y la preparación de pantallas en segundo plano **se pausa mientras usas la app** (antes podía trabarla medio segundo cada vez). La lista de micrófonos y el ícono de las ventanas ya no se calculan en el hilo de la interfaz, y las ventanas secundarias (Acerca de, Licencias, ⚙️ Configuración…) se preparan —y se dibujan, sin que se vean— solo mientras la app está quieta, así abren al instante ya completas, también la primera vez.
- **Imágenes y PDF en paralelo:** convertir o comprimir imágenes procesa 2 o 3 a la vez según el procesador (12 fotos: de 11.8 s a 4.5 s) y comprimir PDF corre 3 Ghostscript a la vez (tardan casi lo mismo que uno solo). El resumen sale en el orden de la lista y dos archivos con el mismo nombre de salida no se pisan.
- **Temporales ordenados:** todo lo temporal (app, FFmpeg, yt-dlp, motor OCR) va a una carpeta por sesión dentro de `%TEMP%\DeusMachinaTools` que se limpia al salir, incluidos los restos de sesiones anteriores que se cerraron mal.
- **Un solo modelo de IA en memoria:** un gestor libera el modelo que no se usa (al cargar otro o tras 20 minutos sin uso).

### 2.- Seguridad de tus archivos

- **Nunca se sobrescribe nada:** si el archivo de salida ya existe, se guarda como `nombre (1).ext`, respetando los sufijos (`_conv`, `_mini`, `_CLEAN`…).
- **Ghostscript y rutas largas:** comprimir un PDF guardado en carpetas muy anidadas fallaba (Ghostscript no abre rutas de más de 260 caracteres). Ahora se trabaja con una copia en una carpeta temporal corta y el resultado se mueve a su sitio; si aun así falla, el resumen explica por qué.
- **WebP:** al limpiar metadatos ya no se pierde el **perfil de color ICC**.

### 3.- Interfaz

- **Resúmenes por módulo** (el título dice de cuál es) y el detalle del motor usado en video y OCR (por ejemplo `Nativo + PaddleOCR GPU`).
- **Cada pestaña procesa solo su lista** en Video e Imágenes: lo que ves es lo que se procesa.
- **Arrastrar y soltar** acepta rutas con espacios y varios archivos en todos los módulos.
- **Ventanas secundarias reutilizables:** las ventanas de resumen, licencias, ayuda y avisos se crean ocultas y ya dibujadas, así aparecen de golpe y centradas (sin parpadeo), con la barra de título en oscuro en Windows.
- **Textos correctos:** plurales bien formados (`1 pág.` / `70 págs.`, `1 archivo` / `5 archivos`).
- **Orden de los controles** en YouTube → Texto igual que en Archivos: Modelo IA · Traducir al inglés · Formato · Idioma.
- **Transcripción con bloques parejos:** Archivos, YouTube → Texto y Subtítulos y Letras tienen ahora todos los bloques del mismo ancho. YouTube → Texto suma el **reloj** de Archivos (dorado mientras trabaja, verde con el total), el registro con colores, **de solo lectura**, más alto y con barra para deslizar (si subes a leer, las líneas nuevas no te bajan al final), y **Copiar / Limpiar arriba** de la consola (antes los botones de abajo se cortaban).
- **YouTube Downloader:** el resumen gris ("H.264 · sin subtítulos") pasó al pie de ⚙️ Configuración (y ya no se ve raro un instante al cambiar una opción), la tarjeta de subtítulos ya no parece trabada (los idiomas aparecen solo al activarlos) y **"🧹 Limpiar terminadas"** ya no corta la última letra.
- **Ventanas de pistas y subtítulos más ligeras:** las de YouTube, Transcripción, Subtítulos y Letras y el Convertidor de video dibujan toda la lista de una vez: abren ya armadas y se deslizan sin que los textos se desacomoden (antes, con muchas opciones, se armaban a pedazos y al deslizar los textos se veían mal). Todas tienen botones para marcar de un clic: **Todas / Ninguna**, o **Todas / Original** (**Principal** en tus archivos) donde hay que quedarse con una como mínimo.
- **Pestañas sin bordes grises:** con Windows escalado (125 %, 150 %) las pestañas y los botones segmentados (PDF, Video, Imágenes, ⚙️ Configuración…) mostraban una rayita y piquitos grises en las orillas; ahora se dibujan a su tamaño exacto.
- **Estado de la tarjeta de OCR centrado** (GPU detectada / "En memoria ✓").

---

## 🐛 Correcciones de Errores

### 1.- Archivos que se dañaban a sí mismos

Convertir un M4A a M4A dejaba el original **truncado** (5 s quedaban en 2) y convertir un PNG a PNG lo sobrescribía en el sitio: la salida se escribía sobre la entrada. Ahora la salida siempre usa un nombre libre.

### 2.- FFmpeg quedaba corriendo tras un error

Con nombres o metadatos en japonés, chino o con emojis, leer la salida de FFmpeg fallaba por codificación y el proceso quedaba vivo consumiendo CPU. Ahora se lee en UTF-8 y el proceso se cierra pase lo que pase.

### 3.- Arrastrar varios archivos con espacios en la ruta

Al soltar varios archivos, una ruta con espacios podía partirse en dos rutas inválidas. Ahora se interpreta la lista tal como la entrega Windows, en todos los módulos.

### 4.- Video: las pestañas se pisaban entre sí

Cargar archivos en "Convertir" y pulsar el botón de "Comprimir" procesaba la lista equivocada. Cada pestaña tiene ahora su propia lista y sus propios controles.

### 5.- Renombrador: ordenar por fecha

Las opciones "Fecha Creación" y "Fecha Modificación" ordenaban siempre por fecha de creación (la condición del código estaba mal escrita y siempre se cumplía la primera). Ahora cada una ordena por lo que dice.

### 6.- Renombrador: intercambiar nombres

No se podían **intercambiar** nombres entre dos archivos (A → B y B → A) y, en algún caso, un archivo podía sobrescribir a otro. El renombrado se hace ahora en dos pasos con nombres temporales, y valida la lista completa antes de tocar nada.

### 7.- PDF: compresión

- Un PDF con `%` en el nombre rompía la llamada a Ghostscript (lo tomaba como patrón de numeración).
- Si la "compresión" dejaba el archivo **más pesado**, se entregaba igual. Ahora se descarta y se informa: *"ya estaba optimizado, se conservó el original"*.

### 8.- Imágenes a PDF: memoria

Con muchas fotos grandes se agotaba la RAM (se decodificaban todas a la vez). Ahora se procesa una por una: 24 fotos de 12 MP pasaron de ~1.1 GB a ~250 MB.

### 9.- Transcripción en vivo

- **Se perdía audio:** mientras Whisper transcribía un fragmento, nadie escuchaba el micrófono. Ahora se graba en paralelo y no se pierde nada, ni lo que dices justo antes de pulsar DETENER.
- **El idioma saltaba** entre fragmentos (una frase en español, la siguiente detectada como portugués). Ahora se fija en cuanto la detección es confiable.

### 10.- Tarjetas del OCR recortadas

En pantallas con escala de Windows al 125 %, los textos de las tarjetas se cortaban ("Máxima precisión, rápi…") aunque cabían: se medían con un tamaño de fuente distinto al que se dibujaba. Ahora se miden con las medidas reales de pantalla.

### 11.- Cerrar la app dejaba procesos vivos

Cerrar con una conversión o descarga en curso dejaba FFmpeg, yt-dlp o el motor OCR trabajando en segundo plano. Ahora se cierran todos.

### 12.- TikTok: videos que no se descargaban

Algunos TikTok fallaban en el descargador: se elegía un H.265 "solo video" que a veces ni descarga y se le pegaba la pista de música del video. Ahora se baja el video con su propio audio, en la mejor resolución.

### 13.- Descargas canceladas que trababan la cola

Cancelar mientras decía "Analizando…" no detenía nada: la descarga seguía ocupando su lugar (aunque ya no se viera) y las siguientes se quedaban esperando. Ahora el lugar se libera al instante y se cierran también los procesos hijos (el FFmpeg de spotDL).

### 14.- Ventanas negras que aparecían y se cerraban

En la app compilada, cada programa de consola que se lanzaba abría una ventana negra por un instante: FFmpeg al convertir de Spotify, el Deno con el que yt-dlp resuelve los retos de YouTube (descargas y Subtítulos y Letras) y el `where ccache` que corre PaddlePaddle cada vez que se carga el motor del OCR. Ahora todos se lanzan sin ventana, en la app y en sus procesos aparte (motor OCR, spotDL).

### 15.- Quitar fondo decía "Descargando" siempre

Buscaba el modelo en otra carpeta y avisaba que lo estaba descargando aunque ya estuviera bajado.

### 16.- Imágenes a PDF: mensaje final larguísimo

El resumen de DPI ahora va en una segunda línea corta (por ejemplo `2 reducidas a 300 DPI · 3 ya bajo 300 DPI (mín. 72)`).

---

## ⚙️ Cambios Internos

- **CUDA sin PyTorch:** `_CudaLigera` / `_TorchLigero` detectan la GPU y preparan las DLL de CUDA/cuDNN (orden de carga incluido) sin importar torch. El empaquetado copia solo las DLL de NVIDIA necesarias.
- **Motor OCR en proceso aparte:** `GestorMotorOCR` arranca el motor con `multiprocessing` (spawn) y se comunica por tubería; un fallo del motor no tumba la app.
- **Motor de metadatos (Metadata Lab):** lectores/escritores/sanitizadores por formato (`_jpeg_*`, `_png_*`, `_webp_*`, `_tiff_*`, `_audio_*`, `_video_*`, `_pdf_*`, `_ooxml_*`) con escritura atómica y verificación de contenido.
- **Motor de lotes por módulo (`LoteTrabajo`) y carril de IA (`CarrilIA`):** cada módulo lleva su cola, sus banderas de cancelación y su proceso externo; el carril serializa lo que carga modelos.
- **Cola de interfaz (`_en_ui`):** ningún hilo de trabajo toca widgets directamente (Tkinter no es seguro entre hilos).
- **Capacidades de FFmpeg** (`ffmpeg_capacidades`) con pruebas reales de NVENC/NVDEC y caché en disco (`ffmpeg_caps.json`) firmada por build de FFmpeg + GPU + driver.
- **Gestor de modelos de IA** (`GestorModelosIA`) con liberación por inactividad y bloqueo mientras un modelo está en uso.
- **Temporales por sesión** (`%TEMP%\DeusMachinaTools\sesion_<pid>`), limpieza de restos antiguos y salida estándar segura en builds sin consola.
- **Helpers nuevos:** `_ruta_unica()`, `_rutas_drop()`, `_plural_pag()`, `_trans_opts_idioma()`, `img_open_any()`, `vid_info()`.
- **Verificación SHA-256** de los wheels de `yt-dlp` y `yt-dlp-ejs`, con carga en caliente de la versión nueva.
- **Registro para deshacer renombrados** (`renombrado_ultimo.json`) en `%LOCALAPPDATA%\DeusMachinaTools`.
- **Nuevo `generar_licencias.py`:** genera `THIRD_PARTY_NOTICES.txt` leyendo las licencias de todos los paquetes del entorno, en orden alfabético, más los componentes externos (FFmpeg, Ghostscript, Deno, NVIDIA, modelos).
- **Código muerto eliminado:** funciones y métodos que ya no usaba ningún flujo (incluido todo el camino viejo de EasyOCR).

---
---
---

# 🇺🇸 ENGLISH

---

## 📋 User Summary

3.0 is a big jump: **OCR was rebuilt from scratch** (PaddleOCR/RapidOCR instead of EasyOCR, engine running in a separate process, page-by-page decisions and reading at 200 DPI), the **metadata editor** went from "strip tags" to a full lab that reads, edits, cleans and **verifies** images, audio, video, PDF and Office documents without recompressing anything, and the **video converter** now really probes what your card can do (NVENC H.264/H.265/AV1, 10-bit, NVDEC, full-GPU pipeline) instead of assuming it.

The app also **no longer loads PyTorch** (it only uses NVIDIA's DLLs): it starts faster and the executable is far smaller. You can now **use several modules at once** — convert a video while compressing images and downloading from YouTube — and anything that loads AI models takes turns so memory never saturates. Add **Spotify downloads**, a **3-download queue**, **subtitles and song lyrics**, **undo last rename**, **language and multilingual mode** in transcription, and one rule that now applies everywhere: **nothing overwrites your files** (if the name exists, it is saved as `file (1)`).

On top of that, **the program becomes free software under the AGPL-3.0 license**: its source code is published at https://github.com/DoMiNaTh0R/DEUS-MACHINA-TOOLS.

---

## 📜 License change: it is now free software (AGPL-3.0)

Starting with 3.0, **DEUS MACHINA | TOOLS is released under the GNU Affero General Public License v3** (AGPL-3.0) or later, instead of a proprietary license.

- **What it means for you:** you can use the program for anything (including commercial use), study how it is built, modify it and redistribute it. If you distribute the program or your own version — or offer its functionality over a network — you must provide the corresponding source code under this same license.
- **Why:** the app links **PyMuPDF (fitz)** directly as a library inside its own process; PyMuPDF is AGPL-3.0, so the whole work must be too. FFmpeg and Ghostscript remain independent external programs (mere aggregation).
- **Source code:** https://github.com/DoMiNaTh0R/DEUS-MACHINA-TOOLS (also emailed on request).
- **What does NOT change:** the NVIDIA libraries (CUDA 12.9.79 and cuDNN 9.10.2.21) shipped with the app are distributed as redistributable components authorized by NVIDIA, remain subject to their own licenses and **are not part of the AGPLv3** applying to the original code. An **additional permission under AGPL section 7** was added (`LICENSE-EXCEPTION.txt`) allowing the program to be combined and distributed with those libraries while acknowledging that NVIDIA retains control of their licensing; the exact files shipped are listed there and in the EULA.
- The app now ships the full license text (`LICENSE.txt`), visible from *About… → View Documentation and Legal → License (AGPL)*, and the terms document (`EULA.txt`) was rewritten to explain your rights under the AGPL.

---

## 🚀 New Features

### 1.- Several Modules Working at Once

The app used to do **one thing at a time**. Now **video, audio, images, PDF, downloads and metadata run in parallel**: each module has its own progress bar, cancel button and summary window (titled with the module name, so you can tell them apart when two finish together). Cancelling one does not touch the others.

Anything that loads AI models (**OCR, Transcription and Background Removal**) runs one at a time on purpose: two large models at once saturate RAM or VRAM. Whoever arrives second shows **"⏳ Waiting for … to finish"** and starts as soon as memory is free.

### 2.- Completely New OCR

- **New engines:** EasyOCR was replaced by **PaddleOCR (GPU and CPU)** and **RapidOCR (CPU)**, with PP-OCRv6 models. You pick one from three cards showing each engine's real state (your detected GPU, "In memory ✓", "Loading…", or why it is unavailable).
- **The engine runs in a separate process:** if PaddlePaddle fails or runs out of VRAM, the app **does not crash**: it reports, restarts it or falls back to CPU/RapidOCR.
- **Page-by-page decision:** in a mixed PDF, pages that already contain real text are extracted exactly and without AI; only scanned pages go through OCR. The .txt states how many pages of each kind.
- **200 DPI:** the reading resolution was chosen by measurement (A4 pages scanned at 200 and 300 DPI, text from 6 to 12 pt): at 200 DPI no character is lost and it is ~45 % faster than 300.
- **Redesigned screen:** drop area matching Transcription, wide progress bar, a clock that changes color per phase, and **SKIP** that finishes the current page before moving to the next file.
- **Real GPU check:** it verifies the card is supported (Turing or newer) before offering GPU mode, and offers a one-click retry if it fails.

### 3.- Metadata Lab: New Metadata Engine

The module went from "strip tags" to a full lab:

- **Reads, edits and writes** metadata for JPEG, PNG, TIFF, WebP (read), RAW/HEIC (read), audio (MP3, FLAC, M4A, OGG, OPUS, WAV), video (MP4, MKV, MOV…), **PDF** and **Office** documents (docx, xlsx, pptx).
- **Real cleaning without recompressing:** JPEG is cleaned at segment level and PNG/WebP at chunk level, keeping what affects how the image looks (JFIF, **ICC color profile**, Adobe APP14) and removing personal data (EXIF, XMP, IPTC, GPS, thumbnails).
- **Verification afterwards:** after cleaning, the app checks the result is still valid and the content did not change (same dimensions and color mode, same tracks and duration for audio/video, same page count for PDF). If anything is off, the result is discarded and the original kept.
- **Atomic writing:** the original file is never touched; the clean copy is written separately and only delivered once it passes verification.
- **Cover art:** view, replace or remove the embedded cover in audio files.

### 4.- Video Converter: New Engine

- **Real capability detection:** the app actually tests what your FFmpeg and your card accept — **NVENC H.264 / H.265 / AV1**, **10-bit**, **NVDEC** (GPU decoding) and the **full-GPU** path (decode, scale and encode without touching RAM) — and picks the best options your machine supports instead of assuming they exist.
- **Calibrated quality levels** per codec (5 levels in "Reduce size") and a "visually identical" mode in "Convert format", each with its CRF/CQ tuned per encoder (including **SVT-AV1** on CPU).
- **Resolution selector** (Original, 1440p, 1080p, 720p, 480p) with GPU scaling when possible.
- **Audio tracks and subtitles:** **Convert** and **Reduce size** ask which audio tracks and which subtitles to keep whenever there is something to choose (several tracks, or subtitles that fit the output format). Convert ticks everything by default (only one track used to survive and subtitles were lost except the first one in MKV); Reduce size ticks only the main audio track and no subtitles, so the file stays small, but always lets you tick more, with **All / Main** and **All / None** buttons. In MP4 and MOV text subtitles become tracks you switch on in the player, with their name (image-based PGS/DVD ones only fit in MKV); in MKV they are kept as-is, along with the fonts used by ASS subtitles. **Extract audio** lets you pick one or several tracks (one file per track, with the language in the name). With "Use the same choice for the other files" it does not ask again for that list.
- **Smart audio per container:** if the track is already compatible it is copied as-is instead of re-encoding.
- **Readable errors:** if FFmpeg fails, the summary shows the useful error line, not the whole dump.

### 5.- Downloads: Spotify, 3-Download Queue, Settings and Verified Updater

- **Spotify:** paste a track, album, playlist or artist link and the audio is downloaded via **spotDL**, with the same flow as YouTube (list warning, subfolder, per-song progress and a prompt every 50). It runs **outside the queue** (it neither waits for nor holds back YouTube downloads), downloads **up to 3 songs at once** and the "Analyzing" step is much faster. In Video mode it saves the audio as the **original M4A** (best quality, no re-encoding) instead of MP3; in Audio mode it uses the chosen format.
- **3-download queue:** three download at a time and the rest wait showing **"⏳ Queued (#2)"**, in arrival order. As soon as one finishes downloading and moves on to converting or packaging, **the next one starts**. Cancelling or pausing **frees its slot instantly**, even while "Analyzing…".
- **⚙️ Downloader settings** (saved automatically): **preferred codec** H.264 (default) or H.265 — VP9.2, AV1 and VP9 still come first when the video has them; the option only sets the order between H.264 and H.265, without slowing the download or ever lowering the resolution —; **audio track** for dubbed videos: original (default), English, Spanish, both or **Ask me** (a window lists the video's languages at download time —many videos carry dozens of dubs—, with **All / Original** buttons; if the chosen one is missing, the original is kept; each track carries its language and name so it can be picked in the player; in Audio mode a single track is saved); **subtitles inside the video**: no (default), Spanish, English, both or **Ask me** (a window lists every language uploaded by the author at download time so you can tick the ones you want, with **All / None**; never automatic ones; added as a selectable track, not burned into the picture; in a playlist it asks only once), **song lyrics** (YouTube Music links only, never Spotify, and only in Video mode; off by default: lyrics are searched on LRCLIB, YouTube Music and other providers and embedded as a "Letra" subtitle track when timed and in the video's lyrics tag; if none is found the download goes ahead without lyrics) and the Spotify warning. **Cover art** is now embedded in **MKV** too (as a `cover.jpg` attachment) and MP4 subtitle tracks show their name (Español, Letra…) in the player; if it ever cannot be embedded, the final status says so ("sin carátula") and the console shows why. A summary of the choices is shown at the bottom of that window, and **"Include Metadata"** is remembered too.
- **TikTok:** the video is always downloaded **with its real audio**, in Audio mode too (the video's music track could be picked instead of what you actually hear).
- **Faster YouTube:** each video is analyzed **only once** (it used to be twice, or three times with subtitles): the download reuses that analysis and saves 1–2 s per video.
- **Videos with two editions:** some videos edited after upload have two versions (for example 964 s and 947 s) and, depending on the session, YouTube serves the older one entirely (video, audio and dubs) or partly (only the DASH formats, or only the HLS ones with their dubs), even though the page and the subtitles belong to the current one. The app spots it from the duration each format states (the HLS audio one is unreliable: the duration of the videos in the same playlist is used instead) and requests the video again with a fresh session (~1 s each, up to 8 times) until the current edition —the one YouTube plays— arrives complete. If it never does, a single edition is downloaded —never the video of one with the audio or dubs of the other— and the download says so ("⚠️ dura 947 s (YouTube dice 964 s)"). Also, if YouTube cuts a download halfway (403 error), it starts from scratch instead of resuming the half-downloaded data with new links. With a YouTube link, timed lyrics come from YouTube Music first, which is synced to that same video (LRCLIB's is the album version and could drift).
- **"🧹 Clear finished":** removes finished, failed or cancelled downloads from the queue. Cancelled ones are now really deleted (they used to be only hidden and kept using memory).
- **Automatic Deno:** the app downloads the JavaScript runtime yt-dlp needs to solve YouTube's challenges (once, from the official release), which prevents many download failures.
- **Verified yt-dlp updater:** it checks the **SHA-256 signature** published by PyPI before installing; if it does not match, nothing is installed and the working version is kept. The updated version is also loaded without reinstalling the app.

### 6.- Transcription: Language Your Way and Live Without Losing Audio

- **Language selector** in all three tabs: *Automatic (detect)*, *Multilingual (mixed)* or one of 17 languages. It is a compact button that opens a scrollable list (a plain dropdown used to cover half the screen).
- **Multilingual** for material mixing languages (a song in Japanese and English, a bilingual interview): it detects the language per segment.
- **Translate to English** with a checkbox, in Files and YouTube → Text.
- **Live:** audio is no longer lost while the model transcribes (recording runs in parallel), the language is locked after the first reliable detection and, when you stop, the model **stays in memory** so you can record again instantly.
- **No intermediate WAV files:** audio is decoded straight to memory at 16 kHz, so transcribing is faster and leaves no leftover files.
- **YouTube → Text accepts Spotify links** (spotDL finds the song on YouTube) and downloads Deno when needed. On TikTok it transcribes the video's real audio.
- **"⚡ Fast mode"** (Files and YouTube → Text, remembered): transcribes several speech chunks at once. With a GPU, 6 minutes of speech went from 21 s to ~4 s with the same text; on CPU, almost twice as fast. Subtitles still come out in normal-length lines. In YouTube → Text the log says whether it is on.
- **New "Subtitles & Lyrics" tab:** downloads a video's **subtitles** (YouTube and other sites) without downloading the audio or using AI, as **.srt, .vtt or .txt**, and a **song's lyrics** (YouTube, YouTube Music or Spotify, even albums and playlists) **plain (.txt) or timed (.lrc)**, searching **LRCLIB**, **YouTube Music** and other providers. A single **🔍 Search and download** button: in Subtitles it opens a window to tick one or several languages (one file per language; YouTube's automatic captions come out clean, without repeated lines) and in Lyrics it downloads right away. Subtitles that paint each person in a different color can be saved as **plain text** (default), with **"Persona 1:", "Persona 2:"…** labels or **as they are** (always with their timings; the choice is remembered). Plain .txt lyrics come out **with the stanzas separated** (if a source gives them all run together, another source is tried). **Lists are accepted**: YouTube and YouTube Music playlists and albums (and other sites' lists), as well as Spotify ones. As in YouTube Downloader, it asks whether to download the list (if the link is a video inside a list, just that video can be downloaded); lists over 25 go **25 at a time** and it asks whether to continue after each batch; and there is a **pause** between items (2–5 s between videos, 1–2.5 s between lyrics) so the site is not flooded. For subtitles, languages are picked on the first video and used for all of them (each list gets its own folder). When it starts, the link is cleared from the field. The log is color-coded and ends with a summary such as **"Terminado: 10/10 letras guardadas con éxito"** (finished, 10/10 saved). If something fails, it says so on screen and in the log, without crashing.
- **Files with several audio tracks** (movies, dubbed videos): if a file has more than one, transcription asks which one to transcribe; with a single track it does not ask at all.

### 7.- Renamer: Undo the Last Rename

New **"↩ Undo last (N)"** button: it restores the original name of **every** file from the last batch, even after closing and reopening the app. It asks for confirmation and skips files that were moved or deleted. It also **warns before renaming** when two files would end up with the same name (marked in red) and can now **swap names** (A ↔ B) without losing any.

### 8.- Images: More Formats and Control

- **SVG, HEIC/HEIF and PSD** open reliably (each through whichever reads it best: FFmpeg or Pillow), with transparency composited over white when the target does not support it.
- **Multi-size ICO** with standard sizes (256 → 16 px) in a single file.
- **CANCEL** in both Convert and Compress: finishes the current image and stops the rest of the queue.

### 9.- PDF: Resolution When Building a PDF from Images

With **"Force A4"** you choose **150 or 300 DPI**. That value is a **ceiling, not a target**: if a photo has less resolution, it is left as is (never upscaled). When finished, the message says how many were reduced and how many were already below it.

### 10.- Warning When Closing With Work in Progress

If you close the app while something is running, the running jobs are listed and confirmation is requested. On accept, external processes (FFmpeg, Ghostscript, yt-dlp, spotDL) and AI engines are actually terminated.

### 11.- "🧹 Free AI model" Button

In the main menu, Transcription, OCR and Background Removal: it unloads whichever AI model is in memory (Whisper, OCR or the background-removal one). If something is using it (or waiting for its turn), it is freed as soon as the last job finishes.

---

## 🛠️ Improvements

### 1.- Startup and App Size

- **No PyTorch:** the app no longer imports PyTorch to detect the GPU or for CUDA; it only uses NVIDIA's DLLs (CUDA 12.9 / cuDNN 9.10) plus lightweight queries to the card (NVML). **The executable is far smaller and starts faster.**
- **NVENC/GPU detection no longer repeats on every startup:** it is measured the first time you open the video module and stored on disk, signed with FFmpeg + GPU + driver. If any of the three changes it is measured again automatically, and there is a **"↻ Re-detect"** button to force it by hand.
- **Background removal preloads its libraries** when you open its tab, so pressing the button no longer means waiting. If the model (176 MB) is missing, it starts downloading **in parallel** and shows real progress.
- **Smoother startup:** heavy libraries start loading while the window is being built, and background screen preparation **pauses while you use the app** (it could freeze it for half a second at a time). The microphone list and the window icon are no longer computed on the UI thread, and secondary windows (About, Licenses, ⚙️ Settings…) are prepared —and drawn, invisibly— only while the app is idle, so they open instantly and complete, the first time too.
- **Images and PDF in parallel:** converting or compressing images handles 2 or 3 at a time depending on the CPU (12 photos: from 11.8 s to 4.5 s) and PDF compression runs 3 Ghostscript processes at once (about as fast as a single one). The summary keeps the list order and two files with the same output name never overwrite each other.
- **Tidy temporary files:** everything temporary (app, FFmpeg, yt-dlp, OCR engine) goes to a per-session folder inside `%TEMP%\DeusMachinaTools` that is cleaned on exit, including leftovers from sessions that closed badly.
- **Only one AI model in memory:** a manager releases the model that is not in use (when another loads, or after 20 idle minutes).

### 2.- File Safety

- **Nothing is ever overwritten:** if the output file exists, it is saved as `name (1).ext`, keeping your suffixes (`_conv`, `_mini`, `_CLEAN`…).
- **Ghostscript and long paths:** compressing a PDF in deeply nested folders used to fail (Ghostscript cannot open paths longer than 260 characters). It now works through a copy in a short temporary folder; if it still fails, the summary explains why.
- **WebP:** cleaning metadata no longer loses the **ICC color profile**.

### 3.- Interface

- **Per-module summaries** (the title states which one) and the engine used for video and OCR (for example `Native + PaddleOCR GPU`).
- **Each tab processes only its own list** in Video and Images: what you see is what gets processed.
- **Drag and drop** accepts paths with spaces and multiple files in every module.
- **Reusable secondary windows:** summary, licenses, help and warning windows are created hidden and fully drawn, so they appear at once and centered (no flicker), with a dark title bar on Windows.
- **Correct wording:** proper plurals (`1 page` / `70 pages`, `1 file` / `5 files`).
- **Control order** in YouTube → Text matching the Files tab: AI Model · Translate to English · Format · Language.
- **Even Transcription blocks:** Files, YouTube → Text and Subtitles & Lyrics now have all their blocks at the same width. YouTube → Text gets the Files **timer** (gold while working, green with the total), a color-coded, **read-only**, taller log with a scrollbar (if you scroll up to read, new lines no longer jump you to the bottom), and **Copy / Clear above** the console (the bottom buttons used to be cut off).
- **YouTube Downloader:** the grey summary ("H.264 · sin subtítulos") moved to the bottom of ⚙️ Settings (and no longer glitches for a moment when an option changes), the subtitles card no longer looks stuck (languages only appear once subtitles are enabled) and **"🧹 Clear finished"** no longer cuts off its last letter.
- **Lighter track and subtitle windows:** the ones in YouTube, Transcription, Subtitles & Lyrics and the Video converter draw the whole list at once: they open fully built and scroll without the text jumping around (with many options they used to build up piece by piece and the text looked broken while scrolling). All of them have one-click buttons: **All / None**, or **All / Original** (**Main** for your own files) where at least one must stay.
- **Tabs without grey edges:** with Windows scaling (125 %, 150 %) tabs and segmented buttons (PDF, Video, Images, ⚙️ Settings…) showed a small grey line and notches at their edges; they are now drawn at their exact size.
- **OCR card status centered** (detected GPU / "In memory ✓").

---

## 🐛 Bug Fixes

### 1.- Files That Damaged Themselves

Converting an M4A to M4A left the original **truncated** (5 s became 2) and converting a PNG to PNG overwrote it in place: the output was written over the input. The output now always uses a free name.

### 2.- FFmpeg Left Running After an Error

With Japanese or Chinese names and metadata, or emojis, reading FFmpeg's output failed on encoding and the process stayed alive consuming CPU. It is now read as UTF-8 and the process is terminated no matter what.

### 3.- Dropping Several Files With Spaces in the Path

When dropping several files, a path with spaces could be split into two invalid paths. The list is now parsed exactly as Windows delivers it, in every module.

### 4.- Video: Tabs Interfering With Each Other

Loading files in "Convert" and pressing the "Compress" button processed the wrong list. Each tab now has its own list and controls.

### 5.- Renamer: Sorting by Date

The "Creation Date" and "Modification Date" options always sorted by creation date (the condition was written incorrectly and the first one always matched). Each now sorts by what it says.

### 6.- Renamer: Swapping Names

Names could not be **swapped** between two files (A → B and B → A) and, in some cases, one file could overwrite another. Renaming now happens in two steps with temporary names, validating the whole list before touching anything.

### 7.- PDF: Compression

- A PDF with `%` in its name broke the Ghostscript call (it was read as a page-numbering pattern).
- If "compression" left the file **heavier**, it was delivered anyway. It is now discarded and reported: *"already optimized, the original was kept"*.

### 8.- Images to PDF: Memory

With many large photos, RAM ran out (all were decoded at once). They are now processed one by one: 24 photos of 12 MP went from ~1.1 GB to ~250 MB.

### 9.- Live Transcription

- **Audio was lost:** while Whisper transcribed a fragment, nobody was listening to the microphone. Recording now runs in parallel and nothing is lost, not even what you say right before pressing STOP.
- **The language jumped** between fragments (one sentence in Spanish, the next detected as Portuguese). It is now locked as soon as detection is reliable.

### 10.- Clipped OCR Cards

On displays with Windows scaling at 125 %, card texts were cut off ("Maximum accuracy, fa…") even though they fit: they were measured with a different font size than the one drawn. They are now measured with real on-screen metrics.

### 11.- Closing the App Left Processes Alive

Closing with a conversion or download in progress left FFmpeg, yt-dlp or the OCR engine working in the background. They are all terminated now.

### 12.- TikTok: Videos That Would Not Download

Some TikToks failed in the downloader: an H.265 "video only" format that sometimes does not even download was picked and the video's music track was attached to it. The video is now downloaded with its own audio, at the best resolution.

### 13.- Cancelled Downloads Blocking the Queue

Cancelling while "Analyzing…" stopped nothing: the download kept its slot (even though it was no longer shown) and the next ones kept waiting. The slot is now freed instantly and child processes (spotDL's FFmpeg) are closed too.

### 14.- Black Windows That Flashed and Closed

In the compiled app, every console program that was launched flashed a black window: FFmpeg when converting from Spotify, the Deno runtime yt-dlp uses to solve YouTube's challenges (downloads and Subtitles & Lyrics) and the `where ccache` PaddlePaddle runs every time the OCR engine loads. They all run without a window now, in the app and in its separate processes (OCR engine, spotDL).

### 15.- Background Removal Always Said "Downloading"

It looked for the model in another folder and reported a download even when the model was already there.

### 16.- Images to PDF: Very Long Final Message

The DPI summary now goes on a short second line (for example `2 reduced to 300 DPI · 3 already below 300 DPI (min. 72)`).

---

## ⚙️ Internal Changes

- **CUDA without PyTorch:** `_CudaLigera` / `_TorchLigero` detect the GPU and prepare the CUDA/cuDNN DLLs (load order included) without importing torch. The build copies only the NVIDIA DLLs that are actually used.
- **OCR engine in a separate process:** `GestorMotorOCR` starts the engine with `multiprocessing` (spawn) and talks to it over a pipe; an engine crash does not take the app down.
- **Metadata engine (Metadata Lab):** per-format readers/writers/sanitizers (`_jpeg_*`, `_png_*`, `_webp_*`, `_tiff_*`, `_audio_*`, `_video_*`, `_pdf_*`, `_ooxml_*`) with atomic writing and content verification.
- **Per-module batch engine (`LoteTrabajo`) and AI lane (`CarrilIA`):** each module carries its own queue, cancel flags and external process; the lane serializes anything that loads models.
- **UI queue (`_en_ui`):** no worker thread touches widgets directly (Tkinter is not thread-safe).
- **FFmpeg capabilities** (`ffmpeg_capacidades`) with real NVENC/NVDEC tests and an on-disk cache (`ffmpeg_caps.json`) signed by FFmpeg build + GPU + driver.
- **AI model manager** (`GestorModelosIA`) with idle release and locking while a model is in use.
- **Per-session temporary folders** (`%TEMP%\DeusMachinaTools\sesion_<pid>`), cleanup of old leftovers and safe standard output in console-less builds.
- **New helpers:** `_ruta_unica()`, `_rutas_drop()`, `_plural_pag()`, `_trans_opts_idioma()`, `img_open_any()`, `vid_info()`.
- **SHA-256 verification** of the `yt-dlp` and `yt-dlp-ejs` wheels, with hot loading of the new version.
- **Rename undo journal** (`renombrado_ultimo.json`) in `%LOCALAPPDATA%\DeusMachinaTools`.
- **New `generar_licencias.py`:** builds `THIRD_PARTY_NOTICES.txt` by reading the licenses of every package in the environment, alphabetically, plus external components (FFmpeg, Ghostscript, Deno, NVIDIA, models).
- **Dead code removed:** functions and methods no longer used by any flow (including the entire old EasyOCR path).

---
---

# —— Bugfixes v2.1 ——
##  🇲🇽 ESPAÑOL

---

- **Conversor de Video:** Corregida la detección errónea de GPU al abrir el módulo (sincronización con la carga de IA).

- **Actualizaciones yt-dlp:** Resuelto el error que exigía permisos de administrador para actualizar la herramienta.

- **Flujo de descargas YT:** Auto-actualización de `yt-dlp` integrada con reintento automático en el mismo widget  conservando los ajustes originales.

## 🇺🇸 ENGLISH
---

- **Video Converter:** Fixed incorrect GPU detection upon opening the module (synchronized with AI loading).

- **yt-dlp Updates:** Resolved an issue that required administrator privileges to update the tool.

- **YT Downloads:** Integrated `yt-dlp` auto-updating with automatic retries within the same widget preserving original settings.

---
---

# —— Novedades v2.0 ——

---
---

# 🇲🇽 ESPAÑOL

---

## 📋 Resumen para el usuario

La versión 2.0 es la actualización más grande hasta ahora. La app abre más rápido, pesa menos y hace más: puedes transcribir y descargar playlists completas de YouTube, quitar fondos de imágenes en lote, elegir la calidad de tus audios y ver los metadatos escritos automáticamente en cada archivo. Las listas de PDFs e imágenes son más fáciles de organizar. La transición de arranque ya no parpadea, el compresor y el convertidor de imágenes muestran datos correctos para todos los formatos, y el renombrador ya no acepta caracteres que rompen los nombres de archivo en Windows.

---

## 🚀 Nuevas Funciones

### 1.- Arranque más rápido

La app ahora carga notablemente más rápido al abrirse:

- Las librerías pesadas (IA de transcripción, OCR, YouTube) se cargan en segundo plano mientras ya ves la ventana principal, en lugar de bloquear el splash.
- Cada módulo se construye solo la primera vez que lo abres, en lugar de cargar todos al arrancar.
- Los botones del menú que dependen de esas librerías muestran un ⏳ mientras cargan y se activan solos cuando están listos, evitando crashes si entrabas a un módulo demasiado rápido.

---

### 2.- Transcripción

#### — Nueva pestaña "YouTube → Texto"

Nueva pestaña entre "Archivos" y "En Vivo". Pega un enlace de YouTube (o de cualquier plataforma compatible) y la app descarga el audio, lo transcribe y guarda el resultado automáticamente. Sin pasos intermedios, sin archivos sueltos.

Incluye selector de modelo de IA, formato de salida (.txt / .srt / .vtt), carpeta de destino propia, switch de GPU independiente del tab de Archivos, y botón para abrir esa carpeta directamente.

**Soporte de listas de reproducción:** si el enlace pertenece a una playlist de YouTube, la app la detecta automáticamente, muestra cuántos videos contiene y pide confirmación antes de empezar. Cada video se transcribe en cascada y los archivos se organizan en una subcarpeta con el nombre de la playlist.

#### — Modelos descargados bajo demanda

Los modelos de faster-whisper ya no vienen empaquetados dentro del ejecutable. Ahora se descargan directamente desde HuggingFace la primera vez que los activas y quedan cacheados en tu equipo. **El resultado: el ejecutable es considerablemente más ligero.**

---

### 3.- YouTube Downloader

#### — Soporte de playlists

La descarga de video y audio ahora soporta listas de reproducción completas. Al pegar una URL de playlist, la app extrae todos los títulos, muestra un resumen y los descarga en cascada, uno por uno, con progreso individual por ítem.

#### — Metadatos en descargas de audio

Al descargar en formato MP3, M4A, OPUS, la app ahora incrusta automáticamente los metadatos del track directamente en el archivo: artista (o canal), título, año de publicación y álbum cuando está disponible. Los archivos quedan listos para cualquier reproductor o gestor de música sin necesidad de editarlos a mano.

#### — Selector de calidad de audio

El convertidor de audio de YouTube ahora incluye un selector de calidad. Puedes elegir entre mantener la calidad original o seleccionar un bitrate específico para balancear entre fidelidad y tamaño de archivo según lo que necesites.

#### — Nuevo formato WAV

Disponible junto a MP3, M4A y OPUS en las descargas de audio.

#### — Actualizador de yt-dlp integrado

Nuevo botón para actualizar yt-dlp sin salir de la app, con indicador de versión actual. Si una descarga falla por versión desactualizada, la actualización se lanza automáticamente.

---

### 4.- Imágenes

#### — Nueva pestaña "Remover Fondo"

Tercera pestaña en el módulo de imágenes. Usa el modelo u2net (vía `rembg`) para eliminar el fondo de una o varias imágenes en lote. Soporta arrastrar y soltar archivos, selector de carpeta de destino y procesamiento con sesión cacheada para no recargar el modelo en cada imagen.

#### — ICO mejorado

Al exportar a formato ICO ahora aparecen dos opciones nuevas: elegir el tamaño base (256, 128, 64, 48, 32, 24 o 16 px) y un checkbox para incluir todos los subtamaños menores dentro del mismo archivo. Antes se generaba un ICO de un solo tamaño que Windows no reconocía bien; ahora genera un ICO multiescala estándar compatible con Explorer, accesos directos y barra de tareas.

---

### 5.- Audio

#### — Selector de calidad / peso

El convertidor de audio ahora incluye un selector de calidad para ajustar el balance entre fidelidad y tamaño del archivo. Además de elegir el formato de salida, puedes optar por mantener la calidad original o generar audios más livianos con diferentes perfiles de compresión, ideal para ahorrar espacio sin perder control sobre el resultado final.

---

## 🛠️ Mejoras

### 1.- Transcripción

#### — Mejoras en "Archivos"

- **Botón "📂 Abrir Carpeta"** — abre directamente la carpeta donde se guardaron las transcripciones.
- **Más formatos al seleccionar archivos** — antes el selector solo mostraba MP3, WAV, M4A, MP4 y MKV. Ahora incluye FLAC, OGG, OPUS, WMA, AAC, AIFF y más, organizados en categorías: *Audio y Video*, *Solo Audio*, *Solo Video*.
- **Contador mejorado** — mientras procesa un lote, el contador muestra el nombre del archivo que está procesando, no solo el número.

---

### 2.- PDF

#### — Imagen a PDF

La lista de imágenes ahora tiene controles completos de reordenamiento: botones ⏫🔼🔽⏬ para mover al inicio, subir, bajar y mover al final (antes solo había "🗑 Eliminar"), y también se puede reordenar arrastrando los elementos directamente con el mouse.

#### — Unir PDFs

La lista de PDFs ahora también se puede reordenar arrastrando. Se añadieron los botones ⏫🔼🔽⏬ completos (antes solo había ▲▼ básicos) y un contador que muestra cuántos PDFs hay cargados.

#### — Compresor de PDF — Resumen de operación mejorado

El panel de resumen tras comprimir un PDF ahora muestra, además del porcentaje de reducción, el tamaño exacto del archivo antes y después de la compresión. Así puedes ver de un vistazo cuánto espacio se ganó en términos concretos, sin hacer cuentas.

---

### 3.- Ventana de Licencias

La ventana de créditos y licencias recibió una revisión interna. El scroll es ahora más fluido gracias a un sistema de debounce que evita el lag al pasar rápido por la lista, y el panel de detalles de cada librería se actualiza al pasar el cursor encima sin saltar ni parpadear.

---

## 🐛 Correcciones de Errores

### 1.- Transición Splash → Ventana Principal

Al abrir la app se producía un parpadeo brusco al cambiar del splash a la ventana principal: los elementos se reposicionaban de golpe y a veces se veía un destello blanco o un estado intermedio sin terminar de pintar.

Se reemplazó la transición abrupta por un sistema de doble fade: el splash se desvanece suavemente y, en el mismo momento en que llega a invisible, la ventana principal aparece desde transparente hasta opacidad completa. Ambas transiciones se encadenan sin hueco visible entre ellas.

---

### 2.- Convertidor de Audio — Error con archivos que contienen portada o metadatos

Al intentar convertir a formatos "raw" como WAV o MP3 sin metadatos (desde fuentes como M4A o FLAC con carátula incrustada), el convertidor lanzaba un error y abortaba el proceso. Se corrigió el pipeline de FFmpeg para que descarte correctamente los streams de imagen/portada al exportar a formatos que no los soportan, sin interrumpir la conversión.

---

### 3.- Compresor de Imágenes — Datos de compresión incorrectos en PNG, GIF, BMP y similares

Para formatos distintos de JPG y WebP, el compresor mostraba porcentajes de reducción poco realistas. Esto ocurría porque se aplicaba la misma lógica de estimación de peso que funciona para formatos con pérdida, pero que no es válida para formatos sin pérdida o con compresión diferente.

Se añadió manejo específico por tipo de archivo: para PNG, GIF, BMP y similares se calculan estimaciones realistas basadas en el tamaño real del resultado, y el resumen distingue claramente entre compresión con pérdida y sin pérdida.

---

### 4.- Convertidor de Imágenes — Error al convertir GIF animado a formato estático

Al convertir un GIF animado a PNG, JPG, TIFF u otro formato estático, la app producía un error o un resultado corrupto porque intentaba procesar todos los frames del GIF a la vez. Se corrigió extrayendo únicamente el frame 0 (el primero) antes de aplicar la conversión, produciendo siempre una imagen estática válida.

---

### 5.- Renombrador Masivo — Caracteres prohibidos en campos de texto

Los campos de Texto Base, Prefijo y Sufijo del renombrador aceptaban caracteres no válidos en nombres de archivo de Windows (`< > : " / \ | ? *`), lo que podía provocar errores al intentar renombrar. Se implementó un sistema de doble protección: un bloqueo a nivel de tecla que impide escribirlos directamente, y un filtro de limpieza silencioso que los elimina si llegan pegados desde el portapapeles.

---

### 6.- Scroll en la pestaña YouTube

El scroll de la cola de descargas de YouTube funcionaba de forma irregular: a veces se desplazaba en saltos bruscos o no respondía al estar el cursor sobre ciertos elementos de la fila. Se ajustó la sensibilidad del canvas (`yscrollincrement` de 4 → 2) y se corrigió el enrutamiento del evento de rueda del mouse para que funcione correctamente sin importar sobre qué parte de la fila esté el cursor.

---

### 7.- Scroll en el Renombrador

Se corrigió un error en los bindings de la rueda del mouse dentro de las filas virtuales del renombrador. La función `_child_mousewheel_wrapper` se redefinió como función local sin argumento `self` explícito, lo que eliminaba un `TypeError` silencioso que en ciertas situaciones impedía el scroll al hacer clic en etiquetas dentro de las filas.

---

### 8.- Scroll en Metadata Lab

El problema de rendimiento y renderizado en el scroll fue resuelto al reemplazar la arquitectura basada en CustomTkinter por una implementación nativa con Tkinter y Canvas. Esto eliminó la recreación constante de elementos, logrando un desplazamiento completamente fluido y sin artefactos visuales.

---

## ⚙️ Cambios Internos

- **Entorno de compilación actualizado:** el ejecutable ahora se construye con **Python 3.13.12** (antes 3.13.5). Este cambio trae correcciones de seguridad y estabilidad del intérprete sin impacto visible para el usuario.
- **`_transcribe_safe()`:** nuevo wrapper alrededor de la llamada a `WhisperModel.transcribe()` que captura excepciones inesperadas sin crashear el hilo de transcripción.
- **Carga por niveles (Tier 1 / Tier 2):** las librerías del startup se separaron en dos capas. Las esenciales bloquean mínimamente el splash; las pesadas (IA, YouTube) se delegan a `_cargar_tier2_background()` en un hilo separado, liberando la UI principal mucho antes.
- **Truncado de nombres en Metadata Lab por píxeles:** el recorte de nombres de archivo largos en la lista del Metadata Lab ahora mide el ancho real en píxeles usando `tkfont`, en lugar de contar caracteres. Los nombres se cortan exactamente antes del botón, igual que en el Explorador de Windows.

---
---
---
---

# 🇺🇸 ENGLISH

---

## 📋 User Summary

Version 2.0 is the biggest update so far. The app opens faster, weighs less and does more: you can transcribe and download full YouTube playlists, remove image backgrounds in batch, choose your audio quality and see metadata written automatically into every file. PDF and image lists are easier to organize. The startup transition no longer flickers, the image compressor and converter show correct data for all formats, and the renamer no longer accepts characters that break filenames on Windows.

---

## 🚀 New Features

### 1.- Faster Startup

The app now loads noticeably faster on launch:

- Heavy libraries (AI transcription, OCR, YouTube) load in the background while you already see the main window, instead of blocking the splash screen.
- Each module is built only the first time you open it, rather than loading everything at startup.
- Menu buttons that depend on those libraries show a ⏳ while loading and activate on their own when ready, preventing crashes if you navigated to a module too quickly.

---

### 2.- Transcription

#### — New "YouTube → Text" Tab

New tab between "Files" and "Live". Paste a YouTube link (or any supported platform) and the app downloads the audio, transcribes it and saves the result automatically. No intermediate steps, no leftover files.

Includes an AI model selector, output format (.txt / .srt / .vtt), its own destination folder, a GPU toggle independent from the Files tab, and a button to open that folder directly.

**Playlist support:** if the link belongs to a YouTube playlist, the app detects it automatically, shows how many videos it contains and asks for confirmation before starting. Each video is transcribed in sequence and the files are organized into a subfolder named after the playlist.

#### — On-demand Model Downloads

faster-whisper models are no longer bundled inside the executable. They are now downloaded directly from HuggingFace the first time you activate them and cached on your machine. **The result: a significantly lighter executable.**

---

### 3.- YouTube Downloader

#### — Playlist Support

Video and audio downloads now support full playlists. Paste a playlist URL and the app extracts all titles, shows a summary and downloads them in sequence, one by one, with individual progress per item.

#### — Audio Download Metadata

When downloading as MP3, M4A, or OPUS, the app now automatically embeds track metadata directly into the file: artist (or channel), title, publication year and album when available. Files are ready for any music player or manager without manual editing.

#### — Audio Quality Selector

The YouTube audio converter now includes a quality selector. You can choose between keeping the original quality or picking a specific bitrate to balance fidelity and file size as needed.

#### — New WAV Format

Available alongside MP3, M4A and OPUS in audio downloads.

#### — Built-in yt-dlp Updater

New button to update yt-dlp without leaving the app, with a current version indicator. If a download fails due to an outdated version, the update is launched automatically.

---

### 4.- Images

#### — New "Remove Background" Tab

Third tab in the Images module. Uses the u2net model (via `rembg`) to remove the background from one or several images in batch. Supports drag-and-drop, a destination folder picker, and processing with a cached session so the model is not reloaded for every image.

#### — Improved ICO Export

Exporting to ICO now offers two new options: choosing the base size (256, 128, 64, 48, 32, 24 or 16 px) and a checkbox to include all smaller sub-sizes within the same file. Previously, a single-size ICO was generated that Windows did not recognize well; now it generates a standard multi-scale ICO compatible with Explorer, shortcuts and the taskbar.

---

### 5.- Audio

#### — Quality / size selector

The audio converter now includes a quality selector to control the balance between fidelity and file size. In addition to choosing the output format, you can keep the original quality or generate lighter files with different compression profiles, making it easy to reduce size without losing control over the final result.

---

## 🛠️ Improvements

### 1.- Transcription

#### — "Files" Tab Improvements

- **"📂 Open Folder" button** — opens the folder where transcriptions were saved directly.
- **More file formats in the selector** — previously only MP3, WAV, M4A, MP4 and MKV were shown. Now includes FLAC, OGG, OPUS, WMA, AAC, AIFF and more, organized into categories: *Audio & Video*, *Audio Only*, *Video Only*.
- **Improved counter** — while processing a batch, the counter shows the name of the file being processed, not just the number.

---

### 2.- PDF

#### — Image to PDF

The image list now has full reordering controls: ⏫🔼🔽⏬ buttons to move to start, move up, move down, and move to end (previously only "🗑 Remove" was available), and items can also be reordered by dragging directly with the mouse.

#### — Merge PDFs

The PDF list can now also be reordered by dragging. Full ⏫🔼🔽⏬ buttons were added (previously only basic ▲▼ were available) and a counter showing how many PDFs are loaded.

#### — PDF Compressor — Improved Operation Summary

The summary panel after compressing a PDF now shows, in addition to the reduction percentage, the exact file size before and after compression. This lets you see at a glance how much space was saved in concrete terms, without any mental math.

---

### 3.- Licenses Window

The credits and licenses window received an internal overhaul. Scrolling is now smoother thanks to a debounce system that prevents lag when scrolling through the list quickly, and the detail panel for each library updates on hover without jumping or flickering.

---

## 🐛 Bug Fixes

### 1.- Splash → Main Window Transition

When opening the app, a jarring flash occurred when switching from the splash to the main window: elements repositioned abruptly and sometimes a white flash or an unfinished intermediate state was visible.

The abrupt transition was replaced with a double-fade system: the splash fades out smoothly and, at the exact moment it becomes invisible, the main window fades in from transparent to fully opaque. Both transitions are chained with no visible gap between them.

---

### 2.- Audio Converter — Error with Files Containing Cover Art or Metadata

When trying to convert to "raw" formats such as WAV or plain MP3 from sources like M4A or FLAC with embedded cover art, the converter threw an error and aborted the process. The FFmpeg pipeline was corrected to properly discard image/cover art streams when exporting to formats that do not support them, without interrupting the conversion.

---

### 3.- Image Compressor — Incorrect Compression Data for PNG, GIF, BMP and Similar

For formats other than JPG and WebP, the compressor displayed unrealistic reduction percentages. This happened because the same size estimation logic used for lossy formats was applied, which is not valid for lossless or differently compressed formats.

Format-specific handling was added: for PNG, GIF, BMP and similar, realistic estimates are calculated based on the actual output size, and the summary clearly distinguishes between lossy and lossless compression.

---

### 4.- Image Converter — Error When Converting Animated GIF to Static Format

When converting an animated GIF to PNG, JPG, TIFF or another static format, the app produced an error or a corrupted result because it tried to process all GIF frames at once. This was fixed by extracting only frame 0 (the first frame) before applying the conversion, always producing a valid static image.

---

### 5.- Mass Renamer — Forbidden Characters in Text Fields

The Base Text, Prefix and Suffix fields in the renamer accepted characters that are invalid in Windows filenames (`< > : " / \ | ? *`), which could cause errors when trying to rename. A double-protection system was implemented: a key-level block that prevents typing them directly, and a silent cleanup filter that strips them if they arrive via paste from the clipboard.

---

### 6.- Scroll in the YouTube Tab

The download queue scroll in the YouTube tab worked irregularly: it sometimes jumped in large steps or did not respond when the cursor was over certain row elements. Canvas sensitivity was adjusted (`yscrollincrement` from 4 → 2) and mouse wheel event routing was corrected to work correctly regardless of which part of the row the cursor is over.

---

### 7.- Scroll in the Renamer

A bug was fixed in the mouse wheel bindings inside the renamer's virtual rows. The `_child_mousewheel_wrapper` function was redefined as a local function without an explicit `self` argument, which was silently eliminating a `TypeError` that in certain situations prevented scrolling when clicking on labels inside the rows.

---

### 8.- Scroll in Metadata Lab

The performance and rendering issues in the scrolling system were resolved by replacing the architecture based on CustomTkinter with a native implementation using Tkinter and Canvas. This eliminated constant element re-creation, resulting in smooth scrolling and no visual artifacts.

---

## ⚙️ Internal Changes

- **Updated build environment:** the executable is now built with **Python 3.13.12** (previously 3.13.5). This brings interpreter security and stability fixes with no visible impact for the user.
- **`_transcribe_safe()`:** new wrapper around the `WhisperModel.transcribe()` call that captures unexpected exceptions without crashing the transcription thread.
- **Tiered loading (Tier 1 / Tier 2):** startup libraries were split into two layers. Essential ones minimally block the splash; heavy ones (AI, YouTube) are delegated to `_cargar_tier2_background()` in a separate thread, freeing the main UI much sooner.
- **Metadata Lab pixel-accurate filename truncation:** long filename truncation in the Metadata Lab list now measures real pixel width using `tkfont`, instead of counting characters. Names are cut exactly before the button, just like in Windows Explorer.

---
