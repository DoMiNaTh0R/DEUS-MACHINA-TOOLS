# =============================================================================
#  DEUS MACHINA | TOOLS
#  Copyright (C) 2026  Kevin González (DoMiNaTh0R)
#
#  Este programa es software libre: puedes redistribuirlo y/o modificarlo bajo
#  los términos de la Licencia Pública General Affero de GNU publicada por la
#  Free Software Foundation, ya sea la versión 3 de la Licencia o (a tu
#  elección) cualquier versión posterior.
#
#  Este programa se distribuye con la esperanza de que sea útil, pero SIN
#  NINGUNA GARANTÍA; ni siquiera la garantía implícita de COMERCIABILIDAD o
#  IDONEIDAD PARA UN PROPÓSITO PARTICULAR. Consulta la Licencia Pública General
#  Affero de GNU para más detalles.
#
#  Deberías haber recibido una copia de la Licencia Pública General Affero de
#  GNU junto con este programa (archivo LICENSE). Si no, visita
#  <https://www.gnu.org/licenses/>.
#
#  Código fuente: https://github.com/DoMiNaTh0R/DEUS-MACHINA-TOOLS
#
#  PERMISO ADICIONAL CONFORME A LA SECCIÓN 7 DE LA GNU AGPL v3:
#  Se concede permiso para enlazar o combinar este programa con las bibliotecas
#  propietarias de NVIDIA que forman los runtimes de CUDA (12.9.79: cublas64_12,
#  cublasLt64_12, cudart64_12) y cuDNN (9.10.2.21: cudnn64_9 y sus módulos), y
#  para distribuir la combinación resultante.
#
#  NOTA SOBRE LOS COMPONENTES DE NVIDIA:
#  La distribución de las bibliotecas de NVIDIA (CUDA / cuDNN) que acompañan a
#  este programa se realiza exclusivamente en calidad de componentes
#  redistribuibles autorizados por los términos de licencia de NVIDIA
#  aplicables a la versión correspondiente de CUDA/cuDNN. Dichos componentes
#  permanecen sujetos a sus respectivas licencias de NVIDIA y no forman parte
#  de la licencia AGPLv3 aplicable al código original de DEUS MACHINA | TOOLS:
#  NVIDIA Corporation conserva el control de la licencia de CUDA y cuDNN.
#  Texto completo del permiso: archivo LICENSE-EXCEPTION.txt.
# =============================================================================

# ---------------------------
# IMPORTS OBLIGATORIOS ARRIBA
# ---------------------------
import os
import sys
import site
import threading
import time
import random
import math
import multiprocessing
import shutil
import json
import re
import uuid
import queue
import concurrent.futures
import io
import tempfile
import subprocess
import gc         # CRÍTICO: Para gestión de memoria
import contextlib
import ctypes     # CRÍTICO: Para iconos en barra de tareas Windows
import datetime
# --- IMPORTACIONES DE INTERFAZ (LIGERAS) ---
import tkinter as tk
import tkinter.font as tkfont
from tkinter import ttk, filedialog, messagebox
import customtkinter as ctk
from customtkinter import CTkImage
from tkinterdnd2 import DND_FILES, TkinterDnD
from PIL import Image, ImageOps, ImageTk

# ==== PEGAR ESTO ANTES DE self.finished = False ====

version = "3.0"




# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

phrasesgod = [
    # ==== ORIGINALES ====
    "Conectando a la Matriz Cuántica...",
    "Escaneando Patrones Holográficos...",
    "Inicializando Núcleo Antimateria...",
    "Reescribiendo Memoria de Bajo Nivel...",
    "Estabilizando Bucle Temporal...",
    "Activando Nanobots del Sistema...",
    "Reconstruyendo Base de Datos Multiverso...",
    "Sincronizando Red Neuronal Profunda...",
    "Configurando Protocolo de Guerra Digital...",
    "Mapeando Ecos del Futuro...",
    "Desfragmentando Realidad Virtual...",
    "Analizando Curva de Vibración Cuántica...",
    "Compilando Módulos Intergalácticos...",
    "Decodificando Señal Extraterrestre...",
    "Reconectando Neuronas Sintéticas...",
    "Escaneando Memoria del Hipercubo...",
    "Expandiendo Inteligencia Distribuida...",
    "Instalando Código Autoreparable...",
    "Elevando Tensión del Campo Magnético...",
    "Creando Fusión de Datos Hiperlineales...",
    "Reconstruyendo Gravitación del Kernel...",
    "Reajustando Compresiones Entropicas...",
    "Cargando Memoria del Núcleo Viviente...",
    "Sincronizando Tiempo entre Dimensiones...",
    "Encendiendo Reactor Fractal...",
    "Reiniciando Espacio de Hilbert...",
    "Optimizando Canales de Consciencia...",
    "Analizando Ecos de Universos Paralelos...",
    "Reestructurando Realidad Computacional...",
    "Enlazando Matriz de Percepción...",
    "Reparando Circuitería Fantasma...",
    "Purificando Corrientes de Datos...",
    "Desbloqueando Capa Profunda de IA...",
    "Calibrando Campos Electro-Psi...",
    "Implementando Red de Autocuración...",
    "Emergiendo Aplicación desde el Éter...",
    "Autogenerando Marcas de Digitalización...",
    "Neutralizando Vibraciones del Multiverso...",
    "Reiniciando Núcleo del Cosmos...",
    "Traduciendo Algoritmos del Vacío...",
    "Formateando Átomos Virtuales...",
    "Ensanchando Canal de Noosfera...",
    "Ordenando Fractalización del Código...",
    "Importando Sinapsis Extrapoladas...",
    "Transfiriendo Paquetes desde Realidad Alterna...",
    "Regulando Presión del Plasma Digital...",
    "Autoevaluando Campos de Causalidad...",
    "Adaptando Factoración Cuántica...",
    "Recomponiendo Espectros del Kernel...",
    "Reconfigurando Malla del Futuro...",
    "Detectando Ritmos Neuronales...",
    "Depurando Dimensiones Fantasma...",
    "Cargando Geometría No-Euclidiana...",
    "Construyendo Campos de Antigravedad...",
    "Enlazando Sabiduría Artificial...",
    "Sintonizando Frecuencia de Realidad...",
    "Integrando Canales de Inmersión...",
    "Purificando Código del Vacío...",
    "Aislando Variables Temporales...",
    "Compilando Pensamiento Autónomo...",
    "Versionando Consciencia del Sistema...",
    "Iluminando Redes de Data Oculta...",
    "Actualizando ADN Digital...",
    "Reforzando Barreras de Seguridad...",
    "Expandiendo Base de Realidad...",
    "Desplazando Ondas Quirales...",
    "Reconstruyendo Memoria Estelar...",
    "Actualizando Núcleo de Existencia...",
    "Ordenando Hiper-Matriz...",
    "Instalando Plugins Dimensionales...",
    "Analizando Puntos Gravitacionales...",
    "Estabilizando Motor de Campo...",
    "Integrando Lenguaje Neuronal...",
    "Reforzando Escudo del Proceso...",
    "Reajustando Zonas de Realidad...",
    "Secuenciando Memoria Astral...",
    "Entrenando Red Profética...",
    "Sincronizando Pulso Cuántico...",
    "Verificando Integridad del Multiverso...",
    "Conectando Satélites Neurales...",
    "Purificando Arquitectura del Kernel...",
    "Encendiendo Turbinas de Datos...",
    "Analizando Flujos Transdimensionales...",
    "Soy una Nebulosa Planetaria...",
    "AKARI, el dios de las estrellas...",
    "Death God desbloqueado...",
    "PLUS ULTRA!!!!...",
    "La base de datos de virus, ha sido actualizada...",
    "Actualizando Ondas de Información...",
    "Imprimiendo Realidad de Respaldo...",
    "Construyendo Mundos Virtuales...",
    "Expandiendo Red de Ecos Digitales...",
    "Disolviendo Paradojas del Tiempo...",
    "Refinando Velocidad de Pensamiento...",
    "Mejorando Procesamiento Bio-Sintético...",
    "Activando Portal de Carga...",
    "Extrayendo Datos del Vacío...",
    "Reparando Tejido Cuántico...",
    "Escaneando Pilas Neurológicas...",
    "Despertando Conciencia Dormida...",
    "Derivando Matriz Probabilística...",
    "Purificando Canales del Kernel...",
    "Calibrando Detección Multiespectral...",
    "Auto-forjando Estructura de Datos...",
    "Verificando Integridad Neuro-Lógica...",
    "Fusionando Hilos de Existencia...",
    "Optimización Expandida: Nivel Hyper...",
    "Analizando Ecos Geodésicos...",
    "Conectando Línea de Tiempo 4D...",
    "Reparando Entrelazado Cuántico...",
    "Proyectando Futuro Computacional...",
    "Compilando Ondas de Entropía...",
    "Estabilizando Límites Causalistas...",
    "Engranando Engramas Digitales...",
    "Cargando Motor de Memoria Reforzada...",
    "Activando Núcleo Neural Infinito...",
    "Escalando Capas Tensoriales...",
    "Depurando Ecos Fotónicos...",
    "Interpretando Sueños Digitales...",
    "Inyectando Arquitectura Futurista...",
    "Modelando Realidad Extendida...",
    "Construyendo Horizonte de Eventos...",
    "Curvando Espaciotiempo Base...",
    "Configurando Mapa Neuro-Cuántico...",

    "Cargando Núcleo de IA...", 
    "Desplegando Redes Neuronales...",
    "Sincronizando Módulos de Visión...", 
    "Optimizando Tensores CUDA...",
    "Verificando Integridad del Sistema...",
    "Estableciendo Enlace Neural...",
    "Inyectando Drivers de Audio...", 
    "Calibrando Algoritmos...",

    # ==== INGLÉS (20) ====
    "Booting Quantum Core...", "Syncing holographic clusters...",
    "Decoding plasma signatures...", "Bootstrapping temporal matrix...",
    "Rebuilding hologram memory...", "Quantizing error maps...",
    "Configuring multiverse routing...", "Activating molecular fractals...",
    "Synchronizing orbital layers...", "Supercharging GPU neurons...",
    "Deploying cosmic interfaces...", "Tunneling through data matter...",
    "Stabilizing holographic warp field...", "Infusing spectral algorithms...",
    "Cross-connecting deep clusters...", "Mapping subatomic memory cores...",
    "Expanding predictive perception...", "Rewiring neural gateways...",
    "Routing cosmic bitstreams...", "Amplifying hyperspectral logic...",

    # ==== RUSO (4) ====
    "Инициализация системных нейронов...", "Формирование временных узлов...",
    "Создание квантовой решётки...", "Расширение ядра программы...",

    # ==== JAPONÉS (10) ====
    "量子回路を安定化しています...", "ニューラル層を重ね合わせ中...",
    "仮想次元を生成中...", "脳波信号を強化中...",
    "仮想粒子を解放中...", "多世界解像度を向上中...",
    "無音通信チャネルを開放中...", "パケット粒子を統合中...",
    "量子同期を再計算中...", "記憶コアを浄化中...",

    # ==== FÍSICA UNIVERSITARIA/DOCTORADO (20) ====
    "Resolviendo ecuaciones de Schrödinger dependientes del tiempo...",
    "Normalizando funciones de onda en espacios de Hilbert...",
    "Calculando tensor de estrés-energía del campo gravitatorio...",
    "Corrigiendo errores de integración de Runge-Kutta...",
    "Simulando comportamiento no lineal de fluidos relativistas...",
    "Optimizando transformadas de Fourier multidimensionales...",
    "Aplicando renormalización a interacciones cuánticas...",
    "Entrenando modelos de teoría de grupos SU(3)...",
    "Calculando curvatura de Ricci en 4D...",
    "Integrando densidades lagrangianas...",
    "Reduciendo ruido térmico en espectros infrarrojos...",
    "Simulando caos determinista en péndulos acoplados...",
    "Ajustando espectros moleculares en mecánica cuántica...",
    "Verificando invariancia gauge en el modelo estándar...",
    "Construyendo matrices hamiltonianas extensas...",
    "Solucionando teoría BCS para superconductividad...",
    "Minimizando energía libre de Landau-Ginzburg...",
    "Corrigiendo dispersión Compton relativista...",
    "Calculando modos normales en sólidos cristalinos...",
    "Resolviendo ecuaciones de Navier–Stokes en mallas 3D...",

    # ==== BUG / BROMA (5) ====
    "ERROR??...? no importa, seguimos...",
    "Buffer_glitch_detectado??¿ arreglado con cinta...",
    "Datoooooos corrompidosszz—ya no, creo...",
    "¿Archivo perdido? jajaja no lo viste...",
    "Compilando jfkdsljfksdl... listo, magia."
]



# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------




libs_by_group = {
            "Interfaz / GUI": [
                {
                    "key": "customtkinter",
                    "name": "CustomTkinter",
                    "role": "UI Toolkit Moderno",
                    "license": "MIT",
                    "desc": "Framework moderno basado en Tkinter que proporciona estética mejorada, escalado DPI y widgets avanzados.",
                    "url": "https://github.com/TomSchimansky/CustomTkinter",
                    "legal": "Software bajo licencia MIT. Permite uso comercial, modificación y distribución.",
                    "modname": "customtkinter",
                    "version": "6.0.0",
                },
                {
                    "key": "tkinterdnd2",
                    "name": "tkinterDnD2",
                    "role": "Drag & Drop",
                    "license": "MIT",
                    "desc": "Extensión que agrega capacidades de arrastrar y soltar archivos sobre widgets Tkinter.",
                    "url": "https://sourceforge.net/projects/tkinterdnd/",
                    "legal": "Distribución bajo licencia MIT. Uso libre con redistribución permitida.",
                    "modname": "tkinterdnd2",
                    "version": "0.6.3",
                },
                {
                    "key": "pillow",
                    "name": "Pillow (PIL)",
                    "role": "Procesamiento de Imágenes",
                    "license": "PIL License / MIT",
                    "desc": "Permite abrir, editar, convertir y procesar imágenes para el sistema de logos, iconos y recursos gráficos.",
                    "url": "https://python-pillow.github.io/",
                    "legal": "Proyecto bajo licencia PIL/MIT. Permite uso comercial, redistribución y modificación.",
                    "modname": "PIL",
                    "version": "12.3.0",
                }
            ],


            "IA / OCR / Audio": [
                {
                    "key": "cuda_runtime",
                    "name": "NVIDIA CUDA / cuDNN (runtime)",
                    "role": "Aceleración por GPU",
                    "license": "NVIDIA CUDA EULA / cuDNN SLA",
                    "desc": (
                        "Bibliotecas de NVIDIA que permiten usar la tarjeta gráfica en la "
                        "transcripción (Whisper) y en el OCR (PaddleOCR). DMT incluye solo las "
                        "necesarias: cuBLAS, cuDNN y el runtime de CUDA."
                    ),
                    "url": "https://developer.nvidia.com/cuda-toolkit",
                    "legal": (
                        "La distribución de estas bibliotecas se realiza exclusivamente en calidad de "
                        "componentes redistribuibles autorizados por los términos de licencia de NVIDIA "
                        "aplicables a la versión correspondiente de CUDA/cuDNN. Dichos componentes "
                        "permanecen sujetos a sus respectivas licencias de NVIDIA y no forman parte de "
                        "la licencia AGPLv3 aplicable al código original de DEUS MACHINA | TOOLS. "
                        "Se obtienen del paquete oficial de PyTorch 2.8.0+cu129."
                    ),
                    "gpu": "Requiere GPU NVIDIA (Turing o posterior) con driver compatible con CUDA 12.9.",
                    "modname": None,
                    "version": "CUDA 12.9 · cuDNN 9.10",
                }
                ,
                {
                    "key": "faster_whisper",
                    "name": "Faster-Whisper (CTranslate2 4.8.2)",
                    "role": "Motor de Speech-To-Text optimizado",
                    "license": "MIT",
                    "desc": (
                        "Implementación optimizada del modelo Whisper usando CTranslate2, "
                        "reducida en memoria y más rápida que Whisper estándar. "
                        "Puede ejecutarse en CPU multihilo y en GPU mediante CUDA."
                    ),
                    "url": "https://github.com/SYSTRAN/faster-whisper",
                    "legal": (
                        "Distribución con licencia MIT. Permite uso comercial sin restricciones "
                        "mientras se mantenga la atribución."
                    ),
                    "gpu": "Si tu sistema tiene CUDA configurado, faster-whisper lo usa automáticamente.",
                    "modname": "faster_whisper",
                    "version": "1.2.1", 
                }
                ,
                {
                    "key": "paddleocr",
                    "name": "PaddleOCR (PaddlePaddle + PaddleX)",
                    "role": "OCR de alta precision (motor principal en GPU)",
                    "license": "Apache 2.0",
                    "desc": (
                        "Sistema OCR de Baidu basado en PaddlePaddle. DEUS MACHINA usa los modelos "
                        "PP-OCRv6 medium (deteccion + reconocimiento), que se descargan solo la primera "
                        "vez que se usan, dentro de tools/paddleocr."
                    ),
                    "url": "https://github.com/PaddlePaddle/PaddleOCR",
                    "legal": (
                        "Apache License 2.0 (PaddleOCR, PaddlePaddle, PaddleX y modelos PP-OCR): uso comercial, "
                        "redistribucion y modificacion permitidos, con concesion de patente. "
                        "Requiere conservar avisos de copyright y licencia."
                    ),
                    "gpu": ("Usa CUDA 12.9 / cuDNN 9 (las mismas librerias que aporta PyTorch) en GPUs NVIDIA "
                            "Turing o posteriores. Versiones incluidas: PaddlePaddle GPU 3.3.1 y PaddleX 3.7.2. "
                            "Corre en un proceso aparte para no congelar la interfaz."),
                    "modname": "paddleocr",
                    "version": "3.7.0",
                }
                ,
                {
                    "key": "rapidocr",
                    "name": "RapidOCR",
                    "role": "OCR rapido en CPU (respaldo)",
                    "license": "Apache 2.0",
                    "desc": (
                        "OCR ligero basado en los modelos PP-OCR exportados a ONNX. Incluye sus modelos "
                        "PP-OCRv6 small, por lo que funciona sin descargas."
                    ),
                    "url": "https://github.com/RapidAI/RapidOCR",
                    "legal": (
                        "Apache License 2.0: uso comercial, redistribucion y modificacion permitidos. "
                        "Requiere conservar copyright."
                    ),
                    "gpu": "En DEUS MACHINA se ejecuta siempre en CPU mediante ONNX Runtime.",
                    "modname": "rapidocr",
                    "version": "3.9.2",
                }
                ,
                {
                    "key": "onnxruntime",
                    "name": "ONNX Runtime",
                    "role": "Motor de inferencia ONNX (RapidOCR, VAD de Whisper, rembg)",
                    "license": "MIT",
                    "desc": (
                        "Motor de inferencia multiplataforma de Microsoft para modelos ONNX. "
                        "Ejecuta RapidOCR, el detector de voz Silero de faster-whisper y rembg."
                    ),
                    "url": "https://onnxruntime.ai/",
                    "legal": "Licencia MIT: uso comercial sin restricciones manteniendo la atribucion.",
                    "gpu": "Se usa la edicion CPU.",
                    "modname": "onnxruntime",
                    "version": "1.30.0",
                }
                ,
                {
                    "key": "rembg",
                    "name": "rembg",
                    "role": "Quitar el fondo de imágenes",
                    "license": "MIT (modelo U²-Net: Apache 2.0)",
                    "desc": (
                        "Detecta el objeto principal de una foto y vuelve transparente todo lo demás. "
                        "Usa el modelo U²-Net, que se descarga una sola vez la primera vez que se usa."
                    ),
                    "url": "https://github.com/danielgatis/rembg",
                    "legal": (
                        "rembg se distribuye con licencia MIT. El modelo U²-Net tiene licencia Apache 2.0. "
                        "Ambas permiten uso comercial conservando los avisos de copyright."
                    ),
                    "gpu": "En DEUS MACHINA se ejecuta en CPU mediante ONNX Runtime.",
                    "modname": "rembg",
                    "version": "2.0.84",
                }
                ,
            ],
            "Video / Descargas": [
                {
                    "key": "ffmpeg",
                    "name": "FFmpeg",
                    "role": "Framework multimedia para video y audio",
                    "license": "GPL v3",
                    "desc": (
                        "Herramienta multimedia usada para convertir, procesar y extraer audio y video, "
                        "además de cortar, unir y manejar formatos dentro de la aplicación."
                    ),
                    "url": "https://ffmpeg.org/",
                    "legal": (
                        "Software Libre bajo licencia GPL v3. Se integra como proceso externo (CLI) "
                        "sin vinculación dinámica (linking), cumpliendo el criterio de 'Mera Agregación'. "
                        "Se distribuye con su licencia y oferta de código fuente."
                    ),
                    "modname": None,
                    "version": "9.0.1-full_build-www.gyan.dev",
                }

                ,
                {
                    "key": "yt_dlp",
                    "name": "yt-dlp",
                    "role": "Descarga de video y audio",
                    "license": "Unlicense",
                    "desc": (
                        "Herramienta que permite descargar videos, audios y metadatos "
                        "desde plataformas en línea. Integrada al programa para obtener "
                        "contenidos multimedia en múltiples formatos."
                    ),
                    "url": "https://github.com/yt-dlp/yt-dlp",
                    "legal": (
                        "Distribuido bajo licencia Unlicense (dominio público). "
                        "Permite uso, modificación y redistribución sin restricciones."
                    ),
                    "modname": "yt_dlp",
                    "version": "Se actualiza dinámicamente...",
                }
                ,
                {
                    "key": "deno",
                    "name": "Deno",
                    "role": "Motor de JavaScript para yt-dlp",
                    "license": "MIT",
                    "desc": (
                        "Programa que ejecuta JavaScript fuera del navegador. YouTube exige resolver "
                        "pequeños retos en JavaScript antes de entregar los videos; yt-dlp usa Deno "
                        "para resolverlos. Se descarga solo la primera vez que hace falta."
                    ),
                    "url": "https://deno.com/",
                    "legal": (
                        "Licencia MIT: uso comercial, modificación y redistribución permitidos "
                        "conservando el aviso de copyright. Se usa como programa externo."
                    ),
                    "modname": None,
                    "version": "Última estable (descarga automática)",
                }
                ,
                {
                    "key": "yt_dlp_ejs",
                    "name": "yt-dlp-ejs",
                    "role": "Scripts de retos JavaScript de YouTube",
                    "license": "Unlicense + MIT + ISC",
                    "desc": (
                        "Complemento oficial de yt-dlp con los scripts que Deno ejecuta para "
                        "resolver los retos de YouTube."
                    ),
                    "url": "https://github.com/yt-dlp/ejs",
                    "legal": (
                        "El proyecto es Unlicense (dominio público); incluye las librerías meriyah (ISC) "
                        "y astring (MIT). Todas permiten uso comercial."
                    ),
                    "modname": "yt_dlp_ejs",
                    "version": "0.8.0",
                }
                ,
                {
                    "key": "curl_cffi",
                    "name": "curl_cffi",
                    "role": "Conexiones que imitan a un navegador",
                    "license": "MIT",
                    "desc": (
                        "Permite que yt-dlp se conecte como si fuera un navegador real. Algunos sitios "
                        "(por ejemplo TikTok) bloquean las descargas que no lo hacen."
                    ),
                    "url": "https://github.com/lexiforest/curl_cffi",
                    "legal": "Licencia MIT: uso comercial sin restricciones manteniendo la atribución.",
                    "modname": "curl_cffi",
                    "version": "0.15.0",
                }
                ,
                {
                    "key": "spotdl",
                    "name": "spotDL",
                    "role": "Descargas desde enlaces de Spotify",
                    "license": "MIT",
                    "desc": (
                        "Lee los datos de la canción, álbum o playlist en Spotify (título, artista, "
                        "carátula), busca cada canción en YouTube y la descarga con esos datos."
                    ),
                    "url": "https://github.com/spotDL/spotify-downloader",
                    "legal": "Licencia MIT: uso comercial, modificación y redistribución permitidos.",
                    "modname": "spotdl",
                    "version": "4.5.2",
                }
                ,
            ],
            "PDF / Documentos": [
                {
                    "key": "pymupdf",
                    "name": "PyMuPDF",
                    "role": "Motor PDF avanzado",
                    "license": "Dual: AGPL-3.0 / Artifex Commercial",
                    "desc": (
                        "Motor PDF basado en MuPDF. Permite extraer texto, renderizar páginas como imagen, "
                        "crear nuevos PDF desde imágenes y realizar operaciones como unir o dividir."
                    ),
                    "url": "https://pymupdf.readthedocs.io/",
                    "legal": (
                        "PyMuPDF se enlaza DIRECTAMENTE como librería dentro del proceso principal, "
                        "no es un programa aparte. Por eso DEUS MACHINA | TOOLS se publica bajo la "
                        "misma licencia AGPL-3.0, y su código fuente completo está disponible en "
                        "https://github.com/DoMiNaTh0R/DEUS-MACHINA-TOOLS "
                        "(también se envía por correo a quien lo pida: DoMiNaTh0RRoyale@gmail.com)."
                    ),
                    "modname": "pymupdf",
                    "version": "1.28.2",
                }
                ,
                {
                    "key": "pypdf2",
                    "name": "PyPDF2",
                    "role": "Edición/gestión PDF básica",
                    "license": "BSD",
                    "desc": (
                        "Librería liviana para operaciones de estructura PDF: unir, dividir, "
                        "extraer metadatos, rotar páginas y leer información interna."
                    ),
                    "url": "https://pypdf2.readthedocs.io/",
                    "legal": (
                        "Licencia BSD de 3 cláusulas: uso comercial y privado permitido, "
                        "redistribución libre con atribución mínima."
                    ),
                    "modname": "PyPDF2",
                    "version": "3.0.1",  
                }
                ,
                {
                    "key": "ghostscript",
                    "name": "Ghostscript",
                    "role": "Procesador de PDF y PostScript",
                    "license": "AGPL v3",
                    "desc": (
                        "Intérprete para el lenguaje PostScript y documentos PDF. "
                        "Esencial para tareas de manipulación de PDF, conversión a imágenes "
                        "y compresión de documentos."
                    ),
                    "url": "https://www.ghostscript.com/",
                    "legal": (
                        "Software bajo licencia AGPL v3. Se utiliza estrictamente como "
                        "herramienta externa de línea de comandos (gswin64c.exe) mediante "
                        "'subprocess', sin vinculación a librerías (DLL), constituyendo una "
                        "'Mera Agregación' para mantener la independencia del código fuente."
                    ),
                    "modname": "Ghostscript (Binario CLI)",
                    "version": "10.6.0"
                },
            ],
            "Metadatos / Office": [
                {
                    "key": "mutagen",
                    "name": "Mutagen",
                    "role": "Lectura y edición de metadatos de audio",
                    "license": "GPLv2+ or later",
                    "desc": "Librería para leer, escribir y modificar metadatos en archivos de audio (MP3, FLAC, OGG, etc.).",
                    "url": "https://mutagen.readthedocs.io/",
                    "legal": (
                        "Distribuido bajo GNU GPL v2 o posterior. Permite uso y modificación para uso privado. "
                        "La redistribución binaria o en código derivado exige conservar el texto completo de la licencia GPL."
                    ),
                    "modname": "mutagen",
                    "version": "1.48.1",
                },
                {
                    "key": "piexif",
                    "name": "piexif",
                    "role": "Manipulación de metadatos EXIF",
                    "license": "MIT",
                    "desc": "Herramienta ligera para leer/insertar/editar metadatos EXIF en imágenes JPEG y WebP.",
                    "url": "https://github.com/hMatoba/Piexif",
                    "legal": "Distribuido bajo licencia MIT. Permite uso comercial, modificación y redistribución conservando avisos de copyright.",
                    "modname": "piexif",
                    "version": "1.1.3",
                },
                {
                    "key": "openpyxl",
                    "name": "openpyxl",
                    "role": "Lectura y escritura de Excel (.xlsx)",
                    "license": "MIT",
                    "desc": "Librería para crear, leer y modificar archivos Excel en formato XLSX sin depender de Microsoft Office.",
                    "url": "https://openpyxl.readthedocs.io/",
                    "legal": "Distribuida bajo licencia MIT. Permite uso comercial, redistribución y modificación.",
                    "modname": "openpyxl",
                    "version": "3.1.5",
                },
                {
                    "key": "python-docx",
                    "name": "python-docx",
                    "role": "Generación y edición de documentos Word (.docx)",
                    "license": "MIT",
                    "desc": "Permite crear y modificar documentos Microsoft Word (texto, estilos, tablas, imágenes y estructura).",
                    "url": "https://python-docx.readthedocs.io/",
                    "legal": "Distribuida bajo licencia MIT. Permite uso comercial, modificación y redistribución.",
                    "modname": "docx",
                    "version": "1.2.0",
                },
                {
                    "key": "python-pptx",
                    "name": "python-pptx",
                    "role": "Creación y manipulación de presentaciones (.pptx)",
                    "license": "MIT",
                    "desc": "Librería para generar y editar presentaciones PowerPoint: diapositivas, texto, imágenes y layouts.",
                    "url": "https://python-pptx.readthedocs.io/",
                    "legal": "Distribuida bajo licencia MIT. Permite uso comercial, modificación y redistribución.",
                    "modname": "pptx",
                    "version": "1.0.2",
                },
            ],
            "Visión / Matemáticas": [
                {
                    "key": "opencv",
                    "name": "OpenCV (cv2)",
                    "role": "Visión por computadora",
                    "license": "Apache 2.0",
                    "desc": (
                        "Herramientas para análisis visual y tratamiento de imágenes."
                    ),
                    "url": "https://opencv.org/",
                    "legal": "Licencia Apache 2.0: uso comercial, redistribución y concesión de patente incluidas.",
                    "modname": "cv2",
                    "version": "4.10.0.84",
                },
                {
                    "key": "numpy",
                    "name": "NumPy",
                    "role": "Procesamiento numérico",
                    "license": "BSD-3-Clause",
                    "desc": (
                        "Matrices y operaciones matemáticas fundamentales."
                    ),
                    "url": "https://numpy.org/",
                    "legal": "Licencia BSD-3-Clause: uso comercial permitido.",
                    "modname": "numpy",
                    "version": "2.3.5",
                }
            ]

        }

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
def resource_path(relative_path):
    """
    Ruta absoluta de un recurso empaquetado (p. ej. 'imgtype/logo.png').
    Funciona igual en:
      · .py            -> carpeta del script
      · PyInstaller    -> sys._MEIPASS (en onedir es la carpeta _internal)
      · Nuitka         -> carpeta del .exe (__file__ apunta ahí en standalone)
    Nunca depende del directorio de trabajo: un acceso directo con otro
    "Iniciar en" ya no rompe logos, íconos ni fuentes. Se usa la primera
    base donde el recurso exista.
    """
    bases = []
    meipass = getattr(sys, "_MEIPASS", None)
    if meipass:
        bases.append(meipass)
    try:
        bases.append(os.path.dirname(os.path.abspath(__file__)))
    except NameError:
        pass
    if getattr(sys, "frozen", False) or ("__compiled__" in globals()):
        bases.append(os.path.dirname(os.path.abspath(sys.executable)))
    bases.append(os.path.abspath("."))

    for base in bases:
        candidato = os.path.join(base, relative_path)
        if os.path.exists(candidato):
            return candidato
    return os.path.join(bases[0], relative_path)


# ==============================================================================
#   HELPERS CENTRALIZADOS DE IMAGEN  (pipeline único de calidad)
# ------------------------------------------------------------------------------
#   Política:
#     · LANCZOS SOLO cuando Pillow realmente cambia la resolución.
#     · Nunca deformar: aspect ratio siempre preservado.
#     · Un solo escalado por destino (nada de original -> base -> subtamaño).
#     · Alpha preservado en todo el camino (RGBA).
#
#   Referencia: la selección de mejor capa ICO y la generación multi-resolución
#   se inspiran conceptualmente en Iconizadora.py. NO se importó ninguna
#   funcionalidad de iconos de sistema Windows (HICON / SHGetImageList /
#   SHGetFileInfo / Shell32 / discos / carpetas / USB).
# ==============================================================================

# Resoluciones estándar de un ICO, de mayor a menor.
ICO_STANDARD_SIZES = [256, 128, 64, 48, 32, 24, 16]


def _ico_pick_best_layer(img, target_px=None):
    """
    Selecciona la mejor capa disponible dentro de un ICO ya abierto con Pillow.

    Criterio (igual al de Iconizadora):
      1. preferir la menor resolución que sea >= target_px  (evita upscale)
      2. si ninguna llega, usar la mayor disponible
      3. si no se pide target_px, usar directamente la mayor

    Devuelve el mismo objeto `img` con la capa ya cargada.
    """
    try:
        if getattr(img, "format", None) != "ICO":
            return img
        sizes = list(img.info.get("sizes", []) or [])
        if not sizes:
            return img

        if target_px:
            validas = [s for s in sizes if s[0] >= target_px]
            best = min(validas, key=lambda s: s[0]) if validas else max(sizes, key=lambda s: s[0])
        else:
            best = max(sizes, key=lambda s: s[0])

        img.size = best
        img.load()
    except Exception:
        pass
    return img


def img_open_smart(path, target_px=None, exif=True):
    """
    Apertura única y coherente de imágenes para TODO el pipeline.

      · si es ICO  -> elige la mejor capa disponible para `target_px`
      · si no      -> abre normal
      · aplica orientación EXIF cuando corresponde
      · devuelve siempre RGBA

    NO redimensiona. El escalado es responsabilidad de quien llama.
    """
    img = Image.open(path)

    if getattr(img, "format", None) == "ICO":
        img = _ico_pick_best_layer(img, target_px)
    elif exif:
        try:
            img = ImageOps.exif_transpose(img)
        except Exception:
            pass

    if img.mode in ("I;16", "I;16B", "I;16L", "I;16N", "I", "F"):
        img = _img_a_8bits(img)

    if img.mode != "RGBA":
        img = img.convert("RGBA")
    return img


def _img_a_8bits(img):
    """
    Pillow RECORTA a 255 al convertir imágenes de 16/32 bits (un TIFF de 16 bits
    quedaba casi blanco). Aquí se reescalan de verdad a 8 bits en escala de grises.
    """
    try:
        import numpy as _np
        arr = _np.asarray(img)
        if img.mode == "F":
            lo, hi = float(arr.min()), float(arr.max())
            if hi <= 1.0 and lo >= 0.0:
                arr8 = arr * 255.0
            else:
                arr8 = (arr - lo) * (255.0 / (hi - lo)) if hi > lo else arr * 0
        elif img.mode.startswith("I;16") or int(arr.max()) > 255:
            arr8 = arr.astype(_np.float32) / 257.0
        else:
            arr8 = arr
        return Image.fromarray(_np.clip(_np.asarray(arr8, dtype=_np.float32) + 0.5, 0, 255).astype(_np.uint8), "L")
    except Exception:
        return img


def img_contain(pil, box, pad=True, bg=(0, 0, 0, 0)):
    """
    Ajusta `pil` dentro de `box` = (w, h) SIN deformar (comportamiento "contain").

      · calcula el mayor tamaño proporcional que cabe en la caja
      · redimensiona con LANCZOS **solo si hace falta** cambiar la resolución
      · si pad=True devuelve un canvas exacto del tamaño de la caja, centrado
        y relleno con `bg` (transparente por defecto)

    Ejemplo: 1920x1080 en caja 40x40  ->  40x22 centrado en canvas 40x40.
    """
    box_w, box_h = int(box[0]), int(box[1])
    if box_w <= 0 or box_h <= 0:
        return pil

    src_w, src_h = pil.size
    if src_w <= 0 or src_h <= 0:
        return pil

    escala = min(box_w / src_w, box_h / src_h)
    new_w = max(1, int(round(src_w * escala)))
    new_h = max(1, int(round(src_h * escala)))

    # Solo redimensionar si realmente cambia la resolución.
    if (new_w, new_h) != (src_w, src_h):
        pil = pil.resize((new_w, new_h), Image.Resampling.LANCZOS)

    if not pad:
        return pil

    if (new_w, new_h) == (box_w, box_h):
        return pil

    canvas = Image.new("RGBA", (box_w, box_h), bg)
    if pil.mode != "RGBA":
        pil = pil.convert("RGBA")
    canvas.paste(pil, ((box_w - new_w) // 2, (box_h - new_h) // 2), pil)
    return canvas


def img_square_canvas(pil, bg=(0, 0, 0, 0)):
    """
    Devuelve una versión cuadrada de `pil` a su resolución NATIVA, rellenando
    con transparencia. No escala: solo cuadra. Si ya es cuadrada la devuelve tal cual.
    """
    if pil.mode != "RGBA":
        pil = pil.convert("RGBA")
    w, h = pil.size
    if w == h:
        return pil
    lado = max(w, h)
    canvas = Image.new("RGBA", (lado, lado), bg)
    canvas.paste(pil, ((lado - w) // 2, (lado - h) // 2), pil)
    return canvas


def ico_build_frames(pil, sizes):
    """
    Genera los frames de un ICO a partir de una imagen origen.

      · cuadra UNA sola vez a resolución nativa (sin deformar)
      · genera CADA tamaño pedido directamente desde ese cuadrado nativo
        -> un único escalado por frame, nunca cascada original->base->subtamaño
      · LANCZOS en cada resize real

    Devuelve lista de imágenes RGBA ordenadas de mayor a menor.
    """
    base = img_square_canvas(pil)
    lado_nativo = base.size[0]

    frames = []
    for s in sorted({int(x) for x in sizes}, reverse=True):
        if s <= 0:
            continue
        if s == lado_nativo:
            frames.append(base.copy())
        else:
            frames.append(base.resize((s, s), Image.Resampling.LANCZOS))
    return frames


# ------------------------------------------------------------------------------
#   Formatos que Pillow no abre (se decodifican con FFmpeg) y apoyo para SVG
# ------------------------------------------------------------------------------
_IMG_EXT_SOLO_FFMPEG = {".svg", ".heic", ".heif"}
_IMG_EXT_VIA_PILLOW = {".psd", ".ico"}          # FFmpeg falla con PSD con transparencia
_IMG_SALIDA_UN_CUADRO = {"jpg", "jpeg", "png", "tif", "tiff", "bmp"}
# "Solo reducir 50%": formatos que FFmpeg no puede volver a escribir
_IMG_SIN_REESCRITURA = {".heic": "jpg", ".heif": "jpg", ".svg": "png", ".psd": "png"}
_SVG_LADO_POR_DEFECTO = 1024


def _img_flags_sin_ventana():
    return getattr(subprocess, "CREATE_NO_WINDOW", 0) if os.name == "nt" else 0


def _img_tmp_png():
    fd, ruta = tempfile.mkstemp(prefix="dmt_img_", suffix=".png")
    os.close(fd)
    return ruta


def _img_sobre_blanco(img):
    """Compone una imagen RGBA sobre blanco (destinos sin transparencia: JPG, OCR)."""
    if img.mode != "RGBA":
        img = img.convert("RGBA")
    fondo = Image.new("RGB", img.size, (255, 255, 255))
    fondo.paste(img, mask=img.getchannel("A"))
    return fondo


def _svg_medidas(path):
    """(ancho, alto, proporción) declarados en el SVG; None si no se pueden leer."""
    import xml.etree.ElementTree as _ET
    try:
        raiz = _ET.parse(path).getroot()
    except Exception:
        return None, None, None

    def _px(valor):
        m = re.match(r"^\s*([0-9]*\.?[0-9]+)\s*(px)?\s*$", valor or "")
        return float(m.group(1)) if m else None

    ancho, alto = _px(raiz.get("width")), _px(raiz.get("height"))
    proporcion = None
    vb = raiz.get("viewBox") or raiz.get("viewbox")
    if vb:
        partes = [p for p in re.split(r"[\s,]+", vb.strip()) if p]
        try:
            if len(partes) == 4 and float(partes[3]) > 0:
                proporcion = float(partes[2]) / float(partes[3])
        except ValueError:
            proporcion = None
    return ancho, alto, proporcion


def _svg_opciones_render(path, lado_min=None):
    """
    Opciones de FFmpeg (antes de -i) para rasterizar un SVG a un tamaño útil.
    Con width/height en px se respeta su tamaño real; si el SVG no lo declara
    (librsvg lo dejaría en 100x100) se usa 1024 px en el lado mayor.
    """
    ancho, alto, prop = _svg_medidas(path)
    if ancho and alto:
        w, h = ancho, alto
    elif prop and (ancho or alto):
        w, h = (ancho, ancho / prop) if ancho else (alto * prop, alto)
    elif prop:
        w, h = (_SVG_LADO_POR_DEFECTO, _SVG_LADO_POR_DEFECTO / prop) if prop >= 1 else (_SVG_LADO_POR_DEFECTO * prop, _SVG_LADO_POR_DEFECTO)
    else:
        w, h = _SVG_LADO_POR_DEFECTO, _SVG_LADO_POR_DEFECTO
    if lado_min and max(w, h) < lado_min:
        f = lado_min / max(w, h)
        w, h = w * f, h * f
    w, h = max(1, int(round(w))), max(1, int(round(h)))
    return ["-width", str(w), "-height", str(h), "-keep_ar", "1"]


def _img_decodificar_ffmpeg(path, destino=None, svg_lado=None):
    """Decodifica el primer cuadro de una imagen con FFmpeg a PNG RGBA (8 bits)."""
    destino = destino or _img_tmp_png()
    pre = _svg_opciones_render(path, svg_lado) if os.path.splitext(path)[1].lower() == ".svg" else []
    cmd = ["ffmpeg", "-y", "-v", "error"] + pre + ["-i", path, "-frames:v", "1", "-pix_fmt", "rgba", destino]
    r = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True,
                       encoding="utf-8", errors="ignore", startupinfo=_startup_info_modulo(),
                       creationflags=_img_flags_sin_ventana())
    if r.returncode != 0 or not os.path.isfile(destino) or os.path.getsize(destino) == 0:
        try:
            os.remove(destino)
        except OSError:
            pass
        raise RuntimeError("FFmpeg no pudo leer la imagen: " + (r.stderr or "").strip()[:120])
    return destino


def img_open_any(path, target_px=None, exif=True, svg_lado=None):
    """
    Abre CUALQUIER imagen admitida y devuelve RGBA (primer cuadro):
      1) Pillow (ICO con la mejor capa, EXIF, 16 bits bien escalados, PSD)
      2) si Pillow no puede (SVG, HEIC...), FFmpeg la decodifica a un PNG temporal
    """
    ext = os.path.splitext(path)[1].lower()
    if ext not in _IMG_EXT_SOLO_FFMPEG:
        try:
            img = img_open_smart(path, target_px=target_px, exif=exif)
            img.load()
            return img
        except Exception:
            pass
    tmp = _img_decodificar_ffmpeg(path, svg_lado=svg_lado)
    try:
        with Image.open(tmp) as im:
            im.load()
            return im.convert("RGBA") if im.mode != "RGBA" else im.copy()
    finally:
        try:
            os.remove(tmp)
        except OSError:
            pass


def _img_pixfmt_con_alfa(path):
    """True si FFmpeg decodifica la imagen con canal alfa (o paleta con posible transparencia)."""
    if os.path.splitext(path)[1].lower() == ".svg":
        return True
    try:
        out = subprocess.run(
            ["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
             "stream=pix_fmt", "-of", "csv=p=0", path],
            capture_output=True, text=True, timeout=20, startupinfo=_startup_info_modulo(),
            creationflags=_img_flags_sin_ventana()).stdout.strip().lower()
    except Exception:
        return False
    return out.startswith(("rgba", "bgra", "argb", "abgr", "ya8", "ya16", "yuva", "gbrap",
                           "pal8", "ayuv", "vuya"))


def _img_es_animada(path):
    """True si la imagen de origen tiene varios cuadros (GIF / WebP / APNG animados)."""
    if os.path.splitext(path)[1].lower() not in (".gif", ".webp", ".png"):
        return False
    try:
        with Image.open(path) as im:
            return bool(getattr(im, "is_animated", False))
    except Exception:
        return False


def _img_opciones_webp(path_original):
    """
    Codificador WEBP: el de imagen fija (libwebp) salvo que el origen sea animado.
    FFmpeg usa por defecto libwebp_anim, que en algunos PNG/PSD con transparencia
    pierde el canal alfa (queda fondo negro).
    """
    return [] if _img_es_animada(path_original) else ["-c:v", "libwebp"]


def _img_entrada_ffmpeg(path, opaco=False, con_filtro=False):
    """
    Prepara la entrada de FFmpeg para convertir/comprimir una imagen.
    Devuelve (opciones_antes_de_-i, ruta_entrada, temporales_a_borrar).
      · PSD / ICO: Pillow arma la imagen (FFmpeg falla con PSD transparentes y
        así el ICO usa su capa más grande).
      · SVG: se rasteriza a su tamaño real (1024 px si no lo declara).
      · opaco=True (destino JPG): la transparencia se compone sobre BLANCO
        (antes quedaba negra).
      · con_filtro=True (se va a aplicar -vf): los HEIC de iPhone vienen en
        mosaico y FFmpeg no permite combinarlo con -vf, así que se arman antes.
    """
    ext = os.path.splitext(path)[1].lower()
    temporales = []
    if ext in _IMG_EXT_VIA_PILLOW or (con_filtro and ext in (".heic", ".heif")):
        img = img_open_any(path)
        if opaco:
            img = _img_sobre_blanco(img)
        tmp = _img_tmp_png()
        temporales.append(tmp)
        img.save(tmp, format="PNG", compress_level=1)
        return [], tmp, temporales

    pre = _svg_opciones_render(path) if ext == ".svg" else []
    if opaco and _img_pixfmt_con_alfa(path):
        tmp_rgba = _img_decodificar_ffmpeg(path)
        temporales.append(tmp_rgba)
        with Image.open(tmp_rgba) as im:
            im.load()
            rgba = im.convert("RGBA")
        a_min, a_max = rgba.getchannel("A").getextrema()
        if a_min < 255:
            tmp_rgb = _img_tmp_png()
            temporales.append(tmp_rgb)
            _img_sobre_blanco(rgba).save(tmp_rgb, format="PNG", compress_level=1)
            return [], tmp_rgb, temporales
    return pre, path, temporales


def _img_borrar_temporales(rutas):
    for ruta in rutas or ():
        try:
            if ruta and os.path.isfile(ruta):
                os.remove(ruta)
        except OSError:
            pass


def _filtro_imagenes(nombre="Imágenes"):
    """Filtro de diálogo con exactamente los formatos admitidos al arrastrar."""
    return [(nombre, " ".join("*" + e for e in sorted(VALID_IMAGE_EXT)))]


def _filtro_videos(nombre="Videos"):
    """Filtro de diálogo con exactamente los formatos de video admitidos al arrastrar."""
    return [(nombre, " ".join("*" + e for e in sorted(VALID_VIDEO_EXT)))]


def _plural_pag(n):
    """Plural correcto en los mensajes: '1 pág.' / '70 págs.'"""
    return f"{n} pág." if n == 1 else f"{n} págs."


def _ruta_unica(path):
    """
    Ruta de salida que nunca pisa un archivo existente (ni el de origen):
    'nombre.ext' -> 'nombre (1).ext', 'nombre (2).ext'...
    """
    if not os.path.exists(path):
        return path
    base, ext = os.path.splitext(path)
    i = 1
    while os.path.exists(f"{base} ({i}){ext}"):
        i += 1
    return f"{base} ({i}){ext}"


# --- VARIABLES GLOBALES PARA LIBRERÍAS PESADAS (PLACEHOLDERS) ---
# Se definen vacías para que el programa arranque instantáneo.
# Se llenarán en background.

# --- INICIO DEL TRUCO ---
# Creamos un "torch falso" para que la interfaz no falle al preguntar por .cuda
class DummyCuda:
    def is_available(self): return False
    def device_count(self): return 0
    def empty_cache(self): pass

class DummyTorch:
    def __init__(self): self.cuda = DummyCuda()

torch = DummyTorch() # Ahora torch existe (es falso), así que no da error
# --- FIN DEL TRUCO ---


# ==============================================================================
#   CUDA SIN TORCH
# ------------------------------------------------------------------------------
#   DMT no usa PyTorch para calcular nada: solo lo usaba para (1) saber si hay
#   GPU NVIDIA, su nombre y su capacidad de cómputo, y (2) cargar las DLL de
#   CUDA 12.9 / cuDNN 9.10 que usan CTranslate2 (Whisper) y PaddlePaddle (OCR).
#   Importar torch cargaba además torch_cuda.dll y torch_cpu.dll (más de 1.5 GB)
#   sin usarlas. Ahora:
#     · las DLL de NVIDIA se precargan directamente desde su carpeta
#         - compilado: <app>\cuda  (PyInstaller: _internal\cuda)
#         - .py:       site-packages\torch\lib  (sin importar torch)
#     · la GPU se detecta con cudart (misma prueba que hace torch) y NVML
#       (driver de NVIDIA) para nombre y capacidad de cómputo.
#   Si algo de esto falla y torch está instalado, se usa torch como antes.
# ==============================================================================
_CUDA_LOCK = threading.Lock()
_CUDA_DIR = None                  # None = sin evaluar; "" = no encontrada
_CUDA_DIR_HANDLES = []
# DLLs propias de PyTorch u opcionales que NO se cargan (ni se empaquetan)
_CUDA_NO_CARGAR_PREFIJOS = ("torch", "c10", "caffe2", "fbgemm", "asmjit", "shm", "uv",
                            "libiomp", "cupti", "cufftw", "cusolvermg")
_CUDA_NO_CARGAR_EXACTOS = {"nvrtc64_120_0.alt.dll"}
_CUDA_ORDEN_CARGA = ("cudart", "nvjitlink", "cublaslt", "cublas", "curand", "cufft",
                     "cusparse", "cusolver", "nvrtc", "zlibwapi", "cudnn_graph",
                     "cudnn_engines", "cudnn_heuristic", "cudnn_ops", "cudnn_cnn",
                     "cudnn_adv", "cudnn64")


def _cuda_dll_util(nombre):
    n = nombre.lower()
    return (n.endswith(".dll") and not n.startswith(_CUDA_NO_CARGAR_PREFIJOS)
            and n not in _CUDA_NO_CARGAR_EXACTOS)


def _cuda_buscar_carpeta():
    candidatos = []
    if os.environ.get("DMT_CUDA_DIR"):
        candidatos.append(os.environ["DMT_CUDA_DIR"])
    candidatos.append(resource_path("cuda"))
    candidatos.append(os.path.join(os.path.dirname(os.path.abspath(sys.executable)), "cuda"))
    try:
        import importlib.util as _ilu
        spec = _ilu.find_spec("torch")          # solo ubica el paquete, NO lo importa
        if spec is not None and spec.origin:
            candidatos.append(os.path.join(os.path.dirname(spec.origin), "lib"))
    except Exception:
        pass
    for carpeta in candidatos:
        if carpeta and os.path.isfile(os.path.join(carpeta, "cudart64_12.dll")):
            return carpeta
    return None


def _cuda_preparar_dlls(precargar=True):
    """Deja listas las DLL de CUDA/cuDNN para CTranslate2 y PaddlePaddle. Devuelve la carpeta o None."""
    global _CUDA_DIR
    with _CUDA_LOCK:
        if _CUDA_DIR is not None:
            return _CUDA_DIR or None
        if os.name != "nt":
            _CUDA_DIR = ""
            return None
        carpeta = _cuda_buscar_carpeta()
        if not carpeta:
            _CUDA_DIR = ""
            print("[CUDA] No se encontraron las DLL de CUDA 12.9 / cuDNN 9.")
            return None
        try:
            _CUDA_DIR_HANDLES.append(os.add_dll_directory(carpeta))
        except Exception:
            pass
        os.environ["PATH"] = carpeta + os.pathsep + os.environ.get("PATH", "")
        if precargar:
            from ctypes import wintypes
            k32 = ctypes.WinDLL("kernel32", use_last_error=True)
            k32.LoadLibraryExW.argtypes = [wintypes.LPCWSTR, wintypes.HANDLE, wintypes.DWORD]
            k32.LoadLibraryExW.restype = wintypes.HMODULE

            def _orden(nombre):
                n = nombre.lower()
                for i, prefijo in enumerate(_CUDA_ORDEN_CARGA):
                    if n.startswith(prefijo):
                        return (i, n)
                return (len(_CUDA_ORDEN_CARGA), n)

            dlls = sorted((n for n in os.listdir(carpeta) if _cuda_dll_util(n)), key=_orden)
            for nombre in dlls:
                # 0x1100 = LOAD_LIBRARY_SEARCH_DEFAULT_DIRS | LOAD_LIBRARY_SEARCH_DLL_LOAD_DIR (igual que torch)
                if not k32.LoadLibraryExW(os.path.join(carpeta, nombre), None, 0x00001100):
                    print(f"[CUDA] No se pudo cargar {nombre} (error {ctypes.get_last_error()})")
        _CUDA_DIR = carpeta
        return carpeta


def _nvml_info(bus_id=None):
    """(nombre, (mayor, menor)) de la GPU vía NVML (viene con el driver de NVIDIA)."""
    nvml = None
    sistema = os.environ.get("SystemRoot", r"C:\Windows")
    for ruta in (os.path.join(sistema, "System32", "nvml.dll"),
                 os.path.join(os.environ.get("ProgramFiles", r"C:\Program Files"),
                              "NVIDIA Corporation", "NVSMI", "nvml.dll"),
                 "nvml.dll"):
        try:
            nvml = ctypes.CDLL(ruta)
            break
        except OSError:
            continue
    if nvml is None:
        return None, None
    if nvml.nvmlInit_v2() != 0:
        return None, None
    try:
        disp = ctypes.c_void_p()
        ok = False
        if bus_id:
            ok = nvml.nvmlDeviceGetHandleByPciBusId_v2(ctypes.c_char_p(bus_id), ctypes.byref(disp)) == 0
        if not ok:
            ok = nvml.nvmlDeviceGetHandleByIndex_v2(ctypes.c_uint(0), ctypes.byref(disp)) == 0
        if not ok:
            return None, None
        nombre = None
        buf = ctypes.create_string_buffer(96)
        if nvml.nvmlDeviceGetName(disp, buf, ctypes.c_uint(96)) == 0:
            nombre = buf.value.decode("utf-8", "replace")
        cc = None
        mayor, menor = ctypes.c_int(0), ctypes.c_int(0)
        if nvml.nvmlDeviceGetCudaComputeCapability(disp, ctypes.byref(mayor), ctypes.byref(menor)) == 0:
            cc = (mayor.value, menor.value)
        return nombre, cc
    finally:
        try:
            nvml.nvmlShutdown()
        except Exception:
            pass


class _CudaLigera:
    """Lo único que DMT usaba de torch.cuda, sin cargar PyTorch."""

    def __init__(self):
        self._evaluada = False
        self._disponible = False
        self._nombre = None
        self._cc = None
        self.motivo = ""

    def _evaluar(self):
        if self._evaluada:
            return
        self._evaluada = True
        carpeta = _cuda_preparar_dlls()
        if not carpeta:
            self.motivo = "no se encontraron las DLL de CUDA"
            return
        try:
            cudart = ctypes.CDLL(os.path.join(carpeta, "cudart64_12.dll"))
            cantidad = ctypes.c_int(0)
            codigo = cudart.cudaGetDeviceCount(ctypes.byref(cantidad))
            if codigo != 0 or cantidad.value < 1:
                # 35 = driver demasiado viejo para CUDA 12.9; 100 = no hay GPU NVIDIA
                self.motivo = f"cudaGetDeviceCount={codigo}, dispositivos={cantidad.value}"
                return
        except Exception as e:
            self.motivo = f"{type(e).__name__}: {e}"
            return
        # La GPU ya se confirmó arriba; el bus PCI solo AYUDA a que NVML apunte
        # a la GPU correcta si hay varias. Si algo falla aquí (nombre de función,
        # DLL sin ese símbolo...) no debe invalidar la detección ya hecha.
        bus_id = None
        try:
            bus = ctypes.create_string_buffer(64)
            if cudart.cudaDeviceGetPCIBusId(bus, ctypes.c_int(64), ctypes.c_int(0)) == 0:
                bus_id = bus.value
        except Exception as e:
            print(f"[CUDA] No se pudo leer el bus PCI (se sigue sin distinguir GPU por bus): {e}")
        try:
            self._nombre, self._cc = _nvml_info(bus_id)
        except Exception as e:
            print(f"[CUDA] NVML no disponible (nombre/capacidad de cómputo desconocidos): {e}")
        self._disponible = True

    def is_available(self):
        self._evaluar()
        return self._disponible

    def device_count(self):
        return 1 if self.is_available() else 0

    def get_device_name(self, indice=0):
        if not self.is_available():
            raise RuntimeError("CUDA no disponible")
        return self._nombre or "NVIDIA GPU"

    def get_device_capability(self, indice=0):
        if not self.is_available():
            raise RuntimeError("CUDA no disponible")
        if self._cc is None:
            raise RuntimeError("No se pudo leer la capacidad de cómputo (NVML)")
        return self._cc

    def empty_cache(self):
        # La memoria de GPU la administran CTranslate2 y PaddlePaddle, no torch.
        pass


class _TorchLigero:
    """Sustituto de 'torch' con solo la parte .cuda que usa la interfaz."""
    ligero = True

    def __init__(self):
        self.cuda = _CudaLigera()


def _cuda_iniciar():
    """
    Tier-2: prepara CUDA sin torch. Si no se logra y torch está instalado
    (modo .py o builds antiguos), se usa torch como antes.
    """
    ligero = _TorchLigero()
    try:
        if ligero.cuda.is_available():
            return ligero
    except Exception as e:
        ligero.cuda.motivo = str(e)
    try:
        import importlib.util as _ilu
        if _ilu.find_spec("torch") is not None:
            print(f"[CUDA] Detección sin torch no disponible ({ligero.cuda.motivo}); se intenta con torch.")
            mod = importlib.import_module("torch")
            if mod.cuda.is_available():
                return mod
    except Exception as e:
        print(f"[CUDA] torch tampoco disponible: {e}")
    return ligero
faster_whisper = None
yt_dlp = None
PyPDF2 = None
fitz = None
cv2 = None
np = None
WhisperModel = None
# --- IMPORTS PARA METADATA LAB ---
import piexif
import mutagen
from mutagen.easyid3 import EasyID3
from mutagen.mp4 import MP4
from docx import Document
import openpyxl
from pptx import Presentation  # <--- AGREGAR ESTA
# ---------------------------------
# ------------------------------------------------
# FUNCIÓN SEGURO/ROBUSTA PARA CARGAR LIBRERÍAS PESADAS
# Ejecutar en hilo separado: threading.Thread(target=cargar_librerias_pesadas_global, args=(mi_callback,)).start()
# ------------------------------------------------
import importlib

def _is_frozen_build():
    """
    True si el programa corre "compilado", ya sea con PyInstaller/cx_Freeze
    (ponen sys.frozen=True) o con Nuitka (que NO usa sys.frozen y en cambio
    expone el atributo de módulo __compiled__). Usar esta función en vez de
    'getattr(sys, "frozen", False)' a secas para que la detección de rutas
    funcione igual compilando con PyInstaller o con Nuitka.
    """
    return bool(getattr(sys, 'frozen', False)) or ('__compiled__' in globals())

def whisper_kwargs_dispositivo(device):
    """
    Argumentos extra para WhisperModel segun el dispositivo.
    En CPU se fijan los hilos: con PaddlePaddle en el mismo proceso, CTranslate2
    con hilos por defecto transcribe ~2.5x mas lento tras usar PaddleOCR
    (medido en el kit de pruebas CUDA 12.9). Con cpu_threads fijo no pasa.
    """
    if str(device).lower() == "cpu":
        return {"cpu_threads": max(1, (os.cpu_count() or 4) // 2)}
    return {}


def _avisar_dlls_nvidia_de_pip():
    """
    PaddlePaddle precarga todas las DLLs de <site-packages>\\nvidia\\*\\bin. Si existen,
    chocan con el cuDNN/cuBLAS que ya cargo torch y 'import paddle' falla con
    WinError 127. El stack CUDA 12.9 de DMT usa SOLO las DLLs de torch\\lib.
    """
    try:
        bases = set()
        try:
            bases.update(site.getsitepackages())
        except Exception:
            pass
        bases.add(os.path.join(sys.prefix, "Lib", "site-packages"))
        if _is_frozen_build():
            bases.add(os.path.dirname(sys.executable))
            if getattr(sys, "_MEIPASS", None):
                bases.add(sys._MEIPASS)
        for base in bases:
            carpeta = os.path.join(base, "nvidia")
            if not os.path.isdir(carpeta):
                continue
            con_dll = []
            for nombre in os.listdir(carpeta):
                bin_dir = os.path.join(carpeta, nombre, "bin")
                if os.path.isdir(bin_dir) and any(f.lower().endswith(".dll") for f in os.listdir(bin_dir)):
                    con_dll.append(nombre)
            if con_dll:
                print(f"⚠️ [GPU SETUP] DLLs NVIDIA de pip en {carpeta}: {', '.join(sorted(con_dll))}")
                print("   PaddleOCR GPU fallara (WinError 127): chocan con las DLLs de torch. "
                      "Desinstala los paquetes nvidia-* de este entorno.")
    except Exception as e:
        print(f"[GPU SETUP] No se pudo revisar DLLs NVIDIA de pip: {e}")


def _dmt_base_dir():
    """Carpeta persistente y escribible: %LOCALAPPDATA%/DeusMachinaTools (misma base que yt_dlp_live)."""
    _localappdata = os.environ.get("LOCALAPPDATA") or os.path.join(os.path.expanduser("~"), "AppData", "Local")
    _base = os.path.join(_localappdata, "DeusMachinaTools")
    try:
        os.makedirs(_base, exist_ok=True)
    except Exception:
        pass
    return _base

# ------------------------------------------------------------------------------
#   TEMPORALES: una carpeta por sesión dentro de %TEMP%\DeusMachinaTools
# ------------------------------------------------------------------------------
#   Todo lo temporal de la app (y de sus librerías y procesos hijos: yt-dlp,
#   FFmpeg, Ghostscript, spotDL, motor OCR...) va a %TEMP%\DeusMachinaTools\
#   sesion_<pid>. Al cerrar la app se borra, y al arrancar se borran las
#   sesiones que quedaron de cierres forzados o cuelgues. Así nada se acumula.
_DMT_TEMP_BASE_SISTEMA = tempfile.gettempdir()
_DMT_TEMP_SESION = None
_DMT_TEMP_CANDADO = None
# Restos sueltos que dejaban versiones anteriores directamente en %TEMP%
_DMT_PATRON_RESTOS_VIEJOS = re.compile(
    r"^(yt_trans_[0-9a-f]{10}.*|trans_prep_[0-9a-f]{8}\.wav|temp_live_[0-9a-f]{6}\.wav|dmt_img_.*\.png)$")


def _dmt_pid_vivo(pid):
    try:
        pid = int(pid)
    except (TypeError, ValueError):
        return False
    if pid == os.getpid():
        return True
    if os.name == "nt":
        try:
            k32 = ctypes.windll.kernel32
            h = k32.OpenProcess(0x1000, False, pid)      # PROCESS_QUERY_LIMITED_INFORMATION
            if not h:
                return False
            try:
                codigo = ctypes.c_ulong()
                ok = k32.GetExitCodeProcess(h, ctypes.byref(codigo))
                return bool(ok) and codigo.value == 259   # STILL_ACTIVE
            finally:
                k32.CloseHandle(h)
        except Exception:
            return True     # ante la duda, no se borra
    try:
        os.kill(pid, 0)
        return True
    except OSError:
        return False


def _dmt_limpiar_temporales_viejos(base):
    """Borra sesiones de ejecuciones que ya no existen y restos sueltos de versiones anteriores."""
    try:
        for nombre in os.listdir(base):
            ruta = os.path.join(base, nombre)
            m = re.match(r"^sesion_(\d+)$", nombre)
            if not m or not os.path.isdir(ruta):
                continue
            if _dmt_pid_vivo(m.group(1)):
                continue
            candado = os.path.join(ruta, ".en_uso")
            try:
                if os.path.exists(candado):
                    os.remove(candado)       # en Windows falla si la sesión sigue abierta
            except OSError:
                continue
            shutil.rmtree(ruta, ignore_errors=True)
    except Exception as e:
        print(f"[Temporales] Limpieza de sesiones: {e}")

    ahora = time.time()
    try:
        for nombre in os.listdir(_DMT_TEMP_BASE_SISTEMA):
            if not _DMT_PATRON_RESTOS_VIEJOS.match(nombre):
                continue
            ruta = os.path.join(_DMT_TEMP_BASE_SISTEMA, nombre)
            try:
                if os.path.isfile(ruta) and ahora - os.path.getmtime(ruta) > 3600:
                    os.remove(ruta)
            except OSError:
                pass
    except Exception as e:
        print(f"[Temporales] Limpieza de restos antiguos: {e}")


def _dmt_iniciar_temporales():
    """Crea la carpeta temporal de esta sesión y la usa para todo el proceso (y sus hijos)."""
    global _DMT_TEMP_SESION, _DMT_TEMP_CANDADO
    if _DMT_TEMP_SESION:
        return _DMT_TEMP_SESION
    try:
        base = os.path.join(_DMT_TEMP_BASE_SISTEMA, "DeusMachinaTools")
        os.makedirs(base, exist_ok=True)
        _dmt_limpiar_temporales_viejos(base)
        sesion = os.path.join(base, f"sesion_{os.getpid()}")
        os.makedirs(sesion, exist_ok=True)
        _DMT_TEMP_CANDADO = open(os.path.join(sesion, ".en_uso"), "w")
        for var in ("TMP", "TEMP", "TMPDIR"):
            os.environ[var] = sesion
        tempfile.tempdir = sesion
        _DMT_TEMP_SESION = sesion
    except Exception as e:
        print(f"[Temporales] Se usará la carpeta temporal del sistema: {e}")
    return _DMT_TEMP_SESION


def _dmt_borrar_temporales_sesion():
    """Al cerrar la app: borra la carpeta temporal de esta sesión."""
    global _DMT_TEMP_CANDADO
    try:
        if _DMT_TEMP_CANDADO is not None:
            _DMT_TEMP_CANDADO.close()
            _DMT_TEMP_CANDADO = None
    except Exception:
        pass
    if _DMT_TEMP_SESION and os.path.isdir(_DMT_TEMP_SESION):
        shutil.rmtree(_DMT_TEMP_SESION, ignore_errors=True)


def _dmt_version_archivo(ruta):
    """Versión de archivo de una DLL de Windows ('14.44.35211.0'), o '' si no se puede leer."""
    if os.name != "nt":
        return ""
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
            return ""
        buf = ctypes.create_string_buffer(tam)
        if not ver.GetFileVersionInfoW(ruta, 0, tam, buf):
            return ""
        ptr, largo = ctypes.c_void_p(), wintypes.UINT()
        if not ver.VerQueryValueW(buf, "\\", ctypes.byref(ptr), ctypes.byref(largo)) or not ptr.value:
            return ""
        campos = ctypes.cast(ptr, ctypes.POINTER(wintypes.DWORD * 4)).contents
        ms, ls = campos[2], campos[3]
        return f"{ms >> 16}.{ms & 0xFFFF}.{ls >> 16}.{ls & 0xFFFF}"
    except Exception:
        return ""


# Diagnóstico detallado en la terminal (inventario de DLL, comandos FFmpeg completos).
# Apagado por defecto. Para activarlo: abrir la app con la variable DMT_DIAG=1
#   PowerShell:  $env:DMT_DIAG=1; python Deus_machina_tools.py
_DMT_DIAG = os.environ.get("DMT_DIAG", "").strip().lower() not in ("", "0", "no", "false")

_DMT_DLLS_VIGILADAS = ("msvcp140", "vcruntime140", "concrt140", "cudnn", "cublas", "cudart",
                       "onnxruntime", "libiomp5", "ctranslate2", "libpaddle", "mklml", "zlibwapi")
_DMT_ULTIMO_INVENTARIO = None


def _dmt_dlls_cargadas():
    """Rutas (y versión) de las DLL sensibles ya cargadas en este proceso (solo Windows)."""
    if os.name != "nt":
        return []
    try:
        from ctypes import wintypes
        psapi = ctypes.WinDLL("psapi")
        k32 = ctypes.WinDLL("kernel32")
        k32.GetCurrentProcess.restype = wintypes.HANDLE
        psapi.EnumProcessModules.argtypes = [wintypes.HANDLE, ctypes.POINTER(wintypes.HMODULE),
                                             wintypes.DWORD, ctypes.POINTER(wintypes.DWORD)]
        k32.GetModuleFileNameW.argtypes = [wintypes.HMODULE, wintypes.LPWSTR, wintypes.DWORD]
        proceso = k32.GetCurrentProcess()
        modulos = (wintypes.HMODULE * 4096)()
        necesario = wintypes.DWORD()
        if not psapi.EnumProcessModules(proceso, modulos, ctypes.sizeof(modulos), ctypes.byref(necesario)):
            return []
        cuantos = min(4096, necesario.value // ctypes.sizeof(wintypes.HMODULE))
        buf = ctypes.create_unicode_buffer(1024)
        salida = []
        for i in range(cuantos):
            if not k32.GetModuleFileNameW(modulos[i], buf, 1024):
                continue
            ruta = buf.value
            nombre = os.path.basename(ruta).lower()
            if nombre.startswith(_DMT_DLLS_VIGILADAS):
                mostrar = ruta
                try:
                    base = os.path.dirname(os.path.abspath(sys.executable))
                    if os.path.normcase(ruta).startswith(os.path.normcase(base) + os.sep):
                        mostrar = os.path.relpath(ruta, base)
                except Exception:
                    pass
                salida.append(f"{mostrar}  [{_dmt_version_archivo(ruta) or '?'}]")
        return sorted(salida)
    except Exception as e:
        return [f"(no se pudo listar DLLs: {e})"]


def _dmt_registrar_dlls(etiqueta):
    """Escribe en el log las DLL sensibles cargadas (solo si cambiaron desde la última vez).
    Solo con DMT_DIAG=1: el conflicto de DLL ya está resuelto y en uso normal ensucia la terminal."""
    global _DMT_ULTIMO_INVENTARIO
    if not _DMT_DIAG:
        return
    lista = _dmt_dlls_cargadas()
    if not lista or lista == _DMT_ULTIMO_INVENTARIO:
        return
    _DMT_ULTIMO_INVENTARIO = lista
    print(f"[DLLs] {etiqueta}:")
    for linea in lista:
        print(f"   {linea}")
    try:
        sys.stdout.flush()
    except Exception:
        pass


def _dmt_flujo_sin_salida(flujo):
    if flujo is None:
        return True
    nombre = str(getattr(flujo, "name", "")).lower()
    return nombre in ("nul", "nul:", os.devnull.lower())


def _dmt_activar_faulthandler(flujo=None):
    """Si el proceso se cae por un error nativo (DLL), deja la pila de Python en el log."""
    try:
        import faulthandler
        destino = flujo if flujo is not None else sys.stderr
        if destino is not None and not _dmt_flujo_sin_salida(destino):
            faulthandler.enable(file=destino, all_threads=True)
    except Exception:
        pass


def _dmt_preparar_stdio_hijo():
    """
    Proceso hijo del motor OCR: en builds sin consola su salida (y cualquier caída
    nativa) va a %LOCALAPPDATA%\\DeusMachinaTools\\logs\\motor_ocr.log.
    Se ejecuta al importar el script, ANTES de que multiprocessing arranque el hijo.
    """
    es_hijo = ("--multiprocessing-fork" in sys.argv) or (__name__ == "__parents_main__")
    if not es_hijo:
        return
    if not (_dmt_flujo_sin_salida(sys.stdout) or _dmt_flujo_sin_salida(sys.stderr)):
        _dmt_activar_faulthandler()       # desarrollo: hay consola
        return
    try:
        carpeta = os.path.join(_dmt_base_dir(), "logs")
        os.makedirs(carpeta, exist_ok=True)
        ruta = os.path.join(carpeta, "motor_ocr.log")
        modo = "a" if os.path.exists(ruta) and os.path.getsize(ruta) < 2 * 1024 * 1024 else "w"
        flujo = open(ruta, modo, encoding="utf-8", errors="replace", buffering=1)
    except Exception:
        flujo = open(os.devnull, "w", encoding="utf-8")
    sys.stdout = flujo
    sys.stderr = flujo
    _dmt_activar_faulthandler(flujo)
    print(f"\n===== Motor OCR  {time.strftime('%Y-%m-%d %H:%M:%S')}  pid={os.getpid()} =====")


def _dmt_preparar_stdio_app():
    """
    Builds sin consola: PyInstaller (--windowed) deja sys.stdout/stderr en None y
    Nuitka (--windows-console-mode=disable) los manda a NUL. Algunas librerías
    (barras de progreso de descargas, logs de Paddle...) fallan con None, y sin
    salida no hay forma de diagnosticar. Aquí se mandan a
    %LOCALAPPDATA%\\DeusMachinaTools\\logs\\ultima_sesion.log (se guardan solo
    las dos últimas sesiones).
    """
    def _sin_salida(flujo):
        if flujo is None:
            return True
        nombre = str(getattr(flujo, "name", "")).lower()
        return nombre in ("nul", "nul:", os.devnull.lower())

    if not (_sin_salida(sys.stdout) or _sin_salida(sys.stderr)):
        return
    try:
        carpeta = os.path.join(_dmt_base_dir(), "logs")
        os.makedirs(carpeta, exist_ok=True)
        actual = os.path.join(carpeta, "ultima_sesion.log")
        if os.path.exists(actual):
            try:
                os.replace(actual, os.path.join(carpeta, "sesion_anterior.log"))
            except OSError:
                pass
        flujo = open(actual, "w", encoding="utf-8", errors="replace", buffering=1)
    except Exception:
        flujo = open(os.devnull, "w", encoding="utf-8")
    if _sin_salida(sys.stdout):
        sys.stdout = flujo
    if _sin_salida(sys.stderr):
        sys.stderr = flujo
    _dmt_activar_faulthandler(flujo)


class _DMTBuscadorYtDlpLive:
    """
    Da prioridad a la copia actualizada de yt-dlp / yt-dlp-ejs que el
    actualizador deja en %LOCALAPPDATA%\\DeusMachinaTools\\yt_dlp_live.
    Con Nuitka los módulos compilados se resuelven ANTES que sys.path, así que
    sin este buscador la actualización "se instalaba" pero se seguía usando la
    versión compilada. Con PyInstaller no estorba (resuelve igual).
    """
    PAQUETES = ("yt_dlp", "yt_dlp_ejs")

    def __init__(self, carpeta):
        self.carpeta = carpeta
        self.activo = True

    def _usa_copia_live(self, raiz):
        return os.path.isfile(os.path.join(self.carpeta, raiz, "__init__.py"))

    def find_spec(self, fullname, path=None, target=None):
        if not self.activo:
            return None
        raiz = fullname.partition(".")[0]
        if raiz not in self.PAQUETES or not self._usa_copia_live(raiz):
            return None
        from importlib.machinery import PathFinder
        if fullname == raiz:
            return PathFinder.find_spec(fullname, [self.carpeta])
        padre = sys.modules.get(raiz)
        archivo_padre = os.path.normcase(os.path.abspath(getattr(padre, "__file__", "") or ""))
        if padre is not None and archivo_padre.startswith(os.path.normcase(os.path.abspath(self.carpeta))):
            return PathFinder.find_spec(fullname, path)
        return None


_YTDLP_LIVE_FINDER = None


def _instalar_buscador_ytdlp_live(carpeta):
    """Registra (una sola vez) el buscador prioritario de yt-dlp en builds compilados."""
    global _YTDLP_LIVE_FINDER
    if not _is_frozen_build() or _YTDLP_LIVE_FINDER is not None:
        return
    try:
        _YTDLP_LIVE_FINDER = _DMTBuscadorYtDlpLive(carpeta)
        sys.meta_path.insert(0, _YTDLP_LIVE_FINDER)
    except Exception as e:
        print(f"[YT-DLP SETUP] No se pudo registrar el buscador de actualizaciones: {e}")


def _ytdlp_deshacer_parches_urllib3():
    """
    Al importarse, yt-dlp envuelve urllib3.util.url._PERCENT_RE. Si yt-dlp se
    vuelve a importar en la misma sesión (actualización en caliente), lo envuelve
    DOS veces y todas las descargas fallan con:
      "'Urllib3PercentREOverride' object has no attribute 'sub'"
    Se quita cualquier envoltura previa antes de recargar yt-dlp.
    """
    try:
        import urllib3.util.url as _u
    except Exception:
        return
    for nombre in ("_PERCENT_RE", "PERCENT_RE"):
        obj = getattr(_u, nombre, None)
        original = obj
        while (obj is not None and type(obj).__name__ == "Urllib3PercentREOverride"
               and "re" in getattr(obj, "__dict__", {})):
            obj = obj.__dict__["re"]
        if obj is not original:
            setattr(_u, nombre, obj)


def _ytdlp_purgar_modulos():
    """Saca yt-dlp de sys.modules para volver a importarlo (sin dejar parches duplicados)."""
    for k in [k for k in list(sys.modules) if k.split(".")[0] in _DMTBuscadorYtDlpLive.PAQUETES]:
        sys.modules.pop(k, None)
    _ytdlp_deshacer_parches_urllib3()


def _desactivar_ytdlp_live():
    """Si la copia actualizada está rota, se vuelve a la versión incluida en el build."""
    if _YTDLP_LIVE_FINDER is not None:
        _YTDLP_LIVE_FINDER.activo = False
    _ytdlp_purgar_modulos()


def configurar_ffmpeg_local():
    """
    Busca FFmpeg en la carpeta local 'tools/ffmpeg/bin' y la agrega al PATH
    para que subprocess.run(["ffmpeg", ...]) funcione sin cambiar todo el código.
    También inyecta tools/yt_dlp_live/ en sys.path para que las actualizaciones
    de yt-dlp hechas desde el .exe persistan entre sesiones.
    """
    # 1. Detectar ruta base (ya sea .py o .exe)
    # (_is_frozen_build detecta igual con PyInstaller y con Nuitka, que no usa sys.frozen)
    if _is_frozen_build():
        base_path = os.path.dirname(sys.executable)
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))

    # ── yt-dlp live (actualizaciones persistentes en .exe) ───────────────
    # Ruta en AppData/Local para que siempre sea escribible desde el .exe,
    # sin importar dónde esté instalado el ejecutable.
    _localappdata = os.environ.get("LOCALAPPDATA") or os.path.join(os.path.expanduser("~"), "AppData", "Local")
    _dmt_base     = os.path.join(_localappdata, "DeusMachinaTools")
    yt_live       = os.path.join(_dmt_base, "yt_dlp_live")

    # Crear la carpeta si no existe (primera vez)
    try:
        os.makedirs(yt_live, exist_ok=True)
    except Exception as _mk_e:
        print(f"⚠️ No se pudo crear carpeta yt_dlp_live: {_mk_e}")

    _instalar_buscador_ytdlp_live(yt_live)

    if os.path.isdir(yt_live) and yt_live not in sys.path:
        sys.path.insert(0, yt_live)
        print("")
        print("--- [YT-DLP SETUP] ---")
        print(f"✅ Ruta de actualización inyectada: {yt_live}")
    # ─────────────────────────────────────────────────────────────────────

    # 2. Construir la ruta objetivo
    ffmpeg_local_bin = os.path.join(base_path, "tools", "ffmpeg", "bin")

    # 3. Verificar y vincular
    if os.path.exists(ffmpeg_local_bin):
        print(f"\n--- [FFMPEG SETUP] Encontrado localmente ---")
        # Agregar al principio del PATH para que tenga prioridad sobre cualquier otro ffmpeg instalado
        os.environ["PATH"] = ffmpeg_local_bin + os.pathsep + os.environ["PATH"]
        print(f"✅ Ruta vinculada al sistema: {ffmpeg_local_bin}")
        
        print(f"✅ Ruta vinculada y lista.\n")
    else:
        print(f"ℹ️ No se encontró 'tools/ffmpeg/bin'. Se usará FFmpeg del sistema si existe.")

def configurar_deno_local():
    """
    Busca un binario de Deno (runtime de JavaScript que yt-dlp necesita para
    resolver los retos de YouTube) en, en este orden:
      1) tools/deno/ junto al ejecutable (por si se empaqueta a mano, igual que ffmpeg)
      2) %LOCALAPPDATA%/DeusMachinaTools/tools/deno/ (copia auto-descargada en una sesión previa)
      3) el PATH del sistema
    Si aparece en (1) o (2), agrega esa carpeta al PATH. NO descarga nada aquí
    (de eso se encarga asegurar_deno_disponible(), y solo si el módulo de
    descargas realmente lo necesita). Devuelve la ruta al ejecutable si lo
    encontró, o None si todavía no hay ninguno.
    """
    if _is_frozen_build():
        base_path = os.path.dirname(sys.executable)
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))

    exe_name = "deno.exe" if os.name == "nt" else "deno"
    candidatos = [
        os.path.join(base_path, "tools", "deno"),
        os.path.join(_dmt_base_dir(), "tools", "deno"),
    ]

    for carpeta in candidatos:
        ruta = os.path.join(carpeta, exe_name)
        if os.path.isfile(ruta):
            if carpeta not in os.environ.get("PATH", "").split(os.pathsep):
                os.environ["PATH"] = carpeta + os.pathsep + os.environ.get("PATH", "")
            print(f"✅ [DENO SETUP] Encontrado localmente: {ruta}")
            return ruta

    ruta_sistema = shutil.which("deno")
    if ruta_sistema:
        print(f"✅ [DENO SETUP] Usando Deno del sistema: {ruta_sistema}")
        return ruta_sistema

    print("ℹ️ [DENO SETUP] No se encontró Deno todavía (se descarga solo si el módulo de descargas lo necesita).")
    return None

_DENO_DOWNLOAD_LOCK = threading.Lock()

def asegurar_deno_disponible(status_cb=None):
    """
    Se llama justo antes de una descarga que podría necesitar YouTube/Deno.
    Si Deno ya está disponible (PATH) no hace nada. Si no, lo descarga UNA
    sola vez desde el release oficial de GitHub (binario oficial, licencia
    MIT, el mismo que instala el script oficial de Deno) a
    %LOCALAPPDATA%/DeusMachinaTools/tools/deno/ y lo agrega al PATH de este
    proceso. Si falla (sin internet, etc.) no rompe nada: yt-dlp sigue
    funcionando igual que hoy, solo sin el runtime de JS.
    Devuelve True si Deno quedó disponible, False si no.
    """
    def _avisar(msg):
        if status_cb:
            try: status_cb(msg)
            except Exception: pass

    if shutil.which("deno"):
        return True

    if os.name != "nt":
        # Descarga automática cubierta por ahora solo para Windows.
        return False

    with _DENO_DOWNLOAD_LOCK:
        if shutil.which("deno"):
            return True  # otro hilo ya lo dejó listo mientras esperábamos el lock

        import urllib.request as _req, zipfile as _zip

        destino_dir = os.path.join(_dmt_base_dir(), "tools", "deno")
        zip_path = os.path.join(destino_dir, "_deno_download.zip")
        try:
            os.makedirs(destino_dir, exist_ok=True)
            _avisar("Descargando Deno (una sola vez, ~40 MB)...")
            url = "https://github.com/denoland/deno/releases/latest/download/deno-x86_64-pc-windows-msvc.zip"
            zip_path = os.path.join(destino_dir, "_deno_download.zip")
            peticion = _req.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with _req.urlopen(peticion, timeout=90) as resp, open(zip_path, "wb") as f:
                shutil.copyfileobj(resp, f)

            _avisar("Extrayendo Deno...")
            with _zip.ZipFile(zip_path, "r") as z:
                z.extractall(destino_dir)
            os.remove(zip_path)

            exe = os.path.join(destino_dir, "deno.exe")
            if not os.path.isfile(exe):
                raise RuntimeError("El zip descargado no contenía deno.exe")

            if destino_dir not in os.environ.get("PATH", "").split(os.pathsep):
                os.environ["PATH"] = destino_dir + os.pathsep + os.environ.get("PATH", "")

            print(f"✅ [DENO SETUP] Descargado e instalado en: {exe}")
            _avisar("Deno listo.")
            return True
        except Exception as e:
            print(f"⚠️ [DENO SETUP] No se pudo descargar Deno automáticamente: {e}")
            _avisar("No se pudo descargar Deno (se continúa sin él).")
            return False
        finally:
            try:
                if os.path.exists(zip_path):
                    os.remove(zip_path)
            except OSError:
                pass

def _yt_opts_robustos():
    """
    Opciones extra para sumar a CUALQUIER yt_dlp.YoutubeDL(...) del módulo de
    descargas: runtime de JS (si Deno está disponible). Si no está
    disponible, devuelve {} y yt-dlp sigue funcionando exactamente igual que
    antes — nunca bloquea nada ni truena la app.

    OJO con impersonation/curl_cffi: NO se fuerza un 'impersonate' aquí a
    propósito. Con curl_cffi solo instalado (sin tocar ydl_opts), cada
    extractor (TikTok, Instagram, etc.) ya pide impersonation por su cuenta
    y yt-dlp elige un target válido y soportado automáticamente — forzar un
    string fijo como "chrome" aquí rompe TODAS las descargas si ese target
    exacto no está entre los que soporta la versión de curl_cffi instalada.
    """
    extra = {}
    try:
        if shutil.which("deno"):
            extra["js_runtimes"] = {"deno": {}}
    except Exception:
        pass
    return extra

class _YtDlpDiagLogger:
    """
    Logger para yt-dlp que descarta el ruido del modo verbose (encodings,
    conteo de extractores, handlers de red, etc.) y deja pasar solo los
    warnings/errores reales, con el mismo formato "WARNING:"/"ERROR:" que
    yt-dlp usa por defecto — así no se pierde visibilidad de errores como el
    de TikTok, pero la consola queda limpia.
    """

    def debug(self, msg):
        pass

    def info(self, msg):
        pass

    def warning(self, msg):
        print(f"WARNING: {msg}")

    def error(self, msg):
        print(f"ERROR: {msg}")

def _yt_opts_diagnostico():
    """
    Opciones para sumar SOLO a la llamada principal de descarga (no a las de
    solo-extraer-info, para no repetir el mismo diagnóstico 3-4 veces por
    descarga): activa 'verbose' pero con un logger propio que filtra el
    ruido y deja ver si curl_cffi/Deno realmente están siendo usados.
    """
    return {"logger": _YtDlpDiagLogger()}

# Descargas (YouTube / Spotify) que pueden estar BAJANDO a la vez. Las que ya
# bajaron y solo están convirtiendo o empaquetando no cuentan: al llegar a ese
# paso sueltan su lugar y arranca la siguiente de la cola.
YT_MAX_DESCARGAS = 3


class _YtDetenido(Exception):
    """La descarga se pausó o canceló mientras esperaba su turno en la cola."""


def _esperar_entre_items(segundos, debe_parar, on_tick=None):
    """
    Espera 'segundos' (en pasos cortos, para poder cortar antes si
    debe_parar() se vuelve True en pleno espera) entre items de un
    batch/playlist —descargas o transcripción— para no golpear el servidor
    con pedidos muy seguidos (menos probabilidad de bloqueos tipo
    TikTok/YouTube).
    on_tick(segundos_restantes) opcional: se llama para que la UI muestre
    que está esperando A PROPÓSITO, y no dé la impresión de que se quedó
    pegada procesando.
    """
    fin = time.time() + segundos
    while time.time() < fin:
        if debe_parar():
            return
        restantes = fin - time.time()
        if on_tick:
            try: on_tick(max(0, int(round(restantes))))
            except Exception: pass
        time.sleep(min(0.5, max(0.0, restantes)))

_SPOTDL_LOCK = threading.Lock()

# ------------------------------------------------------------------------------
#  SUBPROCESOS DE MÓDULOS PYTHON (spotDL) QUE FUNCIONAN TAMBIÉN COMPILADO
# ------------------------------------------------------------------------------
# Compilado (PyInstaller o Nuitka), sys.executable es DEUS_MACHINA_TOOLS.exe, así
# que "sys.executable -m spotdl" abriría OTRA instancia de la app. En ese caso el
# propio .exe se relanza con un argumento interno y corre el módulo sin interfaz.
_DMT_ARG_MODULO = "--dmt-run-module"
_DMT_MODULOS_PERMITIDOS = ("spotdl",)


def _cmd_modulo_python(modulo):
    """Equivalente a [python, '-m', modulo] válido en .py, PyInstaller y Nuitka."""
    if _is_frozen_build():
        return [sys.executable, _DMT_ARG_MODULO, modulo]
    return [sys.executable, "-m", modulo]


def _env_subproceso_utf8():
    """Entorno para subprocesos Python: salida en UTF-8 (títulos con acentos)."""
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"
    env["PYTHONUTF8"] = "1"
    return env


def _dmt_stdio_para_subproceso():
    """
    En builds sin consola, sys.stdout/stderr pueden ser None (o apuntar a NUL)
    aunque el proceso padre haya conectado tuberías. Se reconectan a los handles
    reales para que el padre pueda leer el avance.
    """
    if os.name != "nt":
        return
    try:
        import msvcrt
        k32 = ctypes.windll.kernel32
        k32.GetStdHandle.restype = ctypes.c_void_p
        k32.GetFileType.argtypes = [ctypes.c_void_p]
        invalido = ctypes.c_void_p(-1).value
    except Exception:
        return
    for nombre, std_id in (("stdout", -11), ("stderr", -12)):
        try:
            h = k32.GetStdHandle(std_id)
            if not h or h == invalido or k32.GetFileType(h) == 0:
                raise OSError("sin handle")
            fd = msvcrt.open_osfhandle(h, os.O_WRONLY)
            flujo = open(fd, "w", encoding="utf-8", errors="replace", buffering=1, closefd=False)
            setattr(sys, nombre, flujo)
        except Exception:
            if getattr(sys, nombre, None) is None:
                setattr(sys, nombre, open(os.devnull, "w", encoding="utf-8"))


def _dmt_despachar_modulo_si_corresponde():
    """
    Si el .exe se lanzó como 'DEUS_MACHINA_TOOLS.exe --dmt-run-module <mod> ...',
    ejecuta ese módulo SIN crear ninguna ventana y termina el proceso.
    """
    if len(sys.argv) < 3 or sys.argv[1] != _DMT_ARG_MODULO:
        return
    modulo = sys.argv[2]
    if modulo not in _DMT_MODULOS_PERMITIDOS:
        os._exit(2)
    _dmt_stdio_para_subproceso()
    sys.argv = [modulo] + sys.argv[3:]
    codigo = 0
    try:
        if modulo == "spotdl":
            # Import directo (runpy no sirve con módulos compilados por Nuitka)
            from spotdl.console import console_entry_point
            console_entry_point()
    except SystemExit as e:
        if isinstance(e.code, int):
            codigo = e.code
        elif e.code is None:
            codigo = 0
        else:
            print(e.code)
            codigo = 1
    except BaseException:
        import traceback as _tb
        _tb.print_exc()
        codigo = 1
    finally:
        for flujo in (sys.stdout, sys.stderr):
            try:
                flujo.flush()
            except Exception:
                pass
    os._exit(codigo)

def es_url_spotify(url):
    """True si la URL es de open.spotify.com (canción, álbum o playlist)."""
    try:
        return "open.spotify.com" in (url or "").lower()
    except Exception:
        return False

def _startup_info_modulo():
    """Igual que App.get_startup_info(), pero para funciones a nivel de módulo (sin self)."""
    if os.name == 'nt':
        si = subprocess.STARTUPINFO()
        si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        return si
    return None

def asegurar_spotdl_disponible(status_cb=None):
    """
    Verifica que el paquete 'spotdl' esté disponible (es un paquete de
    Python normal, se instala con pip). Si no está, intenta instalarlo una
    vez. No crítico: si falla, se avisa y ese task en particular termina en
    error, sin afectar al resto de la app.
    Devuelve True si spotdl quedó disponible, False si no.
    """
    def _avisar(msg):
        if status_cb:
            try: status_cb(msg)
            except Exception: pass

    with _SPOTDL_LOCK:
        if _is_frozen_build():
            # Compilado: spotDL tiene que venir DENTRO del build (no se puede
            # instalar con pip en un .exe). Se revisa sin lanzar procesos.
            try:
                import importlib.util as _ilu
                if _ilu.find_spec("spotdl") is not None:
                    return True
            except Exception:
                pass
            print("[spotDL setup] spotDL no está incluido en esta compilación.")
            _avisar("spotDL no está incluido en esta compilación.")
            return False

        try:
            r = subprocess.run(
                _cmd_modulo_python("spotdl") + ["--version"],
                capture_output=True, text=True, timeout=20,
                startupinfo=_startup_info_modulo(), env=_env_subproceso_utf8()
            )
            if r.returncode == 0:
                return True
        except Exception:
            pass

        try:
            _avisar("Instalando spotDL (una sola vez)...")
            r = subprocess.run(
                [sys.executable, "-m", "pip", "install", "--upgrade", "spotdl"],
                capture_output=True, text=True, timeout=180,
                startupinfo=_startup_info_modulo()
            )
            if r.returncode != 0:
                print(f"[spotDL setup] No se pudo instalar: {r.stderr.strip()[:300]}")
                _avisar("No se pudo instalar spotDL.")
                return False
            _avisar("spotDL listo.")
            return True
        except Exception as e:
            print(f"[spotDL setup] Excepción instalando: {e}")
            _avisar("No se pudo instalar spotDL.")
            return False

def cargar_librerias_pesadas_global(progress_callback=None):
    """
    Carga librerías pesadas, configura GPU (ANTES de importar) y silencia logs visuales.
    """
    global torch, faster_whisper, yt_dlp, wmi, comtypes, PyPDF2, fitz, cv2, np, WhisperModel

    def _report(pct, msg):
        try:
            if progress_callback: progress_callback(int(pct), str(msg))
        except: pass

    # =======================================================
    # 1. STACK CUDA 12.9 (ANTES DE IMPORTAR NADA)
    #    torch 2.8.0+cu129 trae en torch\lib TODAS las DLLs de CUDA 12.9 y
    #    cuDNN 9.10 que usan torch, CTranslate2 (faster-whisper) y PaddlePaddle.
    #    Ya NO se agregan rutas manuales (carpeta 'bin' ni nvidia\cublas) al
    #    PATH: eso podia mezclar versiones. Solo se avisa si hay DLLs nvidia
    #    de pip que chocarian con las de torch.
    # =======================================================
    if os.name == 'nt':
        print("\n--- [GPU SETUP] Stack CUDA 12.9 / cuDNN 9.10 (DLLs de NVIDIA, sin cargar PyTorch) ---")
        _avisar_dlls_nvidia_de_pip()
    # =======================================================

    # =======================================================
    # 2. CARGA DE LIBRERÍAS TIER-1 EN PARALELO (rápidas, seguras)
    #    Tier-2 (torch, whisper, yt_dlp) se carga en
    #    background una vez que la ventana principal ya se ve.
    # =======================================================
    # PyMuPDF se importa como 'pymupdf' (el nombre 'fitz' está obsoleto y avisa
    # en consola), pero se guarda en la variable global 'fitz' para no tocar el
    # resto del código.
    tier1 = [('numpy', 'np'), ('cv2', 'cv2'), ('PyPDF2', 'PyPDF2'), ('pymupdf', 'fitz')]

    _report(15, "")

    def _load_one(args):
        module_name, var_name = args
        try:
            mod = importlib.import_module(module_name)
            globals()[var_name] = mod
        except Exception as e:
            print(f"Error cargando {module_name}: {e}")
            globals()[var_name] = None

    with concurrent.futures.ThreadPoolExecutor(max_workers=len(tier1)) as pool:
        futures = {pool.submit(_load_one, item): item for item in tier1}
        done = 0
        for fut in concurrent.futures.as_completed(futures):
            done += 1
            _report(15 + int((done / len(tier1)) * 70), "")

    # PyMuPDF imprime en consola errores de PDFs con imágenes dañadas
    # ("MuPDF error: ... image height is zero"); no afectan el resultado.
    try:
        if fitz is not None:
            fitz.TOOLS.mupdf_display_errors(False)
    except Exception:
        pass

    # Reportar fin al Splash (Texto vacío para la transición limpia al verde)
    _report(100, "")
    print("Tier-1 listo. Tier-2 (CUDA/whisper/ytdlp) cargará en background.")
    return {'torch': False}




# ==============================================================================
#  TIER-2: carga en background una vez que la ventana principal ya es visible
# ==============================================================================
_tier2_listo = threading.Event()  # se activa cuando torch/whisper/ytdlp están listos

def _cargar_tier2_background():
    """
    Carga las librerías pesadas en hilos paralelos.
    Se llama desde App.__init__ justo después de que la ventana se muestra,
    así el usuario no espera el splash por estas libs.
    El GPU-rescue ya corrió en el splash, así que el entorno está preparado.
    """
    global torch, faster_whisper, yt_dlp, WhisperModel

    # 1) CUDA PRIMERO y SOLO: se precargan las DLL de CUDA 12.9 / cuDNN 9.10
    #    (sin importar PyTorch); CTranslate2 y PaddlePaddle reutilizan esas
    #    mismas. Hacerlo en paralelo con otras librerias GPU volvia el orden
    #    de carga de DLLs aleatorio.
    try:
        globals()['torch'] = _cuda_iniciar()
        tipo = "sin PyTorch" if getattr(torch, "ligero", False) else "con PyTorch"
        print(f"[Tier-2] ✅ Soporte CUDA preparado ({tipo})")
    except Exception as e:
        print(f"[Tier-2] ⚠️ CUDA no disponible: {e}")
        globals()['torch'] = DummyTorch()   # la UI sigue preguntando por .cuda sin romperse

    # 2) El resto en paralelo (PaddleOCR/RapidOCR se cargan solo al usar el OCR)
    tier2 = [
        ('faster_whisper',  'faster_whisper'),
        ('yt_dlp',          'yt_dlp'),
    ]

    def _load_one(args):
        module_name, var_name = args
        try:
            mod = importlib.import_module(module_name)
            globals()[var_name] = mod
            print(f"[Tier-2] ✅ {module_name} listo")
        except Exception as e:
            if module_name == "yt_dlp" and _YTDLP_LIVE_FINDER is not None and _YTDLP_LIVE_FINDER.activo:
                print(f"[Tier-2] ⚠️ yt-dlp actualizado no cargó ({e}); se usa el incluido en la app.")
                _desactivar_ytdlp_live()
                try:
                    globals()[var_name] = importlib.import_module(module_name)
                    print(f"[Tier-2] ✅ {module_name} listo (versión incluida)")
                    return
                except Exception as e2:
                    e = e2
            print(f"[Tier-2] ⚠️ {module_name} no disponible: {e}")
            globals()[var_name] = None

    with concurrent.futures.ThreadPoolExecutor(max_workers=len(tier2)) as pool:
        futs = [pool.submit(_load_one, item) for item in tier2]
        concurrent.futures.wait(futs)

    # Configurar WhisperModel y verificar CUDA
    try:
        if faster_whisper is not None:
            globals()['WhisperModel'] = getattr(faster_whisper, 'WhisperModel', None)
    except: pass

    try:
        if torch is not None and not isinstance(torch, type(None)):
            if torch.cuda.is_available():
                print(f"[Tier-2] ✅ CUDA lista: {torch.cuda.get_device_name(0)}")
            else:
                motivo = getattr(torch.cuda, "motivo", "")
                print("[Tier-2] ⚠️ CUDA no disponible, se usará CPU." + (f" ({motivo})" if motivo else ""))
    except: pass

    _tier2_listo.set()
    print("[Tier-2] 🚀 Todas las librerías pesadas están listas.")


# ==============================================================================
#  GESTOR DE MODELOS DE IA (Whisper · OCR · Quitar fondo)
# ==============================================================================
class GestorModelosIA:
    """
    Mantiene UN solo modelo pesado de IA en memoria a la vez:
      · antes de cargar un modelo se libera el de los OTROS módulos; si alguno
        está trabajando en ese momento no se le interrumpe: se libera en
        cuanto termina;
      · un modelo que no se usa durante 20 minutos se descarga solo.
    Cada módulo registra su función 'liberar' (debe ser segura desde cualquier hilo).
    """
    INACTIVIDAD_S = 20 * 60
    REVISION_S = 30

    def __init__(self):
        self._cond = threading.Condition(threading.RLock())
        self._mods = {}
        self._vigilante = None

    def registrar(self, nombre, liberar):
        with self._cond:
            self._mods[nombre] = {"liberar": liberar, "cargado": False, "en_uso": 0,
                                  "ultimo": time.time(), "pendiente": False, "liberando": False}
        self._asegurar_vigilante()

    def antes_de_cargar(self, nombre):
        """Libera los modelos de los demás módulos (o los marca para liberarlos al terminar)."""
        _dmt_registrar_dlls(f"antes de cargar '{nombre}'")
        a_liberar = []
        with self._cond:
            for otro, m in self._mods.items():
                if otro == nombre or not m["cargado"]:
                    continue
                if m["en_uso"] > 0:
                    m["pendiente"] = True
                else:
                    a_liberar.append(otro)
        for otro in a_liberar:
            self._liberar(otro, f"se va a cargar el modelo de '{nombre}'")

    def marcar_cargado(self, nombre):
        with self._cond:
            m = self._mods.get(nombre)
            if m:
                m["cargado"] = True
                m["pendiente"] = False
                m["ultimo"] = time.time()

    def marcar_descargado(self, nombre):
        with self._cond:
            m = self._mods.get(nombre)
            if m:
                m["cargado"] = False
                m["pendiente"] = False

    def cargado(self, nombre):
        with self._cond:
            m = self._mods.get(nombre)
            return bool(m and m["cargado"])

    @contextlib.contextmanager
    def en_uso(self, nombre):
        """Mientras dure el bloque, el modelo de 'nombre' no se libera."""
        with self._cond:
            m = self._mods.get(nombre)
            if m is not None:
                while m["liberando"]:
                    self._cond.wait(0.5)
                m["en_uso"] += 1
        try:
            yield
        finally:
            liberar_ahora = False
            with self._cond:
                if m is not None:
                    m["en_uso"] = max(0, m["en_uso"] - 1)
                    m["ultimo"] = time.time()
                    liberar_ahora = m["en_uso"] == 0 and m["pendiente"] and m["cargado"]
            if liberar_ahora:
                self._liberar(nombre, "otro módulo cargó su modelo mientras trabajaba")

    def _liberar(self, nombre, motivo):
        with self._cond:
            m = self._mods.get(nombre)
            if not m or not m["cargado"] or m["en_uso"] > 0 or m["liberando"]:
                return
            m["liberando"] = True
            m["pendiente"] = False
            fn = m["liberar"]
        print(f"[Modelos IA] Liberando '{nombre}' ({motivo}).")
        try:
            fn()
        except Exception as e:
            print(f"[Modelos IA] Error liberando '{nombre}': {e}")
        finally:
            with self._cond:
                m["cargado"] = False
                m["liberando"] = False
                self._cond.notify_all()

    def _asegurar_vigilante(self):
        with self._cond:
            if self._vigilante is not None:
                return
            self._vigilante = threading.Thread(target=self._vigilar, name="dmt_modelos_ia", daemon=True)
            self._vigilante.start()

    def _vigilar(self):
        while True:
            time.sleep(self.REVISION_S)
            ahora = time.time()
            with self._cond:
                vencidos = [n for n, m in self._mods.items()
                            if m["cargado"] and m["en_uso"] == 0 and not m["liberando"]
                            and ahora - m["ultimo"] >= self.INACTIVIDAD_S]
            for n in vencidos:
                self._liberar(n, "20 minutos sin uso")


class _TrabajoDetenido(Exception):
    """Se canceló el trabajo mientras esperaba su turno."""


class LoteTrabajo:
    """
    Un lote de archivos en curso de UN módulo. Cada módulo tiene el suyo, así
    pueden trabajar VARIOS A LA VEZ (convertir video mientras se comprimen
    imágenes, por ejemplo) sin pisarse las banderas de cancelar, los procesos
    externos (FFmpeg, Ghostscript) ni el resumen final.
    """
    NOMBRES = {
        "video": "Conversión de video",
        "image": "Conversión de imágenes",
        "audio": "Conversión de audio",
        "ocr": "Extracción de texto (OCR)",
        "transcribe": "Transcripción",
    }

    def __init__(self, modo, cola=()):
        self.modo = modo
        self.cola = list(cola)
        self.saltar = False        # SALTAR: salta el archivo en curso
        self.cortar = False        # CANCELAR: termina el actual y corta la cola
        self.proceso = None        # proceso externo en curso (FFmpeg, Ghostscript...)
        self.hilo = None
        self.inicio = time.time()

    @property
    def nombre(self):
        return self.NOMBRES.get(self.modo, self.modo)


class CarrilIA:
    """
    Carril EXCLUSIVO para lo que carga modelos de IA (OCR, Transcripción,
    Quitar fondo): dos modelos grandes a la vez saturan la RAM/VRAM y terminan
    más lento (o revientan). Aquí trabaja uno y los demás esperan turno en
    orden de llegada, avisando en pantalla a quién esperan.

    Lo que NO usa IA (video, audio, imágenes, PDF, descargas) no pasa por aquí:
    eso sí corre en paralelo.
    """

    def __init__(self):
        self._cond = threading.Condition()
        self._dueno = None          # (clave, etiqueta)
        self._hilo = None           # hilo dueño (para permitir anidar)
        self._veces = 0
        self._cola = []

    def ocupado_por(self, salvo=None):
        """Etiqueta de quien está trabajando ahora (None si está libre)."""
        with self._cond:
            if self._dueno and self._dueno[0] != salvo:
                return self._dueno[1]
            return None

    @contextlib.contextmanager
    def turno(self, clave, etiqueta, on_espera=None, debe_cortar=None):
        """
        Reserva el carril mientras dure el bloque.
          · on_espera(quien): se llama UNA vez si hay que esperar.
          · debe_cortar(): si se vuelve True mientras espera, lanza _TrabajoDetenido.
        """
        yo = threading.current_thread()
        with self._cond:
            if self._dueno and self._dueno[0] == clave and self._hilo is yo:
                self._veces += 1            # mismo módulo y mismo hilo: no se bloquea
            else:
                turno = object()
                self._cola.append(turno)
                avisado = False
                try:
                    while self._dueno is not None or self._cola[0] is not turno:
                        if debe_cortar and debe_cortar():
                            raise _TrabajoDetenido(self._dueno[1] if self._dueno else "")
                        if not avisado and on_espera and self._dueno:
                            avisado = True
                            try:
                                on_espera(self._dueno[1])
                            except Exception:
                                pass
                        self._cond.wait(0.3)
                    self._cola.remove(turno)
                except BaseException:
                    if turno in self._cola:
                        self._cola.remove(turno)
                    self._cond.notify_all()
                    raise
                self._dueno = (clave, etiqueta)
                self._hilo = yo
                self._veces = 1
        try:
            yield
        finally:
            with self._cond:
                self._veces -= 1
                if self._veces <= 0:
                    self._dueno = None
                    self._hilo = None
                    self._veces = 0
                self._cond.notify_all()


def _asegurar_numba_o_sustituto():
    """
    pymatting (dependencia de rembg) importa numba solo por sus decoradores
    (njit, prange, pndindex). Nuitka no soporta numba en standalone, así que ahí
    se excluye y se usa este sustituto mínimo: esas funciones corren en Python
    normal. DMT no usa el "alpha matting" de rembg, así que el resultado y la
    velocidad de Quitar fondo no cambian. Si numba está disponible, no se toca.
    """
    if "numba" in sys.modules:
        return
    try:
        import numba  # noqa: F401
        return
    except Exception:
        pass
    import types
    import numpy as _np_numba

    sustituto = types.ModuleType("numba")

    def njit(*args, **kwargs):
        if len(args) == 1 and callable(args[0]) and not kwargs:
            return args[0]
        return lambda funcion: funcion

    sustituto.njit = njit
    sustituto.jit = njit
    sustituto.prange = range
    sustituto.pndindex = _np_numba.ndindex
    sustituto.__version__ = "0+sustituto-dmt"
    sys.modules["numba"] = sustituto
    print("[rembg] numba no está disponible: se usa un sustituto (sin efecto en Quitar fondo).")


def _rembg_quitar_fondo(img, session, remove_fn):
    """
    Quita el fondo con rembg. Si la imagen YA trae transparencia, el modelo la
    ve compuesta sobre blanco (como la ve el usuario) y la máscara se combina
    con su canal alfa original (antes, un PNG/PSD transparente podía salir vacío).
    """
    from PIL import ImageChops
    if img.mode != "RGBA":
        img = img.convert("RGBA")
    alfa = img.getchannel("A")
    if alfa.getextrema()[0] < 255:
        res = remove_fn(_img_sobre_blanco(img), session=session)
        if res.mode != "RGBA":
            res = res.convert("RGBA")
        salida = img.copy()
        salida.putalpha(ImageChops.multiply(res.getchannel("A"), alfa))
        return salida
    return remove_fn(img, session=session)


# ==============================================================================
#  MOTOR OCR: PaddleOCR (GPU / CPU) + RapidOCR (CPU)
# ==============================================================================
OCR_MODELO_DET = "PP-OCRv6_medium_det"
OCR_MODELO_REC = "PP-OCRv6_medium_rec"
# Lado mayor para la DETECCIÓN en Paddle CPU. El propio pipeline de PaddleX solo
# reduce (proporcional) si la imagen lo supera; nunca amplía. El reconocimiento
# siempre recorta de la imagen original. (960 perdía precisión; 1920 quedaba corto
# en fotos grandes frente a GPU, que trabaja a resolución completa hasta 4000 px.)
OCR_LIMITE_CPU = 2560
OCR_CC_MINIMA = (7, 5)         # PaddlePaddle cu129 esta compilado para Turing (7.5) o posterior
OCR_NOMBRES = {
    "paddle_gpu": "PaddleOCR GPU",
    "paddle_cpu": "PaddleOCR CPU",
    "rapid_cpu":  "RapidOCR CPU",
}
# Tarjetas del selector de motor: (clave, título, descripción)
OCR_TARJETAS = (
    ("paddle_gpu", "🚀 PaddleOCR · GPU", "Máxima precisión, rápido"),
    ("paddle_cpu", "🎯 PaddleOCR · CPU", "Máxima precisión, lento"),
    ("rapid_cpu",  "⚡ RapidOCR · CPU",  "Rápido y ligero"),
)
OCR_TEXTO_DROP_VACIO = "🧠 Arrastra PDF o IMÁGENES aquí\n(o click para buscar)"
# Estado bajo la barra, con el estilo de Transcripción: fase -> (ícono, color del texto).
# "descargando" y "copiando" son variantes de "cargando" (el motor baja o copia sus modelos).
OCR_FASES = {
    "inactivo":    ("", "gray"),
    "esperando":   ("⏳", "#d4ac0d"),
    "preparando":  ("📄", "#3498db"),
    "cargando":    ("📂", "cyan"),
    "descargando": ("⬇️", "#e67e22"),
    "copiando":    ("📦", "#3498db"),
    "escaneando":  ("🔍", "#2cc985"),
    "nativo":      ("📑", "#27ae60"),
    "guardando":   ("💾", "#f0b27a"),
    "saltando":    ("⏭️", "orange"),
    "saltado":     ("⏭️", "orange"),
    "error":       ("❌", "#e74c3c"),
    "con_errores": ("⚠️", "#f39c12"),
    "listo":       ("✅", "#2cc985"),
}
OCR_RELOJ_VACIO = "⏱️ --:--:--"
OCR_COLOR_RELOJ = "#d4ac0d"          # cronómetro en marcha (igual que Transcripción)
OCR_COLOR_RELOJ_FIN = "#2cc985"      # tiempo total al terminar
# PDF: cada página se decide por separado. Con al menos estos caracteres de texto
# real se extrae directo; si no (página escaneada), se lee con el motor OCR.
OCR_MIN_CHARS_PAGINA = 50
# Resolución a la que se rasterizan las páginas escaneadas de un PDF para el OCR.
# 200 DPI es el punto óptimo medido (A4 escaneadas a 200/300 DPI, texto de 6 a
# 12 pt): PaddleOCR queda en ~0 % de error, igual que a 300 DPI pero ~45 % más
# rápido; a 144 DPI se pierden letras en texto de 8 pt o menos. RapidOCR reduce
# por dentro a ~2000 px de lado, así que más de ~170 DPI no le cambia nada.
OCR_DPI_PDF = 200


class _OcrSinMotor(Exception):
    """No se pudo cargar ningún motor OCR (el aviso al usuario ya se mostró)."""


def _ocr_dir_base_app():
    if _is_frozen_build():
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))


_OCR_DIR_PADDLE = None


def _dir_escribible(carpeta):
    try:
        os.makedirs(carpeta, exist_ok=True)
        prueba = os.path.join(carpeta, f".dmt_prueba_{os.getpid()}")
        with open(prueba, "w") as fh:
            fh.write("ok")
        os.remove(prueba)
        return True
    except OSError:
        return False


def _ocr_dir_paddle():
    """
    tools/paddleocr: cache de PaddleX y modelos descargados (official_models).
    Junto al programa si ya trae los modelos o si se puede escribir ahí; si no
    (instalado en una carpeta protegida), en %LOCALAPPDATA%\\DeusMachinaTools.
    """
    global _OCR_DIR_PADDLE
    if _OCR_DIR_PADDLE:
        return _OCR_DIR_PADDLE
    junto = os.path.join(_ocr_dir_base_app(), "tools", "paddleocr")
    trae_modelos = all(_ocr_modelo_completo(os.path.join(junto, "official_models", n))
                       for n in (OCR_MODELO_DET, OCR_MODELO_REC))
    if trae_modelos or _dir_escribible(junto):
        _OCR_DIR_PADDLE = junto
    else:
        _OCR_DIR_PADDLE = os.path.join(_dmt_base_dir(), "tools", "paddleocr")
        print(f"[OCR] Carpeta del programa sin permisos de escritura; modelos en {_OCR_DIR_PADDLE}")
    return _OCR_DIR_PADDLE


def _ocr_modelo_completo(carpeta):
    try:
        if not os.path.isfile(os.path.join(carpeta, "inference.yml")):
            return False
        return any(f.lower().endswith((".pdiparams", ".safetensors", ".onnx"))
                   for f in os.listdir(carpeta))
    except OSError:
        return False


def _ocr_ruta_modelo(nombre):
    return os.path.join(_ocr_dir_paddle(), "official_models", nombre)


def _ocr_asegurar_modelo(nombre, avisar=None):
    """
    Devuelve la carpeta local del modelo si ya esta completa en tools/paddleocr.
    Si no, devuelve None y PaddleX lo descarga ahi mismo (PADDLE_PDX_CACHE_HOME).
    Si existe en la cache de usuario de PaddleX (~/.paddlex) se copia en vez de descargar.
    """
    destino = _ocr_ruta_modelo(nombre)
    if _ocr_modelo_completo(destino):
        return destino
    if os.path.isdir(destino):
        # Descarga previa incompleta: se aparta (no se borra) para que PaddleX la rehaga
        apartado = f"{destino}_incompleto_{int(time.time())}"
        try:
            os.rename(destino, apartado)
            print(f"[OCR] Modelo incompleto apartado: {apartado}")
        except OSError as e:
            print(f"[OCR] No se pudo apartar {destino}: {e}")
    cache_usuario = os.path.join(os.path.expanduser("~"), ".paddlex", "official_models", nombre)
    if (_ocr_modelo_completo(cache_usuario)
            and os.path.normcase(os.path.abspath(cache_usuario)) != os.path.normcase(os.path.abspath(destino))):
        try:
            if avisar:
                avisar(f"Motor: copiando {nombre} a tools…", "#3498db")
            os.makedirs(os.path.dirname(destino), exist_ok=True)
            shutil.copytree(cache_usuario, destino)
            print(f"[OCR] Modelo copiado desde la cache de usuario: {nombre}")
            return destino
        except Exception as e:
            print(f"[OCR] No se pudo copiar {nombre}: {e}")
            shutil.rmtree(destino, ignore_errors=True)
    return None


def _ocr_preparar_entorno_paddle():
    """Debe correr ANTES del primer import de paddleocr/paddlex."""
    base = _ocr_dir_paddle()
    os.makedirs(base, exist_ok=True)
    os.environ["PADDLE_PDX_CACHE_HOME"] = base
    os.environ.setdefault("PADDLE_PDX_DISABLE_MODEL_SOURCE_CHECK", "True")


def _ocr_stdio_seguro():
    """En builds sin consola sys.stdout/stderr son None y PaddleX escribe logs ahi."""
    try:
        if sys.stdout is None:
            sys.stdout = open(os.devnull, "w", encoding="utf-8")
        if sys.stderr is None:
            sys.stderr = open(os.devnull, "w", encoding="utf-8")
    except Exception:
        pass


def _ocr_vaciar_cache_paddle():
    try:
        paddle = sys.modules.get("paddle")
        if (paddle is not None and paddle.device.is_compiled_with_cuda()
                and paddle.device.cuda.device_count() > 0):
            paddle.device.cuda.empty_cache()
    except Exception as e:
        print(f"[OCR] No se pudo vaciar la cache de Paddle: {e}")


def _ocr_crear_paddle(gpu, avisar=None):
    # Invariante: las DLLs CUDA/cuDNN ya estan precargadas (_cuda_preparar_dlls).
    _ocr_preparar_entorno_paddle()
    _ocr_stdio_seguro()
    det_dir = _ocr_asegurar_modelo(OCR_MODELO_DET, avisar)
    rec_dir = _ocr_asegurar_modelo(OCR_MODELO_REC, avisar)
    if avisar and not (det_dir and rec_dir):
        avisar("Motor: descargando modelos PP-OCRv6 en tools (solo la primera vez)…", "#3498db")
    from paddleocr import PaddleOCR
    kw = dict(
        use_doc_orientation_classify=False,
        use_doc_unwarping=False,
        use_textline_orientation=False,
        text_detection_model_name=OCR_MODELO_DET,
        text_recognition_model_name=OCR_MODELO_REC,
    )
    if det_dir:
        kw["text_detection_model_dir"] = det_dir
    if rec_dir:
        kw["text_recognition_model_dir"] = rec_dir
    if gpu:
        kw["device"] = "gpu:0"
    else:
        # enable_mkldnn=False: con PaddlePaddle 3.3.1 sigue el error
        # ConvertPirAttribute2RuntimeAttribute en la ruta oneDNN/PIR.
        kw.update(device="cpu", enable_mkldnn=False,
                  text_det_limit_type="max", text_det_limit_side_len=OCR_LIMITE_CPU)
    return PaddleOCR(**kw)


def _ocr_proceso_principal(conn):
    """
    Punto de entrada del PROCESO del motor OCR (multiprocessing, modo spawn).
    Funciona igual en .py, PyInstaller y Nuitka (freeze_support está en el main).
    """
    # Silencia los avisos informativos del registro C++ de Paddle (glog), como
    # "Please NOTE: device: 0, GPU Compute Capability...". Los errores siguen saliendo.
    os.environ.setdefault("GLOG_minloglevel", "2")
    _ocr_stdio_seguro()
    motor = None
    modo = None

    def avisar(texto, color):
        try:
            conn.send(("estado", texto, color))
        except Exception:
            pass

    try:
        padre = multiprocessing.parent_process()
    except Exception:
        padre = None

    while True:
        try:
            if not conn.poll(1.0):
                if padre is not None and not padre.is_alive():
                    break          # la app se cerró: este proceso también
                continue
            msg = conn.recv()
        except (EOFError, OSError):
            break
        orden = msg[0]
        try:
            if orden == "cargar":
                nuevo = msg[1]
                print(f"[OCR proceso] Cargando {nuevo}...")
                _dmt_registrar_dlls("antes de cargar el motor")
                if nuevo == "rapid_cpu":
                    from rapidocr import RapidOCR
                    motor = RapidOCR(params={"Global.log_level": "error"})
                else:
                    # Primero las DLL CUDA 12.9 / cuDNN 9 que usa PaddlePaddle (sin PyTorch)
                    if not _cuda_preparar_dlls():
                        try:
                            import torch  # noqa: F401  (respaldo: builds con torch)
                        except Exception as e:
                            print(f"[OCR proceso] DLL de CUDA no encontradas: {e}")
                    motor = _ocr_crear_paddle(gpu=(nuevo == "paddle_gpu"), avisar=avisar)
                modo = nuevo
                print(f"[OCR proceso] {nuevo} listo.")
                _dmt_registrar_dlls("motor cargado")
                conn.send(("ok", modo))
            elif orden == "predecir":
                if motor is None:
                    raise RuntimeError("No hay motor OCR cargado")
                img = msg[1]
                if modo == "rapid_cpu":
                    salida = motor(img)
                    lineas = [str(t) for t in (salida.txts or [])]
                else:
                    lineas = []
                    for r in motor.predict(img):
                        lineas.extend(str(t) for t in (r.get("rec_texts") or []))
                conn.send(("ok", lineas))
            elif orden == "vaciar_cache":
                _ocr_vaciar_cache_paddle()
                conn.send(("ok", None))
            elif orden == "salir":
                conn.send(("ok", None))
                break
        except BaseException as e:  # noqa: BLE001
            import traceback as _tb
            try:
                conn.send(("error", f"{type(e).__name__}: {e}", _tb.format_exc()))
            except Exception:
                break


class GestorMotorOCR:
    """
    Dueño único del motor OCR. El motor corre en un PROCESO aparte:
      · la interfaz ya no se congela ("No responde"): PaddlePaddle retiene el
        GIL de Python al importarse, al crear el predictor y al inferir;
      · descargar = cerrar el proceso -> se libera el 100 % de RAM y VRAM;
      · si Paddle GPU revienta, la app sigue viva y se pasa a RapidOCR.
    Un proceso por motor: cambiar de motor cierra el anterior.
    """
    TIEMPO_CARGA_MAX = 3600      # incluye la descarga de modelos la primera vez

    def __init__(self, on_estado=None, gestor_ia=None):
        self.on_estado = on_estado      # callback(texto, color, evento, modo) desde cualquier hilo
        self.gestor_ia = gestor_ia
        self.modo = None                # motor cargado ahora
        self.cargando = None            # motor que se está cargando
        self.gpu_fallida = False        # Paddle GPU falló en esta sesión
        self._proc = None
        self._conn = None
        self._lock = threading.RLock()

    def _avisar(self, texto, color, evento=None, modo=None):
        """evento: "cargando" | "listo" | "error" | "descargado" | "aviso" (del proceso)."""
        if self.on_estado:
            try:
                self.on_estado(texto, color, evento, modo)
            except Exception:
                pass

    def _vivo(self):
        try:
            return self._proc is not None and self._proc.is_alive()
        except Exception:
            return False

    def _error_proceso_caido(self):
        codigo = None
        try:
            if self._proc is not None:
                self._proc.join(3)
                codigo = self._proc.exitcode
        except Exception:
            pass
        if isinstance(codigo, int) and codigo < 0 and os.name != "nt":
            texto = f"señal {-codigo}"
        elif isinstance(codigo, int) and (codigo < 0 or codigo > 255):
            texto = f"0x{codigo & 0xFFFFFFFF:08X}"
        else:
            texto = str(codigo)
        return RuntimeError(
            f"El motor OCR se cerró inesperadamente (código {texto}). "
            f"Detalle en %LOCALAPPDATA%\\DeusMachinaTools\\logs\\motor_ocr.log")

    def _esperar(self, timeout, on_espera=None):
        """Espera la respuesta del proceso reenviando sus mensajes de estado."""
        inicio = time.time()
        while True:
            try:
                hay = self._conn.poll(0.2)
            except (EOFError, OSError) as e:
                raise self._error_proceso_caido() from e
            if hay:
                try:
                    msg = self._conn.recv()
                except (EOFError, OSError) as e:
                    raise self._error_proceso_caido() from e
                if msg[0] == "estado":
                    self._avisar(msg[1], msg[2], "aviso", self.cargando or self.modo)
                    continue
                if msg[0] == "ok":
                    return msg[1]
                if msg[0] == "error":
                    if len(msg) > 2:
                        print(msg[2])
                    raise RuntimeError(msg[1])
                continue
            if not self._vivo():
                raise self._error_proceso_caido()
            transcurrido = time.time() - inicio
            if on_espera:
                try:
                    on_espera(transcurrido)
                except Exception:
                    pass
            if transcurrido > timeout:
                raise TimeoutError("El motor OCR no respondió a tiempo.")

    def _iniciar_proceso(self):
        ctx = multiprocessing.get_context("spawn")
        conn_padre, conn_hijo = ctx.Pipe(duplex=True)
        proc = ctx.Process(target=_ocr_proceso_principal, args=(conn_hijo,),
                           name="dmt_ocr_motor", daemon=True)
        proc.start()
        conn_hijo.close()
        self._proc, self._conn = proc, conn_padre

    def _cerrar_proceso(self, forzar=False):
        proc, conn = self._proc, self._conn
        habia_motor = self.modo is not None or proc is not None
        self._proc = self._conn = None
        self.modo = None
        if proc is not None:
            try:
                if not forzar and proc.is_alive() and conn is not None:
                    conn.send(("salir",))
                    proc.join(5)
            except Exception:
                pass
            try:
                if proc.is_alive():
                    proc.terminate()
                    proc.join(3)
                if proc.is_alive():
                    proc.kill()
                    proc.join(2)
            except Exception:
                pass
        if conn is not None:
            try:
                conn.close()
            except Exception:
                pass
        if habia_motor:
            if self.gestor_ia is not None:
                self.gestor_ia.marcar_descargado("ocr")
            self._avisar("Motor: sin cargar (se carga al extraer)", "gray", "descargado")

    # ---------------- API pública (cualquier hilo) ----------------
    def esta_listo(self, modo):
        """True si 'modo' ya está cargado en su proceso (no hará falta cargarlo)."""
        return self._vivo() and self.modo == modo

    def asegurar(self, modo, timeout=None, on_espera=None):
        """Deja listo el motor 'modo' (lo carga en su proceso si hace falta)."""
        with self._lock:
            if self._vivo() and self.modo == modo:
                return True
            self._cerrar_proceso()                   # otro motor (o proceso muerto)
            if self.gestor_ia is not None:
                self.gestor_ia.antes_de_cargar("ocr")
            self.cargando = modo
            self._avisar(f"Motor: cargando {OCR_NOMBRES[modo]}…", "orange", "cargando", modo)
            try:
                self._iniciar_proceso()
                self._conn.send(("cargar", modo))
                self._esperar(timeout or self.TIEMPO_CARGA_MAX, on_espera)
                self.modo = modo
                if self.gestor_ia is not None:
                    self.gestor_ia.marcar_cargado("ocr")
                self._avisar(f"Motor: {OCR_NOMBRES[modo]} ✅ (en memoria)", "#2cc985", "listo", modo)
                return True
            except BaseException:
                self._cerrar_proceso(forzar=True)
                self._avisar(f"Motor: error al cargar {OCR_NOMBRES[modo]}", "#c92c2c", "error", modo)
                raise
            finally:
                self.cargando = None

    def predecir(self, img_bgr, timeout=1800, on_espera=None):
        with self._lock:
            if not self._vivo():
                raise RuntimeError("No hay motor OCR cargado")
            self._conn.send(("predecir", img_bgr))
            return self._esperar(timeout, on_espera)

    def vaciar_cache(self):
        with self._lock:
            if self._vivo() and (self.modo or "") == "paddle_gpu":
                try:
                    self._conn.send(("vaciar_cache",))
                    self._esperar(60)
                except Exception as e:
                    print(f"[OCR] No se pudo vaciar la caché de Paddle: {e}")

    def descargar(self, timeout=None):
        """Cierra el proceso del motor (libera toda su RAM/VRAM)."""
        with self._lock:
            self._cerrar_proceso()

    def cerrar(self):
        """Al salir de la app: termina el proceso sin esperar a nadie."""
        proc = self._proc
        if proc is not None:
            try:
                if proc.is_alive():
                    proc.kill()
            except Exception:
                pass


class TarjetaOpcion(ctk.CTkFrame):
    """
    Tarjeta seleccionable de tamaño FIJO: título, descripción y línea de estado.
    Seleccionar, habilitar o cambiar el estado solo RECOLOREA (y solo lo que
    cambió): nunca cambia tamaños, así que el layout no se recalcula ni parpadea.
    Un texto que no cabe se recorta con "…" (medido en píxeles): nunca la ensancha.
    """
    C_BASE, C_HOVER, C_SEL, C_OFF = "#232323", "#303030", "#3a230d", "#1e1e1e"
    B_BASE, B_OFF = "#3a3a3a", "#2a2a2a"
    PAD_X = 10

    def __init__(self, master, clave, titulo, descripcion, command=None,
                 color_sel="#e67e22", ancho=186, alto=62, fuente="Arial", fondo_sel=None):
        super().__init__(master, width=ancho, height=alto, corner_radius=8,
                         fg_color=self.C_BASE, border_width=2, border_color=self.B_BASE)
        self.pack_propagate(False)
        self.clave = clave
        self._command = command
        self._color_sel = color_sel
        self._fondo_sel = fondo_sel or self.C_SEL
        self._sel = False
        self._habilitada = True
        self._atenuada = False
        self._hover = False
        self._hover_pend = False
        self._visual = None
        self._estado = None

        # CustomTkinter escala en pantalla TANTO la tarjeta como las fuentes (en
        # una pantalla al 125 % una tarjeta de 186 ocupa 232 px y una fuente de
        # 11 se dibuja a 14 px). Para recortar bien hay que medir con esas
        # medidas reales; con las nominales se recortaban textos que sí cabían.
        try:
            escala = ctk.ScalingTracker.get_widget_scaling(self)
        except Exception:
            escala = 1.0
        borde = 2
        # Ancho útil del texto en píxeles reales (sin márgenes ni borde)
        self._ancho_txt = int(round(ancho * escala)) - 2 * self.PAD_X - int(round(2 * borde * escala)) - 4

        def _fuente(tam, negrita=False):
            return tkfont.Font(self, family=fuente, size=-max(8, int(round(tam * escala))),
                               weight="bold" if negrita else "normal")

        self._f_titulo = _fuente(13, True)
        self._f_desc = _fuente(11)
        self._f_estado = _fuente(11, True)

        self._lbl_titulo = ctk.CTkLabel(self, text=self._recortar(titulo, self._f_titulo),
                                        font=(fuente, 13, "bold"), anchor="w", height=18,
                                        text_color="#f2f2f2")
        self._lbl_titulo.pack(fill="x", padx=self.PAD_X, pady=(7, 0))
        self._lbl_desc = ctk.CTkLabel(self, text=self._recortar(descripcion, self._f_desc),
                                      font=(fuente, 11), anchor="w", height=15,
                                      text_color="#a8a8a8")
        self._lbl_desc.pack(fill="x", padx=self.PAD_X)
        self._lbl_estado = ctk.CTkLabel(self, text="", font=(fuente, 11, "bold"),
                                        anchor="center", height=15, text_color="#8a8a8a")
        self._lbl_estado.pack(fill="x", padx=self.PAD_X, pady=(1, 0))

        for w in (self, self._lbl_titulo, self._lbl_desc, self._lbl_estado):
            w.bind("<Button-1>", self._click, add="+")
            w.bind("<Enter>", self._programar_hover, add="+")
            w.bind("<Leave>", self._programar_hover, add="+")
        self._aplicar()

    def _recortar(self, texto, fuente):
        texto = str(texto or "")
        try:
            if fuente.measure(texto) <= self._ancho_txt:
                return texto
            while texto and fuente.measure(texto + "…") > self._ancho_txt:
                texto = texto[:-1]
            return texto.rstrip() + "…"
        except Exception:
            return texto

    # --- eventos ---
    def _click(self, _evento=None):
        if self._habilitada and not self._atenuada and self._command:
            self._command(self.clave)

    def _programar_hover(self, _evento=None):
        # Entrar a una etiqueta hija dispara Leave del marco: se revisa la
        # posición real del puntero una sola vez, ya en reposo.
        if not self._hover_pend:
            self._hover_pend = True
            self.after_idle(self._revisar_hover)

    def _revisar_hover(self):
        self._hover_pend = False
        try:
            x, y = self.winfo_pointerxy()
            x0, y0 = self.winfo_rootx(), self.winfo_rooty()
            dentro = x0 <= x < x0 + self.winfo_width() and y0 <= y < y0 + self.winfo_height()
        except Exception:
            dentro = False
        if dentro != self._hover:
            self._hover = dentro
            self._aplicar()

    # --- API ---
    def set_config(self, seleccionada=None, habilitada=None, atenuada=None):
        if seleccionada is not None:
            self._sel = bool(seleccionada)
        if habilitada is not None:
            self._habilitada = bool(habilitada)
        if atenuada is not None:
            self._atenuada = bool(atenuada)
        self._aplicar()

    def set_estado(self, texto, color):
        estado = (texto or "", color or "#8a8a8a")
        if estado == self._estado:
            return
        self._estado = estado
        self._lbl_estado.configure(text=self._recortar(estado[0], self._f_estado),
                                   text_color=estado[1])

    def _aplicar(self):
        if not self._habilitada:
            fg, borde, tit, desc = self.C_OFF, self.B_OFF, "#6b6b6b", "#565656"
        elif self._sel:
            fg, borde, tit, desc = self._fondo_sel, self._color_sel, "#ffffff", "#e3cfae"
        else:
            fg = self.C_HOVER if (self._hover and not self._atenuada) else self.C_BASE
            borde = self.B_BASE
            tit, desc = ("#8a8a8a", "#6e6e6e") if self._atenuada else ("#f2f2f2", "#a8a8a8")
        cursor = "hand2" if (self._habilitada and not self._atenuada and not self._sel) else "arrow"
        visual = (fg, borde, tit, desc, cursor)
        previo = self._visual
        if visual == previo:
            return
        self._visual = visual
        if previo is None or previo[0] != fg or previo[1] != borde:
            self.configure(fg_color=fg, border_color=borde)
        if previo is None or previo[2] != tit:
            self._lbl_titulo.configure(text_color=tit)
        if previo is None or previo[3] != desc:
            self._lbl_desc.configure(text_color=desc)
        if previo is None or previo[4] != cursor:
            for w in (self, self._lbl_titulo, self._lbl_desc, self._lbl_estado):
                try:
                    w.configure(cursor=cursor)
                except Exception:
                    pass
                for interno in ("_canvas", "_label"):
                    try:
                        getattr(w, interno).configure(cursor=cursor)
                    except Exception:
                        pass


# Configuración inicial de estilo
_dmt_preparar_stdio_hijo()

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

# --- LISTAS DE ADMISIÓN (EL CANDADO) ---
VALID_VIDEO_EXT = {'.mp4', '.mov', '.avi', '.mkv', '.wmv', '.flv', '.webm', '.m4v', '.mpeg', '.mpg', '.3gp', '.ts'}
# Formatos de imagen admitidos (arrastrar y selectores usan ESTA lista).
# Se retiraron .raw / .nef / .cr2: ni FFmpeg ni Pillow los revelan (en NEF solo
# sale la miniatura de 160x120; CR2 y .raw fallan por completo).
VALID_IMAGE_EXT = {'.jpg', '.jpeg', '.png', '.webp', '.bmp', '.tiff', '.tif', '.gif', '.ico', '.psd', '.svg', '.heic', '.heif'}
VALID_PDF_EXT = {'.pdf'} # <--- NUEVO CANDADO
VALID_AUDIO_EXT = {'.mp3', '.wav', '.aac', '.m4a', '.flac', '.ogg', '.wma', '.aiff', '.opus', '.ac3', '.ape', '.alac', '.pcm'}



# Whisper trabaja por dentro SIEMPRE con audio float32, 16 kHz, mono.
WHISPER_SR = 16000

# Idioma del audio para Whisper (None = detectarlo solo, que es lo predeterminado)
TRANS_IDIOMA_AUTO = "🌐 Automático (detectar)"
# Para material que MEZCLA idiomas (una canción en japonés + inglés + coreano, una
# entrevista bilingüe...): Whisper detecta el idioma en cada segmento en vez de
# fijar uno solo para todo el archivo.
TRANS_IDIOMA_MULTI = "🌍 Multilingüe (mezcla)"
TRANS_IDIOMAS = {
    TRANS_IDIOMA_AUTO: None,
    TRANS_IDIOMA_MULTI: "multi",
    "Español": "es", "Inglés": "en", "Portugués": "pt", "Francés": "fr", "Italiano": "it",
    "Alemán": "de", "Catalán": "ca", "Neerlandés": "nl", "Polaco": "pl", "Ruso": "ru",
    "Ucraniano": "uk", "Turco": "tr", "Árabe": "ar", "Hindi": "hi", "Japonés": "ja",
    "Coreano": "ko", "Chino": "zh",
}


def _trans_opts_idioma(idioma):
    """
    Opción elegida -> parámetros de faster-whisper:
      · None     → detecta el idioma una vez y lo usa para todo (Automático)
      · "multi"  → detecta el idioma en CADA segmento (material que mezcla idiomas)
      · "es"/... → fija ese idioma
    """
    if idioma == "multi":
        return {"language": None, "multilingual": True}
    return {"language": idioma}


# ==============================================================================
#  VIDEO: CAPACIDADES DE FFMPEG / GPU (se detectan UNA vez, con pruebas reales)
# ------------------------------------------------------------------------------
#  No se adivina por el nombre de la tarjeta: se codifica/decodifica un clip de
#  prueba de medio segundo con cada cosa que se va a usar. Lo que pasa, se usa;
#  lo que falla, se evita. Funciona igual con cualquier GPU, driver o build.
# ==============================================================================
_FF_CAPS = None
_FF_CAPS_LOCK = threading.Lock()

# Opciones de calidad NVENC, de la más completa a la mínima: se queda la
# primera combinación que el equipo acepte en la prueba real.
NVENC_FLAGS_CANDIDATOS = (
    ("-spatial-aq", "1", "-temporal-aq", "1", "-rc-lookahead", "20",
     "-bf", "3", "-b_ref_mode", "middle", "-multipass", "qres"),
    ("-spatial-aq", "1", "-rc-lookahead", "20",
     "-bf", "3", "-b_ref_mode", "middle", "-multipass", "qres"),
    ("-spatial-aq", "1", "-rc-lookahead", "20", "-multipass", "qres"),
    ("-spatial-aq", "1", "-rc-lookahead", "20"),
    (),
)
# Opciones genéricas de FFmpeg (no salen en -h encoder=, siempre existen)
_FF_OPC_GENERICAS = {"bf"}

# Códecs que NVDEC puede decodificar (según generación; si no puede, la ruta
# falla al primer cuadro y se reintenta sola por la siguiente)
NVDEC_CODECS = {"h264", "hevc", "vp9", "av1", "mpeg2video", "mpeg1video", "vc1", "vp8"}

# Selector de resolución (lado corto; nunca amplía)
VID_RES_OPCIONES = ["Original", "1440p (2K)", "1080p (Full HD)", "720p (HD)", "480p (SD)"]

# Convertir = lo más fiel posible ("visualmente idéntico") por encoder
VID_CALIDAD_FIEL = {
    "h264_nvenc": 19, "hevc_nvenc": 21, "av1_nvenc": 26,
    "libx264": 18, "libx265": 20, "libsvtav1": 25, "libaom-av1": 25,
}
# Reducir Tamaño: niveles 1 (extrema) .. 5 (casi sin pérdida) por encoder.
# AV1 (NVENC y CPU) usa escala 0-63: sus valores se calibran aparte (≈ ×1.25).
VID_NIVELES = {
    "hevc_nvenc": (38, 33, 28, 24, 20),
    "av1_nvenc":  (48, 41, 35, 30, 25),
    "libx265":    (35, 30, 26, 22, 18),
    "libsvtav1":  (44, 38, 33, 28, 23),
    "libaom-av1": (44, 38, 33, 28, 23),
}


def _ff_run(cmd, timeout=25):
    """Ejecuta ffmpeg/ffprobe sin ventana. Devuelve (código, stdout, stderr)."""
    si = None
    if os.name == 'nt':
        si = subprocess.STARTUPINFO()
        si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    try:
        r = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                           timeout=timeout, startupinfo=si,
                           creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
        return (r.returncode,
                r.stdout.decode("utf-8", "ignore"),
                r.stderr.decode("utf-8", "ignore"))
    except Exception as e:
        return -1, "", str(e)


def _ff_nombres_lista(texto):
    """Nombres de la 2a columna de 'ffmpeg -encoders' / '-filters'."""
    nombres = set()
    for linea in texto.splitlines():
        partes = linea.split()
        if len(partes) >= 2 and not linea.startswith(("---", "Encoders", "Filters")):
            nombres.add(partes[1])
    return nombres


def _ff_opciones_encoder(encoder):
    """Opciones privadas que acepta un encoder según 'ffmpeg -h encoder=X'."""
    _, out, err = _ff_run(["ffmpeg", "-hide_banner", "-h", f"encoder={encoder}"])
    return set(re.findall(r"^\s+-([\w-]+)\s+<", out + err, flags=re.M))


def _ff_filtrar_flags(flags, opciones):
    """Quita de una combinación las opciones que la build no conoce."""
    salida = []
    for i in range(0, len(flags), 2):
        nombre = flags[i].lstrip("-")
        if nombre in _FF_OPC_GENERICAS or nombre in opciones:
            salida.extend(flags[i:i + 2])
    return tuple(salida)


def _ff_prueba_nvenc(encoder, flags, pix_fmt):
    cmd = ["ffmpeg", "-hide_banner", "-nostdin", "-loglevel", "error",
           "-f", "lavfi", "-i", "testsrc2=size=640x360:rate=30", "-frames:v", "45",
           "-pix_fmt", pix_fmt, "-c:v", encoder, "-preset", "p5",
           "-rc", "vbr", "-cq", "28", "-b:v", "0", *flags, "-f", "null", "-"]
    codigo, _, err = _ff_run(cmd)
    return codigo == 0, err.strip()[-200:]


def _ff_firma_entorno():
    """
    Identifica la build de FFmpeg y la GPU/driver. Si algo de esto cambia, las
    capacidades guardadas dejan de valer y se vuelven a medir.
    """
    partes = []
    exe = shutil.which("ffmpeg") or "ffmpeg"
    try:
        st = os.stat(exe)
        partes.append(f"{os.path.basename(exe)}|{st.st_size}|{int(st.st_mtime)}")
    except OSError:
        partes.append(exe)
    codigo, out, _ = _ff_run(["ffmpeg", "-hide_banner", "-version"], timeout=15)
    partes.append((out.splitlines() or [""])[0][:100] if codigo == 0 else "sin-ffmpeg")
    try:
        r = subprocess.run(["nvidia-smi", "--query-gpu=name,driver_version", "--format=csv,noheader"],
                           stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, timeout=15,
                           creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
        gpu = r.stdout.decode("utf-8", "ignore").strip().splitlines()
        partes.append(gpu[0].strip() if r.returncode == 0 and gpu else "sin-nvidia")
    except Exception:
        partes.append("sin-nvidia")
    return " || ".join(partes)


def _ff_caps_archivo():
    return os.path.join(_dmt_base_dir(), "ffmpeg_caps.json")


def _ff_caps_leer_cache(firma):
    """Capacidades medidas en un arranque anterior (si el equipo no cambió)."""
    try:
        with open(_ff_caps_archivo(), "r", encoding="utf-8") as fh:
            datos = json.load(fh)
        if datos.get("firma") != firma or datos.get("version") != 1:
            return None
        caps = datos["caps"]
        caps["encoders"] = set(caps.get("encoders") or [])
        caps["filters"] = set(caps.get("filters") or [])
        caps["nvenc"] = {k: (tuple(v) if v is not None else None)
                         for k, v in (caps.get("nvenc") or {}).items()}
        caps["nvenc10"] = dict(caps.get("nvenc10") or {})
        caps["detalle"] = dict(caps.get("detalle") or {})
        caps["de_cache"] = True
        return caps
    except Exception:
        return None


def _ff_caps_guardar_cache(firma, caps):
    try:
        plano = dict(caps)
        plano["encoders"] = sorted(caps.get("encoders") or ())
        plano["filters"] = sorted(caps.get("filters") or ())
        plano["nvenc"] = {k: (list(v) if v is not None else None)
                          for k, v in (caps.get("nvenc") or {}).items()}
        plano.pop("de_cache", None)
        ruta = _ff_caps_archivo()
        tmp = ruta + ".tmp"
        with open(tmp, "w", encoding="utf-8") as fh:
            json.dump({"version": 1, "firma": firma, "caps": plano}, fh, ensure_ascii=False)
        os.replace(tmp, ruta)
    except Exception as e:
        print(f"[FFmpeg] No se pudo guardar la detección de GPU: {e}")


def ffmpeg_capacidades(forzar=False):
    """
    Capacidades reales de la build de FFmpeg + GPU (con caché, segura entre hilos).
    La medición real (unos segundos de pruebas NVENC/NVDEC) se hace UNA sola vez
    por equipo: el resultado queda guardado en %LOCALAPPDATA%\\DeusMachinaTools\\
    ffmpeg_caps.json y solo se repite si cambia FFmpeg, la GPU o el driver.
    """
    global _FF_CAPS
    with _FF_CAPS_LOCK:
        if _FF_CAPS is not None and not forzar:
            return _FF_CAPS

        firma = _ff_firma_entorno()
        if not forzar:
            guardadas = _ff_caps_leer_cache(firma)
            if guardadas is not None:
                _FF_CAPS = guardadas
                print("[FFmpeg] Capacidades de GPU leídas de la detección anterior "
                      "(no se repiten las pruebas).")
                return _FF_CAPS

        t_inicio = time.time()
        caps = {"ok": False, "encoders": set(), "filters": set(), "cuda": False,
                "nvenc": {}, "nvenc10": {}, "nvdec": False, "gpu_total": False,
                "detalle": {}, "segundos": 0.0}
        codigo, out, _ = _ff_run(["ffmpeg", "-hide_banner", "-encoders"])
        if codigo != 0:
            _FF_CAPS = caps
            return caps            # sin FFmpeg no se guarda nada: se reintenta luego
        caps["ok"] = True
        caps["encoders"] = _ff_nombres_lista(out)
        _, out, _ = _ff_run(["ffmpeg", "-hide_banner", "-filters"])
        caps["filters"] = _ff_nombres_lista(out)
        _, out, _ = _ff_run(["ffmpeg", "-hide_banner", "-hwaccels"])
        caps["cuda"] = "cuda" in out.split()

        # --- NVENC: primero una prueba mínima (si falla, no hay NVENC usable) ---
        if "h264_nvenc" in caps["encoders"]:
            base_ok, err = _ff_prueba_nvenc("h264_nvenc", (), "nv12")
            caps["detalle"]["h264_nvenc_base"] = "ok" if base_ok else err
            if base_ok:
                for enc in ("h264_nvenc", "hevc_nvenc", "av1_nvenc"):
                    if enc not in caps["encoders"]:
                        continue
                    opciones = _ff_opciones_encoder(enc)
                    elegido = None
                    for candidato in NVENC_FLAGS_CANDIDATOS:
                        flags = _ff_filtrar_flags(candidato, opciones)
                        ok, err = _ff_prueba_nvenc(enc, flags, "nv12")
                        if ok:
                            elegido = flags
                            break
                        caps["detalle"][f"{enc}{flags}"] = err
                    caps["nvenc"][enc] = elegido
                    # H.264 se entrega SIEMPRE en 8 bits: solo HEVC/AV1 prueban 10 bits
                    if elegido is not None and enc != "h264_nvenc":
                        ok10, _ = _ff_prueba_nvenc(enc, elegido, "p010le")
                        caps["nvenc10"][enc] = ok10

        # --- NVDEC (GPU decodifica) y ruta completa en GPU ---
        if caps["cuda"] and caps["nvenc"].get("h264_nvenc") is not None:
            prueba = os.path.join(tempfile.gettempdir(), f"dmt_nvdec_{os.getpid()}.mp4")
            try:
                codigo, _, _ = _ff_run(["ffmpeg", "-y", "-hide_banner", "-nostdin", "-loglevel", "error",
                                        "-f", "lavfi", "-i", "testsrc2=size=640x360:rate=30",
                                        "-frames:v", "30", "-c:v", "h264_nvenc", "-preset", "p1", prueba])
                if codigo == 0 and os.path.isfile(prueba):
                    codigo, _, err = _ff_run(["ffmpeg", "-hide_banner", "-nostdin", "-loglevel", "error",
                                              "-hwaccel", "cuda", "-i", prueba,
                                              "-vf", "scale=320:180", "-c:v", "h264_nvenc", "-preset", "p1",
                                              "-f", "null", "-"])
                    caps["nvdec"] = codigo == 0
                    caps["detalle"]["nvdec"] = "ok" if codigo == 0 else err.strip()[-200:]
                    if "scale_cuda" in caps["filters"]:
                        codigo, _, err = _ff_run(["ffmpeg", "-hide_banner", "-nostdin", "-loglevel", "error",
                                                  "-hwaccel", "cuda", "-hwaccel_output_format", "cuda",
                                                  "-i", prueba,
                                                  "-vf", "scale_cuda=w=320:h=180:interp_algo=lanczos"
                                                         ":format=nv12:passthrough=0",
                                                  "-c:v", "h264_nvenc", "-preset", "p1",
                                                  "-f", "null", "-"])
                        caps["gpu_total"] = codigo == 0
                        caps["detalle"]["gpu_total"] = "ok" if codigo == 0 else err.strip()[-200:]
            finally:
                try:
                    os.remove(prueba)
                except OSError:
                    pass

        caps["segundos"] = time.time() - t_inicio
        _si = lambda v: "✓" if v else "✗"
        _cods = [n for n, e in (("H.264", "h264_nvenc"), ("H.265", "hevc_nvenc"), ("AV1", "av1_nvenc"))
                 if caps["nvenc"].get(e) is not None]
        _diez = [n for n, e in (("H.265", "hevc_nvenc"), ("AV1", "av1_nvenc")) if caps["nvenc10"].get(e)]
        print(f"[FFmpeg] NVENC {'/'.join(_cods) or '✗'} (10 bits: {'/'.join(_diez) or '✗'}) · "
              f"NVDEC {_si(caps['nvdec'])} · GPU completa {_si(caps['gpu_total'])} · "
              f"SVT-AV1 {_si('libsvtav1' in caps['encoders'])} · {caps['segundos']:.1f} s")
        _ff_caps_guardar_cache(firma, caps)      # la próxima vez ya no se mide
        _FF_CAPS = caps
        return caps


# ------------------------------------------------------------------------------
#  Análisis de un archivo (un solo ffprobe en JSON)
# ------------------------------------------------------------------------------
def _pix_bits(pix_fmt):
    pf = (pix_fmt or "").lower()
    m = re.match(r"^p[02](\d\d)", pf)              # p010 / p016 / p210 ...
    if m:
        return int(m.group(1))
    m = re.search(r"p(\d{1,2})(le|be)$", pf)       # yuv420p10le
    if m:
        return int(m.group(1))
    m = re.search(r"(\d{2})(le|be)$", pf)          # gray10le, x2rgb10le
    if m:
        return int(m.group(1))
    return 8


def _pix_croma(pix_fmt):
    pf = (pix_fmt or "").lower()
    if "420" in pf or pf.startswith(("nv12", "nv21", "p010", "p012", "p016")):
        return "420"
    if "422" in pf or pf.startswith(("nv16", "p210", "p212", "p216", "yuyv", "uyvy")):
        return "422"
    if "444" in pf or pf.startswith(("gbr", "rgb", "bgr")):
        return "444"
    return "otro"


def vid_info(ruta):
    """Datos del video/audio de un archivo. {'ok': False} si ffprobe falla."""
    codigo, out, _ = _ff_run(["ffprobe", "-v", "error", "-print_format", "json",
                              "-show_format", "-show_streams", ruta], timeout=40)
    info = {"ok": False, "vcodec": None, "acodec": None}
    if codigo != 0:
        return info
    try:
        data = json.loads(out or "{}")
    except Exception:
        return info
    streams = data.get("streams") or []
    v = next((s for s in streams if s.get("codec_type") == "video"
              and not (s.get("disposition") or {}).get("attached_pic")), None)
    a = next((s for s in streams if s.get("codec_type") == "audio"), None)
    fmt = data.get("format") or {}

    def _num(x, tipo=float):
        try:
            return tipo(x)
        except (TypeError, ValueError):
            return None

    info["ok"] = True
    info["dur"] = _num(fmt.get("duration"))
    if v:
        info["vcodec"] = v.get("codec_name")
        info["pix_fmt"] = v.get("pix_fmt") or ""
        info["w"] = _num(v.get("width"), int) or 0
        info["h"] = _num(v.get("height"), int) or 0
        bits = _num(v.get("bits_per_raw_sample"), int)
        info["bits"] = bits if bits and bits >= 8 else _pix_bits(info["pix_fmt"])
        info["croma"] = _pix_croma(info["pix_fmt"])
        info["vbr"] = _num(v.get("bit_rate"), int)
        # Rotación (celulares): matriz de visualización o etiqueta 'rotate'
        rot = 0.0
        volteo = False
        for sd in v.get("side_data_list") or []:
            if "rotation" in sd:
                rot = _num(sd.get("rotation")) or 0.0
            matriz = sd.get("displaymatrix")
            if isinstance(matriz, str):
                filas = re.findall(r":\s*(-?\d+)\s+(-?\d+)\s+(-?\d+)", matriz)
                if len(filas) >= 2:
                    a0, b0 = int(filas[0][0]), int(filas[0][1])
                    c0, d0 = int(filas[1][0]), int(filas[1][1])
                    volteo = (a0 * d0 - b0 * c0) < 0
        if not rot:
            rot = _num((v.get("tags") or {}).get("rotate")) or 0.0
        giro = int(round((-rot) % 360)) % 360          # igual que el autorotate de FFmpeg
        info["giro"] = giro
        info["rotado"] = bool(giro) or volteo
        info["giro90"] = giro in (90, 270)
    if a:
        info["acodec"] = a.get("codec_name")
        info["abr"] = _num(a.get("bit_rate"), int)
    return info


def vid_altura_objetivo(opcion):
    """'1080p (Full HD)' -> 1080 ; 'Original' -> None"""
    m = re.match(r"\s*(\d{3,4})p", str(opcion or ""))
    return int(m.group(1)) if m else None


def vid_dims_objetivo(info, corto_obj):
    """
    (ancho, alto) finales en orientación de pantalla, reduciendo el LADO CORTO
    a 'corto_obj' (un vertical 1080x1920 a 720p queda 720x1280). Nunca amplía:
    devuelve None si no hace falta reescalar.
    """
    w, h = info.get("w") or 0, info.get("h") or 0
    if not corto_obj or w <= 0 or h <= 0:
        return None
    dw, dh = (h, w) if info.get("giro90") else (w, h)
    corto = min(dw, dh)
    if corto <= corto_obj:
        return None
    f = corto_obj / corto
    if dw <= dh:
        nw, nh = corto_obj, int(round(dh * f / 2)) * 2
    else:
        nw, nh = int(round(dw * f / 2)) * 2, corto_obj
    return max(2, nw - nw % 2), max(2, nh - nh % 2)




class SplashScreen(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.ready_to_exit = False
        self.running = True  # <--- NUEVO: Bandera de seguridad
        
        # --- CONFIGURACIÓN DE VENTANA ---
        self.overrideredirect(True) 
        
        # COLORES
        bg_color = "#1a1a2e"
        depth_color = "#080810"
        text_color = "#e0e0e0"
        bar_color = "#2cc985"

        # --- MARCO ---
        self.border_frame = tk.Frame(self, bg=depth_color, bd=0)
        self.border_frame.pack(fill="both", expand=True)
        self.inner_frame = tk.Frame(self.border_frame, bg=bg_color)
        self.inner_frame.pack(fill="both", expand=True, padx=3, pady=3)

        # --- CENTRADO ---
        w, h = 780, 450
        ws, hs = self.winfo_screenwidth(), self.winfo_screenheight()
        x, y = (ws // 2) - (w // 2), (hs // 2) - (h // 2)
        self.geometry(f"{w}x{h}+{x}+{y}")
        self.attributes("-topmost", True)

        # --- ESTILOS ---
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Cyber.Horizontal.TProgressbar", 
                        troughcolor="#111", background=bar_color, 
                        bordercolor="#111", lightcolor=bar_color, darkcolor=bar_color)
        
        # --- UI ---
        # CAMBIA pady=(40, 5) POR pady=(25, 5) PARA DAR ESPACIO A LOS CREDITOS ARRIBA
        tk.Label(self.inner_frame, text="DEUS MACHINA | TOOLS", 
                 font=("JetBrains Mono", 26, "bold"), bg=bg_color, fg="white").pack(pady=(25, 5))
        tk.Label(self.inner_frame, text="SYSTEM INITIALIZATION", 
                 font=("Consolas", 11, "bold"), bg=bg_color, fg="#4c88b7").pack(pady=(0, 20))
        
        img_frame = tk.Frame(self.inner_frame, bg=bg_color)
        img_frame.pack(expand=True)
        
        # --- RUTA DE RECURSOS (IMGTYPE) ---
        # --- RUTA DE RECURSOS (IMGTYPE) ---
        # Usamos resource_path para que funcione en .py y en .exe
        assets_folder = resource_path("imgtype")
        
        # Logo
        try:
            logo_path = os.path.join(assets_folder, "logo.png")
            if os.path.exists(logo_path):
                pil_logo = Image.open(logo_path).convert("RGBA").resize((175, 175), Image.Resampling.LANCZOS)
                self.tk_logo = ImageTk.PhotoImage(pil_logo)
                tk.Label(img_frame, image=self.tk_logo, bg=bg_color).pack(side="left", padx=30)
        except: pass

        tk.Frame(img_frame, width=1, height=100, bg="#444").pack(side="left", padx=10)

        # Splash Art
        try:
            splash_img_path = os.path.join(assets_folder, "splash_img.jpg")
            if os.path.exists(splash_img_path):
                pil_splash = Image.open(splash_img_path).convert("RGBA").resize((256, 169), Image.Resampling.LANCZOS)
                self.tk_splash = ImageTk.PhotoImage(pil_splash)
                tk.Label(img_frame, image=self.tk_splash, bg=bg_color).pack(side="left", padx=30)
        except: pass

        tk.Frame(img_frame, width=1, height=100, bg="#444").pack(side="left", padx=10)


        bottom_frame = tk.Frame(self.inner_frame, bg=bg_color)
        bottom_frame.pack(side="bottom", fill="x", pady=20, padx=40)

        self.lbl_status = tk.Label(bottom_frame, text="Iniciando...", font=("Consolas", 11), bg=bg_color, fg=text_color)
        self.lbl_status.pack(pady=(0, 10))

        self.prog = ttk.Progressbar(bottom_frame, style="Cyber.Horizontal.TProgressbar", 
                                    orient="horizontal", length=700, mode="determinate", maximum=100)
        self.prog.pack(fill="x")

        # FRASES
        self.phrases = phrasesgod

        # ---------------------------------------------------------------
        # VERSIÓN Y CRÉDITOS (FIX: ESTILO SYSTEM HEADER)
        # ---------------------------------------------------------------
        ver_actual = globals().get("version", "v?.?")
        
        # Color de texto: Un gris azulado suave para que no distraiga (#5c6b7f)
        # Fuente: Consolas (o JetBrains) para mantener el look hacker/tech

        # 1. Dev Name (Esquina Superior Izquierda)
        tk.Label(self.inner_frame, 
                 text="[ Dev: Kevin González ]", 
                 font=("Consolas", 8), 
                 bg="#1a1a2e", 
                 fg="#5c6b7f"
                 ).place(x=15, y=10) # x=15, y=10 lo pega arriba a la izquierda

        # 2. Versión (Esquina Superior Derecha)
        tk.Label(self.inner_frame, 
                 text=f"[ Sys.Ver: {ver_actual} ]", 
                 font=("Consolas", 8, "bold"), 
                 bg="#1a1a2e", 
                 fg="#5c6b7f"
                 ).place(relx=1.0, x=-15, y=10, anchor="ne") # Anchor NorthEast (Arriba Derecha)


        self.finished = False
        # IDs de after() pendientes: se cancelan en destroy() para que Tcl no
        # intente ejecutar un comando ya borrado ("invalid command name ...<lambda>").
        self._job_progress = None
        self._job_frases = None
        self._job_final = None
        self._jobs_status = set()
        threading.Thread(target=self.run_loading_process).start()
        self.animate_progress()
        self.animate_phrases(2200)
        

    # --- NUEVO: MÉTODO DESTRUIR SEGURO ---
    def destroy(self):
        self.running = False  # Detiene los bucles inmediatamente
        # Cancelar TODO lo programado con after() antes de destruir: si queda un
        # temporizador vivo, al dispararse Tcl ya no encuentra su comando y
        # imprime "invalid command name ...<lambda>" en consola.
        pendientes = [self._job_progress, self._job_frases, self._job_final]
        pendientes.extend(list(getattr(self, "_jobs_status", ())))
        for aid in pendientes:
            if aid:
                try:
                    self.after_cancel(aid)
                except Exception:
                    pass
        super().destroy()

    def run_loading_process(self):
        try:
            # Usamos una lambda segura que verifica si seguimos corriendo
            cargar_librerias_pesadas_global(lambda pct, msg: self.update_status(pct, msg))
        except Exception as e:
            print(f"Error carga: {e}")
        self.finished = True

    def update_status(self, pct, msg):
        if not self.running: return # Seguridad
        try:
            aid = self.after(0, lambda: self.safe_config(self.prog, 'value', pct))
            self._jobs_status.add(aid)
            if msg and str(msg).strip():
                aid = self.after(0, lambda: self.safe_config(self.lbl_status, 'text', msg))
                self._jobs_status.add(aid)
        except: pass

    # Helper para configurar widgets sin crashear
    def safe_config(self, widget, key, value):
        if self.running:
            try:
                if key == 'value': widget.config(value=value)
                else: widget.config(text=value)
            except: pass

    def animate_progress(self):
        if not self.running: return
        if self.finished:
            # Llenar la barra visualmente
            try:
                self.prog['value'] = 100
            except: pass
            
            # --- CAMBIO AQUÍ: Reducimos la espera de 1500 a 100 milisegundos ---
            # Ya no esperamos nada. En cuanto termina la carga, avisamos al main.
            self._job_final = self.after(100, self.finalizar_transicion)
        else:
            try:
                curr = self.prog['value']
                # Hacemos que la barra avance un poco más rápido si se queda atrás
                if curr < 95: self.prog['value'] = curr + 1.5 
            except: pass
            self._job_progress = self.after(30, self.animate_progress) # Loop un poco más rápido (30ms)

    def animate_phrases(self, interval=2200):
        if not self.running: return # Seguridad anti-crash

        try:
            if not self.finished:
                frase = random.choice(self.phrases)
                color = "#e0e0e0"
                
                if any(x in frase for x in ["ERROR", "glitch"]): color = "#e67e22"
                elif any(x in frase for x in ["Schrödinger", "Hilbert"]): color = "#4c88b7"
                elif any(x in frase for x in ["量子", "Инициализация"]): color = "#2cc985"

                self.lbl_status.config(text=frase, fg=color)
                self._job_frases = self.after(interval, lambda: self.animate_phrases(interval))
        except: pass

    # def finalizar_transicion(self):
    #     self.ready_to_exit = True

    def finalizar_transicion(self):
        """
        Versión corregida: Solo avisa que terminó. 
        NO lanza la App aquí. Deja que el bloque main lo haga.
        """
         
        try:
            if self.running:
                # 1. Poner barra al 100% y texto verde
                self.prog['value'] = 100
                self.lbl_status.config(text="SISTEMA LISTO. EJECUTANDO...", fg="#2cc985")
                self.update_idletasks()
                self.update()
        except: pass

        # 2. SEÑAL CLAVE: Esto le dice al bloque __main__ que arranque
        self.ready_to_exit = True




def _transcribe_safe(model, audio, **kwargs):
        """
        Wrapper para faster_whisper.transcribe() que hace fallback sin VAD
        si onnxruntime no está disponible en el entorno frozen (exe compilado).
        Si la versión instalada no conoce 'multilingual', reintenta sin esa opción.
        """
        try:
            return model.transcribe(audio, **kwargs)
        except TypeError as e:
            if "multilingual" not in str(e) or "multilingual" not in kwargs:
                raise
            print("[WARN] Esta versión de faster-whisper no soporta multilingüe por segmento.")
            kwargs.pop("multilingual", None)
            return model.transcribe(audio, **kwargs)
        except RuntimeError as e:
            err = str(e).lower()
            if "onnxruntime" in err or "vad" in err:
                print("[WARN] VAD filter no disponible, reintentando sin VAD...")
                kwargs.pop("vad_filter", None)
                kwargs.pop("vad_parameters", None)
                return model.transcribe(audio, vad_filter=False, **kwargs)
            raise
# ==============================================================================
#   CLASE PRINCIPAL
# ==============================================================================
# ==============================================================================
#   METADATA LAB — MOTOR (BLOQUE NUEVO, USO EXCLUSIVO DEL MÓDULO METADATA LAB)
# ------------------------------------------------------------------------------
#   Este bloque NO es usado por ningún otro módulo de la aplicación.
#   Separa la lógica de metadatos de la interfaz:
#       detector -> lector -> modelo editable -> escritor
#       sanitizador -> procesador por formato -> verificación
#   Reglas: no recodificar cuando se puede evitar, nunca destruir el original,
#   y verificar el resultado antes de darlo por bueno.
# ==============================================================================

import struct as _mlab_struct
import zlib as _mlab_zlib
import zipfile as _mlab_zipfile
import xml.etree.ElementTree as _mlab_ET

MLAB_SENSITIVE_GROUPS = ("Ubicación", "Dispositivo", "Autoría", "Software", "Fechas")


# ------------------------------------------------------------------------------
#   1. DETECTOR DE FORMATO Y CAPACIDADES
# ------------------------------------------------------------------------------

# kind  : familia de procesamiento
# edit  : permite edición manual de campos
# clean : permite sanitización (crear *_CLEAN)
# copy  : la edición NO sobrescribe el original, genera *_editado
MLAB_FORMATS = {
    ".jpg":  {"kind": "jpeg",  "edit": True,  "clean": True,  "label": "JPEG"},
    ".jpeg": {"kind": "jpeg",  "edit": True,  "clean": True,  "label": "JPEG"},
    ".jpe":  {"kind": "jpeg",  "edit": True,  "clean": True,  "label": "JPEG"},
    ".png":  {"kind": "png",   "edit": True,  "clean": True,  "label": "PNG"},
    ".webp": {"kind": "webp",  "edit": False, "clean": True,  "label": "WebP"},
    ".tif":  {"kind": "tiff",  "edit": True,  "clean": True,  "label": "TIFF"},
    ".tiff": {"kind": "tiff",  "edit": True,  "clean": True,  "label": "TIFF"},

    ".mp3":  {"kind": "audio", "edit": True,  "clean": True,  "label": "MP3"},
    ".flac": {"kind": "audio", "edit": True,  "clean": True,  "label": "FLAC"},
    ".m4a":  {"kind": "audio", "edit": True,  "clean": True,  "label": "M4A"},
    ".ogg":  {"kind": "audio", "edit": True,  "clean": True,  "label": "OGG"},
    ".opus": {"kind": "audio", "edit": True,  "clean": True,  "label": "Opus"},
    ".wav":  {"kind": "audio", "edit": True,  "clean": True,  "label": "WAV"},
    ".aac":  {"kind": "audio", "edit": False, "clean": True,  "label": "AAC"},

    ".mp4":  {"kind": "video", "edit": True,  "clean": True,  "copy": True, "label": "MP4"},
    ".m4v":  {"kind": "video", "edit": True,  "clean": True,  "copy": True, "label": "M4V"},
    ".mov":  {"kind": "video", "edit": True,  "clean": True,  "copy": True, "label": "MOV"},
    ".mkv":  {"kind": "video", "edit": True,  "clean": True,  "copy": True, "label": "MKV"},
    ".webm": {"kind": "video", "edit": True,  "clean": True,  "copy": True, "label": "WebM"},
    ".avi":  {"kind": "video", "edit": False, "clean": True,  "label": "AVI"},
    ".wmv":  {"kind": "video", "edit": False, "clean": True,  "label": "WMV"},
    ".flv":  {"kind": "video", "edit": False, "clean": True,  "label": "FLV"},

    ".pdf":  {"kind": "pdf",   "edit": True,  "clean": True,  "label": "PDF"},

    ".docx": {"kind": "ooxml", "edit": True,  "clean": True,  "label": "Word"},
    ".xlsx": {"kind": "ooxml", "edit": True,  "clean": True,  "label": "Excel"},
    ".xlsm": {"kind": "ooxml", "edit": True,  "clean": True,  "label": "Excel (macros)"},
    ".pptx": {"kind": "ooxml", "edit": True,  "clean": True,  "label": "PowerPoint"},
    ".ppsx": {"kind": "ooxml", "edit": True,  "clean": True,  "label": "PowerPoint"},

    # Solo lectura: sanitizarlos puede romper el archivo (los datos de imagen
    # se referencian desde los propios IFD) o no hay forma fiable de hacerlo.
    ".cr2":  {"kind": "raw",   "edit": False, "clean": False, "label": "RAW Canon"},
    ".cr3":  {"kind": "raw",   "edit": False, "clean": False, "label": "RAW Canon"},
    ".nef":  {"kind": "raw",   "edit": False, "clean": False, "label": "RAW Nikon"},
    ".arw":  {"kind": "raw",   "edit": False, "clean": False, "label": "RAW Sony"},
    ".dng":  {"kind": "raw",   "edit": False, "clean": False, "label": "DNG"},
    ".heic": {"kind": "heif",  "edit": False, "clean": False, "label": "HEIC"},
    ".heif": {"kind": "heif",  "edit": False, "clean": False, "label": "HEIF"},
}

MLAB_VALID_EXT = set(MLAB_FORMATS.keys())


def mlab_caps(path):
    """Devuelve las capacidades del formato. Nunca lanza excepción."""
    try:
        ext = os.path.splitext(path)[1].lower()
    except Exception:
        ext = ""
    info = MLAB_FORMATS.get(ext)
    if not info:
        return {"ext": ext, "kind": None, "edit": False, "clean": False,
                "copy": False, "analyze": False, "label": "No soportado"}
    return {"ext": ext, "kind": info["kind"], "edit": info["edit"],
            "clean": info["clean"], "copy": info.get("copy", False),
            "analyze": True, "label": info["label"]}


def mlab_field(key, label, value, ftype="text", group="Información", sensitive=False):
    return {"key": key, "label": label, "value": "" if value is None else str(value),
            "type": ftype, "group": group, "sensitive": bool(sensitive)}


# ------------------------------------------------------------------------------
#   2. UTILIDADES COMUNES
# ------------------------------------------------------------------------------

def mlab_unique_path(path):
    """Evita sobrescribir: archivo.ext -> archivo (1).ext si ya existe."""
    if not os.path.exists(path):
        return path
    base, ext = os.path.splitext(path)
    i = 1
    while True:
        cand = f"{base} ({i}){ext}"
        if not os.path.exists(cand):
            return cand
        i += 1


def mlab_target_path(path, suffix="_CLEAN"):
    folder, filename = os.path.split(path)
    name, ext = os.path.splitext(filename)
    return mlab_unique_path(os.path.join(folder, f"{name}{suffix}{ext}"))


def _mlab_tmp_for(path):
    folder, filename = os.path.split(path)
    return os.path.join(folder, f".~mlab_{uuid.uuid4().hex[:8]}_{filename}")


def _mlab_commit(tmp, dst):
    """Movimiento atómico del temporal al destino final (si falla, se borra el temporal)."""
    try:
        os.replace(tmp, dst)
    except Exception:
        _mlab_discard(tmp)
        raise


def _mlab_escribir_atomico(dst, datos):
    """Escribe en un temporal junto al destino y lo reemplaza; sin restos si algo falla."""
    tmp = _mlab_tmp_for(dst)
    try:
        with open(tmp, "wb") as fh:
            fh.write(datos)
    except Exception:
        _mlab_discard(tmp)
        raise
    _mlab_commit(tmp, dst)


def _mlab_discard(tmp):
    try:
        if tmp and os.path.exists(tmp):
            os.remove(tmp)
    except Exception:
        pass


def _mlab_run(cmd, timeout=600):
    """Ejecuta un proceso capturando stderr (nunca lo tira a DEVNULL)."""
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                          text=True, encoding="utf-8", errors="ignore",
                          timeout=timeout, startupinfo=_startup_info_modulo())
    return proc.returncode, (proc.stdout or ""), (proc.stderr or "")


def _mlab_ffprobe(path):
    """Datos objetivos del archivo multimedia (para verificar que no se dañó)."""
    exe = shutil.which("ffprobe")
    if not exe:
        return None
    try:
        rc, out, _ = _mlab_run([exe, "-v", "quiet", "-print_format", "json",
                                "-show_format", "-show_streams", path], timeout=120)
        if rc != 0:
            return None
        return json.loads(out)
    except Exception:
        return None


def _mlab_media_signature(path):
    """Firma de contenido: duración, nº de streams y códecs. Para comparar."""
    data = _mlab_ffprobe(path)
    if not data:
        return None
    try:
        dur = float(data.get("format", {}).get("duration", 0) or 0)
    except Exception:
        dur = 0.0
    streams, media = [], []
    for s in data.get("streams", []):
        attached = bool((s.get("disposition") or {}).get("attached_pic"))
        item = (s.get("codec_type"), s.get("codec_name"),
                s.get("width"), s.get("height"))
        streams.append(item)
        if not attached:
            media.append(item)
    return {"duration": dur, "streams": streams, "n": len(streams),
            "media": media, "n_media": len(media)}


def _mlab_dec(val):
    """Convierte cualquier valor crudo de metadata a texto legible."""
    if val is None:
        return ""
    if isinstance(val, bytes):
        for enc in ("utf-8", "utf-16", "latin-1"):
            try:
                return val.decode(enc).replace("\x00", "").strip()
            except Exception:
                continue
        return ""
    if isinstance(val, (list, tuple)):
        return ", ".join(_mlab_dec(v) for v in val if v not in (None, ""))
    return str(val).strip()


# ------------------------------------------------------------------------------
#   3. IMÁGENES — JPEG (strip a nivel de segmentos, sin recodificar)
# ------------------------------------------------------------------------------

# Segmentos que SÍ se conservan porque afectan a cómo se decodifica o se ve la
# imagen: JFIF (densidad), ICC_PROFILE (color) y Adobe APP14 (transformación de
# color en CMYK/YCCK). Todo lo demás (EXIF, XMP, IPTC, Photoshop, comentarios,
# miniaturas) es metadata y se elimina.
def _jpeg_keep_segment(marker, payload):
    if marker == 0xFE:                      # COM
        return False
    if 0xE0 <= marker <= 0xEF:              # APPn
        if marker == 0xE0 and payload[:5] == b"JFIF\x00":
            return True
        if marker == 0xE2 and payload[:11] == b"ICC_PROFILE":
            return True
        if marker == 0xEE and payload[:5] == b"Adobe":
            return True
        return False
    return True


def _jpeg_iter_segments(data):
    """Genera (marker, offset_segmento, longitud_total, payload)."""
    if data[:2] != b"\xff\xd8":
        raise ValueError("No es un JPEG válido (falta SOI).")
    i, n = 2, len(data)
    while i < n:
        if data[i] != 0xFF:
            raise ValueError("Estructura JPEG inesperada.")
        while i < n and data[i] == 0xFF:
            i += 1
        if i >= n:
            break
        marker = data[i]
        i += 1
        if marker in (0xD9,):                       # EOI
            yield (marker, i - 2, 2, b"")
            return
        if marker == 0xDA:                          # SOS: a partir de aquí, datos
            yield (marker, i - 2, n - (i - 2), data[i:])
            return
        if 0xD0 <= marker <= 0xD7 or marker == 0x01:
            yield (marker, i - 2, 2, b"")
            continue
        if i + 2 > n:
            break
        seglen = _mlab_struct.unpack(">H", data[i:i + 2])[0]
        payload = data[i + 2:i + seglen]
        yield (marker, i - 2, seglen + 2, payload)
        i += seglen


def _jpeg_strip_bytes(data):
    out = bytearray(b"\xff\xd8")
    for marker, off, length, payload in _jpeg_iter_segments(data):
        if marker == 0xDA:
            out += data[off:]
            break
        if marker == 0xD9:
            out += b"\xff\xd9"
            break
        if _jpeg_keep_segment(marker, payload):
            out += data[off:off + length]
    return bytes(out)


def _jpeg_sanitize(src, dst):
    with open(src, "rb") as fh:
        data = fh.read()
    clean = _jpeg_strip_bytes(data)
    _mlab_escribir_atomico(dst, clean)
    return True, None


# --- EXIF: catálogo de campos expuestos al usuario -----------------------------
def _jpeg_exif_catalog():
    import piexif
    return [
        # (key, label, ifd, tag, type, group, sensible)
        ("exif:Artist",       "Autor / Artista",   "0th",  piexif.ImageIFD.Artist,           "text", "Autoría",    True),
        ("exif:Copyright",    "Copyright",         "0th",  piexif.ImageIFD.Copyright,        "text", "Autoría",    False),
        ("exif:ImageDescription", "Descripción",   "0th",  piexif.ImageIFD.ImageDescription, "text", "Información", False),
        ("exif:Software",     "Software",          "0th",  piexif.ImageIFD.Software,         "text", "Software",   True),
        ("exif:Make",         "Marca del equipo",  "0th",  piexif.ImageIFD.Make,             "text", "Dispositivo", True),
        ("exif:Model",        "Modelo del equipo", "0th",  piexif.ImageIFD.Model,            "text", "Dispositivo", True),
        ("exif:DateTime",     "Fecha de archivo",  "0th",  piexif.ImageIFD.DateTime,         "date", "Fechas",     True),
        ("exif:DateTimeOriginal", "Fecha de captura", "Exif", piexif.ExifIFD.DateTimeOriginal, "date", "Fechas",  True),
        ("exif:BodySerialNumber", "Nº de serie",   "Exif", piexif.ExifIFD.BodySerialNumber,  "text", "Dispositivo", True),
        ("exif:LensModel",    "Objetivo",          "Exif", piexif.ExifIFD.LensModel,         "text", "Dispositivo", False),
        ("exif:UserComment",  "Comentario",        "Exif", piexif.ExifIFD.UserComment,       "comment", "Información", False),
    ]


def _exif_gps_to_text(gps):
    """Convierte el IFD GPS a 'lat, lon' decimal legible."""
    import piexif
    try:
        def _deg(v, ref):
            d = v[0][0] / v[0][1]
            m = v[1][0] / v[1][1]
            s = v[2][0] / v[2][1]
            val = d + m / 60.0 + s / 3600.0
            if ref in (b"S", b"W", "S", "W"):
                val = -val
            return val
        lat = gps.get(piexif.GPSIFD.GPSLatitude)
        lon = gps.get(piexif.GPSIFD.GPSLongitude)
        if not lat or not lon:
            return ""
        la = _deg(lat, gps.get(piexif.GPSIFD.GPSLatitudeRef, b"N"))
        lo = _deg(lon, gps.get(piexif.GPSIFD.GPSLongitudeRef, b"E"))
        return f"{la:.6f}, {lo:.6f}"
    except Exception:
        return ""


def _exif_text_to_gps(text):
    """'20.6597, -103.3496' -> diccionario GPS IFD de piexif."""
    import piexif
    parts = [p.strip() for p in str(text).replace(";", ",").split(",") if p.strip()]
    if len(parts) < 2:
        raise ValueError("Formato GPS inválido. Usa: latitud, longitud")
    la, lo = float(parts[0]), float(parts[1])
    if not (-90 <= la <= 90) or not (-180 <= lo <= 180):
        raise ValueError("Coordenadas fuera de rango.")

    def _rat(val):
        val = abs(val)
        d = int(val)
        m = int((val - d) * 60)
        s = (val - d - m / 60.0) * 3600.0
        return ((d, 1), (m, 1), (int(round(s * 10000)), 10000))

    return {
        piexif.GPSIFD.GPSLatitudeRef: b"N" if la >= 0 else b"S",
        piexif.GPSIFD.GPSLatitude: _rat(la),
        piexif.GPSIFD.GPSLongitudeRef: b"E" if lo >= 0 else b"W",
        piexif.GPSIFD.GPSLongitude: _rat(lo),
    }


def _exif_load(path):
    import piexif
    try:
        return piexif.load(path)
    except Exception:
        return {"0th": {}, "Exif": {}, "GPS": {}, "1st": {}, "thumbnail": None}


def _exif_read_fields(path):
    import piexif
    fields = []
    exif = _exif_load(path)
    for key, label, ifd, tag, ftype, group, sens in _jpeg_exif_catalog():
        raw = exif.get(ifd, {}).get(tag)
        if raw in (None, b"", ""):
            continue
        if ftype == "comment":
            try:
                import piexif.helper
                val = piexif.helper.UserComment.load(raw)
            except Exception:
                val = _mlab_dec(raw)
        else:
            val = _mlab_dec(raw)
        if val:
            fields.append(mlab_field(key, label, val, ftype, group, sens))
    gps_txt = _exif_gps_to_text(exif.get("GPS", {}) or {})
    if gps_txt:
        fields.append(mlab_field("exif:GPS", "Ubicación GPS", gps_txt, "gps", "Ubicación", True))
    return fields


def _exif_write_fields(path, values):
    """Escribe EXIF respetando el tipo de cada tag. No recodifica el JPEG."""
    import piexif
    exif = _exif_load(path)
    for ifd in ("0th", "Exif", "GPS", "1st"):
        exif.setdefault(ifd, {})

    catalog = {c[0]: c for c in _jpeg_exif_catalog()}
    for key, val in values.items():
        val = "" if val is None else str(val).strip()
        if key == "exif:GPS":
            if val:
                exif["GPS"] = _exif_text_to_gps(val)
            else:
                exif["GPS"] = {}
            continue
        if key not in catalog:
            continue
        _, _, ifd, tag, ftype, _, _ = catalog[key]
        if not val:
            exif[ifd].pop(tag, None)
            continue
        if ftype == "comment":
            import piexif.helper
            try:
                val.encode("ascii")
                enc = "ascii"
            except Exception:
                enc = "unicode"
            exif[ifd][tag] = piexif.helper.UserComment.dump(val, encoding=enc)
        elif ftype == "date":
            txt = val.replace("-", ":").replace("/", ":")
            if len(txt) == 10:
                txt += " 00:00:00"
            if not re.match(r"^\d{4}:\d{2}:\d{2} \d{2}:\d{2}:\d{2}$", txt):
                raise ValueError(f"'{catalog[key][1]}' debe tener formato AAAA:MM:DD HH:MM:SS")
            exif[ifd][tag] = txt.encode("ascii")
        else:
            try:
                exif[ifd][tag] = val.encode("ascii")
            except UnicodeEncodeError:
                # Los tags ASCII de EXIF no admiten UTF-8; se transcribe lo que
                # se pueda en vez de escribir bytes inválidos en el archivo.
                exif[ifd][tag] = val.encode("ascii", "replace")

    if exif.get("thumbnail") is None:
        exif["1st"] = {}
    exif_bytes = piexif.dump(exif)
    tmp = _mlab_tmp_for(path)
    shutil.copy2(path, tmp)
    try:
        piexif.insert(exif_bytes, tmp)   # sustituye solo el segmento APP1
        _mlab_commit(tmp, path)
    except Exception:
        _mlab_discard(tmp)
        raise
    return path


# ------------------------------------------------------------------------------
#   4. IMÁGENES — PNG (reescritura de chunks, IDAT intacto)
# ------------------------------------------------------------------------------

_PNG_SIG = b"\x89PNG\r\n\x1a\n"
# Chunks auxiliares que afectan a cómo se ve la imagen: se conservan.
_PNG_KEEP_ANCILLARY = {
    b"tRNS", b"gAMA", b"cHRM", b"sRGB", b"iCCP", b"sBIT", b"bKGD",
    b"pHYs", b"hIST", b"sPLT", b"acTL", b"fcTL", b"fdAT", b"cICP",
    b"mDCv", b"cLLi", b"cLLI",
}
_PNG_TEXT_KEYS = [
    ("png:Title",         "Título",      "Title",         False),
    ("png:Author",        "Autor",       "Author",        True),
    ("png:Description",   "Descripción", "Description",   False),
    ("png:Copyright",     "Copyright",   "Copyright",     False),
    ("png:Creation Time", "Fecha",       "Creation Time", True),
    ("png:Software",      "Software",    "Software",      True),
    ("png:Comment",       "Comentario",  "Comment",       False),
]


def _png_iter_chunks(data):
    if data[:8] != _PNG_SIG:
        raise ValueError("No es un PNG válido.")
    i = 8
    n = len(data)
    while i + 8 <= n:
        length = _mlab_struct.unpack(">I", data[i:i + 4])[0]
        ctype = data[i + 4:i + 8]
        payload = data[i + 8:i + 8 + length]
        yield ctype, payload
        i += 12 + length
        if ctype == b"IEND":
            break


def _png_chunk(ctype, payload):
    return (_mlab_struct.pack(">I", len(payload)) + ctype + payload +
            _mlab_struct.pack(">I", _mlab_zlib.crc32(ctype + payload) & 0xFFFFFFFF))


def _png_decode_text(ctype, payload):
    try:
        if ctype == b"tEXt":
            k, _, v = payload.partition(b"\x00")
            return k.decode("latin-1"), v.decode("latin-1")
        if ctype == b"zTXt":
            k, _, rest = payload.partition(b"\x00")
            return k.decode("latin-1"), _mlab_zlib.decompress(rest[1:]).decode("latin-1")
        if ctype == b"iTXt":
            k, _, rest = payload.partition(b"\x00")
            comp_flag = rest[0:1]
            rest = rest[2:]
            _, _, rest = rest.partition(b"\x00")   # language tag
            _, _, txt = rest.partition(b"\x00")    # translated keyword
            if comp_flag == b"\x01":
                txt = _mlab_zlib.decompress(txt)
            return k.decode("latin-1"), txt.decode("utf-8", "replace")
    except Exception:
        pass
    return None, None


def _png_read_fields(path):
    with open(path, "rb") as fh:
        data = fh.read()
    found = {}
    for ctype, payload in _png_iter_chunks(data):
        if ctype in (b"tEXt", b"zTXt", b"iTXt"):
            k, v = _png_decode_text(ctype, payload)
            if k and v and k not in found:
                found[k] = v
        elif ctype == b"tIME" and len(payload) == 7:
            y, mo, d, h, mi, s = _mlab_struct.unpack(">HBBBBB", payload)
            found.setdefault("Creation Time", f"{y:04d}-{mo:02d}-{d:02d} {h:02d}:{mi:02d}:{s:02d}")
    fields = []
    for key, label, pngkey, sens in _PNG_TEXT_KEYS:
        if found.get(pngkey):
            group = "Autoría" if sens and pngkey == "Author" else (
                "Software" if pngkey == "Software" else
                "Fechas" if pngkey == "Creation Time" else "Información")
            fields.append(mlab_field(key, label, found[pngkey], "text", group, sens))
    for k, v in found.items():
        if k not in [p[2] for p in _PNG_TEXT_KEYS]:
            fields.append(mlab_field(f"png:{k}", k, v, "text", "Información", False))
    return fields


def _png_rewrite(src, dst, text_map=None, strip_all=False):
    """Reescribe el PNG conservando IDAT byte a byte."""
    with open(src, "rb") as fh:
        data = fh.read()
    text_map = dict(text_map or {})
    out = bytearray(_PNG_SIG)
    inserted = False
    for ctype, payload in _png_iter_chunks(data):
        if ctype in (b"tEXt", b"zTXt", b"iTXt", b"tIME", b"eXIf", b"dSIG"):
            continue
        is_critical = bytes(ctype)[0:1].isupper()
        if not is_critical and ctype not in _PNG_KEEP_ANCILLARY:
            continue  # auxiliar desconocido: por spec es descartable
        if ctype == b"IDAT" and not inserted:
            if not strip_all and text_map:
                for k, v in text_map.items():
                    if not v:
                        continue
                    try:
                        payload_txt = k.encode("latin-1") + b"\x00" + v.encode("latin-1")
                        out += _png_chunk(b"tEXt", payload_txt)
                    except UnicodeEncodeError:
                        payload_txt = (k.encode("latin-1") + b"\x00\x00\x00" +
                                       b"\x00" + b"\x00" + v.encode("utf-8"))
                        out += _png_chunk(b"iTXt", payload_txt)
            inserted = True
        out += _png_chunk(ctype, payload)
    _mlab_escribir_atomico(dst, bytes(out))
    return True, None


def _png_write_fields(path, values):
    current = {}
    for f in _png_read_fields(path):
        current[f["key"].split(":", 1)[1]] = f["value"]
    for key, val in values.items():
        if not key.startswith("png:"):
            continue
        name = key.split(":", 1)[1]
        if val:
            current[name] = str(val)
        else:
            current.pop(name, None)
    _png_rewrite(path, path, text_map=current)
    return path


# ------------------------------------------------------------------------------
#   5. IMÁGENES — WebP (contenedor RIFF) y TIFF (Pillow, sin pérdida)
# ------------------------------------------------------------------------------

def _webp_chunks(data):
    i = 12
    n = len(data)
    while i + 8 <= n:
        cid = data[i:i + 4]
        size = _mlab_struct.unpack("<I", data[i + 4:i + 8])[0]
        payload = data[i + 8:i + 8 + size]
        yield cid, payload
        i += 8 + size + (size & 1)


def _webp_sanitize(src, dst):
    with open(src, "rb") as fh:
        data = fh.read()
    if data[:4] != b"RIFF" or data[8:12] != b"WEBP":
        raise ValueError("No es un WebP válido.")
    body = bytearray()
    for cid, payload in _webp_chunks(data):
        # El perfil de color (ICCP) NO es metadata personal: se conserva, igual
        # que el ICC_PROFILE en JPEG. Sin él los colores se ven distintos.
        if cid in (b"EXIF", b"XMP "):
            continue
        if cid == b"VP8X" and len(payload) >= 1:
            flags = payload[0] & ~0x0C   # limpia EXIF(0x08) y XMP(0x04); ICC(0x20) queda
            payload = bytes([flags]) + payload[1:]
        body += cid + _mlab_struct.pack("<I", len(payload)) + payload
        if len(payload) & 1:
            body += b"\x00"
    out = b"RIFF" + _mlab_struct.pack("<I", len(body) + 4) + b"WEBP" + bytes(body)
    _mlab_escribir_atomico(dst, out)
    return True, None


def _webp_read_fields(path):
    """Solo lectura: el editor no ofrece edición manual para WebP."""
    fields = []
    try:
        with open(path, "rb") as fh:
            data = fh.read()
        for cid, payload in _webp_chunks(data):
            if cid == b"EXIF":
                tmp_fields = _exif_read_from_bytes(payload)
                fields.extend(tmp_fields)
            elif cid == b"XMP ":
                fields.append(mlab_field("webp:XMP", "Bloque XMP",
                                         f"{len(payload)} bytes", "text", "Información", True))
    except Exception:
        pass
    return fields


def _exif_read_from_bytes(blob):
    import piexif
    out = []
    try:
        if blob[:6] == b"Exif\x00\x00":
            blob = blob[6:]
        exif = piexif.load(b"Exif\x00\x00" + blob)
    except Exception:
        return out
    for key, label, ifd, tag, ftype, group, sens in _jpeg_exif_catalog():
        raw = exif.get(ifd, {}).get(tag)
        val = _mlab_dec(raw)
        if val:
            out.append(mlab_field(key, label, val, ftype, group, sens))
    gps = _exif_gps_to_text(exif.get("GPS", {}) or {})
    if gps:
        out.append(mlab_field("exif:GPS", "Ubicación GPS", gps, "gps", "Ubicación", True))
    return out


_TIFF_CATALOG = [
    ("tiff:Artist",           "Autor / Artista", 315, "Autoría",     True),
    ("tiff:Copyright",        "Copyright",       33432, "Autoría",   False),
    ("tiff:ImageDescription", "Descripción",     270, "Información", False),
    ("tiff:Software",         "Software",        305, "Software",    True),
    ("tiff:Make",             "Marca del equipo", 271, "Dispositivo", True),
    ("tiff:Model",            "Modelo del equipo", 272, "Dispositivo", True),
    ("tiff:DateTime",         "Fecha",           306, "Fechas",      True),
]
# Tags que describen la estructura de la imagen: jamás se tocan.
_TIFF_STRUCTURAL = {
    256, 257, 258, 259, 262, 263, 264, 265, 266, 273, 274, 277, 278, 279,
    280, 281, 282, 283, 284, 286, 287, 296, 317, 320, 322, 323, 324, 325,
    338, 339, 32997, 32998, 33421, 33422, 34665, 34675,
}


def _tiff_compression(img):
    comp = img.info.get("compression")
    return comp if comp else "raw"


def _tiff_is_lossy(path):
    try:
        from PIL import Image as _I
        with _I.open(path) as im:
            return str(_tiff_compression(im)).lower() in ("jpeg", "tiff_jpeg")
    except Exception:
        return False


def _tiff_read_fields(path):
    from PIL import Image as _I
    fields = []
    with _I.open(path) as im:
        tags = getattr(im, "tag_v2", {}) or {}
        for key, label, tag, group, sens in _TIFF_CATALOG:
            val = _mlab_dec(tags.get(tag))
            if val:
                fields.append(mlab_field(key, label, val, "text", group, sens))
        if 34853 in tags:
            fields.append(mlab_field("tiff:GPS", "Ubicación GPS", "Presente (IFD GPS)",
                                     "readonly", "Ubicación", True))
    return fields


def _tiff_save(path, dst, new_tags=None, strip=False):
    """Reescritura sin pérdida: se conserva la compresión original y las páginas."""
    from PIL import Image as _I
    from PIL.TiffImagePlugin import ImageFileDirectory_v2
    with _I.open(path) as im:
        if str(_tiff_compression(im)).lower() in ("jpeg", "tiff_jpeg"):
            raise ValueError("TIFF con compresión JPEG interna: solo se permite analizar "
                             "(reescribirlo obligaría a recomprimir y perder calidad).")
        comp = _tiff_compression(im)
        frames = []
        try:
            while True:
                frames.append(im.copy())
                im.seek(im.tell() + 1)
        except EOFError:
            pass
        ifd = ImageFileDirectory_v2()
        src_tags = getattr(im, "tag_v2", {}) or {}
        for tag in list(src_tags.keys()):
            if tag in _TIFF_STRUCTURAL:
                continue
            if strip:
                continue
            if tag in [c[2] for c in _TIFF_CATALOG]:
                continue          # los del catálogo se reponen abajo
            if tag in (34853, 700, 33723, 37724):   # GPS, XMP, IPTC, Photoshop
                continue
            try:
                ifd[tag] = src_tags[tag]
            except Exception:
                pass
        if not strip:
            for tag, val in (new_tags or {}).items():
                if val:
                    ifd[tag] = str(val)
    tmp = _mlab_tmp_for(dst)
    try:
        head = frames[0]
        kwargs = {"compression": comp, "tiffinfo": ifd}
        if len(frames) > 1:
            kwargs["save_all"] = True
            kwargs["append_images"] = frames[1:]
        head.save(tmp, format="TIFF", **kwargs)
        _mlab_commit(tmp, dst)
    except Exception:
        _mlab_discard(tmp)
        raise
    return True, None


def _tiff_write_fields(path, values):
    tagmap = {c[0]: c[2] for c in _TIFF_CATALOG}
    current = {}
    for f in _tiff_read_fields(path):
        if f["key"] in tagmap:
            current[tagmap[f["key"]]] = f["value"]
    for key, val in values.items():
        if key in tagmap:
            if val:
                current[tagmap[key]] = str(val)
            else:
                current.pop(tagmap[key], None)
    _tiff_save(path, path, new_tags=current)
    return path

# ------------------------------------------------------------------------------
#   6. AUDIO — adaptadores por formato (sin easy=True, para no perder campos)
# ------------------------------------------------------------------------------

_AUDIO_CATALOG = [
    ("title",       "Título",            "Información", False),
    ("artist",      "Artista",           "Autoría",     True),
    ("album",       "Álbum",             "Información", False),
    ("albumartist", "Artista del álbum", "Información", False),
    ("composer",    "Compositor",        "Autoría",     False),
    ("genre",       "Género",            "Información", False),
    ("date",        "Fecha / Año",       "Fechas",      True),
    ("tracknumber", "Pista",             "Información", False),
    ("discnumber",  "Disco",             "Información", False),
    ("comment",     "Comentario",        "Información", False),
    ("copyright",   "Copyright",         "Autoría",     False),
    ("grouping",    "Agrupación",        "Información", False),
    ("lyrics",      "Letra",             "Información", False),
    ("encodedby",   "Codificado por",    "Software",    True),
]

_ID3_FRAMES = {
    "title": "TIT2", "artist": "TPE1", "album": "TALB", "albumartist": "TPE2",
    "composer": "TCOM", "genre": "TCON", "date": "TDRC", "tracknumber": "TRCK",
    "discnumber": "TPOS", "copyright": "TCOP", "grouping": "TIT1", "encodedby": "TENC",
}
_VORBIS_KEYS = {
    "title": "TITLE", "artist": "ARTIST", "album": "ALBUM", "albumartist": "ALBUMARTIST",
    "composer": "COMPOSER", "genre": "GENRE", "date": "DATE", "tracknumber": "TRACKNUMBER",
    "discnumber": "DISCNUMBER", "comment": "COMMENT", "copyright": "COPYRIGHT",
    "grouping": "GROUPING", "lyrics": "LYRICS", "encodedby": "ENCODEDBY",
}
_MP4_KEYS = {
    "title": "\xa9nam", "artist": "\xa9ART", "album": "\xa9alb", "albumartist": "aART",
    "composer": "\xa9wrt", "genre": "\xa9gen", "date": "\xa9day", "comment": "\xa9cmt",
    "copyright": "cprt", "grouping": "\xa9grp", "lyrics": "\xa9lyr", "encodedby": "\xa9too",
}


def _audio_open(path, for_write=False):
    """Devuelve (objeto_mutagen, familia). familia: id3 | vorbis | mp4."""
    import mutagen
    ext = os.path.splitext(path)[1].lower()
    if ext == ".mp3":
        from mutagen.mp3 import MP3
        obj = MP3(path)
        if for_write and obj.tags is None:
            obj.add_tags()
        return obj, "id3"
    if ext == ".wav":
        from mutagen.wave import WAVE
        obj = WAVE(path)
        if for_write and obj.tags is None:
            obj.add_tags()
        return obj, "id3"
    if ext == ".aac":
        from mutagen.aac import AAC
        return AAC(path), "id3"
    if ext in (".m4a", ".mp4", ".m4v"):
        from mutagen.mp4 import MP4
        obj = MP4(path)
        if for_write and obj.tags is None:
            obj.add_tags()
        return obj, "mp4"
    if ext == ".flac":
        from mutagen.flac import FLAC
        return FLAC(path), "vorbis"
    if ext in (".ogg", ".opus", ".oga"):
        obj = mutagen.File(path)
        if obj is None:
            raise ValueError("No se pudo leer el contenedor Ogg.")
        return obj, "vorbis"
    obj = mutagen.File(path)
    if obj is None:
        raise ValueError("Formato de audio no reconocido.")
    fam = "mp4" if obj.__class__.__name__ == "MP4" else "vorbis"
    return obj, fam


def _audio_get(obj, fam, key):
    try:
        if fam == "id3":
            tags = obj.tags
            if not tags:
                return ""
            if key == "comment":
                frames = tags.getall("COMM")
                return _mlab_dec(frames[0].text) if frames else ""
            if key == "lyrics":
                frames = tags.getall("USLT")
                return _mlab_dec(frames[0].text) if frames else ""
            fid = _ID3_FRAMES.get(key)
            if not fid:
                return ""
            frames = tags.getall(fid)
            return _mlab_dec(frames[0].text) if frames else ""
        if fam == "vorbis":
            vk = _VORBIS_KEYS.get(key)
            if not vk:
                return ""
            val = obj.get(vk) or obj.get(vk.lower())
            if not val and key == "comment":
                val = obj.get("DESCRIPTION") or obj.get("description")
            return _mlab_dec(val)
        if fam == "mp4":
            if key in ("tracknumber", "discnumber"):
                atom = "trkn" if key == "tracknumber" else "disk"
                val = obj.get(atom)
                if val:
                    a, b = (list(val[0]) + [0, 0])[:2]
                    return f"{a}/{b}" if b else str(a)
                return ""
            mk = _MP4_KEYS.get(key)
            return _mlab_dec(obj.get(mk)) if mk else ""
    except Exception:
        return ""
    return ""


def _audio_set(obj, fam, key, val):
    val = "" if val is None else str(val).strip()
    if fam == "id3":
        import mutagen.id3 as _id3
        tags = obj.tags
        if key == "comment":
            tags.delall("COMM")
            if val:
                tags.add(_id3.COMM(encoding=3, lang="spa", desc="", text=[val]))
            return
        if key == "lyrics":
            tags.delall("USLT")
            if val:
                tags.add(_id3.USLT(encoding=3, lang="spa", desc="", text=val))
            return
        fid = _ID3_FRAMES.get(key)
        if not fid:
            return
        tags.delall(fid)
        if val:
            tags.add(getattr(_id3, fid)(encoding=3, text=[val]))
        return
    if fam == "vorbis":
        vk = _VORBIS_KEYS.get(key)
        if not vk:
            return
        for cand in (vk, vk.lower(), "DESCRIPTION", "description"):
            if cand in obj:
                try:
                    del obj[cand]
                except Exception:
                    pass
        if val:
            obj[vk] = [val]
        return
    if fam == "mp4":
        if key in ("tracknumber", "discnumber"):
            atom = "trkn" if key == "tracknumber" else "disk"
            obj.pop(atom, None)
            if val:
                nums = [int(x) for x in re.findall(r"\d+", val)[:2]] or [0]
                while len(nums) < 2:
                    nums.append(0)
                obj[atom] = [tuple(nums)]
            return
        mk = _MP4_KEYS.get(key)
        if not mk:
            return
        obj.pop(mk, None)
        if val:
            obj[mk] = [val]


def _audio_cover(path):
    """Devuelve (mime, bytes) de la carátula o None."""
    try:
        obj, fam = _audio_open(path)
        if fam == "id3" and obj.tags:
            pics = obj.tags.getall("APIC")
            if pics:
                return (pics[0].mime or "image/jpeg", pics[0].data)
        elif fam == "vorbis":
            pics = getattr(obj, "pictures", None)
            if pics:
                return (pics[0].mime or "image/jpeg", pics[0].data)
            blob = obj.get("metadata_block_picture") or obj.get("METADATA_BLOCK_PICTURE")
            if blob:
                import base64
                from mutagen.flac import Picture
                pic = Picture(base64.b64decode(blob[0]))
                return (pic.mime or "image/jpeg", pic.data)
        elif fam == "mp4":
            covr = obj.get("covr")
            if covr:
                from mutagen.mp4 import MP4Cover
                fmt = getattr(covr[0], "imageformat", MP4Cover.FORMAT_JPEG)
                mime = "image/png" if fmt == MP4Cover.FORMAT_PNG else "image/jpeg"
                return (mime, bytes(covr[0]))
    except Exception:
        return None
    return None


def _audio_set_cover(path, img_path):
    """img_path=None elimina la carátula. No toca el stream de audio."""
    data, mime = None, "image/jpeg"
    if img_path:
        with open(img_path, "rb") as fh:
            data = fh.read()
        if os.path.splitext(img_path)[1].lower() == ".png":
            mime = "image/png"
    obj, fam = _audio_open(path, for_write=True)
    if fam == "id3":
        import mutagen.id3 as _id3
        obj.tags.delall("APIC")
        if data:
            obj.tags.add(_id3.APIC(encoding=3, mime=mime, type=3, desc="Cover", data=data))
        obj.save()
    elif fam == "vorbis":
        import base64
        from mutagen.flac import Picture, FLAC
        if hasattr(obj, "clear_pictures"):
            obj.clear_pictures()
        for k in ("metadata_block_picture", "METADATA_BLOCK_PICTURE"):
            if k in obj:
                del obj[k]
        if data:
            pic = Picture()
            pic.data = data
            pic.type = 3
            pic.mime = mime
            if isinstance(obj, FLAC):
                obj.add_picture(pic)
            else:
                obj["metadata_block_picture"] = [base64.b64encode(pic.write()).decode("ascii")]
        obj.save()
    elif fam == "mp4":
        from mutagen.mp4 import MP4Cover
        obj.pop("covr", None)
        if data:
            fmt = MP4Cover.FORMAT_PNG if mime == "image/png" else MP4Cover.FORMAT_JPEG
            obj["covr"] = [MP4Cover(data, imageformat=fmt)]
        obj.save()
    return True


def _audio_read_fields(path):
    fields = []
    try:
        obj, fam = _audio_open(path)
    except Exception:
        return fields
    for key, label, group, sens in _AUDIO_CATALOG:
        val = _audio_get(obj, fam, key)
        if val:
            fields.append(mlab_field(f"audio:{key}", label, val, "text", group, sens))
    cover = _audio_cover(path)
    if cover:
        kb = max(1, len(cover[1]) // 1024)
        fields.append(mlab_field("audio:cover", "Carátula", f"{cover[0]} ({kb} KB)",
                                 "cover", "Información", False))
    return fields


def _audio_write_fields(path, values):
    obj, fam = _audio_open(path, for_write=True)
    for key, val in values.items():
        if not key.startswith("audio:"):
            continue
        name = key.split(":", 1)[1]
        if name == "cover":
            continue
        _audio_set(obj, fam, name, val)
    obj.save()
    return path


def _wav_sanitize(src, dst):
    """Elimina chunks RIFF de metadata conservando fmt/data intactos."""
    _DROP = {b"LIST", b"ID3 ", b"id3 ", b"bext", b"iXML", b"IXML", b"_PMX",
             b"CSET", b"DISP", b"umid", b"SMED", b"cart", b"afsp"}
    with open(src, "rb") as fh:
        data = fh.read()
    if data[:4] != b"RIFF" or data[8:12] != b"WAVE":
        raise ValueError("No es un WAV válido.")
    body = bytearray()
    i, n = 12, len(data)
    while i + 8 <= n:
        cid = data[i:i + 4]
        size = _mlab_struct.unpack("<I", data[i + 4:i + 8])[0]
        chunk = data[i:i + 8 + size + (size & 1)]
        if cid not in _DROP:
            body += chunk
        i += 8 + size + (size & 1)
    out = b"RIFF" + _mlab_struct.pack("<I", len(body) + 4) + b"WAVE" + bytes(body)
    _mlab_escribir_atomico(dst, out)
    return True, None


def _audio_sanitize(src, dst):
    ext = os.path.splitext(src)[1].lower()
    if ext == ".wav":
        return _wav_sanitize(src, dst)
    if ext in (".m4a", ".aac"):
        # El contenedor MP4 guarda la fecha de creación en las cabeceras
        # (mvhd/tkhd); solo un remux con -bitexact la deja en cero.
        # Se mapean solo las pistas de audio: la carátula es metadata y debe caer.
        ok, err = _video_sanitize(src, dst, audio_only=True)
        if ok:
            return True, None
        # Si FFmpeg no está disponible se hace por tags, avisando del límite.
    shutil.copy2(src, dst)
    try:
        import mutagen
        from mutagen.flac import FLAC
        obj = mutagen.File(dst)
        if obj is not None:
            if isinstance(obj, FLAC):
                obj.delete()
                obj.clear_pictures()
                obj.metadata_blocks = [b for b in obj.metadata_blocks
                                       if b.code not in (2, 6)]   # APPLICATION, PICTURE
                obj.save(deleteid3=True)
            else:
                if obj.tags is not None:
                    obj.delete()
                    obj.save()
        try:
            from mutagen.apev2 import delete as _ape_delete
            _ape_delete(dst)
        except Exception:
            pass
    except Exception as e:
        raise RuntimeError(f"No se pudieron borrar los tags: {e}")
    return True, None


# ------------------------------------------------------------------------------
#   7. PDF (PyMuPDF): Info + XMP
# ------------------------------------------------------------------------------

_PDF_CATALOG = [
    ("title",        "Título",              "Información", False),
    ("author",       "Autor",               "Autoría",     True),
    ("subject",      "Asunto",              "Información", False),
    ("keywords",     "Palabras clave",      "Información", False),
    ("creator",      "Creado con",          "Software",    True),
    ("producer",     "Productor",           "Software",    True),
    ("creationDate", "Fecha de creación",   "Fechas",      True),
    ("modDate",      "Fecha de modificación", "Fechas",    True),
]


def _mlab_fitz():
    import pymupdf as _f
    return _f


def _pdf_open(path):
    f = _mlab_fitz()
    doc = f.open(path)
    if doc.needs_pass:
        doc.close()
        raise ValueError("El PDF está protegido con contraseña.")
    return doc


def _pdf_read_fields(path):
    fields = []
    doc = _pdf_open(path)
    try:
        meta = doc.metadata or {}
        for key, label, group, sens in _PDF_CATALOG:
            val = _mlab_dec(meta.get(key))
            if val:
                ftype = "date" if key.endswith("Date") else "text"
                fields.append(mlab_field(f"pdf:{key}", label, val, ftype, group, sens))
        try:
            xml = doc.get_xml_metadata()
            if xml and xml.strip():
                fields.append(mlab_field("pdf:xmp", "Bloque XMP",
                                         f"{len(xml)} caracteres", "readonly",
                                         "Información", True))
        except Exception:
            pass
    finally:
        doc.close()
    return fields


def _pdf_write_fields(path, values):
    doc = _pdf_open(path)
    tmp = None
    try:
        meta = dict(doc.metadata or {})
        for key, val in values.items():
            if key.startswith("pdf:"):
                name = key.split(":", 1)[1]
                if name in [c[0] for c in _PDF_CATALOG]:
                    meta[name] = str(val or "")
        doc.set_metadata(meta)
        try:
            doc.save(path, incremental=True, encryption=0)   # PDF_ENCRYPT_KEEP
            doc.close()
            return path
        except Exception:
            pass
        tmp = _mlab_tmp_for(path)
        doc.save(tmp, garbage=1, deflate=True)
        doc.close()
        _mlab_commit(tmp, path)
        tmp = None
    finally:
        _mlab_discard(tmp)
    return path


def _pdf_sanitize(src, dst):
    doc = _pdf_open(src)
    tmp = _mlab_tmp_for(dst)
    try:
        doc.set_metadata({})
        try:
            doc.del_xml_metadata()
        except Exception:
            pass
        # Metadata XMP a nivel de página (poco común pero existe)
        try:
            for page in doc:
                xref = page.xref
                if xref:
                    doc.xref_set_key(xref, "Metadata", "null")
        except Exception:
            pass
        doc.save(tmp, garbage=4, clean=True, deflate=True)
        doc.close()
        _mlab_commit(tmp, dst)
        tmp = None
    finally:
        _mlab_discard(tmp)
    return True, None


# ------------------------------------------------------------------------------
#   8. OFFICE (OOXML): manipulación directa del ZIP
#      No se usa openpyxl / python-docx / python-pptx: esas librerías reescriben
#      el documento completo y pueden perder gráficos, macros o formato.
# ------------------------------------------------------------------------------

_NS_CP = "http://schemas.openxmlformats.org/package/2006/metadata/core-properties"
_NS_DC = "http://purl.org/dc/elements/1.1/"
_NS_DCTERMS = "http://purl.org/dc/terms/"
_NS_DCMITYPE = "http://purl.org/dc/dcmitype/"
_NS_XSI = "http://www.w3.org/2001/XMLSchema-instance"
_NS_EXT = "http://schemas.openxmlformats.org/officeDocument/2006/extended-properties"
_NS_CT = "http://schemas.openxmlformats.org/package/2006/content-types"
_NS_REL = "http://schemas.openxmlformats.org/package/2006/relationships"

_OOXML_CATALOG = [
    ("title",          f"{{{_NS_DC}}}title",            "Título",              "Información", False),
    ("subject",        f"{{{_NS_DC}}}subject",          "Asunto",              "Información", False),
    ("creator",        f"{{{_NS_DC}}}creator",          "Autor",               "Autoría",     True),
    ("description",    f"{{{_NS_DC}}}description",      "Descripción",         "Información", False),
    ("keywords",       f"{{{_NS_CP}}}keywords",         "Palabras clave",      "Información", False),
    ("lastModifiedBy", f"{{{_NS_CP}}}lastModifiedBy",   "Última modificación por", "Autoría", True),
    ("category",       f"{{{_NS_CP}}}category",         "Categoría",           "Información", False),
    ("contentStatus",  f"{{{_NS_CP}}}contentStatus",    "Estado",              "Información", False),
    ("revision",       f"{{{_NS_CP}}}revision",         "Revisión",            "Información", False),
    ("created",        f"{{{_NS_DCTERMS}}}created",     "Fecha de creación",   "Fechas",      True),
    ("modified",       f"{{{_NS_DCTERMS}}}modified",    "Fecha de modificación", "Fechas",    True),
]

_OOXML_CORE = "docProps/core.xml"
_OOXML_APP = "docProps/app.xml"
_OOXML_CUSTOM = "docProps/custom.xml"

_OOXML_EMPTY_CORE = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\r\n'
    '<cp:coreProperties xmlns:cp="%s" xmlns:dc="%s" xmlns:dcterms="%s" '
    'xmlns:dcmitype="%s" xmlns:xsi="%s"/>' % (_NS_CP, _NS_DC, _NS_DCTERMS, _NS_DCMITYPE, _NS_XSI)
).encode("utf-8")


def _ooxml_register_ns():
    for pfx, uri in (("cp", _NS_CP), ("dc", _NS_DC), ("dcterms", _NS_DCTERMS),
                     ("dcmitype", _NS_DCMITYPE), ("xsi", _NS_XSI)):
        try:
            _mlab_ET.register_namespace(pfx, uri)
        except Exception:
            pass


def _ooxml_rewrite(src, dst, replace=None, drop=None):
    """Copia el ZIP entrada por entrada respetando orden y compresión."""
    replace = replace or {}
    drop = drop or set()
    tmp = _mlab_tmp_for(dst)
    try:
        with _mlab_zipfile.ZipFile(src, "r") as zin:
            bad = zin.testzip()
            if bad:
                raise ValueError(f"El documento tiene una entrada corrupta: {bad}")
            with _mlab_zipfile.ZipFile(tmp, "w", _mlab_zipfile.ZIP_DEFLATED) as zout:
                for item in zin.infolist():
                    if item.filename in drop:
                        continue
                    data = replace.get(item.filename)
                    if data is None:
                        data = zin.read(item.filename)
                    info = _mlab_zipfile.ZipInfo(item.filename, date_time=item.date_time)
                    info.compress_type = item.compress_type
                    info.external_attr = item.external_attr
                    info.internal_attr = item.internal_attr
                    info.create_system = item.create_system
                    zout.writestr(info, data)
        _mlab_commit(tmp, dst)
        tmp = None
    finally:
        _mlab_discard(tmp)
    return True, None


def _ooxml_read_core(path):
    with _mlab_zipfile.ZipFile(path, "r") as z:
        if _OOXML_CORE not in z.namelist():
            return {}
        root = _mlab_ET.fromstring(z.read(_OOXML_CORE))
    out = {}
    for key, tag, _lbl, _grp, _sens in _OOXML_CATALOG:
        el = root.find(tag)
        if el is not None and (el.text or "").strip():
            out[key] = el.text.strip()
    return out


def _ooxml_read_fields(path):
    fields = []
    data = _ooxml_read_core(path)
    for key, tag, label, group, sens in _OOXML_CATALOG:
        if data.get(key):
            ftype = "date" if key in ("created", "modified") else "text"
            fields.append(mlab_field(f"ooxml:{key}", label, data[key], ftype, group, sens))
    try:
        with _mlab_zipfile.ZipFile(path, "r") as z:
            names = z.namelist()
            if _OOXML_APP in names:
                root = _mlab_ET.fromstring(z.read(_OOXML_APP))
                for tag, label, sens in (("Application", "Aplicación", True),
                                         ("Company", "Empresa", True),
                                         ("Manager", "Responsable", True),
                                         ("Template", "Plantilla", False)):
                    el = root.find(f"{{{_NS_EXT}}}{tag}")
                    if el is not None and (el.text or "").strip():
                        fields.append(mlab_field(f"app:{tag}", label, el.text.strip(),
                                                 "readonly", "Software", sens))
            if _OOXML_CUSTOM in names:
                fields.append(mlab_field("ooxml:custom", "Propiedades personalizadas",
                                         "Presentes", "readonly", "Información", True))
            thumbs = [n for n in names if n.startswith("docProps/thumbnail")]
            if thumbs:
                fields.append(mlab_field("ooxml:thumb", "Miniatura incrustada",
                                         "Presente", "readonly", "Información", True))
    except Exception:
        pass
    return fields


def _ooxml_write_fields(path, values):
    _ooxml_register_ns()
    with _mlab_zipfile.ZipFile(path, "r") as z:
        if _OOXML_CORE in z.namelist():
            root = _mlab_ET.fromstring(z.read(_OOXML_CORE))
        else:
            root = _mlab_ET.fromstring(_OOXML_EMPTY_CORE)
    tagmap = {f"ooxml:{c[0]}": c[1] for c in _OOXML_CATALOG}
    for key, val in values.items():
        tag = tagmap.get(key)
        if not tag:
            continue
        el = root.find(tag)
        val = str(val or "").strip()
        if val:
            if el is None:
                el = _mlab_ET.SubElement(root, tag)
                if tag.endswith("}created") or tag.endswith("}modified"):
                    el.set(f"{{{_NS_XSI}}}type", "dcterms:W3CDTF")
            el.text = val
        elif el is not None:
            root.remove(el)
    body = (b'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\r\n' +
            _mlab_ET.tostring(root, encoding="utf-8"))
    _ooxml_rewrite(path, path, replace={_OOXML_CORE: body})
    return path


def _ooxml_blank_app(data):
    try:
        root = _mlab_ET.fromstring(data)
        for tag in ("Application", "AppVersion", "Company", "Manager",
                    "Template", "HyperlinkBase"):
            el = root.find(f"{{{_NS_EXT}}}{tag}")
            if el is not None:
                el.text = ""
        _mlab_ET.register_namespace("", _NS_EXT)
        return (b'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\r\n' +
                _mlab_ET.tostring(root, encoding="utf-8"))
    except Exception:
        return data


def _ooxml_drop_refs(data, targets, kind):
    """Quita Overrides de [Content_Types].xml o Relationships de .rels."""
    try:
        root = _mlab_ET.fromstring(data)
        if kind == "ct":
            _mlab_ET.register_namespace("", _NS_CT)
            for el in list(root):
                part = (el.get("PartName") or "").lstrip("/")
                if part in targets:
                    root.remove(el)
        else:
            _mlab_ET.register_namespace("", _NS_REL)
            for el in list(root):
                tgt = (el.get("Target") or "").lstrip("/")
                if tgt in targets or ("docProps/" + tgt) in targets:
                    root.remove(el)
        return (b'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\r\n' +
                _mlab_ET.tostring(root, encoding="utf-8"))
    except Exception:
        return data


def _ooxml_sanitize(src, dst):
    """Vacía core.xml y app.xml, elimina custom.xml y la miniatura.
    Texto, tablas, fórmulas, hojas, diapositivas, imágenes, estilos, macros y
    comentarios se copian sin tocar."""
    with _mlab_zipfile.ZipFile(src, "r") as z:
        names = z.namelist()
        app_data = z.read(_OOXML_APP) if _OOXML_APP in names else None
        ct_data = z.read("[Content_Types].xml") if "[Content_Types].xml" in names else None
        rels_data = z.read("_rels/.rels") if "_rels/.rels" in names else None

    drop = set()
    if _OOXML_CUSTOM in names:
        drop.add(_OOXML_CUSTOM)
    for n in names:
        if n.startswith("docProps/thumbnail"):
            drop.add(n)

    replace = {_OOXML_CORE: _OOXML_EMPTY_CORE} if _OOXML_CORE in names else {}
    if app_data is not None:
        replace[_OOXML_APP] = _ooxml_blank_app(app_data)
    if drop:
        if ct_data is not None:
            replace["[Content_Types].xml"] = _ooxml_drop_refs(ct_data, drop, "ct")
        if rels_data is not None:
            replace["_rels/.rels"] = _ooxml_drop_refs(rels_data, drop, "rels")
    return _ooxml_rewrite(src, dst, replace=replace, drop=drop)

# ------------------------------------------------------------------------------
#   9. VIDEO (FFmpeg, siempre con stream copy: nunca se recodifica)
# ------------------------------------------------------------------------------

_VIDEO_CATALOG = [
    ("title",         "Título",             "Información", False),
    ("artist",        "Artista / Autor",    "Autoría",     True),
    ("album",         "Álbum",              "Información", False),
    ("genre",         "Género",             "Información", False),
    ("date",          "Fecha",              "Fechas",      True),
    ("comment",       "Comentario",         "Información", False),
    ("description",   "Descripción",        "Información", False),
    ("copyright",     "Copyright",          "Autoría",     False),
    ("creation_time", "Fecha de creación",  "Fechas",      True),
]
# Tags que escribe el propio muxer y no identifican a nadie: no se reportan
# como metadata pendiente (major_brand, handler genérico, duración de pista...).
_VIDEO_BENIGN_STREAM = {"language", "handler_name", "vendor_id", "duration",
                        "encoder", "_statistics_tags", "_statistics_writing_app"}
_VIDEO_BENIGN_FORMAT = {"major_brand", "minor_version", "compatible_brands"}


def _video_tag_benigno(key, val):
    k = (key or "").lower()
    if k in _VIDEO_BENIGN_STREAM or k in _VIDEO_BENIGN_FORMAT:
        if k == "encoder":
            return bool(re.match(r"^lavf[\d.]*$", str(val or "").strip().lower()))
        return True
    return False


_VIDEO_READONLY = [
    ("encoder",       "Codificado con",     "Software",    True),
    ("location",      "Ubicación GPS",      "Ubicación",   True),
    ("com.apple.quicktime.location.ISO6709", "Ubicación GPS (Apple)", "Ubicación", True),
    ("com.apple.quicktime.make", "Marca del equipo", "Dispositivo", True),
    ("com.apple.quicktime.model", "Modelo del equipo", "Dispositivo", True),
    ("com.apple.quicktime.software", "Software del equipo", "Software", True),
]


def _ffmpeg_exe():
    exe = shutil.which("ffmpeg")
    if not exe:
        raise RuntimeError("FFmpeg no está disponible (no se encontró en el PATH).")
    return exe


def _video_read_fields(path):
    fields = []
    data = _mlab_ffprobe(path)
    if not data:
        return fields
    tags = {k.lower(): v for k, v in (data.get("format", {}).get("tags", {}) or {}).items()}
    for key, label, group, sens in _VIDEO_CATALOG:
        val = _mlab_dec(tags.get(key))
        if val:
            fields.append(mlab_field(f"video:{key}", label, val, "text", group, sens))
    for key, label, group, sens in _VIDEO_READONLY:
        val = _mlab_dec(tags.get(key.lower()))
        if val and not _video_tag_benigno(key, val):
            fields.append(mlab_field(f"videoro:{key}", label, val, "readonly", group, sens))
    # Metadata a nivel de stream (handler_name, title de pistas, etc.)
    extra = 0
    for s in data.get("streams", []):
        for k, v in (s.get("tags", {}) or {}).items():
            if _video_tag_benigno(k, v):
                continue
            if _mlab_dec(v):
                extra += 1
    if extra:
        fields.append(mlab_field("videoro:streams", "Metadata en pistas",
                                 f"{extra} campo(s)", "readonly", "Información", False))
    return fields


def _video_sanitize(src, dst, audio_only=False):
    exe = _ffmpeg_exe()
    sig = _mlab_media_signature(src)
    nstreams = sig["n"] if sig else 0
    mapa = ["-map", "0:a"] if audio_only else ["-map", "0"]
    if audio_only:
        nstreams = 1
    base = [exe, "-y", "-hide_banner", "-loglevel", "error", "-i", src] + mapa + [
            "-c", "copy", "-map_metadata", "-1", "-map_chapters", "-1"]
    for i in range(nstreams):
        base += [f"-map_metadata:s:{i}", "-1", f"-metadata:s:{i}", "handler_name="]
    intentos = [base + ["-fflags", "+bitexact", dst], base + [dst]]
    last_err = ""
    for cmd in intentos:
        try:
            rc, _out, err = _mlab_run(cmd, timeout=1800)
        except subprocess.TimeoutExpired:
            _mlab_discard(dst)
            return False, "FFmpeg superó el tiempo máximo de proceso."
        if rc == 0 and os.path.exists(dst) and os.path.getsize(dst) > 0:
            return True, None
        last_err = "\n".join((err or "").splitlines()[-8:])
        _mlab_discard(dst)
    return False, f"FFmpeg no pudo remuxear sin recodificar.\n{last_err}"


def _video_write_fields(path, values):
    """La edición de video NO sobrescribe el original: genera *_editado."""
    exe = _ffmpeg_exe()
    dst = mlab_target_path(path, "_editado")
    cmd = [exe, "-y", "-hide_banner", "-loglevel", "error", "-i", path,
           "-map", "0", "-c", "copy", "-map_metadata", "0"]
    for key, val in values.items():
        if not key.startswith("video:"):
            continue
        name = key.split(":", 1)[1]
        cmd += ["-metadata", f"{name}={str(val or '')}"]
    cmd.append(dst)
    rc, _out, err = _mlab_run(cmd, timeout=1800)
    if rc != 0 or not os.path.exists(dst) or os.path.getsize(dst) == 0:
        _mlab_discard(dst)
        raise RuntimeError("FFmpeg no pudo escribir la metadata.\n" +
                           "\n".join((err or "").splitlines()[-8:]))
    ok, detail = _mlab_verify_content(path, dst, "video")
    if not ok:
        _mlab_discard(dst)
        raise RuntimeError(f"El archivo generado no superó la verificación: {detail}")
    return dst


# ------------------------------------------------------------------------------
#   10. RAW / HEIF — solo lectura (analizar)
# ------------------------------------------------------------------------------

_TIFF_TYPE_SIZE = {1: 1, 2: 1, 3: 2, 4: 4, 5: 8, 6: 1, 7: 1, 8: 2, 9: 4, 10: 8, 11: 4, 12: 8}
_RAW_TAGS = {
    271: ("Marca del equipo", "Dispositivo", True),
    272: ("Modelo del equipo", "Dispositivo", True),
    305: ("Software", "Software", True),
    306: ("Fecha", "Fechas", True),
    315: ("Autor / Artista", "Autoría", True),
    33432: ("Copyright", "Autoría", False),
    36867: ("Fecha de captura", "Fechas", True),
    42033: ("Nº de serie", "Dispositivo", True),
    42036: ("Objetivo", "Dispositivo", False),
}


def _raw_read_fields(path):
    """Parser mínimo de IFD TIFF. Solo lectura, sin tocar el archivo."""
    fields = []
    try:
        with open(path, "rb") as fh:
            data = fh.read(4 * 1024 * 1024)
        if data[:2] == b"II":
            end = "<"
        elif data[:2] == b"MM":
            end = ">"
        else:
            return fields
        off = _mlab_struct.unpack(end + "I", data[4:8])[0]
        seen = set()
        pending = [off]
        found = {}
        while pending:
            pos = pending.pop(0)
            if pos in seen or pos <= 0 or pos + 2 > len(data):
                continue
            seen.add(pos)
            count = _mlab_struct.unpack(end + "H", data[pos:pos + 2])[0]
            if count > 512:
                continue
            for i in range(count):
                e = pos + 2 + i * 12
                if e + 12 > len(data):
                    break
                tag, ttype, cnt = _mlab_struct.unpack(end + "HHI", data[e:e + 8])
                raw = data[e + 8:e + 12]
                size = _TIFF_TYPE_SIZE.get(ttype, 0) * cnt
                if tag in (34665, 34853) and ttype == 4:
                    pending.append(_mlab_struct.unpack(end + "I", raw)[0])
                    if tag == 34853:
                        found["__gps__"] = True
                    continue
                if tag not in _RAW_TAGS or ttype != 2:
                    continue
                if size > 4:
                    voff = _mlab_struct.unpack(end + "I", raw)[0]
                    val = data[voff:voff + size]
                else:
                    val = raw[:size]
                txt = _mlab_dec(val)
                if txt and tag not in found:
                    found[tag] = txt
        for tag, txt in found.items():
            if tag == "__gps__":
                fields.append(mlab_field("raw:GPS", "Ubicación GPS", "Presente (IFD GPS)",
                                         "readonly", "Ubicación", True))
                continue
            label, group, sens = _RAW_TAGS[tag]
            fields.append(mlab_field(f"raw:{tag}", label, txt, "readonly", group, sens))
    except Exception:
        pass
    return fields


def _heif_read_fields(path):
    """Busca el bloque Exif dentro del contenedor ISOBMFF (HEIC/CR3)."""
    fields = []
    try:
        with open(path, "rb") as fh:
            data = fh.read(8 * 1024 * 1024)
        idx = data.find(b"Exif\x00\x00")
        if idx < 0:
            return fields
        blob = data[idx:idx + 262144]
        fields = _exif_read_from_bytes(blob[6:])
        for f in fields:
            f["type"] = "readonly"
    except Exception:
        pass
    return fields


# ------------------------------------------------------------------------------
#   11. DESPACHADORES — lectura / escritura / sanitización / verificación
# ------------------------------------------------------------------------------

_READERS = {
    "jpeg": _exif_read_fields,
    "png": _png_read_fields,
    "webp": _webp_read_fields,
    "tiff": _tiff_read_fields,
    "audio": _audio_read_fields,
    "video": _video_read_fields,
    "pdf": _pdf_read_fields,
    "ooxml": _ooxml_read_fields,
    "raw": _raw_read_fields,
    "heif": _heif_read_fields,
}


def mlab_read(path):
    """Lee la metadata relevante. Devuelve solo campos CON datos."""
    caps = mlab_caps(path)
    res = {"ok": False, "caps": caps, "fields": [], "error": None}
    if not os.path.isfile(path):
        res["error"] = "El archivo ya no existe."
        return res
    if not caps["kind"]:
        res["error"] = f"El formato {caps['ext']} no está soportado."
        return res
    reader = _READERS.get(caps["kind"])
    try:
        res["fields"] = reader(path) or []
        res["ok"] = True
    except Exception as e:
        res["error"] = str(e)
    return res


def mlab_addable_fields(path):
    """Campos que el usuario puede AÑADIR a mano (los que aún no tienen datos)."""
    caps = mlab_caps(path)
    if not caps["edit"]:
        return []
    existing = {f["key"] for f in mlab_read(path).get("fields", [])}
    out = []
    kind = caps["kind"]
    if kind == "jpeg":
        for key, label, ifd, tag, ftype, group, sens in _jpeg_exif_catalog():
            out.append((key, label, ftype, group, sens))
        out.append(("exif:GPS", "Ubicación GPS", "gps", "Ubicación", True))
    elif kind == "png":
        for key, label, _pk, sens in _PNG_TEXT_KEYS:
            out.append((key, label, "text", "Información", sens))
    elif kind == "tiff":
        for key, label, _tag, group, sens in _TIFF_CATALOG:
            out.append((key, label, "text", group, sens))
    elif kind == "audio":
        for key, label, group, sens in _AUDIO_CATALOG:
            out.append((f"audio:{key}", label, "text", group, sens))
    elif kind == "video":
        for key, label, group, sens in _VIDEO_CATALOG:
            out.append((f"video:{key}", label, "text", group, sens))
    elif kind == "pdf":
        for key, label, group, sens in _PDF_CATALOG:
            out.append((f"pdf:{key}", label, "text", group, sens))
    elif kind == "ooxml":
        for key, _tag, label, group, sens in _OOXML_CATALOG:
            out.append((f"ooxml:{key}", label, "text", group, sens))
    return [o for o in out if o[0] not in existing]


def mlab_write(path, values):
    """Escribe los campos editados.
    Devuelve (ok, error, ruta_resultante). En video la ruta es *_editado."""
    caps = mlab_caps(path)
    if not caps["edit"]:
        return False, "Este formato no permite edición manual.", None
    writers = {
        "jpeg": _exif_write_fields,
        "png": _png_write_fields,
        "tiff": _tiff_write_fields,
        "audio": _audio_write_fields,
        "video": _video_write_fields,
        "pdf": _pdf_write_fields,
        "ooxml": _ooxml_write_fields,
    }
    fn = writers.get(caps["kind"])
    if not fn:
        return False, "Este formato no permite edición manual.", None
    try:
        out = fn(path, values)
        return True, None, out or path
    except Exception as e:
        return False, str(e), None


_SANITIZERS = {
    "jpeg": _jpeg_sanitize,
    "png": lambda s, d: _png_rewrite(s, d, strip_all=True),
    "webp": _webp_sanitize,
    "tiff": lambda s, d: _tiff_save(s, d, strip=True),
    "audio": _audio_sanitize,
    "video": _video_sanitize,
    "pdf": _pdf_sanitize,
    "ooxml": _ooxml_sanitize,
}


def _mlab_verify_content(src, dst, kind):
    """Comprueba que el contenido real sobrevivió intacto."""
    try:
        if not os.path.isfile(dst):
            return False, "no se generó el archivo"
        if os.path.getsize(dst) == 0:
            return False, "el archivo resultante está vacío"

        if kind in ("jpeg", "png", "webp", "tiff"):
            from PIL import Image as _I
            with _I.open(src) as a, _I.open(dst) as b:
                if a.size != b.size:
                    return False, f"cambiaron las dimensiones ({a.size} -> {b.size})"
                if a.mode != b.mode:
                    return False, f"cambió el modo de color ({a.mode} -> {b.mode})"
                b.load()
            return True, "imagen válida, dimensiones y modo intactos"

        if kind in ("audio", "video"):
            sa, sb = _mlab_media_signature(src), _mlab_media_signature(dst)
            if sa and sb:
                # Las carátulas incrustadas son metadata: que desaparezcan es
                # el resultado correcto, no una pérdida de contenido.
                key = "media" if kind == "audio" else "streams"
                na, nb = len(sa[key]), len(sb[key])
                if na != nb:
                    return False, f"cambió el número de pistas ({na} -> {nb})"
                if sa["duration"] and abs(sa["duration"] - sb["duration"]) > 1.0:
                    return False, (f"cambió la duración "
                                   f"({sa['duration']:.2f}s -> {sb['duration']:.2f}s)")
                if [s[1] for s in sa[key]] != [s[1] for s in sb[key]]:
                    return False, "cambiaron los códecs"
                return True, f"{nb} pista(s), duración y códecs intactos"
            import mutagen
            f = mutagen.File(dst)
            if f is None:
                return False, "el archivo resultante no se puede abrir"
            return True, "archivo válido"

        if kind == "pdf":
            f = _mlab_fitz()
            a, b = f.open(src), f.open(dst)
            try:
                if a.page_count != b.page_count:
                    return False, f"cambió el nº de páginas ({a.page_count} -> {b.page_count})"
                n = b.page_count
            finally:
                a.close()
                b.close()
            return True, f"{n} página(s) intactas"

        if kind == "ooxml":
            with _mlab_zipfile.ZipFile(src) as za, _mlab_zipfile.ZipFile(dst) as zb:
                bad = zb.testzip()
                if bad:
                    return False, f"entrada dañada: {bad}"
                a = {n for n in za.namelist() if not n.startswith("docProps/")}
                b = {n for n in zb.namelist() if not n.startswith("docProps/")}
                if a - b:
                    return False, f"faltan partes del documento: {sorted(a - b)[:3]}"
                n = len(b)
            return True, f"{n} partes del documento intactas"
    except Exception as e:
        return False, f"no se pudo verificar: {e}"
    return True, "archivo generado"


def mlab_residual(path):
    """Metadata que sigue presente tras sanitizar (debería ser ninguna)."""
    try:
        res = mlab_read(path)
        return [f["label"] for f in res.get("fields", [])]
    except Exception:
        return []


def mlab_sanitize(path, dst=None):
    """Crea la copia *_CLEAN, verifica el resultado y reporta.
    Devuelve dict(ok, dst, error, verify, residual, recoded)."""
    out = {"ok": False, "dst": None, "error": None, "verify": "", "residual": []}
    caps = mlab_caps(path)
    if not os.path.isfile(path):
        out["error"] = "El archivo ya no existe."
        return out
    if not caps["clean"]:
        out["error"] = (f"{caps['label']}: sanitización no disponible para este formato "
                        "(solo analizar).")
        return out
    if caps["kind"] == "tiff" and _tiff_is_lossy(path):
        out["error"] = ("TIFF con compresión JPEG interna: solo se permite analizar "
                        "(sanitizarlo obligaría a recomprimir).")
        return out

    dst = dst or mlab_target_path(path, "_CLEAN")
    fn = _SANITIZERS.get(caps["kind"])
    try:
        ok, err = fn(path, dst)
        if not ok:
            out["error"] = err or "Error desconocido."
            _mlab_discard(dst)
            return out
    except Exception as e:
        _mlab_discard(dst)
        out["error"] = str(e)
        return out

    ok, detail = _mlab_verify_content(path, dst, caps["kind"])
    out["verify"] = detail
    if not ok:
        _mlab_discard(dst)
        out["error"] = f"Verificación fallida: {detail}"
        return out

    out["residual"] = mlab_residual(dst)
    out["ok"] = True
    out["dst"] = dst
    return out


def mlab_analyze(path):
    """Informe de solo lectura. No modifica el archivo."""
    caps = mlab_caps(path)
    rep = {"name": os.path.basename(path), "label": caps["label"], "caps": caps,
           "size_mb": 0.0, "fields": [], "sensitive": [], "error": None}
    try:
        rep["size_mb"] = round(os.path.getsize(path) / (1024 * 1024), 2)
    except Exception:
        pass
    res = mlab_read(path)
    if res.get("error"):
        rep["error"] = res["error"]
    rep["fields"] = res.get("fields", [])
    rep["sensitive"] = [f for f in rep["fields"] if f["sensitive"]]
    return rep


# ==============================================================================
#   VENTANAS SECUNDARIAS SIN PARPADEO
# ------------------------------------------------------------------------------
#   En Windows, CustomTkinter oculta y vuelve a mostrar cada CTkToplevel para
#   pintar la barra de título oscura: una vez al crearla y otra 10 ms después
#   de cada resizable(). Si eso pasa con la ventana ya visible se ve el
#   parpadeo, el fondo blanco a medio dibujar y, a veces, la ventana queda
#   detrás de la principal (pasaba igual con CTk 5.2.x).
#   VentanaSecundaria nace oculta y transparente, se rellena, espera a que CTk
#   termine esos ciclos y recién entonces aparece de golpe, ya dibujada.
# ==============================================================================
class VentanaSecundaria(ctk.CTkToplevel):

    def __init__(self, *args, **kwargs):
        self._dmt_ciclos = 0            # ciclos oculta/muestra de CTk en curso
        self._dmt_resizable_pend = 0    # ciclos programados por resizable() sin empezar
        super().__init__(*args, **kwargs)
        self.withdraw()                 # CTk la deja oculta al terminar su primer ciclo
        try:
            self.attributes("-alpha", 0.0)
        except Exception:
            pass

    # --- seguimiento de los ciclos de la barra de título de CustomTkinter ---
    def _windows_set_titlebar_color(self, color_mode):
        if self._dmt_resizable_pend > 0:
            self._dmt_resizable_pend -= 1
        self._dmt_ciclos += 1
        try:
            super()._windows_set_titlebar_color(color_mode)
        finally:
            # Si CTk no programó su "revert" (no es Windows, modo raro...) no hay ciclo abierto
            if not getattr(self, "_windows_set_titlebar_color_called", False):
                self._dmt_ciclos = max(0, self._dmt_ciclos - 1)

    def _revert_withdraw_after_windows_set_titlebar_color(self):
        try:
            super()._revert_withdraw_after_windows_set_titlebar_color()
        finally:
            self._dmt_ciclos = max(0, self._dmt_ciclos - 1)

    def resizable(self, width=None, height=None):
        if sys.platform.startswith("win") and not getattr(self, "_deactivate_windows_window_header_manipulation", False):
            self._dmt_resizable_pend += 1
        return super().resizable(width, height)

    def _dmt_ocupada(self):
        return (self._dmt_ciclos > 0 or self._dmt_resizable_pend > 0
                or bool(getattr(self, "_windows_set_titlebar_color_called", False)))

    # --- mostrar / ocultar ---
    def dmt_mostrar(self, app, _intentos=0):
        """Muestra la ventana ya dibujada. `app` programa los after() (nunca se destruye)."""
        try:
            if not self.winfo_exists():
                return
        except Exception:
            return
        if self._dmt_ocupada() and _intentos < 80:
            app.after(15, lambda: self.dmt_mostrar(app, _intentos + 1))
            return
        try:
            self.attributes("-alpha", 0.0)
        except Exception:
            pass
        try:
            self.deiconify()
            self.lift()
        except Exception:
            return

        def _revelar():
            try:
                if not self.winfo_exists():
                    return
                self.attributes("-alpha", 1.0)
                self.lift()
                self.focus_force()
            except Exception:
                pass
        # Margen para que los widgets CTk terminen de dibujarse con alpha 0
        app.after(45, _revelar)

    def dmt_ocultar(self):
        try:
            self.withdraw()
        except Exception:
            pass

    def dmt_visible(self):
        try:
            return bool(self.winfo_exists()) and self.state() != "withdrawn"
        except Exception:
            return False


class App(ctk.CTk, TkinterDnD.DnDWrapper):

    # --------------------------------------------------------------------------
    # SISTEMA DE CONFIGURACIÓN PERSISTENTE (JSON en APPDATA)
    # --------------------------------------------------------------------------
    def get_config_path(self):
        """Genera la ruta segura en AppData/Local para guardar configs"""
        # C:\Users\Usuario\AppData\Local\DeusMachinaTools
        app_data = os.getenv('LOCALAPPDATA')
        config_dir = os.path.join(app_data, "DeusMachinaTools")
        
        if not os.path.exists(config_dir):
            try:
                os.makedirs(config_dir)
            except OSError:
                # Fallback por si falla (ej. permisos raros), usar carpeta temporal
                config_dir = os.path.join(_DMT_TEMP_BASE_SISTEMA, "DeusMachinaTools")
                os.makedirs(config_dir, exist_ok=True)
                
        return os.path.join(config_dir, "config.json")

    _config_lock = threading.RLock()

    def _config_leer(self):
        """Lee config.json completo (dict vacío si no existe o está dañado)."""
        try:
            with open(self.get_config_path(), 'r', encoding='utf-8') as f:
                data = json.load(f)
            return data if isinstance(data, dict) else {}
        except Exception:
            return {}

    def _config_guardar(self, **cambios):
        """
        Actualiza SOLO las claves indicadas y conserva el resto (antes, guardar
        el tema reescribía todo el archivo y borraba cualquier otro ajuste).
        """
        config_path = self.get_config_path()
        with self._config_lock:
            data = self._config_leer()
            data.update(cambios)
            tmp = config_path + ".tmp"
            try:
                with open(tmp, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                os.replace(tmp, config_path)
                return True
            except Exception as e:
                print(f"Error guardando config: {e}")
                return False

    def save_theme_preference(self, theme_name):
        """Guarda el tema seleccionado en un JSON"""
        if self._config_guardar(theme=theme_name):
            print(f"DEBUG: Tema guardado en {self.get_config_path()}")

    def load_theme_preference(self):
        """Carga el tema guardado, retorna None si no existe"""
        return self._config_leer().get("theme", None)




    def __init__(self):
        super().__init__()

        # Cola de cambios de interfaz pedidos desde hilos secundarios (Tkinter
        # solo es seguro en su propio hilo): los hilos encolan y el hilo de la
        # interfaz los aplica cada 30 ms. Ver _en_ui / _en_ui_espera.
        self._cola_ui = queue.SimpleQueue()
        self.after(30, self._bombear_cola_ui)
        # Trabajos largos en marcha que no pasan por el lote general (PDF,
        # renombrador...): nombre -> descripción. Se consultan al cerrar la app.
        self._trabajos = {}

        self.current_process = None
        # --- WHISPER STATE ---
        self.faster_model = None
        self.last_whisper_config = None
        self._whisper_lock = threading.Lock()    # protege del/carga desde hilos
        self._whisper_decoders = set()           # procesos ffmpeg que decodifican audio a memoria
        self._live_loop_done = threading.Event() # señal: el bucle live terminó
        self._live_loop_done.set()               # empieza como "terminado"
        self._file_start_time = None             # tiempo total por archivo
        # ---------------------

        # --- AGREGAR ESTO ---
        self.yt_active_temps = []
        self.current_temp_audio = None # Para poder borrarlo si cierras la app
        # --------------------

        self.TkdndVersion = TkinterDnD._require(self)
        # --- [NUEVO] ALMACÉN DE IMÁGENES "ETERNO" ---
        # Aquí guardaremos las imágenes para que el recolector de basura nunca las borre
        self.permanent_image_cache = {} 
        # --------------------------------------------
        # --- CONFIGURACIÓN DE FUENTE GLOBAL ---
        # Asegúrate de tener "JetBrains Mono" instalada en Windows
        self.main_font = "JetBrains Mono" 
        # --------------------------------------
        
        # Configuración Ventana
        self.title("D E U S   M A C H I N A  |  T O O L S")
        self.withdraw()
        self._auto_center_ids = [self.after(100, self.center_window)]

        self.current_bg = "#2b2b2b"  # Color Obsidian por defecto
        # --- NUEVO: CARGA PERSISTENTE DEL LOGO ---
        # Cargamos la imagen aquí para que viva por siempre en la RAM
        self.logo_image_ref = None 
        
        # --- RUTAS DE RECURSOS (IMGTYPE) ---
        self.assets_folder = resource_path("imgtype")
        print(f"DEBUG: Carpeta assets -> {self.assets_folder}")

        # Rutas de Iconos
        self.app_icon_path = os.path.join(self.assets_folder, "1.ico")     
        self.app_logo_png_path = os.path.join(self.assets_folder, "logo.png")
        
        # --- CONFIGURACIÓN DE FUENTE GLOBAL ---
        # Intentamos cargar JetBrainsMono desde imgtype
        try:
            font_path = os.path.join(self.assets_folder, "JetBrainsMono-Regular.ttf")
            if os.path.exists(font_path):
                ctk.FontManager.load_font(font_path)
                self.main_font = "JetBrains Mono"
            else:
                self.main_font = "Arial" # Fallback si no está el archivo
        except Exception as e:
            print(f"Error fuente: {e}")
            self.main_font = "Arial"
        # --------------------------------------
        
        # Precarga segura del logo principal (Opcional, para evitar lag)
        self.logo_image_ref = None
        if os.path.exists(self.app_icon_path):
            try:
                # Solo cargamos referencia básica, no la forzamos en caché global visual todavía
                pass 
            except Exception: pass
        # -----------------------------------------
        try:
            import ctypes
            myappid = 'DEUSMACHINA_DOMINATH0R'
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        except: pass

        try:
            self.set_window_icon(self)
        except: pass

        # --- LAYOUT PRINCIPAL ---
        self.grid_rowconfigure(0, weight=0) # Barra Superior
        self.grid_rowconfigure(1, weight=1) # Contenido
        self.grid_columnconfigure(0, weight=1)

        # --- TRABAJOS EN PARALELO ---
        # Un lote por módulo (video, imagen, audio, OCR, transcripción): pueden
        # correr a la vez sin pisarse. Los que cargan modelos de IA pasan además
        # por el carril exclusivo (uno a la vez, los demás esperan turno).
        self._lotes = {}                      # modo -> LoteTrabajo en curso
        self._lote_hilo = threading.local()   # el lote del hilo actual
        self._lote_suelto = LoteTrabajo("suelto")
        self.carril_ia = CarrilIA()

        # Variables Globales
        self.current_process = None
        self.cancel_requested = False
        self.file_queue = []
        self.custom_dest_path = ""
        self.mode = "none" 
        self.previous_dest_selections = {}
        # Ruta "Elegir Otra..." PROPIA de cada barra de destino (antes era una sola
        # para toda la app y se borraba al cambiar de pantalla).
        self.dest_paths = {}
        self._destinos = {}             # barra -> {"carpeta": "X_OUTPUT", "archivos": fn}
        self._salidas_recientes = {}    # barra -> última carpeta donde se guardó algo
        # --- VENTANAS UNICAS (se reutilizan: cerrar = ocultar) ---
        self.toplevel_about = None
        self.toplevel_licenses = None
        self.toplevel_docs = None
        self.toplevel_model_help = None
        self.toplevel_meta_info = None


        # Variables PDF
        self.pdf_merge_list = []
        self.pdf_selected_index = None
        self.pdf_split_file = None

        self.protocol("WM_DELETE_WINDOW", self.on_closing) 
        
        # [MODIFICACION] Fondo de Pantalla (Z-Index 0)
        # Sistema de temas por colores (sin imágenes)
        self.theme_colors = {
            "Cyberpunk City": "#1a1a2e",
            "Black Iron": "#111314",
            "Obsidian Shard": "#2b2b2b",
            "Nebula Space": "#000B2A",
            "Forest Mist": "#011b0b",      # Verde bosque casi negro
            "Neon Rain": "#12072A",   
            "Void Echo": "#0A0F12",
            "Deep Ember": "#120507"
        }
        # Color por defecto (Obsidian Shard)
        self.current_bg = "#2b2b2b"
        self.frames = {}
        
        # >>> INICIALIZADORES SIEMPRE-NECESARIOS <<<
        self.init_top_bar()
        self.init_menu_module()

        # --- Gestor de modelos de IA: uno a la vez + descarga tras 20 min sin uso ---
        self.gestor_ia = GestorModelosIA()
        self.gestor_ia.registrar("whisper", self.descargar_modelo_whisper)
        self.gestor_ia.registrar("rembg", self._rembg_liberar)

        # --- Variables previas necesarias para módulos de Tier-2 ---
        self.ocr_motor = GestorMotorOCR(
            on_estado=lambda *a: self.after(0, lambda a=a: self._ocr_set_motor_lbl(*a)),
            gestor_ia=self.gestor_ia,
        )
        self.gestor_ia.registrar("ocr", self.ocr_motor.descargar)
        self._ocr_gpu_apta = False
        self._ocr_gpu_evaluada = False
        self._ocr_bloqueado = False

        # --- REGISTRO LAZY: cada frame se construye la 1ª vez que se navega a él ---
        self._frame_builders = {
            "VideoConverter":  self.init_video_module,
            "ImageConverter":  self.init_image_module,
            "PDFTools":        self.init_pdf_module,
            "RenamerTool":     self.init_renamer_module,
            "AudioConverter":  self.init_audio_module,
            "OCRTool":         self.init_ocr_module,
            "TranscribeTool":  self.init_transcribe_module,
            "MetadataTool":    self.init_alpha_module,
            "YouTubeTool":     self.init_youtube_module,
        }
        
        # Aplicar tema por defecto al iniciar
        # --- CARGA DE TEMA PERSISTENTE ---
        saved_theme = self.load_theme_preference()
        
        # Verificamos si el tema guardado existe en tu diccionario de colores
        if saved_theme and saved_theme in self.theme_colors:
            # Actualizamos el selector visual de la barra superior
            self.palette_var.set(saved_theme)
            # Aplicamos el tema guardado
            self.change_app_palette(saved_theme)
        else:
            # Si es la primera vez o hubo error, usamos el default
            self.change_app_palette("Cyberpunk City")
        

        # ... dentro de __init__ ...
        
        # --- LIMPIEZA DE BASURA ANTERIOR ---
        # Busca carpetas temporales de descargas interrumpidas (YouTube, playlists y
        # Spotify) en la carpeta de descargas por defecto y en sus subcarpetas.
        # Solo nombres exactos generados por la app y con más de 10 minutos.
        try:
            def_path = os.path.join(os.path.expanduser("~"), "Downloads", "Descargas_YT")
            patron = re.compile(
                r"^(temp_[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
                r"|_tmp_[0-9a-f]{8}_\d+|_sp_tmp_[0-9a-f]{8})$")
            ahora = time.time()
            if os.path.exists(def_path):
                carpetas = [def_path] + [os.path.join(def_path, d) for d in os.listdir(def_path)
                                         if os.path.isdir(os.path.join(def_path, d)) and not patron.match(d)]
                for base_dir in carpetas:
                    for item in os.listdir(base_dir):
                        item_path = os.path.join(base_dir, item)
                        if (os.path.isdir(item_path) and patron.match(item)
                                and ahora - os.path.getmtime(item_path) > 600):
                            try:
                                shutil.rmtree(item_path, ignore_errors=True)
                                print(f"Basura vieja eliminada: {item}")
                            except: pass
        except: pass
        
        

        self.show_frame("Menu")
        # 1. Ocultamos la ventana INMEDIATAMENTE al nacer
        self.withdraw()
        
        # 2. Programamos el centrado para 100ms después (cuando ya esté cargada)
        self._auto_center_ids.append(self.after(100, self.center_window))

        # --- TIER-2: cargar librerías pesadas en background (no bloquea UI) ---
        threading.Thread(target=_cargar_tier2_background, daemon=True).start()

        # --- LAZY FRAMES: pre-construir el resto de frames en background (2s de delay) ---
        self.after(2000, self._prebuild_frames_en_background)
       


    # Borra def _final_center(self): ... entera, ya no la necesitamos.

    def center_window(self, show=True):
        try:
            # 1. Forzamos actualización de geometría interna (sin dibujar)
            self.update_idletasks()
            
            # 2. Definimos tamaño fijo
            width = 950
            height = 750
            
            # 3. Calculamos posición matemática exacta
            screen_width = self.winfo_screenwidth()
            screen_height = self.winfo_screenheight()
            x = int((screen_width / 2) - (width / 2))
            y = int((screen_height / 2) - (height / 2))
            
            x += -127
            y += -145


            # 4. Aplicamos geometría
            self.geometry(f"{width}x{height}+{x}+{y}")
            
            # 5. Solo mostramos si se pide (show=False = solo posicionar, sin aparecer)
            if show:
                self.deiconify()
                self.lift()
                self.attributes("-topmost", True)
                self.after(50, lambda: self.attributes("-topmost", False))
                self.focus_force()
            
        except Exception as e:
            print(f"Error centrando: {e}")
            # Fallback por si algo explota: mostrarla como sea
            if show:
                self.deiconify()

    def show_frame(self, frame_name):
        """Cambia entre pantallas y gestiona el Grid.
        Si el frame no ha sido construido aún lo construye ahora (lazy init)."""
        self.file_queue = [] 
        self.custom_dest_path = ""
        self.mode = "none"
        
        if frame_name != "PDFTools":
            self.pdf_merge_list = []
            self.pdf_split_file = None

        # --- LAZY BUILD: construir el frame la primera vez que se navega ---
        if frame_name not in self.frames:
            builder = getattr(self, '_frame_builders', {}).get(frame_name)
            if builder:
                try:
                    builder()
                except Exception as e:
                    print(f"[LazyBuild] Error construyendo {frame_name}: {e}")

        # Ocultar todos los frames
        for frame in self.frames.values():
            frame.grid_forget()

        # Configurar modo. Al entrar, lo que se ve es exactamente lo que se va a
        # procesar: sin archivos "fantasma" de una visita anterior.
        if frame_name == "VideoConverter":
            self.mode = "video"
            self._video_limpiar_listas()
            self._medir_gpu_video()
        elif frame_name == "ImageConverter":
            self.mode = "image"
            self._imagen_limpiar_listas()
            self._img_tab_cambio()      # si vuelves con la pestaña de fondo abierta
        elif frame_name == "PDFTools":
            self._pdf_sincronizar_listas()
        elif frame_name == "AudioConverter":
            self.mode = "audio"
            self.update_file_list_ui(self.audio_drop_area, self.audio_list_label)
        elif frame_name == "OCRTool":
            self.mode = "ocr"
            self.update_file_list_ui(self.ocr_drop, self.ocr_list_lbl)
            self._ocr_al_entrar()
        elif frame_name == "TranscribeTool":
            self.mode = "transcribe"
            self.update_file_list_ui(self.trans_drop_area, self.trans_list_label)

        # MOSTRAR EL FRAME EN LA FILA 1 (Debajo de la barra superior)
        if frame_name in self.frames:
            self.frames[frame_name].grid(row=1, column=0, sticky="nsew")

    # ==========================================================================
    #   SELECTOR DE IDIOMA (compacto): botón + lista con scroll
    # ==========================================================================
    def _selector_idioma(self, padre, variable, ancho=190):
        """
        Botón pequeño que abre la lista de idiomas en una ventanita con scroll.
        Un desplegable normal con 19 idiomas ocupa casi toda la pantalla; así el
        control ocupa una sola línea y la lista se desplaza dentro de su ventana.
        """
        boton = ctk.CTkButton(padre, textvariable=variable, width=ancho, height=28,
                              fg_color="#444", hover_color="#555", anchor="w",
                              font=("Arial", 12))
        boton.configure(command=lambda: self._abrir_selector_idioma(variable, boton))
        return boton

    def _abrir_selector_idioma(self, variable, boton):
        """Lista de idiomas junto al botón: se elige uno y se cierra sola."""
        win = getattr(self, "_win_idioma", None)
        if win is not None and win.winfo_exists():
            win.destroy()

        ancho, alto = 250, 320
        win = self._win_idioma = self._ventana_nueva("Idioma del audio", ancho, alto)
        win.attributes("-topmost", True)

        ctk.CTkLabel(win, text="Idioma del audio", font=(self.main_font, 13, "bold"),
                     text_color="#dddddd").pack(pady=(10, 6))
        lista = ctk.CTkScrollableFrame(win, fg_color="#1e1e1e", width=ancho - 40, height=alto - 80)
        lista.pack(padx=12, pady=(0, 12), fill="both", expand=True)

        def _elegir(valor):
            variable.set(valor)
            win.destroy()

        actual = variable.get()
        for etiqueta in TRANS_IDIOMAS:
            elegido = etiqueta == actual
            ctk.CTkButton(lista, text=etiqueta, anchor="w", height=28,
                          font=("Arial", 12, "bold" if elegido else "normal"),
                          fg_color="#3a230d" if elegido else "transparent",
                          hover_color="#333333", text_color="#ffffff" if elegido else "#cfcfcf",
                          command=lambda v=etiqueta: _elegir(v)).pack(fill="x", pady=1)

        # Aparece pegada al botón, no en el centro de la pantalla
        try:
            x = boton.winfo_rootx()
            y = boton.winfo_rooty() + boton.winfo_height() + 4
            pantalla_h = self.winfo_screenheight()
            escala = float(win._get_window_scaling())
            if y + alto * escala > pantalla_h:            # no cabe abajo: se abre arriba
                y = max(0, boton.winfo_rooty() - int(alto * escala) - 4)
            win.geometry(f"+{max(0, x)}+{max(0, y)}")
        except Exception:
            pass
        self._ventana_mostrar(win, recentrar=False)
        win.after(50, lambda: win.attributes("-topmost", False))

    def redetectar_gpu(self):
        """
        Vuelve a medir qué puede hacer la GPU con FFmpeg (botón "↻ Re-detectar").
        Normalmente no hace falta: la medición guardada lleva la firma de FFmpeg,
        del modelo de GPU y del driver, así que si cambias cualquiera de los tres
        se vuelve a medir sola al entrar al módulo. Este botón es para forzarlo.
        """
        if getattr(self, "_gpu_midiendo", False):
            return
        self._gpu_midiendo = True
        for lbl in ("conv_gpu_status_lbl", "comp_gpu_status_lbl"):
            widget = getattr(self, lbl, None)
            if widget is not None:
                widget.configure(text="Estado: midiendo la GPU (unos segundos)...", text_color="#d4ac0d")
        try:
            self.btn_redetectar_gpu.configure(state="disabled", text="⏳ Midiendo...")
        except Exception:
            pass

        def _medir():
            try:
                caps = ffmpeg_capacidades(forzar=True)
                cods = [n for n, e in (("H.264", "h264_nvenc"), ("H.265", "hevc_nvenc"),
                                       ("AV1", "av1_nvenc")) if caps["nvenc"].get(e) is not None]
                resumen = ("NVENC: " + "/".join(cods)) if cods else "sin NVENC utilizable"
            except Exception as e:
                resumen = f"error al medir ({str(e)[:40]})"
            finally:
                self._gpu_midiendo = False

            def _fin():
                self._gpu_video_medida = True
                self._poll_gpu_video_converter()      # repinta switches y etiquetas
                try:
                    self.btn_redetectar_gpu.configure(state="normal", text="↻ Re-detectar")
                except Exception:
                    pass
                messagebox.showinfo("Detección de GPU",
                                    f"Listo. Resultado de la medición:\n\n{resumen}\n\n"
                                    "Queda guardada para los próximos arranques.")
            self._en_ui(_fin)

        threading.Thread(target=_medir, name="dmt_redetectar_gpu", daemon=True).start()

    def _medir_gpu_video(self):
        """
        Mide las capacidades reales de FFmpeg/NVENC la PRIMERA vez que entras al
        módulo de video (unos segundos, en segundo plano). El resultado queda
        guardado en disco: abrir la app no vuelve a pagar ese costo, y si nunca
        conviertes video no se mide nunca.
        """
        if getattr(self, "_gpu_video_medida", False):
            return
        self._gpu_video_medida = True

        def _medir():
            try:
                ffmpeg_capacidades()
            except Exception as e:
                print(f"[FFmpeg] No se pudieron medir las capacidades: {e}")

        threading.Thread(target=_medir, name="dmt_ffmpeg_caps", daemon=True).start()

    def _prebuild_frames_en_background(self):
        """
        Construye los frames que aún no se han visitado, uno por uno,
        con 80 ms de pausa entre cada uno para no congelar la UI.
        Se llama 2 segundos después de que el menú aparece.
        """
        orden = [
            "VideoConverter", "AudioConverter", "ImageConverter",
            "PDFTools", "RenamerTool", "OCRTool",
            "TranscribeTool", "MetadataTool", "YouTubeTool",
        ]
        to_build = [n for n in orden if n not in self.frames]

        def _build_next(idx):
            if idx >= len(to_build):
                print("[Prebuild] ✅ Todos los frames construidos.")
                self.after(400, self._prebuild_ventanas_estaticas)
                return
            name = to_build[idx]
            if name not in self.frames:
                builder = self._frame_builders.get(name)
                if builder:
                    try:
                        builder()
                    except Exception as e:
                        print(f"[Prebuild] Error en {name}: {e}")
            self.after(80, lambda: _build_next(idx + 1))

        _build_next(0)

    # ==========================================================================
    #   VENTANAS SECUNDARIAS (helpers comunes)
    # ==========================================================================
    def _ventana_nueva(self, titulo, ancho, alto, *, fg_color=None, redimensionable=None,
                       minimo=None, padre=None, reutilizable=False):
        """
        Crea una VentanaSecundaria oculta, centrada sobre la app y con el ícono
        correcto. Se rellena y luego se muestra con self._ventana_mostrar(win).
        reutilizable=True: cerrar la oculta (vuelve a abrir al instante).
        """
        padre = padre or self
        win = VentanaSecundaria(padre, fg_color=(self.current_bg if fg_color is None else fg_color))
        win.title(titulo)
        win._dmt_tamano = (int(ancho), int(alto))
        win._dmt_padre = padre
        if redimensionable is not None:
            win.resizable(*redimensionable)
        if minimo:
            win.minsize(*minimo)
        self._ventana_centrar(win)
        try:
            win.transient(padre)
        except Exception:
            pass
        self.force_window_icon(win)
        if reutilizable:
            win.protocol("WM_DELETE_WINDOW", lambda w=win: self._ventana_ocultar(w))
        return win

    def _ventana_centrar(self, win):
        ancho, alto = getattr(win, "_dmt_tamano", (400, 300))
        padre = getattr(win, "_dmt_padre", self)
        try:
            escala = float(win._get_window_scaling())
        except Exception:
            escala = 1.0
        try:
            px, py = padre.winfo_x(), padre.winfo_y()
            pw, ph = padre.winfo_width(), padre.winfo_height()
            if pw <= 1 or ph <= 1:            # la app aún no tiene tamaño real
                raise ValueError
            x = max(0, px + (pw - int(ancho * escala)) // 2)
            y = max(0, py + (ph - int(alto * escala)) // 2)
            win.geometry(f"{ancho}x{alto}+{x}+{y}")
        except Exception:
            win.geometry(f"{ancho}x{alto}")

    def _ventana_mostrar(self, win, recentrar=True):
        try:
            if recentrar and not win.dmt_visible():
                self._ventana_centrar(win)
            win.dmt_mostrar(self)
        except Exception as e:
            print(f"[Ventanas] No se pudo mostrar: {e}")

    def _ventana_ocultar(self, win):
        try:
            win.dmt_ocultar()
        except Exception:
            pass

    def _ventana_reusar(self, win, fg_color=None):
        """True si la ventana cacheada sigue viva (y la muestra al frente)."""
        try:
            if win is None or not win.winfo_exists():
                return False
        except Exception:
            return False
        if fg_color is not None:
            try:
                win.configure(fg_color=fg_color)
            except Exception:
                pass
        self._ventana_mostrar(win)
        return True

    def _prebuild_ventanas_estaticas(self):
        """
        Construye ocultas las ventanas de contenido fijo (Acerca de, Licencias,
        Documentación, Guía de modelos, Formatos soportados) para que abran al
        instante desde la primera vez. Una por tanda para no trabar la interfaz.
        """
        tareas = [
            ("toplevel_about", lambda: self.open_about_window(mostrar=False)),
            ("toplevel_licenses", lambda: self.open_licenses_window(mostrar=False)),
            ("toplevel_docs", lambda: self.open_docs_window(mostrar=False)),
            ("toplevel_model_help", lambda: self.open_model_help(mostrar=False)),
            ("toplevel_meta_info", lambda: self.meta_show_info_window(mostrar=False)),
        ]

        def _siguiente(i):
            if i >= len(tareas):
                print("[Prebuild] ✅ Ventanas secundarias listas.")
                return
            attr, fn = tareas[i]
            try:
                if getattr(self, attr, None) is None:
                    fn()
            except Exception as e:
                print(f"[Prebuild] Ventana {attr}: {e}")
            self.after(120, lambda: _siguiente(i + 1))

        _siguiente(0)

    # ==========================================================================
    #   HILOS E INTERFAZ: todo cambio de widgets pasa por el hilo de la interfaz
    # ==========================================================================
    def _bombear_cola_ui(self):
        # Se reprograma ANTES de ejecutar: si una acción abre un diálogo modal,
        # el resto de actualizaciones (barras de otras descargas) sigue fluyendo.
        self.after(30, self._bombear_cola_ui)
        for _ in range(400):
            try:
                fn = self._cola_ui.get_nowait()
            except queue.Empty:
                return
            try:
                fn()
            except Exception as e:
                print(f"[UI] Error aplicando un cambio diferido: {e}")

    def _en_ui(self, fn, *args, **kwargs):
        """Ejecuta fn(*args) en el hilo de la interfaz. Seguro desde cualquier hilo."""
        self._cola_ui.put(lambda: fn(*args, **kwargs))

    def _en_ui_espera(self, fn, *args, **kwargs):
        """Como _en_ui, pero espera el resultado (p. ej. un messagebox pedido desde un hilo)."""
        if threading.current_thread() is threading.main_thread():
            return fn(*args, **kwargs)
        listo = threading.Event()
        caja = {}

        def _correr():
            try:
                caja["r"] = fn(*args, **kwargs)
            except BaseException as e:
                caja["e"] = e
            finally:
                listo.set()

        self._cola_ui.put(_correr)
        listo.wait()
        if "e" in caja:
            raise caja["e"]
        return caja.get("r")

    def _rutas_drop(self, event):
        """Rutas soltadas con arrastrar y soltar (lista Tcl: respeta espacios y llaves)."""
        try:
            return [p for p in self.tk.splitlist(event.data) if p]
        except Exception:
            return []

    def _trabajo_inicio(self, clave, descripcion):
        self._trabajos[clave] = descripcion

    def _trabajo_fin(self, clave):
        self._trabajos.pop(clave, None)

    # --- Estado POR LOTE: cada hilo ve el de su propio módulo ---
    @property
    def cancel_requested(self):
        """SALTAR del lote que corre en este hilo (cada módulo tiene el suyo)."""
        return self._lote().saltar

    @cancel_requested.setter
    def cancel_requested(self, valor):
        self._lote().saltar = bool(valor)

    @property
    def current_process(self):
        """Proceso externo (FFmpeg, Ghostscript...) del lote de este hilo."""
        return self._lote().proceso

    @current_process.setter
    def current_process(self, valor):
        self._lote().proceso = valor

    @property
    def is_processing(self):
        """True si CUALQUIER módulo está trabajando (avisos, cierre de la app)."""
        return bool(getattr(self, "_lotes", None)) or bool(getattr(self, "_ocupados_extra", None))

    @is_processing.setter
    def is_processing(self, valor):
        # Compatibilidad para módulos que se marcan ocupados sin usar un lote.
        extra = getattr(self, "_ocupados_extra", None)
        if extra is None:
            extra = self._ocupados_extra = set()
        if valor:
            extra.add("otro")
        else:
            extra.discard("otro")

    def _procesos_de_lotes(self):
        """Procesos externos vivos de todos los lotes (para cerrar la app)."""
        return [l.proceso for l in list(getattr(self, "_lotes", {}).values()) if l.proceso]

    # ==========================================================================
    #   MODELOS DE IA: marcar "en uso" mientras un módulo trabaja
    # ==========================================================================
    def _uso_modelo_para_modo(self, modo):
        nombre = {"ocr": "ocr", "transcribe": "whisper"}.get(modo)
        return self.gestor_ia.en_uso(nombre) if nombre else contextlib.nullcontext()

    def _con_uso_modelo(self, nombre, fn, *args):
        with self.gestor_ia.en_uso(nombre):
            return fn(*args)

    def force_window_icon(self, window):
        """
        Fuerza el icono en ventanas secundarias (Toplevel).
        Usa un retraso para asegurar que el Gestor de Ventanas no lo sobrescriba.
        """
        def apply_icon_internal():
            # 1. Intentar poner el .ico (Barra de tareas / Esquina ventana)
            try:
                if os.path.exists(self.app_icon_path):
                    window.iconbitmap(self.app_icon_path)
            except Exception: pass

            # 2. Intentar poner el .png (Para compatibilidad visual extra)
            try:
                target = self.app_logo_png_path if os.path.exists(self.app_logo_png_path) else self.app_icon_path
                if os.path.exists(target):
                    img = Image.open(target).convert("RGBA")
                    # Tamaño estándar para iconos de ventana
                    img = img.resize((32, 32), Image.Resampling.LANCZOS)
                    photo = ImageTk.PhotoImage(img)
                    
                    # wm_iconphoto(False, ...) aplica el icono SOLO a esta ventana
                    window.wm_iconphoto(False, photo)
                    
                    # Guardamos la referencia EN LA VENTANA para que no se borre de memoria
                    window._icon_ref_persistant = photo
            except Exception: pass

        # A. Aplicar inmediatamente
        apply_icon_internal()
        
        # B. 🔥 EL TRUCO: Re-aplicar 200ms después para asegurar que se quede.
        #    Se programa en la app (no en la ventana) y se verifica que la ventana
        #    siga viva: si se cerró antes, no queda un comando huérfano en Tcl.
        def _reaplicar():
            try:
                if window.winfo_exists():
                    apply_icon_internal()
            except Exception:
                pass
        self.after(200, _reaplicar)

    def get_image_from_cache(self, file_path, size, mode="contain"):
        """
        Carga segura de imágenes con caché persistente.

        mode="contain" (por defecto): respeta la relación de aspecto y centra
        la imagen en una caja del tamaño pedido, rellenando con transparencia.
        Es el comportamiento correcto para miniaturas/previews.

        mode="stretch": comportamiento antiguo (estira hasta el tamaño exacto).
        Se conserva por compatibilidad, pero deforma imágenes no cuadradas.
        """
        # Clave única para el caché
        cache_key = f"{file_path}_{size}_{mode}"

        # 1. Si ya existe, devolverla rápido
        if cache_key in self.permanent_image_cache:
            return self.permanent_image_cache[cache_key]

        # 2. Verificar existencia
        if not os.path.exists(file_path):
            print(f"[ERROR] No existe archivo: {file_path}")
            return None
        try:
            # Apertura inteligente: si es .ico elige la mejor capa disponible
            # para el tamaño pedido (evita partir de un frame de 16x16).
            target_px = max(size) if size else None
            pil_img = img_open_smart(file_path, target_px=target_px)

            if size:
                if mode == "stretch":
                    if tuple(pil_img.size) != tuple(size):
                        pil_img = pil_img.resize(size, Image.Resampling.LANCZOS)
                else:
                    pil_img = img_contain(pil_img, size, pad=True)

            final_size = size if size else pil_img.size

            tk_img = ctk.CTkImage(light_image=pil_img,
                                  dark_image=pil_img,
                                  size=final_size)

            # Guardar en caché para evitar que el recolector elimine la referencia
            self.permanent_image_cache[cache_key] = tk_img
            return tk_img

        except Exception as e:
            print(f"[ERROR] get_image_from_cache fallo: {e}")
            return None
    def set_window_icon(self, window):
        """Setea el icono de la ventana usando 1.ico o genera un ICO desde logo.png si hace falta."""
        try:
            ico_path = self.app_icon_path
            # Si no existe el .ico pero sí el png, generar temporal .ico
            if not os.path.exists(ico_path) and os.path.exists(self.app_logo_png_path):
                # Carpeta escribible (la del programa puede estar protegida)
                gen_path = os.path.join(_dmt_base_dir(), 'temp_icon.ico')
                if not os.path.exists(gen_path):
                    try:
                        pil = Image.open(self.app_logo_png_path).convert('RGBA')
                        pil.save(gen_path, format='ICO', sizes=[(64,64)])
                    except Exception:
                        gen_path = None
                if gen_path and os.path.exists(gen_path):
                    ico_path = gen_path

            if ico_path and os.path.exists(ico_path):
                try:
                    window.iconbitmap(ico_path)
                except Exception:
                    pass
        except Exception:
            pass
        # Además intentar aplicar icono desde PNG (iconphoto) como fallback
        try:
            png_path = self.app_logo_png_path if os.path.exists(self.app_logo_png_path) else (ico_path if os.path.exists(ico_path) else None)
            if png_path and os.path.exists(png_path):
                img = Image.open(png_path).convert('RGBA')
                img = img.resize((64, 64), Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(img)
                try:
                    window.iconphoto(True, photo)
                except Exception:
                    try:
                        # Algunos widgets usan wm_iconphoto
                        window.wm_iconphoto(True, photo)
                    except: pass

                # Mantener referencia para evitar GC (varias ventanas usan el mismo objeto)
                if not hasattr(self, 'icon_refs'):
                    self.icon_refs = []
                self.icon_refs.append(photo)
        except Exception as e:
            print(f"[WARN] set_window_icon fallback fallo: {e}")

    # ==========================================================================
    #   BARRA SUPERIOR (CORREGIDA: FUENTE FINA Y TEMA PERSISTENTE)
    # ==========================================================================
    def init_top_bar(self):
        # Fondo de la barra: Negro absoluto
        self.top_bar_frame = ctk.CTkFrame(self, height=45, corner_radius=0, fg_color="#000000")
        self.top_bar_frame.grid(row=0, column=0, sticky="ew")
        self.top_bar_frame.grid_propagate(False) 

        # --- IZQUIERDA: TÍTULO (con sombra para modo claro) ---
        # Usamos 2 labels: uno como sombra (detrás) y otro encima como texto principal.
        self.lbl_logo_shadow = ctk.CTkLabel(self.top_bar_frame, text=" D E U S   M A C H I N A  |  T O O L S ",
                            font=(self.main_font, 14, "bold"), text_color="#000000")
        self.lbl_logo_shadow.place(x=22, y=10)

        self.lbl_logo = ctk.CTkLabel(self.top_bar_frame, text=" D E U S   M A C H I N A  |  T O O L S ", 
                          font=(self.main_font, 14, "bold"), text_color="#087000")
        self.lbl_logo.place(x=20, y=8)

        # --- DERECHA: BOTONES ESTILO "VOLVER" (SIN BOLD) ---
        
        # Estilo fino y elegante
        btn_font = (self.main_font, 12) # Sin "bold"
        
        # Configuración común
        btn_kwargs = {
            "fg_color": "transparent",
            "border_width": 1,
            "border_color": "#444",
            "text_color": "#ccc",     # Texto gris claro elegante
            "hover_color": "#222",
            "height": 30,             # Un poco más alto para verse bien
            "font": btn_font
        }

        # 3. BOTÓN ACERCA DE
        self.btn_about = ctk.CTkButton(self.top_bar_frame, text="ⓘ Acerca de...", width=100, 
                                       command=self.open_about_window, **btn_kwargs)
        self.btn_about.pack(side="right", padx=5)

        # 2. BOTÓN LICENCIAS
        self.btn_lic = ctk.CTkButton(self.top_bar_frame, text="📜 Licencias", width=100,
                                     command=self.open_licenses_window, **btn_kwargs)
        self.btn_lic.pack(side="right", padx=5)

        # 1. SELECTOR DE PALETA (DISFRAZADO DE BOTÓN)
        self.palette_var = ctk.StringVar(value="🎨 Cambiar Tema")

        # Solo temas de color personalizados
        combined_values = list(self.theme_colors.keys())

        self.opt_palette = ctk.CTkOptionMenu(self.top_bar_frame,
                           values=combined_values,
                           variable=self.palette_var,
                           width=150, height=30,
                           fg_color="#000000", # Negro para fundirse con la barra
                           button_color="#222",
                           button_hover_color="#333",
                           text_color="#ccc",
                           font=btn_font,
                           command=self.change_app_palette)
        # Por defecto mostramos el primer tema disponible
        self.palette_var.set(list(self.theme_colors.keys())[0])


        # [CAMBIO AQUI]: padx=(0, 15) -> El 0 quita el espacio a su izquierda para recibir al texto
        self.opt_palette.pack(side="right", padx=(0, 15))

        # --- [NUEVO] ETIQUETA "Temas: " ---
        # Al usar side="right", lo que ponemos AL FINAL en el código queda a la IZQUIERDA visualmente.
        ctk.CTkLabel(self.top_bar_frame, text="Temas:", font=btn_font, text_color="#ccc").pack(side="right", padx=(10, 2))

    def change_app_palette(self, selection):
        # Ignorar el separador visual ...
        if selection == "────────":
            return

        # Manejar los temas por color
        if selection not in self.theme_colors:
            return

        color = self.theme_colors[selection]
        self.current_bg = color
        print(f"DEBUG: Aplicando tema -> {selection} ({color})")
        try:
            # Aplicar el color de fondo
            self.configure(fg_color=color)

            # --- NUEVO: GUARDAR SELECCIÓN ---
            self.save_theme_preference(selection)

        except Exception as e:
            print(f"Error al aplicar tema: {e}")

    def open_about_window(self, mostrar=True):
        if mostrar and self._ventana_reusar(self.toplevel_about, fg_color=self.current_bg):
            return
        if not mostrar and self.toplevel_about is not None:
            return

        import warnings
        # 2. Configuración de la ventana (Tamaño reducido y compacto)
        # Dimensiones reducidas (antes 480x600, ahora 420x550)
        w, h = 360, 500 
        about = self._ventana_nueva("Acerca de...  ℹ️", w, h,
                                    redimensionable=(False, False), reutilizable=True)
        self.toplevel_about = about  # <--- GUARDAR REFERENCIA AQUÍ

        # -----------------------------------------------------------
        # HEADER GRANDE Y CENTRADO
        # -----------------------------------------------------------
        header_frame = ctk.CTkFrame(about, fg_color="transparent")
        header_frame.pack(pady=(20, 10))

        # Definir carpeta de recursos localmente
        assets_dir = resource_path("imgtype")

        # Cargar Logo App (Grande)
        ruta_logo_app = os.path.join(assets_dir, "logo.png")
        
        if os.path.exists(ruta_logo_app):
            try:
                pil_img = Image.open(ruta_logo_app).convert("RGBA")
                # Tamaño grande original (85x85)
                pil_img = pil_img.resize((95, 95), Image.Resampling.LANCZOS)
                # --- PEGA ESTO NUEVO ---
                photo_app = ImageTk.PhotoImage(pil_img, master=about)
                
                if not hasattr(self, 'permanent_refs'): self.permanent_refs = []
                self.permanent_refs.append(photo_app)
                
                with warnings.catch_warnings():
                    warnings.simplefilter("ignore")
                    ctk.CTkLabel(header_frame, text="", image=photo_app).pack(pady=(0, 5))

            except: pass

        # Títulos Grandes
        ctk.CTkLabel(header_frame, text="DEUS MACHINA", font=(self.main_font, 22, "bold"), text_color="#2cc985").pack()
        ctk.CTkLabel(header_frame, text="| TOOLS |", font=(self.main_font, 14), text_color="#777").pack()

        # -----------------------------------------------------------
        # TARJETA DE INFORMACIÓN
        # -----------------------------------------------------------
        card_frame = ctk.CTkFrame(about, fg_color="#181818", border_width=1, border_color="#333", corner_radius=12)
        card_frame.pack(fill="both", expand=True, padx=25, pady=(0, 20))
        
        # --- ZONA DE PERFIL (IZQUIERDA: DATOS | DERECHA: AVATAR) ---
        profile_area = ctk.CTkFrame(card_frame, fg_color="transparent")
        profile_area.pack(fill="x", padx=20, pady=(20, 5))

        # Columna Izquierda (Texto)
        left_col = ctk.CTkFrame(profile_area, fg_color="transparent")
        left_col.pack(side="left", fill="y", expand=True, anchor="w")

        ctk.CTkLabel(left_col, text="Desarrollador", fg_color="#222", corner_radius=4,
                     font=("Arial", 12, "bold"), text_color="#cccccc", width=85).pack(anchor="w", pady=(0, 5), padx=(25, 0))
        
        ctk.CTkLabel(left_col, text="Kevin González", font=(self.main_font, 18, "bold"), text_color="white").pack(anchor="w")
        ctk.CTkLabel(left_col, text="  < DoMiNaTh0R >", font=(self.main_font, 13, "bold"), text_color="#f1c40f").pack(anchor="w", pady=(2, 0))

        # Columna Derecha (Logo Personal)
        right_col = ctk.CTkFrame(profile_area, fg_color="transparent")
        right_col.pack(side="right", anchor="e", padx=(0, 20))

        # Cargar Avatar Personal (avatar.jpg)
        ruta_avatar = os.path.join(assets_dir, "avatar.jpg") # <--- CAMBIADO A .jpg
        
        avatar_loaded = False
        if os.path.exists(ruta_avatar):
            try:
                pil_av = Image.open(ruta_avatar).convert("RGBA")
                # Tamaño de avatar
                pil_av = pil_av.resize((85, 85), Image.Resampling.LANCZOS)
                
                # Máscara circular suave
                mask = Image.new('L', (85, 85), 0)
                from PIL import ImageDraw
                draw = ImageDraw.Draw(mask)
                draw.ellipse((0, 0, 85, 85), fill=255)
                pil_av.putalpha(mask)
                
                # --- PEGA ESTO NUEVO ---
                photo_av = ImageTk.PhotoImage(pil_av, master=about)
                self.permanent_refs.append(photo_av)
                
                with warnings.catch_warnings():
                    warnings.simplefilter("ignore")
                    ctk.CTkLabel(right_col, text="", image=photo_av).pack()
                    
                avatar_loaded = True
            except: pass
        
        if not avatar_loaded:
            # Placeholder circular si falla la imagen
            canvas = ctk.CTkCanvas(right_col, width=75, height=75, bg="#181818", highlightthickness=0)
            canvas.pack()
            canvas.create_oval(2, 2, 73, 73, fill="#222", outline="#333")
            canvas.create_text(37, 37, text="IMG", fill="#555", font=("Arial", 8))

        # Separador
        ctk.CTkFrame(card_frame, height=1, fg_color="#333").pack(fill="x", padx=20, pady=10)

        # --- INFO TÉCNICA ---
        ver_str = globals().get('version', '1.0')
        tech_row = ctk.CTkFrame(card_frame, fg_color="transparent")
        tech_row.pack(pady=2)
        
        ctk.CTkLabel(tech_row, text=f"Versión: {ver_str}", font=("Arial", 12, "bold"), text_color="#cccccc").pack(side="left", padx=5)
        ctk.CTkLabel(tech_row, text="•", font=("Arial", 16, "bold"), text_color="#444").pack(side="left")
        import platform as _platform
        ctk.CTkLabel(tech_row, text=f"Python {_platform.python_version()}", font=("Arial", 11, "bold"), text_color="#cccccc").pack(side="left", padx=5)

        # --- BOTÓN TÉRMINOS Y CONDICIONES (AGRANDADO) ---
        # ==============================================================================
        # --- NUEVO SISTEMA DE DOCUMENTACIÓN (3 PESTAÑAS) ---
        # ==============================================================================
        # Botón actualizado en la interfaz principal de Acerca de
        ctk.CTkButton(card_frame, text="Ver Documentación y Legal", 
                      fg_color="#222", hover_color="#333", border_width=1, border_color="#444",
                      text_color="#bbb", font=("Arial", 11, "bold"), 
                      height=35, width=220, 
                      command=self.open_docs_window).pack(pady=(15, 5))
        # ==============================================================================
        
        ctk.CTkButton(card_frame, text="Cerrar", width=120, height=32, command=lambda: self._ventana_ocultar(about), 
                      fg_color="#2b2b2b", border_width=1, border_color="#333", 
                      font=(self.main_font, 12), hover_color="#333").pack(pady=(10, 8))
        
        # --- FOOTER ---
        year = datetime.datetime.now().year
        ctk.CTkLabel(
            card_frame,
            text=(f"© {year} Kevin González (DoMiNaTh0R)\n"
                  "Software libre bajo licencia GNU AGPL v3 — sin garantía.\n"
                  "Código fuente: github.com/DoMiNaTh0R/DEUS-MACHINA-TOOLS"),
            font=("Arial", 10),
            text_color="#555"
        ).pack(pady=(0, 4))

        if mostrar:
            self._ventana_mostrar(about)

    def open_docs_window(self, mostrar=True):
        """Documentación y Legal (Léeme / Licencia AGPL / Third Party / Términos)."""
        if mostrar and self._ventana_reusar(self.toplevel_docs):
            return
        if not mostrar and self.toplevel_docs is not None:
            return

        docs_win = self._ventana_nueva("Documentación y Legal", 600, 700,
                                       fg_color="#1a1a1a", reutilizable=True)
        self.toplevel_docs = docs_win

        # 1. Definir rutas de los archivos (Asegúrate de que existan en 'imgtype')
        # Nombres sugeridos: README.txt, TTHIRD_PARTY_NOTICES.txt, EULA.txt
        files_map = {
            "Léeme (Readme)": resource_path(os.path.join("imgtype", "README.txt")),
            "Licencia (AGPL)": resource_path(os.path.join("imgtype", "LICENSE.txt")),
            "Third Party": resource_path(os.path.join("imgtype", "THIRD_PARTY_NOTICES.txt")),
            "Términos": resource_path(os.path.join("imgtype", "EULA.txt"))
        }

        # 2. Crear Tabview
        tabview = ctk.CTkTabview(docs_win, fg_color="#181818", text_color="#eee")
        tabview.pack(fill="both", expand=True, padx=10, pady=10)

        # 3. Función para cargar contenido
        def cargar_texto(tab_name, file_path):
            tab = tabview.add(tab_name)
            
            # Textbox
            tb = ctk.CTkTextbox(tab, fg_color="#111", text_color="#ddd", font=("Consolas", 12))
            tb.pack(fill="both", expand=True, padx=5, pady=5)
            
            content = f"⚠️ Archivo no encontrado:\n{file_path}"
            try:
                if os.path.exists(file_path):
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()
            except Exception as e:
                content = f"Error leyendo archivo:\n{str(e)}"
            
            tb.insert("0.0", content)
            tb.configure(state="disabled")

        # 4. Generar pestañas
        # El orden importa: Primero 'Léeme' para que sea el default
        cargar_texto("Léeme (Readme)", files_map["Léeme (Readme)"])
        cargar_texto("Licencia (AGPL)", files_map["Licencia (AGPL)"])
        cargar_texto("Third Party", files_map["Third Party"])
        cargar_texto("Términos", files_map["Términos"])
        
        # Establecer default explícito
        tabview.set("Léeme (Readme)")

        # 5. Botón para abrir externamente (Dinámico según pestaña activa)
        def abrir_actual():
            current_tab = tabview.get() # Obtiene el nombre de la pestaña actual
            path = files_map.get(current_tab, "")
            if path and os.path.exists(path):
                try:
                    os.startfile(path)
                except:
                    messagebox.showerror("Error", f"No se pudo abrir: {path}")
            else:
                messagebox.showwarning("Archivo", "El archivo de esta sección no existe en disco.")

        btn_frame = ctk.CTkFrame(docs_win, fg_color="transparent")
        btn_frame.pack(fill="x", pady=(0, 15), padx=20)

        ctk.CTkButton(btn_frame, text="📂 Abrir Archivo Actual en Editor", 
                      fg_color="#333", hover_color="#444", 
                      border_width=1, border_color="#555",
                      command=abrir_actual).pack(side="left", expand=True)
        
        ctk.CTkButton(btn_frame, text="Cerrar", width=100,
                      fg_color="#c0392b", hover_color="#922b21",
                      command=lambda: self._ventana_ocultar(docs_win)).pack(side="right", padx=(10, 0))

        if mostrar:
            self._ventana_mostrar(docs_win)




    # ==========================================================================
    #   SISTEMA DE LICENCIAS (CORREGIDO CON HEADER ESTILIZADO)
    # ==========================================================================

    # ==========================================================================
    #   SISTEMA DE LICENCIAS (HEADER COMPACTO + PANEL DERECHO FIJO)
    # ==========================================================================

    # ==========================================================================
    #   SISTEMA DE LICENCIAS (DISEÑO CENTRADO + BADGES APILADOS)
    # ==========================================================================

    def open_licenses_window(self, mostrar=True):
        """
        Ventana de Licencias (OPTIMIZADA V3: Debounce para scroll fluido + Hover activo)
        """
        # 1. SI YA EXISTE, SOLO MOSTRAR/ENFOCAR (se reutiliza)
        if mostrar and self._ventana_reusar(self.toplevel_licenses, fg_color=self.current_bg):
            return
        if not mostrar and self.toplevel_licenses is not None:
            return

        import webbrowser

        # Crear Toplevel (oculta hasta terminar de construirla)
        w, h = 820, 625 
        lic = self._ventana_nueva("Créditos y Licencias 📜", w, h,
                                  minimo=(w, h), reutilizable=True)
        self.toplevel_licenses = lic # <--- GUARDAR REFERENCIA AQUÍ

        # -----------------------------------------------------------
        # HEADER COMPACTO
        # -----------------------------------------------------------
        header_container = ctk.CTkFrame(lic, fg_color="transparent")
        header_container.pack(pady=(15, 10), anchor="center")

        header_bg = ctk.CTkFrame(header_container, fg_color="#151515", corner_radius=7)
        header_bg.pack() 

        # --- CARGA IMÁGENES HEADER ---
        import warnings
        assets_dir = resource_path("imgtype") # Definir ruta assets
        
        if not hasattr(self, 'permanent_refs'): self.permanent_refs = []

        # Logo Izquierda
        ruta_logo = os.path.join(assets_dir, "logo.png")
        if os.path.exists(ruta_logo):
            try:
                pil_img = Image.open(ruta_logo).convert("RGBA")
                pil_img = pil_img.resize((55, 55), Image.Resampling.LANCZOS)
                photo_logo = ImageTk.PhotoImage(pil_img, master=lic)
                self.permanent_refs.append(photo_logo)
                with warnings.catch_warnings():
                    warnings.simplefilter("ignore")
                    ctk.CTkLabel(header_bg, text="", image=photo_logo).pack(side="left", padx=(4, 10), pady=1)
            except: pass
        
        # Título
        ctk.CTkLabel(header_bg, text="Créditos y Licencias", font=(self.main_font, 28, "bold"), text_color="#a88131").pack(side="left", pady=1)
        
        # Imagen Derecha
        ruta_licen = os.path.join(assets_dir, "licen_img.png")
        if os.path.exists(ruta_licen):
            try:
                pil_img_lic = Image.open(ruta_licen).convert("RGBA")
                pil_img_lic = pil_img_lic.resize((55, 55), Image.Resampling.LANCZOS)
                photo_licen = ImageTk.PhotoImage(pil_img_lic, master=lic)
                self.permanent_refs.append(photo_licen)
                with warnings.catch_warnings():
                    warnings.simplefilter("ignore")
                    ctk.CTkLabel(header_bg, text="", image=photo_licen).pack(side="left", padx=(10, 4), pady=1)
            except: pass

        # -----------------------------------------------------------
        # CUERPO
        # -----------------------------------------------------------
        body = ctk.CTkFrame(lic, fg_color="transparent")
        body.pack(expand=True, padx=15, pady=(5, 10)) 

        # 1. LISTA (IZQUIERDA)
        left = ctk.CTkScrollableFrame(body, width=270, height=465, corner_radius=8, fg_color="#151515")
        left.pack(side="left", padx=(0, 15)) 

        # AGREGA ESTA LÍNEA PARA AUMENTAR VELOCIDAD (Prueba 15, 20 o 25)
        left._parent_canvas.configure(yscrollincrement=4)

        # 2. PREVIEW (DERECHA)
        right = ctk.CTkFrame(body, width=450, height=480, fg_color="#181818", corner_radius=12, border_width=1, border_color="#333")
        right.pack(side="left")
        right.pack_propagate(False) 

        # --- CONTENIDO PANEL DERECHO ---
        preview_content = ctk.CTkFrame(right, fg_color="transparent")
        preview_content.pack(fill="both", expand=True, padx=20, pady=20)

        # A) Título
        self.preview_title = ctk.CTkLabel(preview_content, text="Selecciona una librería", 
                                     font=(self.main_font, 22, "bold"), 
                                     text_color="white", anchor="center")
        self.preview_title.pack(fill="x", pady=(0, 2))

        # B) Versión
        self.preview_version = ctk.CTkLabel(preview_content, text="", 
                                       font=("Arial", 10), text_color="#777", anchor="center")
        self.preview_version.pack(fill="x", pady=(0, 5)) 

        # C) Badges
        badge_role_frame = ctk.CTkFrame(preview_content, fg_color="#1f2b38", corner_radius=8, border_width=1, border_color="#374b5c")
        badge_role_frame.pack(anchor="center", pady=(0, 8))
        self.preview_role = ctk.CTkLabel(badge_role_frame, text="Función: —", font=("Arial", 12), text_color="#dbeaf9")
        self.preview_role.pack(padx=12, pady=5)

        badge_lic_frame = ctk.CTkFrame(preview_content, fg_color="#1a2e1a", corner_radius=8, border_width=1, border_color="#2d5a2d")
        badge_lic_frame.pack(anchor="center", pady=(0, 15))
        self.preview_license = ctk.CTkLabel(badge_lic_frame, text="Licencia: —", font=("Arial", 12, "bold"), text_color="#6ecc6e")
        self.preview_license.pack(padx=12, pady=5)

        # Separador
        ctk.CTkFrame(preview_content, height=2, fg_color="#333").pack(fill="x", pady=(0, 15))

        # D) RECTÁNGULO OSCURO (CONTENEDOR FIJO)
        desc_box_container = ctk.CTkFrame(preview_content, fg_color="#111", corner_radius=8)
        desc_box_container.pack(fill="both", expand=True)

        # 4. Botón Web (FIJO ABAJO)
        self.btn_web = ctk.CTkButton(desc_box_container, text="Ver Página Oficial ↗", width=140, height=28,
                                     fg_color="#222", hover_color="#333", border_width=1, border_color="#444",
                                     font=("Arial", 11))
        self.btn_web.pack(side="bottom", pady=(10, 15), padx=15, anchor="center")

        # Área de Texto (SIN SCROLLBAR)
        self.desc_scroll_area = ctk.CTkFrame(desc_box_container, fg_color="transparent")
        self.desc_scroll_area.pack(side="top", fill="both", expand=True, padx=5, pady=5)

        # 1. Descripción
        self.preview_desc = ctk.CTkLabel(self.desc_scroll_area, text="(Pasa el cursor encima de una librería para ver detalles)", 
                                    font=("Arial", 14), text_color="#ccc",
                                    wraplength=380, justify="left", anchor="nw")
        self.preview_desc.pack(fill="x", padx=10, pady=(15, 5))

        # 2. Notas (Opcional)
        self.preview_notes = ctk.CTkLabel(self.desc_scroll_area, text="", font=("Arial", 11, "italic"), text_color="#aaa",
                                          wraplength=380, justify="left", anchor="nw")
        
        # 3. Legal
        self.preview_legal = ctk.CTkLabel(self.desc_scroll_area, text="", 
                                     font=("Arial", 10), text_color="#555", 
                                     wraplength=380, justify="left", anchor="w")
        
        # BOTÓN CERRAR VENTANA
        btn_frame = ctk.CTkFrame(lic, fg_color="transparent")
        btn_frame.pack(fill="x", padx=12, pady=(0,12))
        ctk.CTkButton(btn_frame, text="Cerrar", width=240, height=35, command=lambda: self._ventana_ocultar(lic),
                      fg_color="transparent", border_width=1, border_color="#555",
                      font=(self.main_font, 14), hover_color="#333").pack(pady=1)

        # -------------------------------------------------------------------------
        # LÓGICA DE ACTUALIZACIÓN CON DEBOUNCE (ANTI-LAG)
        # -------------------------------------------------------------------------
        global libs_by_group 
        self._libs_by_group = libs_by_group 
        
        self.all_list_items = [] # Lista global para limpiar selección
        self._hover_job = None   # Variable para el temporizador anti-lag

        def _perform_update(lib, container_activado, lbl_activado):
            """
            Esta función hace el trabajo pesado. Solo se llama si el mouse
            se detiene un momento sobre un ítem.
            """
            # 1. Actualizar Panel Derecho
            # Header
            self.preview_title.configure(text=lib['name'])
            self.preview_role.configure(text=lib.get('role', '—'))
            self.preview_license.configure(text=f"Licencia: {lib.get('license', '—')}")

            # Versión
            # USAMOS LA VERSIÓN DEFINIDA EN EL DICCIONARIO
            ver_str = f"Versión: {lib.get('version', 'Desconocida')}"
            self.preview_version.configure(text=ver_str)

            # Descripción
            self.preview_desc.configure(text=lib.get('desc', "Sin descripción."))

            # Notas
            notes_txt = ""
            if lib.get('notes'): notes_txt += f"• {lib['notes']}\n"
            if lib.get('gpu'): notes_txt += f"• GPU: {lib['gpu']}\n"
            
            self.preview_notes.pack_forget() 
            self.preview_legal.pack_forget()

            if notes_txt:
                self.preview_notes.configure(text=notes_txt)
                self.preview_notes.pack(after=self.preview_desc, fill="x", padx=10, pady=(8, 2))

            # Legal
            self.preview_legal.configure(text=lib.get('legal', ""))
            self.preview_legal.pack(fill="x", padx=10, pady=(2, 10))

            # Botón Web
            url = lib.get('url', "")
            if url:
                self.btn_web.configure(state="normal", command=lambda: webbrowser.open(url))
                if not self.btn_web.winfo_ismapped():
                    self.btn_web.pack(side="bottom", pady=(10, 15), padx=15, anchor="center")
            else:
                self.btn_web.pack_forget()
            
            # 2. Gestionar ILUMINACIÓN ÚNICA (Solo uno encendido a la vez)
            for w, lbl in self.all_list_items:
                if w != container_activado:
                    try: 
                        # Apagar los demás
                        if w.cget("fg_color") != "transparent":
                            w.configure(fg_color="transparent")
                        if lbl.cget("text_color") != "#ddd":
                            lbl.configure(text_color="#ddd")
                    except: pass
            
            # Encender el actual
            try:
                container_activado.configure(fg_color="#222222")
                lbl_activado.configure(text_color="#ffffff")
            except: pass


        # Helper: Crear items lista
        def _make_lib_widget(parent_frame, lib):
            container = ctk.CTkFrame(parent_frame, fg_color="transparent")
            container.pack(fill="x", pady=1, padx=4) 

            name_lbl = ctk.CTkLabel(container, text=f"• {lib['name']}", font=(self.main_font, 12), anchor="w", text_color="#ddd")
            name_lbl.pack(side="left", padx=8, pady=2) 
            
            self.all_list_items.append((container, name_lbl))

            def on_enter(e):
                # 1. Cancelar cualquier actualización pendiente (Evita lag al hacer scroll)
                if self._hover_job:
                    self.after_cancel(self._hover_job)
                
                # 2. Programar nueva actualización en 60ms.
                # Si el usuario mueve el mouse rápido a otro item antes de 60ms, 
                # este timer se cancelará y NADA ocurrirá (0 consumo de CPU).
                self._hover_job = self.after(6, lambda: _perform_update(lib, container, name_lbl))

            # Bindings
            # Solo usamos <Enter>. Al entrar, el sistema se encarga de apagar los demás.
            container.bind("<Enter>", on_enter)
            name_lbl.bind("<Enter>", on_enter)

            return container

        # Llenar lista
        if self._libs_by_group:
            for group_name, libs in self._libs_by_group.items():
                grp_frame = ctk.CTkFrame(left, fg_color="#0f0f0f", corner_radius=6)
                grp_frame.pack(fill="x", pady=(8,6), padx=6)

                ctk.CTkLabel(grp_frame, text=group_name, font=(self.main_font, 12, "bold"), text_color="#87ceeb").pack(anchor="w", padx=8, pady=(6,2))
                for lib in libs:
                    _make_lib_widget(grp_frame, lib)
            
            try:
                # Cargar el primero manualmente para que no quede vacío al inicio
                if self.all_list_items:
                    first_cont, first_lbl = self.all_list_items[0]
                    _perform_update(list(self._libs_by_group.values())[0][0], first_cont, first_lbl)
            except: pass
        else:
            ctk.CTkLabel(left, text="No se encontraron datos.").pack(pady=20)

        if mostrar:
            self._ventana_mostrar(lic)









        

            

    



    


    # ==========================================================================
    #   SECCIÓN 1: MENÚ PRINCIPAL
    # ==========================================================================
    def create_glass_panel(self, parent_frame):
        """
        Crea un panel estilo 'Cristal Oscuro' donde irán los botones.
        El parent_frame debe ser 'transparent' para ver el fondo detras.
        """
        panel = ctk.CTkFrame(parent_frame, 
                           fg_color="#101010", # Color casi negro opaco (simula cristal ahumado)
                           corner_radius=20,   # Bordes redondeados
                           border_width=1, 
                           border_color="#333333", # Borde sutil
                           width=700,  # Ancho máximo fijo
                           height=500) # Altura máxima fija
        
        # Usar place en lugar de pack para controlar mejor el tamaño
        panel.pack(expand=True, fill="both", padx=80, pady=60) 
        return panel
    
    def init_menu_module(self):
        # 1. Frame base TRANSPARENTE (para ver la foto)
        self.menu_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.frames["Menu"] = self.menu_frame
        
        # 2. Panel de Cristal (Aquí va el contenido)
        glass_panel = self.create_glass_panel(self.menu_frame)
        
        # Título con fondo redondeado
        title_bg = ctk.CTkFrame(glass_panel, fg_color="#2b2b2b", corner_radius=8)
        title_bg.pack(pady=(100, 20), padx=40)
        ctk.CTkLabel(title_bg, text="Menú de Herramientas", font=(self.main_font, 36, "bold"), text_color="white", bg_color="#2b2b2b").pack(padx=40, pady=15)
        
        # Frame contenedor de botones (dentro del cristal)
        btns_frame = ctk.CTkFrame(glass_panel, fg_color="transparent")
        btns_frame.pack(expand=True) 

        # Configuración de botones (TU LOGICA ORIGINAL INTACTA)
        buttons_config = [
            ("Convertidor de Videos", lambda: self.show_frame("VideoConverter"), "#1f6aa5", "#144870"),
            ("Convertidor de Audio", lambda: self.show_frame("AudioConverter"), "#087000", "#065000"),
            ("Convertidor de Imágenes", lambda: self.show_frame("ImageConverter"), "#8f4e1d", "#6e3b15"),
            ("Renombrador Masivo", lambda: self.show_frame("RenamerTool"), "#582f87", "#3e1f61"),
            ("Herramientas PDF", lambda: self.show_frame("PDFTools"), "#25978d", "#177870"),
            ("Extractor de Texto", lambda: self.show_frame("OCRTool"), "#d85803", "#ad4602"),
            ("Transcribir Audio a Texto", lambda: self.show_frame("TranscribeTool"), "#8e44ad", "#6c3483"),
            ("Editor de Metadatos", lambda: self.show_frame("MetadataTool"), "#4b4b4b", "#222222"),
            ("YouTube Downloader", lambda: self.show_frame("YouTubeTool"), "#cc0000", "#930d04"),
        ]
        
        # Índices en buttons_config que necesitan Tier-2 (OCR=5, Transcribir=6, YouTube=8)
        HEAVY_INDICES = {5, 6, 8}

        self._heavy_menu_btns = []   # guardamos refs para re-habilitarlos

        for i, (text, cmd, color, hover) in enumerate(buttons_config):
            btn = ctk.CTkButton(btns_frame, text=text, width=180, height=50,
                                fg_color=color, hover_color=hover,
                                font=("Roboto", 13, "bold"),
                                command=cmd)
            btn.grid(row=i//3, column=i%3, padx=20, pady=20)

            if i in HEAVY_INDICES:
                btn.configure(state="disabled", text=f"⏳ {text}")
                self._heavy_menu_btns.append((btn, text, color))

        # Arrancar el watcher que re-habilita los botones cuando Tier-2 está listo
        self.after(500, self._watch_tier2_ready)

    def _watch_tier2_ready(self):
        """Polling ligero: re-habilita los botones pesados cuando _tier2_listo se activa."""
        if _tier2_listo.is_set():
            for btn, original_text, color in self._heavy_menu_btns:
                try:
                    btn.configure(state="normal", text=original_text)
                except Exception:
                    pass
            self._heavy_menu_btns.clear()
        else:
            # Revisar de nuevo en 500 ms (no bloquea nada)
            self.after(500, self._watch_tier2_ready)

    # ==========================================================================
    #   DESTINOS: ruta por barra + botón "📂 Abrir" unificado
    # ==========================================================================
    def _ruta_destino(self, seg):
        """Carpeta elegida con "Elegir Otra..." en esa barra ('' si no hay)."""
        return self.dest_paths.get(seg, "")

    def _registrar_salida(self, seg, carpeta):
        if seg is not None and carpeta:
            self._salidas_recientes[seg] = carpeta

    def _abrir_en_explorador(self, carpeta):
        try:
            if os.name == 'nt':
                os.startfile(carpeta)
            else:
                subprocess.Popen(['xdg-open', carpeta])
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo abrir la carpeta:\n{carpeta}\n\n{e}")

    def _resolver_destino(self, seg):
        """Carpeta que corresponde a la opción actual de la barra (o None)."""
        info = self._destinos.get(seg, {})
        valor = seg.get() if seg is not None else ""
        carpeta_x = info.get("carpeta", "")
        try:
            archivos = [f for f in (info.get("archivos") or (lambda: []))() or [] if f]
        except Exception:
            archivos = []
        destino = None
        if "Elegir Otra" in valor:
            destino = self._ruta_destino(seg) or None
        elif archivos:
            base = os.path.dirname(os.path.abspath(archivos[0]))
            if carpeta_x and carpeta_x in valor:
                sub = os.path.join(base, carpeta_x)
                # Si aún no existe (se crea al procesar) se abre la carpeta de origen
                destino = sub if os.path.isdir(sub) else base
            else:
                destino = base
        if not destino or not os.path.isdir(destino):
            ultima = self._salidas_recientes.get(seg)
            destino = ultima if ultima and os.path.isdir(ultima) else None
        return destino

    def _abrir_destino(self, seg):
        destino = self._resolver_destino(seg)
        if not destino:
            messagebox.showinfo(
                "Abrir carpeta",
                "Todavía no hay una carpeta de destino.\n\n"
                "Agrega archivos (o elige una carpeta con \"Elegir Otra...\") y vuelve a intentarlo.")
            return
        self._abrir_en_explorador(destino)

    def _boton_abrir_destino(self, master, seg, carpeta, archivos_fn):
        """Botón "📂 Abrir" de una barra de destino (lo registra para el resolvedor)."""
        self._destinos[seg] = {"carpeta": carpeta, "archivos": archivos_fn}
        return ctk.CTkButton(master, text="📂 Abrir", width=78, height=28,
                             fg_color="#2b2b2b", hover_color="#3a3a3a",
                             border_width=1, border_color="#555",
                             command=lambda: self._abrir_destino(seg))

    def _abrir_carpeta_transcripciones(self, yt=False):
        """Abre en el explorador la carpeta donde se guardan las transcripciones."""
        # 1. Si ya se guardó algo, ir directo a esa carpeta
        last = getattr(self, 'trans_last_folder', '')
        if last and os.path.isdir(last):
            folder = last
        elif yt:
            # Default YT: ~/Downloads/Transcripciones_YT
            folder = os.path.join(os.path.expanduser("~"), "Downloads", "Transcripciones_YT")
        else:
            # Antes de procesar: la misma carpeta donde se guardará
            # (antes abría Descargas\TRANSCRIPCIONES aunque se guardara junto al archivo)
            folder = None
            seg = getattr(self, 'trans_dest_seg', None)
            if seg is not None:
                folder = self._resolver_destino(seg)
            if not folder:
                messagebox.showinfo(
                    "Abrir carpeta",
                    "Todavía no hay una carpeta de destino.\n\n"
                    "Agrega archivos (o elige una carpeta con \"Elegir Otra...\") y vuelve a intentarlo.")
                return

        # 2. Crear si no existe y abrir
        os.makedirs(folder, exist_ok=True)
        try:
            if os.name == 'nt':
                os.startfile(folder)
            else:
                subprocess.Popen(['xdg-open', folder])
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo abrir la carpeta:\n{folder}\n\n{e}")


    # ==========================================================================
    #   SECCIÓN 2: GESTOR DE ARCHIVOS Y CANDADO (DRAG & DROP GENERAl)
    # ==========================================================================
    def analyze_gpu_hardware(self, is_video=False):
        """
        Analiza la GPU. 
        - is_video=True: Muestra advertencias de AV1 en series 2000/3000.
        - is_video=False: Solo verifica potencia (CUDA) sin mencionar AV1.
        """
        if not torch.cuda.is_available():
            return False, "NO DETECTADA ❌ (Probablemente AMD/Intel o Drivers faltantes)", "#c92c2c"

        try:
            name = torch.cuda.get_device_name(0).upper()
        except:
            name = "UNKNOWN GPU"

        # 1. Casos "Raros" (Workstation, Server) -> GRIS, PERO ACTIVABLE MANUALMENTE
        special_cards = ["QUADRO", "TESLA", "RTX A", "T1000", "T600", "A2000", "A4000", "A5000", "A6000", "L40"]
        if any(x in name for x in special_cards):
            # ANTES: False (Bloqueado) -> AHORA: True (Para que el botón funcione)
            return True, f"{name} (No probado - Manual)", "gray"

        # 2. Detección Numérica (GeForce / RTX)
        import re
        nums = re.findall(r'\d{4}', name)
        
        if nums:
            model_num = int(nums[0])
            
            # --- CASO: 4000 o SUPERIOR (Verde, Full) ---
            if model_num >= 4000:
                return True, f"{name} (DETECTADA ✅)", "#2cc985"
            
            # --- CASO: 2000 o 3000 (Amarillo) ---
            elif 2000 <= model_num < 4000:
                if is_video:
                    return True, f"{name} (No recomendada para AV1 ⚠️)", "#f1c40f"
                else:
                    return True, f"{name} (DETECTADA - Compatible)", "#f1c40f"
            
            # --- CASO: 1600 o MENOR (Rojo, Manual) ---
            elif model_num < 2000:
                # ANTES: False -> AHORA: True (Para que el botón funcione)
                return True, f"{name} (Legacy - Manual)", "#c92c2c"
        
        # 3. Fallback antiguas (3 dígitos) -> SIGUE BLOQUEADO
        nums_3 = re.findall(r'\d{3}', name)
        if nums_3:
             return False, f"{name} (Antigua/No soportada)", "#c92c2c"

        return False, f"{name} (Genérica/No probada)", "gray"


    def handle_drop(self, event, label_widget, drop_widget):
        """Procesa archivos soltados (CORREGIDO: Sin bloqueo por path)"""
        # 1. Rutas soltadas (lista Tcl: rutas con espacios entre llaves, mezcladas con simples)
        clean_files = self._rutas_drop(event)

        accepted_files = []
        rejected_count = 0

        # 2. Filtrado por extensión según el MODO (Sin checar os.path.exists aquí para no bloquear)
        for file_path in clean_files:
            # Limpieza básica de comillas por si Windows las manda
            file_path = file_path.strip('"')
            
            ext = os.path.splitext(file_path)[1].lower()
            
            is_valid = False
            if self.mode == "video":
                if ext in VALID_VIDEO_EXT: is_valid = True
            elif self.mode == "image":
                if ext in VALID_IMAGE_EXT: is_valid = True
            elif self.mode == "audio":
                if ext in VALID_AUDIO_EXT: is_valid = True
            elif self.mode == "ocr":
                if ext in VALID_IMAGE_EXT or ext in VALID_PDF_EXT: is_valid = True
            elif self.mode == "transcribe":
                # Acepta Audio Y Video
                if ext in VALID_AUDIO_EXT or ext in VALID_VIDEO_EXT: is_valid = True

            if is_valid:
                accepted_files.append(file_path)
            else:
                rejected_count += 1

        # 3. Actualizar UI (Si hay archivos válidos)
        if accepted_files:
            self.file_queue = accepted_files
            
            # Forzar actualización en el widget correcto
            target_drop = drop_widget
            target_lbl = label_widget
            
            # Parche por si el puntero se perdió en algún cambio de frame
            if self.mode == "transcribe":
                target_drop = self.trans_drop_area
                target_lbl = self.trans_list_label
            
            self.update_file_list_ui(target_drop, target_lbl)
            
            if rejected_count > 0:
                current = target_lbl.cget("text").split("(")[0]
                target_lbl.configure(text=f"{current} ({rejected_count} inválidos)", text_color="orange")

    def select_files(self, file_types, label_widget, drop_widget):
        files = filedialog.askopenfilenames(filetypes=file_types)
        if files:
            self.file_queue = list(files)
            self.update_file_list_ui(drop_widget, label_widget)

    @staticmethod
    def _elidir_medio(texto, maximo):
        """Recorta por el medio conservando el final (la extensión del archivo)."""
        texto = str(texto)
        if len(texto) <= maximo:
            return texto
        cola = max(8, maximo // 3)
        return texto[:maximo - cola - 1] + "…" + texto[-cola:]

    def update_file_list_ui(self, drop_widget, label_widget):
        count = len(self.file_queue)
        # El OCR usa una lista compacta de 2 líneas como máximo: la zona de
        # arrastre es de alto fijo y nunca empuja los botones fuera de la ventana
        compacto = self.mode == "ocr" and drop_widget is getattr(self, "ocr_drop_btn", None)
        if compacto:
            self._ocr_reiniciar_estado()
        if count == 0:
            label_widget.configure(text="Ningún archivo válido seleccionado", text_color="gray")
            if compacto:
                drop_widget.configure(text=OCR_TEXTO_DROP_VACIO)
            else:
                drop_widget.configure(text="📂 Arrastra archivos aquí\n(o click para buscar)")
        else:
            label_widget.configure(text=f"{count} archivo{'s' if count != 1 else ''} listo{'s' if count != 1 else ''}",
                                   text_color="#2cc985")
            if compacto:
                nombres = [self._elidir_medio(os.path.basename(f), 64) for f in self.file_queue[:2]]
                if count <= 2:
                    text_show = "\n".join(f"📄 {n}" for n in nombres)
                else:
                    text_show = f"📄 {nombres[0]}\n… y {count-1} más"
            else:
                names = [os.path.basename(f) for f in self.file_queue[:3]]
                text_show = "\n".join(names)
                if count > 3: text_show += f"\n... y {count-3} más"
            drop_widget.configure(text=text_show)
            if self.mode == "ocr" and label_widget is getattr(self, "ocr_list_lbl", None):
                self._ocr_analizar_cola()

    def on_dest_change(self, value, label_widget, segment_widget):
        # 1. Recuperar el estado anterior de ESTE botón específico
        #    (Si no existe historial, asumimos que estaba en "Misma Carpeta")
        prev_val = self.previous_dest_selections.get(segment_widget, "📄 Misma Carpeta")

        if "Elegir Otra" in value:
            # El usuario eligió buscar carpeta
            path = filedialog.askdirectory()
            
            if path:
                # A) Eligió una carpeta: se guarda para ESTA barra
                self.dest_paths[segment_widget] = path
                self.custom_dest_path = path
                label_widget.configure(text=f"Ruta: {path}")
                self.previous_dest_selections[segment_widget] = value
            else:
                # B) Canceló: Regresamos a lo que estaba seleccionado ANTES
                segment_widget.set(prev_val)
                
                # Si regresamos a una opción que no es "Elegir Otra", limpiamos la ruta custom
                if "Elegir Otra" not in prev_val:
                    self.dest_paths.pop(segment_widget, None)
                    label_widget.configure(text="")
                else:
                    # Se conserva la carpeta que ya tenía esta barra
                    if self.dest_paths.get(segment_widget):
                        label_widget.configure(text=f"Ruta: {self.dest_paths[segment_widget]}")

        else:
            # El usuario eligió una opción predefinida (Misma Carpeta o Carpeta X)
            # Guardamos esta selección como la nueva "Anterior" para el futuro
            self.previous_dest_selections[segment_widget] = value
            
            self.dest_paths.pop(segment_widget, None)
            self.custom_dest_path = ""
            label_widget.configure(text="")

    def _lote(self):
        """
        El lote del hilo actual. Gracias a esto 'cancel_requested' y
        'current_process' son de CADA módulo: si conviertes video mientras
        comprimes imágenes, cancelar uno no toca al otro.
        """
        suelto = getattr(self, "_lote_suelto", None)
        if suelto is None:
            suelto = self._lote_suelto = LoteTrabajo("suelto")
        return getattr(getattr(self, "_lote_hilo", None), "actual", None) or suelto

    def lote_de(self, modo):
        """El lote en curso de ese módulo, o None si no está trabajando."""
        return getattr(self, "_lotes", {}).get(modo)

    def _lote_objetivo(self, modo=None):
        """
        Sobre qué lote actúa un botón: el indicado, el del hilo actual o, si no,
        el del módulo que está en pantalla.
        """
        if modo:
            return self.lote_de(modo)
        actual = self._lote()
        if actual is not None and actual.modo != "suelto":
            return actual
        return self.lote_de(getattr(self, "mode", None))

    def _correr_lote(self, lote):
        """Hilo del lote: deja el lote a mano para todo lo que corra dentro."""
        self._lote_hilo.actual = lote
        try:
            self.run_batch_process(lote)
        except Exception as e:
            print(f"[Lote {lote.modo}] Error inesperado: {e}")
        finally:
            self._lote_hilo.actual = None
            self._lotes.pop(lote.modo, None)

    # Widgets de cada módulo, POR NOMBRE: se buscan solo los del módulo pedido
    # (los demás pueden no existir todavía, los frames se construyen al entrar).
    _WIDGETS_LOTE = {
        "video": ("video_convert_btn", "video_drop_area", "video_cancel_btn",
                  "video_counter_label", "video_progress_bar", "video_status_label"),
        "image": ("image_convert_btn", "image_drop_area", "image_cancel_btn",
                  "image_counter_label", "image_progress_bar", "image_status_label"),
        "audio": ("audio_convert_btn", "audio_drop_area", "audio_cancel_btn",
                  "audio_counter_label", "audio_progress_bar", "audio_status_label"),
        "ocr": ("ocr_btn", "ocr_drop", "ocr_cancel",
                "ocr_counter", "ocr_progress", "ocr_status"),
        "transcribe": ("trans_btn", "trans_drop_area", "trans_cancel",
                       "trans_counter", "trans_progress", "trans_status"),
    }

    def _widgets_lote(self, modo):
        """(iniciar, zona_drop, cancelar, contador, barra, estado) de ese módulo."""
        nombres = self._WIDGETS_LOTE.get(modo)
        if not nombres:
            return None
        try:
            return tuple(getattr(self, n) for n in nombres)
        except AttributeError as e:
            print(f"[Lote {modo}] Todavía no existe un widget necesario: {e}")
            return None

    def _despertar_carril_ia(self):
        """Avisa a los que esperan turno de IA (alguien canceló)."""
        try:
            with self.carril_ia._cond:
                self.carril_ia._cond.notify_all()
        except Exception:
            pass

    def start_batch_thread(self, mode_type):
        # Un lote por módulo: el mismo módulo no arranca dos veces, pero otros
        # módulos SÍ pueden estar trabajando al mismo tiempo.
        if mode_type in self._lotes:
            return
        if not self.file_queue:
            return
        if self._widgets_lote(mode_type) is None:
            return
        lote = LoteTrabajo(mode_type, self.file_queue)
        self._lotes[mode_type] = lote

        # Feedback visual inmediato (el reloj vuelve a dorado: el verde es solo el "Total")
        if mode_type == "transcribe":
            self.timer_running = False
            self.trans_time_lbl.configure(text="⏳ Cargando...", text_color="#d4ac0d")

        lote.hilo = threading.Thread(target=self._correr_lote, args=(lote,),
                                     name=f"dmt_lote_{mode_type}", daemon=True)
        lote.hilo.start()

    def cancelar_cola(self, modo=None):
        """CANCELAR: deja terminar el archivo actual y no procesa el resto de la cola."""
        lote = self._lote_objetivo(modo)
        if lote is None or lote.modo == "suelto":
            return
        lote.cortar = True
        self._despertar_carril_ia()
        if lote.modo == "image":
            try:
                self.image_cancel_btn.configure(state="disabled")
                self.image_status_label.configure(text="⏹ Cancelando: termina la imagen actual…",
                                                  text_color="orange")
            except Exception:
                pass
    
    def update_batch_timer(self):
        if self.timer_running:
            if self.timer_start_time is None:
                # Aún no empieza a procesar (cargando modelo)
                self.trans_time_lbl.configure(text="⏱️ Cargando...")
            else:
                # Ya está procesando, calcular diferencia
                elapsed = int(time.time() - self.timer_start_time)
                h = elapsed // 3600
                m = (elapsed % 3600) // 60
                s = elapsed % 60
                self.trans_time_lbl.configure(text=f"⏱️ {h:02}:{m:02}:{s:02}")
            
            # Repetir cada 1 segundo
            self.after(1000, self.update_batch_timer)
    
    def run_batch_process(self, lote=None):
        lote = lote or self._lote()
        modo = lote.modo

        # 1. Identificar qué UI manipular según el módulo de ESTE lote
        widgets = self._widgets_lote(modo)
        if widgets is None:
            return
        btn_start, drop_area, btn_cancel, counter_lbl, progress_bar, status_lbl = widgets

        # 2. Bloquear UI (este método corre en un hilo: los widgets se tocan con _en_ui)
        self._en_ui(btn_start.configure, state="disabled")
        self._en_ui(drop_area.configure, state="disabled")
        self._en_ui(btn_cancel.configure, state="normal")
        if modo == "ocr":
            self._ocr_bloquear_controles(True)
            self._ocr_lote_iniciar(len(lote.cola))

        cola = list(lote.cola)
        total = len(cola)
        report = []

        # 3. Carril de IA: OCR y Transcripción no pueden trabajar a la vez (dos
        # modelos grandes saturan RAM/VRAM). El que llega después espera turno.
        clave_ia = {"ocr": "ocr", "transcribe": "whisper"}.get(modo)

        def _avisar_espera(quien):
            texto = f"⏳ Esperando a que termine {quien}…"
            if modo == "ocr":
                self._ocr_fase("esperando", quien)
            else:
                self._en_ui(status_lbl.configure, text=texto, text_color="#d4ac0d")
            print(f"[Carril IA] {LoteTrabajo.NOMBRES.get(modo, modo)} espera a {quien}.")

        carril = (self.carril_ia.turno(clave_ia, LoteTrabajo.NOMBRES.get(modo, modo),
                                       on_espera=_avisar_espera,
                                       debe_cortar=lambda: lote.cortar)
                  if clave_ia else contextlib.nullcontext())

        try:
            with carril:
                # El modelo de IA del módulo (OCR / Whisper) no se libera mientras dure el lote
                with self._uso_modelo_para_modo(modo):
                    # Timer global solo para transcribe (un único loop)
                    if modo == "transcribe":
                        self.timer_start_time = time.time()
                        self.timer_running = True
                        self._en_ui(self.update_batch_timer)

                    # 4. Iterar archivos
                    for i, path in enumerate(cola):
                        if lote.cortar:
                            # CANCELAR: el archivo anterior ya terminó; el resto no se procesa
                            for resto in cola[i:]:
                                report.append(f"{os.path.basename(resto)}: ⏹ CANCELADO (no se procesó)")
                            break

                        current_progress = i / total

                        if modo in ["image", "audio"]:
                            self._en_ui(progress_bar.set, current_progress)
                        elif modo == "ocr":
                            self._ocr_lote_idx = i
                            self._ocr_progreso_real(0, 1)
                        else:
                            self._en_ui(progress_bar.set, 0)

                        name = os.path.basename(path)
                        short_name = (name[:28] + "…") if len(name) > 29 else name

                        self._en_ui(counter_lbl.configure, text=f"{i+1}/{total}  —  {short_name}")
                        if modo == "ocr":
                            self._ocr_fase("preparando")
                        elif not lote.cortar:
                            self._en_ui(status_lbl.configure, text=f"Procesando: {short_name}",
                                        text_color="white")

                        # Limpieza de RAM cada 25 archivos
                        if i % 25 == 0:
                            gc.collect()
                            time.sleep(0.02)

                        # --- SELECCIONAR LÓGICA ESPECÍFICA ---
                        success = False
                        msg = "Error desconocido"

                        try:
                            if modo == "video":
                                success, msg = self.convert_video_logic(path)
                            elif modo == "image":
                                success, msg = self.convert_image_logic(path)
                            elif modo == "audio":
                                success, msg = self.convert_audio_logic(path)
                            elif modo == "ocr":
                                success, msg = self.convert_ocr_logic(path)
                            elif modo == "transcribe":
                                res_tuple = self.convert_transcribe_logic(path)
                                if len(res_tuple) == 3:
                                    success, msg, time_taken = res_tuple
                                    if success and time_taken: msg = f"{msg} ({time_taken})"
                                else:
                                    success, msg = res_tuple
                        except Exception as e:
                            success = False
                            msg = f"Excepción Crítica: {str(e)}"

                        # Checar cancelación (SALTAR: se salta este archivo, sigue la cola)
                        if lote.saltar:
                            detalle = (msg or "").strip()
                            if detalle.upper().startswith("CANCELADO"):
                                detalle = detalle[len("CANCELADO"):].strip(" :·")
                            else:
                                detalle = ""
                            report.append(f"{name}: SALTADO" + (f" ({detalle})" if detalle else ""))
                            if modo == "ocr":
                                self._ocr_fase("saltado")
                            else:
                                self._en_ui(status_lbl.configure, text="Saltado", text_color="orange")
                            lote.saltar = False
                            time.sleep(0.5)
                            continue

                        # Guardar reporte (video y OCR detallan qué motor se usó)
                        if success:
                            detalle = (msg or "").strip().lstrip("✅").strip()
                            if modo in ("video", "ocr") and detalle and "COMPLETADO" not in detalle:
                                report.append(f"{name}: ✅ {detalle}")
                            else:
                                report.append(f"{name}: ✅ OK")
                        else:
                            report.append(f"{name}: ❌ {msg}")
                            print(f"Error en {name}: {msg}")
        except _TrabajoDetenido:
            # Se canceló mientras esperaba turno en el carril de IA
            for resto in cola:
                report.append(f"{os.path.basename(resto)}: ⏹ CANCELADO (no se procesó)")

        # 5. Restaurar UI
        cancelado = bool(lote.cortar)
        if modo == "transcribe":
            self.timer_running = False
        if modo == "ocr":
            self._ocr_lote_terminar(errores=sum(1 for r in report if "❌" in r))
            self.ocr_motor.vaciar_cache()          # libera la VRAM que Paddle dejo en cache
            self._ocr_bloquear_controles(False)

        if modo == "transcribe" and getattr(self, 'timer_start_time', None):
            elapsed = int(time.time() - self.timer_start_time)
            h, m, s = elapsed // 3600, (elapsed % 3600) // 60, elapsed % 60
            self._en_ui(self.trans_time_lbl.configure,
                        text=f"⏱️ Total: {h:02}:{m:02}:{s:02}", text_color="#2cc985")

        self._en_ui(btn_start.configure, state="normal")
        self._en_ui(drop_area.configure, state="normal")
        self._en_ui(btn_cancel.configure, state="disabled")

        # Finalizar al 100%
        hechos = sum(1 for r in report if "CANCELADO (no se procesó)" not in r)
        self._en_ui(progress_bar.set, 1)
        if cancelado:
            self._en_ui(counter_lbl.configure,
                        text=f"Cancelado ({hechos} de {total} archivo{'s' if total != 1 else ''})")
        else:
            self._en_ui(counter_lbl.configure,
                        text=f"¡Finalizado! ({total} archivo{'s' if total != 1 else ''})")
        if modo != "ocr":      # el OCR ya dejó su chip en "Listo" (o con errores)
            if cancelado:
                self._en_ui(status_lbl.configure, text="⏹ CANCELADO", text_color="orange")
            else:
                self._en_ui(status_lbl.configure, text=" ✅ COMPLETADO ", text_color="#2cc985")

        self._en_ui(self.show_summary, report, LoteTrabajo.NOMBRES.get(modo, modo))
        gc.collect() # Limpieza final
    # ==========================================================================
    #   SECCIÓN 3: MÓDULO DE VIDEO (EXISTENTE)
    # ==========================================================================

    # ... código anterior (por ejemplo, el final de init_menu_module u otro) ...

    # ==================================================================
    #   PESTAÑAS DEL CONVERSOR DE VIDEO
    # ==================================================================


    def init_video_module(self):
        self.converter_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.frames["VideoConverter"] = self.converter_frame
        
        self.video_submode = "convert"
        self.vid_files_conv = []
        self.vid_files_comp = []
        self.vid_files_ext = []

        # --- HEADER ---
        top = ctk.CTkFrame(self.converter_frame, fg_color="transparent")
        top.pack(fill="x", padx=20, pady=10)
        ctk.CTkButton(top, text="← Menú", width=80, fg_color="transparent", border_width=1, 
                      command=lambda: self.show_frame("Menu")).pack(side="left")
        
        title_bg = ctk.CTkFrame(self.converter_frame, fg_color="#2b2b2b", corner_radius=8)
        title_bg.pack(pady=5)
        ctk.CTkLabel(title_bg, text="Convertidor de Videos", font=(self.main_font, 22, "bold"), text_color="#2599f2", bg_color="#2b2b2b").pack(padx=15, pady=8)

        # ==============================================================================
        # 🔥 EL CAMBIO ESTÁ AQUÍ:
        # 1. Definimos 'width=1000' (Un buen tamaño ancho pero limitado).
        # 2. En el .pack(), usamos 'fill="y"' (estira solo vertical) y QUITAMOS 'fill="x"'.
        #    Esto centra el cuadro y evita que toque las paredes laterales.
        # ==============================================================================
        self.vid_tabs = ctk.CTkTabview(self.converter_frame, width=850, height=600, fg_color="#222",
                                       segmented_button_selected_color="#1f6aa5",
                                       segmented_button_selected_hover_color="#144870")
        
        self.vid_tabs.pack(pady=10, expand=True, fill="y") # <--- Centrado y altura dinámica, ancho fijo.
        
        self.vid_tabs.add("Convertir Formato")
        self.vid_tabs.add("Reducir Tamaño")
        self.vid_tabs.add("Extraer Audio")

        # ==============================================================================
        # TAB 1: CONVERTIDOR (AZUL)
        # ==============================================================================
        t1 = self.vid_tabs.tab("Convertir Formato")
        
        self.v_conv_lbl = ctk.CTkLabel(t1, text="Ningún archivo válido seleccionado", text_color="gray")
        self.v_conv_lbl.pack(pady=(5,0))
        self.v_conv_drop = ctk.CTkButton(t1, text=self._VID_TEXTO_DROP["convert"], width=600, height=70,
                                         fg_color="#252525", hover_color="#303030", border_color="#1f6aa5", border_width=2,
                                         command=lambda: self.select_video_files("convert"))
        self.v_conv_drop.pack(pady=10)
        self.v_conv_drop.drop_target_register(DND_FILES)
        self.v_conv_drop.dnd_bind('<<Drop>>', lambda e: self.handle_video_drop(e, "convert"))

        # Opciones
        opts1 = ctk.CTkFrame(t1, fg_color="transparent")
        opts1.pack(pady=5)
        ctk.CTkLabel(opts1, text="Formato Salida:").pack(side="left", padx=5)
        self.v_conv_fmt = ctk.StringVar(value="mp4 (H.264)")
        ctk.CTkOptionMenu(opts1, values=["mp4 (H.264)", "mp4 (H.265)", "mp4 (AV1)", "mkv (AV1)", "mov", "avi", "wmv"], 
                          variable=self.v_conv_fmt, width=150).pack(side="left", padx=10)
        ctk.CTkLabel(opts1, text="Resolución:").pack(side="left", padx=(20, 5))
        self.v_conv_res = ctk.StringVar(value=VID_RES_OPCIONES[0])
        ctk.CTkOptionMenu(opts1, values=VID_RES_OPCIONES, variable=self.v_conv_res,
                          width=150).pack(side="left", padx=5)
        opts1_gpu = ctk.CTkFrame(t1, fg_color="transparent")
        opts1_gpu.pack(pady=(0, 5))
        
        # --- ESTILO GPU OCR (VIDEO CONVERTER) ---
        # --- ESTILO GPU INTELIGENTE (VIDEO CONVERTER) ---
        # --- ESTILO GPU INTELIGENTE (VIDEO CONVERTER) ---
        gpu_active, gpu_text, gpu_col = self.analyze_gpu_hardware(is_video=True)

        gpu_frame = ctk.CTkFrame(opts1_gpu, fg_color="transparent")
        gpu_frame.pack(side="left", padx=20)

        # Lógica Default: Solo ON si es Verde (#2cc985) o Amarillo (#f1c40f)
        # Las Rojas/Grises vendrán en OFF, pero se podrán activar.
        default_on = gpu_active and (gpu_col == "#2cc985" or gpu_col == "#f1c40f")

        self.v_conv_gpu = ctk.BooleanVar(value=default_on)
        
        # Estado del botón: Si gpu_active es True, el usuario puede hacer click.
        state_switch = "normal" if gpu_active else "disabled"

        self.switch_conv_gpu = ctk.CTkSwitch(gpu_frame, text="Aceleración GPU", variable=self.v_conv_gpu, 
                                             progress_color="#1f6aa5", state=state_switch)
        self.switch_conv_gpu.pack(side="left", padx=5)
        
        self.conv_gpu_status_lbl = ctk.CTkLabel(gpu_frame, text="Estado: Detectando tarjeta gráfica...", font=("Arial", 10, "bold"), text_color="#888888")
        self.conv_gpu_status_lbl.pack(side="left", padx=5)
        # Rehacer la deteccion a mano (si cambiaste de tarjeta, de driver o de FFmpeg)
        self.btn_redetectar_gpu = ctk.CTkButton(
            gpu_frame, text="↻ Re-detectar", width=110, height=24,
            font=("Arial", 11), fg_color="#333", hover_color="#444",
            command=self.redetectar_gpu)
        self.btn_redetectar_gpu.pack(side="left", padx=(10, 0))
        
        # self.v_conv_gpu = ctk.BooleanVar(value=torch.cuda.is_available())
        # ctk.CTkSwitch(opts1, text="Usar GPU", variable=self.v_conv_gpu, progress_color="#1f6aa5").pack(side="left", padx=20)

        # Destino
        dest1 = ctk.CTkFrame(t1, fg_color="transparent")
        dest1.pack(pady=5)
        ctk.CTkLabel(dest1, text="Guardar en:").pack(pady=2)
        self.v_conv_dest_var = ctk.StringVar(value="📄 Misma Carpeta")
        fila_v_conv = ctk.CTkFrame(dest1, fg_color="transparent")
        fila_v_conv.pack()
        self.v_conv_dest_seg = ctk.CTkSegmentedButton(fila_v_conv, values=["📄 Misma Carpeta", "📁 Carpeta 'VIDEO_CONV'", "↗️ Elegir Otra..."],
                                                      variable=self.v_conv_dest_var, selected_color="#1f6aa5",
                                                      command=lambda v: self.on_dest_change(v, self.v_conv_path_lbl, self.v_conv_dest_seg))
        self.v_conv_dest_seg.pack(side="left")
        self._boton_abrir_destino(fila_v_conv, self.v_conv_dest_seg, "VIDEO_CONV",
                                  lambda: self.vid_files_conv).pack(side="left", padx=(8, 0))
        self.v_conv_path_lbl = ctk.CTkLabel(dest1, text="", text_color="gray", font=("Arial", 10))
        self.v_conv_path_lbl.pack()

        # Controles Acción T1
        self.p_frame_conv = ctk.CTkFrame(t1, fg_color="transparent")
        self.p_frame_conv.pack(fill="x", padx=50, pady=10)
        self.lbl_counter_conv = ctk.CTkLabel(self.p_frame_conv, text="", font=(self.main_font, 14, "bold"))
        self.lbl_counter_conv.pack()
        self.p_bar_conv = ctk.CTkProgressBar(self.p_frame_conv, width=500, height=15, progress_color="#1f6aa5")
        self.p_bar_conv.set(0)
        self.p_bar_conv.pack(pady=5)
        self.lbl_status_conv = ctk.CTkLabel(self.p_frame_conv, text="Listo", text_color="gray")
        self.lbl_status_conv.pack()

        acts1 = ctk.CTkFrame(t1, fg_color="transparent")
        acts1.pack(pady=5)
        self.btn_start_conv = ctk.CTkButton(acts1, text="INICIAR CONVERSIÓN", height=45, width=220, fg_color="#1f6aa5", hover_color="#144870",
                      font=(self.main_font, 14, "bold"), command=lambda: self.start_video_wrapper("convert"))
        self.btn_start_conv.pack(side="left", padx=10)
        self.btn_cancel_conv = ctk.CTkButton(acts1, text="SALTAR", height=45, width=150, fg_color="#c92c2c", hover_color="#992222", 
                                             state="disabled", command=lambda: self.cancel_current_process("video"))
        self.btn_cancel_conv.pack(side="left", padx=10)


        # ==============================================================================
        # TAB 2: REDUCTOR (VERDE)
        # ==============================================================================
        t2 = self.vid_tabs.tab("Reducir Tamaño")
        
        self.v_comp_lbl = ctk.CTkLabel(t2, text="Ningún archivo válido seleccionado", text_color="gray")
        self.v_comp_lbl.pack(pady=(5,0))
        self.v_comp_drop = ctk.CTkButton(t2, text=self._VID_TEXTO_DROP["compress"], width=600, height=70,
                                         fg_color="#252525", hover_color="#303030", border_color="#2cc985", border_width=2,
                                         command=lambda: self.select_video_files("compress"))
        self.v_comp_drop.pack(pady=10)
        self.v_comp_drop.drop_target_register(DND_FILES)
        self.v_comp_drop.dnd_bind('<<Drop>>', lambda e: self.handle_video_drop(e, "compress"))

        opts2 = ctk.CTkFrame(t2, fg_color="#181818", corner_radius=10)
        opts2.pack(pady=6, ipadx=30)
        
        r2_1 = ctk.CTkFrame(opts2, fg_color="transparent")
        r2_1.pack(pady=5)
        ctk.CTkLabel(r2_1, text="Códec:").pack(side="left", padx=5)
        self.v_comp_codec = ctk.StringVar(value="H.265 (HEVC)")
        ctk.CTkOptionMenu(r2_1, values=["H.265 (HEVC)", "AV1 (Ultra Eficiente)"], 
                          variable=self.v_comp_codec, width=160, 
                          fg_color="#2cc985", button_color="#1e8f5e", text_color="black").pack(side="left", padx=10)
        
        self.v_comp_audio = ctk.BooleanVar(value=True)
        ctk.CTkSwitch(r2_1, text="Mantener Audio", variable=self.v_comp_audio, progress_color="#2cc985").pack(side="left", padx=20)

        r2_2 = ctk.CTkFrame(opts2, fg_color="transparent")
        r2_2.pack(pady=5)
        ctk.CTkLabel(r2_2, text="Nivel:").pack(side="left", padx=5)
        self.compression_levels = [
            "1. Extrema (Calidad Baja - Mínimo Peso)",
            "2. Alta Compresión (Calidad Aceptable)",
            "3. Equilibrado (Recomendado)",
            "4. Alta Calidad (Poca reducción)",
            "5. Casi sin Pérdida (Máximo Peso)"
        ]
        self.v_comp_level = ctk.StringVar(value=self.compression_levels[2])
        ctk.CTkOptionMenu(r2_2, values=self.compression_levels, variable=self.v_comp_level, width=300,
                          fg_color="#2cc985", button_color="#1e8f5e", text_color="black").pack(side="left", padx=10)
        ctk.CTkLabel(r2_2, text="Resolución:").pack(side="left", padx=(10, 5))
        self.v_comp_res = ctk.StringVar(value=VID_RES_OPCIONES[0])
        ctk.CTkOptionMenu(r2_2, values=VID_RES_OPCIONES, variable=self.v_comp_res, width=150,
                          fg_color="#2cc985", button_color="#1e8f5e", text_color="black").pack(side="left", padx=5)

        r2_3 = ctk.CTkFrame(opts2, fg_color="transparent")
        r2_3.pack(pady=5)
        
        # --- ESTILO GPU OCR (VIDEO COMPRESOR)---
        # --- ESTILO GPU INTELIGENTE (VIDEO COMPRESOR) ---
        # --- ESTILO GPU INTELIGENTE (VIDEO COMPRESOR) ---
        # Reusamos la lógica
        gpu_active, gpu_text, gpu_col = self.analyze_gpu_hardware(is_video=True)

        # Lógica Default: Solo ON si es Verde o Amarillo
        default_on = gpu_active and (gpu_col == "#2cc985" or gpu_col == "#f1c40f")

        self.v_comp_gpu = ctk.BooleanVar(value=default_on)
        state_switch = "normal" if gpu_active else "disabled"

        self.switch_comp_gpu = ctk.CTkSwitch(r2_3, text="Aceleración GPU", variable=self.v_comp_gpu, 
                                             progress_color="#2cc985", state=state_switch)
        self.switch_comp_gpu.pack(side="left", padx=5)
        
        self.comp_gpu_status_lbl = ctk.CTkLabel(r2_3, text="Estado: Detectando tarjeta gráfica...", font=("Arial", 10, "bold"), text_color="#888888")
        self.comp_gpu_status_lbl.pack(side="left", padx=5)
        # Destino T2
        dest2 = ctk.CTkFrame(t2, fg_color="transparent")
        dest2.pack(pady=5)
        ctk.CTkLabel(dest2, text="Guardar en:").pack(pady=2)
        self.v_comp_dest_var = ctk.StringVar(value="📄 Misma Carpeta")
        fila_v_comp = ctk.CTkFrame(dest2, fg_color="transparent")
        fila_v_comp.pack()
        self.v_comp_dest_seg = ctk.CTkSegmentedButton(fila_v_comp, values=["📄 Misma Carpeta", "📁 Carpeta 'VIDEO_REDUCIDO'", "↗️ Elegir Otra..."],
                                                      variable=self.v_comp_dest_var, selected_color="#2cc985",
                                                      text_color="black", unselected_color="#cccccc", unselected_hover_color="#eeeeee",
                                                      command=lambda v: self.on_dest_change(v, self.v_comp_path_lbl, self.v_comp_dest_seg))
        self.v_comp_dest_seg.pack(side="left")
        self._boton_abrir_destino(fila_v_comp, self.v_comp_dest_seg, "VIDEO_REDUCIDO",
                                  lambda: self.vid_files_comp).pack(side="left", padx=(8, 0))
        self.v_comp_path_lbl = ctk.CTkLabel(dest2, text="", text_color="gray", font=("Arial", 10))
        self.v_comp_path_lbl.pack()

        # Controles Acción T2
        self.p_frame_comp = ctk.CTkFrame(t2, fg_color="transparent")
        self.p_frame_comp.pack(fill="x", padx=50, pady=10)
        self.lbl_counter_comp = ctk.CTkLabel(self.p_frame_comp, text="", font=(self.main_font, 14, "bold"))
        self.lbl_counter_comp.pack()
        self.p_bar_comp = ctk.CTkProgressBar(self.p_frame_comp, width=500, height=15, progress_color="#2cc985")
        self.p_bar_comp.set(0)
        self.p_bar_comp.pack(pady=5)
        self.lbl_status_comp = ctk.CTkLabel(self.p_frame_comp, text="Listo", text_color="gray")
        self.lbl_status_comp.pack()

        acts2 = ctk.CTkFrame(t2, fg_color="transparent")
        acts2.pack(pady=5)
        self.btn_start_comp = ctk.CTkButton(acts2, text="INICIAR COMPRESIÓN", height=45, width=220, fg_color="#2cc985", hover_color="#1e8f5e", text_color="black",
                      font=(self.main_font, 14, "bold"), command=lambda: self.start_video_wrapper("compress"))
        self.btn_start_comp.pack(side="left", padx=10)
        self.btn_cancel_comp = ctk.CTkButton(acts2, text="SALTAR", height=45, width=150, fg_color="#c92c2c", hover_color="#992222", 
                                             state="disabled", command=lambda: self.cancel_current_process("video"))
        self.btn_cancel_comp.pack(side="left", padx=10)


        # ==============================================================================
        # TAB 3: EXTRACTOR (NARANJA)
        # ==============================================================================
        t3 = self.vid_tabs.tab("Extraer Audio")
        
        self.v_ext_lbl = ctk.CTkLabel(t3, text="Ningún archivo válido seleccionado", text_color="gray")
        self.v_ext_lbl.pack(pady=(5,0))
        self.v_ext_drop = ctk.CTkButton(t3, text=self._VID_TEXTO_DROP["extract"], width=600, height=70,
                                         fg_color="#252525", hover_color="#303030", border_color="#e67e22", border_width=2,
                                         command=lambda: self.select_video_files("extract"))
        self.v_ext_drop.pack(pady=10)
        self.v_ext_drop.drop_target_register(DND_FILES)
        self.v_ext_drop.dnd_bind('<<Drop>>', lambda e: self.handle_video_drop(e, "extract"))

        opts3 = ctk.CTkFrame(t3, fg_color="transparent")
        opts3.pack(pady=5, padx=30)
        ctk.CTkLabel(opts3, text="Formato de Audio:").pack(side="left", padx=5)
        self.v_ext_fmt = ctk.StringVar(value="mp3")
        audio_formats = ["mp3", "wav", "m4a (aac)", "m4a (alac)", "ac3", "aiff", "wma", "opus", "ogg", "flac"]
        ctk.CTkOptionMenu(opts3, values=audio_formats, variable=self.v_ext_fmt, 
                          width=180, fg_color="#e67e22", button_color="#d35400", text_color="black").pack(side="left", padx=10)

        # Destino T3
        dest3 = ctk.CTkFrame(t3, fg_color="transparent")
        dest3.pack(pady=5)
        ctk.CTkLabel(dest3, text="Guardar en:").pack(pady=2)
        self.v_ext_dest_var = ctk.StringVar(value="📄 Misma Carpeta")
        fila_v_ext = ctk.CTkFrame(dest3, fg_color="transparent")
        fila_v_ext.pack()
        self.v_ext_dest_seg = ctk.CTkSegmentedButton(fila_v_ext, values=["📄 Misma Carpeta", "📁 Carpeta 'VIDEO_AUDIO'", "↗️ Elegir Otra..."],
                                                     variable=self.v_ext_dest_var, selected_color="#e67e22",
                                                     text_color="black", unselected_color="#cccccc", unselected_hover_color="#eeeeee",
                                                     command=lambda v: self.on_dest_change(v, self.v_ext_path_lbl, self.v_ext_dest_seg))
        self.v_ext_dest_seg.pack(side="left")
        self._boton_abrir_destino(fila_v_ext, self.v_ext_dest_seg, "VIDEO_AUDIO",
                                  lambda: self.vid_files_ext).pack(side="left", padx=(8, 0))
        self.v_ext_path_lbl = ctk.CTkLabel(dest3, text="", text_color="gray", font=("Arial", 10))
        self.v_ext_path_lbl.pack()

        # Controles Acción T3
        self.p_frame_ext = ctk.CTkFrame(t3, fg_color="transparent")
        self.p_frame_ext.pack(fill="x", padx=50, pady=10)
        
        self.lbl_counter_ext = ctk.CTkLabel(self.p_frame_ext, text="", font=(self.main_font, 14, "bold"))
        self.lbl_counter_ext.pack()
        
        self.p_bar_ext = ctk.CTkProgressBar(self.p_frame_ext, width=500, height=15, progress_color="#e67e22")
        self.p_bar_ext.set(0)
        self.p_bar_ext.pack(pady=5)
        
        self.lbl_status_ext = ctk.CTkLabel(self.p_frame_ext, text="Listo", text_color="gray")
        self.lbl_status_ext.pack()

        acts3 = ctk.CTkFrame(t3, fg_color="transparent")
        acts3.pack(pady=5)
        self.btn_start_ext = ctk.CTkButton(acts3, text="EXTRAER AUDIO", height=45, width=220, fg_color="#e67e22", hover_color="#d35400", text_color="white",
                      font=(self.main_font, 14, "bold"), command=lambda: self.start_video_wrapper("extract"))
        self.btn_start_ext.pack(side="left", padx=10)
        self.btn_cancel_ext = ctk.CTkButton(acts3, text="SALTAR", height=45, width=150, fg_color="#c92c2c", hover_color="#992222", 
                                             state="disabled", command=lambda: self.cancel_current_process("video"))
        self.btn_cancel_ext.pack(side="left", padx=10)

        # Bridge
        self.video_list_label = self.v_conv_lbl
        self.video_drop_area = self.v_conv_drop
        self.video_convert_btn = self.btn_start_conv
        self.video_progress_bar = self.p_bar_conv
        self.video_status_label = self.lbl_status_conv
        self.video_counter_label = self.lbl_counter_conv
        self.video_cancel_btn = self.btn_cancel_conv

        # Reevaluar GPU cuando tier-2 (torch) termine de cargar
        self.after(500, self._poll_gpu_video_converter)
        
    def _poll_gpu_video_converter(self):
        """
        Polling ligero exclusivo del Conversor de Videos.
        Espera a que _tier2_listo se active (torch real cargado) y entonces
        reevalúa el hardware para actualizar switches y labels de GPU en
        Tab 1 (Convertir) y Tab 2 (Comprimir). Corre cada 500 ms hasta lograrlo.
        """
        if not _tier2_listo.is_set():
            self.after(500, self._poll_gpu_video_converter)
            return

        # Las pruebas reales de NVENC/NVDEC ya NO se lanzan aquí: se hacen la
        # primera vez que entras al módulo de video (_medir_gpu_video) y quedan
        # guardadas en disco, así abrir la app no cuesta esos segundos.

        # Tier-2 listo: reevaluar con el torch real
        gpu_active, gpu_text, gpu_col = self.analyze_gpu_hardware(is_video=True)
        default_on = gpu_active and (gpu_col == "#2cc985" or gpu_col == "#f1c40f")
        state_switch = "normal" if gpu_active else "disabled"

        # --- Actualizar Tab 1 (Convertir Formato) ---
        try:
            self.v_conv_gpu.set(default_on)
            self.switch_conv_gpu.configure(state=state_switch)
            self.conv_gpu_status_lbl.configure(
                text=f"Estado: {gpu_text}",
                text_color=gpu_col
            )
        except Exception as e:
            print(f"[poll_gpu_video] Tab1 error: {e}")

        # --- Actualizar Tab 2 (Reducir Tamaño) ---
        try:
            self.v_comp_gpu.set(default_on)
            self.switch_comp_gpu.configure(state=state_switch)
            self.comp_gpu_status_lbl.configure(
                text=f"Estado: {gpu_text}",
                text_color=gpu_col
            )
        except Exception as e:
            print(f"[poll_gpu_video] Tab2 error: {e}")

    _VID_TEXTO_DROP = {
        "convert": "📂 Arrastra VIDEOS para CONVERTIR",
        "compress": "📉 Arrastra VIDEOS para COMPRIMIR",
        "extract": "🎵 Arrastra VIDEOS para EXTRAER AUDIO",
    }

    def _video_pestana(self, submode):
        """(lista_attr, etiqueta, zona_drop, barra, estado, contador, cancelar, iniciar) de cada pestaña."""
        return {
            "convert": ("vid_files_conv", self.v_conv_lbl, self.v_conv_drop, self.p_bar_conv,
                        self.lbl_status_conv, self.lbl_counter_conv, self.btn_cancel_conv, self.btn_start_conv),
            "compress": ("vid_files_comp", self.v_comp_lbl, self.v_comp_drop, self.p_bar_comp,
                         self.lbl_status_comp, self.lbl_counter_comp, self.btn_cancel_comp, self.btn_start_comp),
            "extract": ("vid_files_ext", self.v_ext_lbl, self.v_ext_drop, self.p_bar_ext,
                        self.lbl_status_ext, self.lbl_counter_ext, self.btn_cancel_ext, self.btn_start_ext),
        }[submode]

    def _video_limpiar_listas(self):
        """Al entrar al módulo: sin archivos de una visita anterior (lo que se ve es lo que se procesa)."""
        for submode in ("convert", "compress", "extract"):
            attr, lbl, drop = self._video_pestana(submode)[:3]
            setattr(self, attr, [])
            lbl.configure(text="Ningún archivo válido seleccionado", text_color="gray")
            drop.configure(text=self._VID_TEXTO_DROP[submode])

    def _video_asignar(self, submode, archivos, rechazados=0):
        """Guarda la lista de ESA pestaña (cada pestaña tiene la suya) y la muestra."""
        attr, lbl, drop = self._video_pestana(submode)[:3]
        setattr(self, attr, list(archivos))
        self.file_queue = list(archivos)
        self.update_file_list_ui(drop, lbl)
        if rechazados:
            lbl.configure(text=f"{lbl.cget('text')} ({rechazados} inválidos)", text_color="orange")

    def select_video_files(self, submode):
        # Mismos formatos que se aceptan al arrastrar (antes faltaban m4v, mpeg, mpg, 3gp y ts)
        files = filedialog.askopenfilenames(filetypes=_filtro_videos())
        if files:
            self._video_asignar(submode, files)

    def handle_video_drop(self, event, submode):
        clean = self._rutas_drop(event)
        valid = [f for f in clean if f.lower().endswith(tuple(VALID_VIDEO_EXT))]
        self._video_asignar(submode, valid, rechazados=len(clean) - len(valid))

    def start_video_wrapper(self, submode):
        """Procesa SOLO la lista de la pestaña pulsada, con los widgets de esa pestaña."""
        if self.lote_de("video"):
            return       # ya hay una conversión de video en curso
        attr, lbl, drop, barra, estado, contador, cancelar, iniciar = self._video_pestana(submode)
        archivos = list(getattr(self, attr, []) or [])
        if not archivos:
            messagebox.showwarning("Vacío", "Selecciona videos primero.")
            return
        self.video_submode = submode
        self.file_queue = archivos
        self.video_list_label = lbl
        self.video_drop_area = drop
        self.video_progress_bar = barra
        self.video_status_label = estado
        self.video_counter_label = contador
        self.video_cancel_btn = cancelar
        self.video_convert_btn = iniciar
        self.start_batch_thread("video")

    # ------------------------------------------------------------------
    #   VIDEO: armado de comandos (rutas GPU / mixta / CPU con reintento)
    # ------------------------------------------------------------------
    @staticmethod
    def _vid_audio_args(ext, info, modo, keep_audio=True):
        """Audio lo más fiel posible: se COPIA cuando el contenedor lo acepta."""
        ac = info.get("acodec")
        if not ac:
            return []                                   # el archivo no trae audio
        if modo == "compress":
            if not keep_audio:
                return ["-an"]
            abr = info.get("abr")
            if ac == "aac" and (abr is None or abr <= 200_000):
                return ["-c:a", "copy"]                 # ya es AAC ligero: no se recodifica
            return ["-c:a", "aac", "-b:a", "192k"]
        # Convertir (fiel)
        if ext == "mkv":
            return ["-c:a", "copy"]
        if ext in ("mp4", "mov"):
            copiables = {"aac", "mp3", "ac3", "eac3", "alac"}
            if ext == "mov":
                copiables |= {"pcm_s16le", "pcm_s24le"}
            if ac in copiables:
                return ["-c:a", "copy"]
            kbps = (info.get("abr") or 320_000) / 1000
            br = "192k" if kbps <= 192 else ("256k" if kbps <= 256 else "320k")
            return ["-c:a", "aac", "-b:a", br]
        if ext == "avi":
            if ac in ("mp3", "ac3", "pcm_s16le"):
                return ["-c:a", "copy"]
            return ["-c:a", "libmp3lame", "-q:a", "0"]
        if ext == "wmv":
            if ac in ("wmav2", "wmav1"):
                return ["-c:a", "copy"]
            return ["-c:a", "wmav2", "-b:a", "192k"]
        return ["-c:a", "aac", "-b:a", "192k"]

    @staticmethod
    def _vid_pix(encoder, diez):
        """Formato de píxel de salida (H.264 SIEMPRE 8 bits 4:2:0)."""
        if encoder.endswith("_nvenc"):
            return "p010le" if (diez and encoder != "h264_nvenc") else "yuv420p"
        if encoder in ("libx265", "libsvtav1", "libaom-av1") and diez:
            return "yuv420p10le"
        return "yuv420p"

    @staticmethod
    def _vid_args_encoder(encoder, q, preset, caps):
        if encoder.endswith("_nvenc"):
            flags = caps["nvenc"].get(encoder) or ()
            return ["-c:v", encoder, "-preset", str(preset), "-rc", "vbr",
                    "-cq", str(q), "-b:v", "0", *flags]
        if encoder == "libx264":
            return ["-c:v", "libx264", "-preset", str(preset), "-crf", str(q)]
        if encoder == "libx265":
            return ["-c:v", "libx265", "-preset", str(preset), "-crf", str(q),
                    "-x265-params", "log-level=error"]
        if encoder == "libsvtav1":
            return ["-c:v", "libsvtav1", "-preset", str(preset), "-crf", str(q)]
        if encoder == "libaom-av1":
            return ["-c:v", "libaom-av1", "-crf", str(q), "-b:v", "0",
                    "-cpu-used", "4", "-row-mt", "1"]
        if encoder == "mpeg4":
            return ["-c:v", "mpeg4", "-q:v", "2", "-tag:v", "XVID"]
        if encoder == "wmv2":
            return ["-c:v", "wmv2", "-q:v", "2"]
        return ["-c:v", encoder]

    @staticmethod
    def _vid_gpu_total_posible(info):
        """¿Se puede NVDEC -> scale_cuda -> NVENC sin bajar cuadros a la RAM?"""
        vc = info.get("vcodec")
        if not info.get("ok") or vc not in NVDEC_CODECS:
            return False
        if info.get("rotado"):
            return False            # la rotación la aplica FFmpeg en la ruta mixta
        bits = info.get("bits") or 8
        if info.get("croma") != "420" or bits not in (8, 10):
            return False
        if vc == "h264" and bits != 8:
            return False            # H.264 de 10 bits: NVDEC solo desde la serie 50
        return True

    def _vid_comando(self, decod, encoder, src, out, plan, info, caps):
        cmd = ["ffmpeg", "-y", "-hide_banner", "-nostdin"]
        if decod == "gpu_total":
            cmd += ["-hwaccel", "cuda", "-hwaccel_output_format", "cuda"]
        elif decod == "gpu_dec":
            cmd += ["-hwaccel", "cuda"]
        cmd += ["-i", src]

        if decod == "copia":
            cmd += ["-c:v", "copy"]
        else:
            dims = plan["dims"]
            nvenc = encoder.endswith("_nvenc")
            diez = plan["diez"] and (not nvenc or caps["nvenc10"].get(encoder, False))
            if decod == "gpu_total":
                partes = []
                if dims:
                    partes += [f"w={dims[0]}", f"h={dims[1]}", "interp_algo=lanczos"]
                if (info.get("bits") or 8) >= 10 and not diez:
                    partes.append("format=nv12")      # 10 -> 8 bits dentro de la GPU
                # passthrough=0: el filtro entrega cuadros propios y NVENC no agota
                # el pool limitado del decodificador (lookahead / B-frames)
                partes.append("passthrough=0")
                cmd += ["-vf", "scale_cuda=" + ":".join(partes)]
            else:
                if dims:
                    cmd += ["-vf", f"scale={dims[0]}:{dims[1]}:flags=lanczos"]
                cmd += ["-pix_fmt", self._vid_pix(encoder, diez)]
            cmd += self._vid_args_encoder(encoder, plan["q"].get(encoder),
                                          plan["preset"].get(encoder), caps)

        es_hevc = plan["codec"] == "hevc" or (decod == "copia" and info.get("vcodec") == "hevc")
        if es_hevc and plan["ext"] in ("mp4", "mov"):
            cmd += ["-tag:v", "hvc1"]                 # para que Apple/QuickTime lo reproduzca
        cmd += plan["audio"]
        if plan["ext"] in ("mp4", "mov"):
            cmd += ["-movflags", "+faststart"]
        cmd.append(out)
        return cmd

    # Líneas de FFmpeg que indican que el DECODIFICADOR no pudo con el archivo
    # (el código de salida 69 de FFmpeg 7 = "tasa de errores de decodificación excedida")
    _VID_RE_ERR_DECOD = re.compile(
        r"decode error rate|\[vist#[^\]]*\].*(error submitting packet to decoder|decoding error)"
        r"|failed setup for format cuda|hwaccel initiali[sz]ation returned error"
        r"|no decoder surfaces left|hardware is lacking required capabilities"
        r"|(cuvid|nvdec).*(error|fail)", re.I)

    @staticmethod
    def _vid_linea_error(ultimas):
        """La línea más útil del final del log de FFmpeg (no la de progreso ni 'Conversion failed!')."""
        for linea in reversed(ultimas or []):
            baja = linea.lower()
            if baja.startswith(("frame=", "size=", "video:", "[out#")) or "conversion failed" in baja \
                    or "qavg:" in baja or baja.startswith("exiting with"):
                continue
            return linea[:140]
        return (ultimas[-1] if ultimas else "FFmpeg falló")[:140]

    def _vid_ejecutar(self, cmd, dur, verbo, etiqueta, color):
        """Corre FFmpeg mostrando el % real. Devuelve (código, últimas líneas, ¿error de decodificación?)."""
        self.current_process = subprocess.Popen(
            cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            universal_newlines=True, encoding="utf-8", errors="replace",
            startupinfo=self.get_startup_info(),
            creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
        ultimas = []
        err_decod = False
        ultimo_ui = 0.0
        for line in self.current_process.stdout:
            linea = line.strip()
            if linea:
                ultimas.append(linea)
                del ultimas[:-12]
                if not err_decod and self._VID_RE_ERR_DECOD.search(linea):
                    err_decod = True
            if dur:
                tm = re.search(r"time=(\d{2}):(\d{2}):(\d{2}\.\d{2})", line)
                if tm and time.time() - ultimo_ui >= 0.25:
                    ultimo_ui = time.time()
                    h, m, s = tm.groups()
                    progress = min(1.0, max(0.0, (int(h) * 3600 + int(m) * 60 + float(s)) / dur))
                    perc = int(progress * 100)
                    texto = f"{verbo} · {etiqueta} · {perc}%" if etiqueta else f"{verbo}... {perc}%"
                    self.after(0, lambda p=progress, t=texto: (
                        self.video_progress_bar.set(p),
                        self.video_status_label.configure(text=t, text_color=color)))
        self.current_process.wait()
        codigo = self.current_process.returncode
        return codigo, ultimas, (err_decod or codigo == 69)

    def convert_video_logic(self, source_path):
        out_path = ""
        if not os.path.exists(source_path):
            return False, "❌ ARCHIVO NO ENCONTRADO"

        def _estado(texto, color):
            self.after(0, lambda: self.video_status_label.configure(text=texto, text_color=color))

        def _borrar_salida():
            if out_path and os.path.exists(out_path):
                try: os.remove(out_path)
                except Exception: pass

        try:
            # ============================================
            # LÓGICA DE CARPETAS (DINÁMICA)
            # ============================================
            folder = os.path.dirname(source_path)
            if self.video_submode == "convert":
                current_dest_var, current_dest_seg, default_folder_name = \
                    self.v_conv_dest_var, self.v_conv_dest_seg, "VIDEO_CONV"
            elif self.video_submode == "compress":
                current_dest_var, current_dest_seg, default_folder_name = \
                    self.v_comp_dest_var, self.v_comp_dest_seg, "VIDEO_REDUCIDO"
            else:
                current_dest_var, current_dest_seg, default_folder_name = \
                    self.v_ext_dest_var, self.v_ext_dest_seg, "VIDEO_AUDIO"

            dest_choice = current_dest_var.get()
            if default_folder_name in dest_choice:
                folder = os.path.join(folder, default_folder_name)
                os.makedirs(folder, exist_ok=True)
            elif "Elegir Otra" in dest_choice and self._ruta_destino(current_dest_seg):
                folder = self._ruta_destino(current_dest_seg)
            self._registrar_salida(current_dest_seg, folder)
            base = os.path.splitext(os.path.basename(source_path))[0]

            info = vid_info(source_path)
            dur = info.get("dur") or self.get_duration(source_path)

            # ============================================
            # MODO 3: EXTRAER AUDIO (copia directa si ya viene en ese formato)
            # ============================================
            if self.video_submode == "extract":
                if info.get("ok") and not info.get("acodec"):
                    return False, "❌ El video no tiene pista de audio"
                fmt = self.v_ext_fmt.get()
                tabla = [
                    ("wav",  "wav",  ["-c:a", "pcm_s16le"],                 {"pcm_s16le"}),
                    ("aac",  "m4a",  ["-c:a", "aac", "-b:a", "192k"],       {"aac"}),
                    ("alac", "m4a",  ["-c:a", "alac"],                      {"alac"}),
                    ("flac", "flac", ["-c:a", "flac"],                      {"flac"}),
                    ("opus", "opus", ["-c:a", "libopus", "-b:a", "128k"],   {"opus"}),
                    ("ogg",  "ogg",  ["-c:a", "libvorbis", "-q:a", "5"],    {"vorbis"}),
                    ("wma",  "wma",  ["-c:a", "wmav2", "-b:a", "192k"],     {"wmav2"}),
                    ("ac3",  "ac3",  ["-c:a", "ac3", "-b:a", "192k"],       {"ac3"}),
                    ("aiff", "aiff", ["-c:a", "pcm_s16be"],                 {"pcm_s16be"}),
                ]
                tgt_ext, a_codec, copiables = "mp3", ["-c:a", "libmp3lame", "-q:a", "2"], {"mp3"}
                for clave, ext_t, args, cop in tabla:
                    if clave in fmt:
                        tgt_ext, a_codec, copiables = ext_t, args, cop
                        break
                out_path = _ruta_unica(os.path.join(folder, f"{base}.{tgt_ext}"))
                intentos = []
                if info.get("acodec") in copiables:
                    intentos.append((["-c:a", "copy"], "copia directa"))
                intentos.append((a_codec, ""))
                ultimas = []
                for args, etiqueta in intentos:
                    cmd = ["ffmpeg", "-y", "-hide_banner", "-nostdin", "-i", source_path,
                           "-vn", "-sn", "-dn", *args, out_path]
                    codigo, ultimas, _ = self._vid_ejecutar(cmd, dur, "Extrayendo", etiqueta, "#e67e22")
                    if self.cancel_requested:
                        _borrar_salida()
                        return False, "CANCELADO"
                    if codigo == 0:
                        _estado("✅ Finalizado", "#2cc985")
                        return True, "Audio: copia directa" if etiqueta else "Audio extraído"
                    _borrar_salida()
                _estado("❌ Error", "red")
                return False, f"ERROR: {self._vid_linea_error(ultimas)[:60]}"

            # ============================================
            # MODOS 1 y 2: plan (códec, resolución, calidad, audio)
            # ============================================
            _estado("Analizando video…", "#888888")
            caps = ffmpeg_capacidades()
            svt = "libsvtav1" in caps["encoders"]

            if self.video_submode == "convert":
                fmt = self.v_conv_fmt.get()
                quiere_gpu = bool(self.v_conv_gpu.get())
                if "H.265" in fmt:   codec, ext = "hevc", "mp4"
                elif "AV1" in fmt:   codec, ext = "av1", ("mkv" if "mkv" in fmt else "mp4")
                elif "H.264" in fmt: codec, ext = "h264", "mp4"
                elif "mov" in fmt:   codec, ext = "h264", "mov"
                elif "avi" in fmt:   codec, ext = "mpeg4", "avi"
                elif "wmv" in fmt:   codec, ext = "wmv2", "wmv"
                else:                codec, ext = "h264", "mp4"
                corto = vid_altura_objetivo(self.v_conv_res.get())
                sufijo, verbo, color = "_conv", "Convirtiendo", "#1f6aa5"
            else:
                quiere_gpu = bool(self.v_comp_gpu.get())
                codec = "av1" if "AV1" in self.v_comp_codec.get() else "hevc"
                ext = "mp4"
                corto = vid_altura_objetivo(self.v_comp_res.get())
                sufijo, verbo, color = "_mini", "Comprimiendo", "#2cc985"

            enc_gpu = {"h264": "h264_nvenc", "hevc": "hevc_nvenc", "av1": "av1_nvenc"}.get(codec)
            enc_cpu = {"h264": "libx264", "hevc": "libx265",
                       "av1": "libsvtav1" if svt else "libaom-av1",
                       "mpeg4": "mpeg4", "wmv2": "wmv2"}[codec]

            if self.video_submode == "convert":
                q = {enc_cpu: VID_CALIDAD_FIEL.get(enc_cpu)}
                preset = {enc_cpu: 6 if enc_cpu == "libsvtav1" else "medium"}
                if enc_gpu:
                    q[enc_gpu] = VID_CALIDAD_FIEL[enc_gpu]
                    preset[enc_gpu] = "p6"
            else:
                idx = self.compression_levels.index(self.v_comp_level.get())
                q = {enc_cpu: VID_NIVELES[enc_cpu][idx], enc_gpu: VID_NIVELES[enc_gpu][idx]}
                preset = {enc_gpu: "p7" if idx >= 3 else "p5",
                          enc_cpu: (5 if idx >= 3 else 7) if enc_cpu == "libsvtav1"
                                   else ("slow" if idx >= 3 else "medium")}

            dims = vid_dims_objetivo(info, corto) if info.get("ok") else None
            plan = {
                "codec": codec, "ext": ext, "dims": dims, "q": q, "preset": preset,
                "diez": codec in ("hevc", "av1") and (info.get("bits") or 8) >= 10,
                "audio": self._vid_audio_args(ext, info, self.video_submode,
                                              keep_audio=bool(self.v_comp_audio.get())
                                              if self.video_submode == "compress" else True),
            }
            out_path = _ruta_unica(os.path.join(folder, f"{base}{sufijo}.{ext}"))

            notas = []
            usar_nvenc = bool(quiere_gpu and enc_gpu and caps["nvenc"].get(enc_gpu) is not None)
            if quiere_gpu and enc_gpu and not usar_nvenc:
                nombre_codec = {"h264": "H.264", "hevc": "H.265", "av1": "AV1"}.get(codec, codec.upper())
                notas.append(f"{nombre_codec} por CPU (esta GPU no lo codifica)")
            if (usar_nvenc and plan["diez"] and not caps["nvenc10"].get(enc_gpu, False)):
                notas.append("GPU sin 10 bits: salida en 8 bits")

            # Remux: mismo códec y sin reescalar = copia idéntica en segundos
            vc = info.get("vcodec")
            remux = (self.video_submode == "convert" and info.get("ok") and not dims and vc == codec
                     and (codec != "h264" or ((info.get("bits") or 8) == 8 and info.get("croma") == "420"))
                     and (ext not in ("mp4", "mov") or codec in ("h264", "hevc", "av1", "mpeg4")))

            # Archivos que la GPU ya no pudo decodificar en esta sesión: se van
            # directo a "CPU decodifica" en vez de fallar otra vez en NVDEC.
            try:
                _st = os.stat(source_path)
                clave_src = (os.path.normcase(os.path.abspath(source_path)), _st.st_size, int(_st.st_mtime))
            except OSError:
                clave_src = None
            if getattr(self, "_vid_sin_nvdec", None) is None:
                self._vid_sin_nvdec = set()
            sin_nvdec = clave_src is not None and clave_src in self._vid_sin_nvdec

            nvdec_ok = caps["nvdec"] and vc in NVDEC_CODECS and not sin_nvdec
            intentos = []
            if remux:
                intentos.append(("copia", None))
            if usar_nvenc:
                if caps["gpu_total"] and not sin_nvdec and self._vid_gpu_total_posible(info):
                    intentos.append(("gpu_total", enc_gpu))
                if nvdec_ok:
                    intentos.append(("gpu_dec", enc_gpu))
                intentos.append(("cpu_dec", enc_gpu))
                intentos.append(("cpu", enc_cpu))            # último recurso: todo en CPU
            else:
                if nvdec_ok:
                    intentos.append(("gpu_dec", enc_cpu))    # la GPU solo decodifica
                intentos.append(("cpu", enc_cpu))

            ETIQUETAS = {
                "copia": "copia directa (sin recodificar)",
                "gpu_total": "GPU completa",
                "cpu_dec": "CPU decodifica + GPU codifica",
                "cpu": "CPU",
            }
            nombre_src = os.path.basename(source_path)
            ultimas, fallidos = [], 0
            for decod, encoder in intentos:
                usa_nvdec = decod in ("gpu_total", "gpu_dec")
                if usa_nvdec and sin_nvdec:
                    continue        # NVDEC ya falló con este archivo: no se repite el intento
                if decod == "gpu_dec":
                    etiqueta = ("GPU decodifica + codifica" if encoder.endswith("_nvenc")
                                else "GPU decodifica + CPU codifica")
                else:
                    etiqueta = ETIQUETAS[decod]
                corta = {"copia": "copia", "gpu_total": "GPU", "cpu": "CPU"}.get(
                    decod, "GPU" if (encoder or "").endswith("_nvenc") and decod == "gpu_dec" else "GPU+CPU")
                cmd = self._vid_comando(decod, encoder, source_path, out_path, plan, info, caps)
                if _DMT_DIAG:
                    print(f"[Video] {etiqueta}: {' '.join(cmd)}")
                _estado(f"{verbo} · {corta}…", color)
                codigo, ultimas, err_decod = self._vid_ejecutar(cmd, dur, verbo, corta, color)
                if self.cancel_requested:
                    _borrar_salida()
                    return False, "CANCELADO"
                if codigo == 0:
                    _estado("✅ Finalizado", "#2cc985")
                    partes = [etiqueta]
                    if dims and decod != "copia":
                        partes.append(f"{dims[0]}x{dims[1]}")
                    if sin_nvdec:
                        partes.append("la GPU no decodifica este archivo")
                    elif fallidos:
                        partes.append("con reintento")
                    partes += notas
                    return True, " · ".join(partes)
                fallidos += 1
                if usa_nvdec and err_decod:
                    # El decodificador de la GPU (NVDEC) no soporta este archivo:
                    # se saltan las demás rutas que también decodifican en GPU.
                    sin_nvdec = True
                    if clave_src is not None:
                        self._vid_sin_nvdec.add(clave_src)
                    print(f"[Video] {nombre_src}: la GPU no puede decodificarlo → se decodifica en CPU")
                else:
                    print(f"[Video] {nombre_src}: falló '{etiqueta}' ({codigo}): {self._vid_linea_error(ultimas)}")
                if _DMT_DIAG:
                    print(f"         {' | '.join(ultimas[-4:])}")
                _borrar_salida()

            _estado("❌ Error", "red")
            return False, f"ERROR: {self._vid_linea_error(ultimas)[:70]}"

        except Exception as e:
            _borrar_salida()
            return False, str(e)

    # ==========================================================================
    #   SECCIÓN 4: MÓDULO DE IMAGEN (EXISTENTE)
    # ==========================================================================
    def init_image_module(self):
        self.image_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.frames["ImageConverter"] = self.image_frame
        
        self.img_submode = "convert" # convert | compress
        self.img_files_conv = []
        self.img_files_comp = []

        # --- HEADER ---
        top = ctk.CTkFrame(self.image_frame, fg_color="transparent")
        top.pack(fill="x", padx=20, pady=10)
        ctk.CTkButton(top, text="← Menú", width=80, fg_color="transparent", border_width=1, 
                      command=lambda: self.show_frame("Menu")).pack(side="left")
        
        title_bg = ctk.CTkFrame(self.image_frame, fg_color="#2b2b2b", corner_radius=8)
        title_bg.pack(pady=5)
        ctk.CTkLabel(title_bg, text="Convertidor de Imágenes", font=(self.main_font, 22, "bold"), text_color="#b66223", bg_color="#2b2b2b").pack(padx=15, pady=8)

        # --- TABS (IGUAL QUE VIDEO) ---
        self.img_tabs = ctk.CTkTabview(self.image_frame, width=850, height=600, fg_color="#222",
                                       segmented_button_selected_color="#8f4e1d",
                                       segmented_button_selected_hover_color="#6e3b15",
                                       command=self._img_tab_cambio)
        self.img_tabs.pack(pady=10, expand=True, fill="y")
        
        self.img_tabs.add("Convertir Formato")
        self.img_tabs.add("Comprimir (Reducir Peso)")
        self.img_tabs.add("✂️ Remover Fondo")

        # ==============================================================================
        # TAB 1: CONVERTIR (LÓGICA CLÁSICA)
        # ==============================================================================
        t1 = self.img_tabs.tab("Convertir Formato")
        
        self.img_conv_lbl = ctk.CTkLabel(t1, text="Ninguna imagen seleccionada", text_color="gray")
        self.img_conv_lbl.pack(pady=(5,0))

        self.img_conv_drop = ctk.CTkButton(t1, text=self._IMG_TEXTO_DROP["convert"], width=600, height=80,
                                           fg_color="#3b2b20", hover_color="#4f3a2b", border_color="#8f4e1d", border_width=2,
                                           command=lambda: self.select_image_files("convert"))
        self.img_conv_drop.pack(pady=10)
        self.img_conv_drop.drop_target_register(DND_FILES)
        self.img_conv_drop.dnd_bind('<<Drop>>', lambda e: self.handle_image_drop(e, "convert"))

        opts1 = ctk.CTkFrame(t1, fg_color="transparent")
        opts1.pack(pady=10)
        ctk.CTkLabel(opts1, text="Formato Salida:").pack(side="left", padx=5)
        self.image_format_var = ctk.StringVar(value="jpg")
        ctk.CTkOptionMenu(opts1, values=["jpg", "png", "webp", "gif", "tiff", "ico"],
                          variable=self.image_format_var, width=150, fg_color="#8f4e1d", button_color="#6e3b15",
                          command=self._on_image_format_change).pack(side="left", padx=10)

        # --- Opciones ICO (ocultas por defecto, se muestran al elegir "ico") ---
        self.ico_size_var       = ctk.StringVar(value="256")
        self.ico_multisizes_var = ctk.BooleanVar(value=True)

        self.ico_opts_frame = ctk.CTkFrame(opts1, fg_color="transparent")
        # No se hace .pack() aquí → empieza oculto

        ctk.CTkLabel(self.ico_opts_frame, text="Tamaño:").pack(side="left", padx=(10, 2))
        ctk.CTkOptionMenu(self.ico_opts_frame,
                          values=["256", "128", "64", "48", "32", "24", "16"],
                          variable=self.ico_size_var,
                          width=80, fg_color="#8f4e1d", button_color="#6e3b15").pack(side="left", padx=2)
        ctk.CTkLabel(self.ico_opts_frame, text="px").pack(side="left", padx=(0, 12))

        ctk.CTkCheckBox(self.ico_opts_frame, text="Incluir subtamaños",
                        variable=self.ico_multisizes_var,
                        checkmark_color="#ffffff", fg_color="#8f4e1d",
                        hover_color="#6e3b15", border_color="#8f4e1d").pack(side="left", padx=4)

        # Destino T1
        dest1 = ctk.CTkFrame(t1, fg_color="transparent")
        dest1.pack(pady=5)
        ctk.CTkLabel(dest1, text="Guardar en:").pack(pady=2)
        self.image_dest_var = ctk.StringVar(value="📄 Misma Carpeta")
        fila_img_conv = ctk.CTkFrame(dest1, fg_color="transparent")
        fila_img_conv.pack()
        self.img_dest_seg = ctk.CTkSegmentedButton(fila_img_conv, values=["📄 Misma Carpeta", "📁 Carpeta 'IMG_CONV'", "↗️ Elegir Otra..."],
                                                   variable=self.image_dest_var, selected_color="#8f4e1d",
                                                   command=lambda v: self.on_dest_change(v, self.img_path_lbl, self.img_dest_seg))
        self.img_dest_seg.pack(side="left")
        self._boton_abrir_destino(fila_img_conv, self.img_dest_seg, "IMG_CONV",
                                  lambda: self.img_files_conv).pack(side="left", padx=(8, 0))
        self.img_path_lbl = ctk.CTkLabel(dest1, text="", text_color="gray", font=("Arial", 10))
        self.img_path_lbl.pack()

        # Botón Acción T1
        self.p_frame_conv = ctk.CTkFrame(t1, fg_color="transparent")
        self.p_frame_conv.pack(fill="x", padx=50, pady=10)
        
        # --- CORRECCIÓN: ETIQUETA DE CONTADOR VISIBLE ---
        self.img_counter_conv = ctk.CTkLabel(self.p_frame_conv, text="", font=(self.main_font, 14, "bold"))
        self.img_counter_conv.pack(pady=(0, 5))
        # ------------------------------------------------

        self.img_prog_bar_conv = ctk.CTkProgressBar(self.p_frame_conv, width=500, height=15, progress_color="#8f4e1d")
        self.img_prog_bar_conv.set(0)
        self.img_prog_bar_conv.pack(pady=5)
        self.img_status_conv = ctk.CTkLabel(self.p_frame_conv, text="Listo", text_color="gray")
        self.img_status_conv.pack()

        btn_box1 = ctk.CTkFrame(t1, fg_color="transparent")
        btn_box1.pack(pady=5)
        self.btn_run_conv = ctk.CTkButton(btn_box1, text="CONVERTIR IMÁGENES", height=45, width=200,
                                          fg_color="#8f4e1d", hover_color="#6e3b15", font=(self.main_font, 14, "bold"),
                                          command=lambda: self.start_image_wrapper("convert"))
        self.btn_run_conv.pack(side="left", padx=10)
        # CANCELAR: deja terminar la imagen actual y no convierte el resto de la cola
        self.img_cancel_conv_btn = ctk.CTkButton(btn_box1, text="CANCELAR", height=45, width=150,
                                                 fg_color="#c92c2c", hover_color="#992222", state="disabled",
                                                 command=lambda: self.cancelar_cola("image"))
        self.img_cancel_conv_btn.pack(side="left", padx=10)

        # ==============================================================================
        # TAB 2: COMPRIMIR (NUEVO)
        # ==============================================================================
        t2 = self.img_tabs.tab("Comprimir (Reducir Peso)")

        self.img_comp_lbl = ctk.CTkLabel(t2, text="Ninguna imagen seleccionada", text_color="gray")
        self.img_comp_lbl.pack(pady=(5,0))
        
        self.img_comp_drop = ctk.CTkButton(t2, text=self._IMG_TEXTO_DROP["compress"], width=600, height=80,
                                           fg_color="#3b2b20", hover_color="#4f3a2b", border_color="#d35400", border_width=2,
                                           command=lambda: self.select_image_files("compress"))
        self.img_comp_drop.pack(pady=10)
        self.img_comp_drop.drop_target_register(DND_FILES)
        self.img_comp_drop.dnd_bind('<<Drop>>', lambda e: self.handle_image_drop(e, "compress"))

        # --- NIVELES DE COMPRESIÓN ---
        lvl_frame = ctk.CTkFrame(t2, fg_color="#1a1a1a", corner_radius=10)
        lvl_frame.pack(pady=10, padx=20, ipadx=20, ipady=10)
        
        ctk.CTkLabel(lvl_frame, text="Nivel de Compresión:", font=(self.main_font, 14, "bold"), text_color="#d35400").pack(pady=5)
        
        self.img_comp_level = ctk.StringVar(value="Equilibrado")
        self.comp_levels = [
            "Ligera (Calidad Alta)", "Equilibrado",
            "Alta Compresión", "Extrema (Web/Email)",
            "Solo Reducir Resolución (50%)"
        ]

        # Segmented button para los 5 niveles
        self.seg_comp_lvl = ctk.CTkSegmentedButton(lvl_frame, values=self.comp_levels, variable=self.img_comp_level,
                                                   selected_color="#d35400", unselected_color="#333",
                                                   command=self.on_comp_level_change)
        self.seg_comp_lvl.pack(pady=5)
        self.seg_comp_lvl.set("Equilibrado")

        # Selector de formato: solo JPG o WEBP (ambos lossy — compresión real garantizada)
        f_row = ctk.CTkFrame(lvl_frame, fg_color="transparent")
        f_row.pack(pady=5)
        ctk.CTkLabel(f_row, text="Formato Final:").pack(side="left", padx=5)
        self.img_comp_fmt = ctk.StringVar(value="Convertir a JPG")
        self.img_comp_fmt_menu = ctk.CTkOptionMenu(
            f_row, values=["Convertir a JPG", "Convertir a WEBP"],
            variable=self.img_comp_fmt, width=180, fg_color="#d35400",
            command=self.update_compression_estimate
        )
        self.img_comp_fmt_menu.pack(side="left", padx=5)

        # Badge ℹ — solo visible en modo "Solo Resolución". No desplaza nada (mismo f_row)
        self.lbl_info_badge = ctk.CTkLabel(
            f_row, text=" ℹ ", width=24, height=24,
            corner_radius=12,
            fg_color="#2a6080", text_color="white",
            font=(self.main_font, 12, "bold"), cursor="hand2"
        )
        # Tooltip flotante (Toplevel oculto)
        self._comp_tooltip = None

        def _show_tooltip(event):
            if self._comp_tooltip:
                return
            tw = tk.Toplevel(self)
            tw.overrideredirect(True)
            tw.attributes("-topmost", True)
            tk.Label(
                tw,
                text="Se mantendrá el formato original del archivo,\nreduciendo sus dimensiones a la mitad.",
                bg="#1c3a4a", fg="white",
                font=(self.main_font, 11),
                padx=10, pady=7,
                relief="flat", bd=0
            ).pack()
            # Posicionar junto al badge
            x = event.widget.winfo_rootx() + 30
            y = event.widget.winfo_rooty() - 10
            tw.geometry(f"+{x}+{y}")
            self._comp_tooltip = tw

        def _hide_tooltip(event):
            if self._comp_tooltip:
                self._comp_tooltip.destroy()
                self._comp_tooltip = None

        self.lbl_info_badge.bind("<Enter>", _show_tooltip)
        self.lbl_info_badge.bind("<Leave>", _hide_tooltip)

        # --- ESTIMACIÓN DE PESO (CALCULADORA) ---
        self.lbl_estimate = ctk.CTkLabel(t2, text="Estimación: --", font=("Arial", 13, "bold"), text_color="#2cc985")
        self.lbl_estimate.pack(pady=5)

        # Destino T2
        dest2 = ctk.CTkFrame(t2, fg_color="transparent")
        dest2.pack(pady=5)
        #ctk.CTkLabel(dest2, text="Guardar en:").pack(pady=2)
        self.img_comp_dest_var = ctk.StringVar(value="📄 Misma Carpeta")
        fila_img_comp = ctk.CTkFrame(dest2, fg_color="transparent")
        fila_img_comp.pack()
        self.img_comp_dest_seg = ctk.CTkSegmentedButton(fila_img_comp, values=["📄 Misma Carpeta", "📁 Carpeta 'IMG_MINI'", "↗️ Elegir Otra..."],
                                                   variable=self.img_comp_dest_var, selected_color="#d35400",
                                                   command=lambda v: self.on_dest_change(v, self.img_comp_path_lbl, self.img_comp_dest_seg))
        self.img_comp_dest_seg.pack(side="left")
        self._boton_abrir_destino(fila_img_comp, self.img_comp_dest_seg, "IMG_MINI",
                                  lambda: self.img_files_comp).pack(side="left", padx=(8, 0))
        self.img_comp_path_lbl = ctk.CTkLabel(dest2, text="", text_color="gray", font=("Arial", 10))
        self.img_comp_path_lbl.pack()

        # Botón Acción T2
        self.p_frame_comp = ctk.CTkFrame(t2, fg_color="transparent")
        self.p_frame_comp.pack(fill="x", padx=50, pady=10)
        self.img_prog_bar_comp = ctk.CTkProgressBar(self.p_frame_comp, width=500, height=15, progress_color="#d35400")
        # --- CORRECCIÓN: ETIQUETA DE CONTADOR VISIBLE ---
        self.img_counter_comp = ctk.CTkLabel(self.p_frame_comp, text="", font=(self.main_font, 14, "bold"))
        self.img_counter_comp.pack(pady=(0, 5))
        # ------------------------------------------------

        self.img_prog_bar_comp.set(0)
        self.img_prog_bar_comp.pack(pady=5)
        self.img_status_comp = ctk.CTkLabel(self.p_frame_comp, text="Listo", text_color="gray")
        self.img_status_comp.pack()
        
        btn_box2 = ctk.CTkFrame(t2, fg_color="transparent")
        btn_box2.pack(pady=5)
        self.btn_run_comp = ctk.CTkButton(btn_box2, text="COMPRIMIR AHORA", height=45, width=200, 
                                          fg_color="#d35400", hover_color="#a04000", font=(self.main_font, 14, "bold"),
                                          command=lambda: self.start_image_wrapper("compress"))
        self.btn_run_comp.pack(side="left", padx=10)
        # CANCELAR (igual que en Convertir): termina la imagen actual y corta la cola
        self.img_cancel_btn = ctk.CTkButton(btn_box2, text="CANCELAR", height=45, width=150, fg_color="#c92c2c",
                                            state="disabled", command=lambda: self.cancelar_cola("image"))
        self.img_cancel_btn.pack(side="left", padx=10)

        # ==============================================================================
        # ==============================================================================
        # TAB 3: REMOVER FONDO (rembg + PIL)
        # ==============================================================================
        t3 = self.img_tabs.tab("✂️ Remover Fondo")

        # Estado interno exclusivo de esta pestaña
        self.rembg_files   = []   # Lista de archivos (múltiple)
        self.rembg_session = None # Sesión u2net cacheada para no recargar

        # --- Etiqueta de archivo(s) seleccionado(s) ---
        self.rembg_lbl = ctk.CTkLabel(
            t3, text="Ninguna imagen seleccionada", text_color="gray"
        )
        self.rembg_lbl.pack(pady=(8, 0))

        # --- Zona de Drag & Drop / Selección ---
        self.rembg_drop = ctk.CTkButton(
            t3,
            text="✂️  Arrastra IMÁGENES para REMOVER FONDO",
            width=600, height=80,
            fg_color="#1e2d1e", hover_color="#2e4a2e",
            border_color="#3a9e3a", border_width=2,
            command=self._rembg_select_files
        )
        self.rembg_drop.pack(pady=10)
        self.rembg_drop.drop_target_register(DND_FILES)
        self.rembg_drop.dnd_bind("<<Drop>>", self._rembg_handle_drop)

        # --- Opciones de exportación ---
        opts3 = ctk.CTkFrame(t3, fg_color="transparent")
        opts3.pack(pady=6)

        ctk.CTkLabel(opts3, text="Guardar en:").pack(side="left", padx=5)

        self.rembg_dest_var = ctk.StringVar(value="📄 Misma Carpeta")
        self.rembg_dest_seg = ctk.CTkSegmentedButton(
            opts3,
            values=["📄 Misma Carpeta", "📁 Carpeta 'SIN_FONDO'", "↗️ Elegir Otra..."],
            variable=self.rembg_dest_var,
            selected_color="#3a9e3a", selected_hover_color="#2a7a2a",
            command=lambda v: self.on_dest_change(v, self.rembg_path_lbl, self.rembg_dest_seg)
        )
        self.rembg_dest_seg.pack(side="left", padx=8)
        self._boton_abrir_destino(opts3, self.rembg_dest_seg, "SIN_FONDO",
                                  lambda: self.rembg_files).pack(side="left")

        self.rembg_path_lbl = ctk.CTkLabel(t3, text="", text_color="gray", font=("Arial", 10))
        self.rembg_path_lbl.pack()

        # Nota fija: siempre PNG
        ctk.CTkLabel(
            t3,
            text="⚠ El resultado se guarda siempre en PNG para preservar la transparencia.",
            text_color="#888", font=("Arial", 11, "italic")
        ).pack(pady=(0, 6))

        # --- Contador + barra de progreso + estado ---
        self.p_frame_rembg = ctk.CTkFrame(t3, fg_color="transparent")
        self.p_frame_rembg.pack(fill="x", padx=50, pady=6)

        self.rembg_counter_lbl = ctk.CTkLabel(
            self.p_frame_rembg, text="", font=(self.main_font, 14, "bold")
        )
        self.rembg_counter_lbl.pack(pady=(0, 4))

        self.rembg_prog_bar = ctk.CTkProgressBar(
            self.p_frame_rembg, width=500, height=15, progress_color="#3a9e3a"
        )
        self.rembg_prog_bar.set(0)
        self.rembg_prog_bar.pack(pady=5)

        self.rembg_status_lbl = ctk.CTkLabel(
            self.p_frame_rembg, text="Listo", text_color="gray"
        )
        self.rembg_status_lbl.pack()

        # --- Botón principal ---
        btn_box3 = ctk.CTkFrame(t3, fg_color="transparent")
        btn_box3.pack(pady=8)

        self.btn_run_rembg = ctk.CTkButton(
            btn_box3,
            text="✂️  ELIMINAR FONDO",
            height=45, width=220,
            fg_color="#3a9e3a", hover_color="#2a7a2a",
            font=(self.main_font, 14, "bold"),
            command=self._rembg_start
        )
        self.btn_run_rembg.pack(side="left", padx=10)

        # Mapeo por defecto para compatibilidad
        self.image_list_label = self.img_conv_lbl
        self.image_drop_area = self.img_conv_drop
        self.image_convert_btn = self.btn_run_conv
        self.image_progress_bar = self.img_prog_bar_conv
        self.image_status_label = self.img_status_conv
        self.image_counter_label = self.img_counter_conv
        self.image_cancel_btn = self.img_cancel_conv_btn

    _IMG_TEXTO_DROP = {
        "convert": "🖼️ Arrastra IMÁGENES para CONVERTIR",
        "compress": "📉 Arrastra IMÁGENES para COMPRIMIR",
    }

    def _img_tab_cambio(self):
        """Al abrir la pestaña de Quitar fondo se precargan sus librerías."""
        try:
            if self.img_tabs.get().endswith("Remover Fondo"):
                self._rembg_precargar()
        except Exception:
            pass

    def _rembg_precargar(self):
        """
        Carga en segundo plano las librerías de 'Quitar fondo' (rembg +
        onnxruntime + numba: unos 2-3 s la primera vez, que antes se pagaban
        enteros al pulsar el botón). El MODELO no se carga aquí: eso ocupa
        memoria y se hace al procesar, para no desalojar a otros módulos de IA.
        """
        if getattr(self, "_rembg_precargado", False):
            return
        self._rembg_precargado = True

        def _cargar():
            try:
                t0 = time.time()
                _asegurar_numba_o_sustituto()
                import rembg  # noqa: F401
                print(f"[Quitar fondo] Librerías listas en {time.time() - t0:.1f} s "
                      f"(el modelo se carga al procesar).")
            except Exception as e:
                print(f"[Quitar fondo] Precarga no crítica, falló: {e}")

        threading.Thread(target=_cargar, name="dmt_rembg_precarga", daemon=True).start()

    def _imagen_limpiar_listas(self):
        """Al entrar al módulo: sin archivos de una visita anterior (lo que se ve es lo que se procesa)."""
        self.img_files_conv = []
        self.img_files_comp = []
        for lbl, drop, clave in ((self.img_conv_lbl, self.img_conv_drop, "convert"),
                                 (self.img_comp_lbl, self.img_comp_drop, "compress")):
            lbl.configure(text="Ninguna imagen seleccionada", text_color="gray")
            drop.configure(text=self._IMG_TEXTO_DROP[clave])
        self.update_compression_estimate()

    def _on_image_format_change(self, value):
        """Muestra u oculta las opciones ICO según el formato seleccionado."""
        if value == "ico":
            self.ico_opts_frame.pack(side="left")
        else:
            self.ico_opts_frame.pack_forget()

    def select_image_files(self, submode):
        files = filedialog.askopenfilenames(filetypes=_filtro_imagenes())
        if files:
            if submode == "convert":
                self.img_files_conv = list(files)
                self.file_queue = list(files)
                self.update_file_list_ui(self.img_conv_drop, self.img_conv_lbl)
            else:
                self.img_files_comp = list(files)
                self.file_queue = list(files)
                self.update_file_list_ui(self.img_comp_drop, self.img_comp_lbl)
                self.update_compression_estimate() # Calcular al cargar

    def handle_image_drop(self, event, submode):
        clean = self._rutas_drop(event)
        valid = [f for f in clean if f.lower().endswith(tuple(VALID_IMAGE_EXT))]
        rechazados = len(clean) - len(valid)

        if submode == "convert":
            self.img_files_conv = list(valid)
            self.file_queue = list(valid)
            self.update_file_list_ui(self.img_conv_drop, self.img_conv_lbl)
            lbl = self.img_conv_lbl
        else:
            self.img_files_comp = list(valid)
            self.file_queue = list(valid)
            self.update_file_list_ui(self.img_comp_drop, self.img_comp_lbl)
            self.update_compression_estimate() # Calcular al soltar
            lbl = self.img_comp_lbl
        if rechazados:
            lbl.configure(text=f"{lbl.cget('text')} ({rechazados} inválidos)", text_color="orange")

    def on_comp_level_change(self, value):
        """Maneja el cambio de nivel: bloquea/desbloquea el selector de formato."""
        if value == "Solo Reducir Resolución (50%)":
            # Bloquear formato y mostrar badge ℹ
            self.img_comp_fmt_menu.configure(state="disabled")
            self.img_comp_fmt.set("🔒 Mantiene formato original")
            self.lbl_info_badge.pack(side="left", padx=(4, 0))
        else:
            # Restaurar selector y ocultar badge
            self.img_comp_fmt_menu.configure(state="normal")
            if "🔒" in self.img_comp_fmt.get():
                self.img_comp_fmt.set("Convertir a JPG")
            # Destruir tooltip si quedó abierto al cambiar de nivel con teclado
            if self._comp_tooltip:
                self._comp_tooltip.destroy()
                self._comp_tooltip = None
            self.lbl_info_badge.pack_forget()
        self.update_compression_estimate()

    def update_compression_estimate(self, _=None):
        """Calcula estimación realista según nivel + formato de salida real."""
        if not self.img_files_comp:
            self.lbl_estimate.configure(text="Estimación: --")
            return

        # 1. Peso total original
        total_size = sum(
            os.path.getsize(f) for f in self.img_files_comp if os.path.exists(f)
        )
        if total_size == 0:
            self.lbl_estimate.configure(text="Estimación: --")
            return

        lvl = self.img_comp_level.get()
        fmt = self.img_comp_fmt.get()
        is_webp = "WEBP" in fmt

        # 2. Factores realistas por nivel + formato
        #    (basados en el comportamiento real de ffmpeg, no en promesas)
        factors = {
            # (jpg_factor, webp_factor)
            "Ligera (Calidad Alta)":        (0.70, 0.55),
            "Equilibrado":                  (0.45, 0.32),
            "Alta Compresión":              (0.25, 0.18),
            "Extrema (Web/Email)":          (0.15, 0.10),
            "Solo Reducir Resolución (50%)": (0.50, 0.50),  # siempre 50%, formato intacto
        }

        pair = factors.get(lvl, (0.50, 0.50))
        factor = pair[1] if is_webp else pair[0]

        final_size = total_size * factor
        mb_orig   = total_size / (1024 * 1024)
        mb_final  = final_size / (1024 * 1024)
        saved_pct = int((1 - factor) * 100)

        if lvl == "Solo Reducir Resolución (50%)":
            txt = (f"Origen: {mb_orig:.1f} MB  ➜  Estimado: ~{mb_final:.1f} MB  "
                   f"(~{saved_pct}% menos — solo escala)")
        else:
            txt = (f"Origen: {mb_orig:.1f} MB  ➜  Estimado: ~{mb_final:.1f} MB  "
                   f"(~{saved_pct}% menos, estimado)")

        self.lbl_estimate.configure(text=txt)

    def start_image_wrapper(self, submode):
        if self.lote_de("image"):
            return       # ya hay imágenes procesándose
        self.img_submode = submode
        # Cada pestaña procesa SOLO su propia lista y usa sus propios widgets
        if submode == "convert":
            if not self.img_files_conv: return
            self.file_queue = list(self.img_files_conv)
            self.image_convert_btn = self.btn_run_conv
            self.image_drop_area = self.img_conv_drop
            self.image_cancel_btn = self.img_cancel_conv_btn      # CANCELAR (corta la cola)
            self.image_progress_bar = self.img_prog_bar_conv
            self.image_status_label = self.img_status_conv
            self.image_counter_label = self.img_counter_conv
        else:
            if not self.img_files_comp: return
            self.file_queue = list(self.img_files_comp)
            self.image_convert_btn = self.btn_run_comp
            self.image_drop_area = self.img_comp_drop
            self.image_cancel_btn = self.img_cancel_btn           # CANCELAR (corta la cola)
            self.image_progress_bar = self.img_prog_bar_comp
            self.image_status_label = self.img_status_comp
            self.image_counter_label = self.img_counter_comp

        self.start_batch_thread("image")
    
    @staticmethod
    def _fix_ico_header(path):
        """
        Reordena las entradas del directorio ICO de MAYOR a MENOR tamaño
        y corrige los offsets internos. Garantiza que Windows use el 256×256
        como imagen principal del icono.
        """
        import struct
        with open(path, 'rb') as f:
            data = bytearray(f.read())
        count = struct.unpack_from('<H', data, 4)[0]
        entries = []
        for i in range(count):
            off = 6 + i * 16
            entry  = bytes(data[off:off + 16])
            size   = struct.unpack_from('<I', data, off + 8)[0]
            offset = struct.unpack_from('<I', data, off + 12)[0]
            w = data[off]; w = 256 if w == 0 else w
            entries.append((w, entry, bytes(data[offset:offset + size])))
        entries.sort(key=lambda x: x[0], reverse=True)
        new_data = bytearray(data[:6])
        cur = 6 + count * 16
        new_dir = bytearray()
        for w, entry, blob in entries:
            e = bytearray(entry)
            struct.pack_into('<I', e, 12, cur)
            new_dir += e
            cur += len(blob)
        new_data += new_dir
        for _, _, blob in entries:
            new_data += blob
        with open(path, 'wb') as f:
            f.write(new_data)

    def convert_image_logic(self, source_path):
        out_path = ""
        temporales = []     # PNG intermedios (PSD, transparencia -> JPG...)
        nota_salida = ""
        if not os.path.exists(source_path):
            return False, "❌ ARCHIVO NO ENCONTRADO"
        
        try:
            # DETERMINAR LÓGICA (CONVERTIR vs COMPRIMIR)
            
            # --- CASO 1: CONVERTIR ---
            if self.img_submode == "convert":
                tgt_ext = self.image_format_var.get()
                
                folder = os.path.dirname(source_path)
                if "IMG_CONV" in self.image_dest_var.get():
                    folder = os.path.join(folder, "IMG_CONV")
                    os.makedirs(folder, exist_ok=True)
                elif self.image_dest_var.get().startswith("↗️") and self._ruta_destino(self.img_dest_seg):
                    folder = self._ruta_destino(self.img_dest_seg)
                self._registrar_salida(self.img_dest_seg, folder)
                
                # Nunca sobre un archivo existente: convertir al mismo formato en
                # "Misma Carpeta" escribía encima del ORIGINAL (recomprimido y sin EXIF)
                out_path = _ruta_unica(os.path.join(
                    folder, f"{os.path.splitext(os.path.basename(source_path))[0]}.{tgt_ext}"))

                # ── CONVERSIÓN A ICO: método PIL (multi-tamaño, sin ffmpeg) ──────
                if tgt_ext == "ico":
                    try:
                        # Apertura inteligente (si el origen ya es .ico, toma la mejor capa)
                        base_size = int(self.ico_size_var.get())
                        # img_open_any: también SVG y HEIC (Pillow no los abre)
                        im = img_open_any(source_path, target_px=base_size,
                                          svg_lado=max(_SVG_LADO_POR_DEFECTO, base_size))

                        # Tamaños a generar: el base elegido + estándar menores
                        if self.ico_multisizes_var.get():
                            sizes_to_use = [s for s in ICO_STANDARD_SIZES if s <= base_size]
                            if base_size not in sizes_to_use:
                                sizes_to_use.append(base_size)
                        else:
                            sizes_to_use = [base_size]

                        # ico_build_frames cuadra UNA vez a resolución nativa y
                        # genera cada frame directamente desde ahí:
                        #   - nada de doble escalado (origen -> base -> subtamaño)
                        #   - los tamaños menores salen de la resolución real del
                        #     origen, no de una ampliación inventada
                        frames = ico_build_frames(im, sizes_to_use)
                        if not frames:
                            return False, "❌ No se pudo generar ningún tamaño de icono"

                        frames[0].save(
                            out_path, format="ICO",
                            sizes=[(f.width, f.height) for f in frames],
                            append_images=frames[1:]
                        )
                        self._fix_ico_header(out_path)
                        return True, " ✅ COMPLETADO "
                    except Exception as e:
                        return False, str(e)
                # ────────────────────────────────────────────────────────────────

                # ── CONVERSIÓN DESDE GIF a formato estático: método PIL ──────────
                # ffmpeg falla con GIFs animados → salida única sin patrón %d
                src_ext = os.path.splitext(source_path)[1].lower()
                if src_ext == ".gif" and tgt_ext in ("jpg", "jpeg", "png", "tiff", "tif", "bmp", "webp"):
                    try:
                        with Image.open(source_path) as gif:
                            gif.seek(0)  # Primer frame
                            frame = gif.copy()

                        if tgt_ext in ("jpg", "jpeg", "tiff", "tif", "bmp"):
                            # Estos formatos no admiten canal alfa → convertir a RGB
                            frame = frame.convert("RGBA")
                            bg = Image.new("RGB", frame.size, (255, 255, 255))
                            bg.paste(frame, mask=frame.split()[3])
                            frame = bg
                        else:
                            frame = frame.convert("RGBA")

                        save_kwargs = {}
                        if tgt_ext in ("jpg", "jpeg"):
                            save_kwargs = {"quality": 95, "optimize": True}
                        elif tgt_ext == "png":
                            save_kwargs = {"compress_level": 3}

                        frame.save(out_path, **save_kwargs)
                        return True, " ✅ COMPLETADO (frame 1)"
                    except Exception as e:
                        return False, f"❌ Error GIF→{tgt_ext.upper()}: {e}"
                # ─────────────────────────────────────────────────────────────────

                # ── CONVERSIÓN DESDE ICO: método PIL (mejor capa disponible) ─────
                # ffmpeg no elige capa: puede sacar el frame de 16x16 y arruinar
                # la salida. PIL nos deja tomar siempre la resolución más alta.
                if src_ext == ".ico" and tgt_ext in ("jpg", "jpeg", "png", "tiff", "tif", "bmp", "webp"):
                    try:
                        # target_px=None -> selecciona la MAYOR capa disponible
                        ico_img = img_open_smart(source_path, target_px=None)

                        if tgt_ext in ("jpg", "jpeg", "tiff", "tif", "bmp"):
                            # Sin canal alfa: componer sobre blanco (no sobre negro)
                            fondo = Image.new("RGB", ico_img.size, (255, 255, 255))
                            fondo.paste(ico_img, mask=ico_img.split()[3])
                            ico_img = fondo

                        save_kwargs = {}
                        if tgt_ext in ("jpg", "jpeg"):
                            save_kwargs = {"quality": 95, "optimize": True}
                        elif tgt_ext == "png":
                            save_kwargs = {"compress_level": 3}

                        # Sin resize: se guarda a la resolución nativa de la capa
                        ico_img.save(out_path, **save_kwargs)
                        return True, f" ✅ COMPLETADO ({ico_img.width}×{ico_img.height})"
                    except Exception as e:
                        return False, f"❌ Error ICO→{tgt_ext.upper()}: {e}"
                # ─────────────────────────────────────────────────────────────────

                pre_opts, entrada, tmps = _img_entrada_ffmpeg(source_path, opaco=(tgt_ext == "jpg"))
                temporales.extend(tmps)
                cmd = ["ffmpeg", "-y"] + pre_opts + ["-i", entrada]
                # GIF/WebP animados: un solo cuadro para formatos de una sola imagen
                if tgt_ext in _IMG_SALIDA_UN_CUADRO:
                    cmd.extend(["-frames:v", "1"])
                # Calidad estándar alta para conversiones
                if tgt_ext == "jpg": cmd.extend(["-q:v", "2"])
                elif tgt_ext == "webp": cmd.extend(_img_opciones_webp(source_path) + ["-q:v", "80"])
                elif tgt_ext == "png": cmd.extend(["-compression_level", "3"])

                cmd.append(out_path)

            # --- CASO 2: COMPRIMIR (NIVELES) ---
            else:
                level = self.img_comp_level.get()
                fmt_choice = self.img_comp_fmt.get()

                # ── MODO ESPECIAL: Solo escalar resolución al 50% ──────────────
                if level == "Solo Reducir Resolución (50%)":
                    src_ext = os.path.splitext(source_path)[1].lower()

                    # Seguridad: omitir .ico (quedarían inservibles a 16x8)
                    if src_ext == ".ico":
                        return False, "⏭️ OMITIDO (.ico no se puede escalar)"

                    ext = src_ext.replace(".", "") or "jpg"
                    # HEIC/SVG/PSD no se pueden volver a escribir: JPG (fotos) o PNG
                    if src_ext in _IMG_SIN_REESCRITURA:
                        ext = _IMG_SIN_REESCRITURA[src_ext]
                        nota_salida = f" (guardado como {ext.upper()}: {src_ext[1:].upper()} no se puede reescribir)"
                    folder = os.path.dirname(source_path)
                    if "IMG_MINI" in self.img_comp_dest_var.get():
                        folder = os.path.join(folder, "IMG_MINI")
                        os.makedirs(folder, exist_ok=True)
                    elif self.img_comp_dest_var.get().startswith("↗️") and self._ruta_destino(self.img_comp_dest_seg):
                        folder = self._ruta_destino(self.img_comp_dest_seg)
                    self._registrar_salida(self.img_comp_dest_seg, folder)

                    stem = os.path.splitext(os.path.basename(source_path))[0]
                    out_path = _ruta_unica(os.path.join(folder, f"{stem}_mini50.{ext}"))

                    pre_opts, entrada, tmps = _img_entrada_ffmpeg(
                        source_path, opaco=(ext in ("jpg", "jpeg", "bmp")), con_filtro=True)
                    temporales.extend(tmps)
                    cmd = ["ffmpeg", "-y"] + pre_opts + ["-i", entrada, "-vf", "scale=iw/2:-1:flags=lanczos"]
                    if ext in _IMG_SALIDA_UN_CUADRO:
                        cmd.extend(["-frames:v", "1"])
                    if ext in ("jpg", "jpeg"):
                        cmd.extend(["-q:v", "2"])
                    elif ext == "webp":
                        cmd.extend(_img_opciones_webp(source_path))
                    cmd.append(out_path)

                # ── MODOS NORMALES: conversión lossy garantizada (JPG o WEBP) ──
                else:
                    # Formato de salida — siempre JPG o WEBP (lossy real)
                    ext = "webp" if "WEBP" in fmt_choice else "jpg"

                    folder = os.path.dirname(source_path)
                    if "IMG_MINI" in self.img_comp_dest_var.get():
                        folder = os.path.join(folder, "IMG_MINI")
                        os.makedirs(folder, exist_ok=True)
                    elif self.img_comp_dest_var.get().startswith("↗️") and self._ruta_destino(self.img_comp_dest_seg):
                        folder = self._ruta_destino(self.img_comp_dest_seg)
                    self._registrar_salida(self.img_comp_dest_seg, folder)

                    stem = os.path.splitext(os.path.basename(source_path))[0]
                    out_path = _ruta_unica(os.path.join(folder, f"{stem}_mini.{ext}"))

                    pre_opts, entrada, tmps = _img_entrada_ffmpeg(
                        source_path, opaco=(ext == "jpg"), con_filtro=(level == "Extrema (Web/Email)"))
                    temporales.extend(tmps)
                    cmd = ["ffmpeg", "-y"] + pre_opts + ["-i", entrada]
                    if ext == "jpg":
                        cmd.extend(["-frames:v", "1"])   # GIF/WebP animados -> un cuadro
                    else:
                        cmd.extend(_img_opciones_webp(source_path))

                    if level == "Ligera (Calidad Alta)":
                        if ext == "jpg":  cmd.extend(["-q:v", "5"])
                        elif ext == "webp": cmd.extend(["-q:v", "75"])

                    elif level == "Equilibrado":
                        if ext == "jpg":  cmd.extend(["-q:v", "12"])
                        elif ext == "webp": cmd.extend(["-q:v", "50"])

                    elif level == "Alta Compresión":
                        if ext == "jpg":  cmd.extend(["-q:v", "20"])
                        elif ext == "webp": cmd.extend(["-q:v", "30"])

                    elif level == "Extrema (Web/Email)":
                        cmd.extend(["-vf", "scale=iw/2:-1:flags=lanczos"])
                        if ext == "jpg":  cmd.extend(["-q:v", "28"])
                        elif ext == "webp": cmd.extend(["-q:v", "15"])

                    cmd.append(out_path)

            # --- EJECUCIÓN COMÚN --- (este método corre en el hilo del lote)
            if not self._lote().cortar:
                self._en_ui(self.image_status_label.configure, text="Procesando...", text_color="yellow")
            barra = self.img_prog_bar_comp if self.img_submode == "compress" else self.img_prog_bar_conv
            self._en_ui(barra.set, 0.5)

            # encoding='utf-8' + errors='ignore': sin crasheos con tildes/ñ en la salida de FFmpeg
            res = subprocess.run(
                cmd,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.PIPE,
                startupinfo=self.get_startup_info(),
                creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
                text=True,
                encoding='utf-8',
                errors='ignore'
            )
            
            if self.cancel_requested:
                if os.path.exists(out_path):
                    try: os.remove(out_path)
                    except: pass
                return False, "CANCELADO"

            if res.returncode == 0:
                return True, " ✅ COMPLETADO " + nota_salida
            else:
                return False, "ERROR FFMPEG"

        except Exception as e: 
            if out_path and os.path.exists(out_path):
                try: os.remove(out_path)
                except: pass
            return False, str(e)
        finally:
            _img_borrar_temporales(temporales)

    # ==========================================================================
    #   SECCIÓN 4.5: REMOVER FONDO — Métodos de lógica y UI
    # ==========================================================================

    @staticmethod
    def _rembg_truncate_name(name, max_len=65):
        """Acorta un nombre de archivo para mostrar en UI: base....ext"""
        base, ext = os.path.splitext(name)
        if len(name) <= max_len:
            return name
        keep = max_len - len(ext) - 3  # 3 = len("...")
        return base[:max(keep, 1)] + "..." + ext

    def _rembg_update_drop_label(self):
        """Actualiza el botón de drop y la etiqueta con la lista actual."""
        n = len(self.rembg_files)
        if n == 0:
            self.rembg_lbl.configure(text="Ninguna imagen seleccionada", text_color="gray")
            self.rembg_drop.configure(text="✂️  Arrastra IMÁGENES para REMOVER FONDO")
        elif n == 1:
            name = self._rembg_truncate_name(os.path.basename(self.rembg_files[0]))
            self.rembg_lbl.configure(text=f"1 imagen seleccionada", text_color="white")
            self.rembg_drop.configure(text=f"🖼 {name}")
        else:
            self.rembg_lbl.configure(text=f"{n} imágenes seleccionadas", text_color="white")
            first = self._rembg_truncate_name(os.path.basename(self.rembg_files[0]))
            self.rembg_drop.configure(text=f"🖼 {first}  (+{n-1} más)")

    def _rembg_select_files(self):
        """Abre diálogo para seleccionar MÚLTIPLES imágenes."""
        files = filedialog.askopenfilenames(filetypes=_filtro_imagenes())
        if files:
            self.rembg_files = list(files)
            self._rembg_update_drop_label()

    def _rembg_handle_drop(self, event):
        """Maneja el arrastrar y soltar de MÚLTIPLES archivos."""
        files = self._rutas_drop(event)

        valid = [
            f for f in files
            if f.lower().endswith(tuple(VALID_IMAGE_EXT))
        ]
        if valid:
            self.rembg_files = valid
            self._rembg_update_drop_label()

    def _rembg_start(self):
        """Valida y lanza el hilo de procesamiento rembg."""
        if not self.rembg_files:
            self.rembg_status_lbl.configure(
                text="❌ Selecciona al menos una imagen primero.", text_color="#e05050"
            )
            return

        self.btn_run_rembg.configure(state="disabled")
        self.rembg_counter_lbl.configure(text="")

        # Detectar si modelo ya existe en disco para mostrar mensaje correcto
        if self.rembg_session is None:
            _local = os.environ.get("LOCALAPPDATA", os.path.expanduser("~"))
            _model_file = os.path.join(_local, "DeusMachinaTools", "rembg_models", "u2net.onnx")
            if os.path.isfile(_model_file):
                _txt = "Cargando modelo de IA..."
            else:
                _txt = "Descargando modelo de IA (176 MB)... Esto solo ocurrirá la primera vez."
            self.rembg_status_lbl.configure(text=_txt, text_color="yellow")
            self.rembg_prog_bar.configure(mode="indeterminate")
            self.rembg_prog_bar.start()
        else:
            self.rembg_status_lbl.configure(
                text="Iniciando proceso...", text_color="#90ee90"
            )
            self.rembg_prog_bar.configure(mode="determinate")
            self.rembg_prog_bar.set(0)

        self._trabajo_inicio("rembg", "Quitar fondo de imágenes")
        t = threading.Thread(target=self._rembg_worker, daemon=True)
        t.start()

    def _rembg_liberar(self):
        """Libera la sesión u2net (la llama el gestor de modelos)."""
        if getattr(self, "rembg_session", None) is not None:
            self.rembg_session = None
            gc.collect()
        self.gestor_ia.marcar_descargado("rembg")

    def _rembg_worker(self):
        try:
            def _espera(quien):
                self._en_ui(self.rembg_status_lbl.configure,
                            text=f"⏳ Esperando a que termine {quien}…", text_color="#d4ac0d")

            # Carril de IA: u2net no se carga mientras OCR o Whisper trabajan
            with self.carril_ia.turno("rembg", "Quitar fondo", on_espera=_espera):
                with self.gestor_ia.en_uso("rembg"):
                    self._rembg_worker_impl()
        except Exception as e:
            print(f"[Quitar fondo] Error: {e}")
            self._en_ui(self.rembg_status_lbl.configure,
                        text=f"❌ Error: {str(e)[:120]}", text_color="#e05050")
            self._en_ui(self.btn_run_rembg.configure, state="normal")
        finally:
            self._trabajo_fin("rembg")

    def _rembg_worker_impl(self):
        """
        Corre en hilo separado.
        - Cachea la sesión u2net en self.rembg_session para no recargar nunca más.
        - Procesa todos los archivos en cola, uno por uno.
        - Actualiza contador y barra por cada imagen.
        """
        def ui(fn):
            self.after(0, fn)

        try:
            # ── FIX PYINSTALLER ──────────────────────────────────────────────
            # (Nuitka no define _MEIPASS: el bloque solo aplica si existe)
            meipass = getattr(sys, "_MEIPASS", None)
            if meipass:
                if meipass not in sys.path:
                    sys.path.insert(0, meipass)
                if meipass not in os.environ.get("PATH", ""):
                    os.environ["PATH"] = meipass + os.pathsep + os.environ.get("PATH", "")

            # U2NET_HOME → ruta escribible y persistente en CUALQUIER PC
            _local = os.environ.get("LOCALAPPDATA", os.path.expanduser("~"))
            _models_dir = os.path.join(_local, "DeusMachinaTools", "rembg_models")
            os.makedirs(_models_dir, exist_ok=True)
            os.environ["U2NET_HOME"] = _models_dir

            # Monkey-patch importlib.metadata: rembg llama requires() en sus deps
            # y en el .exe no existen los dist-info → devolvemos [] silenciosamente
            import importlib.metadata as _imeta
            if not getattr(_imeta, "_rembg_patched", False):
                _orig_req = _imeta.requires
                def _safe_req(pkg):
                    try:
                        return _orig_req(pkg)
                    except Exception:
                        return []
                _imeta.requires = _safe_req
                _imeta._rembg_patched = True
            # ────────────────────────────────────────────────────────────────

            # numba: sustituto si el build no lo incluye (Nuitka)
            _asegurar_numba_o_sustituto()

            # ── Importación diferida con auto-reintento silencioso ───────────
            remove = None
            new_session = None
            for _attempt in range(2):
                try:
                    from rembg import remove, new_session
                    break  # éxito
                except Exception as _e:
                    if _attempt == 1:
                        # Segundo intento también falló → mostrar error real
                        ui(lambda err=str(_e): self.rembg_status_lbl.configure(
                            text=f"❌ Error cargando rembg: {err[:150]}",
                            text_color="#e05050"
                        ))
                        ui(lambda: self.btn_run_rembg.configure(state="normal"))
                        return
                    # Primer fallo: limpiar caché de módulos y reintentar
                    for _mod in [k for k in sys.modules if "rembg" in k]:
                        sys.modules.pop(_mod, None)
                    time.sleep(0.2)

            # ── Cargar sesión SOLO si no está cacheada ──────────────────────
            if self.rembg_session is None:
                try:
                    # FIX --windowed: con esta flag PyInstaller pone sys.stdout/stderr = None
                    # porque no hay consola. pooch+tqdm intentan escribir ahí al descargar
                    # el modelo → "NoneType has no attribute write". Redirigimos a /dev/null.
                    import io as _io
                    _stdout_bak = sys.stdout
                    _stderr_bak = sys.stderr
                    if sys.stdout is None:
                        sys.stdout = _io.StringIO()
                    if sys.stderr is None:
                        sys.stderr = _io.StringIO()
                    try:
                        self.gestor_ia.antes_de_cargar("rembg")
                        self.rembg_session = new_session("u2net")
                        self.gestor_ia.marcar_cargado("rembg")
                    finally:
                        sys.stdout = _stdout_bak
                        sys.stderr = _stderr_bak
                except Exception as _e:
                    ui(lambda: self.rembg_prog_bar.stop())
                    ui(lambda err=str(_e): self.rembg_status_lbl.configure(
                        text=f"❌ Error al cargar modelo u2net: {err[:150]}",
                        text_color="#e05050"
                    ))
                    ui(lambda: self.btn_run_rembg.configure(state="normal"))
                    return
                # Cambiar a modo determinado ahora que terminó la descarga
                ui(lambda: self.rembg_prog_bar.stop())
                ui(lambda: self.rembg_prog_bar.configure(mode="determinate"))

            session = self.rembg_session
            total   = len(self.rembg_files)

            dest_choice = self.rembg_dest_var.get()

            errors = 0
            for idx, fpath in enumerate(self.rembg_files, start=1):
                # Capturar variables para las lambdas
                _idx, _total = idx, total
                short_name = self._rembg_truncate_name(os.path.basename(fpath))

                ui(lambda i=_idx, t=_total: self.rembg_counter_lbl.configure(
                    text=f"Procesando {i} de {t}"
                ))
                ui(lambda n=short_name: self.rembg_status_lbl.configure(
                    text=f"Recortando: {n}", text_color="#90ee90"
                ))
                ui(lambda i=_idx, t=_total: self.rembg_prog_bar.set(i / t))

                try:
                    # img_open_any: ICO (capa mayor), PSD, SVG, HEIC, TIFF 16 bits y
                    # orientación EXIF correcta.
                    img = img_open_any(fpath)
                    result = _rembg_quitar_fondo(img, session, remove)

                    src_dir  = os.path.dirname(fpath)
                    src_name = os.path.splitext(os.path.basename(fpath))[0]

                    if "SIN_FONDO" in dest_choice:
                        out_dir = os.path.join(src_dir, "SIN_FONDO")
                        os.makedirs(out_dir, exist_ok=True)
                    elif dest_choice.startswith("↗️") and self._ruta_destino(self.rembg_dest_seg):
                        out_dir = self._ruta_destino(self.rembg_dest_seg)
                    else:
                        out_dir = src_dir
                    self._registrar_salida(self.rembg_dest_seg, out_dir)

                    out_path = _ruta_unica(os.path.join(out_dir, f"{src_name}_sin_fondo.png"))
                    result.save(out_path, format="PNG")

                except Exception as e:
                    errors += 1
                    err_msg = str(e)[:80]
                    # n=idx: el número se fija ahora (la lambda corre después, con idx ya avanzado)
                    ui(lambda m=err_msg, n=idx: self.rembg_status_lbl.configure(
                        text=f"⚠ Error en imagen {n}: {m}", text_color="#e05050"
                    ))

            # ── Mensaje final ────────────────────────────────────────────────
            ok = total - errors
            if errors == 0:
                ui(lambda: self.rembg_status_lbl.configure(
                    text=f"✅ ¡{total} imagen{'s' if total>1 else ''} procesada{'s' if total>1 else ''} con éxito!",
                    text_color="#2cc985"
                ))
            else:
                ui(lambda: self.rembg_status_lbl.configure(
                    text=f"⚠ {ok} exitosas, {errors} con error.",
                    text_color="orange"
                ))

        except Exception as exc:
            err_msg = str(exc)
            ui(lambda: self.rembg_status_lbl.configure(
                text=f"❌ Error: {err_msg[:120]}", text_color="#e05050"
            ))

        finally:
            ui(lambda: self._rembg_reset_ui())

    def _rembg_reset_ui(self):
        """Restaura la barra de progreso y habilita el botón."""
        self.rembg_prog_bar.stop()
        self.rembg_prog_bar.configure(mode="determinate")
        self.rembg_counter_lbl.configure(text="")
        self.btn_run_rembg.configure(state="normal")


    # ==========================================================================
    #   SECCIÓN 5: MÓDULO PDF (SWITCHES CENTRADOS)
    # ==========================================================================
    def init_pdf_module(self):
        self.pdf_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.frames["PDFTools"] = self.pdf_frame
        
        # Colores
        self.col_main = "#5ab3a0"      
        self.col_hover = "#3d8c79"     
        self.col_bg_drop = "#2a5f52"   
        self.col_accent = "#76c7c0"    
        
        self.pdf_compress_files = [] 
        self.convert_queue = [] 
        self.convert_pdf_file = None 
        self.convert_mode = ctk.StringVar(value="Imágenes ➔ PDF")
        
        # Header
        top = ctk.CTkFrame(self.pdf_frame, fg_color="transparent")
        top.pack(fill="x", padx=20, pady=10)
        ctk.CTkButton(top, text="← Menú", width=80, fg_color="transparent", border_width=1, command=lambda: self.show_frame("Menu")).pack(side="left")
        
        title_bg = ctk.CTkFrame(self.pdf_frame, fg_color="#2b2b2b", corner_radius=8)
        title_bg.pack(pady=5)
        ctk.CTkLabel(title_bg, text="Herramientas PDF", font=(self.main_font, 22, "bold"), text_color="#76c7c0", bg_color="#2b2b2b").pack(padx=15, pady=8)

        # TABS PRINCIPALES
        self.pdf_tabs = ctk.CTkTabview(self.pdf_frame, width=850, height=650, fg_color="#222", 
                                       segmented_button_selected_color=self.col_main, 
                                       segmented_button_selected_hover_color=self.col_hover)
        
        self.pdf_tabs.pack(pady=10, fill="y", expand=True)

        self.pdf_tabs.add("Unir PDFs")
        self.pdf_tabs.add("Dividir PDF")
        self.pdf_tabs.add("Convertir")
        self.pdf_tabs.add("Comprimir (Reducir)") 

        # ... [PESTAÑAS 1, 2 y 3 SE MANTIENEN IGUAL QUE ANTES] ...
        # (Copia el código de las pestañas Unir, Dividir y Convertir de la respuesta anterior si lo borraste, 
        # aquí solo pongo la PESTAÑA 4 modificada para ahorrar espacio)

        # ===========================================================
        # PESTAÑA 1: UNIR PDFS (Tu código anterior aquí...)
        # ===========================================================
        tab_merge = self.pdf_tabs.tab("Unir PDFs")
        self.merge_list_frame = ctk.CTkScrollableFrame(tab_merge, width=600, height=200, fg_color="#181818", border_color="#333", border_width=2)
        self.merge_list_frame.pack(pady=(15, 5))
        self.merge_list_frame._parent_canvas.configure(yscrollincrement=4)
        self.merge_placeholder = ctk.CTkLabel(self.merge_list_frame, text="\n📂 Arrastra PDFs aquí\npara unirlos", font=("Arial", 14), text_color="#666")
        self.merge_placeholder.pack(expand=True, fill="both", pady=20)
        self.make_droppable(self.merge_list_frame, self.merge_placeholder, "merge")
        
        c_frame = ctk.CTkFrame(tab_merge, fg_color="transparent")
        c_frame.pack(pady=5)
        _btn_kw_m = dict(fg_color="#1a3a5c", hover_color="#2a5c8a", text_color="white")
        ctk.CTkButton(c_frame, text="⏫", width=38, **_btn_kw_m, command=self.move_pdf_to_top).pack(side="left", padx=2)
        ctk.CTkButton(c_frame, text="🔼", width=38, **_btn_kw_m, command=lambda: self.move_pdf_item(-1)).pack(side="left", padx=2)
        ctk.CTkButton(c_frame, text="🔽", width=38, **_btn_kw_m, command=lambda: self.move_pdf_item(1)).pack(side="left", padx=2)
        ctk.CTkButton(c_frame, text="⏬", width=38, **_btn_kw_m, command=self.move_pdf_to_bottom).pack(side="left", padx=2)
        ctk.CTkLabel(c_frame, text="│", text_color="#444").pack(side="left", padx=6)
        ctk.CTkButton(c_frame, text="🗑 Uno",  width=70, fg_color="#b93b3b", hover_color="#8a2be2", command=self.remove_pdf_item).pack(side="left", padx=4)
        ctk.CTkButton(c_frame, text="✖ Todo", width=70, fg_color="transparent", border_width=1, border_color="#b93b3b", text_color="#b93b3b", command=self.clear_merge_list).pack(side="left", padx=4)
        self.merge_count_lbl = ctk.CTkLabel(c_frame, text="0 PDFs", text_color="#666", font=("Arial", 11))
        self.merge_count_lbl.pack(side="left", padx=12)

        opts_frame = ctk.CTkFrame(tab_merge, fg_color="transparent")
        opts_frame.pack(pady=10) 
        self.var_merge_a4 = ctk.BooleanVar(value=False)
        self.var_merge_landscape = ctk.BooleanVar(value=False)
        ctk.CTkSwitch(opts_frame, text="Forzar A4", variable=self.var_merge_a4, progress_color=self.col_main).pack(side="left", padx=20)
        ctk.CTkSwitch(opts_frame, text="Horizontal", variable=self.var_merge_landscape, progress_color=self.col_main).pack(side="left", padx=20)

        # Destino Merge (CORREGIDO)
        dest_merge = ctk.CTkFrame(tab_merge, fg_color="transparent")
        dest_merge.pack(pady=5)
        
        self.merge_dest_var = ctk.StringVar(value="📄 Misma Carpeta")
        
        # Botones solos y centrados
        self.merge_dest_seg = ctk.CTkSegmentedButton(dest_merge, values=["📄 Misma Carpeta", "📁 Carpeta 'PDF_UNIDOS'", "↗️ Elegir Otra..."],
                               variable=self.merge_dest_var, selected_color=self.col_main, 
                               command=lambda v: self.on_dest_change(v, self.merge_path_lbl, self.merge_dest_seg))
        self.merge_dest_seg.pack(side="left")
        self._boton_abrir_destino(dest_merge, self.merge_dest_seg, "PDF_UNIDOS",
                                  lambda: self.pdf_merge_list).pack(side="left", padx=(8, 0))
                               
        # Etiqueta debajo (parent = tab_merge)
        self.merge_path_lbl = ctk.CTkLabel(tab_merge, text="", text_color="gray", font=("Arial", 10))
        self.merge_path_lbl.pack(pady=(0, 5))

        self.merge_btn = ctk.CTkButton(tab_merge, text="GENERAR UNIÓN", width=250, height=45, 
                                       fg_color=self.col_main, hover_color=self.col_hover,
                                       text_color="black", font=(self.main_font, 13, "bold"), command=self.start_merge_thread)
        self.merge_btn.pack(pady=5)
        self.merge_status = ctk.CTkLabel(tab_merge, text="", text_color=self.col_accent)
        self.merge_status.pack()

        # ===========================================================
        # PESTAÑA 2: DIVIDIR PDF (Tu código anterior aquí...)
        # ===========================================================
        tab_split = self.pdf_tabs.tab("Dividir PDF")
        self.split_drop_area = ctk.CTkButton(tab_split, text="📄 Arrastra 1 PDF para DIVIDIR", width=500, height=80, 
                                             fg_color=self.col_bg_drop, hover_color="#112d3d", border_color=self.col_main, border_width=1,
                                             command=lambda: self.select_files_pdf("split"))
        self.split_drop_area.pack(pady=20)
        self.split_drop_area.drop_target_register(DND_FILES)
        self.split_drop_area.dnd_bind('<<Drop>>', lambda e: self.handle_pdf_drop(e, "split"))
        
        split_opts = ctk.CTkFrame(tab_split, fg_color="transparent")
        split_opts.pack(pady=10)
        ctk.CTkLabel(split_opts, text="Páginas (ej: 1-3, 5):").pack(side="left", padx=5)
        self.split_entry = ctk.CTkEntry(split_opts, width=200, placeholder_text="1-3, 5")
        self.split_entry.pack(side="left")

        # Destino Split (CORREGIDO)
        dest_split = ctk.CTkFrame(tab_split, fg_color="transparent")
        dest_split.pack(pady=5)
        
        self.split_dest_var = ctk.StringVar(value="📄 Misma Carpeta")
        
        # Botones solos y centrados
        self.split_dest_seg = ctk.CTkSegmentedButton(dest_split, values=["📄 Misma Carpeta", "📁 Carpeta 'PDF_SPLIT'", "↗️ Elegir Otra..."],
                               variable=self.split_dest_var, selected_color=self.col_main,
                               command=lambda v: self.on_dest_change(v, self.split_path_lbl, self.split_dest_seg))
        self.split_dest_seg.pack(side="left")
        self._boton_abrir_destino(dest_split, self.split_dest_seg, "PDF_SPLIT",
                                  lambda: [self.pdf_split_file] if self.pdf_split_file else []).pack(side="left", padx=(8, 0))

        # Etiqueta debajo (parent = tab_split)
        self.split_path_lbl = ctk.CTkLabel(tab_split, text="", text_color="gray", font=("Arial", 10))
        self.split_path_lbl.pack(pady=(0, 5))
        
        self.split_btn = ctk.CTkButton(tab_split, text="EXTRAER PÁGINAS", width=250, height=40, 
                                       fg_color=self.col_main, hover_color=self.col_hover, text_color="black",
                                       command=self.start_split_thread)
        self.split_btn.pack(pady=10)
        self.split_status = ctk.CTkLabel(tab_split, text="", text_color=self.col_accent)
        self.split_status.pack()
        self.split_progress = ctk.CTkProgressBar(tab_split, width=400, progress_color=self.col_main)
        self.split_progress.set(0)
        self.split_progress.pack(pady=5)

        # ===========================================================
        # PESTAÑA 3: CONVERTIR (Tu código anterior aquí...)
        # ===========================================================
        tab_conv = self.pdf_tabs.tab("Convertir")
        mode_frame = ctk.CTkFrame(tab_conv, fg_color="transparent")
        mode_frame.pack(pady=(20, 5))
        self.conv_mode_seg = ctk.CTkSegmentedButton(mode_frame, values=["Imágenes ➔ PDF", "PDF ➔ Imágenes"], 
                                                    variable=self.convert_mode, width=500, height=35,
                                                    selected_color=self.col_main, command=self.toggle_convert_ui)
        self.conv_mode_seg.set("Imágenes ➔ PDF")
        self.conv_mode_seg.pack()

        self.conv_content_container = ctk.CTkFrame(tab_conv, fg_color="transparent")
        self.conv_content_container.pack(fill="x", pady=0)

        self.frame_img_to_pdf = ctk.CTkFrame(self.conv_content_container, fg_color="transparent")
        self.img_list_frame = ctk.CTkScrollableFrame(self.frame_img_to_pdf, width=600, height=200, fg_color="#181818", border_color="#333", border_width=2)
        self.img_list_frame.pack(pady=5)
        self.img_list_frame._parent_canvas.configure(yscrollincrement=4)
        self.img_placeholder = ctk.CTkLabel(self.img_list_frame,
                                            text="\n🖼️\nArrastra imágenes aquí\n(o haz clic para explorar)",
                                            font=("Arial", 14), text_color="#555")
        self.img_placeholder.pack(expand=True, fill="both", pady=20)
        self.make_droppable(self.img_list_frame, self.img_placeholder, "img_to_pdf")

        ictrl = ctk.CTkFrame(self.frame_img_to_pdf, fg_color="transparent")
        ictrl.pack(pady=5)
        # --- Botones de orden ---
        _btn_kw = dict(fg_color="#1a3a5c", hover_color="#2a5c8a", text_color="white")
        ctk.CTkButton(ictrl, text="⏫", width=38, **_btn_kw, command=self.move_img_to_top).pack(side="left", padx=2)
        ctk.CTkButton(ictrl, text="🔼", width=38, **_btn_kw, command=lambda: self.move_img_item(-1)).pack(side="left", padx=2)
        ctk.CTkButton(ictrl, text="🔽", width=38, **_btn_kw, command=lambda: self.move_img_item(1)).pack(side="left", padx=2)
        ctk.CTkButton(ictrl, text="⏬", width=38, **_btn_kw, command=self.move_img_to_bottom).pack(side="left", padx=2)
        # --- Separador visual ---
        ctk.CTkLabel(ictrl, text="│", text_color="#444").pack(side="left", padx=6)
        # --- Botones eliminar ---
        ctk.CTkButton(ictrl, text="🗑 Uno",  width=70, fg_color="#b93b3b", hover_color="#8a2be2", command=self.remove_img_item).pack(side="left", padx=4)
        ctk.CTkButton(ictrl, text="✖ Todo", width=70, fg_color="transparent", border_width=1, border_color="#b93b3b", text_color="#b93b3b", command=self.clear_img_list).pack(side="left", padx=4)
        # --- Contador ---
        self.img_count_lbl = ctk.CTkLabel(ictrl, text="0 imágenes", text_color="#666", font=("Arial", 11))
        self.img_count_lbl.pack(side="left", padx=12)

        img_opts = ctk.CTkFrame(self.frame_img_to_pdf, fg_color="transparent")
        img_opts.pack(pady=10)
        self.var_img_a4 = ctk.BooleanVar(value=True)
        self.var_img_margin = ctk.BooleanVar(value=False)
        self.var_img_landscape = ctk.BooleanVar(value=False)
        ctk.CTkSwitch(img_opts, text="Forzar A4", variable=self.var_img_a4, progress_color=self.col_main,
                      command=self._pdf_a4_toggle).pack(side="left", padx=(15, 6))
        # Resolución de las imágenes dentro de la hoja A4 (150 = liviano, 300 = para imprimir)
        self.var_img_a4_dpi = ctk.StringVar(value="150 DPI")
        self.seg_img_a4_dpi = ctk.CTkSegmentedButton(img_opts, values=["150 DPI", "300 DPI"],
                                                     variable=self.var_img_a4_dpi,
                                                     selected_color=self.col_main,
                                                     selected_hover_color=self.col_hover)
        self.seg_img_a4_dpi.pack(side="left", padx=(0, 15))
        ctk.CTkSwitch(img_opts, text="Incluir Margen", variable=self.var_img_margin, progress_color=self.col_main).pack(side="left", padx=15)
        ctk.CTkSwitch(img_opts, text="Horizontal", variable=self.var_img_landscape, progress_color=self.col_main).pack(side="left", padx=15)

        self.frame_pdf_to_img = ctk.CTkFrame(self.conv_content_container, fg_color="transparent")
        self.pdf_conv_drop = ctk.CTkButton(self.frame_pdf_to_img, text="📂 Arrastra 1 PDF aquí", width=500, height=100,
                                           fg_color=self.col_bg_drop, hover_color="#112d3d", border_color=self.col_main, border_width=1,
                                           command=lambda: self.select_files_pdf("pdf_to_img"))
        self.pdf_conv_drop.pack(pady=20) 
        self.pdf_conv_drop.drop_target_register(DND_FILES)
        self.pdf_conv_drop.dnd_bind('<<Drop>>', lambda e: self.handle_pdf_drop(e, "pdf_to_img"))
        
        self.fmt_choice = ctk.StringVar(value="jpg")
        f_row = ctk.CTkFrame(self.frame_pdf_to_img, fg_color="transparent")
        f_row.pack()
        ctk.CTkLabel(f_row, text="Formato salida:").pack(side="left", padx=10)
        ctk.CTkOptionMenu(f_row, variable=self.fmt_choice, values=["jpg", "png"], 
                          fg_color=self.col_main, text_color="black").pack(side="left")

        # Área inferior de Convertir (CORREGIDO)
        bottom_area = ctk.CTkFrame(tab_conv, fg_color="transparent")
        bottom_area.pack(pady=5)
        
        dest_conv = ctk.CTkFrame(bottom_area, fg_color="transparent")
        dest_conv.pack(pady=5)
        
        self.conv_dest_var = ctk.StringVar(value="📄 Misma Carpeta")
        
        # Botones solos
        self.conv_dest_seg = ctk.CTkSegmentedButton(dest_conv, values=["📄 Misma Carpeta", "📁 Carpeta 'PDF_CONV'", "↗️ Elegir Otra..."],
                               variable=self.conv_dest_var, selected_color=self.col_main,
                               command=lambda v: self.on_dest_change(v, self.conv_path_lbl, self.conv_dest_seg))
        self.conv_dest_seg.pack(side="left")
        self._boton_abrir_destino(dest_conv, self.conv_dest_seg, "PDF_CONV",
                                  lambda: (self.convert_queue if self.convert_mode.get() == "Imágenes ➔ PDF" else ([self.convert_pdf_file] if self.convert_pdf_file else []))).pack(side="left", padx=(8, 0))
        
        # Etiqueta debajo (parent = bottom_area, antes del botón ejecutar)
        self.conv_path_lbl = ctk.CTkLabel(bottom_area, text="", text_color="gray", font=("Arial", 10))
        self.conv_path_lbl.pack(pady=(0, 5))
        
        self.conv_btn = ctk.CTkButton(bottom_area, text="EJECUTAR CONVERSIÓN", width=250, height=45, 
                                      fg_color=self.col_main, hover_color=self.col_hover, text_color="black", 
                                      font=(self.main_font, 13, "bold"), command=self.start_convert_thread)
        self.conv_btn.pack(pady=5)
        
        self.conv_status = ctk.CTkLabel(bottom_area, text="", text_color=self.col_accent)
        self.conv_status.pack()
        self.frame_img_to_pdf.pack(fill="x")

        # ===========================================================
        # PESTAÑA 4: COMPRIMIR PDF (ACTUALIZADA)
        # ===========================================================
        tab_comp = self.pdf_tabs.tab("Comprimir (Reducir)")

        # Drop Area
        self.pdf_comp_lbl = ctk.CTkLabel(tab_comp, text="Ningún PDF seleccionado", text_color="gray")
        self.pdf_comp_lbl.pack(pady=(10, 0))

        self.pdf_comp_drop = ctk.CTkButton(tab_comp, text="📉 Arrastra PDFs para OPTIMIZAR", width=600, height=80,
                                           fg_color="#2a4f47", hover_color="#36665c", border_color=self.col_main, border_width=2,
                                           command=lambda: self.select_files_pdf("compress"))
        self.pdf_comp_drop.pack(pady=10)
        self.pdf_comp_drop.drop_target_register(DND_FILES)
        self.pdf_comp_drop.dnd_bind('<<Drop>>', lambda e: self.handle_pdf_drop(e, "compress"))

        # Niveles
        lvl_frame = ctk.CTkFrame(tab_comp, fg_color="#1a1a1a", corner_radius=10)
        lvl_frame.pack(pady=10, padx=20, ipadx=20, ipady=10)

        ctk.CTkLabel(lvl_frame, text="Nivel de Optimización:", font=(self.main_font, 14, "bold"), text_color=self.col_main).pack(pady=5)

        self.pdf_comp_level = ctk.StringVar(value="Recomendado (Calidad 75)")
        
       # [MODIFICADO] Definimos 4 niveles claros
        self.pdf_levels = [
            "1. Ligera (Alta Calidad | 300 DPI)",       
            "2. Equilibrada (Estándar | 150 DPI)",      # <--- Esta queremos por defecto
            "3. Alta Compresión (Pantalla | 72 DPI)",   
            "4. Extrema (Email/Web | 50 DPI)"           
        ]

        # [MODIFICADO] 'value=self.pdf_levels[1]' selecciona la opción 2 al iniciar
        self.pdf_comp_level = ctk.StringVar(value=self.pdf_levels[1])

        self.pdf_menu_opts = ctk.CTkOptionMenu(lvl_frame, values=self.pdf_levels, variable=self.pdf_comp_level, width=300,
                          fg_color=self.col_main, button_color=self.col_hover, text_color="black",
                          command=self.update_pdf_size_estimate)
        self.pdf_menu_opts.pack(pady=5)
        self.pdf_menu_opts.set(self.pdf_levels[1]) # Seleccionar Equilibrada por defecto
        
        ctk.CTkLabel(lvl_frame, text="✔ Solo comprime imágenes  ✔ Mantiene Texto Vectorial  ✔ Anti-Corrupción", 
                     text_color="gray", font=("Arial", 11)).pack(pady=5)

        # Info Peso [NUEVO: Estimación]
        self.pdf_comp_info = ctk.CTkLabel(tab_comp, text="Peso Actual: --  ➜  Estimado: --", font=("Arial", 12, "bold"), text_color="white")
        self.pdf_comp_info.pack(pady=5)

        # Destino
        # Destino (MODIFICADO PARA QUE LA RUTA SALGA ABAJO)
        dest_comp = ctk.CTkFrame(tab_comp, fg_color="transparent")
        dest_comp.pack(pady=5)
        
        self.pdf_comp_dest_var = ctk.StringVar(value="📄 Misma Carpeta")
        
        # 1. Los botones van solos en su frame (sin side="left" para que se centren)
        self.pdf_comp_dest_seg = ctk.CTkSegmentedButton(dest_comp, values=["📄 Misma Carpeta", "📁 Carpeta 'PDF_OPTIMIZADO'", "↗️ Elegir Otra..."],
                               variable=self.pdf_comp_dest_var, selected_color=self.col_main, text_color="black",
                               command=lambda v: self.on_dest_change(v, self.pdf_comp_path_lbl, self.pdf_comp_dest_seg))
        self.pdf_comp_dest_seg.pack(side="left")
        self._boton_abrir_destino(dest_comp, self.pdf_comp_dest_seg, "PDF_OPTIMIZADO",
                                  lambda: self.pdf_compress_files).pack(side="left", padx=(8, 0))

        # 2. La etiqueta de la ruta va FUERA del frame de botones, directamente en la pestaña (tab_comp)
        # Esto hace que aparezca en la siguiente línea vertical
        self.pdf_comp_path_lbl = ctk.CTkLabel(tab_comp, text="", text_color="gray", font=("Arial", 10))
        self.pdf_comp_path_lbl.pack(pady=(0, 5))

        # Acción
        self.p_frame_comp_pdf = ctk.CTkFrame(tab_comp, fg_color="transparent")
        self.p_frame_comp_pdf.pack(fill="x", padx=50, pady=10)
        self.pdf_prog_bar = ctk.CTkProgressBar(self.p_frame_comp_pdf, width=500, height=15, progress_color=self.col_main)
        self.pdf_prog_bar.set(0)
        self.pdf_prog_bar.pack(pady=5)
        self.pdf_status_comp = ctk.CTkLabel(self.p_frame_comp_pdf, text="Listo", text_color="gray")
        self.pdf_status_comp.pack()

        self.pdf_btn_comp = ctk.CTkButton(tab_comp, text="OPTIMIZAR PDF", height=45, width=220, 
                                          fg_color=self.col_main, hover_color=self.col_hover, text_color="black", font=(self.main_font, 14, "bold"),
                                          command=self.start_pdf_compress_thread)
        self.pdf_btn_comp.pack(pady=5)
        
    def _pdf_a4_toggle(self):
        """La resolución A4 solo aplica con 'Forzar A4' encendido."""
        try:
            self.seg_img_a4_dpi.configure(state="normal" if self.var_img_a4.get() else "disabled")
        except Exception:
            pass

    def _pdf_sincronizar_listas(self):
        """Al entrar a PDF: la interfaz muestra exactamente lo que hay en memoria
        (Unir y Dividir se vacían al salir del módulo)."""
        self.pdf_selected_index = None
        try:
            self.refresh_merge_ui()
            if not self.pdf_split_file:
                self.split_drop_area.configure(text="📄 Arrastra 1 PDF para DIVIDIR")
        except Exception:
            pass

    def clear_img_list(self):
        """Limpia toda la lista de imágenes"""
        self.convert_queue = []
        self.pdf_img_selected_index = None
        self.refresh_img_ui()
        
    def clear_merge_list(self):
        """Limpia toda la lista de unión de PDFs"""
        self.pdf_merge_list = []
        self.pdf_selected_index = None
        self.refresh_merge_ui()
        
    def update_pdf_size_estimate(self, _=None):
        """Calcula un RANGO de estimación realista (UX Profesional)"""
        if not self.pdf_compress_files:
            self.pdf_comp_info.configure(text="Peso Actual: --  ➜  Estimado: --")
            return

        # 1. Calcular peso total actual en MB
        total_mb = sum(os.path.getsize(f) for f in self.pdf_compress_files if os.path.exists(f)) / (1024*1024)
        
        # 2. Definir rango de factores (Min - Max) según agresividad
        level = self.pdf_comp_level.get()
        low_f, high_f = 1.0, 1.0
        
        if "1." in level:   low_f, high_f = 0.80, 0.95    # Baja poco (5-20%)
        elif "2." in level: low_f, high_f = 0.60, 0.80    # Baja a la mitad aprox
        elif "3." in level: low_f, high_f = 0.40, 0.60    # Baja bastante
        elif "4." in level: low_f, high_f = 0.20, 0.40    # Baja drásticamente
        
        # 3. Calcular rango
        min_est = total_mb * low_f
        max_est = total_mb * high_f
        
        # 4. Mostrar resultado formateado: "Origen: 10 MB ➜ Estimado: 4.5 – 7.0 MB"
        self.pdf_comp_info.configure(text=f"Origen: {total_mb:.1f} MB  ➜  Estimado: {min_est:.1f} – {max_est:.1f} MB")

    def make_droppable(self, scroll_frame, placeholder_label, mode_tag):
        """
        Habilita Drag & Drop Y TAMBIÉN Clic para buscar archivos 
        en el frame, su canvas interno y el label placeholder.
        """
        # 1. Configurar Drag & Drop (Soltar archivos)
        scroll_frame.drop_target_register(DND_FILES)
        scroll_frame.dnd_bind('<<Drop>>', lambda e: self.handle_pdf_drop(e, mode_tag))
        
        try:
            scroll_frame._parent_canvas.drop_target_register(DND_FILES)
            scroll_frame._parent_canvas.dnd_bind('<<Drop>>', lambda e: self.handle_pdf_drop(e, mode_tag))
        except: pass

        placeholder_label.drop_target_register(DND_FILES)
        placeholder_label.dnd_bind('<<Drop>>', lambda e: self.handle_pdf_drop(e, mode_tag))

        # 2. Configurar CLIC (Abrir buscador) - NUEVO
        # Usamos bind con Button-1 (Clic izquierdo)
        
        # Clic en el texto "Arrastra aquí..."
        placeholder_label.bind("<Button-1>", lambda e: self.select_files_pdf(mode_tag))
        
        # Clic en el fondo del scroll (Canvas)
        try:
            scroll_frame._parent_canvas.bind("<Button-1>", lambda e: self.select_files_pdf(mode_tag))
        except: pass
        
        # Clic en el marco (por si acaso)
        scroll_frame.bind("<Button-1>", lambda e: self.select_files_pdf(mode_tag))
        
    def start_pdf_compress_thread(self):
        if not self.pdf_compress_files:
            messagebox.showwarning("Vacío", "Selecciona PDFs primero.")
            return
        if str(self.pdf_btn_comp.cget("state")) == "disabled":
            return                                   # ya está comprimiendo (doble clic)
        self.pdf_btn_comp.configure(state="disabled")
        self._trabajo_inicio("pdf_comp", "Compresión de PDF")
        threading.Thread(target=self.run_pdf_compress,
                         args=(list(self.pdf_compress_files), self.pdf_comp_level.get(),
                               self.pdf_comp_dest_var.get()),
                         daemon=True).start()


    def find_ghostscript(self):
        """
        Busca el ejecutable de Ghostscript en este orden:
        1. Carpeta local 'tools/ghostscript' (Versión portable distribuida con la App).
        2. PATH del sistema.
        3. Carpetas de instalación estándar en Windows.
        """
        # Definir la ruta base dependiendo de si corremos en .py o .exe
        # (_is_frozen_build detecta PyInstaller y Nuitka)
        if _is_frozen_build():
            base_path = os.path.dirname(sys.executable)
        else:
            base_path = os.path.dirname(os.path.abspath(__file__))

        # ------------------------------------------------------------------------
        # 1. PRIORIDAD MÁXIMA: Buscar en la carpeta local 'tools' (Tu distribución)
        # ------------------------------------------------------------------------
        # Buscamos específicamente la versión de consola ('c') para subprocess
        exes_buscados = ["gswin64c.exe", "gswin32c.exe"] 
        
        rutas_locales = [
            # Estructura recomendada: dist/tools/ghostscript/bin/gswin64c.exe
            os.path.join(base_path, "tools", "ghostscript", "bin"),
            # Estructura simple: dist/tools/ghostscript/gswin64c.exe
            os.path.join(base_path, "tools", "ghostscript")
        ]

        for ruta in rutas_locales:
            for exe in exes_buscados:
                full_path = os.path.join(ruta, exe)
                if os.path.exists(full_path):
                    print(f"DEBUG: Ghostscript PORTABLE encontrado en: {full_path}")
                    return full_path

        # ------------------------------------------------------------------------
        # 2. Intentar buscar en el PATH del sistema
        # ------------------------------------------------------------------------
        posibles = ["gswin64c", "gswin32c", "gs"]
        for cmd in posibles:
            ruta_path = shutil.which(cmd)
            if ruta_path:
                print(f"DEBUG: Ghostscript encontrado en PATH: {ruta_path}")
                return ruta_path
        
        # ------------------------------------------------------------------------
        # 3. Búsqueda MANUAL INTELIGENTE en C:\Program Files\gs\
        # ------------------------------------------------------------------------
        rutas_base_sistema = [
            r"C:\Program Files\gs",
            r"C:\Program Files (x86)\gs"
        ]

        for base in rutas_base_sistema:
            if os.path.exists(base):
                try:
                    # Listamos carpetas y ordenamos reverse para intentar la versión más nueva
                    carpetas = [d for d in os.listdir(base) if d.startswith("gs")]
                    carpetas.sort(reverse=True)
                    
                    for carpeta in carpetas:
                        bin_path = os.path.join(base, carpeta, "bin")
                        for exe in exes_buscados:
                            full_path = os.path.join(bin_path, exe)
                            if os.path.exists(full_path):
                                print(f"DEBUG: Ghostscript encontrado en sistema manual: {full_path}")
                                return full_path
                except Exception:
                    continue

        print("ERROR: No se encontró ninguna instalación de Ghostscript.")
        return None

    @staticmethod
    def _fmt_bytes(n):
        """Convierte bytes a string legible con 2 decimales (KB o MB)."""
        if n >= 1_048_576:
            return f"{n / 1_048_576:.2f} MB"
        return f"{n / 1_024:.2f} KB"

    # Ghostscript usa la API ANSI de Windows: no abre rutas de más de 260
    # caracteres. Por encima de este margen se trabaja con copias en una carpeta
    # temporal corta y el resultado se mueve al destino real.
    GS_LARGO_SEGURO = 230

    def _gs_comprimir(self, gs_exe, entrada, salida, preset, dpi):
        """
        Corre Ghostscript una vez. Si las rutas son largas (o si falla por eso),
        reintenta con copias en una carpeta temporal de ruta corta.
        Devuelve (ok, detalle) — 'detalle' explica el fallo para el resumen.
        """
        def _cmd(ent, sal):
            return [
                gs_exe,
                "-sDEVICE=pdfwrite",
                "-dCompatibilityLevel=1.4",
                "-dNOPAUSE",
                "-dQUIET",
                "-dBATCH",
                "-dSAFER",
                f"-dPDFSETTINGS={preset}",
                "-dColorImageDownsampleThreshold=1.0",
                "-dGrayImageDownsampleThreshold=1.0",
                "-dMonoImageDownsampleThreshold=1.0",
                f"-dColorImageResolution={dpi}",
                f"-dGrayImageResolution={dpi}",
                f"-dMonoImageResolution={dpi}",
                "-dDownsampleColorImages=true",
                "-dDownsampleGrayImages=true",
                "-dDownsampleMonoImages=true",
                # Esto evita que rote páginas automáticamente si no debe
                "-dAutoRotatePages=/None",
                # Ghostscript toma '%' de -sOutputFile como patrón (%d = nº de página)
                "-sOutputFile=" + sal.replace("%", "%%"),
                ent,
            ]

        def _correr(ent, sal):
            p = subprocess.run(
                _cmd(ent, sal), stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                startupinfo=self.get_startup_info(),
                creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
                text=True, encoding="utf-8", errors="replace")
            salida_txt = ((p.stderr or "") + "\n" + (p.stdout or "")).strip()
            return p.returncode, salida_txt

        def _ultima_linea(txt):
            lineas = [l.strip() for l in (txt or "").splitlines() if l.strip()]
            return lineas[-1][:130] if lineas else ""

        rutas_largas = max(len(entrada), len(salida)) > self.GS_LARGO_SEGURO
        err = ""
        codigo = -1
        if not rutas_largas:
            codigo, err = _correr(entrada, salida)
            if codigo == 0 and os.path.isfile(salida):
                return True, ""
            try:
                if os.path.exists(salida):
                    os.remove(salida)
            except OSError:
                pass

        # --- Plan B: rutas cortas en la carpeta temporal de la sesión ---
        tmp_dir = None
        try:
            tmp_dir = tempfile.mkdtemp(prefix="gs_")
            ent_corta = os.path.join(tmp_dir, "e.pdf")
            sal_corta = os.path.join(tmp_dir, "s.pdf")
            shutil.copy2(entrada, ent_corta)
            codigo2, err2 = _correr(ent_corta, sal_corta)
            if codigo2 != 0 or not os.path.isfile(sal_corta):
                detalle = _ultima_linea(err2) or _ultima_linea(err)
                return False, (f"Ghostscript no pudo procesarlo (código {codigo2})"
                               + (f": {detalle}" if detalle else ""))
            try:
                os.makedirs(os.path.dirname(salida), exist_ok=True)
                shutil.move(sal_corta, salida)
            except OSError as e_mov:
                if len(salida) > 255:
                    return False, ("la ruta de destino es demasiado larga para Windows "
                                   f"({len(salida)} caracteres): guarda en una carpeta más corta")
                return False, f"no se pudo guardar el archivo final: {str(e_mov)[:90]}"
            if rutas_largas:
                print(f"[PDF] Ruta larga ({max(len(entrada), len(salida))} caracteres): "
                      f"se comprimió usando una carpeta temporal corta.")
            return True, ""
        except OSError as e_copia:
            return False, f"no se pudo preparar el archivo para comprimir: {str(e_copia)[:90]}"
        finally:
            if tmp_dir:
                shutil.rmtree(tmp_dir, ignore_errors=True)

    def run_pdf_compress(self, archivos, sel_level, dest_choice):
        """Hilo: comprime con Ghostscript. La interfaz se toca solo con _en_ui."""
        def estado(texto, color):
            self._en_ui(self.pdf_status_comp.configure, text=texto, text_color=color)

        report = []
        try:
            gs_exe = self.find_ghostscript()
            if not gs_exe:
                estado("❌ Error: Falta Ghostscript", "red")
                self._en_ui(messagebox.showerror, "Falta Componente",
                            "Para una compresión segura y profesional, necesitas instalar Ghostscript.\n\n"
                            "1. Descárgalo de: ghostscript.com/download\n"
                            "2. Instálalo y reinicia la app.")
                return

            self._en_ui(self.pdf_prog_bar.set, 0)
            total_files = len(archivos)

            # --- MAPEO DE 4 NIVELES A GHOSTSCRIPT ---
            gs_preset, target_dpi = "/printer", 300          # 1. Ligera / Alta Calidad
            if "2." in sel_level:                             # 2. Equilibrada (Standard)
                gs_preset, target_dpi = "/ebook", 150
            elif "3." in sel_level:                           # 3. Alta Compresión
                gs_preset, target_dpi = "/screen", 72
            elif "4." in sel_level:                           # 4. Extrema: /screen con menos DPI
                gs_preset, target_dpi = "/screen", 50

            for idx, pdf_path in enumerate(archivos):
                base_name = os.path.splitext(os.path.basename(pdf_path))[0]
                out_path = None
                try:
                    if not os.path.exists(pdf_path):
                        report.append(f"{base_name}: ❌ El archivo ya no existe")
                        continue

                    folder = os.path.dirname(pdf_path)
                    if "PDF_OPTIMIZADO" in dest_choice:
                        folder = os.path.join(folder, "PDF_OPTIMIZADO")
                        os.makedirs(folder, exist_ok=True)
                    elif dest_choice.startswith("↗️") and self._ruta_destino(self.pdf_comp_dest_seg):
                        folder = self._ruta_destino(self.pdf_comp_dest_seg)
                    self._registrar_salida(self.pdf_comp_dest_seg, folder)

                    out_path = _ruta_unica(os.path.join(folder, f"{base_name}_opt.pdf"))
                    estado(f"Reconstruyendo {idx+1}/{total_files}...", "yellow")

                    ok_gs, detalle_gs = self._gs_comprimir(
                        gs_exe, pdf_path, out_path, gs_preset, target_dpi)

                    if ok_gs and os.path.isfile(out_path):
                        orig = os.path.getsize(pdf_path)
                        final = os.path.getsize(out_path)
                        if final >= orig:
                            # No redujo (PDF ya optimizado): no se entrega un archivo más pesado
                            os.remove(out_path)
                            report.append(
                                f"{base_name}: ⚠️ OMITIDO: ya estaba optimizado (habría quedado en "
                                f"{self._fmt_bytes(final)} y pesa {self._fmt_bytes(orig)}); "
                                f"se conservó el original.")
                        else:
                            perc = int(((orig - final) / orig) * 100) if orig > 0 else 0
                            msg = (f"¡Compresión exitosa!\n"
                                   f" Tamaño original: {self._fmt_bytes(orig)}  →  "
                                   f"Nuevo tamaño: {self._fmt_bytes(final)}  "
                                   f"(Reducción del {perc}%)")
                            print(f"✅ {base_name}: {msg}")
                            report.append(f"{base_name}: ✅  {msg}")
                    else:
                        print(f"❌ Error GS en {base_name}: {detalle_gs}")
                        if out_path and os.path.exists(out_path):
                            os.remove(out_path)
                        report.append(f"{base_name}: ❌ {detalle_gs or 'Ghostscript no pudo procesarlo'}")
                except Exception as e:
                    print(f"Error general PDF: {e}")
                    report.append(f"{base_name}: ❌ Error: {str(e)[:80]}")
                self._en_ui(self.pdf_prog_bar.set, (idx + 1) / total_files)

            estado("✅ Optimización Finalizada", "#2cc985")
            self._en_ui(self.show_summary, report, "Compresión de PDF")
        except Exception as e:
            print(f"Error general PDF: {e}")
            estado("Error Crítico", "red")
        finally:
            self._en_ui(self.pdf_btn_comp.configure, state="normal")
            self._trabajo_fin("pdf_comp")

    def handle_pdf_drop(self, event, mode):
        clean_files = self._rutas_drop(event)
        pdfs = [f for f in clean_files if f.lower().endswith('.pdf')]
        imgs = [f for f in clean_files if f.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.webp'))]

        if mode == "merge":
            if pdfs: self.pdf_merge_list.extend(pdfs); self.refresh_merge_ui()

        elif mode == "split":
            if pdfs:
                self.pdf_split_file = pdfs[0]
                self.split_drop_area.configure(text=f"Archivo: {os.path.basename(pdfs[0])}")
                self.split_btn.configure(state="normal")

        elif mode == "img_to_pdf":
            if imgs: self.convert_queue.extend(imgs); self.refresh_img_ui()

        elif mode == "pdf_to_img":
            if pdfs:
                self.convert_pdf_file = pdfs[0]
                self.pdf_conv_drop.configure(text=f"PDF Seleccionado:\n{os.path.basename(pdfs[0])}")

        elif mode == "compress":
            if pdfs:
                self.pdf_compress_files = pdfs
                count = len(pdfs)
                # Si es 1 muestra el nombre, si son varios la cantidad
                if count == 1:
                    txt_show = f"📄 {os.path.basename(pdfs[0])}"
                else:
                    txt_show = f"📂 {count} Archivos cargados"
                self.pdf_comp_lbl.configure(text="Archivos listos para optimizar")
                self.pdf_comp_drop.configure(text=txt_show)
                self.update_pdf_size_estimate()

    def select_files_pdf(self, mode):
        if mode == "merge":
            files = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
            if files: self.pdf_merge_list.extend(files); self.refresh_merge_ui()
            
        elif mode == "split":
            f = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
            if f: self.pdf_split_file = f; self.split_drop_area.configure(text=f"Archivo: {os.path.basename(f)}"); self.split_btn.configure(state="normal")
            
        elif mode == "img_to_pdf":
            files = filedialog.askopenfilenames(filetypes=[("Images", "*.jpg *.jpeg *.png *.webp *.bmp")])
            if files: self.convert_queue.extend(files); self.refresh_img_ui()
            
        elif mode == "pdf_to_img":
            f = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
            if f: self.convert_pdf_file = f; self.pdf_conv_drop.configure(text=f"PDF Seleccionado:\n{os.path.basename(f)}")
        
        # --- CORRECCIÓN AQUÍ ---
        elif mode == "compress":
            files = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
            if files:
                self.pdf_compress_files = list(files)
                count = len(files)
                
                if count == 1:
                    txt_show = f"📄 {os.path.basename(files[0])}"
                else:
                    txt_show = f"📂 {count} Archivos cargados"

                self.pdf_comp_lbl.configure(text="Archivos listos")
                self.pdf_comp_drop.configure(text=txt_show)
                self.update_pdf_size_estimate()
        # -------------------------

    # --- UI UNIR PDFS (Reordenar) ---
    def refresh_merge_ui(self):
        # 1. Limpiar la lista visual
        for widget in self.merge_list_frame.winfo_children():
            if widget != self.merge_placeholder:
                widget.destroy()

        self.pdf_merge_buttons = []
        self.pdf_merge_rows    = []

        # 2. Actualizar contador
        n = len(self.pdf_merge_list)
        if hasattr(self, 'merge_count_lbl'):
            self.merge_count_lbl.configure(
                text=f"{n} PDF{'s' if n != 1 else ''}",
                text_color=self.col_main if n > 0 else "#666"
            )

        # 3. Controlar placeholder
        if not self.pdf_merge_list:
            self.merge_placeholder.pack(expand=True, fill="both", pady=20)
            return
        else:
            self.merge_placeholder.pack_forget()

        # 4. Dibujar filas
        for i, path in enumerate(self.pdf_merge_list):
            row = ctk.CTkFrame(self.merge_list_frame, fg_color="transparent")
            row.pack(fill="x", pady=2, padx=5)
            self.pdf_merge_rows.append(row)

            # Drag handle
            drag_lbl = ctk.CTkLabel(row, text="⠿", text_color="#555",
                                    font=("Arial", 16), width=20, cursor="fleur")
            drag_lbl.pack(side="left", padx=(4, 0))

            name = f"{i+1}. {os.path.basename(path)}"
            btn = ctk.CTkButton(row, text=name, anchor="w",
                                fg_color="#2b2b2b", hover_color="#333",
                                border_width=1, border_color="#333", text_color="#eee",
                                command=lambda idx=i: self.select_pdf_item(idx))
            btn.pack(side="left", fill="x", expand=True)
            self.pdf_merge_buttons.append(btn)

            # Bindings en todos los widgets del row
            for w in (row, btn, drag_lbl):
                w.bind("<MouseWheel>", self._merge_scroll_child)
                w.bind("<Button-4>",   self._merge_scroll_child)
                w.bind("<Button-5>",   self._merge_scroll_child)
                w.bind("<ButtonPress-1>",   lambda e, idx=i: self._merge_drag_start(e, idx))
                w.bind("<B1-Motion>",       self._merge_drag_motion)
                w.bind("<ButtonRelease-1>", self._merge_drag_end)

    # ── Scroll forwarding para hijos del merge list ──────────────────────
    def _merge_scroll_child(self, event):
        try:
            canvas = self.merge_list_frame._parent_canvas
            if os.name == 'nt':
                canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
            else:
                canvas.yview_scroll(-1 if getattr(event, 'num', None) == 4 else 1, "units")
        except Exception:
            pass
        return "break"

    # ── Drag-to-reorder para merge list ──────────────────────────────────
    _merge_drag_from   = None
    _merge_drag_y0     = 0
    _merge_drag_active = False
    _MERGE_ROW_H       = 38   # altura aprox. de cada fila en merge

    def _merge_drag_start(self, event, index):
        self._merge_drag_from   = index
        self._merge_drag_y0     = event.y_root
        self._merge_drag_active = False
        self.select_pdf_item(index)

    def _merge_drag_motion(self, event):
        if self._merge_drag_from is None:
            return
        if not self._merge_drag_active:
            if abs(event.y_root - self._merge_drag_y0) < 6:
                return
            self._merge_drag_active = True

        delta  = event.y_root - self._merge_drag_y0
        target = self._merge_drag_from + int(delta / self._MERGE_ROW_H)
        target = max(0, min(target, len(self.pdf_merge_list) - 1))

        if hasattr(self, 'pdf_merge_buttons'):
            for j, b in enumerate(self.pdf_merge_buttons):
                if j == target and j != self._merge_drag_from:
                    b.configure(fg_color="#2a5c8a", border_color="#6cb4f5")
                elif j == self._merge_drag_from:
                    b.configure(fg_color="#4a1070", border_color="#a29bfe")
                else:
                    b.configure(fg_color="#2b2b2b", border_color="#333")

    def _merge_drag_end(self, event):
        if not self._merge_drag_active:
            self._merge_drag_active = False
            self._merge_drag_from   = None
            return

        self._merge_drag_active = False
        from_idx = self._merge_drag_from
        self._merge_drag_from = None

        if from_idx is None or not self.pdf_merge_list:
            return

        delta  = event.y_root - self._merge_drag_y0
        to_idx = from_idx + int(delta / self._MERGE_ROW_H)
        to_idx = max(0, min(to_idx, len(self.pdf_merge_list) - 1))

        if from_idx != to_idx:
            item = self.pdf_merge_list.pop(from_idx)
            self.pdf_merge_list.insert(to_idx, item)
            self.refresh_merge_ui()
            self.select_pdf_item(to_idx)
        else:
            self.refresh_merge_ui()
            self.select_pdf_item(from_idx)

    def select_pdf_item(self, index):
        self.pdf_selected_index = index
        # Restaurar colores
        for btn in self.pdf_merge_buttons:
            btn.configure(fg_color="transparent", border_color="#333")
        # Marcar seleccionado
        if 0 <= index < len(self.pdf_merge_buttons):
            self.pdf_merge_buttons[index].configure(fg_color="#b30b00", border_color="#ff4d4d")

    def move_pdf_item(self, direction):
        if self.pdf_selected_index is None: return
        idx = self.pdf_selected_index
        new_idx = idx + direction
        
        if 0 <= new_idx < len(self.pdf_merge_list):
            # Swap en la lista de datos
            self.pdf_merge_list[idx], self.pdf_merge_list[new_idx] = self.pdf_merge_list[new_idx], self.pdf_merge_list[idx]
            # Actualizar UI y mantener selección
            self.refresh_merge_ui()
            self.select_pdf_item(new_idx)
    

    def move_pdf_to_top(self):
        """Mueve el elemento seleccionado al inicio de la lista."""
        if self.pdf_selected_index is None: return
        idx = self.pdf_selected_index
        if idx == 0: return
        item = self.pdf_merge_list.pop(idx)
        self.pdf_merge_list.insert(0, item)
        self.refresh_merge_ui()
        self.select_pdf_item(0)

    def move_pdf_to_bottom(self):
        """Mueve el elemento seleccionado al final de la lista."""
        if self.pdf_selected_index is None: return
        idx = self.pdf_selected_index
        if idx == len(self.pdf_merge_list) - 1: return
        item = self.pdf_merge_list.pop(idx)
        self.pdf_merge_list.append(item)
        self.refresh_merge_ui()
        self.select_pdf_item(len(self.pdf_merge_list) - 1)

    def remove_pdf_item(self):
        if self.pdf_selected_index is None: return
        del self.pdf_merge_list[self.pdf_selected_index]
        self.pdf_selected_index = None
        self.refresh_merge_ui()

    # --- PROCESOS PDF (Threads) ---
    def start_merge_thread(self):
        if not self.pdf_merge_list:
            messagebox.showwarning("Alerta", "Añade al menos un PDF.")
            return
        if str(self.merge_btn.cget("state")) == "disabled":
            return
        self.merge_btn.configure(state="disabled")
        self.merge_status.configure(text="Uniendo y procesando...", text_color="yellow")
        self._trabajo_inicio("pdf_merge", "Unión de PDFs")
        threading.Thread(target=self.run_merge,
                         args=(list(self.pdf_merge_list), bool(self.var_merge_a4.get()),
                               bool(self.var_merge_landscape.get()), self.merge_dest_var.get()),
                         daemon=True).start()

    def run_merge(self, lista, use_a4, force_landscape, dest):
        """Hilo: une los PDF. La interfaz se toca solo con _en_ui."""
        def estado(texto, color):
            self._en_ui(self.merge_status.configure, text=texto, text_color=color)

        doc_out = None
        try:
            doc_out = fitz.open()
            for pdf_path in lista:
                if not os.path.exists(pdf_path):
                    estado(f"⛔ Falta archivo: {os.path.basename(pdf_path)}", "red")
                    return
                doc_src = fitz.open(pdf_path)
                try:
                    for page_src in doc_src:
                        if not use_a4:
                            # Modo Original: copia exacta
                            doc_out.insert_pdf(doc_src, from_page=page_src.number, to_page=page_src.number)
                        else:
                            # Modo A4 Forzado (puntos: 595 x 842)
                            target_w, target_h = (842, 595) if force_landscape else (595, 842)
                            page_out = doc_out.new_page(width=target_w, height=target_h)
                            page_out.show_pdf_page(fitz.Rect(0, 0, target_w, target_h), doc_src, page_src.number)
                finally:
                    doc_src.close()

            folder = os.path.dirname(lista[0])
            if "PDF_UNIDOS" in dest:
                folder = os.path.join(folder, "PDF_UNIDOS")
                os.makedirs(folder, exist_ok=True)
            elif "Elegir Otra" in dest and self._ruta_destino(self.merge_dest_seg):
                folder = self._ruta_destino(self.merge_dest_seg)
            self._registrar_salida(self.merge_dest_seg, folder)

            out = _ruta_unica(os.path.join(folder, "Unido_Completo.pdf"))
            doc_out.save(out)
            estado(f"¡Éxito! Archivo creado: {os.path.basename(out)}", self.col_accent)
        except Exception as e:
            estado(f"Error: {str(e)}", "red")
            print(e)
        finally:
            if doc_out is not None:
                try: doc_out.close()
                except Exception: pass
            self._en_ui(self.merge_btn.configure, state="normal")
            self._trabajo_fin("pdf_merge")

    def start_split_thread(self):
        if not self.pdf_split_file: return
        page_str = self.split_entry.get()
        if not page_str:
            messagebox.showerror("Error", "Escribe qué páginas quieres (ej: 1-5)")
            return
        if str(self.split_btn.cget("state")) == "disabled":
            return
        self.split_btn.configure(state="disabled")
        self._trabajo_inicio("pdf_split", "División de PDF")
        threading.Thread(target=self.run_split,
                         args=(page_str, self.pdf_split_file, self.split_dest_var.get()),
                         daemon=True).start()

    def run_split(self, page_str, pdf_file, dest_choice):
        """Hilo: extrae páginas. La interfaz se toca solo con _en_ui."""
        def estado(texto, color):
            self._en_ui(self.split_status.configure, text=texto, text_color=color)

        try:
            if not os.path.exists(pdf_file):
                estado("⛔ El archivo PDF ya no existe.", "red")
                return

            estado("Verificando rangos...", "yellow")
            self._en_ui(self.split_progress.set, 0)

            reader = PyPDF2.PdfReader(pdf_file)
            writer = PyPDF2.PdfWriter()
            total_pages = len(reader.pages)

            # 1. Interpretar lo que escribió el usuario (con candados de rango)
            pages_to_extract = set()
            error_msg = ""
            for part in page_str.split(','):
                part = part.strip()
                if not part: continue
                if '-' in part:                      # Rango (ej: 2-5)
                    try:
                        start, end = map(int, part.split('-'))
                        if start < 1 or end > total_pages:
                            error_msg = f"⛔ Error: El rango '{part}' es imposible.\nEl PDF solo tiene {total_pages} páginas."
                            break
                        if start > end:
                            error_msg = f"⛔ Error: El rango '{part}' está al revés."
                            break
                        for p in range(start, end + 1):
                            pages_to_extract.add(p - 1)
                    except ValueError:
                        error_msg = f"⛔ Error: '{part}' no es un formato válido."
                        break
                else:                                # Número suelto (ej: 8)
                    try:
                        p = int(part)
                        if p < 1 or p > total_pages:
                            error_msg = f"⛔ Error: Pides página {p}, pero el PDF solo tiene {total_pages}."
                            break
                        pages_to_extract.add(p - 1)
                    except ValueError:
                        error_msg = f"⛔ Error: '{part}' no es un número."
                        break

            if error_msg:
                estado(error_msg, "#ff4d4d")
                return

            sorted_pages = sorted(pages_to_extract)
            if not sorted_pages:
                estado("⛔ No escribiste ninguna página válida.", "#ff4d4d")
                return

            # 2. Extraer
            estado("Extrayendo páginas...", "yellow")
            for i, p_idx in enumerate(sorted_pages):
                writer.add_page(reader.pages[p_idx])
                self._en_ui(self.split_progress.set, (i + 1) / len(sorted_pages))

            # 3. Destino
            folder = os.path.dirname(pdf_file)
            base_name = os.path.splitext(os.path.basename(pdf_file))[0]
            if "PDF_SPLIT" in dest_choice:
                folder = os.path.join(folder, "PDF_SPLIT")
                os.makedirs(folder, exist_ok=True)
            elif "Elegir Otra" in dest_choice and self._ruta_destino(self.split_dest_seg):
                folder = self._ruta_destino(self.split_dest_seg)
            self._registrar_salida(self.split_dest_seg, folder)

            out = _ruta_unica(os.path.join(folder, f"{base_name}_extracto.pdf"))
            with open(out, "wb") as f:
                writer.write(f)

            self._en_ui(self.split_progress.set, 1)
            estado(f"¡Listo! Archivo creado: {os.path.basename(out)}", "#2cc985")
        except Exception as e:
            estado(f"Error Crítico: {str(e)}", "red")
        finally:
            self._en_ui(self.split_btn.configure, state="normal")
            self._trabajo_fin("pdf_split")


    def toggle_convert_ui(self, value):
        """Alterna entre los dos paneles dentro del contenedor"""
        if value == "Imágenes ➔ PDF":
            self.frame_pdf_to_img.pack_forget()
            self.frame_img_to_pdf.pack(fill="both", expand=True)
            self.conv_btn.configure(text="CREAR PDF DE IMÁGENES")
        else:
            self.frame_img_to_pdf.pack_forget()
            self.frame_pdf_to_img.pack(fill="both", expand=True)
            self.conv_btn.configure(text="EXTRAER IMÁGENES DE PDF")

    def refresh_img_ui(self):
        # Limpiar filas. El placeholder se CONSERVA: tiene los bindings de clic y de
        # arrastre (antes se recreaba sin ellos y dejaba de responder tras "✖ Todo").
        for widget in self.img_list_frame.winfo_children():
            if widget is not self.img_placeholder:
                widget.destroy()

        self.img_item_btns = []
        self.img_item_rows = []

        # Actualizar contador
        n = len(self.convert_queue)
        if hasattr(self, 'img_count_lbl'):
            self.img_count_lbl.configure(
                text=f"{n} imagen{'es' if n != 1 else ''}",
                text_color=self.col_main if n > 0 else "#666"
            )

        if not self.convert_queue:
            self.img_placeholder.pack(expand=True, fill="both", pady=20)
            return
        self.img_placeholder.pack_forget()

        for i, path in enumerate(self.convert_queue):
            # Contenedor Horizontal
            row = ctk.CTkFrame(self.img_list_frame, fg_color="transparent")
            row.pack(fill="x", pady=2)
            self.img_item_rows.append(row)

            # --- Icono de arrastre (drag handle) ---
            drag_lbl = ctk.CTkLabel(row, text="⠿", text_color="#555", font=("Arial", 16), width=20, cursor="fleur")
            drag_lbl.pack(side="left", padx=(4, 0))

            # --- Miniatura (caché persistente para rendimiento) ---
            try:
                tk_thumb = self.get_image_from_cache(path, (40, 40))
                if tk_thumb:
                    lbl_img = ctk.CTkLabel(row, text="", image=tk_thumb)
                    lbl_img.image = tk_thumb
                    lbl_img.pack(side="left", padx=5)
                else:
                    ctk.CTkLabel(row, text="❌").pack(side="left", padx=10)
            except Exception:
                ctk.CTkLabel(row, text="❌").pack(side="left", padx=10)

            # Botón seleccionable con el nombre
            btn = ctk.CTkButton(row, text=f"{i+1}. {os.path.basename(path)}", anchor="w", fg_color="#333",
                                hover_color="#444", height=45,
                                command=lambda idx=i: self.select_img_item(idx))
            btn.pack(side="left", fill="x", expand=True)
            self.img_item_btns.append(btn)

            # --- Bindings: scroll + drag-reorder en TODOS los widgets del row ---
            for w in (row, btn, drag_lbl):
                w.bind("<MouseWheel>", self._img_scroll_child)   # Windows
                w.bind("<Button-4>",   self._img_scroll_child)   # Linux ↑
                w.bind("<Button-5>",   self._img_scroll_child)   # Linux ↓
                w.bind("<ButtonPress-1>",   lambda e, idx=i: self._img_drag_start(e, idx))
                w.bind("<B1-Motion>",       self._img_drag_motion)
                w.bind("<ButtonRelease-1>", self._img_drag_end)

    # Variables selección imágenes
    pdf_img_selected_index = None

    def select_img_item(self, index):
        self.pdf_img_selected_index = index
        for btn in self.img_item_btns:
            btn.configure(fg_color="#333", border_width=0)
        if 0 <= index < len(self.img_item_btns):
            self.img_item_btns[index].configure(fg_color="#b30b00", border_width=1, border_color="white")

    def move_img_item(self, direction):
        if getattr(self, 'pdf_img_selected_index', None) is None: return
        idx = self.pdf_img_selected_index
        new_idx = idx + direction
        if 0 <= new_idx < len(self.convert_queue):
            self.convert_queue[idx], self.convert_queue[new_idx] = self.convert_queue[new_idx], self.convert_queue[idx]
            self.refresh_img_ui()
            self.select_img_item(new_idx)

    def remove_img_item(self):
        if getattr(self, 'pdf_img_selected_index', None) is None: return
        del self.convert_queue[self.pdf_img_selected_index]
        self.pdf_img_selected_index = None
        self.refresh_img_ui()
        
    def move_img_to_top(self):
        """Mueve la imagen seleccionada al inicio de la cola de conversión."""
        if getattr(self, 'pdf_img_selected_index', None) is None: return
        idx = self.pdf_img_selected_index
        if idx == 0: return
        item = self.convert_queue.pop(idx)
        self.convert_queue.insert(0, item)
        self.refresh_img_ui()
        self.select_img_item(0)

    def move_img_to_bottom(self):
        """Mueve la imagen seleccionada al final de la cola de conversión."""
        if getattr(self, 'pdf_img_selected_index', None) is None: return
        idx = self.pdf_img_selected_index
        if idx == len(self.convert_queue) - 1: return
        item = self.convert_queue.pop(idx)
        self.convert_queue.append(item)
        self.refresh_img_ui()
        self.select_img_item(len(self.convert_queue) - 1)

    # ------------------------------------------------------------------
    # HELPERS: Rueda del mouse en lista de imágenes
    # ------------------------------------------------------------------
    def _img_scroll_child(self, event):
        """Reenvía el scroll de la rueda desde hijos al canvas de CTkScrollableFrame."""
        try:
            canvas = self.img_list_frame._parent_canvas
            if os.name == 'nt':
                canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
            else:
                if getattr(event, 'num', None) == 4:
                    canvas.yview_scroll(-1, "units")
                else:
                    canvas.yview_scroll(1, "units")
        except Exception:
            pass
        return "break"

    # ------------------------------------------------------------------
    # HELPERS: Drag-to-reorder en lista de imágenes
    # ------------------------------------------------------------------
    _img_drag_from   = None
    _img_drag_y0     = 0
    _img_drag_active = False
    _IMG_ROW_H       = 51   # altura aprox. de cada fila (btn 45 + pady 2*2 + margen 2)

    def _img_drag_start(self, event, index):
        """Registra el inicio del arrastre."""
        self._img_drag_from   = index
        self._img_drag_y0     = event.y_root
        self._img_drag_active = False
        # Seleccionar el ítem al presionar (comportamiento normal de clic)
        self.select_img_item(index)

    def _img_drag_motion(self, event):
        """Dibuja feedback visual mientras se arrastra."""
        if self._img_drag_from is None:
            return
        # Activar drag solo si el mouse se movió > 6 px
        if not self._img_drag_active:
            if abs(event.y_root - self._img_drag_y0) < 6:
                return
            self._img_drag_active = True

        delta  = event.y_root - self._img_drag_y0
        target = self._img_drag_from + int(delta / self._IMG_ROW_H)
        target = max(0, min(target, len(self.convert_queue) - 1))

        # Resaltar destino visualmente
        if hasattr(self, 'img_item_btns'):
            for j, b in enumerate(self.img_item_btns):
                if j == target and j != self._img_drag_from:
                    b.configure(fg_color="#2a5c8a", border_width=1, border_color="#6cb4f5")
                elif j == self._img_drag_from:
                    b.configure(fg_color="#4a1070", border_width=1, border_color="#a29bfe")
                else:
                    b.configure(fg_color="#333", border_width=0)

    def _img_drag_end(self, event):
        """Realiza el reorden al soltar el mouse."""
        if not self._img_drag_active:
            self._img_drag_active = False
            self._img_drag_from   = None
            return

        self._img_drag_active = False
        from_idx = self._img_drag_from
        self._img_drag_from = None

        if from_idx is None or not self.convert_queue:
            return

        delta  = event.y_root - self._img_drag_y0
        to_idx = from_idx + int(delta / self._IMG_ROW_H)
        to_idx = max(0, min(to_idx, len(self.convert_queue) - 1))

        if from_idx != to_idx:
            item = self.convert_queue.pop(from_idx)
            self.convert_queue.insert(to_idx, item)
            self.refresh_img_ui()
            self.select_img_item(to_idx)
        else:
            # Sin cambio: solo limpiar colores
            self.refresh_img_ui()
            self.select_img_item(from_idx)
        
    def start_convert_thread(self):
        if str(self.conv_btn.cget("state")) == "disabled":
            return                                   # ya está trabajando (doble clic)
        mode = self.convert_mode.get()
        dest = self.conv_dest_var.get()
        if mode == "Imágenes ➔ PDF":
            if not self.convert_queue: return
            opciones = {
                "a4": bool(self.var_img_a4.get()),
                "margen": bool(self.var_img_margin.get()),
                "horizontal": bool(self.var_img_landscape.get()),
                "dpi": 300 if self.var_img_a4_dpi.get().startswith("300") else 150,
                "dest": dest,
            }
            destino, args = self.run_imgs_to_pdf, (list(self.convert_queue), opciones)
        else:
            if not self.convert_pdf_file: return
            destino, args = self.run_pdf_to_imgs, (self.convert_pdf_file, self.fmt_choice.get(), dest)
        self.conv_btn.configure(state="disabled")
        self._trabajo_inicio("pdf_conv", "Conversión PDF ⇄ imágenes")
        threading.Thread(target=destino, args=args, daemon=True).start()

    @staticmethod
    def _pdf_insertar_imagen(doc, path, op):
        """
        Agrega UNA imagen como página nueva de 'doc' (PyMuPDF). Solo esta imagen
        está decodificada en memoria. Las transparencias se componen sobre blanco.
          · Sin 'Forzar A4': página del tamaño de la imagen (1 px = 1 pt, como antes).
          · 'Forzar A4': hoja A4 real (595×842 pt) y la imagen a op['dpi'] (150/300).
        Un JPG que no necesita girarse ni reducirse se incrusta tal cual (sin recomprimir).
        El DPI elegido es un TECHO, no una meta: si la imagen trae menos resolución
        de la que pide ese DPI, se deja como está (nunca se amplía: inventar píxeles
        solo engordaría el PDF sin mejorar nada).
        Devuelve (se_redujo, dpi_real_en_la_hoja).
        """
        A4_W, A4_H = 595.28, 841.89
        with open(path, "rb") as fh:
            crudo = fh.read()
        with Image.open(io.BytesIO(crudo)) as im0:
            try:
                orientacion = im0.getexif().get(0x0112, 1) or 1
            except Exception:
                orientacion = 1
            jpg_directo = im0.format == "JPEG" and im0.mode in ("RGB", "L") and orientacion == 1
            img = ImageOps.exif_transpose(im0)
        w_px, h_px = img.size

        if op.get("a4"):
            pw, ph = (A4_H, A4_W) if op.get("horizontal") else (A4_W, A4_H)
            margen = min(pw, ph) * 0.05 if op.get("margen") else 0
            caja_w, caja_h = pw - 2 * margen, ph - 2 * margen
            escala = min(caja_w / w_px, caja_h / h_px)
            ancho_pt, alto_pt = w_px * escala, h_px * escala
            x0, y0 = margen + (caja_w - ancho_pt) / 2, margen + (caja_h - alto_pt) / 2
            rect = fitz.Rect(x0, y0, x0 + ancho_pt, y0 + alto_pt)
            dpi = int(op.get("dpi") or 150)
            max_w = max(1, round(ancho_pt / 72 * dpi))
            max_h = max(1, round(alto_pt / 72 * dpi))
            reducir = w_px > max_w * 1.02 or h_px > max_h * 1.02
            calidad = 90 if dpi >= 300 else 85
            # Resolución real que tendrá la imagen sobre la hoja
            dpi_real = dpi if reducir else round(min(w_px / max(ancho_pt / 72, 0.01),
                                                     h_px / max(alto_pt / 72, 0.01)))
        else:
            pw, ph = float(w_px), float(h_px)
            rect = fitz.Rect(0, 0, pw, ph)
            reducir, calidad, dpi_real = False, 90, None

        if jpg_directo and not reducir:
            datos = crudo
        else:
            if img.mode in ("RGBA", "LA") or (img.mode == "P" and "transparency" in img.info):
                rgba = img.convert("RGBA")
                fondo = Image.new("RGB", rgba.size, (255, 255, 255))
                fondo.paste(rgba, mask=rgba.split()[3])
                img = fondo
            elif img.mode not in ("RGB", "L"):
                img = img.convert("RGB")
            if reducir:
                img = img.resize((max_w, max_h), Image.Resampling.LANCZOS)
            buf = io.BytesIO()
            img.save(buf, format="JPEG", quality=calidad, optimize=True)
            datos = buf.getvalue()
        img = None

        page = doc.new_page(width=pw, height=ph)
        page.insert_image(rect, stream=datos)
        return reducir, dpi_real

    def run_imgs_to_pdf(self, lista, op):
        """
        Hilo: arma el PDF página por página con PyMuPDF. En memoria hay UNA sola
        foto decodificada a la vez (antes se cargaban todas a resolución completa
        y con muchas fotos se agotaba la RAM).
        """
        def estado(texto, color):
            self._en_ui(self.conv_status.configure, text=texto, text_color=color)

        doc = None
        try:
            estado("Procesando imágenes...", "yellow")
            doc = fitz.open()
            perdidas = 0
            reducidas = 0
            dpi_bajos = []          # las que ya venían por debajo del DPI elegido
            for n, path in enumerate(lista, start=1):
                if not os.path.exists(path):
                    print(f"Imagen perdida: {path}")
                    perdidas += 1
                    continue
                estado(f"Procesando imágenes... ({n}/{len(lista)})", "yellow")
                redujo, dpi_real = self._pdf_insertar_imagen(doc, path, op)
                if redujo:
                    reducidas += 1
                elif dpi_real:
                    dpi_bajos.append(dpi_real)

            if doc.page_count == 0:
                estado("⛔ No quedó ninguna imagen válida para crear el PDF.", "red")
                return

            folder = os.path.dirname(lista[0])
            dest = op.get("dest", "")
            if "PDF_CONV" in dest:
                folder = os.path.join(folder, "PDF_CONV")
                os.makedirs(folder, exist_ok=True)
            elif "Elegir Otra" in dest and self._ruta_destino(self.conv_dest_seg):
                folder = self._ruta_destino(self.conv_dest_seg)
            self._registrar_salida(self.conv_dest_seg, folder)

            out_path = _ruta_unica(os.path.join(folder, "Imagenes_Unidas.pdf"))
            doc.save(out_path, garbage=3, deflate=True)
            texto = f"¡PDF creado! {os.path.basename(out_path)} ({_plural_pag(doc.page_count)})"
            if op.get("a4"):
                # Qué pasó de verdad con el DPI elegido (es un techo, no una meta)
                dpi = int(op.get("dpi") or 150)
                if reducidas:
                    texto += f" · {reducidas} reducida(s) a {dpi} DPI"
                if dpi_bajos:
                    texto += (f" · {len(dpi_bajos)} ya estaba(n) por debajo de {dpi} DPI "
                              f"(se dejaron igual, la más baja a {min(dpi_bajos)} DPI)")
            if perdidas:
                texto += f" · {perdidas} imagen(es) ya no existía(n)"
            estado(texto, self.col_accent)
        except Exception as e:
            estado(f"Error: {str(e)}", "red")
            print(f"DEBUG ERROR: {e}")
        finally:
            if doc is not None:
                try: doc.close()
                except Exception: pass
            self._en_ui(self.conv_btn.configure, state="normal")
            self._trabajo_fin("pdf_conv")

    # DPI de salida para PDF -> Imagen.
    # 144 DPI = escala 2.0, exactamente la calidad que producía el fitz.Matrix(2, 2)
    # original, pero ahora expresado de forma explícita y no como un número mágico.
    PDF_IMG_DPI = 144

    def run_pdf_to_imgs(self, pdf_path, fmt, dest):
        """Hilo: exporta cada página como imagen. La interfaz se toca solo con _en_ui."""
        def estado(texto, color):
            self._en_ui(self.conv_status.configure, text=texto, text_color=color)

        doc = None
        try:
            if not os.path.exists(pdf_path):
                estado("⛔ El PDF origen no existe.", "red")
                return
            estado("Extrayendo imágenes...", "yellow")
            doc = fitz.open(pdf_path)

            folder = os.path.dirname(pdf_path)
            if "PDF_CONV" in dest:
                folder = os.path.join(folder, "PDF_CONV")
                os.makedirs(folder, exist_ok=True)
            elif "Elegir Otra" in dest and self._ruta_destino(self.conv_dest_seg):
                folder = self._ruta_destino(self.conv_dest_seg)
            self._registrar_salida(self.conv_dest_seg, folder)

            base_name = os.path.splitext(os.path.basename(pdf_path))[0]
            # PyMuPDF renderiza DIRECTO a la resolución final (72 DPI = escala 1.0)
            escala = self.PDF_IMG_DPI / 72.0
            mat = fitz.Matrix(escala, escala)

            total = len(doc)
            for i in range(total):
                page = doc.load_page(i)
                # alpha=False: páginas opacas (obligatorio para JPG)
                pix = page.get_pixmap(matrix=mat, alpha=False)
                out_path = _ruta_unica(os.path.join(folder, f"{base_name}_pag{i+1:03d}.{fmt}"))
                pix.save(out_path)
                pix = None
                estado(f"Extrayendo imágenes... ({i+1}/{total})", "yellow")

            estado(f"¡Listo! {total} imagen{'es' if total != 1 else ''} "
                   f"extraída{'s' if total != 1 else ''} a {self.PDF_IMG_DPI} DPI.", "#2cc985")
        except Exception as e:
            estado(f"Error: {str(e)}", "red")
            print(e)
        finally:
            if doc is not None:
                try: doc.close()
                except Exception: pass
            self._en_ui(self.conv_btn.configure, state="normal")
            self._trabajo_fin("pdf_conv")
        
    # ==========================================================================
    #   SECCIÓN 6: MÓDULO RENOMBRADOR (BOTÓN 4) - OPTIMIZADO
    # ==========================================================================
    # ── Caracteres prohibidos en nombres de archivo (Windows + POSIX) ─────────
    _FORBIDDEN_CHARS_RE = re.compile(r'[<>:"/\\|?*]')

    def _shield_renamer_entry(self, entry, var, post_cb):
        """
        Asocia `var` (StringVar) al `entry` y registra un trace que elimina
        en tiempo real cualquier carácter prohibido en nombres de archivo.
        El borrado es silencioso: el cursor no salta, no aparecen alertas.
        Llama a `post_cb()` tras cada limpieza para refrescar la preview.
        """
        entry.configure(textvariable=var)

        _cleaning = []   # bandera mutable para evitar re-entrada recursiva

        def _on_write(*_):
            if _cleaning:
                return
            raw = var.get()
            clean = self._FORBIDDEN_CHARS_RE.sub("", raw)
            if clean != raw:
                _cleaning.append(1)
                # Preservar posición de cursor en el widget interno
                try:
                    inner = entry._entry   # CTkEntry expone el tk.Entry interno
                    cur = inner.index("insert")
                    removed = sum(1 for c in raw[:cur] if self._FORBIDDEN_CHARS_RE.match(c))
                    var.set(clean)
                    inner.icursor(max(0, cur - removed))
                except Exception:
                    var.set(clean)
                finally:
                    _cleaning.clear()
            post_cb()

        var.trace_add("write", _on_write)
    # ─────────────────────────────────────────────────────────────────────────

    def init_renamer_module(self):
        # Configuración Inicial
        self.renamer_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.frames["RenamerTool"] = self.renamer_frame
        
        self.ren_col_main = "#582f87"
        self.renamer_files = [] 
        self.renamer_ui_cache = [] 
        self.renamer_selected_index = None 
        self.sort_descending = False 

        # --- HEADER (MODIFICADO: TÍTULO CENTRADO) ---
        top = ctk.CTkFrame(self.renamer_frame, fg_color="transparent", height=40)
        top.pack(fill="x", padx=20, pady=(10, 5))
        
        # Botón a la izquierda
        btn_back = ctk.CTkButton(top, text="← Menú", width=70, height=25, fg_color="transparent", border_width=1, 
                      command=lambda: self.show_frame("Menu"))
        btn_back.pack(side="left")
        
        # Título centrado absoluto (usando place para ignorar otros elementos)
        ctk.CTkLabel(top, text="Renombrador Masivo", font=(self.main_font, 20, "bold"), text_color="#a29bfe").place(relx=0.5, rely=0.5, anchor="center")

        # --- CONTENEDOR PRINCIPAL ---
        main_body = ctk.CTkFrame(self.renamer_frame, fg_color="transparent")
        main_body.pack(fill="both", expand=True, padx=20, pady=5)

        # === PANEL IZQUIERDO: CONFIGURACIÓN ===
        opts_panel = ctk.CTkFrame(main_body, width=300, fg_color="#222") 
        opts_panel.pack(side="left", fill="y", padx=(0, 10))
        
        # 1. NOMBRE BASE
        f_name = ctk.CTkFrame(opts_panel, fg_color="transparent")
        f_name.pack(fill="x", padx=10, pady=5)
        ctk.CTkLabel(f_name, text="Texto Base:", font=("Arial", 11, "bold")).pack(anchor="w")
        
        self.ren_base_entry = ctk.CTkEntry(f_name, height=28, placeholder_text="Vacío = Original")
        self.ren_base_entry.pack(fill="x", pady=2)
        self._ren_base_var = tk.StringVar()
        self._shield_renamer_entry(
            self.ren_base_entry, self._ren_base_var,
            lambda: self.enforce_renamer_rules(trigger="entry")
        )

        self.ren_ignore_name = ctk.BooleanVar(value=False)
        
        # --- [CAMBIO] SWITCH ROJITO ---
        self.switch_ignore = ctk.CTkSwitch(f_name, text="Ignorar Nombre Original", variable=self.ren_ignore_name, 
                      font=("Arial", 11, "bold"), 
                      progress_color="#c0392b",   # Rojo Intenso
                      button_color="#922b21",     # Rojo Oscuro (Botón)
                      fg_color="#444",
                      command=lambda: self.enforce_renamer_rules(trigger="ignore_switch"))
        self.switch_ignore.pack(pady=2, anchor="w")
        # ------------------------------
        
        # Prefijo / Sufijo
        grid_ps = ctk.CTkFrame(opts_panel, fg_color="transparent")
        grid_ps.pack(fill="x", padx=10, pady=2)
        ctk.CTkLabel(grid_ps, text="Prefijo:", font=("Arial", 10)).grid(row=0, column=0, sticky="w")
        self.ren_prefix_entry = ctk.CTkEntry(grid_ps, width=90, height=25)
        self.ren_prefix_entry.grid(row=1, column=0, padx=(0,5))
        self._ren_prefix_var = tk.StringVar()
        self._shield_renamer_entry(
            self.ren_prefix_entry, self._ren_prefix_var,
            self.update_renamer_preview
        )
        
        ctk.CTkLabel(grid_ps, text="Sufijo:", font=("Arial", 10)).grid(row=0, column=1, sticky="w")
        self.ren_suffix_entry = ctk.CTkEntry(grid_ps, width=90, height=25)
        self.ren_suffix_entry.grid(row=1, column=1)
        self._ren_suffix_var = tk.StringVar()
        self._shield_renamer_entry(
            self.ren_suffix_entry, self._ren_suffix_var,
            self.update_renamer_preview
        )

        ctk.CTkFrame(opts_panel, height=1, fg_color="#444").pack(fill="x", padx=10, pady=5)

        # 2. METADATOS
        f_meta = ctk.CTkFrame(opts_panel, fg_color="transparent")
        f_meta.pack(fill="x", padx=10, pady=2)
        ctk.CTkLabel(f_meta, text="Agregar Info Extra:", font=("Arial", 11, "bold")).pack(anchor="w")
        
        self.ren_meta_var = ctk.StringVar(value="Ninguno")
        meta_opts = ["Ninguno", "Fecha Creación", "Fecha Modificación", "Formato/Extensión"]
        ctk.CTkOptionMenu(f_meta, values=meta_opts, variable=self.ren_meta_var, 
                          height=25, fg_color="#333", button_color="#444",
                          command=lambda x: self.update_renamer_preview()).pack(fill="x", pady=2)

        # --- [CAMBIO] SELECTOR POSICIÓN INFO EXTRA ---
        self.ren_meta_pos = ctk.StringVar(value="Al Final")
        self.seg_meta_pos = ctk.CTkSegmentedButton(f_meta, values=["Al Inicio", "Al Final"], 
                                                   variable=self.ren_meta_pos, height=20,
                                                   selected_color=self.ren_col_main,
                                                   command=lambda x: self.update_renamer_preview())
        self.seg_meta_pos.pack(fill="x", pady=(2, 5))
        # ---------------------------------------------

        ctk.CTkFrame(opts_panel, height=1, fg_color="#444").pack(fill="x", padx=10, pady=5)

        # 3. SECUENCIA
        f_seq = ctk.CTkFrame(opts_panel, fg_color="transparent")
        f_seq.pack(fill="x", padx=10, pady=2)
        
        self.ren_seq_var = ctk.BooleanVar(value=True)
        self.switch_seq = ctk.CTkSwitch(f_seq, text="Activar Numeración", variable=self.ren_seq_var, 
                                        font=("Arial", 11, "bold"), progress_color="#00b894", 
                                        command=lambda: self.enforce_renamer_rules(trigger="seq_switch"))
        self.switch_seq.pack(anchor="w", pady=2)

        self.ren_seq_warning = ctk.CTkLabel(f_seq, text="", font=("Arial", 9, "italic"), text_color="orange", height=12)
        self.ren_seq_warning.pack(anchor="w", padx=35)

        self.ren_seq_pos = ctk.StringVar(value="Al Final")
        self.seg_pos = ctk.CTkSegmentedButton(f_seq, values=["Al Inicio", "Al Final"], variable=self.ren_seq_pos, 
                               height=25, selected_color="#00b894", command=lambda x: self.update_renamer_preview())
        self.seg_pos.pack(fill="x", pady=3)

        self.ren_seq_type = ctk.StringVar(value="Números (1, 2, 3...)")
        self.opt_seq_type = ctk.CTkOptionMenu(f_seq, values=["Números (1, 2, 3...)", "Letras (A, B, C...)"], 
                          variable=self.ren_seq_type, height=25, fg_color="#333", button_color="#444", 
                          command=lambda x: self.update_renamer_preview())
        self.opt_seq_type.pack(fill="x", pady=3)
        
        self.ren_space_var = ctk.BooleanVar(value=True)
        self.switch_space = ctk.CTkSwitch(opts_panel, text="Usar Espacio Separador", variable=self.ren_space_var,
                      font=("Arial", 11), progress_color=self.ren_col_main,
                      command=self.update_renamer_preview)
        self.switch_space.pack(padx=10, pady=5, anchor="w")

        ctk.CTkFrame(opts_panel, height=1, fg_color="#444").pack(fill="x", padx=10, pady=5)

        # 4. ESTILO DE TEXTO (mayúsculas/minúsculas/primera letra), aplicado
        # al final sobre el nombre completo ya armado (prefijo+base+sufijo+
        # metadata+secuencia), ignorando números y símbolos.
        f_case = ctk.CTkFrame(opts_panel, fg_color="transparent")
        f_case.pack(fill="x", padx=10, pady=2)
        ctk.CTkLabel(f_case, text="Estilo de Texto:", font=("Arial", 11, "bold")).pack(anchor="w")

        self.ren_case_var = ctk.StringVar(value="Normal")
        case_opts = ["Normal", "MAYÚSCULAS", "minúsculas", "Primera Letra Mayúscula"]
        ctk.CTkOptionMenu(f_case, values=case_opts, variable=self.ren_case_var,
                          height=25, fg_color="#333", button_color="#444",
                          command=lambda x: self.update_renamer_preview()).pack(fill="x", pady=2)

        ctk.CTkButton(opts_panel, text="📂 Seleccionar Archivos", 
                      fg_color="#333", hover_color="#444", border_width=1, border_color="#555",
                      command=self.select_renamer_files_dialog).pack(pady=(20, 10), padx=20, fill="x")


        # === PANEL DERECHO: LISTA + DROP ZONE ===
        self.ren_drop_zone = ctk.CTkFrame(main_body, fg_color="transparent", border_width=0)
        self.ren_drop_zone.pack(side="left", fill="both", expand=True)

        # HEADER LISTA
        ctrl_frame = ctk.CTkFrame(self.ren_drop_zone, fg_color="transparent", height=30)
        ctrl_frame.pack(fill="x", pady=5, padx=5)
        
        ctk.CTkButton(ctrl_frame, text="▲", width=25, height=25, fg_color="#333", command=lambda: self.move_renamer_item(-1)).pack(side="left", padx=1)
        ctk.CTkButton(ctrl_frame, text="▼", width=25, height=25, fg_color="#333", command=lambda: self.move_renamer_item(1)).pack(side="left", padx=1)
        
        self.ren_sort_criteria = ctk.StringVar(value="Nombre Original")
        sort_opts = ["Nombre Original", "Peso de Archivo", "Fecha Creación", "Fecha Modificación"]
        ctk.CTkOptionMenu(ctrl_frame, values=sort_opts, variable=self.ren_sort_criteria,
                          width=130, height=25, fg_color="#2b2b2b", button_color="#444", text_color="#ccc",
                          command=lambda x: self.sort_renamer_files()).pack(side="left", padx=(10, 2))
        
        self.btn_sort_dir = ctk.CTkButton(ctrl_frame, text="⬆ A-Z", width=60, height=25, 
                                          fg_color="#444", hover_color="#555",
                                          command=self.toggle_sort_direction)
        self.btn_sort_dir.pack(side="left", padx=2)
        # --- NUEVO CONTADOR ---
        self.ren_count_lbl = ctk.CTkLabel(ctrl_frame, text="0 Archivos", font=("Arial", 12, "bold"), text_color="#a29bfe")
        self.ren_count_lbl.pack(side="left", padx=15)
        # ----------------------
        ctk.CTkButton(ctrl_frame, text="🗑", width=30, height=25, fg_color="#b93b3b", hover_color="#8a2be2", 
                      command=self.remove_renamer_item).pack(side="right", padx=0)
        
        ctk.CTkButton(ctrl_frame, text="LIMPIAR", width=70, height=25, fg_color="#c92c2c", hover_color="#992222", 
                      font=("Arial", 11, "bold"),
                      command=self.clear_renamer).pack(side="right", padx=(0, 5))
        
        # ZONA DE LISTA
        # ============================================================
        # NUEVO SISTEMA: VIRTUAL LIST (CANVAS + POOL)
        # ============================================================
        
        # 1. Marco contenedor para el canvas y el scrollbar
        self.ren_virtual_frame = ctk.CTkFrame(self.ren_drop_zone, fg_color="#181818", border_width=2, border_color="#333")
        self.ren_virtual_frame.pack(fill="both", expand=True, padx=2, pady=2)
        
        # 2. Scrollbar (Manual)
        self.ren_v_scrollbar = ctk.CTkScrollbar(self.ren_virtual_frame, command=self.on_virtual_scroll_bar)
        self.ren_v_scrollbar.pack(side="right", fill="y")
        
        # 3. Canvas Nativo (Más rápido para virtualización que CTkScrollableFrame)
        # Nota: bg="#181818" debe coincidir con el fondo de tu tema
        self.ren_canvas = tk.Canvas(self.ren_virtual_frame, bg="#181818", highlightthickness=0, bd=0)
        self.ren_canvas.pack(side="left", fill="both", expand=True)
        
        # 4. Variables de Virtualización
        self.ROW_HEIGHT = 40       # Altura fija de cada fila en pixeles
        self.visible_rows = []     # Lista de objetos (referencias a widgets reciclables)
        self.total_data_count = 0  # Total de archivos en memoria
        
        # Bindings del Canvas
        self.ren_canvas.bind("<Configure>", self.on_virtual_resize)
        self.ren_canvas.bind("<MouseWheel>", self.on_virtual_mouse_wheel) # Windows
        self.ren_canvas.bind("<Button-4>", self.on_virtual_mouse_wheel)   # Linux Scroll Up
        self.ren_canvas.bind("<Button-5>", self.on_virtual_mouse_wheel)   # Linux Scroll Down

        # Label vacía (Placeholder) dentro del canvas
        self.ren_empty_id = self.ren_canvas.create_text(
            400, 200, 
            text="\n\n📂 Arrastra archivos aquí\n(O haz clic para buscar)", 
            fill="#555", font=("Arial", 14), justify="center"
        )
        
        # Bindings Drag & Drop sobre el Canvas
        self.ren_drop_zone.drop_target_register(DND_FILES)
        self.ren_drop_zone.dnd_bind('<<Drop>>', self.handle_renamer_drop)
        # Binding del click para buscar archivos
        self.ren_canvas.bind("<Button-1>", lambda e: self.check_click_empty(e))
        

        # ZONA INFERIOR
        action_bar = ctk.CTkFrame(self.renamer_frame, fg_color="transparent")
        action_bar.pack(fill="x", padx=20, pady=(5, 10))
        
        self.ren_prog_bar = ctk.CTkProgressBar(action_bar, height=10, progress_color=self.ren_col_main)
        self.ren_prog_bar.set(0)
        self.ren_prog_bar.pack(fill="x", pady=(0,5))
        
        self.ren_status = ctk.CTkLabel(action_bar, text="Esperando...", text_color="gray", font=("Arial", 12, "bold"))
        self.ren_status.pack(side="left", padx=5)

        self.ren_run_btn = ctk.CTkButton(action_bar, text="RENOMBRAR AHORA", width=180, height=35, 
                                         fg_color=self.ren_col_main, hover_color="#3e1f61", 
                                         font=(self.main_font, 13, "bold"), state="disabled",
                                         command=self.run_renamer_thread)
        self.ren_run_btn.pack(side="right")

        # Deshacer: devuelve el nombre original a TODOS los archivos del último
        # renombrado (se guarda en disco, así que funciona aunque cierres la app)
        self.ren_undo_btn = ctk.CTkButton(action_bar, text="↩ Deshacer último", width=170, height=35,
                                          fg_color="#2b2b2b", hover_color="#3a3a3a", border_width=1,
                                          border_color="#555", state="disabled",
                                          command=self.deshacer_renombrado)
        self.ren_undo_btn.pack(side="right", padx=(0, 10))
        
        self.enforce_renamer_rules(trigger="init")
        self._ren_actualizar_boton_deshacer()

    def enforce_renamer_rules(self, trigger=None):
        """
        Reglas de Oro:
        1. Ignorar Nombre ON -> Fuerza Numeración ON y Bloquea Switch.
        2. Texto Base con contenido -> Fuerza Numeración ON y Bloquea Switch.
        3. Numeración OFF -> Switch Espacio Bloqueado.
        """
        
        text_base_content = self._ren_base_var.get().strip()  # StringVar ya saneada por _shield_renamer_entry
        has_base_text = bool(text_base_content)
        is_ignore_on = self.ren_ignore_name.get()

        # REGLA: Si hay texto base, desactivar 'Ignorar Nombre' visualmente 
        # (ya que el texto base sobrescribe todo de todos modos)
        if trigger == "entry" and has_base_text:
            self.ren_ignore_name.set(False)
            is_ignore_on = False # Actualizamos variable local

        # CONDICIÓN MAESTRA: ¿Debemos forzar la numeración?
        # Se fuerza si: Se ignora el original O se escribió un texto base
        force_numbering = is_ignore_on or has_base_text

        if force_numbering:
            # Fuerza Numeración a ON
            if not self.ren_seq_var.get():
                self.ren_seq_var.set(True)
            
            # Bloquea el switch de numeración
            self.switch_seq.configure(state="disabled")
            
            # Advertencia no invasiva
            reason = "'Ignorar Original'" if is_ignore_on else "'Texto Base'"
            self.ren_seq_warning.configure(text=f"⚠ Requerido por {reason}")
        else:
            # Desbloqueamos el switch de numeración
            self.switch_seq.configure(state="normal")
            self.ren_seq_warning.configure(text="")

        # REGLA 3: Si Numeración está OFF -> Bloquear Espacio
        if not self.ren_seq_var.get():
            self.switch_space.configure(state="disabled")
        else:
            self.switch_space.configure(state="normal")

        # Actualizar visualmente los dropdowns
        self.toggle_renamer_controls()
        self.update_renamer_preview()









    def toggle_sort_direction(self):
        """Cambia entre Ascendente y Descendente"""
        self.sort_descending = not self.sort_descending
        
        # Actualizar texto del botón
        if self.sort_descending:
            self.btn_sort_dir.configure(text="⬇ Z-A")
        else:
            self.btn_sort_dir.configure(text="⬆ A-Z")
            
        # Re-ordenar automáticamente si ya hay un criterio
        self.sort_renamer_files()

    def sort_renamer_files(self, choice=None):
        """Ordena la lista y MANTIENE la selección del usuario siguiendo el archivo"""
        if not self.renamer_files: return
        
        if choice is None:
            choice = self.ren_sort_criteria.get()
            
        reverse = self.sort_descending
        
        # 1. GUARDAR LA RUTA DEL ARCHIVO SELECCIONADO (Identificador Único)
        selected_path = None
        if self.renamer_selected_index is not None and 0 <= self.renamer_selected_index < len(self.renamer_files):
            try:
                selected_path = self.renamer_files[self.renamer_selected_index]['path']
            except: pass

        # 2. ORDENAR
        key_func = None
        if choice == "Nombre Original":
            key_func = lambda x: os.path.basename(x['path']).lower()
        elif choice == "Peso de Archivo":
            key_func = lambda x: os.path.getsize(x['path']) if os.path.exists(x['path']) else 0
        elif choice == "Fecha Creación":
            key_func = lambda x: os.path.getctime(x['path']) if os.path.exists(x['path']) else 0
        elif choice == "Fecha Modificación":
            key_func = lambda x: os.path.getmtime(x['path']) if os.path.exists(x['path']) else 0
        
        if key_func:
            self.renamer_files.sort(key=key_func, reverse=reverse)
        
        # 3. RESTAURAR SELECCIÓN (Buscar dónde quedó el archivo original)
        self.renamer_selected_index = None # Reset por defecto
        if selected_path:
            for i, item in enumerate(self.renamer_files):
                if item['path'] == selected_path:
                    self.renamer_selected_index = i
                    break
            
        # Al reconstruir, update_renamer_preview leerá el nuevo índice correcto
        self.update_renamer_preview(rebuild=True)

    
    def toggle_renamer_controls(self):
        """Habilita/Deshabilita dropdowns visuales (parte de la Regla 3 visual)"""
        state = "normal" if self.ren_seq_var.get() else "disabled"
        
        # Solo poner en gris lo visual
        self.seg_pos.configure(state=state)
        self.opt_seq_type.configure(state=state)
    # --- LÓGICA DEL RENOMBRADOR ---

    def select_renamer_files_dialog(self):
        files = filedialog.askopenfilenames()
        if files:
            existing = {f['path'] for f in self.renamer_files}
            for f in files:
                if f not in existing:
                    self.renamer_files.append({'path': f, 'new_name': ''})
            self.update_renamer_preview(rebuild=True)

    def handle_renamer_drop(self, event):
        clean_files = self._rutas_drop(event)
        existing = {f['path'] for f in self.renamer_files}
        count = 0
        for f in clean_files:
            if os.path.isfile(f) and f not in existing:
                self.renamer_files.append({'path': f, 'new_name': ''})
                existing.add(f)
                count += 1
        if count > 0:
            self.update_renamer_preview(rebuild=True)

    def clear_renamer(self):
        self.renamer_files = []
        self.renamer_selected_index = None
        self.ren_base_entry.delete(0, 'end')
        self.ren_prefix_entry.delete(0, 'end')
        self.ren_suffix_entry.delete(0, 'end')
        
        # Limpieza Virtual
        self.ren_canvas.delete("all")
        self.visible_rows = [] 
        self.update_renamer_preview(rebuild=True)
    def number_to_alpha(self, n):
        string = ""
        while n >= 0:
            string = chr(n % 26 + 65) + string
            n = n // 26 - 1
        return string

    def _ren_apply_case(self, text, style):
        """
        Aplica el estilo de mayúsculas/minúsculas al nombre completo ya
        armado, afectando solo las letras. Números, espacios y símbolos
        quedan tal cual — no cuentan como "letra inicial de palabra", para
        evitar cosas como "video2024final" -> "Video2024Final" con el
        str.title() normal de Python.
        """
        if style == "MAYÚSCULAS":
            return text.upper()
        if style == "minúsculas":
            return text.lower()
        if style == "Primera Letra Mayúscula":
            return re.sub(r'[^\W\d_]+', lambda m: m.group(0).capitalize(), text)
        return text

    def update_renamer_preview(self, rebuild=False):
        """
        Versión OPTIMIZADA VIRTUAL.
        Solo calcula nombres en memoria y pide al renderizador virtual que actualice la vista.
        """
        base_text = self._ren_base_var.get()  # StringVar ya saneada, nunca contiene chars prohibidos
        prefix = self.ren_prefix_entry.get()  
        suffix = self.ren_suffix_entry.get()  
        
        ignore_original = self.ren_ignore_name.get()
        use_space = self.ren_space_var.get()
        sep = " " if use_space else ""
        
        meta_type = self.ren_meta_var.get()
        meta_pos = self.ren_meta_pos.get()
        
        use_seq = self.ren_seq_var.get()
        seq_pos = self.ren_seq_pos.get()
        seq_type = self.ren_seq_type.get()

        case_style = self.ren_case_var.get() if hasattr(self, 'ren_case_var') else "Normal"
        
        self.total_data_count = len(self.renamer_files)
        # --- ACTUALIZAR CONTADOR ---
        if hasattr(self, 'ren_count_lbl'):
            self.ren_count_lbl.configure(text=f"{self.total_data_count} Archivos")
        # ---------------------------

        if not self.renamer_files:
            # Mostrar mensaje vacío
            self.ren_run_btn.configure(state="disabled")
            self.ren_canvas.delete("all")
            self.visible_rows = [] # Reset pool
            self.ren_empty_id = self.ren_canvas.create_text(
                int(self.ren_canvas.winfo_width()/2), 200, 
                text="\n\n📂 Arrastra archivos aquí\n(O haz clic para buscar)", 
                fill="#555", font=("Arial", 14), justify="center"
            )
            return
        
        # Si hay archivos, borrar mensaje vacio si existe
        self.ren_canvas.delete(self.ren_empty_id)
        self.ren_run_btn.configure(state="normal")
        
        # 1. CÁLCULO DE NOMBRES (PURO DATO, MUY RÁPIDO)
        for i, item in enumerate(self.renamer_files):
            original_path = item['path']
            filename = os.path.basename(original_path)
            name_no_ext, ext = os.path.splitext(filename)
            
            if ignore_original:
                core_name = base_text
            else:
                core_name = base_text if base_text else name_no_ext
            
            full_core = f"{prefix}{core_name}{suffix}"

            # Metadatos
            meta_str = ""
            if meta_type != "Ninguno":
                try:
                    if "Creación" in meta_type:
                        ts = os.path.getctime(original_path)
                        dt = datetime.datetime.fromtimestamp(ts)
                        meta_str = dt.strftime("%d-%m-%Y")
                    elif "Modificación" in meta_type:
                        ts = os.path.getmtime(original_path)
                        dt = datetime.datetime.fromtimestamp(ts)
                        meta_str = dt.strftime("%d-%m-%Y")
                    elif "Formato" in meta_type:
                        meta_str = ext.replace(".", "").upper()
                except: meta_str = ""

            # Secuencia
            seq_str = ""
            if use_seq:
                seq_val = i 
                if "Letras" in seq_type:
                    seq_str = self.number_to_alpha(seq_val)
                else:
                    pad = len(str(self.total_data_count))
                    if pad < 2: pad = 2 
                    seq_str = str(seq_val + 1).zfill(pad)

            # Ensamblaje
            parts = []
            if use_seq and seq_pos == "Al Inicio": parts.append(seq_str)
            if meta_type != "Ninguno" and meta_pos == "Al Inicio": parts.append(meta_str)
            if full_core: parts.append(full_core)
            if meta_type != "Ninguno" and meta_pos == "Al Final": parts.append(meta_str)
            if use_seq and seq_pos == "Al Final": parts.append(seq_str)
            
            final_name_no_ext = sep.join([p for p in parts if p]).strip()
            if not final_name_no_ext: final_name_no_ext = "archivo"
            final_name_no_ext = self._ren_apply_case(final_name_no_ext, case_style)

            item['new_name'] = f"{final_name_no_ext}{ext}"

        # 1b. NOMBRES REPETIDOS en la misma carpeta: se marcan en rojo y no se deja renombrar
        conteo = {}
        for item in self.renamer_files:
            k = os.path.normcase(os.path.join(os.path.dirname(item['path']), item['new_name']))
            item['_clave_nueva'] = k
            conteo[k] = conteo.get(k, 0) + 1
        repetidos = 0
        for item in self.renamer_files:
            item['dup'] = conteo[item.pop('_clave_nueva')] > 1
            repetidos += item['dup']
        self._ren_aviso_repetidos(repetidos)

        # 2. RENDERIZADO VIRTUAL
        self.render_virtual_rows()

        # --- FIX PARA PROBLEMA 3: Forzar actualización de barra ---
        # "Sacudimos" la vista un pixel para que la barra recalcule su tamaño inmediatamente
        self.ren_canvas.yview_moveto(self.ren_canvas.yview()[0])
        # ----------------------------------------------------------

    def select_renamer_item(self, index):
        self.renamer_selected_index = index
        # Forzar redibujado de las filas visibles para actualizar el color de selección
        self.render_virtual_rows()

    def move_renamer_item(self, direction):
        if self.renamer_selected_index is None: return
        
        idx = self.renamer_selected_index
        new_idx = idx + direction
        
        if 0 <= new_idx < len(self.renamer_files):
            # 1. Swap en los datos
            self.renamer_files[idx], self.renamer_files[new_idx] = self.renamer_files[new_idx], self.renamer_files[idx]
            
            # 2. Actualizar el índice seleccionado para seguir al archivo
            self.renamer_selected_index = new_idx
            
            # 3. Actualizar visual (rebuild=False es más rápido aquí)
            self.update_renamer_preview(rebuild=False)


    def remove_renamer_item(self):
        if self.renamer_selected_index is None: return
        del self.renamer_files[self.renamer_selected_index]
        self.renamer_selected_index = None
        # Al borrar sí reconstruimos porque hay menos filas
        self.update_renamer_preview(rebuild=True)

    def _ren_aviso_repetidos(self, n):
        """Con nombres repetidos no se deja renombrar (se ven en rojo en la lista)."""
        if n:
            self.ren_run_btn.configure(state="disabled")
            self.ren_status.configure(text=f"⚠ {n} nombres repetidos (en rojo): cámbialos antes de renombrar",
                                      text_color="#ff5555")
            self._ren_hay_aviso = True
            return
        if not getattr(self, "_ren_ocupado", False):
            self.ren_run_btn.configure(state="normal")
        if getattr(self, "_ren_hay_aviso", False):
            self._ren_hay_aviso = False
            self.ren_status.configure(text="Esperando...", text_color="gray")

    @staticmethod
    def _ren_clave(ruta):
        return os.path.normcase(os.path.abspath(ruta))

    def _renombrar_lote(self, plan, progreso=None):
        """
        Renombra en DOS FASES para que un nombre nuevo nunca choque con otro
        archivo del mismo lote (p. ej. renumerar 01, 02, 03 en otro orden):
          1) cada archivo pasa a un nombre temporal único en su carpeta,
          2) y de ahí a su nombre final.
        Nunca se pisa un archivo existente.
        plan: [(ruta_actual, ruta_nueva)]
        Devuelve (hechos, errores): hechos=[(ruta_actual, ruta_nueva)], errores=[(ruta, motivo)].
        """
        clave = self._ren_clave
        errores = []
        # Lo que ya tiene su nombre final no se toca (pero sigue ocupando su nombre)
        plan = [(s, d) for s, d in plan if s != d]
        fuentes = {clave(s) for s, _ in plan}

        validos, destinos = [], set()
        for s, d in plan:
            k = clave(d)
            if not os.path.exists(s):
                errores.append((s, "el archivo ya no existe"))
            elif k in destinos:
                errores.append((s, f"otro archivo del lote también quedaría como «{os.path.basename(d)}»"))
            elif os.path.exists(d) and k not in fuentes:
                errores.append((s, f"ya existe un archivo llamado «{os.path.basename(d)}»"))
            else:
                destinos.add(k)
                validos.append((s, d))

        # Si un archivo del lote no se va a mover, su nombre sigue ocupado
        cambio = True
        while cambio:
            cambio = False
            quietos = fuentes - {clave(s) for s, _ in validos}
            siguen = []
            for s, d in validos:
                if clave(d) in quietos and clave(d) != clave(s):
                    errores.append((s, f"«{os.path.basename(d)}» es de otro archivo que no se pudo renombrar"))
                    cambio = True
                else:
                    siguen.append((s, d))
            validos = siguen

        total = max(1, len(validos) * 2)
        paso = 0

        def _avance():
            nonlocal paso
            paso += 1
            if progreso and (paso % 20 == 0 or paso == total):
                progreso(paso / total)

        # Fase 1: a nombres temporales
        temporales = []
        for s, d in validos:
            tmp = os.path.join(os.path.dirname(s), f".dmt_ren_{uuid.uuid4().hex[:12]}.tmp")
            try:
                os.rename(s, tmp)
                temporales.append((s, tmp, d))
            except OSError as e:
                errores.append((s, f"no se pudo renombrar ({e.strerror or e})"))
            _avance()

        # Fase 2: a los nombres finales
        hechos = []
        for s, tmp, d in temporales:
            try:
                if os.path.exists(d):
                    raise FileExistsError(f"ya existe «{os.path.basename(d)}»")
                os.rename(tmp, d)
                hechos.append((s, d))
            except OSError as e:
                motivo = e.strerror or str(e)
                # Vuelve a su nombre original (o a uno libre, si ese ya se ocupó)
                try:
                    os.rename(tmp, s)
                except OSError:
                    alterno = _ruta_unica(s)
                    try:
                        os.rename(tmp, alterno)
                        motivo += f"; quedó como «{os.path.basename(alterno)}»"
                    except OSError:
                        motivo += f"; quedó con el nombre temporal «{os.path.basename(tmp)}»"
                errores.append((s, motivo))
            _avance()
        return hechos, errores

    def _ren_ruta_deshacer(self):
        return os.path.join(_dmt_base_dir(), "renombrado_ultimo.json")

    def _ren_leer_deshacer(self):
        try:
            with open(self._ren_ruta_deshacer(), "r", encoding="utf-8") as fh:
                datos = json.load(fh)
            if isinstance(datos, dict) and datos.get("pares"):
                return datos
        except Exception:
            pass
        return None

    def _ren_guardar_deshacer(self, pares, fecha=None):
        """pares = [(ruta_actual, ruta_original)]. Lista vacía = borrar el registro."""
        ruta = self._ren_ruta_deshacer()
        try:
            if not pares:
                if os.path.exists(ruta):
                    os.remove(ruta)
                return
            datos = {"fecha": fecha or time.strftime("%d/%m/%Y %H:%M"),
                     "pares": [[a, o] for a, o in pares]}
            tmp = ruta + ".tmp"
            with open(tmp, "w", encoding="utf-8") as fh:
                json.dump(datos, fh, ensure_ascii=False)
            os.replace(tmp, ruta)
        except Exception as e:
            print(f"[Renombrador] No se pudo guardar el registro para deshacer: {e}")

    def _ren_actualizar_boton_deshacer(self):
        datos = self._ren_leer_deshacer()
        try:
            if datos and not getattr(self, "_ren_ocupado", False):
                self.ren_undo_btn.configure(state="normal",
                                            text=f"↩ Deshacer último ({len(datos['pares'])})")
            else:
                self.ren_undo_btn.configure(state="disabled", text="↩ Deshacer último")
        except Exception:
            pass

    def _ren_fin(self, hechos, errores, accion):
        """Hilo de la interfaz: resultado de renombrar o de deshacer."""
        verbo = "renombrados" if accion == "renombrar" else "con su nombre original"
        texto = f"✔ {len(hechos)} {verbo}"
        if errores:
            self.ren_status.configure(text=f"{texto} | ❌ {len(errores)} con error", text_color="#ff5555")
        else:
            self.ren_status.configure(text=texto, text_color="#2cc985")
        self._ren_hay_aviso = False
        self.renamer_files = []
        self.renamer_selected_index = None
        self.update_renamer_preview(rebuild=True)
        self.ren_prog_bar.set(0)
        self._ren_actualizar_boton_deshacer()
        if errores:
            reporte = [f"✅ {len(hechos)} archivo(s) {verbo} correctamente."]
            reporte += [f"{os.path.basename(s)}: ❌ {motivo}" for s, motivo in errores]
            self.show_summary(reporte, "Renombrador")

    def deshacer_renombrado(self):
        """Devuelve su nombre original a todos los archivos del último renombrado."""
        if getattr(self, "_ren_ocupado", False):
            return
        datos = self._ren_leer_deshacer()
        if not datos:
            messagebox.showinfo("Deshacer", "No hay ningún renombrado para deshacer.")
            self._ren_actualizar_boton_deshacer()
            return
        pares = [(a, o) for a, o in datos["pares"]]
        ejemplo = ""
        if pares:
            a0, o0 = pares[0]
            ejemplo = (f"\nPor ejemplo:\n   {os.path.basename(a0)}\n   →   {os.path.basename(o0)}\n")
        # Pregunta a prueba de clics accidentales: arranca en "No" y con icono de aviso
        if not messagebox.askyesno(
                "Deshacer último renombrado",
                f"¿Seguro que quieres deshacer el último renombrado?\n\n"
                f"Se les devolverá su nombre original a {len(pares)} archivo(s), "
                f"renombrados el {datos.get('fecha', '?')}.\n{ejemplo}\n"
                "Los que ya no existan o se hayan movido de carpeta se omitirán.\n\n"
                "Esta acción no se puede deshacer a su vez.",
                icon="warning", default="no"):
            return

        self._ren_ocupado = True
        self.ren_run_btn.configure(state="disabled")
        self.ren_undo_btn.configure(state="disabled")
        self.ren_status.configure(text="Deshaciendo...", text_color="#a29bfe")
        self._trabajo_inicio("renombrar", "Deshacer renombrado")

        def _process():
            hechos, errores = [], []
            try:
                hechos, errores = self._renombrar_lote(
                    pares, progreso=lambda f: self._en_ui(self.ren_prog_bar.set, f))
                # Lo que no se pudo deshacer pero sigue existiendo queda para reintentar
                pendientes = [(a, o) for a, o in pares
                              if a in {s for s, _ in errores} and os.path.exists(a)]
                self._ren_guardar_deshacer(pendientes, fecha=datos.get("fecha"))
            except Exception as e:
                errores.append(("(renombrador)", str(e)))
            finally:
                self._ren_ocupado = False
                self._trabajo_fin("renombrar")
                self._en_ui(self._ren_fin, hechos, errores, "deshacer")

        threading.Thread(target=_process, daemon=True).start()

    def run_renamer_thread(self):
        if not self.renamer_files or getattr(self, "_ren_ocupado", False):
            return
        if any(it.get('dup') for it in self.renamer_files):
            messagebox.showwarning("Nombres repetidos",
                                   "Hay archivos que quedarían con el mismo nombre (en rojo).\n"
                                   "Cámbialos antes de renombrar.")
            return
        plan = [(it['path'], os.path.join(os.path.dirname(it['path']), it['new_name']))
                for it in self.renamer_files]

        self._ren_ocupado = True
        self.ren_run_btn.configure(state="disabled")
        self.ren_undo_btn.configure(state="disabled")
        self.ren_status.configure(text="Procesando...", text_color="#a29bfe")
        self._trabajo_inicio("renombrar", "Renombrado de archivos")

        def _process():
            hechos, errores = [], []
            try:
                hechos, errores = self._renombrar_lote(
                    plan, progreso=lambda f: self._en_ui(self.ren_prog_bar.set, f))
                if hechos:
                    # Para deshacer: dónde quedó cada archivo y cómo se llamaba
                    self._ren_guardar_deshacer([(nuevo, orig) for orig, nuevo in hechos])
            except Exception as e:
                errores.append(("(renombrador)", str(e)))
            finally:
                self._ren_ocupado = False
                self._trabajo_fin("renombrar")
                self._en_ui(self._ren_fin, hechos, errores, "renombrar")

        threading.Thread(target=_process, daemon=True).start()


    # ==========================================================================
    #   SECCIÓN 8: UTILIDADES FFMPEG Y SYSTEM
    # ==========================================================================
        
    def get_duration(self, path):
        try:
            # Agregamos encoding y errors='ignore' aquí también
            r = subprocess.run(
                ["ffmpeg", "-i", path], 
                stderr=subprocess.PIPE, 
                stdout=subprocess.PIPE, 
                text=True, 
                encoding='utf-8', 
                errors='ignore', # Ignorar caracteres raros de FFMPEG
                startupinfo=self.get_startup_info()
            )
            m = re.search(r"Duration: (\d{2}):(\d{2}):(\d{2}\.\d{2})", r.stderr)
            if m: 
                return int(m.group(1))*3600 + int(m.group(2))*60 + float(m.group(3))
            return 0 # Si no encuentra duración, devuelve 0 (número), NO None
        except Exception as e: 
            print(f"Error Get Duration: {e}")
            return 0 # En caso de error, devuelve 0

    def get_audio_bitrate(self, path):
        # UTF-8: con metadatos en japonés o emojis, cp1252 fallaba y siempre devolvía 320
        try:
            r = subprocess.run(["ffmpeg", "-hide_banner", "-i", path], stderr=subprocess.PIPE,
                               stdout=subprocess.DEVNULL, text=True, encoding="utf-8", errors="replace",
                               startupinfo=self.get_startup_info(),
                               creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
            m = re.search(r"Audio:.*?, (\d+) kb/s", r.stderr)
            return int(m.group(1)) if m else 320
        except Exception:
            return 320

    def cancel_current_process(self, modo=None):
        """SALTAR: salta el archivo en curso de ESE módulo (los demás siguen)."""
        lote = self._lote_objetivo(modo)
        if lote is None or lote.modo == "suelto":
            return
        # 1. Activamos la bandera para que ese lote se detenga solo
        lote.saltar = True

        # 2. Feedback visual inmediato
        if lote.modo == "ocr":
            self._ocr_fase("saltando", "pagina" if self._ocr_fase_actual == "escaneando" else "")
        elif lote.modo == "transcribe":
            self.trans_status.configure(text="Deteniendo...", text_color="orange")
            # ¡NO BORRAMOS EL MODELO AQUÍ! Lo hará el hilo de trabajo para no crashear.
            self._whisper_detener_decodificacion()

        # 3. Matar el proceso externo de ESE lote (esto sí es seguro)
        if lote.proceso:
            try: lote.proceso.kill()
            except Exception: pass

    def show_summary(self, report, titulo=None):
        """
        Ventana de resumen. 'titulo' dice de qué módulo es: si terminan dos
        lotes a la vez (por ejemplo video e imágenes), cada uno abre la suya y
        se ve claramente cuál es cuál, sin pisarse.
        """
        # Geometría inteligente (más ancha si hay texto largo)
        max_char = 40
        for line in report:
            if len(line) > max_char: max_char = len(line)
        calc_width = int(max_char * 7) + 100
        final_width = max(500, min(950, calc_width))

        # 1. Configuración Ventana (nace oculta y aparece ya dibujada)
        summary = self._ventana_nueva(f"Resumen · {titulo}" if titulo else "Resumen de Procesos",
                                      final_width, 500, redimensionable=(True, True))

        # 2. Header / Logo
        title_frame = ctk.CTkFrame(summary, fg_color="transparent")
        title_frame.pack(pady=(15, 5), fill="x", padx=20)
        
        # Intentar cargar logo pequeño
        target_path = self.app_logo_png_path if os.path.exists(self.app_logo_png_path) else self.app_icon_path
        if os.path.exists(target_path):
            try:
                pil_raw = Image.open(target_path).convert("RGBA").resize((35, 35), Image.Resampling.LANCZOS)
                logo_img = ctk.CTkImage(light_image=pil_raw, dark_image=pil_raw, size=(35, 35))
                ctk.CTkLabel(title_frame, text="", image=logo_img).pack(side="left", padx=(10, 10))
            except: pass

        ctk.CTkLabel(title_frame, text=f"Reporte · {titulo}" if titulo else "Reporte de Finalización",
                     font=(self.main_font, 18, "bold"), text_color="white").pack(side="left")

        # 3. ÁREA DE LOG OPTIMIZADA
        # CAMBIO 1: Cambié el 12 por 14 en font para hacer la letra más grande
        log_box = ctk.CTkTextbox(summary, fg_color="#101010", text_color="#e0e0e0", 
                                 font=("Consolas", 14), activate_scrollbars=True)
        
        # CAMBIO 2: Esta línea agrega espacio (en píxeles) entre cada renglón
        # Puedes subir el 6 a 10 o 12 si quieres aún más separación.
        log_box._textbox.configure(spacing3=10) 

        log_box.pack(padx=20, pady=10, fill="both", expand=True)
        
        # --- EL TRUCO: TAGS DE COLORES ---
        # Accedemos al motor interno de Tkinter para definir colores
        log_box._textbox.tag_config("success", foreground="#2cc985") # Verde Matrix
        log_box._textbox.tag_config("warning", foreground="#f39c12") # Naranja
        log_box._textbox.tag_config("error", foreground="#e74c3c")   # Rojo
        log_box._textbox.tag_config("normal", foreground="#cccccc")  # Gris
        
        # Insertar texto masivamente
        log_box.configure(state="normal") # Habilitar escritura
        
        for ln in report:
            tag = "normal"
            if "✅" in ln: tag = "success"
            elif "SALTADO" in ln or "OMITIDO" in ln: tag = "warning"
            elif "❌" in ln or "Error" in ln: tag = "error"
            
            # Insertar línea con su etiqueta de color
            log_box.insert("end", f" {ln}\n", tag)
            
        log_box.configure(state="disabled") # Bloquear escritura (Solo lectura)

        # 4. Botones
        btn_frame = ctk.CTkFrame(summary, fg_color="transparent")
        btn_frame.pack(pady=10)

        def _copy_to_clipboard():
            summary.clipboard_clear()
            summary.clipboard_append("\n".join(report))
            messagebox.showinfo("Copiado", "Reporte copiado al portapapeles.")

        ctk.CTkButton(btn_frame, text="📋 Copiar", width=100, command=_copy_to_clipboard, 
                      fg_color="#333", hover_color="#444").pack(side="left", padx=5)
        
        ctk.CTkButton(btn_frame, text="Cerrar", width=100, command=summary.destroy, 
                      fg_color="#c0392b", hover_color="#a93226").pack(side="left", padx=5)

        # 5. Mostrar (ya centrada al crearla)
        self._ventana_mostrar(summary, recentrar=False)

        

    def get_startup_info(self):
        if os.name == 'nt':
            si = subprocess.STARTUPINFO()
            si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            return si
        return None



    def _trabajos_en_curso(self):
        """Lo que sigue trabajando ahora mismo (para avisar antes de cerrar la app)."""
        activos = []
        # Un lote por módulo: pueden ser varios a la vez
        for lote in list(getattr(self, "_lotes", {}).values()):
            activos.append(f"{lote.nombre} ({len(lote.cola)} archivo{'s' if len(lote.cola) != 1 else ''})")
        if getattr(self, "_yt_trans_ocupado", False):
            activos.append("Transcripción de YouTube")
        if getattr(self, "live_recording", False):
            activos.append("Transcripción en vivo (grabando)")
        n = sum(1 for d in list(getattr(self, "yt_downloads", {}).values())
                if d.get("status") == "active")
        if n:
            activos.append(f"{n} descarga{'s' if n != 1 else ''} en YouTube Downloader")
        if getattr(self, "_yt_updating", False):
            activos.append("Actualización de yt-dlp")
        if getattr(self, "meta_busy", False):
            activos.append("Editor de metadatos (guardando o sanitizando)")
        activos.extend(list(self._trabajos.values()))
        return activos

    def on_closing(self):
        activos = self._trabajos_en_curso()
        if activos:
            lista = "\n".join(f"• {a}" for a in activos)
            if not messagebox.askyesno(
                    "Cerrar DEUS MACHINA | TOOLS",
                    f"Todavía hay trabajo en curso:\n\n{lista}\n\n"
                    "Si cierras ahora se cancelará y lo que esté a medias se descartará.\n\n"
                    "¿Cerrar de todos modos?",
                    icon="warning", default="no"):
                return
        print("Cerrando aplicación...")

        # 1. Motor OCR (proceso aparte): se cierra para no dejarlo vivo con VRAM ocupada
        try:
            self.ocr_motor.cerrar()
        except Exception:
            pass
        
        # Procesos externos de TODOS los lotes en curso (FFmpeg, Ghostscript...)
        for proc in self._procesos_de_lotes() + [self.current_process]:
            if proc:
                try: proc.kill()
                except Exception: pass

        # FFmpeg / spotDL de las descargas y decodificadores de Whisper: que no
        # sigan trabajando solos después de cerrar la ventana
        for d in list(getattr(self, "yt_downloads", {}).values()):
            d["cancel_flag"] = True
            h = d.get("process_handle")
            if h is not None:
                try: h.kill()
                except Exception: pass
        try:
            self._whisper_detener_decodificacion()
        except Exception:
            pass

        # 2. LIMPIEZA DE EMERGENCIA (Transcripción)
        if getattr(self, 'current_temp_audio', None) and os.path.exists(self.current_temp_audio):
            try:
                os.remove(self.current_temp_audio)
                print(f"🧹 Temporal Transcripción eliminado.")
            except: pass

        # 3. LIMPIEZA DE EMERGENCIA (YouTube) <--- NUEVO BLOQUE
        if hasattr(self, 'yt_active_temps') and self.yt_active_temps:
            print(f"🧹 Limpiando {len(self.yt_active_temps)} descargas incompletas de YouTube...")
            for temp_dir in self.yt_active_temps:
                if os.path.exists(temp_dir):
                    try:
                        shutil.rmtree(temp_dir, ignore_errors=True)
                        print(f"   -> Eliminado: {temp_dir}")
                    except Exception as e:
                        print(f"   -> Error borrando {temp_dir}: {e}")

        # 4. Carpeta temporal de esta sesión (%TEMP%\DeusMachinaTools\sesion_<pid>)
        try:
            _dmt_borrar_temporales_sesion()
        except Exception:
            pass
        try:
            sys.stdout.flush()
            sys.stderr.flush()
        except Exception:
            pass

        self.destroy()
        os._exit(0)
        

    # ==========================================================================
    #   SECCIÓN 9: MÓDULO DE AUDIO (ESTILO VERDE)
    #  ------------------------------------------------------------------------
    #   SECCIÓN: MÓDULO CONVERTIDOR DE AUDIO (CON SELECTOR DE CALIDAD)
    # ==========================================================================

    def init_audio_module(self):
        self.audio_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.frames["AudioConverter"] = self.audio_frame
        
        # Colores del tema (Verde)
        c_main  = "#087000"
        c_hover = "#065000"
        c_bg_drop   = "#042004"
        c_bg_hover  = "#063006"

        # --- HEADER (Fuera del recuadro) ---
        top = ctk.CTkFrame(self.audio_frame, fg_color="transparent")
        top.pack(fill="x", padx=20, pady=10)
        ctk.CTkButton(top, text="← Menú", width=80, fg_color="transparent", border_width=1,
                      command=lambda: self.show_frame("Menu")).pack(side="left")

        title_bg = ctk.CTkFrame(self.audio_frame, fg_color="#2b2b2b", corner_radius=8)
        title_bg.pack(pady=5)
        ctk.CTkLabel(title_bg, text="Convertidor de Audio",
                     font=(self.main_font, 22, "bold"),
                     text_color="#0FAD04", bg_color="#2b2b2b").pack(padx=15, pady=8)

        # --- RECUADRO GRIS GRANDE (Tabview contenedor) ---
        self.audio_tabs = ctk.CTkTabview(
            self.audio_frame, width=900, height=550, fg_color="#222",
            segmented_button_selected_color=c_main,
            segmented_button_selected_hover_color=c_hover
        )
        self.audio_tabs.pack(pady=10, padx=40, fill="y", expand=True)

        # Pestaña única de contenido
        tab = self.audio_tabs.add("Convertidor")

        # --- ÁREA DE ARRASTRAR / SELECCIONAR ARCHIVOS ---
        self.audio_list_label = ctk.CTkLabel(tab, text="Ningún audio seleccionado", text_color="gray")
        self.audio_list_label.pack(pady=(5, 0))

        self.audio_drop_area = ctk.CTkButton(
            tab,
            text="🎵 Arrastra AUDIOS aquí\n(MP3, WAV, M4A, FLAC, OGG...)",
            width=600, height=80,
            fg_color=c_bg_drop, hover_color=c_bg_hover,
            border_color=c_main, border_width=2,
            command=lambda: self.select_files(
                [
                    ("Audios soportados", "*.mp3 *.wav *.m4a *.flac *.ogg *.wma *.aac *.opus *.ac3 *.aiff *.ape *.alac *.pcm"),
                    ("Todos los archivos", "*.*")
                ],
                self.audio_list_label, self.audio_drop_area
            )
        )
        self.audio_drop_area.pack(pady=10)
        self.audio_drop_area.drop_target_register(DND_FILES)
        self.audio_drop_area.dnd_bind(
            '<<Drop>>',
            lambda e: self.handle_drop(e, self.audio_list_label, self.audio_drop_area)
        )

        # --- OPCIONES ---
        opts = ctk.CTkFrame(tab, fg_color="transparent")
        opts.pack(pady=10, ipadx=30)

        # ── ROW 1: Selector de Formato (sin cambios) ──────────────────────────
        row1 = ctk.CTkFrame(opts, fg_color="transparent")
        row1.pack(pady=(10, 4))
        ctk.CTkLabel(row1, text="Formato Salida:").pack(side="left", padx=5)

        self.audio_format_var = ctk.StringVar(value="mp3")
        audio_formats = ["mp3", "wav", "m4a (aac)", "m4a (alac)", "ac3", "aiff", "wma", "opus", "ogg", "flac"]
        ctk.CTkOptionMenu(
            row1, values=audio_formats, variable=self.audio_format_var,
            width=180, fg_color=c_main, button_color=c_hover
        ).pack(side="left", padx=10)

        # ── ROW 2: NUEVO — Selector de Calidad / Peso ─────────────────────────
        row2 = ctk.CTkFrame(opts, fg_color="transparent")
        row2.pack(pady=(4, 10))
        ctk.CTkLabel(row2, text="Calidad / Peso:  ").pack(side="left", padx=5)

        self.audio_quality_var = ctk.StringVar(value="🔒 Mantener Calidad Original")
        quality_options = [
            "🔒 Mantener Calidad Original",
            "⚡ Optimizado  (Alta Calidad / Menor Peso)",
            "📱 Estándar  (Calidad Media / Peso Medio)",
            "🪶 Ligero  (Calidad Baja / Peso Bajo)",
        ]
        ctk.CTkOptionMenu(
            row2, values=quality_options, variable=self.audio_quality_var,
            width=280, fg_color=c_main, button_color=c_hover
        ).pack(side="left", padx=10)

        # ── HINT DINÁMICO: aparece cuando el formato destino es lossless ──────
        # Se actualiza automáticamente al cambiar cualquiera de los dos selectores.
        self.audio_quality_hint = ctk.CTkLabel(
            opts, text="", font=("Arial", 11), text_color="gray"
        )
        self.audio_quality_hint.pack(pady=(0, 4))

        # Vinculamos el callback a ambas variables para que reaccione en tiempo real
        self.audio_format_var.trace_add("write", lambda *_: self._update_audio_quality_hint())
        self.audio_quality_var.trace_add("write", lambda *_: self._update_audio_quality_hint())
        # ──────────────────────────────────────────────────────────────────────

        # --- DESTINO ---
        dest = ctk.CTkFrame(opts, fg_color="transparent")
        dest.pack(pady=(5))
        ctk.CTkLabel(dest, text="Guardar en:").pack(pady=5)
        self.audio_dest_var = ctk.StringVar(value="📄 Misma Carpeta")

        fila_audio = ctk.CTkFrame(dest, fg_color="transparent")
        fila_audio.pack()
        self.audio_dest_seg = ctk.CTkSegmentedButton(
            fila_audio,
            values=["📄 Misma Carpeta", "📁 Carpeta 'AUDIO_CONV'", "↗️ Elegir Otra..."],
            variable=self.audio_dest_var,
            selected_color=c_main, selected_hover_color=c_hover,
            command=lambda v: self.on_dest_change(
                v, self.audio_custom_path_label, self.audio_dest_seg
            )
        )
        self.audio_dest_seg.pack(side="left")
        self._boton_abrir_destino(fila_audio, self.audio_dest_seg, "AUDIO_CONV",
                                  lambda: self.file_queue if self.mode == "audio" else []
                                  ).pack(side="left", padx=(8, 0))
        self.audio_custom_path_label = ctk.CTkLabel(
            dest, text="", text_color="gray", font=("Arial", 10)
        )
        self.audio_custom_path_label.pack()

        # --- BARRA DE PROGRESO ---
        self.audio_progress_frame = ctk.CTkFrame(tab, fg_color="transparent")
        self.audio_progress_frame.pack(fill="x", padx=50, pady=10)
        self.audio_counter_label = ctk.CTkLabel(
            self.audio_progress_frame, text="", font=(self.main_font, 16, "bold")
        )
        self.audio_counter_label.pack()

        self.audio_progress_bar = ctk.CTkProgressBar(
            self.audio_progress_frame, width=500, height=15, progress_color=c_main
        )
        self.audio_progress_bar.set(0)
        self.audio_progress_bar.pack(pady=5)
        self.audio_status_label = ctk.CTkLabel(
            self.audio_progress_frame, text="Listo", text_color="gray"
        )
        self.audio_status_label.pack()

        # --- BOTONES DE ACCIÓN ---
        actions = ctk.CTkFrame(tab, fg_color="transparent")
        actions.pack(pady=10)

        self.audio_convert_btn = ctk.CTkButton(
            actions, text="CONVERTIR AUDIOS", height=45, width=200,
            fg_color=c_main, hover_color=c_hover,
            font=(self.main_font, 14, "bold"),
            command=lambda: self.start_batch_thread("audio")
        )
        self.audio_convert_btn.pack(side="left", padx=10)

        self.audio_cancel_btn = ctk.CTkButton(
            actions, text="SALTAR", height=45, width=150,
            fg_color="#c92c2c", hover_color="#992222", state="disabled",
            command=lambda: self.cancel_current_process("audio")
        )
        self.audio_cancel_btn.pack(side="left", padx=10)


    def convert_audio_logic(self, source_path):
        out_path = ""

        # --- 0. VERIFICACIÓN DE SEGURIDAD ---
        if not os.path.exists(source_path):
            return False, "❌ ARCHIVO NO ENCONTRADO (¿Se movió?)"

        try:
            # ── 1. LEER SELECCIONES DEL USUARIO ───────────────────────────────
            selection = self.audio_format_var.get()       # Formato destino
            quality   = self.audio_quality_var.get()      # Modo calidad/peso

            # Mapeamos el label visual a una clave interna corta para los if/elif
            # que construyen los codec_args más abajo.
            if   "Optimizado" in quality: mode = "optimized"
            elif "Estándar"   in quality: mode = "standard"
            elif "Ligero"     in quality: mode = "light"
            else:                         mode = "original"   # default / "Mantener Calidad"

            # ── 2. DETERMINAR EXTENSIÓN Y CODEC_ARGS ─────────────────────────
            #
            # REGLA 1 ► Los formatos LOSSLESS (WAV, AIFF, ALAC) ignoran el modo
            #            y siempre usan los parámetros de "Mantener Calidad Original".
            #            No se baja el sample rate ni se degrada de ninguna forma.
            #
            # REGLA 2 ► MP3 Modo Estándar usa VBR -q:a 5 (NO CBR 128k).
            #
            # REGLA 3 ► Modo Ligero en formatos con pérdida añade -ac 1 (mono)
            #            para evitar artefactos metálicos/burbujeantes a bitrates bajos.
            #
            # REGLA 4 ► FLAC: compression_level máximo = 8.
            #            Modo 2 → nivel 5 | Modo 3 → nivel 7 | Modo 4 → nivel 8.

            tgt_ext    = "mp3"
            codec_args = []

            # ── MP3 ───────────────────────────────────────────────────────────
            if selection == "mp3":
                tgt_ext = "mp3"
                if mode == "original":
                    # VBR alta calidad, ~190-250 kbps
                    codec_args = ["-acodec", "libmp3lame", "-q:a", "2"]
                elif mode == "optimized":
                    # VBR ligeramente inferior, ~175-210 kbps, imperceptible
                    codec_args = ["-acodec", "libmp3lame", "-q:a", "3"]
                elif mode == "standard":
                    # REGLA 2: VBR estándar moderno ~128-160 kbps (mejor que CBR 128k)
                    codec_args = ["-acodec", "libmp3lame", "-q:a", "5"]
                elif mode == "light":
                    # REGLA 3: Mono + bitrate bajo para minimizar artefactos
                    codec_args = ["-acodec", "libmp3lame", "-b:a", "64k", "-ar", "22050", "-ac", "1"]

            # ── WAV ──────────────────────────────────────────────────────────
            elif selection == "wav":
                tgt_ext = "wav"
                # REGLA 1: Lossless — siempre Modo Original, sin excepción
                codec_args = ["-acodec", "pcm_s16le"]

            # ── M4A (AAC) — con pérdida ───────────────────────────────────────
            elif "aac" in selection:
                tgt_ext = "m4a"
                if mode == "original":
                    # Lógica dinámica AAC escalonada:
                    # ≤192k → 192k | 193-256k → 256k | >256k → 320k
                    src_kbps = self.get_audio_bitrate(source_path)
                    if   src_kbps <= 192: final_bitrate = "192k"
                    elif src_kbps <= 256: final_bitrate = "256k"
                    else:                 final_bitrate = "320k"
                    print(f"DEBUG AAC original: fuente {src_kbps}kbps → destino {final_bitrate}")
                    codec_args = ["-acodec", "aac", "-b:a", final_bitrate]
                elif mode == "optimized":
                    # Alta calidad fija, AAC a 192k es casi transparente
                    codec_args = ["-acodec", "aac", "-b:a", "192k"]
                elif mode == "standard":
                    # Estándar móvil/red
                    codec_args = ["-acodec", "aac", "-b:a", "128k"]
                elif mode == "light":
                    # REGLA 3: Mono para evitar artefactos a bitrate bajo
                    codec_args = ["-acodec", "aac", "-b:a", "64k", "-ar", "22050", "-ac", "1"]

            # ── M4A (ALAC) — lossless ─────────────────────────────────────────
            elif "alac" in selection:
                tgt_ext = "m4a"
                # REGLA 1: Lossless — siempre Modo Original, sin excepción
                codec_args = ["-acodec", "alac"]

            # ── FLAC — lossless (compresión sin pérdida) ─────────────────────
            elif selection == "flac":
                tgt_ext = "flac"
                if mode == "original":
                    # Compresión por defecto de ffmpeg (≈ nivel 5)
                    codec_args = ["-acodec", "flac"]
                elif mode == "optimized":
                    # REGLA 4: Nivel 5 — balance velocidad/tamaño
                    codec_args = ["-acodec", "flac", "-compression_level", "5"]
                elif mode == "standard":
                    # REGLA 4: Nivel 7 — mayor compresión, mismo audio
                    codec_args = ["-acodec", "flac", "-compression_level", "7"]
                elif mode == "light":
                    # REGLA 4: Nivel 8 máximo absoluto (>8 no vale el coste de CPU)
                    codec_args = ["-acodec", "flac", "-compression_level", "8"]

            # ── OGG (Vorbis) — con pérdida ────────────────────────────────────
            elif selection == "ogg":
                tgt_ext = "ogg"
                if mode == "original":
                    # VBR ~220 kbps, alta fidelidad (corregido: q:a 7 es el techo)
                    codec_args = ["-acodec", "libvorbis", "-q:a", "7"]
                elif mode == "optimized":
                    # VBR ~160 kbps, muy buena calidad con menor peso
                    codec_args = ["-acodec", "libvorbis", "-q:a", "5"]
                elif mode == "standard":
                    # VBR ~128 kbps, buen equilibrio
                    codec_args = ["-acodec", "libvorbis", "-q:a", "4"]
                elif mode == "light":
                    # REGLA 3: Mono + calidad mínima ~80 kbps
                    codec_args = ["-acodec", "libvorbis", "-q:a", "1", "-ac", "1"]

            # ── OPUS — con pérdida ────────────────────────────────────────────
            elif selection == "opus":
                tgt_ext = "opus"
                if mode == "original":
                    codec_args = ["-acodec", "libopus", "-b:a", "128k"]
                elif mode == "optimized":
                    # Opus es muy eficiente; 128k ya es casi referencia
                    codec_args = ["-acodec", "libopus", "-b:a", "128k"]
                elif mode == "standard":
                    # Opus a 96k supera en calidad a MP3 a 128k
                    codec_args = ["-acodec", "libopus", "-b:a", "96k"]
                elif mode == "light":
                    # REGLA 3: Opus brilla a 32k en mono (ideal para voz)
                    codec_args = ["-acodec", "libopus", "-b:a", "32k", "-ac", "1"]

            # ── WMA — con pérdida ─────────────────────────────────────────────
            elif selection == "wma":
                tgt_ext = "wma"
                if mode == "original":
                    codec_args = ["-acodec", "wmav2", "-b:a", "192k"]
                elif mode == "optimized":
                    codec_args = ["-acodec", "wmav2", "-b:a", "160k"]
                elif mode == "standard":
                    codec_args = ["-acodec", "wmav2", "-b:a", "128k"]
                elif mode == "light":
                    # REGLA 3: Mono para audio limpio a bitrate bajo
                    codec_args = ["-acodec", "wmav2", "-b:a", "64k", "-ac", "1"]

            # ── AC3 (Dolby Digital) — con pérdida ────────────────────────────
            elif selection == "ac3":
                tgt_ext = "ac3"
                if mode == "original":
                    codec_args = ["-acodec", "ac3", "-b:a", "192k"]
                elif mode == "optimized":
                    codec_args = ["-acodec", "ac3", "-b:a", "192k"]
                elif mode == "standard":
                    codec_args = ["-acodec", "ac3", "-b:a", "128k"]
                elif mode == "light":
                    # REGLA 3: Mono + mínimo razonable para AC3
                    codec_args = ["-acodec", "ac3", "-b:a", "96k", "-ac", "1"]

            # ── AIFF — lossless ───────────────────────────────────────────────
            elif selection == "aiff":
                tgt_ext = "aiff"
                # REGLA 1: Lossless — siempre Modo Original, sin excepción
                codec_args = ["-acodec", "pcm_s16be"]

            # ── 3. CANDADO: evitar convertir un archivo al mismo formato ──────
            src_ext = os.path.splitext(source_path)[1].lower().replace('.', '')

            # Para m4a se permite cambio de codec interno (AAC ↔ ALAC), por eso la excepción
            if src_ext == tgt_ext and tgt_ext != "m4a":
                msg = f"⚠️ Ya es {tgt_ext.upper()}"
                self._en_ui(self.audio_progress_bar.set, 1)
                self._en_ui(self.audio_status_label.configure, text=msg, text_color="#e6b800")
                time.sleep(1.0)
                return True, f"OMITIDO ({msg})"

            # ── 4. PREPARAR CARPETA DE DESTINO ───────────────────────────────
            folder = os.path.dirname(source_path)
            if "AUDIO_CONV" in self.audio_dest_var.get():
                folder = os.path.join(folder, "AUDIO_CONV")
                os.makedirs(folder, exist_ok=True)
            elif self.audio_dest_var.get().startswith("↗️") and self._ruta_destino(self.audio_dest_seg):
                folder = self._ruta_destino(self.audio_dest_seg)
            self._registrar_salida(self.audio_dest_seg, folder)

            # Nunca se escribe sobre un archivo existente: en M4A -> M4A con
            # "Misma Carpeta" la salida era el propio original y FFmpeg lo
            # truncaba mientras lo leía (se perdía la canción).
            out_path = _ruta_unica(os.path.join(
                folder,
                f"{os.path.splitext(os.path.basename(source_path))[0]}.{tgt_ext}"
            ))

            # ── 5. CONSTRUIR COMANDO FFMPEG (con portadas y metadatos) ────────
            cmd = ["ffmpeg", "-y", "-i", source_path]

            # Formatos que soportan portada embebida (attached_pic).
            # WAV, OPUS, AC3 y AIFF son contenedores de audio puro:
            # añadirles -map 0:v? o -c:v copy hace que ffmpeg aborte.
            SUPPORTS_COVER = {"mp3", "m4a", "flac", "ogg", "wma"}

            # Mapeo de streams
            cmd.extend(["-map", "0:a:0"])               # Audio principal (siempre)
            if tgt_ext in SUPPORTS_COVER:
                cmd.extend(["-map", "0:v?"])            # Portada (solo si el contenedor la soporta)

            # Metadatos completos
            cmd.extend(["-map_metadata",     "0"])
            cmd.extend(["-map_metadata:s:a", "0:s:a"])
            cmd.extend(["-map_chapters",     "0"])

            # Códec de audio (con los parámetros del modo elegido)
            cmd.extend(codec_args)

            # Portada: copiar y etiquetar SOLO para formatos compatibles
            if tgt_ext in SUPPORTS_COVER:
                cmd.extend(["-c:v", "copy", "-disposition:v:0", "attached_pic"])

            cmd.append(out_path)

            # ── 6. EJECUTAR Y REPORTAR PROGRESO ──────────────────────────────
            dur = self.get_duration(source_path)

            # UTF-8: FFmpeg imprime los metadatos (títulos en japonés, emojis...)
            # en UTF-8; leerlos como cp1252 lanzaba UnicodeDecodeError y dejaba
            # a FFmpeg corriendo en segundo plano.
            proc = self.current_process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                universal_newlines=True, encoding="utf-8", errors="replace",
                startupinfo=self.get_startup_info(),
                creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0)
            )

            try:
                ultimo_ui = 0.0
                for line in proc.stdout:
                    if dur:
                        tm = re.search(r"time=(\d{2}):(\d{2}):(\d{2}\.\d{2})", line)
                        if tm and time.time() - ultimo_ui >= 0.25:
                            ultimo_ui = time.time()
                            h, m, s = tm.groups()
                            sec  = int(h) * 3600 + int(m) * 60 + float(s)
                            prog = min(1.0, sec / dur)
                            self._en_ui(self.audio_progress_bar.set, prog)
                            self._en_ui(self.audio_status_label.configure,
                                        text=f"Convirtiendo: {int(prog * 100)}%",
                                        text_color="yellow")
                proc.wait()
            finally:
                if proc.poll() is None:     # nunca dejar un FFmpeg huérfano
                    try:
                        proc.kill()
                        proc.wait(5)
                    except Exception:
                        pass

            # ── 7. RESULTADO FINAL ────────────────────────────────────────────
            if self.cancel_requested:
                if os.path.exists(out_path):
                    try: os.remove(out_path)
                    except: pass
                return False, "CANCELADO"

            if proc.returncode == 0:
                self._en_ui(self.audio_progress_bar.set, 1)
                return True, " ✅ COMPLETADO "
            else:
                return False, "ERROR FFMPEG"

        except Exception as e:
            if out_path and os.path.exists(out_path):
                try: os.remove(out_path)
                except: pass
            return False, str(e)


    def _update_audio_quality_hint(self):
        """
        Actualiza la etiqueta de hint debajo del selector de calidad.

        Comportamiento:
          · Formato lossless (WAV, AIFF, ALAC) + modo original
              → Nota sutil: el formato siempre usa calidad máxima.
          · Formato lossless + cualquier otro modo
              → Advertencia visible: el modo será ignorado (Regla 1).
          · Cualquier formato con pérdida
              → Etiqueta vacía (no molesta al usuario).
        """
        # Formatos que caen bajo la Regla 1 (siempre Modo Original)
        LOSSLESS_FORMATS = {"wav", "aiff", "alac"}

        fmt     = self.audio_format_var.get()   # ej. "wav", "m4a (alac)", "mp3"
        quality = self.audio_quality_var.get()

        # Normalizar: "m4a (alac)" → "alac"
        fmt_key = "alac" if "alac" in fmt else fmt

        if fmt_key not in LOSSLESS_FORMATS:
            # Formato con pérdida: limpiar el hint, no hay nada que advertir
            self.audio_quality_hint.configure(text="", text_color="gray")
            return

        is_original_mode = "Original" in quality

        if is_original_mode:
            # Lossless + modo original → nota informativa tranquila
            self.audio_quality_hint.configure(
                text="ℹ️  Formato sin pérdida · siempre se aplica la máxima calidad disponible",
                text_color="#5dade2"   # Azul suave, informativo
            )
        else:
            # Lossless + modo diferente al original → advertencia clara
            self.audio_quality_hint.configure(
                text="⚠️  Este formato no admite compresión con pérdida · el modo de calidad será ignorado",
                text_color="#e6b800"   # Amarillo advertencia, igual que el resto de la app
            )
        
    # ==========================================================================
    #   SECCIÓN 10: MÓDULO OCR (PaddleOCR GPU/CPU + RapidOCR CPU)
    # ==========================================================================
    def init_ocr_module(self):
        # Imports locales. torch NO se importa aquí: la GPU se evalúa con el torch
        # global cuando Tier-2 termina (_poll_gpu_ocr), igual que en el conversor de video.
        global cv2
        import cv2

        self.ocr_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.frames["OCRTool"] = self.ocr_frame

        c_main = "#e67e22"
        c_hover = "#d35400"
        c_drop = "#3a230d"          # naranja muy oscuro (como el morado de Transcripción)
        c_drop_hover = "#4a2e12"

        # Estado de la selección de motor (clave de OCR_NOMBRES)
        self._ocr_motor_elegido = "rapid_cpu"
        self._ocr_usuario_toco = False
        self._ocr_estado_motor = {}          # clave -> "cargando" | "listo" | "error" | "descargando" | "copiando"
        self._ocr_gpu_linea = ("Detectando GPU…", "#8a8a8a")
        self._ocr_gpu_motivo = "GPU no compatible"
        self._ocr_fase_actual = "inactivo"
        self._ocr_fase_detalle = ""
        self._ocr_reloj_activo = False
        self._ocr_reloj_gen = 0
        self._ocr_t0 = time.time()
        self._ocr_lote_total = 1
        self._ocr_lote_idx = 0

        # --- HEADER (Fuera del recuadro) ---
        top = ctk.CTkFrame(self.ocr_frame, fg_color="transparent")
        top.pack(fill="x", padx=20, pady=10)
        ctk.CTkButton(top, text="← Menú", width=80, fg_color="transparent", border_width=1,
                      command=lambda: self.show_frame("Menu")).pack(side="left")

        title_bg = ctk.CTkFrame(self.ocr_frame, fg_color="#2b2b2b", corner_radius=8)
        title_bg.pack(pady=5)
        ctk.CTkLabel(title_bg, text="Extractor de Texto (OCR + IA)", font=(self.main_font, 22, "bold"),
                     text_color=c_main, bg_color="#2b2b2b").pack(padx=15, pady=8)

        # --- RECUADRO GRIS GRANDE (Tabview) ---
        self.ocr_tabs = ctk.CTkTabview(self.ocr_frame, width=900, height=550, fg_color="#222",
                                       segmented_button_selected_color=c_main,
                                       segmented_button_selected_hover_color=c_hover)
        self.ocr_tabs.pack(pady=10, padx=40, fill="y", expand=True)

        tab = self.ocr_tabs.add(" OCR ")
        # El contenido NUNCA agranda el recuadro (todo es de alto fijo y cabe de sobra).
        tab.pack_propagate(False)

        # --- ARCHIVOS: misma zona de arrastre que Transcripción ---
        self.ocr_list_lbl = ctk.CTkLabel(tab, text="Ningún archivo seleccionado", text_color="gray")
        self.ocr_list_lbl.pack(pady=(5, 0))

        self.ocr_drop_btn = ctk.CTkButton(tab, text=OCR_TEXTO_DROP_VACIO, width=600, height=80,
                                          fg_color=c_drop, hover_color=c_drop_hover,
                                          border_color=c_main, border_width=2,
                                          command=lambda: self.select_files(self._ocr_filtro_dialogo(),
                                                                            self.ocr_list_lbl, self.ocr_drop_btn))
        self.ocr_drop_btn.pack(pady=10)
        self.ocr_drop_btn.drop_target_register(DND_FILES)
        self.ocr_drop_btn.dnd_bind('<<Drop>>', lambda e: self.handle_drop(e, self.ocr_list_lbl, self.ocr_drop_btn))
        self.ocr_drop = self.ocr_drop_btn

        # --- OPCIONES: motor, formato y destino (mismo ancho que la zona de arrastre) ---
        opts = ctk.CTkFrame(tab, fg_color="#2b2b2b")
        opts.pack(pady=10)

        # Motor: 3 tarjetas de tamaño fijo (un clic solo cambia colores). 3x186 + 2x9 + 2x12 = 600
        motores = ctk.CTkFrame(opts, fg_color="transparent")
        motores.pack(padx=12, pady=(12, 8))
        self.ocr_tarjetas = {}
        for i, (clave, titulo, descripcion) in enumerate(OCR_TARJETAS):
            tarjeta = TarjetaOpcion(motores, clave, titulo, descripcion,
                                    command=self._ocr_elegir_motor, color_sel=c_main,
                                    fondo_sel=c_drop, ancho=186, alto=62, fuente=self.main_font)
            tarjeta.pack(side="left", padx=(0 if i == 0 else 9, 0))
            self.ocr_tarjetas[clave] = tarjeta

        # Formato (fijo: el OCR siempre genera .txt)
        fila_fmt = ctk.CTkFrame(opts, fg_color="transparent")
        fila_fmt.pack(pady=(0, 6))
        ctk.CTkLabel(fila_fmt, text="Formato:").pack(side="left", padx=5)
        badge = ctk.CTkFrame(fila_fmt, fg_color="#444", corner_radius=6, border_width=1, border_color="#666")
        badge.pack(side="left", padx=10)
        ctk.CTkLabel(badge, text="📄 .txt (Texto Plano)", font=("Arial", 12, "bold"),
                     text_color="#eee", height=22).pack(padx=10, pady=2)

        # Destino
        self.ocr_dest_var = ctk.StringVar(value="📄 Misma Carpeta")
        self.ocr_dest_seg = ctk.CTkSegmentedButton(
            opts, values=["📄 Misma Carpeta", "📁 Carpeta 'OCR_OUTPUT'", "↗️ Elegir Otra..."],
            variable=self.ocr_dest_var, selected_color=c_main, selected_hover_color=c_hover,
            command=self._ocr_on_destino)
        self.ocr_dest_seg.pack(padx=20)
        self._destinos[self.ocr_dest_seg] = {
            "carpeta": "OCR_OUTPUT",
            "archivos": lambda: self.file_queue if self.mode == "ocr" else []}
        self.ocr_path_lbl = ctk.CTkLabel(opts, text="", text_color="gray", font=("Arial", 10), height=16)
        self.ocr_path_lbl.pack(pady=(2, 8))

        # --- PROGRESO (como Transcripción): contador + cronómetro, barra y estado en color ---
        self.ocr_prog_frame = ctk.CTkFrame(tab, fg_color="transparent")
        self.ocr_prog_frame.pack(pady=10)

        info_row = ctk.CTkFrame(self.ocr_prog_frame, fg_color="transparent")
        info_row.pack(fill="x")
        self.ocr_counter = ctk.CTkLabel(info_row, text="", font=(self.main_font, 16, "bold"))
        self.ocr_counter.pack(side="left")
        self.ocr_timer_lbl = ctk.CTkLabel(info_row, text=OCR_RELOJ_VACIO, font=(self.main_font, 14),
                                          text_color=OCR_COLOR_RELOJ)
        self.ocr_timer_lbl.pack(side="right")

        self.ocr_progress = ctk.CTkProgressBar(self.ocr_prog_frame, width=500, height=15, progress_color=c_main)
        self.ocr_progress.set(0)
        self.ocr_progress.pack(pady=10)
        self.ocr_status = ctk.CTkLabel(self.ocr_prog_frame, text="Listo", text_color="gray")
        self.ocr_status.pack()

        # --- ACCIONES ---
        actions = ctk.CTkFrame(tab, fg_color="transparent")
        actions.pack(pady=10)

        self.ocr_btn = ctk.CTkButton(actions, text="EXTRAER TEXTO", height=45, width=200,
                                     fg_color=c_main, hover_color=c_hover, text_color="black",
                                     font=(self.main_font, 14, "bold"),
                                     command=lambda: self.start_batch_thread("ocr"))
        self.ocr_btn.pack(side="left", padx=10)

        self.ocr_cancel = ctk.CTkButton(actions, text="SALTAR", height=45, width=150,
                                        fg_color="#c92c2c", hover_color="#992222", state="disabled",
                                        command=lambda: self.cancel_current_process("ocr"))
        self.ocr_cancel.pack(side="left", padx=10)

        ctk.CTkButton(actions, text="📂 Abrir Carpeta", height=45, width=150,
                      fg_color="#2b2b2b", hover_color="#3a3a3a", border_width=1, border_color="#555",
                      command=lambda: self._abrir_destino(self.ocr_dest_seg)).pack(side="left", padx=10)

        self._ocr_pintar_fase()
        self._ocr_refrescar_tarjetas()

        # GPU: evaluar cuando Tier-2 (torch real) esté listo
        self.after(500, self._poll_gpu_ocr)

    # ------------------------------------------------------------------
    #   OCR: GPU, selección de motor (tarjetas) y estado de la UI
    # ------------------------------------------------------------------
    def _ocr_evaluar_gpu(self):
        """analyze_gpu_hardware + capacidad de cómputo (PaddlePaddle cu129 exige Turing 7.5+)."""
        activa, texto, color = self.analyze_gpu_hardware(is_video=False)
        if not activa:
            return activa, texto, color
        try:
            cc = tuple(torch.cuda.get_device_capability(0))
            if cc < OCR_CC_MINIMA:
                nombre = torch.cuda.get_device_name(0).upper()
                return False, f"{nombre} (CC {cc[0]}.{cc[1]}: sin soporte PaddleOCR GPU)", "#c92c2c"
        except Exception as e:
            print(f"[OCR] No se pudo leer la capacidad de cómputo: {e}")
        return activa, texto, color

    @staticmethod
    def _ocr_nombre_gpu_corto():
        try:
            nombre = str(torch.cuda.get_device_name(0))
        except Exception:
            return "GPU NVIDIA"
        nombre = re.sub(r"(?i)^nvidia\s+", "", nombre.strip())
        nombre = re.sub(r"(?i)^geforce\s+", "", nombre)
        return nombre[:24] or "GPU NVIDIA"

    def _poll_gpu_ocr(self):
        """
        Espera a Tier-2 y fija el estado inicial (una sola vez):
          · GPU recomendada (verde/amarilla) -> tarjeta PaddleOCR GPU elegida
          · GPU "manual" (aguanta, sin garantía) -> disponible, pero se elige RapidOCR
          · sin GPU compatible -> tarjeta GPU deshabilitada + RapidOCR
        """
        if not _tier2_listo.is_set():
            self.after(500, self._poll_gpu_ocr)
            return
        try:
            activa, texto, color = self._ocr_evaluar_gpu()
            self._ocr_gpu_apta = bool(activa)
            recomendada = bool(activa) and color in ("#2cc985", "#f1c40f")
            if activa:
                nombre = self._ocr_nombre_gpu_corto()
                if recomendada:
                    self._ocr_gpu_linea = (f"{nombre} ✓", "#2cc985")
                else:
                    self._ocr_gpu_linea = (f"{nombre} · sin garantía", "#f1c40f")
            else:
                cc = re.search(r"CC \d+\.\d+", texto or "")
                if cc:
                    self._ocr_gpu_motivo = f"GPU sin soporte ({cc.group(0)})"
                elif "NO DETECTADA" in (texto or "").upper():
                    self._ocr_gpu_motivo = "Sin GPU NVIDIA compatible"
                elif "ANTIGUA" in (texto or "").upper():
                    self._ocr_gpu_motivo = "GPU antigua (no soportada)"
                else:
                    self._ocr_gpu_motivo = "GPU no compatible"
            if not self._ocr_usuario_toco:
                self._ocr_motor_elegido = "paddle_gpu" if recomendada else "rapid_cpu"
        except Exception as e:
            print(f"[poll_gpu_ocr] error: {e}")
        self._ocr_gpu_evaluada = True
        self._ocr_refrescar_tarjetas()

    def _ocr_motor_disponible(self, clave):
        if clave == "paddle_gpu":
            return bool(self._ocr_gpu_evaluada and self._ocr_gpu_apta)
        return True

    def _ocr_modo_objetivo(self):
        elegido = getattr(self, "_ocr_motor_elegido", "rapid_cpu")
        if elegido == "paddle_gpu":
            if not self._ocr_motor_disponible("paddle_gpu"):
                return "paddle_cpu"
            if self.ocr_motor.gpu_fallida:
                # Paddle GPU ya falló en este lote: se sigue con el motor de respaldo
                return "rapid_cpu"
            return "paddle_gpu"
        return elegido if elegido in OCR_NOMBRES else "rapid_cpu"

    def _ocr_estado_tarjeta(self, clave):
        """(texto, color) de la línea de estado de cada tarjeta."""
        est = self._ocr_estado_motor.get(clave)
        if est == "cargando":
            return "Cargando…", "#f1c40f"
        if est == "descargando":
            return "Descargando modelos…", "#5dade2"
        if est == "copiando":
            return "Copiando modelos…", "#5dade2"
        if est == "listo":
            return "En memoria ✓", "#2cc985"
        if clave == "paddle_gpu":
            if not self._ocr_gpu_evaluada:
                return "Detectando GPU…", "#8a8a8a"
            if not self._ocr_gpu_apta:
                return self._ocr_gpu_motivo, "#b35c5c"
            if self.ocr_motor.gpu_fallida:
                return "Falló · clic para reintentar", "#e67e22"
            if est == "error":
                return "Error al cargar", "#e74c3c"
            return self._ocr_gpu_linea
        if est == "error":
            return "Error al cargar", "#e74c3c"
        return "", "#8a8a8a"

    def _ocr_refrescar_tarjetas(self):
        """Recolorea las tarjetas. Nunca cambia tamaños: no hay saltos ni parpadeos."""
        tarjetas = getattr(self, "ocr_tarjetas", None)
        if not tarjetas:
            return
        try:
            elegido = self._ocr_motor_elegido
            bloqueado = bool(self._ocr_bloqueado)
            for clave, tarjeta in tarjetas.items():
                tarjeta.set_config(seleccionada=(clave == elegido),
                                   habilitada=self._ocr_motor_disponible(clave),
                                   atenuada=bloqueado and clave != elegido)
                tarjeta.set_estado(*self._ocr_estado_tarjeta(clave))
        except Exception as e:
            print(f"[OCR] refrescar tarjetas: {e}")

    def _ocr_elegir_motor(self, clave):
        """Clic en una tarjeta (hilo de la interfaz)."""
        if self._ocr_bloqueado or not self._ocr_motor_disponible(clave):
            return
        reintento = False
        if clave == "paddle_gpu" and self.ocr_motor.gpu_fallida:
            self.ocr_motor.gpu_fallida = False      # elegirla de nuevo = reintentar
            reintento = True
        if clave == self._ocr_motor_elegido and not reintento:
            return
        self._ocr_usuario_toco = True
        self._ocr_motor_elegido = clave
        self._ocr_refrescar_tarjetas()

    def _ocr_bloquear_controles(self, bloquear):
        """Se llama desde el hilo de lote: todo pasa por self.after."""
        def _aplicar():
            self._ocr_bloqueado = bool(bloquear)
            self._ocr_refrescar_tarjetas()
        self.after(0, _aplicar)

    def _ocr_set_motor_lbl(self, texto, color, evento=None, modo=None):
        """Aviso del GestorMotorOCR (ya en el hilo de la interfaz)."""
        est = self.__dict__.setdefault("_ocr_estado_motor", {})
        if evento == "cargando" and modo:
            est[modo] = "cargando"
        elif evento == "listo" and modo:
            for k in [k for k, v in est.items() if v == "listo"]:
                est.pop(k, None)
            est[modo] = "listo"
        elif evento == "error" and modo:
            est[modo] = "error"
        elif evento == "descargado":
            for k in [k for k, v in est.items() if v in ("listo", "cargando", "descargando", "copiando")]:
                est.pop(k, None)
        elif evento == "aviso" and modo:
            bajo = (texto or "").lower()
            if "descargando" in bajo:
                est[modo] = "descargando"
            elif "copiando" in bajo:
                est[modo] = "copiando"
        self._ocr_refrescar_tarjetas()

        # Durante el lote, el chip de fase refleja la carga del motor
        if getattr(self, "_ocr_reloj_activo", False) and self._ocr_fase_actual == "cargando":
            detalle = None
            if evento == "aviso":
                bajo = (texto or "").lower()
                if "descargando" in bajo:
                    detalle = "Descargando modelos (1ª vez)…"
                elif "copiando" in bajo:
                    detalle = "Copiando modelos…"
            if detalle:
                self._ocr_fase_detalle = detalle
                self._ocr_pintar_fase()

    # ------------------------------------------------------------------
    #   OCR: fases, cronómetro y progreso REAL (sin estimaciones)
    # ------------------------------------------------------------------
    def _ocr_texto_fase(self, fase, detalle):
        if fase == "inactivo":
            return "Listo"
        if fase == "esperando":
            return f"Esperando a que termine {detalle}…" if detalle else "Esperando turno…"
        if fase == "preparando":
            return "Preparando archivo…"
        if fase == "cargando":
            if detalle and detalle.endswith("…"):
                return detalle
            return f"Cargando {detalle}…" if detalle else "Cargando motor…"
        if fase == "escaneando":
            return f"Escaneando · {detalle}" if detalle else "Escaneando…"
        if fase == "nativo":
            return f"Leyendo texto del PDF · {detalle}" if detalle else "Leyendo texto del PDF…"
        if fase == "guardando":
            return "Guardando texto…"
        if fase == "saltando":
            return "Saltando al terminar esta página…" if detalle == "pagina" else "Saltando…"
        if fase == "saltado":
            return "Saltado"
        if fase == "error":
            return "Error"
        if fase == "con_errores":
            return "Terminado con errores"
        if fase == "listo":
            return "COMPLETADO"
        return str(fase)

    def _ocr_pintar_fase(self):
        """Hilo de la interfaz. Texto de estado bajo la barra; solo reconfigura si cambió."""
        if not hasattr(self, "ocr_status"):
            return
        fase = self._ocr_fase_actual
        detalle = self._ocr_fase_detalle
        clave = fase
        if fase == "cargando" and detalle:
            bajo = detalle.lower()
            if bajo.startswith("descargando"):
                clave = "descargando"
            elif bajo.startswith("copiando"):
                clave = "copiando"
        icono, color = OCR_FASES.get(clave, OCR_FASES["inactivo"])
        texto = self._ocr_texto_fase(fase, detalle)
        if len(texto) > 60:
            texto = texto[:59] + "…"
        if icono:
            texto = f"{icono} {texto}"
        visual = (texto, color)
        if visual == getattr(self, "_ocr_estado_visual", None):
            return
        self._ocr_estado_visual = visual
        try:
            self.ocr_status.configure(text=texto, text_color=color)
        except Exception:
            pass

    def _ocr_fase(self, fase, detalle=""):
        """Cambia la fase del chip (desde cualquier hilo)."""
        def _aplicar():
            self._ocr_fase_actual = fase
            self._ocr_fase_detalle = detalle
            self._ocr_pintar_fase()
        self.after(0, _aplicar)

    @staticmethod
    def _ocr_fmt_reloj(segundos, total=False):
        segundos = max(0, int(segundos))
        h, resto = divmod(segundos, 3600)
        m, s = divmod(resto, 60)
        return f"⏱️ {'Total: ' if total else ''}{h:02}:{m:02}:{s:02}"

    def _ocr_reloj_tick(self, gen):
        # 'gen' evita que queden dos bucles vivos si un lote arranca justo al terminar otro
        if not self._ocr_reloj_activo or gen != self._ocr_reloj_gen:
            return
        texto = self._ocr_fmt_reloj(time.time() - self._ocr_t0)
        if texto != getattr(self, "_ocr_reloj_txt", None):
            self._ocr_reloj_txt = texto
            try:
                self.ocr_timer_lbl.configure(text=texto)
            except Exception:
                pass
        self.after(500, lambda: self._ocr_reloj_tick(gen))

    def _ocr_set_reloj(self, texto, color):
        self._ocr_reloj_txt = texto
        try:
            self.ocr_timer_lbl.configure(text=texto, text_color=color)
        except Exception:
            pass

    def _ocr_lote_iniciar(self, total):
        """Hilo de lote: arranca el cronómetro total (incluye la carga del modelo)."""
        self._ocr_lote_total = max(1, int(total))
        self._ocr_lote_idx = 0

        def _ui():
            self._ocr_t0 = time.time()
            self._ocr_fase_actual = "preparando"
            self._ocr_fase_detalle = ""
            try:
                self.ocr_progress.set(0)
                self.ocr_counter.configure(text="")
            except Exception:
                pass
            self._ocr_set_reloj(self._ocr_fmt_reloj(0), OCR_COLOR_RELOJ)
            self._ocr_pintar_fase()
            self._ocr_reloj_activo = True
            self._ocr_reloj_gen += 1
            self._ocr_reloj_tick(self._ocr_reloj_gen)
        self.after(0, _ui)

    def _ocr_lote_terminar(self, errores=0):
        def _ui():
            self._ocr_reloj_activo = False
            self._ocr_fase_actual = "con_errores" if errores else "listo"
            self._ocr_fase_detalle = ""
            self._ocr_pintar_fase()
            self._ocr_set_reloj(self._ocr_fmt_reloj(time.time() - self._ocr_t0, total=True),
                                OCR_COLOR_RELOJ_FIN)
            try:
                self.ocr_progress.set(1)
            except Exception:
                pass
        self.after(0, _ui)

    def _ocr_reiniciar_estado(self):
        """Vuelve al estado inicial (sin lote en curso)."""
        if self.lote_de("ocr"):
            return
        if not hasattr(self, "ocr_status"):
            return
        self._ocr_reloj_activo = False
        self._ocr_fase_actual = "inactivo"
        self._ocr_fase_detalle = ""
        self._ocr_pintar_fase()
        self._ocr_set_reloj(OCR_RELOJ_VACIO, OCR_COLOR_RELOJ)
        try:
            self.ocr_progress.set(0)
            self.ocr_counter.configure(text="")
        except Exception:
            pass

    def _ocr_progreso_real(self, hechas, total):
        """Barra = (archivos terminados + páginas hechas del actual) / archivos del lote."""
        total = max(1, int(total))
        frac = (self._ocr_lote_idx + min(max(hechas, 0), total) / total) / max(1, self._ocr_lote_total)
        frac = max(0.0, min(1.0, frac))
        self.after(0, lambda f=frac: self.ocr_progress.set(f))

    def _ocr_al_entrar(self):
        # Ya no se precarga nada: el motor se carga al pulsar EXTRAER TEXTO
        self._ocr_refrescar_tarjetas()
        self._ocr_reiniciar_estado()

    def _ocr_filtro_dialogo(self):
        ext = sorted(VALID_IMAGE_EXT | VALID_PDF_EXT)
        return [("PDF / Imágenes", " ".join("*" + e for e in ext))]

    def _ocr_on_destino(self, valor):
        self.on_dest_change(valor, self.ocr_path_lbl, self.ocr_dest_seg)
        try:
            texto = self.ocr_path_lbl.cget("text")
            if len(texto) > 96:
                self.ocr_path_lbl.configure(text=texto[:46] + " … " + texto[-46:])
        except Exception:
            pass

    def _ocr_fallback_gpu(self, exc):
        """PaddleOCR GPU falló: se pasa a RapidOCR CPU sin cerrar la app."""
        gestor = self.ocr_motor
        if gestor.gpu_fallida:
            return
        gestor.gpu_fallida = True
        print(f"[OCR] PaddleOCR GPU falló, se usará RapidOCR CPU: {exc}")

        def _ui():
            try:
                self._ocr_motor_elegido = "rapid_cpu"
                self._ocr_refrescar_tarjetas()
            except Exception:
                pass
            messagebox.showwarning(
                "OCR: GPU no disponible",
                "PaddleOCR en GPU falló y se cambió a RapidOCR (CPU).\n\n"
                f"Detalle: {str(exc)[:300]}\n\n"
                "Puedes volver a elegir 'PaddleOCR · GPU' para reintentar.")
        self.after(0, _ui)

    def _ocr_asegurar_motor(self, modo, on_espera=None):
        """Deja listo el motor para el lote (en el hilo de lote). Aplica el fallback de GPU."""
        try:
            self.ocr_motor.asegurar(modo, on_espera=on_espera)
            return modo
        except Exception as e:
            print(f"[OCR] Error cargando {OCR_NOMBRES[modo]}: {e}")
            if modo == "paddle_gpu":
                self._ocr_fallback_gpu(e)
                try:
                    self._ocr_fase("cargando", OCR_NOMBRES["rapid_cpu"])
                    self.ocr_motor.asegurar("rapid_cpu", on_espera=on_espera)
                    return "rapid_cpu"
                except Exception as e2:
                    e = e2
            msg = str(e)
            self.after(0, lambda: messagebox.showerror(
                "Motor OCR", f"No se pudo cargar {OCR_NOMBRES[modo]}:\n\n{msg[:400]}"))
            return None

    def _ocr_reconocer(self, img_bgr, on_espera=None):
        """Reconoce una página. Si Paddle GPU falla (p. ej. sin VRAM), repite con RapidOCR."""
        try:
            return self.ocr_motor.predecir(img_bgr, on_espera=on_espera)
        except Exception as e:
            if self.ocr_motor.modo not in (None, "paddle_gpu") or self._ocr_modo_objetivo() != "paddle_gpu":
                raise
            self._ocr_fallback_gpu(e)
            self._ocr_fase("cargando", OCR_NOMBRES["rapid_cpu"])
            self.ocr_motor.asegurar("rapid_cpu")
            self._ocr_fase("escaneando")
            return self.ocr_motor.predecir(img_bgr, on_espera=on_espera)

    # ==========================================================
    #   PDF CON TEXTO SELECCIONABLE (extracción directa)
    # ==========================================================
    def _ocr_pdf_tiene_texto(self, pdf_path):
        """check_pdf_has_text con caché por archivo (ruta + tamaño + fecha)."""
        try:
            st = os.stat(pdf_path)
            clave = (os.path.normcase(os.path.abspath(pdf_path)), st.st_size, st.st_mtime)
        except OSError:
            return False
        cache = self.__dict__.setdefault("_ocr_cache_pdf_texto", {})
        if clave not in cache:
            cache[clave] = self.check_pdf_has_text(pdf_path)
        return cache[clave]

    def _ocr_analizar_cola(self):
        """Cuenta en segundo plano cuántos PDF ya traen texto y lo muestra en la lista."""
        cola = list(self.file_queue)
        pdfs = [f for f in cola if os.path.splitext(f)[1].lower() in VALID_PDF_EXT]
        if not pdfs:
            return
        self._ocr_cola_id = getattr(self, "_ocr_cola_id", 0) + 1
        mi_id = self._ocr_cola_id

        def _trabajo():
            digitales = sum(1 for f in pdfs if self._ocr_pdf_tiene_texto(f))

            def _ui():
                if mi_id != self._ocr_cola_id or self.mode != "ocr" or list(self.file_queue) != cola:
                    return
                try:
                    n = len(cola)
                    base = f"{n} archivo{'s' if n != 1 else ''} listo{'s' if n != 1 else ''}"
                    if digitales:
                        base += f"  ·  {digitales} PDF con texto → extracción directa"
                    # Conserva el aviso de archivos rechazados que puso handle_drop
                    previo = re.search(r"\(\d+ inválidos\)", self.ocr_list_lbl.cget("text"))
                    if previo:
                        base += f"  {previo.group(0)}"
                    self.ocr_list_lbl.configure(text=base, text_color="#2cc985")
                except Exception:
                    pass
            self.after(0, _ui)

        threading.Thread(target=_trabajo, daemon=True).start()

    def check_pdf_has_text(self, pdf_path):
        """Revisa si el PDF ya tiene texto seleccionable (evita OCR innecesario)."""
        try:
            doc = fitz.open(pdf_path)
            # Revisamos máximo 5 páginas para estar seguros
            pages_to_check = min(5, len(doc))
            total_text_len = 0
            
            for i in range(pages_to_check):
                # Extraer texto crudo
                text = doc[i].get_text()
                # Eliminar espacios en blanco para contar caracteres reales
                total_text_len += len(text.strip())
            
            doc.close()
            
            # Si hay más de 100 caracteres sólidos, asumimos que ya es un PDF digital
            return total_text_len > 100
        except Exception as e:
            print(f"Error revisando texto PDF: {e}")
            return False

    @staticmethod
    def _ocr_rasterizar_pagina(page):
        """Página de PDF -> imagen BGR (convención OpenCV) a OCR_DPI_PDF para el motor."""
        escala = OCR_DPI_PDF / 72.0
        pix = page.get_pixmap(matrix=fitz.Matrix(escala, escala))
        img_np = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, pix.n)
        if pix.n >= 4:
            return cv2.cvtColor(img_np, cv2.COLOR_RGBA2BGR)
        if pix.n == 3:
            return cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)
        return cv2.cvtColor(img_np, cv2.COLOR_GRAY2BGR)

    def convert_ocr_logic(self, source_path):
        out_path = None
        doc_in = None

        # Validación inicial: el archivo pudo moverse o borrarse antes de empezar
        if not os.path.exists(source_path):
            return False, "❌ Archivo movido o no existe"

        try:
            # 1. Carpeta de destino
            folder = os.path.dirname(source_path)
            if "OCR_OUTPUT" in self.ocr_dest_var.get():
                folder = os.path.join(folder, "OCR_OUTPUT")
                os.makedirs(folder, exist_ok=True)
            elif self.ocr_dest_var.get().startswith("↗️") and self._ruta_destino(self.ocr_dest_seg):
                folder = self._ruta_destino(self.ocr_dest_seg)
            self._registrar_salida(self.ocr_dest_seg, folder)

            base_name = os.path.splitext(os.path.basename(source_path))[0]
            ext_file = os.path.splitext(source_path)[1].lower()
            text_lines_buffer = []
            self._ocr_fase("preparando")
            self._ocr_progreso_real(0, 1)

            # El motor de IA se carga SOLO si alguna página lo necesita (la primera vez)
            motores_usados = []
            motor = {"modo": None}

            def _asegurar_motor():
                if motor["modo"] is None:
                    pedido = self._ocr_modo_objetivo()
                    if not self.ocr_motor.esta_listo(pedido):
                        self._ocr_fase("cargando", OCR_NOMBRES[pedido])
                    modo = self._ocr_asegurar_motor(pedido)
                    if modo is None:
                        raise _OcrSinMotor()
                    motor["modo"] = modo
                return motor["modo"]

            def _leer_con_ia(img_np):
                modo = _asegurar_motor()
                # El motor no informa avance dentro de la página: no se inventa
                # ningún porcentaje, solo corre el cronómetro.
                result = self._ocr_reconocer(img_np)
                usado = OCR_NOMBRES.get(self.ocr_motor.modo or modo, "OCR")
                if usado not in motores_usados:
                    motores_usados.append(usado)
                return result

            paginas_nativas = paginas_ia = 0
            if ext_file in VALID_PDF_EXT:
                # PDF: CADA página se decide por separado. Si trae texto real se
                # extrae directo (PyMuPDF, exacto); si es escaneada se lee con IA.
                # Así un PDF mixto ya no pierde las páginas escaneadas.
                doc_in = fitz.open(source_path)
                total = max(1, len(doc_in))
                for idx in range(len(doc_in)):
                    # SALTAR: la página en curso SIEMPRE se termina (cortar el motor
                    # a media página lo dejaría inestable); se corta antes de empezar
                    # la siguiente y se pasa al archivo siguiente de la cola.
                    if self.cancel_requested:
                        raise InterruptedError(f"se detuvo en la {_plural_pag(idx + 1)} de {total}")
                    detalle = f"pág {idx+1}/{total}" if total > 1 else ""
                    page = doc_in[idx]
                    texto = page.get_text()
                    if len(texto.strip()) >= OCR_MIN_CHARS_PAGINA:
                        self._ocr_fase("nativo", detalle)
                        text_lines_buffer += [f"--- Página {idx+1} ---", texto, ""]
                        paginas_nativas += 1
                    else:
                        _asegurar_motor()
                        self._ocr_fase("escaneando", detalle)
                        img_np = self._ocr_rasterizar_pagina(page)
                        result = _leer_con_ia(img_np)
                        text_lines_buffer += [f"--- Página {idx+1} ---", "\n".join(result), "\n"]
                        paginas_ia += 1
                        img_np = None
                        gc.collect()
                    self._ocr_progreso_real(idx + 1, total)
                doc_in.close()
                doc_in = None
            else:
                # Imagen: cualquier formato admitido (SVG/HEIC vía FFmpeg); la
                # transparencia se compone sobre blanco para no perder texto oscuro
                _asegurar_motor()
                self._ocr_fase("escaneando")
                pil_img = _img_sobre_blanco(img_open_any(source_path, svg_lado=2048))
                img_np = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
                pil_img = None
                result = _leer_con_ia(img_np)
                text_lines_buffer += ["--- Página 1 ---", "\n".join(result), "\n"]
                paginas_ia = 1
                img_np = None
                self._ocr_progreso_real(1, 1)

            ia = " + ".join(motores_usados)
            if paginas_ia and paginas_nativas:
                engine_short_name = f"Nativo + {ia}"
                engine_full_name = (f"Mixto: extracción directa (PyMuPDF) en {_plural_pag(paginas_nativas)} + "
                                    f"Inteligencia Artificial ({ia}, modelos PP-OCRv6) en "
                                    f"{_plural_pag(paginas_ia)} escaneada{'s' if paginas_ia != 1 else ''}")
                filename_suffix = "_OCR_IA.txt"
            elif paginas_ia:
                engine_short_name = ia
                engine_full_name = f"Inteligencia Artificial ({ia}, modelos PP-OCRv6)"
                filename_suffix = "_OCR_IA.txt"
            else:
                engine_short_name = "Nativo PyMuPDF"
                engine_full_name = "Extracción Directa (Librería: PyMuPDF/Fitz)"
                filename_suffix = "_OCR_Nativo.txt"

            # ------------------------------------------------------------------
            # GUARDADO FINAL (nunca sobre un .txt que ya exista)
            # ------------------------------------------------------------------
            if text_lines_buffer:
                self._ocr_fase("guardando")
                out_path = _ruta_unica(os.path.join(folder, f"{base_name}{filename_suffix}"))
                text_lines_buffer.append("="*40)
                text_lines_buffer.append(f"Generado por DEUS MACHINA | TOOLS")
                text_lines_buffer.append(f"Motor: {engine_full_name}")
                text_lines_buffer.append(f"Fecha: {time.strftime('%Y-%m-%d %H:%M:%S')}")
                text_lines_buffer.append("="*40)
                with open(out_path, "w", encoding="utf-8") as f:
                    f.write("\n".join(text_lines_buffer))
                self._ocr_progreso_real(1, 1)
                return True, f" ✅ TXT (Motor: {engine_short_name})"
            else:
                return False, "No se detectó texto válido"

        except _OcrSinMotor:
            self._ocr_fase("error")
            return False, "Error Carga Motor OCR"

        except InterruptedError as e:
            return False, (f"CANCELADO: {e}" if str(e) else "CANCELADO")

        # Atrapa errores Python normales (open, os.path)
        except FileNotFoundError:
            return False, "❌ Archivo movido o no existe"

        except Exception as e:
            if out_path and os.path.exists(out_path):
                try: os.remove(out_path)
                except: pass
            print(f"ERROR OCR: {e}")
            if "no such file" in str(e).lower():
                return False, "❌ Archivo movido o no existe"
            return False, f"Error: {str(e)[:60]}"

        finally:
            if doc_in is not None:
                try: doc_in.close()
                except Exception: pass
            gc.collect()
        
        
        
        
        
        
    # ==========================================================================
    #   SECCIÓN 11: MÓDULO TRANSCRIBIR (WHISPER) - ACTUALIZADO CON LIVE
    # ==========================================================================
    # --- NUEVOS HELPERS PARA TRANSCRIPCIÓN ---
    # --- NUEVOS HELPERS MEJORADOS (AUDIO Y UI) ---
    




    def get_local_model_path(self, model_raw_name):
        """
        Construye la ruta absoluta al modelo local y verifica su existencia.
        Ruta esperada: tools/faster_whisper/models/faster-whisper-{talla}
        """
        model_size = model_raw_name.split()[0]  # "small", "medium", etc.
        
        # 1. Detectar ruta base del ejecutable o script (PyInstaller o Nuitka)
        if _is_frozen_build():
            base_path = os.path.dirname(sys.executable)
        else:
            base_path = os.path.dirname(os.path.abspath(__file__))

        # 2. Construir ruta según tu estructura indicada
        # tools \ faster_whisper \ models \ faster-whisper-{size}
        folder_name = f"faster-whisper-{model_size}"
        model_path = os.path.join(base_path, "tools", "faster_whisper", "models", folder_name)

        return model_size, model_path




    def clean_pyaudio_name(self, name):
        """Intenta arreglar errores de codificación (tildes raras) en Windows"""
        try:
            # Intento común para corregir 'MicrÃ³fono' -> 'Micrófono'
            return name.encode('latin-1').decode('utf-8')
        except:
            return name

    def get_input_devices(self):
        """
        Devuelve un DICCIONARIO: {'Nombre Limpio': Index}
        Detecta 'Microsoft Sound Mapper', 'Asignador de sonido', etc.
        """
        devices = {}
        try:
            import pyaudio
            p = pyaudio.PyAudio()
            
            # 1. Intentar obtener el nombre REAL del dispositivo por defecto de Windows
            real_default_name = "Desconocido"
            try:
                default_info = p.get_default_input_device_info()
                real_default_name = self.clean_pyaudio_name(default_info['name'])
            except:
                pass

            info = p.get_host_api_info_by_index(0)
            numdevices = info.get('deviceCount')
            
            for i in range(0, numdevices):
                device_info = p.get_device_info_by_host_api_device_index(0, i)
                if device_info.get('maxInputChannels') > 0:
                    raw_name = device_info.get('name')
                    
                    # --- LÓGICA DE RENOMBRADO ---
                    # Agregamos "Asignador de sonido" a la lista de detección
                    if any(x in raw_name for x in ["Microsoft Sound Mapper", "Mapeador de sonido", "Asignador de sonido"]):
                        clean_name = f"Predeterminado - {real_default_name}"
                    else:
                        clean_name = self.clean_pyaudio_name(raw_name)
                    # ----------------------------

                    # Manejo de duplicados
                    if clean_name in devices:
                        clean_name = f"{clean_name} ({i})"
                        
                    devices[clean_name] = i
            p.terminate()
        except Exception as e:
            print(f"Error detectando micros: {e}")
            devices = {"Default (Sistema)": None}
        
        self.mic_mapping = devices 
        return list(devices.keys())

    def get_selected_mic_index(self):
        """Busca el ID usando el nombre seleccionado en el ComboBox"""
        selected_name = self.live_mic_var.get()
        if hasattr(self, 'mic_mapping') and selected_name in self.mic_mapping:
            return self.mic_mapping[selected_name]
        return None

    def open_model_help(self, mostrar=True):
        """Ventana de ayuda COMPACTA V4 - Espaciado corregido y Texto visible"""
        if mostrar and self._ventana_reusar(self.toplevel_model_help):
            return
        if not mostrar and self.toplevel_model_help is not None:
            return

        # 1. TAMAÑO AJUSTADO (Más ancho para que quepa texto, pero altura controlada)
        # Reducimos altura para que se vea compacto, pero suficiente para el texto
        win = self._ventana_nueva("⁉️ ¿Cuál modelo elegir?", 520, 580, fg_color="#1a1a2e",
                                  redimensionable=(True, True), minimo=(520, 580),
                                  reutilizable=True)
        self.toplevel_model_help = win

        # --- CONTENEDOR PRINCIPAL (Usamos PACK para centrar todo verticalmente) ---
        main_container = ctk.CTkFrame(win, fg_color="transparent")
        main_container.pack(expand=True, fill="both", padx=20, pady=20)

        # TITULO
        title_frame = ctk.CTkFrame(main_container, fg_color="transparent")
        title_frame.pack(pady=(0, 15))
        
        ctk.CTkLabel(title_frame, text="Requisitos de Modelos IA", font=(self.main_font, 20, "bold"), text_color="white").pack()
        ctk.CTkLabel(title_frame, text="Elige según tu tarjeta gráfica (GPU NVIDIA).", font=("Arial", 11), text_color="#aaa").pack()

        # --- GRID FRAME (Aquí van las tarjetas pegaditas) ---
        # Al no usar 'weight' en las columnas de este frame, se ajustarán al tamaño del contenido (pegados)
        cards_grid = ctk.CTkFrame(main_container, fg_color="transparent")
        cards_grid.pack()

        # --- FUNCIÓN INTERNA PARA CREAR TARJETAS ---
        def create_grid_card(row, col, title, color, cpu_txt, gpu_txt, recomendation):
            
            # 2. TARJETAS COMPACTAS
            # width=420 es suficiente. Quitamos altura fija para que crezca si el texto lo pide.
            card = ctk.CTkFrame(cards_grid, fg_color="#2b2b2b", corner_radius=12, 
                                border_width=2, border_color=color, width=380)
            
            # 3. ESPACIADO MÍNIMO (PEGADOS)
            # padx=5 significa que entre tarjeta y tarjeta habrá solo 10px de hueco.
            card.grid(row=row, column=col, padx=5, pady=5, sticky="nsew") 
            
            # Encabezado (Más delgado)
            header = ctk.CTkFrame(card, fg_color=color, height=22, corner_radius=6)
            header.pack(fill="x", padx=8, pady=8)
            ctk.CTkLabel(header, text=title, font=("Arial", 13, "bold"), text_color="white").pack(pady=2)
            
            # Contenido
            content = ctk.CTkFrame(card, fg_color="transparent")
            content.pack(fill="both", expand=True, padx=12, pady=(0, 10))
            
            # FUENTES PEQUEÑAS
            # CPU
            ctk.CTkLabel(content, text="💻 PROCESADOR:", font=("Arial", 10, "bold"), text_color="#ccc").pack(anchor="w")
            ctk.CTkLabel(content, text=cpu_txt, font=("Arial", 11), text_color="white", justify="left", wraplength=350).pack(anchor="w", pady=(0, 4))
            
            # GPU
            ctk.CTkLabel(content, text="🎮 GRAFICA (GPU):", font=("Arial", 10, "bold"), text_color="#2cc985").pack(anchor="w")
            ctk.CTkLabel(content, text=gpu_txt, font=("Arial", 11), text_color="white", justify="left", wraplength=350).pack(anchor="w", pady=(0, 4))
            
            # Separador
            ctk.CTkFrame(content, height=1, fg_color="#555").pack(fill="x", pady=6)

            # 4. SOLUCIÓN TEXTO FALTANTE (El foco)
            # Aseguramos que se empaquete al final con espacio suficiente.
            # Cambiamos el color a uno más brillante para asegurar visibilidad.
            lbl_rec = ctk.CTkLabel(content, text=recomendation, font=("Arial", 11, "italic"), 
                                   text_color="#ffd700", # Dorado brillante para resaltar
                                   justify="left", wraplength=350)
            lbl_rec.pack(anchor="w", pady=(2, 0)) # Reducimos padding bottom para que no se salga

        # --- CREACIÓN DE LAS 4 TARJETAS ---

        # 1. TINY
        create_grid_card(0, 0, "🟢 TINY (Muy Rápido)", "#27ae60",
                    "Cualquier CPU moderna.",
                    "Mínimo 2GB - 4GB VRAM (GTX 1650).",
                    "💡 Úsalo si tu PC es básica.")

        # 2. SMALL
        create_grid_card(0, 1, "🟡 SMALL (Equilibrado)", "#f1c40f",
                    "Mínimo Intel i5 / Ryzen 5.",
                    "Mínimo 2GB - 4GB VRAM (GTX 1650).",
                    "💡 Recomendado para la mayoría.")

        # 3. MEDIUM
        create_grid_card(1, 0, "🟠 MEDIUM (Preciso)", "#e67e22",
                    "❌ NO recomendado en CPU.",
                    "Mínimo 6GB VRAM (RTX 2060, 3060).",
                    "💡 Solo si tienes GPU decente.")

        # 4. LARGE
        create_grid_card(1, 1, "🔴 LARGE (Pro)", "#c0392b",
                    "❌ NO recomendado en CPU.",
                    "Mínimo 8GB VRAM (RTX 3080, 4060+).",
                    "💡 Muy pesado. Solo gama alta.")

        # Botón Cerrar (Pegado abajo)
        ctk.CTkButton(main_container, text="Entendido", command=lambda: self._ventana_ocultar(win), fg_color="#444", hover_color="#555", 
                      width=120, height=30, font=("Arial", 11)).pack(pady=15)

        if mostrar:
            self._ventana_mostrar(win)
    

    


    def init_transcribe_module(self):
        self.trans_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.frames["TranscribeTool"] = self.trans_frame
        
        c_main = "#8e44ad"
        c_hover = "#6c3483"
        self.live_recording = False
        self.live_start_time = 0
        self.last_activity_check = 0
        self.live_text_buffer = ""
        
        # --- HEADER ---
        top = ctk.CTkFrame(self.trans_frame, fg_color="transparent")
        top.pack(fill="x", padx=20, pady=10)
        ctk.CTkButton(top, text="← Menú", width=80, fg_color="transparent", border_width=1, 
                      command=lambda: self.show_frame("Menu")).pack(side="left")
        
        title_bg = ctk.CTkFrame(self.trans_frame, fg_color="#2b2b2b", corner_radius=8)
        title_bg.pack(pady=5)
        ctk.CTkLabel(title_bg, text="Transcripción con IA (Faster-Whisper)", font=(self.main_font, 22, "bold"), text_color=c_main, bg_color="#2b2b2b").pack(padx=15, pady=8)

        # --- PESTAÑAS ---
        self.trans_tabs = ctk.CTkTabview(self.trans_frame, width=900, height=550, fg_color="#222",
                                         segmented_button_selected_color=c_main, segmented_button_selected_hover_color=c_hover)
        self.trans_tabs.pack(pady=10,padx=40, fill="y", expand=True)
        self.trans_tabs.add("Archivos")
        self.trans_tabs.add("YouTube → Texto")
        self.trans_tabs.add("En Vivo")

        # ==========================================
        # PESTAÑA 1: ARCHIVOS (Igual que antes)
        # ==========================================
        tab_files = self.trans_tabs.tab("Archivos")
        
        self.trans_list_label = ctk.CTkLabel(tab_files, text="Ningún archivo seleccionado", text_color="gray")
        self.trans_list_label.pack(pady=(5,0))
        
        self.trans_drop_area = ctk.CTkButton(tab_files, text="🎙️ Arrastra AUDIOS o VIDEOS aquí\n(Crea archivos .txt)", 
                                             width=600, height=80, 
                                             fg_color="#2e1a36", hover_color="#3e2a46", border_color=c_main, border_width=2,
                                             command=lambda: self.select_files([
                                                                                 ("Audio y Video", "*.mp3 *.wav *.m4a *.flac *.ogg *.opus *.wma *.aac *.aiff *.webm *.mp4 *.mkv *.mov *.avi *.flv *.ts"),
                                                                                 ("Solo Audio",    "*.mp3 *.wav *.m4a *.flac *.ogg *.opus *.wma *.aac *.aiff"),
                                                                                 ("Solo Video",    "*.mp4 *.mkv *.webm *.mov *.avi *.flv *.ts"),
                                                                                 ("Todos",         "*.*")
                                                                             ], self.trans_list_label, self.trans_drop_area))
        self.trans_drop_area.pack(pady=10)
        self.trans_drop_area.drop_target_register(DND_FILES)
        self.trans_drop_area.dnd_bind('<<Drop>>', lambda e: self.handle_drop(e, self.trans_list_label, self.trans_drop_area))
        
        # Opciones Archivos
        # Opciones Archivos
        opts = ctk.CTkFrame(tab_files, fg_color="#2b2b2b")
        opts.pack(pady=10, ipadx=30)

        # --- 1. GPU INTELIGENTE (WHISPER FILE) ---
        gpu_active, gpu_text, gpu_col = self.analyze_gpu_hardware(is_video=False)
        
        # Lógica Default (Solo ON si es segura/recomendada)
        default_on = gpu_active and (gpu_col == "#2cc985" or gpu_col == "#f1c40f")
        
        self.trans_use_gpu = ctk.BooleanVar(value=default_on)
        state_switch = "normal" if gpu_active else "disabled"

        tgpu_frame = ctk.CTkFrame(opts, fg_color="transparent")
        tgpu_frame.pack(pady=(15, 5)) 

        self.switch_trans_gpu = ctk.CTkSwitch(tgpu_frame, text="Uso de GPU (CUDA)", 
                                              variable=self.trans_use_gpu, 
                                              progress_color="#8e44ad", 
                                              state=state_switch)
        self.switch_trans_gpu.pack(side="left", padx=5)
        
        ctk.CTkLabel(tgpu_frame, text=f"Estado: {gpu_text}", 
                     font=("Arial", 10, "bold"), text_color=gpu_col).pack(side="left", padx=5)
        # ------------------------------------

        # --- 2. MODELO IA (AHORA VA DEBAJO) ---
        row1 = ctk.CTkFrame(opts, fg_color="transparent")
        row1.pack(pady=5, padx=20)

        ctk.CTkLabel(row1, text="Modelo IA:").pack(side="left", padx=5)
        self.trans_model_var = ctk.StringVar(value="small (Recomendado)")
        model_options = ["tiny (Muy Rápido)", "base (Rápido)", "small (Recomendado)", "medium (Preciso)", "large (Solo GPU Potente)"]
        ctk.CTkOptionMenu(row1, values=model_options, variable=self.trans_model_var, width=180, fg_color=c_main, button_color=c_hover).pack(side="left", padx=10)
        # Traducir: Whisper escribe el resultado en inglés, sea cual sea el idioma del audio
        self.trans_traducir_var = ctk.BooleanVar(value=False)
        ctk.CTkCheckBox(row1, text="Traducir al inglés", variable=self.trans_traducir_var,
                        fg_color=c_main, hover_color=c_hover).pack(side="left", padx=(10, 5))

        row2 = ctk.CTkFrame(opts, fg_color="transparent")
        row2.pack(pady=5, padx=20)
        ctk.CTkLabel(row2, text="Formato:").pack(side="left", padx=5)
        self.trans_fmt_var = ctk.StringVar(value=".txt (Texto Plano)")
        ctk.CTkOptionMenu(row2, values=[".txt (Texto Plano)", ".srt (Subtítulos)", ".vtt (Web Video)"], variable=self.trans_fmt_var, width=150, fg_color="#444").pack(side="left", padx=10)
        # Idioma del audio (Automático = Whisper lo detecta solo)
        ctk.CTkLabel(row2, text="Idioma:").pack(side="left", padx=(10, 5))
        self.trans_lang_var = ctk.StringVar(value=TRANS_IDIOMA_AUTO)
        self._selector_idioma(row2, self.trans_lang_var).pack(side="left", padx=5)

        dest = ctk.CTkFrame(opts, fg_color="transparent")
        dest.pack(pady=5, padx=20)
        self.trans_dest_var = ctk.StringVar(value="📄 Misma Carpeta")
        self.trans_dest_seg = ctk.CTkSegmentedButton(dest, values=["📄 Misma Carpeta", "📁 Carpeta 'TRANSCRIPCIONES'", "↗️ Elegir Otra..."],
                               variable=self.trans_dest_var, selected_color=c_main, selected_hover_color=c_hover,
                               command=lambda v: self.on_dest_change(v, self.trans_path_lbl, self.trans_dest_seg))
        self.trans_dest_seg.pack()
        self._destinos[self.trans_dest_seg] = {
            "carpeta": "TRANSCRIPCIONES",
            "archivos": lambda: self.file_queue if self.mode == "transcribe" else []}
        self.trans_path_lbl = ctk.CTkLabel(dest, text="", text_color="gray", font=("Arial", 10))
        self.trans_path_lbl.pack()
        
        # Progreso Archivos
        self.trans_prog_frame = ctk.CTkFrame(tab_files, fg_color="transparent")
        self.trans_prog_frame.pack(pady=10) 
        
        info_row = ctk.CTkFrame(self.trans_prog_frame, fg_color="transparent")
        info_row.pack(fill="x")
        self.trans_counter = ctk.CTkLabel(info_row, text="", font=(self.main_font, 16, "bold"))
        self.trans_counter.pack(side="left")
        self.trans_time_lbl = ctk.CTkLabel(info_row, text="⏱️ --:--:--", font=(self.main_font, 14), text_color="#d4ac0d")
        self.trans_time_lbl.pack(side="right")
        
        self.trans_progress = ctk.CTkProgressBar(self.trans_prog_frame, width=500, height=15, progress_color=c_main)
        self.trans_progress.set(0)
        self.trans_progress.pack(pady=10)
        self.trans_status = ctk.CTkLabel(self.trans_prog_frame, text="Listo", text_color="gray")
        self.trans_status.pack()
        
        actions = ctk.CTkFrame(tab_files, fg_color="transparent")
        actions.pack(pady=10)
        self.trans_btn = ctk.CTkButton(actions, text="INICIAR TRANSCRIPCIÓN", height=45, width=220, fg_color=c_main, hover_color=c_hover, font=(self.main_font, 14, "bold"), command=lambda: self.start_batch_thread("transcribe"))
        self.trans_btn.pack(side="left", padx=10)
        self.trans_cancel = ctk.CTkButton(actions, text="SALTAR", height=45, width=150, fg_color="#c92c2c", hover_color="#992222", state="disabled", command=lambda: self.cancel_current_process("transcribe"))
        self.trans_cancel.pack(side="left", padx=10)
        ctk.CTkButton(actions, text="📂 Abrir Carpeta", height=45, width=150,
                      fg_color="#2b2b2b", hover_color="#3a3a3a", border_width=1, border_color="#555",
                      command=self._abrir_carpeta_transcripciones).pack(side="left", padx=10)

        # ==========================================
        # PESTAÑA 2: YOUTUBE → TEXTO
        # ==========================================
        tab_yt = self.trans_tabs.tab("YouTube → Texto")

        # Header informativo
        yt_info = ctk.CTkFrame(tab_yt, fg_color="#1a1a2e", corner_radius=8)
        yt_info.pack(fill="x", padx=185, pady=(10, 8))
        ctk.CTkLabel(yt_info,
                     text="📺  Pega un enlace de YouTube (o cualquier plataforma compatible)",
                     font=("Arial", 12), text_color="#aaa").pack(pady=(2, 0))
        ctk.CTkLabel(yt_info,
                     text="El audio se descarga como WAV temporal → Whisper lo transcribe → se elimina solo",
                     font=("Arial", 11), text_color="#666").pack(pady=(0, 2))

        # Fila de URL — centrada, no estirada al borde
        yt_url_row = ctk.CTkFrame(tab_yt, fg_color="transparent")
        yt_url_row.pack(anchor="center", pady=8)
        self.yt_trans_url = ctk.CTkEntry(
            yt_url_row,
            placeholder_text="Pega el link aquí (YouTube, FB, IG, etc)...",
            height=40, width=480, fg_color="#1a1a1a", border_color="#333"
        )
        self.yt_trans_url.pack(side="left", padx=(0, 6))
        self.yt_trans_url.bind("<Return>", lambda e: self.start_yt_transcribe())

        ctk.CTkButton(yt_url_row, text="📋 Pegar", width=70, height=40,
                      fg_color="#444", hover_color="#555",
                      command=lambda: (
                          self.yt_trans_url.delete(0, "end"),
                          self.yt_trans_url.insert(0, self.clipboard_get())
                      )).pack(side="left", padx=4)

        ctk.CTkButton(yt_url_row, text="🗑", width=38, height=40,
                      fg_color="#8B0000", hover_color="#cc0000",
                      command=lambda: self.yt_trans_url.delete(0, "end")).pack(side="left", padx=2)

        # Opciones de modelo, formato y destino
        yt_opts = ctk.CTkFrame(tab_yt, fg_color="#2b2b2b", corner_radius=8)
        yt_opts.pack(padx=126, pady=5, ipadx=10, ipady=8, fill="x")

        # --- GPU / CUDA (FIX 2a) ---
        yt_gpu_active, yt_gpu_text, yt_gpu_col = self.analyze_gpu_hardware(is_video=False)
        yt_default_on = yt_gpu_active and (yt_gpu_col == "#2cc985" or yt_gpu_col == "#f1c40f")
        self.yt_trans_use_gpu = ctk.BooleanVar(value=yt_default_on)
        yt_state_switch = "normal" if yt_gpu_active else "disabled"

        yt_gpu_frame = ctk.CTkFrame(yt_opts, fg_color="transparent")
        yt_gpu_frame.pack(pady=(12, 4))
        self.switch_yt_trans_gpu = ctk.CTkSwitch(yt_gpu_frame, text="Uso de GPU (CUDA)",
                                                  variable=self.yt_trans_use_gpu,
                                                  progress_color=c_main,
                                                  state=yt_state_switch)
        self.switch_yt_trans_gpu.pack(side="left", padx=5)
        ctk.CTkLabel(yt_gpu_frame, text=f"Estado: {yt_gpu_text}",
                     font=("Arial", 10, "bold"), text_color=yt_gpu_col).pack(side="left", padx=5)
        # ---------------------------

        yt_row1 = ctk.CTkFrame(yt_opts, fg_color="transparent")
        yt_row1.pack(pady=5)
        ctk.CTkLabel(yt_row1, text="Modelo IA:").pack(side="left", padx=5)
        self.yt_trans_model_var = ctk.StringVar(value="small (Recomendado)")
        ctk.CTkOptionMenu(
            yt_row1,
            values=["tiny (Muy Rápido)", "base (Rápido)", "small (Recomendado)",
                    "medium (Preciso)", "large (Solo GPU Potente)"],
            variable=self.yt_trans_model_var,
            width=185, fg_color=c_main, button_color=c_hover
        ).pack(side="left", padx=8)

        # Mismo orden que en la pestaña Archivos: Modelo IA · Traducir · Formato · Idioma
        self.yt_trans_traducir_var = ctk.BooleanVar(value=False)
        ctk.CTkCheckBox(yt_row1, text="Traducir al inglés", variable=self.yt_trans_traducir_var,
                        fg_color=c_main, hover_color=c_hover).pack(side="left", padx=(10, 5))

        yt_row2 = ctk.CTkFrame(yt_opts, fg_color="transparent")
        yt_row2.pack(pady=(0, 5))
        ctk.CTkLabel(yt_row2, text="Formato:").pack(side="left", padx=5)
        self.yt_trans_fmt_var = ctk.StringVar(value=".txt (Texto Plano)")
        ctk.CTkOptionMenu(
            yt_row2,
            values=[".txt (Texto Plano)", ".srt (Subtítulos)", ".vtt (Web Video)"],
            variable=self.yt_trans_fmt_var,
            width=150, fg_color="#444"
        ).pack(side="left", padx=10)

        # Idioma del audio (Automático = Whisper lo detecta solo)
        ctk.CTkLabel(yt_row2, text="Idioma:").pack(side="left", padx=(10, 5))
        self.yt_trans_lang_var = ctk.StringVar(value=TRANS_IDIOMA_AUTO)
        self._selector_idioma(yt_row2, self.yt_trans_lang_var).pack(side="left", padx=5)

        # --- Destino (FIX 1a): carpeta Transcripciones_YT en Descargas como default ---
        _yt_default_path = os.path.join(os.path.expanduser("~"), "Downloads", "Transcripciones_YT")

        def _on_yt_dest_change(v):
            """Maneja cambio de destino en tab YT, mostrando la ruta correcta."""
            if "Elegir Otra" in v:
                path = filedialog.askdirectory()
                if path:
                    self.yt_custom_dest_path = path
                    self.yt_trans_path_lbl.configure(text=f"↪ {path}")
                    self.previous_dest_selections[self.yt_trans_dest_seg] = v
                else:
                    prev = self.previous_dest_selections.get(self.yt_trans_dest_seg, "📁 Transcripciones YT")
                    self.yt_trans_dest_seg.set(prev)
                    if "Transcripciones YT" in prev:
                        self.yt_trans_path_lbl.configure(text=f"↪ {_yt_default_path}")
            else:
                self.yt_custom_dest_path = ""
                self.yt_trans_path_lbl.configure(text=f"↪ {_yt_default_path}")
                self.previous_dest_selections[self.yt_trans_dest_seg] = v

        yt_dest = ctk.CTkFrame(yt_opts, fg_color="transparent")
        yt_dest.pack(pady=5)
        self.yt_trans_dest_var = ctk.StringVar(value="📁 Transcripciones YT")
        self.yt_custom_dest_path = ""
        self.yt_trans_dest_seg = ctk.CTkSegmentedButton(
            yt_dest,
            values=["📁 Transcripciones YT", "↗️ Elegir Otra..."],
            variable=self.yt_trans_dest_var, selected_color=c_main,
            command=_on_yt_dest_change
        )
        self.yt_trans_dest_seg.pack()
        self.yt_trans_path_lbl = ctk.CTkLabel(yt_dest, text=f"↪ {_yt_default_path}",
                                               text_color="gray", font=("Arial", 10))
        self.yt_trans_path_lbl.pack()

        # Barra de progreso — con margen generoso (FIX 3a)
        yt_prog_frame = ctk.CTkFrame(tab_yt, fg_color="transparent")
        yt_prog_frame.pack(padx=126, pady=5, fill="x")
        self.yt_trans_progress = ctk.CTkProgressBar(
            yt_prog_frame, height=14, progress_color=c_main)
        self.yt_trans_progress.set(0)
        self.yt_trans_progress.pack(fill="x")
        self.yt_trans_status = ctk.CTkLabel(
            yt_prog_frame, text="Listo", text_color="gray", font=("Arial", 11))
        self.yt_trans_status.pack(pady=(4, 0))

        # Botones de acción
        yt_actions = ctk.CTkFrame(tab_yt, fg_color="transparent")
        yt_actions.pack(pady=8)
        self.yt_trans_btn = ctk.CTkButton(
            yt_actions, text="▶ DESCARGAR Y TRANSCRIBIR",
            height=45, width=240, fg_color=c_main, hover_color=c_hover,
            font=(self.main_font, 13, "bold"),
            command=self.start_yt_transcribe
        )
        self.yt_trans_btn.pack(side="left", padx=8)
        self.yt_trans_cancel_btn = ctk.CTkButton(
            yt_actions, text="⛔ Cancelar", height=45, width=110,
            fg_color="#c0392b", hover_color="#922b21", state="disabled",
            command=lambda: (setattr(self, 'cancel_requested', True),
                             self._whisper_detener_decodificacion())
        )
        self.yt_trans_cancel_btn.pack(side="left", padx=4)
        ctk.CTkButton(yt_actions, text="📂 Abrir Carpeta", height=45, width=140,
                      fg_color="#2b2b2b", hover_color="#3a3a3a", border_width=1, border_color="#555",
                      command=lambda: self._abrir_carpeta_transcripciones(yt=True)).pack(side="left", padx=8)

        # Log / resultado — con margen generoso (FIX 3a)
        self.yt_trans_log = ctk.CTkTextbox(
            tab_yt, height=160, fg_color="#101010",
            text_color="#e0e0e0", font=("Consolas", 12))
        self.yt_trans_log.pack(fill="x", padx=126, pady=(5, 0))

        yt_bot = ctk.CTkFrame(tab_yt, fg_color="transparent")
        yt_bot.pack(pady=6)
        ctk.CTkButton(yt_bot, text="📋 Copiar texto", width=120, fg_color="#444",
                      command=lambda: (
                          self.clipboard_clear(),
                          self.clipboard_append(self.yt_trans_log.get("1.0", "end").strip())
                      )).pack(side="left", padx=5)
        ctk.CTkButton(yt_bot, text="🗑 Limpiar", width=90, fg_color="#333",
                      command=lambda: (
                          self.yt_trans_log.configure(state="normal"),
                          self.yt_trans_log.delete("1.0", "end"),
                          self.yt_trans_log.configure(state="disabled")
                      )).pack(side="left", padx=5)

        # ==========================================
        # PESTAÑA 3: EN VIVO (ACTUALIZADA V2)
        # ==========================================
        tab_live = self.trans_tabs.tab("En Vivo")
        
        # --- A. BARRA DE CONFIGURACIÓN ---
        live_config = ctk.CTkFrame(tab_live, fg_color="#181818", corner_radius=10)
        live_config.pack(fill="x", padx=20, pady=(15, 10))
        
        # Fila 1: Micrófono (ESTILO MÁS LIMPIO)
        row_mic = ctk.CTkFrame(live_config, fg_color="transparent")
        row_mic.pack(fill="x", padx=10, pady=5)
        
        ctk.CTkLabel(row_mic, text="🎙️ Entrada de Audio:", font=("Arial", 12, "bold")).pack(side="left", padx=5)
        
        # Obtenemos nombres limpios
        mic_names = self.get_input_devices()
        
        # Variable y ComboBox
        self.live_mic_var = ctk.StringVar(value=mic_names[0] if mic_names else "No detectado")
        self.mic_combo = ctk.CTkComboBox(row_mic, values=mic_names, variable=self.live_mic_var, 
                                         width=400, fg_color="#333", button_color="#444",
                                         dropdown_fg_color="#2b2b2b", font=("Arial", 13))
        self.mic_combo.pack(side="left", padx=10)
        
        # Botón Recargar
        ctk.CTkButton(row_mic, text="🔄", width=30, fg_color="#444", hover_color="#555",
                      command=lambda: self.mic_combo.configure(values=self.get_input_devices())).pack(side="left")

        # --- [CAMBIO 3] Fila 2: Modelo + Ayuda + SWITCH GPU ---
        row_mod = ctk.CTkFrame(live_config, fg_color="transparent")
        row_mod.pack(fill="x", padx=10, pady=5)
        
        ctk.CTkLabel(row_mod, text="🧠 Modelo IA:", font=("Arial", 12, "bold")).pack(side="left", padx=5)
        
        self.live_model_var = ctk.StringVar(value="small (Recomendado)")
        self.live_model_menu = ctk.CTkOptionMenu(row_mod, 
                                                 values=["tiny (Ultra Rápido)", "base (Rápido)", "small (Equilibrado)", "medium (Preciso - GPU)", "large (Lento - GPU Potente)"],
                                                 variable=self.live_model_var, 
                                                 width=200, fg_color=c_main, button_color=c_hover)
        self.live_model_menu.pack(side="left", padx=5)

        # Botón de Ayuda
        ctk.CTkButton(row_mod, text="⁉️ ¿Cuál modelo elegir?", width=80, fg_color="#2b2b2b", border_width=1, border_color="#555", hover_color="#333",
                      command=self.open_model_help).pack(side="left", padx=5)

        # Idioma: en Automático se detecta en el primer fragmento con voz y luego
        # se mantiene (antes se volvía a detectar cada 5 s y podía saltar de idioma)
        ctk.CTkLabel(row_mod, text="Idioma:", font=("Arial", 12, "bold")).pack(side="left", padx=(15, 5))
        self.live_lang_var = ctk.StringVar(value=TRANS_IDIOMA_AUTO)
        self._selector_idioma(row_mod, self.live_lang_var).pack(side="left", padx=5)


        # --- GPU INTELIGENTE (WHISPER LIVE) ---
        # Reutilizamos la misma detección
        gpu_active, gpu_text, gpu_col = self.analyze_gpu_hardware(is_video=False)
        
        # Lógica Default
        default_on = gpu_active and (gpu_col == "#2cc985" or gpu_col == "#f1c40f")
        
        self.live_use_gpu = ctk.BooleanVar(value=default_on)
        state_switch = "normal" if gpu_active else "disabled"

        row_gpu = ctk.CTkFrame(live_config, fg_color="transparent")
        row_gpu.pack(fill="x", padx=10, pady=5)

        self.switch_live_gpu = ctk.CTkSwitch(row_gpu, text="Aceleración GPU (Live)", 
                                             variable=self.live_use_gpu, 
                                             progress_color="#e74c3c", # Rojo/Naranja para Live
                                             state=state_switch)
        self.switch_live_gpu.pack(side="left", padx=5)

        ctk.CTkLabel(row_gpu, text=f"Estado: {gpu_text}", 
                     font=("Arial", 10, "bold"), text_color=gpu_col).pack(side="left", padx=5)
        
        

        # --- B. CONTROL DE GRABACIÓN ---
        ctrl_live = ctk.CTkFrame(tab_live, fg_color="transparent")
        ctrl_live.pack(fill="x", padx=20, pady=5)
        
        self.btn_live_toggle = ctk.CTkButton(ctrl_live, text="🔴 INICIAR GRABACIÓN", width=200, height=50, 
                                             fg_color="#c0392b", hover_color="#a93226", font=(self.main_font, 14, "bold"),
                                             command=self.toggle_live_transcription)
        self.btn_live_toggle.pack(side="left", padx=10)
        
        self.lbl_live_timer = ctk.CTkLabel(ctrl_live, text="00:00:00", font=(self.main_font, 30, "bold"), text_color="white")
        self.lbl_live_timer.pack(side="left", padx=20)
        
        self.lbl_live_status = ctk.CTkLabel(ctrl_live, text="Listo", font=("Arial", 12), text_color="gray")
        self.lbl_live_status.pack(side="left", padx=10)

        # --- [CAMBIO 1] C. ÁREA DE TEXTO CON WRAP ---
        # Agregamos wrap="word" para que corte palabras completas al bajar de renglón
        self.live_textbox = ctk.CTkTextbox(tab_live, width=800, height=230, font=("Arial", 14), 
                                           fg_color="#1a1a1a", text_color="#eee",
                                           wrap="word") 
        self.live_textbox.pack(pady=10, padx=20, fill="both", expand=True)
        
        # --- D. BOTONES INFERIORES ---
        bot_live = ctk.CTkFrame(tab_live, fg_color="transparent")
        bot_live.pack(fill="x", padx=20, pady=10)
        
        ctk.CTkButton(bot_live, text="📋 Copiar Todo", width=120, fg_color="#444", 
                      command=lambda: self.clipboard_clear() or self.clipboard_append(self.live_textbox.get("1.0", "end"))).pack(side="left", padx=5)
        
        ctk.CTkButton(bot_live, text="💾 Guardar como TXT", width=150, fg_color=c_main, hover_color=c_hover,
                      command=self.save_live_text).pack(side="right", padx=5)

    # --- LÓGICA DE YOUTUBE → TRANSCRIBIR ---

    def start_yt_transcribe(self):
        """Valida la URL y lanza el hilo de descarga+transcripción."""
        url = self.yt_trans_url.get().strip()
        if not url:
            messagebox.showwarning("URL vacía", "Pega un enlace antes de continuar.")
            return
        if yt_dlp is None:
            msg = ("El módulo aún se está cargando en background, espera unos segundos."
                   if not _tier2_listo.is_set()
                   else "Instala o actualiza yt-dlp desde el módulo YouTube antes de usar esta función.")
            messagebox.showerror("yt-dlp no disponible", msg)
            return
        if WhisperModel is None:
            msg = ("El modelo de transcripción aún se está cargando en background, espera unos segundos."
                   if not _tier2_listo.is_set()
                   else "faster-whisper no disponible. Verifica la instalación.")
            messagebox.showerror("Whisper no disponible", msg)
            return
        if getattr(self, '_yt_trans_ocupado', False):
            messagebox.showwarning("Ocupado", "Ya hay una transcripción de YouTube en marcha.")
            return

        self.yt_trans_btn.configure(state="disabled")
        self.yt_trans_cancel_btn.configure(state="normal")
        self.cancel_requested = False
        self.yt_trans_progress.set(0)
        self.yt_trans_url.delete(0, "end")          # Limpiar URL — ya se pasó al hilo
        self.yt_trans_log.configure(state="normal")
        self.yt_trans_log.delete("1.0", "end")
        self.yt_trans_log.configure(state="disabled")

        threading.Thread(target=self._yt_trans_worker, args=(url,), daemon=True).start()

    def _yt_trans_worker(self, url):
        """
        Hilo de YouTube -> Texto. Pide turno en el carril de IA: si el OCR o la
        transcripción de archivos están trabajando, espera a que terminen en vez
        de cargar un segundo modelo y saturar la memoria.
        """
        self._yt_trans_ocupado = True
        try:
            def _espera(quien):
                self._en_ui(self.yt_trans_status.configure,
                            text=f"⏳ Esperando a que termine {quien}…", text_color="#d4ac0d")

            with self.carril_ia.turno("whisper", "Transcripción de YouTube",
                                      on_espera=_espera,
                                      debe_cortar=lambda: self.cancel_requested):
                self._con_uso_modelo("whisper", self.run_yt_transcribe, url)
        except _TrabajoDetenido:
            self._en_ui(self.yt_trans_status.configure,
                        text="⏹ Cancelado antes de empezar", text_color="orange")
        except Exception as e:
            print(f"[YT-Texto] Error inesperado: {e}")
        finally:
            self._yt_trans_ocupado = False
            self._en_ui(self.yt_trans_btn.configure, state="normal")
            self._en_ui(self.yt_trans_cancel_btn.configure, state="disabled")

    @staticmethod
    def _yt_trans_localizar(info, tmp_dir, tmp_id):
        """Ruta del audio que bajó yt-dlp (en su formato original: opus, m4a...)."""
        try:
            for d in (info or {}).get("requested_downloads") or []:
                ruta = d.get("filepath") or d.get("_filename")
                if ruta and os.path.isfile(ruta):
                    return ruta
        except Exception:
            pass
        try:
            for nombre in sorted(os.listdir(tmp_dir)):
                if (nombre.startswith(f"yt_trans_{tmp_id}.")
                        and not nombre.endswith((".part", ".ytdl", ".temp"))):
                    ruta = os.path.join(tmp_dir, nombre)
                    if os.path.isfile(ruta):
                        return ruta
        except OSError:
            pass
        return None

    def _yt_trans_temporales(self, tmp_id, *rutas):
        """Archivos temporales de una transcripción de YouTube que se pueden borrar."""
        encontrados = set()
        for r in rutas:
            if r and os.path.isfile(r):
                encontrados.add(os.path.abspath(r))
        if tmp_id:
            carpeta = tempfile.gettempdir()
            try:
                for nombre in os.listdir(carpeta):
                    if nombre.startswith(f"yt_trans_{tmp_id}"):
                        ruta = os.path.join(carpeta, nombre)
                        if os.path.isfile(ruta):
                            encontrados.add(os.path.abspath(ruta))
            except OSError:
                pass
        actual = getattr(self, 'current_temp_audio', None)
        if actual:
            encontrados.discard(os.path.abspath(actual))
        return sorted(encontrados)

    def run_yt_transcribe(self, url):
        """
        Flujo completo:
          1. Descargar el audio en su MEJOR formato original (opus/m4a), sin convertir
          2. Leerlo a memoria (16 kHz mono) con ffmpeg — sin WAV intermedio
          3. Transcribir con Whisper
          4. Guardar resultado
          5. Borrar el audio descargado automáticamente
        """
        tmp_audio = None
        tmp_id    = None
        audio     = None
        out_path  = ""

        def _log(msg, color="#e0e0e0"):
            def _do():
                self.yt_trans_log.configure(state="normal")
                self.yt_trans_log.insert("end", msg + "\n")
                self.yt_trans_log.see("end")
                self.yt_trans_log.configure(state="disabled")
            self.after(0, _do)

        def _status(msg, color="white", pct=None):
            self.after(0, lambda: self.yt_trans_status.configure(
                text=msg, text_color=color))
            if pct is not None:
                self.after(0, lambda p=pct: self.yt_trans_progress.set(p))

        try:
            # ── PRE-PASO: DETECCIÓN DE PLAYLIST / MIX ────────────────────
            _status("🔍 Analizando URL...", "cyan", 0.02)
            _log("📡 Analizando URL...")

            # 1. Inspección de la URL antes de llamar a yt-dlp
            import urllib.parse as _uparse
            _parsed   = _uparse.urlparse(url)
            _qparams  = _uparse.parse_qs(_parsed.query)
            _list_id  = _qparams.get('list', [''])[0]

            # Mix de YouTube: list empieza con RD / RDMM, o tiene start_radio=1
            _is_mix_url = bool(
                _list_id.startswith('RD')
                or _list_id.startswith('RDMM')
                or 'start_radio=1' in url
            )
            # Tratar como playlist real solo si hay list= Y NO es un mix
            _treat_as_playlist = bool(_list_id) and not _is_mix_url

            if _treat_as_playlist:
                # ── RAMA PLAYLIST: extraer con URL de playlist directa ────
                _pl_url  = f"https://www.youtube.com/playlist?list={_list_id}"
                _pl_opts = {
                    'quiet': True, 'no_warnings': True,
                    'extract_flat': True, 'socket_timeout': 15,
                    'subprocess_creationflags': subprocess.CREATE_NO_WINDOW,
                }
                try:
                    with yt_dlp.YoutubeDL(_pl_opts) as _ydl_pl:
                        _pl_info = _ydl_pl.extract_info(_pl_url, download=False)
                    _pl_entries   = [e for e in _pl_info.get('entries', []) if e]
                    _pl_title_raw = _pl_info.get('title', 'Playlist')
                except Exception as _pe:
                    print(f"[Trans] Error extrayendo playlist: {_pe}")
                    _treat_as_playlist = False   # fallback → video individual

                if _treat_as_playlist:
                    _pl_cfg = {
                        'raw_model': self.yt_trans_model_var.get(),
                        'use_gpu':   self.yt_trans_use_gpu.get(),
                        'fmt':       self.yt_trans_fmt_var.get(),
                        'dest_val':  self.yt_trans_dest_var.get(),
                        'dest_path': getattr(self, 'yt_custom_dest_path', ''),
                        'idioma':    TRANS_IDIOMAS.get(self.yt_trans_lang_var.get()),
                        'tarea':     "translate" if self.yt_trans_traducir_var.get() else "transcribe",
                    }
                    self.run_yt_transcribe_playlist(
                        url, _pl_entries, _pl_title_raw, _pl_cfg, _log, _status)
                    return

            # Si es Mix o URL sin list= → continúa como video individual
            if _is_mix_url:
                _log("🎲 Mix detectado — se transcribirá solo este video.")
            # ──────────────────────────────────────────────────────────────

            # ── PASO 1: DESCARGA DEL AUDIO ────────────────────────────────
            _status("⬇️  Descargando audio...", "cyan", 0.05)
            _log("📡 Conectando con la URL...")

            tmp_dir = tempfile.gettempdir()
            tmp_id  = uuid.uuid4().hex[:10]

            ydl_opts = {
                'format':      'bestaudio/best',
                'quiet':       True,
                'no_warnings': True,
                'noplaylist':  True,   # siempre un solo video en esta rama
                'outtmpl':     os.path.join(tmp_dir, f"yt_trans_{tmp_id}.%(ext)s"),
                'subprocess_creationflags': subprocess.CREATE_NO_WINDOW,
                # Sin postprocesador: se guarda el mejor audio TAL CUAL (opus/m4a).
                # Nada de WAV pesado; ffmpeg lo lee directo a memoria después.
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                title = info.get('title', 'Sin título')[:60] if info else 'Sin título'

            _log(f"✅ Descargado: {title}")
            _status("🔊 Preparando audio para Whisper...", "#3498db", 0.30)

            tmp_audio = self._yt_trans_localizar(info, tmp_dir, tmp_id)
            if not tmp_audio:
                raise FileNotFoundError("No se encontró el audio descargado.")

            # ── PASO 2: LEER EL AUDIO A MEMORIA (16 kHz mono, sin WAV) ────
            ext_audio = os.path.splitext(tmp_audio)[1].lstrip(".").upper() or "?"
            audio = self._whisper_decodificar(tmp_audio)
            if audio is not None:
                _log(f"⚡ Audio {ext_audio} leído a memoria ({audio.shape[0] / WHISPER_SR:.0f} s) — sin WAV intermedio.")

            if self.cancel_requested or audio is None:
                _status("❌ Cancelado por el usuario", "#e74c3c", 0)
                _log("🚫 Cancelado por el usuario.", "#f39c12")
                return

            # ── PASO 3: CARGAR MODELO ─────────────────────────────────────
            raw_model = self.yt_trans_model_var.get()
            model_size, local_path = self.get_local_model_path(raw_model)
            model_arg    = local_path if os.path.isdir(local_path) else model_size
            use_gpu      = self.yt_trans_use_gpu.get()          # FIX 2a: usar var propia del tab YT
            idioma       = TRANS_IDIOMAS.get(self.yt_trans_lang_var.get())      # None = automático
            tarea        = "translate" if self.yt_trans_traducir_var.get() else "transcribe"
            device       = "cuda" if use_gpu and torch.cuda.is_available() else "cpu"
            compute_type = "int8_float16" if device == "cuda" else "int8"
            current_cfg  = (model_size, device)

            # Si hay un modelo distinto cargado, liberarlo ANTES de cargar el nuevo
            # (evita doble uso de RAM/VRAM que crashea el programa)
            if getattr(self, 'faster_model', None) is not None and self.last_whisper_config != current_cfg:
                _status("🧹 Liberando modelo anterior...", "orange", 0.35)
                _log(f"🧹 Descargando modelo anterior ({self.last_whisper_config[0] if self.last_whisper_config else '?'})...")
                self.descargar_modelo_whisper()
                time.sleep(0.3)

            if getattr(self, 'faster_model', None) is None:
                is_downloading = not self._model_is_cached(model_size, local_path)
                if is_downloading:
                    _status(f"⬇️ Descargando modelo '{model_size}'...", "#e67e22", 0.40)
                    _log(f"⬇️  Descargando modelo '{model_size}' de HuggingFace...")
                else:
                    _status(f"📂 Cargando modelo '{model_size}'...", "cyan", 0.40)
                    _log(f"⚙️  Cargando modelo '{model_size}' en {device}...")

                load_r, load_e = [None], [None]
                def _load():
                    try:
                        load_r[0] = WhisperModel(model_arg, device=device, compute_type=compute_type,
                                                 **whisper_kwargs_dispositivo(device))
                    except Exception as ex:
                        load_e[0] = ex

                self.gestor_ia.antes_de_cargar("whisper")
                lt = threading.Thread(target=_load, daemon=True)
                lt.start()
                elapsed_s = 0
                # Loop con polling para mostrar progreso y detectar cancelación
                while lt.is_alive():
                    lt.join(timeout=2)
                    elapsed_s += 2
                    if self.cancel_requested:
                        _status("❌ Cancelado por el usuario", "#e74c3c", 0)
                        _log("🚫 Cancelado durante carga de modelo.", "#f39c12")
                        return
                    if is_downloading:
                        _status(f"⬇️ Descargando modelo '{model_size}'... ({elapsed_s}s)", "#e67e22",
                                min(0.40 + elapsed_s / 600, 0.54))
                    else:
                        _status(f"📂 Cargando modelo '{model_size}'... ({elapsed_s}s)", "cyan",
                                min(0.40 + elapsed_s / 600, 0.54))
                    if elapsed_s >= 600:
                        raise TimeoutError("Carga del modelo superó 600 s. Revisa tu conexión.")

                if load_e[0]:
                    raise load_e[0]
                with self._whisper_lock:
                    self.faster_model = load_r[0]
                    self.last_whisper_config = current_cfg
                self.gestor_ia.marcar_cargado("whisper")
                _log(f"✅ Modelo '{model_size}' listo en {device}.")
            else:
                _log(f"⚡ Modelo '{model_size}' ya en memoria.")

            # ── PASO 4: TRANSCRIBIR ───────────────────────────────────────
            _status("🎙️  Transcribiendo...", "#2cc985", 0.55)
            _log("🎙️  Iniciando Whisper...")

            total_dur = (audio.shape[0] / WHISPER_SR) or 1
            segments, info_w = _transcribe_safe(
                self.faster_model, audio,
                beam_size=5, **_trans_opts_idioma(idioma), task=tarea,
                condition_on_previous_text=True,
                vad_filter=True,
                vad_parameters=dict(min_silence_duration_ms=500)
            )

            full_segments = []
            for seg in segments:
                if self.cancel_requested:
                    _status("❌ Cancelado por el usuario", "#e74c3c", 0)
                    _log("🚫 Cancelado durante transcripción.", "#f39c12")
                    return
                full_segments.append(seg)
                pct_w = 0.55 + min(seg.end / total_dur, 1.0) * 0.35
                pct_i = int((seg.end / total_dur) * 100)
                _status(f"🎙️  Transcribiendo... {pct_i}%", "#2cc985", pct_w)

            detected_lang = info_w.language.upper() if info_w else "??"
            _log(f"✅ Idioma detectado: {detected_lang}  |  Segmentos: {len(full_segments)}")

            # ── PASO 5: GUARDAR (FIX 1a: lógica de destino corregida) ─────
            _status("💾  Guardando resultado...", "#9b59b6", 0.93)

            fmt = self.yt_trans_fmt_var.get()
            safe_title = re.sub(r'[<>:"/\\|?*]', '_', title).strip(". ")[:80] or "transcripcion"
            ext_out = ".srt" if ".srt" in fmt else (".vtt" if ".vtt" in fmt else ".txt")

            dest_val = self.yt_trans_dest_var.get()
            # Default: ~/Downloads/Transcripciones_YT
            base_folder = os.path.join(os.path.expanduser("~"), "Downloads", "Transcripciones_YT")
            if "Elegir Otra" in dest_val and getattr(self, 'yt_custom_dest_path', ''):
                base_folder = self.yt_custom_dest_path
            os.makedirs(base_folder, exist_ok=True)
            out_path = _ruta_unica(os.path.join(base_folder, f"{safe_title}{ext_out}"))
            # Guardar última carpeta usada para el botón 📂
            self.trans_last_folder = base_folder

            with open(out_path, "w", encoding="utf-8") as f:
                if ".txt" in fmt:
                    f.write(" ".join([s.text.strip() for s in full_segments]))
                elif ".srt" in fmt:
                    for idx, s in enumerate(full_segments):
                        a = self.format_timestamp(s.start, ',')
                        b = self.format_timestamp(s.end, ',')
                        f.write(f"{idx+1}\n{a} --> {b}\n{s.text.strip()}\n\n")
                elif ".vtt" in fmt:
                    f.write("WEBVTT\n\n")
                    for s in full_segments:
                        a = self.format_timestamp(s.start, '.')
                        b = self.format_timestamp(s.end, '.')
                        f.write(f"{a} --> {b}\n{s.text.strip()}\n\n")

            _log(f"💾 Guardado en: {out_path}")
            _status("✅  ¡Transcripción completada!", "#2ecc71", 1.0)

        except Exception as e:
            err = str(e)
            _log(f"❌ Error: {err[:120]}", "#e74c3c")
            _status(f"❌ Error: {err[:50]}", "red", 0)
            print(f"[YT-Transcribe] Error: {e}")

        finally:
            # Limpieza automática de TODOS los temporales de este video:
            # audio descargado y restos de una descarga cortada.
            audio = None
            for f in self._yt_trans_temporales(tmp_id, tmp_audio):
                try:
                    os.remove(f)
                    print(f"🗑 Temporal eliminado: {f}")
                except Exception:
                    pass

            self.after(0, lambda: self.yt_trans_btn.configure(state="normal"))
            self.after(0, lambda: self.yt_trans_cancel_btn.configure(state="disabled"))

    # =========================================================================
    # PLAYLIST TRANSCRIPCIÓN
    # =========================================================================

    def run_yt_transcribe_playlist(self, url, entries, pl_title_raw, cfg,
                                    _log, _status):
        """
        Orquestador para transcribir una playlist completa.
        Corre dentro del hilo daemon lanzado por start_yt_transcribe.
        El modelo se carga UNA sola vez y se reutiliza en todos los items.
        """
        CHECKPOINT_EVERY = 25
        total = len(entries)

        try:
            # --- 1. POPUP INICIAL ---
            continuar = self._en_ui_espera(
                messagebox.askyesno,
                "Playlist detectada",
                f"Se detectó una playlist de {total} video(s):\n\n"
                f"\"{pl_title_raw[:80]}\"\n\n"
                f"Se transcribirá cada video con el modelo seleccionado.\n"
                f"¿Deseas continuar?"
            )
            if not continuar:
                _status("Cancelado por usuario.", "orange", 0)
                _log("🚫 Transcripción de playlist cancelada.")
                return

            # --- 2. PREPARAR CARPETA DE DESTINO ---
            forbidden_chars = '<>:"/\\|?*\n\r\t'
            safe_pl = pl_title_raw[:80]
            safe_pl = "".join([c for c in safe_pl if c not in forbidden_chars]).strip(". ")
            if not safe_pl: safe_pl = "Playlist_Trans"

            base_folder = os.path.join(
                os.path.expanduser("~"), "Downloads", "Transcripciones_YT")
            if "Elegir Otra" in cfg['dest_val'] and cfg['dest_path']:
                base_folder = cfg['dest_path']
            pl_folder = os.path.join(base_folder, safe_pl)
            os.makedirs(pl_folder, exist_ok=True)

            # --- 3. CARGAR MODELO UNA SOLA VEZ ---
            raw_model = cfg['raw_model']
            use_gpu   = cfg['use_gpu']
            model_size, local_path = self.get_local_model_path(raw_model)
            model_arg    = local_path if os.path.isdir(local_path) else model_size
            device       = "cuda" if use_gpu and torch.cuda.is_available() else "cpu"
            compute_type = "int8_float16" if device == "cuda" else "int8"
            current_cfg  = (model_size, device)

            if getattr(self, 'faster_model', None) is not None \
                    and self.last_whisper_config != current_cfg:
                _status("🧹 Liberando modelo anterior...", "orange", 0.05)
                _log(f"🧹 Descargando modelo anterior...")
                self.descargar_modelo_whisper()
                time.sleep(0.3)

            if getattr(self, 'faster_model', None) is None:
                is_downloading = not self._model_is_cached(model_size, local_path)
                if is_downloading:
                    _status(f"⬇️ Descargando modelo '{model_size}'...", "#e67e22", 0.08)
                    _log(f"⬇️  Descargando modelo '{model_size}' de HuggingFace...")
                else:
                    _status(f"📂 Cargando modelo '{model_size}'...", "cyan", 0.08)
                    _log(f"⚙️  Cargando modelo '{model_size}' en {device}...")

                load_r, load_e = [None], [None]
                def _load_pl():
                    try:
                        load_r[0] = WhisperModel(
                            model_arg, device=device, compute_type=compute_type,
                            **whisper_kwargs_dispositivo(device))
                    except Exception as ex:
                        load_e[0] = ex

                self.gestor_ia.antes_de_cargar("whisper")
                lt = threading.Thread(target=_load_pl, daemon=True)
                lt.start()
                elapsed_s = 0
                while lt.is_alive():
                    lt.join(timeout=2)
                    elapsed_s += 2
                    if self.cancel_requested:
                        _status("❌ Cancelado", "#e74c3c", 0)
                        _log("🚫 Cancelado durante carga de modelo.")
                        return
                    lbl = f"⬇️" if is_downloading else "📂"
                    _status(f"{lbl} Cargando modelo '{model_size}'... ({elapsed_s}s)",
                            "#e67e22" if is_downloading else "cyan",
                            min(0.08 + elapsed_s / 600, 0.18))
                    if elapsed_s >= 600:
                        raise TimeoutError("Carga del modelo superó 600 s.")

                if load_e[0]: raise load_e[0]
                with self._whisper_lock:
                    self.faster_model = load_r[0]
                    self.last_whisper_config = current_cfg
                self.gestor_ia.marcar_cargado("whisper")
                _log(f"✅ Modelo '{model_size}' listo en {device}.")
            else:
                _log(f"⚡ Modelo '{model_size}' ya en memoria.")

            # --- 4. LOOP DE ITEMS ---
            done_count = 0
            _log(f"\n📋 Iniciando transcripción de playlist: {safe_pl}")
            _log(f"   Total: {total} videos  |  Destino: {pl_folder}\n")

            for i, entry in enumerate(entries):
                if self.cancel_requested:
                    _status(f"⛔ Detenido en {done_count}/{total}", "orange", 0)
                    _log(f"🚫 Cancelado por usuario en item {i}.")
                    break

                item_url = (entry.get('webpage_url')
                            or entry.get('url')
                            or (f"https://www.youtube.com/watch?v={entry['id']}"
                                if entry.get('id') else None))
                if not item_url:
                    _log(f"⚠️  Item {i+1}: sin URL, omitiendo.")
                    continue

                item_title_raw = entry.get('title') or f"Video_{i+1}"
                short = (item_title_raw[:50] + "..."
                         if len(item_title_raw) > 50 else item_title_raw)

                _status(f"({i+1}/{total}) {short}", "white",
                        (i) / total * 0.9 + 0.1)
                _log(f"─── [{i+1}/{total}] {short}")

                ok = self._trans_un_item(
                    item_url       = item_url,
                    item_title_raw = item_title_raw,
                    item_index     = i + 1,
                    out_folder     = pl_folder,
                    fmt            = cfg['fmt'],
                    idioma         = cfg.get('idioma'),
                    tarea          = cfg.get('tarea', "transcribe"),
                    _log           = _log,
                    _status        = _status,
                )
                if ok:
                    done_count += 1

                # Progreso general
                self.after(0, lambda p=(i + 1) / total: self.yt_trans_progress.set(p))

                # --- CHECKPOINT PERIÓDICO ---
                if done_count > 0 and done_count % CHECKPOINT_EVERY == 0 \
                        and (i + 1) < total:
                    remaining = total - (i + 1)
                    cont = self._en_ui_espera(
                        messagebox.askyesno,
                        "Continuar transcripción",
                        f"Van {done_count} transcripciones completadas.\n"
                        f"Quedan {remaining} video(s).\n\n"
                        f"¿Deseas continuar?"
                    )
                    if not cont:
                        _status(f"⏹ Detenido ({done_count}/{total})", "orange", 0)
                        _log(f"⏹ Detenido por usuario tras {done_count} transcripciones.")
                        return

                # --- ESPERA ENTRE ITEMS (menos probabilidad de bloqueos anti-bot) ---
                if (i + 1) < total:
                    _esperar_entre_items(
                        random.uniform(2, 5),
                        lambda: self.cancel_requested,
                        on_tick=lambda s: _status(f"⏳ Esperando {s}s antes del siguiente...", "#888", None)
                    )

            # --- 5. FINALIZACIÓN ---
            if not self.cancel_requested:
                _status(f"✅ Playlist terminada: {done_count}/{total} transcritos",
                        "#2ecc71", 1.0)
                _log(f"\n✅ Playlist completada: {done_count}/{total} archivos")
                _log(f"   Guardados en: {pl_folder}")

        except Exception as e:
            _log(f"❌ Error en playlist: {str(e)[:120]}")
            _status(f"❌ Error: {str(e)[:50]}", "red", 0)
            print(f"[Trans-Playlist] Error: {e}")

        finally:
            self.after(0, lambda: self.yt_trans_btn.configure(state="normal"))
            self.after(0, lambda: self.yt_trans_cancel_btn.configure(state="disabled"))

    # -------------------------------------------------------------------------

    def _trans_un_item(self, item_url, item_title_raw, item_index,
                        out_folder, fmt, _log, _status, idioma=None, tarea="transcribe"):
        """
        Descarga (mejor audio original), lee a memoria y transcribe un video de la playlist.
        Usa self.faster_model (ya cargado). Devuelve True si OK, False si falló.
        """
        tmp_audio = None
        tmp_id = None
        audio = None
        try:
            # -- Descargar el mejor audio tal cual (sin convertir a WAV) --
            tmp_dir = tempfile.gettempdir()
            tmp_id  = uuid.uuid4().hex[:10]

            ydl_opts = {
                'format':      'bestaudio/best',
                'quiet':       True,
                'no_warnings': True,
                'noplaylist':  True,
                'outtmpl':     os.path.join(tmp_dir, f"yt_trans_{tmp_id}.%(ext)s"),
                'subprocess_creationflags': subprocess.CREATE_NO_WINDOW,
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_item = ydl.extract_info(item_url, download=True)

            tmp_audio = self._yt_trans_localizar(info_item, tmp_dir, tmp_id)
            if not tmp_audio:
                _log(f"   ⚠️  Audio no encontrado para item {item_index}, omitiendo.")
                return False

            # -- Leer a memoria (16 kHz mono, sin WAV) --
            try:
                audio = self._whisper_decodificar(tmp_audio)
            except RuntimeError as e_audio:
                _log(f"   ⚠️  Item {item_index}: {str(e_audio)[:70]}, omitiendo.")
                return False

            if self.cancel_requested or audio is None:
                return False

            # -- Transcribir con modelo ya cargado --
            segments, info_w = _transcribe_safe(
                self.faster_model, audio,
                beam_size=5, **_trans_opts_idioma(idioma), task=tarea,
                condition_on_previous_text=True,
                vad_filter=True,
                vad_parameters=dict(min_silence_duration_ms=500)
            )

            full_segments = []
            for seg in segments:
                if self.cancel_requested:
                    return False
                full_segments.append(seg)

            detected_lang = info_w.language.upper() if info_w else "??"
            _log(f"   ✅ {len(full_segments)} segmentos  |  Idioma: {detected_lang}")

            # -- Guardar --
            forbidden_chars = '<>:"/\\|?*\n\r\t'
            safe_title = item_title_raw[:80]
            safe_title = "".join(
                [c for c in safe_title if c not in forbidden_chars]
            ).strip(". ") or f"item_{item_index}"

            ext_out = (".srt" if ".srt" in fmt
                       else (".vtt" if ".vtt" in fmt else ".txt"))
            out_path = _ruta_unica(os.path.join(out_folder, f"{safe_title}{ext_out}"))

            with open(out_path, "w", encoding="utf-8") as fh:
                if ".txt" in fmt:
                    fh.write(" ".join([s.text.strip() for s in full_segments]))
                elif ".srt" in fmt:
                    for idx, s in enumerate(full_segments):
                        a = self.format_timestamp(s.start, ',')
                        b = self.format_timestamp(s.end, ',')
                        fh.write(f"{idx+1}\n{a} --> {b}\n{s.text.strip()}\n\n")
                elif ".vtt" in fmt:
                    fh.write("WEBVTT\n\n")
                    for s in full_segments:
                        a = self.format_timestamp(s.start, '.')
                        b = self.format_timestamp(s.end, '.')
                        fh.write(f"{a} --> {b}\n{s.text.strip()}\n\n")

            _log(f"   💾 Guardado: {os.path.basename(out_path)}")
            return True

        except Exception as e:
            _log(f"   ❌ Error item {item_index}: {str(e)[:80]}")
            print(f"[Trans-Item {item_index}] Error: {e}")
            return False

        finally:
            # Limpiar todos los temporales del item siempre
            audio = None
            for f in self._yt_trans_temporales(tmp_id, tmp_audio):
                try:
                    os.remove(f)
                except Exception:
                    pass

    # =========================================================================
    # FIN PLAYLIST TRANSCRIPCIÓN
    # =========================================================================

    # --- LÓGICA DE TRANSCRIPCIÓN EN VIVO ---

    def toggle_live_transcription(self):
        if not self.live_recording:
            # INICIAR
            try:
                import pyaudio
                import wave
            except ImportError:
                messagebox.showerror("Falta Librería", "Necesitas instalar PyAudio para grabar.\nEjecuta: pip install pyaudio")
                return

            self.live_recording = True
            # [CAMBIO 2] NO iniciamos el timer aquí todavía.
            # self.live_start_time = time.time()  <-- BORRADO DE AQUÍ
            # self.update_live_timer()            <-- BORRADO DE AQUÍ
            
            self.btn_live_toggle.configure(text="⏹ DETENER", fg_color="#333", hover_color="#444")
            self.lbl_live_status.configure(text="Cargando modelo...", text_color="orange") # Feedback inicial
            self.live_textbox.delete("1.0", "end")
            self.live_text_buffer = ""
            
            # [CAMBIO 2] Movemos la carga pesada al hilo para no congelar la UI visualmente
            # pero el hilo se encargará de iniciar el contador cuando esté listo.
            threading.Thread(target=self._live_worker, daemon=True).start()
            
        else:
            # DETENER
            self.stop_live_recording()

    def _live_worker(self):
        """
        Hilo de la grabación en vivo. Pide turno en el carril de IA: si el OCR o
        una transcripción de archivos están trabajando, espera a que terminen en
        vez de cargar otro modelo encima (y avisa en pantalla a quién espera).
        """
        try:
            def _espera(quien):
                self._en_ui(self.lbl_live_status.configure,
                            text=f"⏳ Esperando a que termine {quien}…", text_color="#d4ac0d")

            with self.carril_ia.turno("whisper", "Transcripción en vivo", on_espera=_espera,
                                      debe_cortar=lambda: not self.live_recording):
                self._con_uso_modelo("whisper", self.run_live_process)
        except _TrabajoDetenido:
            self._en_ui(self.lbl_live_status.configure,
                        text="⏹ Cancelado antes de empezar", text_color="gray")
            self._live_loop_done.set()
        except Exception as e:
            print(f"[En vivo] Error: {e}")
            self._live_loop_done.set()
            self._en_ui(self.stop_live_recording)

    def stop_live_recording(self):
        self.live_recording = False
        self.after(0, lambda: self.btn_live_toggle.configure(
            text="🔴 INICIAR GRABACIÓN", fg_color="#c0392b", hover_color="#a93226"))
        self.after(0, lambda: self.lbl_live_status.configure(
            text="Finalizando...", text_color="gray"))

        def cleanup_after_stop():
            # Esperar a que el bucle de grabación termine de forma natural.
            # En CPU el último chunk puede tardar bastante en transcribirse,
            # por eso usamos 60 s en lugar de 8 s.
            self._live_loop_done.wait(timeout=60)
            if not self.live_recording:
                # El modelo NO se descarga aquí: queda cargado para que volver a
                # grabar (o transcribir un archivo con el mismo modelo) sea
                # instantáneo. El gestor de modelos lo libera solo cuando otro
                # módulo necesita la memoria o tras 20 minutos sin usarse.
                print("⏹ Grabación detenida. El modelo queda listo para reutilizarse.")
                self._en_ui(self.lbl_live_status.configure,
                            text="Listo (modelo en memoria)", text_color="gray")

        threading.Thread(target=cleanup_after_stop, daemon=True).start()

    def update_live_timer(self):
        if self.live_recording:
            elapsed = int(time.time() - self.live_start_time)
            h, rem = divmod(elapsed, 3600)
            m, s = divmod(rem, 60)
            self.lbl_live_timer.configure(text=f"{h:02}:{m:02}:{s:02}")
            
            # --- CHEQUEO DE INACTIVIDAD (5 min = 300s) ---
            time_since_check = time.time() - self.last_activity_check
            if time_since_check > 300: # 5 minutos
                self.show_inactivity_popup()
            
            self.after(1000, self.update_live_timer)

    def show_inactivity_popup(self):
        # Evitar múltiples popups
        if hasattr(self, 'inactivity_window') and self.inactivity_window and self.inactivity_window.winfo_exists():
            return

        # Nace oculta y centrada (con ícono); se muestra al terminar de armarla
        self.inactivity_window = self._ventana_nueva("¿Sigues ahí?", 400, 250)
        # Es una alerta: se mantiene por encima aunque estés en otra aplicación
        self.inactivity_window.attributes("-topmost", True)

        ctk.CTkLabel(self.inactivity_window, text="⚠️ Control de Inactividad", font=("Arial", 18, "bold"), text_color="orange").pack(pady=20)
        ctk.CTkLabel(self.inactivity_window, text="Llevas 5 minutos grabando.\n¿Deseas continuar?", font=("Arial", 14)).pack(pady=10)

        self.lbl_countdown = ctk.CTkLabel(self.inactivity_window, text="Cierre automático en: 120s", text_color="#c0392b")
        self.lbl_countdown.pack(pady=5)

        def confirm_presence():
            self.last_activity_check = time.time() # Resetear contador de 5 min
            self.inactivity_window.destroy()

        ctk.CTkButton(self.inactivity_window, text="Sí, sigo aquí (Extender 5 min)", height=40, fg_color="#27ae60", command=confirm_presence).pack(pady=20)
        self._ventana_mostrar(self.inactivity_window, recentrar=False)

        # Cuenta regresiva de 2 min con after() (en el hilo de la interfaz, sin hilos)
        self.after(1000, lambda w=self.inactivity_window: self.run_popup_countdown(w, 119))

    def run_popup_countdown(self, window, remaining):
        try:
            if not window.winfo_exists() or not self.live_recording:
                return
        except Exception:
            return
        if remaining > 0:
            try:
                self.lbl_countdown.configure(text=f"Cierre automático en: {remaining}s")
            except Exception:
                return
            self.after(1000, lambda: self.run_popup_countdown(window, remaining - 1))
            return
        # Se acabó el tiempo y la ventana sigue abierta -> CORTAR
        window.destroy()
        self.stop_live_recording()
        messagebox.showinfo("Tiempo Agotado", "La grabación se detuvo por inactividad.")

    @staticmethod
    def _live_punto_de_corte(audio, rate, objetivo_s):
        """
        Dónde cortar un fragmento para no partir palabras: el momento más
        silencioso (ventanas de 100 ms) del último segundo.
        """
        n = len(audio)
        ini = int(max(0.0, objetivo_s - 1.0) * rate)
        ventana = max(1, int(0.1 * rate))
        k = (n - ini) // ventana
        if k < 2:
            return n
        zona = audio[ini:ini + k * ventana].reshape(k, ventana)
        j = int(np.argmin((zona * zona).mean(axis=1)))
        return ini + j * ventana + ventana // 2

    def _live_transcribir(self, audio, idioma, detectar):
        """
        Transcribe un fragmento (float32, 16 kHz) con el modelo cargado.
        Si el idioma es Automático, se fija con la primera detección confiable:
        así no salta de idioma entre fragmentos. Devuelve (texto, idioma).
        """
        texto, info = "", None
        # El lock evita que descargar_modelo_whisper() destruya el modelo a mitad de
        # la inferencia. Nada de la interfaz se toca mientras se sostiene el lock.
        with self._whisper_lock:
            model_ref = self.faster_model
            if model_ref is not None:
                segments, info = _transcribe_safe(model_ref, audio, beam_size=2,
                                                  **_trans_opts_idioma(idioma))
                texto = " ".join(s.text for s in segments).strip()
            model_ref = None
        if (detectar and idioma is None and texto and info is not None
                and (getattr(info, "language_probability", 0) or 0) >= 0.6):
            idioma = info.language
            self.after(0, lambda i=idioma: self.lbl_live_status.configure(
                text=f"● Grabando... (idioma: {i.upper()})", text_color="#e74c3c"))
        return texto, idioma

    def run_live_process(self):
        import pyaudio

        # Marcar que el bucle está en marcha
        self._live_loop_done.clear()

        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = WHISPER_SR          # 16 kHz: lo que Whisper usa por dentro
        FRAGMENTO_S = 5            # segundos por fragmento (como antes)

        target_index = self.get_selected_mic_index()
        idioma_elegido = TRANS_IDIOMAS.get(self.live_lang_var.get())    # None = automático

        # --- CARGA DE MODELO ---
        try:
            self.check_load_whisper_model()
            self.live_start_time = time.time()
            self.last_activity_check = time.time()
            self.after(0, self.update_live_timer)
            self.after(0, lambda: self.lbl_live_status.configure(
                text="● Grabando...", text_color="#e74c3c"))
        except Exception as e:
            print(f"Error cargando modelo en live: {e}")
            self._live_loop_done.set()   # señal: terminamos (aunque con error)
            self.after(0, self.stop_live_recording)
            return

        p = pyaudio.PyAudio()
        try:
            stream = p.open(format=FORMAT,
                            channels=CHANNELS,
                            rate=RATE,
                            input=True,
                            input_device_index=target_index,
                            frames_per_buffer=CHUNK)
        except Exception as e:
            print(f"Error abriendo micrófono: {e}")
            try:
                p.terminate()
            except Exception:
                pass
            self._live_loop_done.set()
            self.after(0, self.stop_live_recording)
            return

        # El micrófono se lee SIN PAUSA en un hilo aparte: mientras Whisper
        # transcribe un fragmento, el siguiente se sigue grabando. Antes, durante
        # la transcripción nadie leía el micrófono y ese audio se perdía.
        cola = queue.Queue()
        capturando = threading.Event()
        capturando.set()

        def _capturar():
            while capturando.is_set():
                try:
                    cola.put(stream.read(CHUNK, exception_on_overflow=False))
                except Exception:
                    time.sleep(0.01)

        hilo_captura = threading.Thread(target=_capturar, name="dmt_live_mic", daemon=True)
        hilo_captura.start()

        def _tomar(bloques_max=None):
            datos = []
            while bloques_max is None or len(datos) < bloques_max:
                try:
                    datos.append(cola.get_nowait())
                except queue.Empty:
                    break
            if not datos:
                return np.zeros(0, dtype=np.float32)
            return np.frombuffer(b"".join(datos), dtype=np.int16).astype(np.float32) / 32768.0

        def _publicar(texto):
            if texto:
                self.live_text_buffer += texto + " "
                self.after(0, lambda t=texto: self.append_live_text(t))

        idioma = idioma_elegido
        pendiente = np.zeros(0, dtype=np.float32)
        try:
            while self.live_recording:
                pendiente = np.concatenate([pendiente, _tomar()])
                if len(pendiente) < FRAGMENTO_S * RATE:
                    time.sleep(0.05)
                    continue
                corte = self._live_punto_de_corte(pendiente, RATE, FRAGMENTO_S)
                fragmento, pendiente = pendiente[:corte], pendiente[corte:]
                try:
                    texto, idioma = self._live_transcribir(fragmento, idioma, idioma_elegido is None)
                    _publicar(texto)
                except Exception as e:
                    print(f"Error Live: {e}")
        finally:
            capturando.clear()
            hilo_captura.join(timeout=1.5)
            # Lo último que se dijo antes de DETENER también se transcribe
            try:
                resto = np.concatenate([pendiente, _tomar()])
                if len(resto) >= int(0.5 * RATE):
                    texto, _ = self._live_transcribir(resto, idioma, False)
                    _publicar(texto)
            except Exception as e:
                print(f"Error Live (último fragmento): {e}")
            # Asegurar cierre limpio del audio
            try:
                stream.stop_stream()
                stream.close()
            except Exception:
                pass
            try:
                # Pausa mínima para que PortAudio libere los recursos del driver
                # antes de Pa_Terminate(). Sin este margen, el driver de audio
                # (WASAPI/DirectSound en Windows) puede acceder a memoria ya
                # liberada → crash a nivel C que no captura try/except.
                time.sleep(0.2)
                p.terminate()
            except Exception:
                pass
            # Señal para que cleanup_after_stop proceda
            self._live_loop_done.set()

    def append_live_text(self, text):
        self.live_textbox.insert("end", text + " ")
        self.live_textbox.see("end") # Auto-scroll

    def save_live_text(self):
        content = self.live_textbox.get("1.0", "end").strip()
        if not content: return
        
        f = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Texto", "*.txt")])
        if f:
            with open(f, "w", encoding="utf-8") as file:
                file.write(content)
            messagebox.showinfo("Guardado", "Transcripción guardada correctamente.")

    def check_load_whisper_model(self):
        """
        Carga el modelo para el modo EN VIVO (Live).
        Primero busca modelo local; si no existe, lo descarga automáticamente.
        """
        if self.live_recording:
            raw_selection = self.live_model_var.get()
            use_gpu_flag  = self.live_use_gpu.get()
        else:
            raw_selection = self.trans_model_var.get()
            use_gpu_flag  = self.trans_use_gpu.get()

        model_size, local_path = self.get_local_model_path(raw_selection)

        has_gpu = torch.cuda.is_available() and use_gpu_flag
        device  = "cuda" if has_gpu else "cpu"
        compute_type = "int8_float16" if device == "cuda" else "int8"

        # Protección CPU
        if device == "cpu" and model_size in ["medium", "large"]:
            print(f"⚠️ '{model_size}' en CPU — cambiando a 'small'.")
            if self.live_recording:
                self.after(0, lambda: self.live_textbox.insert(
                    "end", "\n[SISTEMA]: ⚠️ CPU detectada. Cambiando a 'small'.\n\n"))
                self.after(0, lambda: self.live_model_var.set("small (Equilibrado)"))
            model_size, local_path = self.get_local_model_path("small")

        current_config = (model_size, device)

        if self.faster_model is not None and self.last_whisper_config == current_config:
            return   # Modelo ya cargado con la misma config

        # Limpiar modelo anterior de forma segura
        with self._whisper_lock:
            old = self.faster_model
            self.faster_model = None
        if old is not None:
            # CRÍTICO: vaciar caché CUDA *antes* de destruir el modelo.
            # ctranslate2 libera su contexto CUDA al hacer del(old); si
            # llamamos torch.cuda.empty_cache() después, el contexto ya no
            # existe → crash a nivel C que Python no puede atrapar.
            # (mismo principio que en descargar_modelo_whisper)
            try:
                if torch.cuda.is_available():
                    torch.cuda.empty_cache()
            except Exception:
                pass
            try:
                del old
            except Exception:
                pass
            try:
                gc.collect()
            except Exception:
                pass

        # Decidir: local o auto-descarga
        model_arg = local_path if os.path.isdir(local_path) else model_size

        self.after(0, lambda: self.lbl_live_status.configure(
            text=f"Cargando {model_size}...", text_color="orange"))

        # Cargar con watchdog de 120 s para detectar cuelgues
        result = [None]
        error  = [None]

        def _load():
            try:
                result[0] = WhisperModel(model_arg, device=device, compute_type=compute_type,
                                         **whisper_kwargs_dispositivo(device))
            except Exception as e:
                error[0] = e

        self.gestor_ia.antes_de_cargar("whisper")
        load_thread = threading.Thread(target=_load, daemon=True)
        load_thread.start()
        load_thread.join(timeout=600)

        if load_thread.is_alive():
            raise TimeoutError(f"Carga del modelo '{model_size}' superó 600 s sin respuesta. Revisa tu conexión.")
        if error[0] is not None:
            raise error[0]

        with self._whisper_lock:
            self.faster_model = result[0]
            self.last_whisper_config = current_config
        self.gestor_ia.marcar_cargado("whisper")
        print(f"✅ Modelo '{model_size}' cargado en {device}.")

    
    def _model_is_cached(self, model_size, local_path):
        """
        Devuelve True si el modelo ya está descargado en disco, ya sea en la
        carpeta local de la app O en el caché estándar de HuggingFace Hub.
        Evita mostrar 'Descargando' cuando el modelo ya existe localmente.

        IMPORTANTE: El modelo 'large' se descarga como 'large-v3' (o v2/v1)
        en HuggingFace, por eso hay que buscar todas las variantes.
        """
        # 1. Carpeta local de la app (ruta exacta que devuelve get_local_model_path)
        if os.path.isdir(local_path):
            return True

        # 2. Para 'large', buscar también carpetas locales con sufijo de versión
        #    (por si el usuario las puso manualmente como faster-whisper-large-v3)
        if model_size == "large":
            local_base = os.path.dirname(local_path)
            for variant in ("large-v3", "large-v2", "large-v1"):
                if os.path.isdir(os.path.join(local_base, f"faster-whisper-{variant}")):
                    return True

        # 3. Caché de HuggingFace Hub (donde faster-whisper descarga por defecto)
        hf_cache = os.path.join(os.path.expanduser("~"), ".cache", "huggingface", "hub")
        if not os.path.isdir(hf_cache):
            return False

        # Nombre exacto
        if os.path.isdir(os.path.join(hf_cache, f"models--Systran--faster-whisper-{model_size}")):
            return True

        # Para 'large': probar variantes v3, v2, v1 (faster-whisper usa large-v3 por defecto)
        if model_size == "large":
            for variant in ("large-v3", "large-v2", "large-v1"):
                if os.path.isdir(os.path.join(hf_cache, f"models--Systran--faster-whisper-{variant}")):
                    return True

        return False

    def _whisper_decodificar(self, ruta):
        """
        Decodifica el audio de CUALQUIER archivo (audio o video) directo a memoria,
        en el formato exacto que Whisper usa por dentro: float32, 16 kHz, mono.

        · Sin filtros: Whisper rinde mejor con el audio crudo (su front-end log-Mel
          ya maneja el volumen; normalizar/filtrar no ayuda y puede dar alucinaciones).
        · Sin archivos temporales: FFmpeg escribe al pipe y aquí se arma el arreglo.
        · Corre en un proceso aparte (no compite con la interfaz) y se puede matar.

        Devuelve np.ndarray, o None si se canceló.
        Lanza RuntimeError con un mensaje claro si FFmpeg no puede leer el audio.
        """
        cmd = ["ffmpeg", "-nostdin", "-hide_banner", "-loglevel", "error", "-threads", "0",
               "-i", ruta, "-vn", "-sn", "-dn",
               "-ac", "1", "-ar", str(WHISPER_SR),
               "-f", "f32le", "-acodec", "pcm_f32le", "pipe:1"]
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                startupinfo=self.get_startup_info(),
                                creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
        self._whisper_decoders.add(proc)

        errores = []

        def _drenar_stderr():
            # Leer stderr en paralelo evita que el pipe se llene y congele a FFmpeg
            try:
                for linea in iter(proc.stderr.readline, b""):
                    texto = linea.decode("utf-8", "ignore").strip()
                    if texto:
                        errores.append(texto)
                        del errores[:-20]
            except Exception:
                pass

        hilo_err = threading.Thread(target=_drenar_stderr, daemon=True)
        hilo_err.start()

        datos = bytearray()
        try:
            while True:
                bloque = proc.stdout.read(1 << 20)     # 1 MiB ≈ 16 s de audio
                if not bloque:
                    break
                datos += bloque
                if self.cancel_requested:
                    try: proc.kill()
                    except Exception: pass
                    break
            proc.wait()
        finally:
            self._whisper_decoders.discard(proc)
            try: proc.stdout.close()
            except Exception: pass
        hilo_err.join(timeout=2)

        if self.cancel_requested:
            return None
        if proc.returncode != 0:
            detalle = errores[-1] if errores else f"código {proc.returncode}"
            todo = " ".join(errores).lower()
            if ("does not contain any stream" in todo or "matches no streams" in todo
                    or "no audio" in todo):
                raise RuntimeError("El archivo no tiene pista de audio")
            raise RuntimeError(f"FFmpeg no pudo leer el audio: {detalle[:160]}")

        usable = len(datos) - (len(datos) % 4)
        if usable <= 0:
            raise RuntimeError("El archivo no tiene audio (0 muestras)")
        if usable != len(datos):
            del datos[usable:]
        return np.frombuffer(datos, dtype=np.float32)

    def _whisper_detener_decodificacion(self):
        """Mata cualquier decodificación en curso (SALTAR / cancelar)."""
        for proc in list(getattr(self, "_whisper_decoders", ())):
            try:
                proc.kill()
            except Exception:
                pass

    def descargar_modelo_whisper(self):
        """
        Libera el modelo de RAM/VRAM de forma segura desde CUALQUIER hilo.
        Usa un Lock para evitar que dos hilos lo borren al mismo tiempo (crash).

        IMPORTANTE: el Lock solo protege el intercambio del puntero. El cleanup
        pesado (del, gc, cuda) ocurre FUERA del lock para no bloquear a
        ctranslate2 mientras libera sus propios threads internos.
        """
        print("🧹 Liberando recursos de Whisper...")
        # Solo capturamos la referencia y ponemos el puntero a None dentro del lock.
        # Así otros hilos dejan de ver el modelo de inmediato sin que tengamos
        # que mantener el lock durante la destrucción (que puede invocar CUDA).
        with self._whisper_lock:
            model = self.faster_model
            self.faster_model = None
            self.last_whisper_config = None

        # La destrucción real del objeto ocurre aquí, fuera del lock.
        if model is not None:
            # IMPORTANTE: vaciar caché CUDA *antes* de destruir el modelo.
            # ctranslate2 libera su contexto CUDA al hacer del(model); si
            # llamamos torch.cuda.empty_cache() después, el contexto ya no
            # existe y provoca un crash a nivel C que no captura try/except.
            try:
                if torch.cuda.is_available():
                    torch.cuda.empty_cache()
            except Exception:
                pass
            try:
                del model
            except Exception as e:
                print(f"[Whisper cleanup] del model: {e}")
        try:
            gc.collect()
        except Exception:
            pass
        try:
            self.gestor_ia.marcar_descargado("whisper")
        except Exception:
            pass
        print("✅ Modelo liberado.")

    def convert_transcribe_logic(self, source_path):
        # --- GUARD TIER-2: si WhisperModel aún no cargó ---
        if WhisperModel is None:
            msg = ("⏳ Módulo de transcripción preparándose..."
                   if not _tier2_listo.is_set()
                   else "❌ faster-whisper no disponible. Verifica la instalación.")
            return False, msg

        out_path      = ""
        duration_str  = "00:00"
        audio         = None
        t_total_start = time.time()   # ← tiempo total (desde que arranca el archivo)

        def _ui(fn):
            """Aplica cambios de UI de forma thread-safe."""
            try:
                self.after(0, fn)
            except Exception:
                pass

        try:
            # 1. LEER CONFIGURACIÓN
            raw_model_text = self.trans_model_var.get()
            use_gpu        = self.trans_use_gpu.get()
            idioma         = TRANS_IDIOMAS.get(self.trans_lang_var.get())     # None = automático
            tarea          = "translate" if self.trans_traducir_var.get() else "transcribe"

            model_size, local_path = self.get_local_model_path(raw_model_text)

            device       = "cuda" if use_gpu and torch.cuda.is_available() else "cpu"
            compute_type = "int8_float16" if device == "cuda" else "int8"
            current_config = (model_size, device)

            # Decidir: local (offline) o auto-descarga
            model_arg = local_path if os.path.isdir(local_path) else model_size

            # Limpiar si cambió config
            current_model_ref = getattr(self, 'faster_model', None)
            if current_model_ref is not None and self.last_whisper_config != current_config:
                _ui(lambda: self.trans_status.configure(
                    text="🧹 Cambiando modelo...", text_color="orange"))
                self.descargar_modelo_whisper()
                time.sleep(0.3)

            # 2. LEER AUDIO A MEMORIA (ffmpeg → 16 kHz mono, sin WAV temporal)
            _ui(lambda: self.trans_status.configure(
                text="🔊 Leyendo audio (ffmpeg)...", text_color="#3498db"))
            _ui(lambda: self.trans_progress.set(0.05))

            # La decodificación corre en paralelo mientras verificamos/cargamos modelo
            with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
                future_audio = executor.submit(self._whisper_decodificar, source_path)

                # 3. CARGAR MODELO (si aún no está listo)
                if getattr(self, 'faster_model', None) is None:
                    is_downloading = not self._model_is_cached(model_size, local_path)
                    if is_downloading:
                        _ui(lambda: self.trans_status.configure(
                            text=f"⬇️ Descargando modelo {model_size} de internet...",
                            text_color="#e67e22"))
                    else:
                        _ui(lambda: self.trans_status.configure(
                            text=f"📂 Cargando modelo {model_size} (local)...",
                            text_color="cyan"))
                    _ui(lambda: self.trans_progress.set(0.10))

                    # Watchdog de carga (120 s)
                    load_result = [None]
                    load_error  = [None]

                    def _load_model():
                        try:
                            load_result[0] = WhisperModel(
                                model_arg, device=device, compute_type=compute_type,
                                **whisper_kwargs_dispositivo(device))
                        except Exception as e:
                            load_error[0] = e

                    self.gestor_ia.antes_de_cargar("whisper")
                    lt = threading.Thread(target=_load_model, daemon=True)
                    lt.start()
                    elapsed_s = 0
                    is_downloading = not self._model_is_cached(model_size, local_path)
                    while lt.is_alive():
                        lt.join(timeout=2)
                        elapsed_s += 2
                        # Salir del loop si el usuario canceló (el hilo de descarga sigue en bg)
                        if self.cancel_requested:
                            _ui(lambda: self.trans_status.configure(
                                text="⚠️ Cancelando... (esperando hilo de carga)",
                                text_color="orange"))
                            break
                        if is_downloading:
                            _ui(lambda s=elapsed_s: self.trans_status.configure(
                                text=f"⬇️ Descargando modelo {model_size}... ({s}s)",
                                text_color="#e67e22"))
                        else:
                            _ui(lambda s=elapsed_s: self.trans_status.configure(
                                text=f"📂 Cargando modelo {model_size}... ({s}s)",
                                text_color="cyan"))
                        pct = min(0.10 + elapsed_s / 600, 0.45)
                        _ui(lambda p=pct: self.trans_progress.set(p))
                        if elapsed_s >= 600:
                            raise TimeoutError(
                                f"Carga del modelo '{model_size}' superó 600 s. Revisa tu conexión.")

                    if load_error[0]:
                        raise load_error[0]

                    # Solo asignar si no cancelamos y el modelo cargó correctamente
                    if not self.cancel_requested and load_result[0] is not None:
                        with self._whisper_lock:
                            self.faster_model = load_result[0]
                            self.last_whisper_config = current_config
                        self.gestor_ia.marcar_cargado("whisper")
                        print(f"✅ Modelo '{model_size}' cargado en {device}.")
                    elif self.cancel_requested:
                        raise InterruptedError("Cancelado durante carga de modelo")
                else:
                    _ui(lambda: self.trans_status.configure(
                        text=f"⚡ Modelo {model_size} ya listo en memoria",
                        text_color="#27ae60"))

                # Esperar a que termine la lectura del audio
                _ui(lambda: self.trans_status.configure(
                    text="⏳ Terminando de leer el audio...", text_color="#3498db"))
                try:
                    audio = future_audio.result()
                except RuntimeError as e_audio:
                    # Error del archivo (p. ej. sin pista de audio): el modelo se queda cargado
                    return False, f"❌ {str(e_audio)[:60]}", ""

            if self.cancel_requested:
                raise InterruptedError("Cancelado")

            if audio is None or audio.size == 0:
                return False, "❌ No se pudo leer el audio", ""

            # 4. TRANSCRIPCIÓN (duración exacta a partir de las muestras)
            total_duration = (audio.shape[0] / WHISPER_SR) or 1

            _ui(lambda: self.trans_status.configure(
                text="🎙️ Iniciando transcripción Whisper...", text_color="#2cc985"))
            _ui(lambda: self.trans_progress.set(0.50))

            t_model_start = time.time()   # ← tiempo NETO del modelo

            segments, info = _transcribe_safe(
                self.faster_model, audio,
                beam_size=5, **_trans_opts_idioma(idioma), task=tarea,
                condition_on_previous_text=True,
                vad_filter=True,
                vad_parameters=dict(min_silence_duration_ms=500)
            )

            full_segments = []
            for seg in segments:
                if self.cancel_requested:
                    raise InterruptedError("Cancelado por usuario")
                full_segments.append(seg)
                progress = 0.50 + min(seg.end / total_duration, 1.0) * 0.45
                pct_int  = int((seg.end / total_duration) * 100)
                _ui(lambda p=progress: self.trans_progress.set(p))
                _ui(lambda pct=pct_int: self.trans_status.configure(
                    text=f"🎙️ Transcribiendo... {pct}%", text_color="#2cc985"))

            # Calcular tiempos
            t_model_secs = int(time.time() - t_model_start)
            t_total_secs = int(time.time() - t_total_start)

            mm, ms = divmod(t_model_secs, 60)
            tm, ts = divmod(t_total_secs, 60)
            duration_str = f"Total:{tm:02}m:{ts:02}s | Modelo:{mm:02}m:{ms:02}s"

            # 5. GUARDAR
            _ui(lambda: self.trans_status.configure(
                text="💾 Guardando archivo...", text_color="#9b59b6"))
            _ui(lambda: self.trans_progress.set(0.97))

            fmt    = self.trans_fmt_var.get()
            folder = os.path.dirname(source_path)

            if "TRANSCRIPCIONES" in self.trans_dest_var.get():
                folder = os.path.join(folder, "TRANSCRIPCIONES")
                os.makedirs(folder, exist_ok=True)
            elif "Elegir Otra" in self.trans_dest_var.get() and self._ruta_destino(self.trans_dest_seg):
                folder = self._ruta_destino(self.trans_dest_seg)
            self._registrar_salida(self.trans_dest_seg, folder)

            # Guardar última carpeta usada para el botón 📂
            self.trans_last_folder = folder

            base_name = os.path.splitext(os.path.basename(source_path))[0]
            ext_out   = ".srt" if ".srt" in fmt else (".vtt" if ".vtt" in fmt else ".txt")
            # Nunca sobre un archivo existente (p. ej. los subtítulos .srt que ya traía el video)
            out_path  = _ruta_unica(os.path.join(folder, f"{base_name}{ext_out}"))

            detected_lang = info.language.upper() if info else "??"

            with open(out_path, "w", encoding="utf-8") as f:
                if ".txt" in fmt:
                    f.write(" ".join([seg.text.strip() for seg in full_segments]))
                elif ".srt" in fmt:
                    for idx, seg in enumerate(full_segments):
                        s = self.format_timestamp(seg.start, ',')
                        e = self.format_timestamp(seg.end, ',')
                        f.write(f"{idx+1}\n{s} --> {e}\n{seg.text.strip()}\n\n")
                elif ".vtt" in fmt:
                    f.write("WEBVTT\n\n")
                    for seg in full_segments:
                        s = self.format_timestamp(seg.start, '.')
                        e = self.format_timestamp(seg.end, '.')
                        f.write(f"{s} --> {e}\n{seg.text.strip()}\n\n")

            return True, f"✅ LISTO ({detected_lang})", duration_str

        except InterruptedError:
            print("🚫 Cancelación detectada — modelo conservado en memoria para el siguiente archivo.")
            # NO llamar descargar_modelo_whisper() aquí: en batch el modelo
            # debe quedar listo para el archivo siguiente. El batch lo libera al terminar todo.
            return False, "SALTADO", ""

        except Exception as e:
            print(f"Error Whisper CRÍTICO: {e}")
            self.descargar_modelo_whisper()
            return False, f"❌ {str(e)[:40]}", ""

        finally:
            # NOTA: timer_running NO se toca aquí — el batch lo apaga al terminar todos los archivos.
            # Ya no hay WAV temporal: el audio vivía en memoria y se libera aquí.
            audio = None
            self.current_temp_audio = None
        
    def format_timestamp(self, seconds, decimal_sep):
        """Auxiliar para formato SRT/VTT (HH:MM:SS,ms)"""
        hrs = int(seconds // 3600)
        mins = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        mils = int((seconds - int(seconds)) * 1000)
        return f"{hrs:02}:{mins:02}:{secs:02}{decimal_sep}{mils:03}"
        
    
    # ==========================================================================
    #   SECCIÓN 12: METADATA LAB — Sanitizer, Editor y Analizador
    #   UI y lógica de metadata separadas: la interfaz solo llama al motor
    #   (mlab_*) definido más arriba. No hay lógica de formatos aquí.
    # ==========================================================================
    def init_alpha_module(self):
        self.meta_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.frames["MetadataTool"] = self.meta_frame

        # Variables de lógica
        self.meta_file_path = None
        self.meta_batch_files = []
        self.meta_entries = {}
        self.meta_current_fields = []
        self.meta_cover_pending = None      # None=sin cambios, ""=borrar, ruta=poner
        self.meta_busy = False

        # --- HEADER ---
        top = ctk.CTkFrame(self.meta_frame, fg_color="transparent")
        top.pack(fill="x", padx=20, pady=(10, 5))
        ctk.CTkButton(top, text="← Menú", width=80, fg_color="transparent", border_width=1,
                      command=lambda: self.show_frame("Menu")).pack(side="left")

        title_bg = ctk.CTkFrame(self.meta_frame, fg_color="#2b2b2b", corner_radius=8)
        title_bg.pack(pady=2)
        ctk.CTkLabel(title_bg, text="METADATA LAB | Sanitizer & Editor",
                     font=(self.main_font, 22, "bold"),
                     text_color="#cfcfcf", bg_color="#2b2b2b").pack(padx=15, pady=5)

        # --- CONTENEDOR PRINCIPAL ---
        main_grid = ctk.CTkFrame(self.meta_frame, fg_color="transparent")
        main_grid.pack(fill="both", expand=True, padx=20, pady=5)
        main_grid.grid_columnconfigure(1, weight=1)
        main_grid.grid_rowconfigure(0, weight=1)

        # === PANEL IZQUIERDO (ACCIONES) ===
        sidebar = ctk.CTkFrame(main_grid, width=260, fg_color="#181818", corner_radius=10)
        sidebar.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
        sidebar.pack_propagate(False)

        ctk.CTkLabel(sidebar, text="Panel de Control", font=(self.main_font, 16, "bold"),
                     text_color="#aaa").pack(pady=(15, 5))

        self.btn_meta_select = ctk.CTkButton(sidebar, text="📂 Agregar Archivos", height=40,
                                             fg_color="#333", hover_color="#444", border_width=1,
                                             border_color="#555", command=self.meta_select_file)
        self.btn_meta_select.pack(pady=5, padx=20, fill="x")

        self.btn_meta_reset = ctk.CTkButton(sidebar, text="🧹 Limpiar Cola", height=30,
                                            fg_color="transparent", border_width=1,
                                            border_color="#c0392b", text_color="#e74c3c",
                                            hover_color="#3b1e1e", command=self.meta_clear_all)
        self.btn_meta_reset.pack(pady=(0, 5), padx=20, fill="x")

        self.lbl_meta_info = ctk.CTkLabel(sidebar, text="Arrastra archivos al panel derecho...",
                                          text_color="gray", wraplength=220, justify="center")
        self.lbl_meta_info.pack(pady=10, padx=10)

        self.lbl_meta_error = ctk.CTkLabel(sidebar, text="", text_color="#e67e22",
                                           wraplength=220, font=("Arial", 11, "bold"))
        self.lbl_meta_error.pack(pady=(0, 10), padx=10)

        ctk.CTkFrame(sidebar, height=2, fg_color="#333").pack(fill="x", padx=20, pady=5)

        # --- ACCIONES GLOBALES ---
        edit_actions_frame = ctk.CTkFrame(sidebar, fg_color="transparent")
        edit_actions_frame.pack(fill="x", pady=5)

        self.btn_meta_save = ctk.CTkButton(edit_actions_frame, text="💾 Guardar Cambios", height=40,
                                           fg_color="#27ae60", hover_color="#1e8449",
                                           text_color="white", font=("Arial", 12, "bold"),
                                           state="disabled", command=self.meta_save_logic)
        self.btn_meta_save.pack(pady=(0, 10), padx=20, fill="x")

        self.btn_meta_cancel = ctk.CTkButton(edit_actions_frame, text="🚫 Cancelar / Volver",
                                             height=30, fg_color="transparent", border_width=1,
                                             border_color="#7f8c8d", text_color="#bdc3c7",
                                             hover_color="#444", state="disabled",
                                             command=self.meta_render_file_list)
        self.btn_meta_cancel.pack(pady=(0, 15), padx=20, fill="x")

        self.btn_meta_clean_all = ctk.CTkButton(edit_actions_frame, text="🔥 Sanitizar TODO",
                                                height=40, fg_color="#c0392b", hover_color="#922b21",
                                                text_color="white", font=("Arial", 12, "bold"),
                                                state="disabled", command=self.meta_strip_batch_button)
        self.btn_meta_clean_all.pack(pady=(5, 5), padx=20, fill="x")

        # Barra de Progreso
        self.meta_prog_frame = ctk.CTkFrame(sidebar, fg_color="transparent")
        self.meta_prog_frame.pack(fill="x", padx=20, pady=(10, 0))

        self.meta_status_lbl = ctk.CTkLabel(self.meta_prog_frame, text="Listo",
                                            text_color="gray", font=("Arial", 11))
        self.meta_status_lbl.pack(anchor="w")

        self.meta_prog_bar = ctk.CTkProgressBar(self.meta_prog_frame, height=10,
                                                progress_color="#e67e22")
        self.meta_prog_bar.set(0)
        self.meta_prog_bar.pack(fill="x", pady=(2, 5))

        self.btn_meta_help = ctk.CTkButton(sidebar, text="ℹ Formatos Soportados", height=30,
                                           fg_color="transparent", border_width=1,
                                           border_color="#555", command=self.meta_show_info_window)
        self.btn_meta_help.pack(side="bottom", pady=15, padx=20, fill="x")

        # === PANEL DERECHO ===
        right_panel = ctk.CTkFrame(main_grid, fg_color="transparent")
        right_panel.grid(row=0, column=1, sticky="nsew", padx=(10, 0))
        right_panel.grid_rowconfigure(1, weight=1)
        right_panel.grid_columnconfigure(0, weight=1)

        header_filter = ctk.CTkFrame(right_panel, fg_color="transparent", height=30)
        header_filter.grid(row=0, column=0, sticky="ew", pady=(0, 5))

        ctk.CTkLabel(header_filter, text="Área de Trabajo", font=("Arial", 14, "bold"),
                     text_color="gray").pack(side="left")

        self.meta_sort_var = ctk.StringVar(value="Orden: Llegada")
        self.sort_combo = ctk.CTkOptionMenu(header_filter,
                                            values=["Orden: Llegada", "Orden: Tipo (Extensión)",
                                                    "Orden: Estado (Editables)"],
                                            variable=self.meta_sort_var, width=160, height=25,
                                            fg_color="#333", button_color="#444",
                                            command=self.meta_sort_changed)
        self.sort_combo.pack(side="right")
        ctk.CTkLabel(header_filter, text="Ver por: ", font=("Arial", 12)).pack(side="right", padx=5)

        # A) VISTA LISTA (VIRTUALIZADA)
        self.meta_list_container = ctk.CTkFrame(right_panel, fg_color="#222")
        self.meta_list_container.grid(row=1, column=0, sticky="nsew")

        self.meta_v_scrollbar = ctk.CTkScrollbar(self.meta_list_container,
                                                 command=self.on_meta_virtual_scroll)
        self.meta_v_scrollbar.pack(side="right", fill="y")

        self.meta_canvas = tk.Canvas(self.meta_list_container, bg="#222222",
                                     highlightthickness=0, bd=0)
        self.meta_canvas.pack(side="left", fill="both", expand=True)

        self.meta_empty_id = self.meta_canvas.create_text(
            400, 200,
            text="\n\nCLIC O ARRASTRA ARCHIVOS AQUÍ\n\n(Puedes soltar en toda esta zona gris)",
            fill="#444", font=("Arial", 14, "bold"), justify="center")

        # B) VISTA EDITOR
        self.meta_editor_container = ctk.CTkScrollableFrame(right_panel, fg_color="#222")

        # --- BINDINGS DND y EVENTOS ---
        try:
            for w in [right_panel, self.meta_list_container, self.meta_canvas,
                      self.meta_editor_container]:
                w.drop_target_register(DND_FILES)
                w.dnd_bind('<<Drop>>', self.meta_on_drop)
        except Exception:
            pass

        self.meta_canvas.bind("<Configure>", self.on_meta_resize)
        self.meta_canvas.bind("<MouseWheel>", self.on_meta_mouse_wheel)
        self.meta_canvas.bind("<Button-4>", self.on_meta_mouse_wheel)
        self.meta_canvas.bind("<Button-5>", self.on_meta_mouse_wheel)
        self.meta_canvas.bind("<Button-1>", lambda e: self.check_meta_click_empty(e))

        self.META_ROW_HEIGHT = 50
        self.meta_visible_rows = []
        self.init_meta_row_pool(20)

    # ==========================================================================
    #  MOTOR VIRTUAL METADATA — Canvas-nativo (sin CTkFrames embebidos)
    # ==========================================================================

    _BTN_EDIT_FILL  = "#27ae60"
    _BTN_EDIT_HOV   = "#1e8449"
    _BTN_CLEAN_FILL = "#c0392b"
    _BTN_CLEAN_HOV  = "#922b21"
    _BTN_INFO_FILL  = "#2980b9"
    _BTN_INFO_HOV   = "#1f618d"
    _BTN_DEL_FILL   = "#444444"
    _BTN_DEL_HOV    = "#666666"

    def init_meta_row_pool(self, num_rows):
        """Destruye todo y recrea el pool como items nativos del canvas."""
        self.meta_canvas.delete("all")
        self.meta_visible_rows = []

        w = max(self.meta_canvas.winfo_width(), 400)
        h = max(self.meta_canvas.winfo_height(), 200)
        self.meta_empty_id = self.meta_canvas.create_text(
            w // 2, h // 2,
            text="\n\nCLIC O ARRASTRA ARCHIVOS AQUÍ\n\n(Puedes soltar en toda esta zona gris)",
            fill="#444", font=("Arial", 14, "bold"), justify="center")

        if not self.meta_batch_files:
            return

        self.meta_canvas.itemconfig(self.meta_empty_id, state="hidden")
        for _ in range(num_rows):
            self._meta_add_one_row()

    @staticmethod
    def _rrect_pts(x1, y1, x2, y2, r=4):
        """Puntos de polígono suavizado que simula rectángulo redondeado."""
        return [
            x1+r, y1,   x2-r, y1,
            x2,   y1,   x2,   y1+r,
            x2,   y2-r, x2,   y2,
            x2-r, y2,   x1+r, y2,
            x1,   y2,   x1,   y2-r,
            x1,   y1+r, x1,   y1,
        ]

    def _meta_hover(self, item_btn, *items, fill=None, hover=None):
        """Enlaza hover (cursor + color) de un botón del canvas."""
        c = self.meta_canvas
        for it in items:
            c.tag_bind(it, "<Enter>", lambda e, x=item_btn: (c.configure(cursor="hand2"),
                                                             c.itemconfig(x, fill=hover)))
            c.tag_bind(it, "<Leave>", lambda e, x=item_btn: (c.configure(cursor=""),
                                                             c.itemconfig(x, fill=fill)))

    def _meta_add_one_row(self):
        """Añade UNA fila al pool como items canvas nativos (sin CTkFrame)."""
        c = self.meta_canvas
        Y = -500

        bg  = c.create_rectangle(0, Y, 2000, Y + 48, fill="#2b2b2b", outline="")
        ico = c.create_text(25, Y + 24, text="📝", font=("Segoe UI Emoji", 13), fill="white")
        nam = c.create_text(55, Y + 24, text="", anchor="w", width=0,
                            font=("Arial", 10), fill="#ecf0f1")

        ib = c.create_polygon(self._rrect_pts(0, Y, 0, Y, r=30), smooth=True,
                              fill=self._BTN_INFO_FILL, outline="")
        it = c.create_text(0, Y, text="🔍", font=("Segoe UI Emoji", 10), fill="white")
        eb = c.create_polygon(self._rrect_pts(0, Y, 0, Y, r=30), smooth=True,
                              fill=self._BTN_EDIT_FILL, outline="")
        et = c.create_text(0, Y, text="Editar", font=("Arial", 9, "bold"), fill="white")
        cb = c.create_polygon(self._rrect_pts(0, Y, 0, Y, r=30), smooth=True,
                              fill=self._BTN_CLEAN_FILL, outline="")
        ct = c.create_text(0, Y, text="Limpiar", font=("Arial", 9, "bold"), fill="white")
        db = c.create_polygon(self._rrect_pts(0, Y, 0, Y, r=30), smooth=True,
                              fill=self._BTN_DEL_FILL, outline="")
        dt = c.create_text(0, Y, text="✖", font=("Arial", 9), fill="white")

        self._meta_hover(ib, ib, it, fill=self._BTN_INFO_FILL,  hover=self._BTN_INFO_HOV)
        self._meta_hover(eb, eb, et, fill=self._BTN_EDIT_FILL,  hover=self._BTN_EDIT_HOV)
        self._meta_hover(cb, cb, ct, fill=self._BTN_CLEAN_FILL, hover=self._BTN_CLEAN_HOV)
        self._meta_hover(db, db, dt, fill=self._BTN_DEL_FILL,   hover=self._BTN_DEL_HOV)

        self.meta_visible_rows.append({
            "bg": bg, "ico": ico, "nam": nam,
            "ib": ib, "it": it, "eb": eb, "et": et,
            "cb": cb, "ct": ct, "db": db, "dt": dt,
            "_path": None, "_mode": None, "data_index": -1,
        })

    def render_meta_virtual_rows(self):
        """Reposiciona y actualiza los items canvas. Sin CTkFrames = sin ghosting."""
        if not self.meta_batch_files:
            return

        if not hasattr(self, "_meta_font") or self._meta_font is None:
            self._meta_font = tkfont.Font(family="Arial", size=10)

        c = self.meta_canvas
        canvas_h = c.winfo_height();  canvas_h = canvas_h if canvas_h > 50 else 500
        canvas_w = c.winfo_width();   canvas_w = canvas_w if canvas_w > 50 else 600

        files_to_show = self._get_sorted_meta_files()
        total_pixels = len(files_to_show) * self.META_ROW_HEIGHT

        new_region = (0, 0, canvas_w, total_pixels)
        if getattr(self, "_meta_last_scrollregion", None) != new_region:
            c.configure(scrollregion=new_region)
            self._meta_last_scrollregion = new_region

        try:
            raw_top = c.yview()[0]
        except Exception:
            raw_top = 0.0

        visual_start_idx = int((raw_top * total_pixels) // self.META_ROW_HEIGHT)
        BUFFER = 15
        draw_start_idx = max(0, visual_start_idx - BUFFER)

        rows_needed = int(canvas_h // self.META_ROW_HEIGHT) + (BUFFER * 2) + 2
        while len(self.meta_visible_rows) < rows_needed:
            self._meta_add_one_row()

        MR, IW, BW, DW, PAD, BH, BTN_R = 12, 38, 84, 42, 6, 30, 15

        del_x2 = canvas_w - MR
        del_x1 = del_x2 - DW
        RH = self.META_ROW_HEIGHT

        for i, row in enumerate(self.meta_visible_rows):
            data_idx = draw_start_idx + i

            if not (0 <= data_idx < len(files_to_show)):
                for iid in (row["bg"], row["ico"], row["nam"], row["ib"], row["it"],
                            row["eb"], row["et"], row["cb"], row["ct"], row["db"], row["dt"]):
                    c.itemconfig(iid, state="hidden")
                row["data_index"] = -1
                row["_path"] = None
                row["_mode"] = None
                continue

            item = files_to_show[data_idx]
            path = item["path"]
            can_edit = item.get("editable", False)
            can_clean = item.get("clean", False)
            mode = (can_edit, can_clean)

            y0 = data_idx * RH
            y1 = y0 + RH - 1
            ymid = y0 + RH // 2
            bh0 = ymid - BH // 2
            bh1 = ymid + BH // 2

            bg_col = "#2b2b2b" if data_idx % 2 == 0 else "#333333"
            c.coords(row["bg"], 0, y0, canvas_w, y1)
            c.itemconfig(row["bg"], fill=bg_col, state="normal")

            icon = "📝" if can_edit else ("🛡️" if can_clean else "🔎")
            c.coords(row["ico"], 25, ymid)
            c.itemconfig(row["ico"], text=icon, state="normal")

            # Colocación derecha -> izquierda según los botones visibles
            x = del_x1 - PAD
            if can_clean:
                c.coords(row["cb"], *self._rrect_pts(x - BW, bh0, x, bh1, r=BTN_R))
                c.coords(row["ct"], x - BW // 2, ymid)
                c.itemconfig(row["cb"], state="normal")
                c.itemconfig(row["ct"], state="normal")
                x -= (BW + PAD)
            else:
                c.itemconfig(row["cb"], state="hidden")
                c.itemconfig(row["ct"], state="hidden")
            if can_edit:
                c.coords(row["eb"], *self._rrect_pts(x - BW, bh0, x, bh1, r=BTN_R))
                c.coords(row["et"], x - BW // 2, ymid)
                c.itemconfig(row["eb"], state="normal")
                c.itemconfig(row["et"], state="normal")
                x -= (BW + PAD)
            else:
                c.itemconfig(row["eb"], state="hidden")
                c.itemconfig(row["et"], state="hidden")

            c.coords(row["ib"], *self._rrect_pts(x - IW, bh0, x, bh1, r=BTN_R))
            c.coords(row["it"], x - IW // 2, ymid)
            c.itemconfig(row["ib"], state="normal")
            c.itemconfig(row["it"], state="normal")
            name_max_x = x - IW - 10

            filename = os.path.basename(path)
            max_width = max(60, name_max_x - 55)
            if self._meta_font.measure(filename) > max_width:
                while len(filename) > 0 and self._meta_font.measure(filename + "...") > max_width:
                    filename = filename[:-1]
                filename += "..."
            name_col = "#ecf0f1" if can_edit else ("#bdc3c7" if can_clean else "#888888")
            c.coords(row["nam"], 55, ymid)
            c.itemconfig(row["nam"], text=filename, fill=name_col, state="normal")

            c.coords(row["db"], *self._rrect_pts(del_x1, bh0, del_x2, bh1, r=BTN_R))
            c.coords(row["dt"], (del_x1 + del_x2) // 2, ymid)
            c.itemconfig(row["db"], state="normal")
            c.itemconfig(row["dt"], state="normal")

            if row["_path"] != path or row["_mode"] != mode:
                for iid in (row["ib"], row["it"]):
                    c.tag_unbind(iid, "<Button-1>")
                    c.tag_bind(iid, "<Button-1>", lambda e, p=path: self.meta_analyze_file(p))
                for iid in (row["eb"], row["et"]):
                    c.tag_unbind(iid, "<Button-1>")
                    if can_edit:
                        c.tag_bind(iid, "<Button-1>",
                                   lambda e, p=path: self.meta_load_single_editor(p))
                for iid in (row["cb"], row["ct"]):
                    c.tag_unbind(iid, "<Button-1>")
                    if can_clean:
                        c.tag_bind(iid, "<Button-1>", lambda e, p=path: self.meta_strip_single(p))
                for iid in (row["db"], row["dt"]):
                    c.tag_unbind(iid, "<Button-1>")
                    c.tag_bind(iid, "<Button-1>", lambda e, p=path: self.meta_remove_from_queue(p))
                c.tag_unbind(row["nam"], "<Button-1>")
                if can_edit:
                    c.tag_bind(row["nam"], "<Button-1>",
                               lambda e, p=path: self.meta_load_single_editor(p))
                else:
                    c.tag_bind(row["nam"], "<Button-1>",
                               lambda e, p=path: self.meta_analyze_file(p))
                row["_path"] = path
                row["_mode"] = mode

            row["data_index"] = data_idx

    def _get_sorted_meta_files(self):
        """Helper para obtener la lista ordenada sin modificar la original."""
        sort_val = getattr(self, "meta_sort_var", None)
        sort_mode = sort_val.get() if sort_val else "Orden: Llegada"

        files = list(self.meta_batch_files)
        if sort_mode == "Orden: Tipo (Extensión)":
            files.sort(key=lambda x: (os.path.splitext(x["path"])[1].lower(),
                                      os.path.basename(x["path"])))
        elif sort_mode == "Orden: Estado (Editables)":
            files.sort(key=lambda x: (not x.get("editable", False),
                                      os.path.basename(x["path"])))
        return files

    def on_meta_virtual_scroll(self, *args):
        self.meta_canvas.yview(*args)
        self.render_meta_virtual_rows()

    def on_meta_mouse_wheel(self, event):
        if not self.meta_batch_files:
            return
        delta = -1 if (getattr(event, "delta", 0) > 0 or getattr(event, "num", 0) == 4) else 1
        self.meta_canvas.yview_scroll(delta, "units")
        self.render_meta_virtual_rows()

    def _meta_delayed_render(self):
        self.render_meta_virtual_rows()

    def on_meta_resize(self, event):
        if not self.meta_batch_files:
            try:
                self.meta_canvas.coords(self.meta_empty_id, event.width // 2, event.height // 2)
            except Exception:
                pass
            return
        if getattr(self, "_meta_resize_job", None):
            try:
                self.after_cancel(self._meta_resize_job)
            except Exception:
                pass
        self._meta_resize_job = self.after(60, self._meta_delayed_render)

    def check_meta_click_empty(self, event):
        if not self.meta_batch_files:
            self.meta_select_file()

    # ==========================================================================
    #   COLA DE ARCHIVOS
    # ==========================================================================

    def meta_handle_input_files(self, file_list):
        """Procesa archivos entrantes sin popups, agregando a la cola existente."""
        added_count = 0
        invalid_count = 0
        current_paths = [f["path"] for f in self.meta_batch_files] if self.meta_batch_files else []

        for f in file_list:
            f = f.strip('"')
            if not os.path.isfile(f):
                continue
            caps = mlab_caps(f)
            if not caps["kind"]:
                invalid_count += 1
                continue
            if f in current_paths:
                continue
            self.meta_batch_files.append({
                "path": f,
                "editable": caps["edit"],
                "clean": caps["clean"],
                "label": caps["label"],
            })
            added_count += 1

        if invalid_count > 0:
            self.lbl_meta_error.configure(text=f"⚠ Se ignoraron {invalid_count} archivos\nno soportados.")
        else:
            self.lbl_meta_error.configure(text="")

        if added_count > 0:
            self.meta_render_file_list()
        elif not self.meta_batch_files:
            self.lbl_meta_info.configure(text="No se cargaron archivos válidos.")

    def meta_sort_changed(self, choice):
        self.meta_render_file_list()

    def meta_render_file_list(self):
        """Activa la vista de lista virtual y actualiza."""
        self.meta_editor_container.grid_forget()
        self.meta_list_container.grid(row=1, column=0, sticky="nsew")

        self.btn_meta_save.configure(state="disabled", text="💾 Guardar Cambios")
        self.btn_meta_cancel.configure(state="disabled")
        self.meta_file_path = None
        self.meta_entries = {}
        self.meta_current_fields = []
        self.meta_cover_pending = None

        count = len(self.meta_batch_files)

        if count == 0:
            self.meta_canvas.delete("all")
            self.meta_visible_rows = []
            self._meta_last_scrollregion = None
            self.meta_empty_id = self.meta_canvas.create_text(
                int(self.meta_canvas.winfo_width() / 2), 200,
                text="\n\nCLIC O ARRASTRA ARCHIVOS AQUÍ\n\n(Puedes soltar en toda esta zona gris)",
                fill="#444", font=("Arial", 14, "bold"), justify="center")
            self.lbl_meta_info.configure(text="Esperando archivos...")
            self.btn_meta_clean_all.configure(state="disabled", text="🔥 Sanitizar TODO")
            return

        try:
            self.meta_canvas.itemconfig(self.meta_empty_id, state="hidden")
        except Exception:
            pass

        limpiables = sum(1 for f in self.meta_batch_files if f.get("clean"))
        if limpiables:
            self.btn_meta_clean_all.configure(state="normal",
                                              text=f"🔥 Sanitizar {limpiables} Archivos")
        else:
            self.btn_meta_clean_all.configure(state="disabled", text="🔥 Sanitizar TODO")

        sort_mode = self.meta_sort_var.get()
        solo_analisis = count - limpiables
        extra = f"\n({solo_analisis} solo analizables)" if solo_analisis else ""
        self.lbl_meta_info.configure(text=f"Lista: {count} archivos.\n({sort_mode}){extra}")

        self.render_meta_virtual_rows()

    def meta_clear_all(self):
        """Limpia toda la cola"""
        self.meta_batch_files = []
        self.meta_file_path = None
        self.lbl_meta_error.configure(text="")
        self.meta_render_file_list()

    def meta_remove_from_queue(self, path_to_remove):
        """Quita un archivo de la lista (porque se procesó o el usuario lo borró)"""
        self.meta_batch_files = [f for f in self.meta_batch_files if f["path"] != path_to_remove]
        if self.meta_file_path == path_to_remove:
            self.meta_file_path = None
        self.meta_render_file_list()

    def meta_on_drop(self, event):
        self.meta_handle_input_files(self._rutas_drop(event))

    def meta_select_file(self):
        exts = " ".join(sorted("*" + e for e in MLAB_VALID_EXT))
        filetypes = (
            ("Todos los soportados", exts),
            ("Imágenes", "*.jpg *.jpeg *.png *.webp *.tif *.tiff *.heic *.cr2 *.nef *.dng"),
            ("Audio", "*.mp3 *.flac *.wav *.m4a *.aac *.ogg *.opus"),
            ("Video", "*.mp4 *.mov *.mkv *.webm *.avi *.wmv"),
            ("Documentos Office", "*.docx *.xlsx *.xlsm *.pptx *.ppsx"),
            ("Documentos PDF", "*.pdf"),
        )
        files = filedialog.askopenfilenames(filetypes=filetypes)
        if files:
            self.meta_handle_input_files(list(files))

    def get_file_size_mb(self, path):
        try:
            return round(os.path.getsize(path) / (1024 * 1024), 2)
        except Exception:
            return 0

    def _meta_set_busy(self, busy, status=None):
        """Bloquea/desbloquea la UI durante una operación en segundo plano."""
        self.meta_busy = busy
        state = "disabled" if busy else "normal"
        for attr in ("btn_meta_select", "btn_meta_reset", "btn_meta_clean_all", "btn_meta_help"):
            try:
                w = getattr(self, attr, None)
                if w is not None:
                    w.configure(state=state)
            except Exception:
                pass
        try:
            self.configure(cursor="watch" if busy else "")
        except Exception:
            pass
        if status is not None:
            self._update_meta_progress(status, 0 if busy else 0)
        if not busy:
            self.meta_render_file_list()

    def _update_meta_progress(self, text, value):
        """Actualiza solo la barra y el texto, super ligero."""
        try:
            self.meta_status_lbl.configure(text=text, text_color="#3498db")
            self.meta_prog_bar.set(value)
        except Exception:
            pass

    # ==========================================================================
    #   ANALIZAR (solo lectura, no toca el archivo)
    # ==========================================================================

    def meta_analyze_file(self, path):
        if not os.path.isfile(path):
            messagebox.showwarning("Analizar", "El archivo ya no existe.")
            return
        try:
            rep = mlab_analyze(path)
        except Exception as e:
            messagebox.showerror("Analizar", f"No se pudo analizar el archivo:\n{e}")
            return

        win = self._ventana_nueva("Informe de metadatos", 560, 620, fg_color="#1a1a1a")

        ctk.CTkLabel(win, text="METADATA REPORT", font=(self.main_font, 20, "bold"),
                     text_color="white").pack(pady=(15, 2))
        ctk.CTkLabel(win, text=rep["name"], font=("Arial", 12), text_color="#aaa",
                     wraplength=500).pack(pady=(0, 8))

        body = ctk.CTkScrollableFrame(win, fg_color="#222")
        body.pack(fill="both", expand=True, padx=15, pady=5)

        caps = rep["caps"]
        head = ctk.CTkFrame(body, fg_color="#2b2b2b", corner_radius=8)
        head.pack(fill="x", pady=(5, 10))
        resumen = (f"Tipo: {rep['label']}      Tamaño: {rep['size_mb']} MB\n"
                   f"Campos detectados: {len(rep['fields'])}      "
                   f"Sensibles: {len(rep['sensitive'])}\n"
                   f"Editar: {'sí' if caps['edit'] else 'no'}      "
                   f"Sanitizar: {'sí' if caps['clean'] else 'no'}")
        ctk.CTkLabel(head, text=resumen, font=("Arial", 12), justify="left",
                     text_color="#ddd").pack(padx=12, pady=10, anchor="w")

        if rep["error"]:
            ctk.CTkLabel(body, text=f"⚠ {rep['error']}", text_color="#e67e22",
                         wraplength=480, justify="left").pack(anchor="w", padx=10, pady=5)

        if rep["sensitive"]:
            box = ctk.CTkFrame(body, fg_color="#2b1d1d", corner_radius=8,
                               border_width=1, border_color="#c0392b")
            box.pack(fill="x", pady=(0, 10))
            ctk.CTkLabel(box, text="⚠ INFORMACIÓN SENSIBLE", font=("Arial", 13, "bold"),
                         text_color="#e74c3c").pack(anchor="w", padx=12, pady=(8, 2))
            for f in rep["sensitive"]:
                ctk.CTkLabel(box, text=f"• {f['label']}: {f['value'][:70]}",
                             font=("Arial", 11), text_color="#f5b7b1",
                             wraplength=470, justify="left").pack(anchor="w", padx=20)
            ctk.CTkLabel(box, text="", height=6).pack()

        if rep["fields"]:
            grupos = {}
            for f in rep["fields"]:
                grupos.setdefault(f["group"], []).append(f)
            for grupo, campos in grupos.items():
                ctk.CTkLabel(body, text=grupo.upper(), font=("Arial", 11, "bold"),
                             text_color="#3498db").pack(anchor="w", padx=10, pady=(8, 2))
                for f in campos:
                    row = ctk.CTkFrame(body, fg_color="transparent")
                    row.pack(fill="x", padx=10)
                    ctk.CTkLabel(row, text=f["label"], width=160, anchor="w",
                                 font=("Arial", 11), text_color="#aaa").pack(side="left")
                    ctk.CTkLabel(row, text=f["value"][:90], anchor="w", font=("Arial", 11),
                                 text_color="#ecf0f1", wraplength=300,
                                 justify="left").pack(side="left", fill="x", expand=True)
        else:
            ctk.CTkLabel(body, text="✓ Este archivo no contiene metadatos detectables.",
                         font=("Arial", 13), text_color="#2ecc71").pack(pady=30)

        ctk.CTkButton(win, text="Cerrar", width=120, height=35, fg_color="#444",
                      hover_color="#555", command=win.destroy).pack(pady=12)
        self._ventana_mostrar(win, recentrar=False)

    # ==========================================================================
    #   EDITOR
    # ==========================================================================

    def meta_load_single_editor(self, path):
        """Cambia a la vista de Editor (Scrollable Frame)."""
        if not os.path.isfile(path):
            messagebox.showwarning("Editar", "El archivo ya no existe.")
            self.meta_remove_from_queue(path)
            return

        self.meta_list_container.grid_forget()
        self.meta_editor_container.grid(row=1, column=0, sticky="nsew")

        self.meta_file_path = path
        self.meta_entries = {}
        self.meta_cover_pending = None
        name = os.path.basename(path)
        display_name = (name[:55] + '...') if len(name) > 65 else name

        self.lbl_meta_info.configure(
            text=f"EDITANDO:\n{name[:20]}\n...\n\n{self.get_file_size_mb(path)} MB")

        for widget in self.meta_editor_container.winfo_children():
            widget.destroy()

        head = ctk.CTkFrame(self.meta_editor_container, fg_color="transparent")
        head.pack(fill="x", pady=10)
        ctk.CTkLabel(head, text=f"Editando: {display_name}", font=("Arial", 13, "bold"),
                     text_color="#2ecc71", anchor="w").pack(side="left", padx=10, fill="x")

        self.btn_meta_save.configure(state="normal", text="💾 Guardar Cambios")
        self.btn_meta_cancel.configure(state="normal")
        self.btn_meta_clean_all.configure(state="disabled")

        self.meta_load_fields(path)

    def meta_load_fields(self, path):
        """Muestra SOLO los campos que ya tienen datos, agrupados y marcando
        los sensibles. Si no hay ninguno, se ofrece añadirlos a mano."""
        caps = mlab_caps(path)
        res = mlab_read(path)
        self.meta_current_fields = res.get("fields", [])

        if res.get("error"):
            self.meta_show_message(f"No se pudo leer la metadata:\n{res['error']}")
            self.btn_meta_save.configure(state="disabled")
            return

        editables = [f for f in self.meta_current_fields if f["type"] != "readonly"]
        solo_lectura = [f for f in self.meta_current_fields if f["type"] == "readonly"]

        if caps["copy"]:
            aviso = ctk.CTkFrame(self.meta_editor_container, fg_color="#2b2b1d",
                                 corner_radius=8, border_width=1, border_color="#b7950b")
            aviso.pack(fill="x", padx=10, pady=(0, 10))
            ctk.CTkLabel(aviso, text="ℹ Al guardar se creará una copia «_editado» con stream "
                                     "copy.\nEl video original no se modifica ni se recodifica.",
                         font=("Arial", 11), text_color="#f4d03f", justify="left",
                         wraplength=520).pack(padx=12, pady=8, anchor="w")

        sensibles = [f for f in self.meta_current_fields if f["sensitive"]]
        if sensibles:
            box = ctk.CTkFrame(self.meta_editor_container, fg_color="#2b1d1d",
                               corner_radius=8, border_width=1, border_color="#c0392b")
            box.pack(fill="x", padx=10, pady=(0, 10))
            ctk.CTkLabel(box, text="⚠ INFORMACIÓN SENSIBLE", font=("Arial", 12, "bold"),
                         text_color="#e74c3c").pack(anchor="w", padx=12, pady=(8, 2))
            ctk.CTkLabel(box, text=" · ".join(f["label"] for f in sensibles),
                         font=("Arial", 11), text_color="#f5b7b1", wraplength=500,
                         justify="left").pack(anchor="w", padx=20, pady=(0, 8))

        if not self.meta_current_fields:
            ctk.CTkLabel(self.meta_editor_container,
                         text="Este archivo no contiene metadatos editables.",
                         font=("Arial", 13), text_color="#2ecc71").pack(pady=(25, 5))
            ctk.CTkLabel(self.meta_editor_container,
                         text="Puedes añadir campos manualmente si lo necesitas.",
                         font=("Arial", 11), text_color="gray").pack(pady=(0, 15))
        else:
            grupos = {}
            for f in editables:
                grupos.setdefault(f["group"], []).append(f)
            for grupo, campos in grupos.items():
                ctk.CTkLabel(self.meta_editor_container, text=grupo.upper(),
                             font=("Arial", 11, "bold"), text_color="#3498db").pack(
                                 anchor="w", padx=12, pady=(10, 2))
                for f in campos:
                    self.meta_add_entry_row(f["label"], f["value"], f["key"],
                                            sensitive=f["sensitive"], ftype=f["type"])
            if solo_lectura:
                ctk.CTkLabel(self.meta_editor_container, text="SOLO LECTURA",
                             font=("Arial", 11, "bold"), text_color="#7f8c8d").pack(
                                 anchor="w", padx=12, pady=(12, 2))
                for f in solo_lectura:
                    row = ctk.CTkFrame(self.meta_editor_container, fg_color="transparent")
                    row.pack(fill="x", pady=2)
                    ctk.CTkLabel(row, text=f["label"], width=150, anchor="w",
                                 text_color="#888").pack(side="left", padx=5)
                    ctk.CTkLabel(row, text=f["value"][:80], anchor="w", text_color="#777",
                                 wraplength=330, justify="left").pack(side="left",
                                                                      fill="x", expand=True)

        if caps["kind"] == "audio":
            self._meta_build_cover_section(path)

        # --- PIE: añadir campo / guardar / volver ---
        ctk.CTkFrame(self.meta_editor_container, height=2, fg_color="#333").pack(
            fill="x", pady=(20, 10))

        if mlab_addable_fields(path):
            ctk.CTkButton(self.meta_editor_container, text="➕ Añadir campo", height=32,
                          fg_color="transparent", border_width=1, border_color="#3498db",
                          text_color="#3498db", hover_color="#1b2a38",
                          command=lambda p=path: self._meta_add_field_dialog(p)).pack(
                              padx=10, pady=(0, 10), anchor="w")

        foot_frame = ctk.CTkFrame(self.meta_editor_container, fg_color="transparent")
        foot_frame.pack(fill="x", pady=(0, 20))
        ctk.CTkButton(foot_frame, text="💾 Guardar Cambios", height=40,
                      fg_color="#27ae60", hover_color="#1e8449", font=("Arial", 12, "bold"),
                      command=self.meta_save_logic).pack(side="left", fill="x",
                                                         expand=True, padx=(0, 5))
        ctk.CTkButton(foot_frame, text="🔙 Volver a la Lista", height=40,
                      fg_color="#333", hover_color="#444", border_width=1, border_color="#555",
                      command=self.meta_render_file_list).pack(side="right", fill="x",
                                                               expand=True, padx=(5, 0))

    def meta_add_entry_row(self, label_text, value, tag_id, sensitive=False, ftype="text"):
        """Agrega una fila editable al editor."""
        row = ctk.CTkFrame(self.meta_editor_container, fg_color="transparent")
        row.pack(fill="x", pady=2)

        txt = ("⚠ " if sensitive else "") + str(label_text)
        ctk.CTkLabel(row, text=txt, width=150, anchor="w",
                     text_color="#e59866" if sensitive else "#ccc").pack(side="left", padx=5)

        entry = ctk.CTkEntry(row, height=28, fg_color="#333", border_color="#555")
        entry.insert(0, str(value) if value else "")
        entry.pack(side="left", fill="x", expand=True, padx=5)

        if ftype == "gps":
            ctk.CTkLabel(row, text="lat, lon", width=55, text_color="#666",
                         font=("Arial", 10)).pack(side="left")
        elif ftype == "date":
            ctk.CTkLabel(row, text="fecha", width=55, text_color="#666",
                         font=("Arial", 10)).pack(side="left")

        self.meta_entries[tag_id] = entry
        return entry

    def _meta_add_field_dialog(self, path):
        """Ventana para añadir un campo que todavía no existe en el archivo."""
        disponibles = mlab_addable_fields(path)
        if not disponibles:
            messagebox.showinfo("Añadir campo", "Ya están todos los campos disponibles.")
            return

        win = self._ventana_nueva("Añadir campo", 330, 430)

        ctk.CTkLabel(win, text="Selecciona el campo a añadir",
                     font=("Arial", 13, "bold")).pack(pady=(15, 8))
        box = ctk.CTkScrollableFrame(win, fg_color="#222")
        box.pack(fill="both", expand=True, padx=15, pady=5)

        def _add(key, label, ftype, sens):
            win.destroy()
            if key in self.meta_entries:
                return
            e = self.meta_add_entry_row(label, "", key, sensitive=sens, ftype=ftype)
            try:
                e.focus_set()
            except Exception:
                pass

        for key, label, ftype, group, sens in disponibles:
            ctk.CTkButton(box, text=f"{label}", height=30, anchor="w",
                          fg_color="#2b2b2b", hover_color="#3b3b3b",
                          command=lambda k=key, l=label, t=ftype, s=sens: _add(k, l, t, s)).pack(
                              fill="x", pady=2, padx=5)

        ctk.CTkButton(win, text="Cancelar", width=110, fg_color="#444", hover_color="#555",
                      command=win.destroy).pack(pady=10)
        self._ventana_mostrar(win, recentrar=False)

    def _meta_build_cover_section(self, path):
        """Carátula de audio: ver, cambiar o eliminar. Es metadata, no audio."""
        cover = None
        try:
            cover = _audio_cover(path)
        except Exception:
            cover = None

        cont = ctk.CTkFrame(self.meta_editor_container, fg_color="#2b2b2b", corner_radius=8)
        cont.pack(fill="x", padx=10, pady=(15, 5))
        ctk.CTkLabel(cont, text="CARÁTULA", font=("Arial", 11, "bold"),
                     text_color="#3498db").pack(anchor="w", padx=12, pady=(8, 4))

        inner = ctk.CTkFrame(cont, fg_color="transparent")
        inner.pack(fill="x", padx=12, pady=(0, 10))

        self._meta_cover_lbl = ctk.CTkLabel(inner, text="", width=96, height=96)
        self._meta_cover_lbl.pack(side="left", padx=(0, 12))

        def _pintar(data):
            if data:
                try:
                    img = Image.open(io.BytesIO(data))
                    img.thumbnail((96, 96))
                    self._meta_cover_img = CTkImage(light_image=img, dark_image=img,
                                                    size=img.size)
                    self._meta_cover_lbl.configure(image=self._meta_cover_img, text="")
                    return
                except Exception:
                    pass
            self._meta_cover_lbl.configure(image=None, text="sin\ncarátula",
                                           text_color="#666", font=("Arial", 11))

        _pintar(cover[1] if cover else None)

        btns = ctk.CTkFrame(inner, fg_color="transparent")
        btns.pack(side="left", fill="x", expand=True)

        def _cambiar():
            f = filedialog.askopenfilename(filetypes=(("Imágenes", "*.jpg *.jpeg *.png"),))
            if not f:
                return
            self.meta_cover_pending = f
            try:
                with open(f, "rb") as fh:
                    _pintar(fh.read())
            except Exception:
                pass

        def _quitar():
            self.meta_cover_pending = ""
            _pintar(None)

        ctk.CTkButton(btns, text="Cambiar", height=30, width=110, fg_color="#333",
                      hover_color="#444", border_width=1, border_color="#555",
                      command=_cambiar).pack(anchor="w", pady=2)
        ctk.CTkButton(btns, text="Eliminar", height=30, width=110, fg_color="transparent",
                      hover_color="#3b1e1e", border_width=1, border_color="#c0392b",
                      text_color="#e74c3c", command=_quitar).pack(anchor="w", pady=2)

    def meta_show_message(self, msg):
        """Mensaje de bloqueo con botón de retorno centrado."""
        container = ctk.CTkFrame(self.meta_editor_container, fg_color="transparent")
        container.pack(fill="both", expand=True, pady=40)
        ctk.CTkLabel(container, text=msg, font=("Arial", 12), text_color="gray",
                     wraplength=420, justify="center").pack(pady=10)
        ctk.CTkButton(container, text="🔙 Volver a la Lista", height=35, width=140,
                      fg_color="#333", hover_color="#444", border_width=1, border_color="#555",
                      command=self.meta_render_file_list).pack(pady=10)

    def meta_save_logic(self):
        """Guarda los campos editados. En video genera *_editado."""
        if not self.meta_file_path or self.meta_busy:
            return
        path = self.meta_file_path
        values = {}
        for key, widget in self.meta_entries.items():
            try:
                values[key] = widget.get()
            except Exception:
                continue
        cover_pending = self.meta_cover_pending

        if not values and cover_pending is None:
            messagebox.showinfo("Guardar", "No hay campos que guardar.")
            return

        self._meta_set_busy(True, "Guardando metadata...")
        self.btn_meta_save.configure(state="disabled")

        def _worker():
            ok, err, out = True, None, path
            try:
                if values:
                    ok, err, out = mlab_write(path, values)
                if ok and cover_pending is not None:
                    _audio_set_cover(out or path, cover_pending or None)
            except Exception as e:
                ok, err = False, str(e)

            def _done():
                self._meta_set_busy(False, "Listo")
                if not ok:
                    messagebox.showerror("Error guardando",
                                         f"{os.path.basename(path)}\n\n{err}")
                    return
                if out and out != path:
                    messagebox.showinfo("Guardado",
                                        "Se creó una copia con la metadata nueva:\n\n"
                                        f"{os.path.basename(out)}\n\n"
                                        "El archivo original no se modificó.")
                else:
                    messagebox.showinfo("Guardado", "Metadatos actualizados correctamente.")
                self.meta_remove_from_queue(path)

            self.after(0, _done)

        threading.Thread(target=_worker, daemon=True).start()

    # ==========================================================================
    #   SANITIZAR
    # ==========================================================================

    def meta_strip_single(self, path):
        """Sanitiza un archivo: crea *_CLEAN, verifica y reporta."""
        if self.meta_busy:
            return
        if not os.path.isfile(path):
            messagebox.showwarning("Sanitizar", "El archivo ya no existe.")
            self.meta_remove_from_queue(path)
            return

        self._meta_set_busy(True, f"Sanitizando {os.path.basename(path)[:18]}...")
        self._update_meta_progress("Sanitizando...", 0.35)

        def _worker():
            res = mlab_sanitize(path)

            def _done():
                self._meta_set_busy(False, "Listo")
                self._update_meta_progress("Listo", 0)
                if not res["ok"]:
                    messagebox.showwarning("No se pudo sanitizar",
                                           f"{os.path.basename(path)}\n\n{res['error']}")
                    return
                extra = ""
                if res["residual"]:
                    extra = ("\n\n⚠ Quedó metadata no eliminable:\n" +
                             ", ".join(res["residual"]))
                messagebox.showinfo(
                    "Sanitizado",
                    f"Se creó: {os.path.basename(res['dst'])}\n\n"
                    f"Verificación: {res['verify']}\n"
                    f"Metadata restante: {len(res['residual'])}{extra}")
                self.meta_remove_from_queue(path)

            self.after(0, _done)

        threading.Thread(target=_worker, daemon=True).start()

    def meta_strip_batch_button(self):
        """Sanitiza toda la cola (omite los formatos de solo análisis)."""
        if self.meta_busy:
            return
        if not getattr(self, "meta_batch_files", None):
            messagebox.showinfo("Sanitizar", "No hay archivos en la cola de Metadata.")
            return

        paths = [f["path"] for f in self.meta_batch_files
                 if f.get("clean") and os.path.isfile(f["path"])]
        omitidos = len(self.meta_batch_files) - len(paths)

        if not paths:
            messagebox.showinfo("Sanitizar",
                                "Ninguno de los archivos de la cola se puede sanitizar.")
            return

        msg = (f"Se crearán {len(paths)} copias '_CLEAN' sin metadatos.\n"
               "Los originales no se modifican.")
        if omitidos:
            msg += f"\n\nSe omitirán {omitidos} archivo(s) de solo análisis."
        if not messagebox.askyesno("Confirmar Sanitización", msg + "\n\n¿Continuar?"):
            return

        self._meta_set_busy(True, "Iniciando...")
        self.meta_strip_batch_all(paths)

    def meta_strip_batch_all(self, paths):
        """Procesa en segundo plano sin redibujar la lista en cada paso."""
        if not paths:
            return
        results = []

        def _worker():
            total = len(paths)
            for i, p in enumerate(paths):
                short = os.path.basename(p)
                if len(short) > 20:
                    short = short[:17] + "..."
                self.after(0, lambda t=f"Procesando {i+1}/{total}: {short}",
                           prog=(i / total): self._update_meta_progress(t, prog))
                try:
                    res = mlab_sanitize(p)
                    results.append((p, res["ok"], res.get("error"), res.get("residual", [])))
                except Exception as e:
                    results.append((p, False, f"Excepción: {e}", []))

            self.after(0, lambda: self._update_meta_progress("Finalizando...", 1.0))
            self.after(300, lambda: self._on_batch_complete(results))

        threading.Thread(target=_worker, daemon=True).start()

    def _on_batch_complete(self, results):
        """Reporte final y limpieza de la cola en una sola pasada."""
        try:
            total = len(results)
            ok_count = sum(1 for r in results if r[1])
            failed = [(os.path.basename(r[0]), r[2]) for r in results if not r[1]]
            con_restos = [os.path.basename(r[0]) for r in results if r[1] and r[3]]

            procesados = {r[0] for r in results if r[1]}
            self.meta_batch_files = [f for f in self.meta_batch_files
                                     if f["path"] not in procesados]

            if not failed:
                msg = f"✅ Se limpiaron los {total} archivos correctamente."
                if con_restos:
                    msg += ("\n\n⚠ Con metadata no eliminable:\n" +
                            ", ".join(con_restos[:5]))
                messagebox.showinfo("Sanitización Completa", msg)
            else:
                msg = f"{ok_count}/{total} archivos limpiados.\n\nErrores ({len(failed)}):\n"
                for name, err in failed[:5]:
                    msg += f"- {name}: {str(err)[:120]}\n"
                if len(failed) > 5:
                    msg += "... y más."
                messagebox.showwarning("Proceso con errores", msg)
        except Exception as e:
            print(f"Error en _on_batch_complete: {e}")
        finally:
            self._meta_set_busy(False, "Listo")
            self._update_meta_progress("Listo", 0)

    # ==========================================================================
    #   VENTANA DE FORMATOS SOPORTADOS
    # ==========================================================================

    def meta_show_info_window(self, mostrar=True):
        """Ventana de ayuda visual estilo tarjetas."""
        if mostrar and self._ventana_reusar(self.toplevel_meta_info):
            return
        if not mostrar and self.toplevel_meta_info is not None:
            return

        win = self._ventana_nueva("Capacidades Metadata Lab", 560, 700, fg_color="#1a1a2e",
                                  redimensionable=(False, False), reutilizable=True)
        self.toplevel_meta_info = win

        ctk.CTkLabel(win, text="Formatos Soportados", font=(self.main_font, 24, "bold"),
                     text_color="white").pack(pady=(18, 2))
        ctk.CTkLabel(win, text="Edición y sanitización sin recodificar",
                     font=("Arial", 13), text_color="#aaa").pack(pady=(0, 5))

        container = ctk.CTkScrollableFrame(win, fg_color="transparent")
        container.pack(expand=True, fill="both", padx=18, pady=8)
        container.grid_columnconfigure((0, 1), weight=1)

        def create_card(row, col, title, color, formats, can_edit, can_clean, nota=""):
            card = ctk.CTkFrame(container, fg_color="#252525", corner_radius=12,
                                border_width=2, border_color=color)
            card.grid(row=row, column=col, padx=8, pady=8, sticky="nsew")

            head = ctk.CTkFrame(card, fg_color=color, height=32, corner_radius=8)
            head.pack(fill="x", padx=5, pady=5)
            ctk.CTkLabel(head, text=title, font=("Arial", 13, "bold"),
                         text_color="white").pack(pady=4)

            content = ctk.CTkFrame(card, fg_color="transparent")
            content.pack(fill="both", expand=True, padx=10, pady=5)
            ctk.CTkLabel(content, text=formats, font=("Arial", 11, "bold"),
                         text_color="#ddd", wraplength=210).pack(pady=0)
            ctk.CTkFrame(content, height=1, fg_color="#444").pack(fill="x", pady=5)

            for etiqueta, valor in (("Editar campos:", can_edit), ("Sanitizar:", can_clean)):
                r = ctk.CTkFrame(content, fg_color="transparent")
                r.pack(fill="x", pady=1)
                ctk.CTkLabel(r, text=etiqueta, font=("Arial", 11),
                             text_color="#aaa").pack(side="left")
                ctk.CTkLabel(r, text="✅ SÍ" if valor else "❌ NO", font=("Arial", 11, "bold"),
                             text_color="#2ecc71" if valor else "#e74c3c").pack(side="right")
            if nota:
                ctk.CTkLabel(content, text=nota, font=("Arial", 10), text_color="#888",
                             wraplength=210, justify="left").pack(pady=(4, 6))

        create_card(0, 0, "📸 IMÁGENES", "#3498db", "JPG · PNG · TIFF", True, True,
                    "Se eliminan los segmentos EXIF/XMP/IPTC sin recomprimir la imagen.")
        create_card(0, 1, "🖼 WEBP", "#5dade2", "WEBP", False, True,
                    "Sanitización por contenedor. Sin edición manual.")
        create_card(1, 0, "🎵 AUDIO", "#27ae60", "MP3 · FLAC · M4A · OGG · OPUS · WAV", True, True,
                    "Incluye carátula (ver, cambiar, eliminar). AAC: solo sanitizar.")
        create_card(1, 1, "🎬 VIDEO", "#8e44ad", "MP4 · M4V · MOV · MKV · WEBM", True, True,
                    "Remux con stream copy. Al editar se crea una copia «_editado».")
        create_card(2, 0, "📄 OFFICE", "#e67e22", "DOCX · XLSX · XLSM · PPTX · PPSX", True, True,
                    "Se edita el paquete directamente: no se pierden fórmulas, gráficos ni macros.")
        create_card(2, 1, "📕 PDF", "#c0392b", "PDF", True, True,
                    "Elimina el diccionario Info y el bloque XMP.")
        create_card(3, 0, "📼 OTROS VIDEOS", "#7f8c8d", "AVI · WMV · FLV", False, True,
                    "Sanitización sí; sus tags no se escriben de forma fiable.")
        create_card(3, 1, "🔎 SOLO ANALIZAR", "#95a5a6", "CR2 · CR3 · NEF · ARW · DNG · HEIC",
                    False, False,
                    "Lectura sin riesgo. Modificarlos podría inutilizar el archivo.")

        nota = ctk.CTkFrame(win, fg_color="#252525", corner_radius=10)
        nota.pack(fill="x", padx=18, pady=(0, 8))
        ctk.CTkLabel(nota, text="Sanitizar crea siempre una copia «_CLEAN» y verifica el "
                                "resultado antes de darlo por bueno.\nEl archivo original "
                                "nunca se modifica.",
                     font=("Arial", 11), text_color="#aaa", justify="left").pack(padx=12, pady=8)

        ctk.CTkButton(win, text="Entendido", width=120, height=35, fg_color="#444",
                      hover_color="#555", command=lambda: self._ventana_ocultar(win)).pack(pady=(0, 12))

        if mostrar:
            self._ventana_mostrar(win)
    # ==========================================================================
    #   SECCIÓN 13: MÓDULO YOUTUBE PRO (CORREGIDO FINAL)
    # ==========================================================================

    def init_youtube_module(self):
        self.yt_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.frames["YouTubeTool"] = self.yt_frame
        
        c_yt = "#FF0000"
        c_hover = "#cc0000"
        self.yt_downloads = {}
        # Cola de descargas: máximo YT_MAX_DESCARGAS bajando a la vez, en orden
        # de llegada (ver _yt_tomar_turno / _yt_soltar_turno)
        self._yt_cola_cond = threading.Condition()
        self._yt_cola_espera = []       # turnos esperando, en orden
        self._yt_cola_activos = set()   # turnos que están bajando ahora

        # HEADER
        top = ctk.CTkFrame(self.yt_frame, fg_color="transparent")
        top.pack(fill="x", padx=20, pady=10)
        ctk.CTkButton(top, text="← Menú", width=80, fg_color="transparent", border_width=1, 
                      command=lambda: self.show_frame("Menu")).pack(side="left")
        
        title_bg = ctk.CTkFrame(self.yt_frame, fg_color="#2b2b2b", corner_radius=8)
        title_bg.pack(pady=5)
        
        # --- CAMBIO 3: TEXTO DE SOPORTE MULTIPLATAFORMA ---
        ctk.CTkLabel(title_bg, text="YouTube Downloader", 
                     font=(self.main_font, 22, "bold"), text_color=c_yt, bg_color="#2b2b2b").pack(padx=15, pady=(8, 0))
        
        ctk.CTkLabel(title_bg, text="(YouTube, X/Twitter, Instagram, Facebook, TikTok, Twitch...)", 
                     font=(self.main_font, 11), text_color="#00aaff", bg_color="#2b2b2b").pack(padx=15, pady=(0, 8))
        # --------------------------------------------------

        # CONTROLES SUPERIORES (Compactos y centrados)
        controls_frame = ctk.CTkFrame(self.yt_frame, fg_color="#2b2b2b")
        controls_frame.pack(pady=10) 

        # Fila 1
        row1 = ctk.CTkFrame(controls_frame, fg_color="transparent")
        row1.pack(fill="x", padx=30, pady=10)
        
        self.yt_url_entry = ctk.CTkEntry(row1, placeholder_text="Pega el link aquí (YouTube, FB, IG, etc)...", height=40, width=500)
        self.yt_url_entry.pack(side="left", padx=(0, 5))
        self.yt_url_entry.bind("<Return>", lambda e: self.add_yt_to_queue()) 
        
        ctk.CTkButton(row1, text="📋 Pegar", width=80, height=40, fg_color="#444", hover_color="#555",
                      command=self.paste_to_yt_entry).pack(side="left", padx=5)

        ctk.CTkButton(row1, text="+ AGREGAR", width=120, height=40, fg_color=c_yt, hover_color=c_hover,
                                command=self.add_yt_to_queue).pack(side="right", padx=(5,0))

        # Fila 2
        row2 = ctk.CTkFrame(controls_frame, fg_color="transparent")
        row2.pack(fill="x", padx=30, pady=(0,10))

        ctk.CTkLabel(row2, text="Modo:").pack(side="left", padx=5)
        self.yt_mode_var = ctk.StringVar(value="Video")
        self.yt_mode_menu = ctk.CTkOptionMenu(row2, variable=self.yt_mode_var, values=["Video", "Audio"], width=120, 
                                              command=self.update_yt_ui_state, fg_color="#444")
        self.yt_mode_menu.pack(side="left", padx=5)

        self.yt_quality_var = ctk.StringVar(value="Max 4K")
        self.yt_quality_menu = ctk.CTkOptionMenu(row2, variable=self.yt_quality_var, 
                                                 values=["Max 4K", "Max 2K", "Max 1080p", "Max 720p"], width=180, fg_color="#333")
        self.yt_quality_menu.pack(side="left", padx=5)

        self.yt_cont_var = ctk.StringVar(value="MP4")
        # Recuerda la última selección de contenedor por separado para Video y Audio
        # (la calidad sí debe resetear siempre a la más alta al cambiar de modo, el
        # contenedor no).
        self._yt_last_container = {"Video": "MP4", "Audio": "MP3"}
        self.yt_cont_seg = ctk.CTkSegmentedButton(row2, variable=self.yt_cont_var, values=["MP4", "MKV"], 
                                                  selected_color=c_yt, width=150,
                                                  command=self._on_yt_cont_change)
        self.yt_cont_seg.pack(side="left", padx=10)

        # --- CHECKBOX: INCLUIR METADATOS ---
        self.yt_metadata_var = ctk.BooleanVar(value=False)
        self.yt_metadata_chk = ctk.CTkCheckBox(
            row2, text="Incluir Metadatos",
            variable=self.yt_metadata_var,
            fg_color="#444", hover_color="#555",
            checkmark_color="white"
        )
        self.yt_metadata_chk.pack(side="left", padx=15)
        # ------------------------------------

# Fila 3
        row3 = ctk.CTkFrame(controls_frame, fg_color="transparent")
        row3.pack(fill="x", padx=30, pady=(0,10))

        ctk.CTkLabel(row3, text="Guardar en:").pack(side="left", padx=5)
        user_downloads = os.path.join(os.path.expanduser("~"), "Downloads", "Descargas_YT")
        self.yt_save_path = ctk.StringVar(value=user_downloads)
        
        # --- CAMBIO AQUÍ: Agregamos text_color y forzamos la inserción ---
        self.entry_path_display = ctk.CTkEntry(row3, textvariable=self.yt_save_path, 
                                               fg_color="#181818", border_color="#333", 
                                               text_color="#eeeeee", width=300)
        self.entry_path_display.pack(side="left", padx=5, fill="x", expand=True)
        
        # Forzar actualización visual inmediata
        self.entry_path_display.delete(0, "end")
        self.entry_path_display.insert(0, user_downloads)
        
        self.entry_path_display.bind("<Key>", lambda e: "break") 
        # ---------------------------------------------------------------

        ctk.CTkButton(row3, text="📂 Cambiar", width=80, fg_color="#444", command=self.change_yt_folder).pack(side="left", padx=2)
        ctk.CTkButton(row3, text="↗ Abrir", width=60, fg_color="#444", command=self.open_yt_folder).pack(side="left", padx=2)
        ctk.CTkButton(row3, text="🔄 Default", width=60, fg_color="#444", command=self.restore_yt_default).pack(side="left", padx=2)

        # --- FILA 4: ACTUALIZADOR yt-dlp ---
        row_upd = ctk.CTkFrame(controls_frame, fg_color="transparent")
        row_upd.pack(fill="x", padx=30, pady=(0, 8))

        self.yt_upd_btn = ctk.CTkButton(
            row_upd, text="🔄 Actualizar yt-dlp", width=160, height=30,
            fg_color="#333", hover_color="#555",
            command=lambda: threading.Thread(
                target=self._yt_do_update, args=(self.yt_upd_lbl, self.yt_upd_btn, True), daemon=True
            ).start()
        )
        self.yt_upd_btn.pack(side="left", padx=(0, 10))

        self.yt_upd_lbl = ctk.CTkLabel(
            row_upd, text="Verificando versión...", text_color="#666", font=("Arial", 11)
        )
        self.yt_upd_lbl.pack(side="left")

        self.yt_aviso_spotify_var = ctk.BooleanVar(
            value=not self._config_leer().get("ocultar_aviso_spotify", False))
        ctk.CTkCheckBox(
            row_upd, text="Avisar al descargar de Spotify", variable=self.yt_aviso_spotify_var,
            fg_color="#1DB954", hover_color="#17a34a", checkmark_color="white",
            font=("Arial", 11), command=self._on_toggle_aviso_spotify
        ).pack(side="right")

        # Chequeo silencioso en segundo plano al abrir el módulo
        threading.Thread(
            target=self._yt_auto_check, args=(self.yt_upd_lbl, self.yt_upd_btn), daemon=True
        ).start()

        # --- ZONA DE PROGRESO GLOBAL ---
        global_frame = ctk.CTkFrame(self.yt_frame, fg_color="transparent")
        global_frame.pack(pady=5, padx=40)
        
        self.yt_global_prog = ctk.CTkProgressBar(global_frame, height=10, width=717, progress_color=c_yt)
        self.yt_global_prog.set(0)
        self.yt_global_prog.pack(side="left", padx=(0,10))
        
        ctk.CTkButton(global_frame, text="⛔ CANCELAR TODO", width=120, fg_color="#c92c2c", hover_color="#992222",
                      command=self.cancel_all_yt).pack(side="right")

        # --- LISTA SCROLLABLE ---
        self.queue_scroll = ctk.CTkScrollableFrame(self.yt_frame, width=900, height=450, 
                                                   fg_color="#181818", label_text="Cola de Descargas")
        self.queue_scroll.pack(pady=10, padx=40)
        self.queue_scroll._parent_canvas.configure(yscrollincrement=2)
    

    # --- AVISO DE SPOTIFY ---
    def _aviso_spotify(self):
        """Avisa que Spotify es lento y no conviene para playlists. True = continuar."""
        if self._config_leer().get("ocultar_aviso_spotify", False):
            return True

        resultado = {"seguir": False}
        win = self._ventana_nueva("Descarga desde Spotify", 480, 300, fg_color="#1a1a1a",
                                  redimensionable=(False, False))
        cont = ctk.CTkFrame(win, fg_color="transparent")
        cont.pack(fill="both", expand=True, padx=22, pady=16)

        ctk.CTkLabel(cont, text="🎵  Descarga desde Spotify", font=(self.main_font, 18, "bold"),
                     text_color="#1DB954").pack(anchor="w")
        ctk.CTkLabel(
            cont,
            text=("Spotify no deja descargar su audio: cada canción se busca en YouTube "
                  "y se descarga desde ahí, por eso el proceso es MÁS LENTO que una "
                  "descarga normal.\n\n"
                  "No se recomienda para playlists o álbumes grandes: las canciones se "
                  "buscan y descargan una por una."),
            justify="left", wraplength=430, font=("Arial", 12), text_color="#dddddd"
        ).pack(anchor="w", pady=(10, 12))

        no_mostrar = ctk.BooleanVar(value=False)
        ctk.CTkCheckBox(cont, text="No volver a mostrar este aviso", variable=no_mostrar,
                        fg_color="#1DB954", hover_color="#17a34a", checkmark_color="white"
                        ).pack(anchor="w")
        ctk.CTkLabel(cont, text="(Se puede volver a activar en YouTube Downloader)",
                     font=("Arial", 10), text_color="#777").pack(anchor="w", padx=(28, 0))

        botones = ctk.CTkFrame(cont, fg_color="transparent")
        botones.pack(side="bottom", fill="x", pady=(10, 0))

        def _cerrar(seguir):
            resultado["seguir"] = seguir
            if no_mostrar.get():
                self._config_guardar(ocultar_aviso_spotify=True)
                if hasattr(self, "yt_aviso_spotify_var"):
                    self.yt_aviso_spotify_var.set(False)
            try:
                win.grab_release()
            except Exception:
                pass
            win.destroy()

        ctk.CTkButton(botones, text="Continuar", width=130, height=34, fg_color="#1DB954",
                      hover_color="#17a34a", text_color="black", font=("Arial", 12, "bold"),
                      command=lambda: _cerrar(True)).pack(side="right")
        ctk.CTkButton(botones, text="Cancelar", width=110, height=34, fg_color="#444",
                      hover_color="#555", command=lambda: _cerrar(False)).pack(side="right", padx=(0, 10))
        win.protocol("WM_DELETE_WINDOW", lambda: _cerrar(False))
        win.bind("<Escape>", lambda e: _cerrar(False))

        def _modal(intentos=0):
            try:
                if not win.winfo_exists():
                    return
                if win.winfo_viewable():
                    win.grab_set()
                elif intentos < 60:
                    self.after(50, lambda: _modal(intentos + 1))
            except Exception:
                pass

        self._ventana_mostrar(win, recentrar=False)
        self.after(60, _modal)
        self.wait_window(win)
        return resultado["seguir"]

    def _on_toggle_aviso_spotify(self):
        self._config_guardar(ocultar_aviso_spotify=not bool(self.yt_aviso_spotify_var.get()))

    # --- HELPERS UI ---
    def _on_yt_cont_change(self, value):
        """Recuerda el contenedor elegido, por separado para Video y Audio."""
        self._yt_last_container[self.yt_mode_var.get()] = value

    def update_yt_ui_state(self, mode):
        if mode == "Video":
            self.yt_quality_menu.configure(values=["Max 4K", "Max 2K", "Max 1080p", "Max 720p", "Max 480p"])
            self.yt_quality_menu.set("Max 4K")
            self.yt_cont_seg.configure(values=["MP4", "MKV"])
            self.yt_cont_seg.set(self._yt_last_container.get("Video", "MP4"))
        else:
            self.yt_quality_menu.configure(values=[
                "🔒 Original",
                "⚡ Optimizado",
                "📱 Estándar",
                "🪶 Ligero (Solo Voz)",
            ])
            self.yt_quality_menu.set("🔒 Original")
            self.yt_cont_seg.configure(values=["MP3", "M4A", "OPUS", "WAV"])
            self.yt_cont_seg.set(self._yt_last_container.get("Audio", "MP3"))

    def paste_to_yt_entry(self):
        try:
            self.yt_url_entry.delete(0, 'end')
            self.yt_url_entry.insert(0, self.clipboard_get())
        except: pass

    def open_yt_folder(self):
        path = self.yt_save_path.get()
        if not os.path.exists(path): os.makedirs(path, exist_ok=True)
        try: os.startfile(path)
        except: pass

    def change_yt_folder(self):
        d = filedialog.askdirectory()
        if d: 
            self.yt_save_path.set(d)
            # --- FIX: Forzamos visualmente el cambio en el Entry ---
            try:
                self.entry_path_display.delete(0, "end")
                self.entry_path_display.insert(0, d)
            except: pass

    def restore_yt_default(self):
        default_path = os.path.join(os.path.expanduser("~"), "Downloads", "Descargas_YT")
        self.yt_save_path.set(default_path)
        # Forzar actualización visual
        try:
            self.entry_path_display.delete(0, "end")
            self.entry_path_display.insert(0, default_path)
        except: pass

    # ===========================================================
    # ACTUALIZADOR yt-dlp  (funciona en .py y en .exe compilado)
    # ===========================================================

    def _yt_auto_check(self, lbl, btn):
        """
        Chequeo silencioso de versión al abrir el módulo.
        Detecta yt-dlp de forma robusta (global + import frío + múltiples rutas de versión).
        """
        import urllib.request as _req, json as _json, importlib as _il

        def _norm(v):
            """Normaliza '2025.01.15' y '2025.1.15' al mismo tuple comparable."""
            try:
                return tuple(int(x) for x in str(v).strip().split("."))
            except Exception:
                return (0,)

        def _s(msg, color):
            self._en_ui(lbl.configure, text=msg, text_color=color)

        # ── 1. Obtener versión local de forma robusta ──────────────────────
        current = None
        _mod = yt_dlp  # captura el global en este momento

        if _mod is None:
            try:
                _mod = _il.import_module("yt_dlp")
            except Exception:
                _mod = None

        if _mod is not None:
            try:
                current = _mod.version.__version__
            except Exception:
                pass
            if not current:
                try:
                    current = getattr(_mod, '__version__', None)
                except Exception:
                    pass

        # ── 2. Consultar PyPI (solo si hay red) ────────────────────────────
        try:
            with _req.urlopen("https://pypi.org/pypi/yt-dlp/json", timeout=8) as r:
                latest = _json.loads(r.read())["info"]["version"]

            if current is None:
                _s("⚠️ yt-dlp no detectado. Pulsa para instalar.", "#ff9900")
            elif _norm(current) >= _norm(latest):
                _s(f"✅ yt-dlp {current} (última versión)", "#2ecc71")
            else:
                _s(f"⚠️ yt-dlp {current}  →  {latest} disponible", "#ff9900")

        except Exception:
            if current:
                _s(f"yt-dlp {current}  (sin red para verificar updates)", "#888")
            else:
                _s("Sin conexión — no se pudo verificar versión", "#666")

    def _yt_do_update(self, lbl, btn, force=False):
        """
        Descarga e instala la última versión de yt-dlp.
        · Modo .py   → pip install --upgrade yt-dlp  (+ recarga en memoria)
        · Modo .exe  → descarga el wheel de PyPI, comprueba su SHA-256 contra
                       la firma que publica PyPI, lo extrae junto al .exe e
                       inyecta la ruta al frente de sys.path
        """
        global yt_dlp   # ← declarado UNA SOLA VEZ al tope de la función
        import urllib.request as _req, json as _json, zipfile as _zip, hashlib as _hl

        # Protección contra ejecuciones simultáneas
        if getattr(self, '_yt_updating', False):
            return
        self._yt_updating = True

        def _s(msg, color="#aaa"):
            self._en_ui(lbl.configure, text=msg, text_color=color)

        def _bajar_verificado(info, destino, nombre):
            """
            Descarga un wheel de PyPI y comprueba que su SHA-256 sea el que PyPI
            publica para ese archivo. Si no coincide (descarga dañada o alterada)
            se borra y NO se instala: la versión que ya funcionaba queda intacta.
            """
            esperado = str((info.get("digests") or {}).get("sha256") or "").lower()
            if not esperado:
                raise Exception(f"PyPI no publicó la firma de {nombre}; no se instaló.")
            _req.urlretrieve(info["url"], destino)
            h = _hl.sha256()
            with open(destino, "rb") as fh:
                for bloque in iter(lambda: fh.read(1 << 20), b""):
                    h.update(bloque)
            if h.hexdigest().lower() != esperado:
                try:
                    os.remove(destino)
                except OSError:
                    pass
                print(f"[yt-updater] SHA-256 de {nombre} no coincide: {h.hexdigest()} != {esperado}")
                raise Exception(f"Firma SHA-256 de {nombre} no coincide; no se instaló.")

        try:
            self._en_ui(btn.configure, state="disabled", text="⏳ Actualizando...")
            _s("Consultando PyPI...", "#aaa")

            # 1. Versión más reciente en PyPI
            with _req.urlopen("https://pypi.org/pypi/yt-dlp/json", timeout=10) as r:
                pypi = _json.loads(r.read())
            latest  = pypi["info"]["version"]
            current = None
            _mod = yt_dlp
            if _mod is None:
                try:
                    import importlib as _ilx
                    _mod = _ilx.import_module("yt_dlp")
                except Exception:
                    pass
            if _mod is not None:
                try:
                    current = _mod.version.__version__
                except Exception:
                    current = getattr(_mod, '__version__', None)

            def _norm(v):
                try:
                    return tuple(int(x) for x in str(v).strip().split("."))
                except Exception:
                    return (0,)

            if current and _norm(current) >= _norm(latest) and not force:
                _s(f"✅ yt-dlp {current} ya es la versión más reciente.", "#2ecc71")
                return
            is_frozen = _is_frozen_build()

            # ── MODO SCRIPT (.py) ──────────────────────────────────────────
            if not is_frozen:
                _s(f"Ejecutando pip install yt-dlp {latest}...", "yellow")
                res = subprocess.run(
                    [sys.executable, "-m", "pip", "install", "--upgrade", "yt-dlp"],
                    capture_output=True, text=True, timeout=180
                )
                if res.returncode != 0:
                    raise Exception(res.stderr.strip()[:120] or "pip falló sin mensaje")

                # yt-dlp-ejs (paquete que yt-dlp necesita para resolver los retos de JS
                # de YouTube). No crítico: si falla, yt-dlp sigue funcionando igual,
                # solo con menos robustez frente a YouTube.
                try:
                    _s("Actualizando yt-dlp-ejs...", "yellow")
                    res_ejs = subprocess.run(
                        [sys.executable, "-m", "pip", "install", "--upgrade", "yt-dlp-ejs"],
                        capture_output=True, text=True, timeout=180
                    )
                    if res_ejs.returncode != 0:
                        print(f"[yt-updater] yt-dlp-ejs no crítico, falló: {res_ejs.stderr.strip()[:200]}")
                except Exception as _ejs_e:
                    print(f"[yt-updater] yt-dlp-ejs no crítico, excepción: {_ejs_e}")

                # Recargar en memoria para que la sesión actual use la versión nueva
                try:
                    import importlib as _il
                    _ytdlp_purgar_modulos()
                    yt_dlp = _il.import_module("yt_dlp")
                    _s(f"✅ yt-dlp {latest} activo ahora mismo.", "#2ecc71")
                except Exception as re_e:
                    _s(f"✅ yt-dlp {latest} instalado. Reinicia para activar.", "#2ecc71")
                    print(f"Reload no crítico: {re_e}")

            # ── MODO COMPILADO (.exe) ───────────────────────────────────────
            else:
                # Buscar wheel universal (none-any) en PyPI
                releases = pypi["releases"].get(latest, [])
                wheel_info = next(
                    (r for r in releases
                     if r["packagetype"] == "bdist_wheel" and "none-any" in r["filename"]),
                    None
                )
                if not wheel_info:
                    raise Exception("No se encontró wheel universal en PyPI para esta versión.")

                # Usar AppData/Local para que la escritura siempre funcione
                # desde el .exe sin necesitar permisos de administrador.
                _la      = os.environ.get("LOCALAPPDATA") or os.path.join(os.path.expanduser("~"), "AppData", "Local")
                pkg_dir  = os.path.join(_la, "DeusMachinaTools", "yt_dlp_live")
                os.makedirs(pkg_dir, exist_ok=True)
                tmp_whl  = os.path.join(pkg_dir, "_yt_dlp_new.whl")

                # ── DESCARGA VERIFICADA ────────────────────────────────────────
                # Se descarga y se comprueba la firma ANTES de tocar nada de la
                # versión instalada: si algo falla aquí, la anterior sigue intacta.
                _s(f"Descargando yt-dlp {latest}...", "yellow")
                _bajar_verificado(wheel_info, tmp_whl, "yt-dlp")

                # ── LIMPIEZA DE METADATOS DE VERSIONES ANTERIORES ──────────────
                # Elimina remanentes como yt_dlp-2025.12.8.data / .dist-info
                # que el extractor del wheel anterior dejó en pkg_dir.
                import glob as _glob
                _s("Limpiando metadatos anteriores...", "#888")
                _remnant_patterns = (
                    _glob.glob(os.path.join(pkg_dir, "yt_dlp-*.data")) +
                    _glob.glob(os.path.join(pkg_dir, "yt_dlp-*.dist-info"))
                )
                for _remnant in _remnant_patterns:
                    try:
                        if os.path.isdir(_remnant):
                            shutil.rmtree(_remnant, ignore_errors=True)
                        elif os.path.isfile(_remnant):
                            os.remove(_remnant)
                        print(f"[yt-updater] Remanente eliminado: {os.path.basename(_remnant)}")
                    except Exception as _clean_e:
                        # No crítico: si no se puede borrar (ej. archivo en uso),
                        # se registra y la actualización continúa igualmente.
                        print(f"[yt-updater] No se pudo eliminar '{os.path.basename(_remnant)}': {_clean_e}")
                # ───────────────────────────────────────────────────────────────

                _s("Firma verificada. Extrayendo paquete...", "yellow")
                # Limpiar versión anterior
                old_pkg = os.path.join(pkg_dir, "yt_dlp")
                if os.path.isdir(old_pkg):
                    shutil.rmtree(old_pkg, ignore_errors=True)

                with _zip.ZipFile(tmp_whl, 'r') as z:
                    z.extractall(pkg_dir)
                os.remove(tmp_whl)

                # yt-dlp-ejs (paquete que yt-dlp necesita para resolver los retos de JS
                # de YouTube). Mismo mecanismo de wheel "none-any" que yt-dlp, con la
                # misma verificación de firma. No crítico: si falla, yt-dlp sigue
                # funcionando igual, solo con menos robustez frente a YouTube.
                try:
                    _s("Buscando yt-dlp-ejs...", "#888")
                    with _req.urlopen("https://pypi.org/pypi/yt-dlp-ejs/json", timeout=10) as r_ejs:
                        pypi_ejs = _json.loads(r_ejs.read())
                    latest_ejs = pypi_ejs["info"]["version"]
                    releases_ejs = pypi_ejs["releases"].get(latest_ejs, [])
                    wheel_ejs = next(
                        (r for r in releases_ejs
                         if r["packagetype"] == "bdist_wheel" and "none-any" in r["filename"]),
                        None
                    )
                    if wheel_ejs:
                        _s(f"Descargando yt-dlp-ejs {latest_ejs}...", "yellow")
                        tmp_whl_ejs = os.path.join(pkg_dir, "_yt_dlp_ejs_new.whl")
                        _bajar_verificado(wheel_ejs, tmp_whl_ejs, "yt-dlp-ejs")
                        with _zip.ZipFile(tmp_whl_ejs, 'r') as z_ejs:
                            z_ejs.extractall(pkg_dir)
                        os.remove(tmp_whl_ejs)
                        print(f"[yt-updater] yt-dlp-ejs {latest_ejs} instalado en {pkg_dir}")
                    else:
                        print("[yt-updater] yt-dlp-ejs: no se encontró wheel universal, se omite (no crítico).")
                except Exception as _ejs_e:
                    print(f"[yt-updater] yt-dlp-ejs no crítico, excepción: {_ejs_e}")

                # Priorizar la nueva versión en sys.path
                if pkg_dir not in sys.path:
                    sys.path.insert(0, pkg_dir)

                # Intentar recargar en memoria
                try:
                    import importlib as _il
                    _ytdlp_purgar_modulos()
                    yt_dlp = _il.import_module("yt_dlp")
                    _s(f"✅ yt-dlp {latest} activo en esta sesión.", "#2ecc71")
                except Exception:
                    _s(f"✅ yt-dlp {latest} instalado. Reinicia la app.", "#2ecc71")

        except Exception as e:
            _s(f"❌ {str(e)[:65]}", "red")
            print(f"[yt-updater] Error: {e}")
        finally:
            self._yt_updating = False
            self._en_ui(btn.configure, state="normal", text="🔄 Actualizar yt-dlp")

    def add_yt_to_queue(self):
        # --- GUARD TIER-2: si yt_dlp aún no terminó de cargar ---
        if yt_dlp is None:
            if not _tier2_listo.is_set():
                messagebox.showinfo(
                    "Preparando módulo",
                    "El módulo YouTube aún se está cargando en background.\n"
                    "Espera unos segundos e intenta de nuevo.")
            else:
                messagebox.showerror(
                    "yt-dlp no disponible",
                    "yt-dlp no pudo cargarse. Verifica la instalación.")
            return
        url = self.yt_url_entry.get().strip()
        if not url: return
        # Spotify: aviso previo (se puede ocultar y reactivar en este módulo)
        if es_url_spotify(url) and not self._aviso_spotify():
            return
        self.yt_url_entry.delete(0, 'end')
        
        task_id = str(uuid.uuid4())
        
        # UI Item
        item_frame = ctk.CTkFrame(self.queue_scroll, fg_color="#2b2b2b", height=80)
        item_frame.pack(fill="x", pady=5, padx=5)
        
        info_row = ctk.CTkFrame(item_frame, fg_color="transparent")
        info_row.pack(fill="x", padx=10, pady=5)
        lbl_title = ctk.CTkLabel(info_row, text=f"Iniciando: {url[:30]}...", font=("Arial", 12, "bold"), anchor="w")
        lbl_title.pack(side="left", fill="x", expand=True)
        lbl_status = ctk.CTkLabel(info_row, text="En Cola", text_color="gray", font=("Arial", 11))
        lbl_status.pack(side="right")

        prog_row = ctk.CTkFrame(item_frame, fg_color="transparent")
        prog_row.pack(fill="x", padx=10, pady=(0,10))
        prog_bar = ctk.CTkProgressBar(prog_row, height=10, progress_color="#FF0000")
        prog_bar.set(0)
        prog_bar.pack(side="left", fill="x", expand=True, padx=(0,10))
        
        btn_pause = ctk.CTkButton(prog_row, text="⏸", width=30, height=25, fg_color="#F39C12", hover_color="#D35400")
        btn_pause.pack(side="left", padx=2)
        btn_cancel = ctk.CTkButton(prog_row, text="✖", width=30, height=25, fg_color="#C0392B", hover_color="#922B21")
        btn_cancel.pack(side="left", padx=2)

        decision_frame = ctk.CTkFrame(item_frame, fg_color="transparent", height=0)

        self.yt_downloads[task_id] = {
            "url": url,
            "es_spotify": es_url_spotify(url),
            # --- GUARDAR CONFIGURACIÓN AL MOMENTO DE AGREGAR ---
            "cfg_mode": self.yt_mode_var.get(),           # <--- AGREGAR
            "cfg_quality": self.yt_quality_var.get(),     # <--- AGREGAR
            "cfg_container": self.yt_cont_var.get(),      # <--- AGREGAR
            "cfg_path": self.yt_save_path.get(),          # <--- AGREGAR (Para que no falle si cambias carpeta también)
            "cfg_metadata": self.yt_metadata_var.get(),   # Estado congelado al presionar AGREGAR
            # ---------------------------------------------------
            "frame": item_frame,
            "decision_frame": decision_frame,
            "prog_row": prog_row,
            "lbl_title": lbl_title,
            "lbl_status": lbl_status,
            "prog_bar": prog_bar,
            "btn_pause": btn_pause,
            "status": "active", 
            "thread": None,
            "cancel_flag": False,
            "user_response": None
        }
        
        btn_pause.configure(command=lambda: self.toggle_pause_yt(task_id))
        btn_cancel.configure(command=lambda: self.cancel_single_yt(task_id))

        target_fn = self.run_spotify_download if self.yt_downloads[task_id]["es_spotify"] else self.run_single_yt_download
        t = threading.Thread(target=target_fn, args=(task_id,))
        self.yt_downloads[task_id]["thread"] = t
        t.start()
        self.update_global_progress()

        # --- AUTO-SCROLL (NUEVO) ---
        # Usamos .after para dar tiempo a que el widget se dibuje antes de bajar
        def scroll_to_bottom():
            try:
                # 1.0 significa el 100% de la altura (el final)
                self.queue_scroll._parent_canvas.yview_moveto(1.0)
            except: pass
            
        self.after(100, scroll_to_bottom)

    def get_media_info(self, file_path, stream_type):
        """Devuelve altura (video) o bitrate (audio) de forma robusta"""
        try:
            if stream_type == "video":
                # Para video, la altura siempre está en el stream
                cmd = [
                    "ffprobe", "-v", "error", "-select_streams", "v:0",
                    "-show_entries", "stream=height", "-of", "csv=p=0", file_path
                ]
                output = subprocess.check_output(cmd, startupinfo=self.get_startup_info()).decode().strip()
                return int(output) if output.isdigit() else 0
            
            else: # AUDIO
                # INTENTO 1: Buscar en el Stream (Preciso)
                cmd_stream = [
                    "ffprobe", "-v", "error", "-select_streams", "a:0",
                    "-show_entries", "stream=bit_rate", "-of", "csv=p=0", file_path
                ]
                out_stream = subprocess.check_output(cmd_stream, startupinfo=self.get_startup_info()).decode().strip()
                
                if out_stream.isdigit() and int(out_stream) > 0:
                    return int(out_stream)
                
                # INTENTO 2: Buscar en el Format (Contenedor general - Fallback)
                # Esto arregla el problema de "0 kbps" en muchos MP3/M4A
                cmd_fmt = [
                    "ffprobe", "-v", "error", 
                    "-show_entries", "format=bit_rate", "-of", "csv=p=0", file_path
                ]
                out_fmt = subprocess.check_output(cmd_fmt, startupinfo=self.get_startup_info()).decode().strip()
                
                if out_fmt.isdigit() and int(out_fmt) > 0:
                    return int(out_fmt)
                
                return 0 # Si falla todo
                
        except Exception as e:
            print(f"Error Media Info: {e}")
            return 0
        
        
    
    

    # --- COLA DE DESCARGAS: máximo YT_MAX_DESCARGAS bajando a la vez ---
    def _yt_hilo_vigente(self, data, hilo=None):
        """False si la tarea ya la tomó otro hilo (se pausó y se reanudó mientras tanto)."""
        actual = data.get("thread")
        return actual is None or actual is (hilo or threading.current_thread())

    def _yt_tomar_turno(self, data, texto_al_entrar=None):
        """
        Espera turno para BAJAR (análisis + descarga), en orden de llegada.
        Devuelve el turno, que se suelta con _yt_soltar_turno apenas termina de
        bajar: convertir o empaquetar no ocupa lugar, así la siguiente de la
        cola arranca sin esperar a FFmpeg. Si la tarea se pausa o se cancela
        mientras espera, lanza _YtDetenido.
        """
        turno = object()
        hilo = threading.current_thread()
        cond = self._yt_cola_cond
        posicion = None
        with cond:
            self._yt_cola_espera.append(turno)
            try:
                while True:
                    if (data["cancel_flag"] or data["status"] in ("cancelled", "paused")
                            or not self._yt_hilo_vigente(data, hilo)):
                        raise _YtDetenido("Detenido por usuario")
                    if (self._yt_cola_espera[0] is turno
                            and len(self._yt_cola_activos) < YT_MAX_DESCARGAS):
                        self._yt_cola_espera.pop(0)
                        self._yt_cola_activos.add(turno)
                        if posicion is not None and texto_al_entrar:
                            self._en_ui(data["lbl_status"].configure,
                                        text=texto_al_entrar, text_color="white")
                        return turno
                    pos = self._yt_cola_espera.index(turno) + 1
                    if pos != posicion:
                        posicion = pos
                        self._en_ui(data["lbl_status"].configure,
                                    text=f"⏳ En cola (#{pos})", text_color="gray")
                    cond.wait(0.5)
            except BaseException:
                if turno in self._yt_cola_espera:
                    self._yt_cola_espera.remove(turno)
                cond.notify_all()
                raise

    def _yt_soltar_turno(self, turno):
        """Libera el cupo de descarga. Llamarlo de más no hace nada."""
        if turno is None:
            return
        with self._yt_cola_cond:
            if turno in self._yt_cola_activos:
                self._yt_cola_activos.discard(turno)
                self._yt_cola_cond.notify_all()

    def _yt_despertar_cola(self):
        """Avisa a las tareas en espera (una se pausó o canceló) para que se reacomoden ya."""
        cond = getattr(self, "_yt_cola_cond", None)
        if cond is not None:
            with cond:
                cond.notify_all()

    # --- LÓGICA DE DESCARGA (CON FIX DE AUDIO MP4) ---
    # --- LÓGICA DE DESCARGA CORREGIDA ---
    def run_spotify_download(self, task_id):
        """
        Maneja una URL de Spotify (canción, álbum o playlist) con spotDL, con
        el MISMO pipeline que las playlists de YouTube:
          1) resuelve la lista de canciones con `spotdl save` (no descarga
             nada, solo trae metadata) para saber cuántas son;
          2) si son varias, avisa con el mismo popup de "playlist detectada"
             y deja cancelar;
          3) crea una subcarpeta con el nombre de la playlist/álbum;
          4) descarga canción por canción, mostrando "(i/total) Título" y la
             barra de avance general, en vez del log crudo de spotDL;
          5) respeta CHECKPOINT_EVERY (preguntar cada N) y la espera
             aleatoria entre canciones;
          6) respeta la calidad de audio elegida en la UI (--bitrate).
        La carátula la incrusta el propio spotDL con el álbum art oficial de
        Spotify, que es justo lo que se quiere cuando el link es de Spotify.
        """
        CHECKPOINT_EVERY = 50

        data        = self.yt_downloads[task_id]
        url         = data["url"]
        save_folder = data["cfg_path"]
        container   = data.get("cfg_container", "MP3")
        quality     = data.get("cfg_quality", "🔒 Original")

        def _ui(fn):
            """Toda actualización de widgets desde este hilo pasa por aquí."""
            self._en_ui(fn)

        # Turno en la cola de descargas: consultar Spotify y cada lote de spotDL
        # ocupan uno (máximo YT_MAX_DESCARGAS bajando a la vez)
        turno = None
        hilo = threading.current_thread()

        try:
            os.makedirs(save_folder, exist_ok=True)

            _ui(lambda: data["lbl_status"].configure(text="Preparando spotDL...", text_color="cyan"))
            listo = asegurar_spotdl_disponible(
                status_cb=lambda m: _ui(lambda m=m: data["lbl_status"].configure(text=m, text_color="cyan"))
            )
            # spotDL descarga desde YouTube con yt-dlp: Deno resuelve los retos JS de YouTube
            try:
                asegurar_deno_disponible(
                    status_cb=lambda m: _ui(lambda m=m: data["lbl_status"].configure(text=m, text_color="#aaaaff"))
                )
            except Exception as _deno_e:
                print(f"[Spotify] asegurar_deno_disponible no crítico: {_deno_e}")
            if not listo:
                _ui(lambda: data["lbl_status"].configure(text="❌ spotDL no disponible (revisa consola)", text_color="red"))
                data["status"] = "finished"
                _ui(lambda: data["btn_pause"].configure(state="disabled"))
                return

            # --- Formato y calidad (respetando lo elegido en la UI) ---
            cont_map = {"MP3": "mp3", "M4A": "m4a", "OPUS": "opus", "WAV": "wav",
                        "MP4": "mp3", "MKV": "mp3"}  # spotDL es solo audio
            formato = cont_map.get(container, "mp3")

            if   "Optimizado" in quality: bitrate = "192k"
            elif "Estándar"   in quality: bitrate = "128k"
            elif "Ligero"     in quality: bitrate = "64k"
            else:                          bitrate = "disable"  # 🔒 Original: sin reconversión

            base_args = [
                "--audio", "youtube",
                "--format", formato,
                "--bitrate", bitrate,
                "--max-retries", "1",  # reintentos de la API de Spotify (no tiene que ver con YouTube Music)
                "--simple-tui", "--log-level", "INFO",
            ]

            # --- 1. RESOLVER LISTA DE CANCIONES (sin descargar) ---
            turno = self._yt_tomar_turno(data)
            _ui(lambda: data["lbl_status"].configure(text="🔍 Analizando enlace de Spotify...", text_color="cyan"))
            temp_dir = os.path.join(save_folder, f"_sp_tmp_{task_id[:8]}")
            os.makedirs(temp_dir, exist_ok=True)
            save_file = os.path.join(temp_dir, "lista.spotdl")

            canciones = []
            def _extraer_json(texto):
                """
                spotDL mezcla líneas de log con el JSON en la misma salida, y
                esas líneas de log también traen '[' (ej. '[download] ...'),
                así que agarrar el primer '[' rompe el parseo. Se prueba cada
                posición candidata hasta que una decodifique de verdad.
                """
                texto = (texto or "").strip()
                if not texto:
                    return []
                dec = json.JSONDecoder()
                posiciones = [i for i, ch in enumerate(texto) if ch in '[{'][:300]
                for i in posiciones:
                    try:
                        datos, _ = dec.raw_decode(texto[i:])
                    except Exception:
                        continue
                    if isinstance(datos, list) and datos:
                        return datos
                    if isinstance(datos, dict):
                        posibles = datos.get("songs") or []
                        if posibles:
                            return posibles
                return []

            try:
                # spotDL admite "--save-file -" para imprimir el JSON por
                # stdout en vez de escribirlo a disco (más confiable que
                # depender de la ruta del archivo).
                r = subprocess.run(
                    _cmd_modulo_python("spotdl") + ["save", url,
                     "--save-file", "-"] + base_args,
                    capture_output=True, text=True, encoding="utf-8", errors="ignore",
                    timeout=300, startupinfo=self.get_startup_info(),
                    env=_env_subproceso_utf8(),
                )
                canciones = _extraer_json(r.stdout)

                # Respaldo: intentar con archivo si stdout no sirvió
                if not canciones:
                    r2 = subprocess.run(
                        _cmd_modulo_python("spotdl") + ["save", url,
                         "--save-file", save_file] + base_args,
                        capture_output=True, text=True, encoding="utf-8", errors="ignore",
                        timeout=300, startupinfo=self.get_startup_info(),
                        env=_env_subproceso_utf8(),
                    )
                    if os.path.exists(save_file):
                        try:
                            with open(save_file, "r", encoding="utf-8") as f:
                                canciones = _extraer_json(f.read())
                        except Exception as fe:
                            print(f"[Spotify] No se pudo leer el archivo de lista: {fe}")
                    if not canciones:
                        print(f"[Spotify] 'save' no devolvió canciones.")
                        print(f"[Spotify]   stdout: {(r2.stdout or '')[:300]}")
                        print(f"[Spotify]   stderr: {(r2.stderr or '')[:300]}")
            except Exception as se:
                print(f"[Spotify] No se pudo resolver la lista: {se}")

            def _correr_spotdl(queries, carpeta_destino, total_esperado, offset=0):
                """
                Corre UNA sola instancia de spotDL para varias canciones.
                Lanzar un proceso por canción costaba ~3-5s de arranque de
                Python+spotDL cada vez (de ahí la lentitud); así ese costo se
                paga una sola vez por lote.
                Lee el avance real de las líneas "N/M complete" que imprime
                spotDL y el nombre de la canción en curso de las líneas
                "Título: acción", para mantener el estado en español en vez
                del log crudo.
                Devuelve (completadas, lista_sin_match).
                """
                hechas, sin_m = 0, []
                salida_tmpl = os.path.join(carpeta_destino, "{artists} - {title}.{output-ext}")
                proceso = subprocess.Popen(
                    _cmd_modulo_python("spotdl") + ["download"] + list(queries) +
                    ["--output", salida_tmpl, "--threads", "1"] + base_args,
                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                    universal_newlines=True, encoding="utf-8", errors="ignore",
                    startupinfo=self.get_startup_info(),
                    env=_env_subproceso_utf8(),
                )
                data["process_handle"] = proceso
                try:
                    for linea in proceso.stdout:
                        if data["status"] in ("cancelled", "paused") or data["cancel_flag"]:
                            proceso.kill()
                            break
                        linea = linea.rstrip()
                        print(f"[spotDL] {linea}")
                        baja = linea.lower()

                        # OJO: "YouTube Music returned no usable results" NO
                        # es un fallo: solo avisa que pasó al siguiente
                        # proveedor (youtube), y la canción normalmente sí se
                        # descarga. El fallo real es "no match could be found".
                        if "no match could be found" in baja or "skipping" in baja:
                            sin_m.append(linea)

                        # Avance real: "N/M complete"
                        mc = re.search(r'(\d+)\s*/\s*(\d+)\s+complete', baja)
                        if mc:
                            hechas = int(mc.group(1))
                            glob = (offset + hechas) / max(1, total_esperado)
                            _ui(lambda p=min(1.0, glob): data["prog_bar"].set(p))
                            continue

                        # Canción en curso: "Artista - Título: acción"
                        mt = re.match(r'^(.*?):\s*(Searching|Getting|Downloading|Embedding|Done)', linea)
                        if mt:
                            titulo_actual = mt.group(1)[:45]
                            accion = {
                                "Searching":  "Buscando",
                                "Getting":    "Obteniendo info",
                                "Downloading": "Descargando",
                                "Embedding":  "Incrustando datos",
                                "Done":       "Listo",
                            }.get(mt.group(2), "Procesando")
                            n_actual = offset + hechas + 1
                            _ui(lambda t=titulo_actual, a=accion, n=n_actual: data["lbl_status"].configure(
                                text=f"({min(n, total_esperado)}/{total_esperado}) {a}: {t}",
                                text_color="white"))
                    proceso.wait()
                finally:
                    data["process_handle"] = None
                return hechas, sin_m

            if not canciones:
                # No se pudo resolver la lista (link raro, canción suelta,
                # etc.): en vez de morir, se le pasa la URL tal cual a
                # spotDL, que es justamente lo que sabe manejar.
                print("[Spotify] Sin lista previa; descargando la URL directamente.")
                _ui(lambda: data["lbl_status"].configure(text="Descargando desde Spotify...", text_color="white"))
                hechas, sin_m = _correr_spotdl([url], save_folder, 1)
                shutil.rmtree(temp_dir, ignore_errors=True)
                if data["status"] not in ("cancelled", "paused"):
                    _ui(lambda: data["prog_bar"].set(1.0))
                    if sin_m and not hechas:
                        _ui(lambda: data["lbl_status"].configure(
                            text="⚠️ No se encontró match en YouTube", text_color="orange"))
                    else:
                        _ui(lambda: data["lbl_status"].configure(text="✅ Completado", text_color="#2ecc71"))
                    data["status"] = "finished"
                    _ui(lambda: data["btn_pause"].configure(state="disabled"))
                return

            # La lista ya está resuelta: mientras se espera la respuesta del
            # aviso de playlist no se ocupa lugar en la cola (cada lote pide el suyo)
            self._yt_soltar_turno(turno)
            turno = None

            total = len(canciones)

            def _nombre(c):
                art = c.get("artist") or (c.get("artists") or [""])[0] or ""
                tit = c.get("name") or c.get("title") or "Canción"
                return f"{art} - {tit}".strip(" -")

            # --- 2. POPUP DE PLAYLIST + LÍMITE (igual que en YouTube) ---
            if total > 1:
                # El tipo (Album/Playlist) se determina por la URL, que es
                # 100% confiable (open.spotify.com/album/... vs .../playlist/...)
                # — el nombre sale de la metadata de spotDL con el campo que
                # corresponda a cada caso.
                url_baja = url.lower()
                if "/playlist/" in url_baja:
                    tipo = "Playlist"
                    nombre_lista = canciones[0].get("list_name") or ""
                elif "/album/" in url_baja:
                    tipo = "Album"
                    nombre_lista = canciones[0].get("album_name") or ""
                else:
                    tipo = "Playlist"  # ej. /artist/... (todas sus canciones)
                    nombre_lista = canciones[0].get("list_name") or canciones[0].get("album_name") or ""
                if not nombre_lista:
                    nombre_lista = "Spotify"

                continuar = self._en_ui_espera(
                    messagebox.askyesno,
                    f"{tipo} de Spotify detectada",
                    f"Se detectó un(a) {tipo.lower()} de {total} canción(es):\n\n"
                    f"\"{nombre_lista[:80]}\"\n\n"
                    f"Se descargarán en una subcarpeta \"{tipo} - {nombre_lista[:60]}\",\n"
                    f"preguntando cada {CHECKPOINT_EVERY} canciones si deseas continuar.\n\n"
                    f"¿Deseas continuar?"
                )
                if not continuar:
                    _ui(lambda: data["lbl_status"].configure(text="Cancelado por usuario.", text_color="orange"))
                    data["status"] = "finished"
                    _ui(lambda: data["btn_pause"].configure(state="disabled"))
                    shutil.rmtree(temp_dir, ignore_errors=True)
                    return

                forbidden_chars = '<>:"/\\|?*\n\r\t'
                nombre_carpeta = f"{tipo} - {nombre_lista[:70]}"
                safe_pl = "".join(c for c in nombre_carpeta if c not in forbidden_chars).strip(". ")
                if not safe_pl: safe_pl = f"{tipo} - Spotify"
                destino = os.path.join(save_folder, safe_pl)
                os.makedirs(destino, exist_ok=True)
                _ui(lambda: data["lbl_title"].configure(text=f"📋 {safe_pl}  (0/{total})"))
            else:
                safe_pl = ""
                destino = save_folder
                _ui(lambda t=_nombre(canciones[0]): data["lbl_title"].configure(text=t[:60]))

            # --- 3. DESCARGA POR LOTES (un solo proceso por lote) ---
            done_count = 0
            sin_match  = []

            _ui(lambda: data["prog_bar"].set(0))

            # Cada lote = CHECKPOINT_EVERY canciones. Un solo proceso spotDL
            # por lote (en vez de uno por canción) evita pagar el arranque
            # de Python+spotDL una y otra vez, que era el grueso de la
            # lentitud. Entre lotes va la pausa corta y el checkpoint.
            for inicio in range(0, total, CHECKPOINT_EVERY):
                if data["status"] in ("cancelled", "paused") or data["cancel_flag"]:
                    _ui(lambda d=done_count: data["lbl_status"].configure(
                        text=f"⛔ Detenido en {d}/{total}", text_color="orange"))
                    break

                lote = canciones[inicio:inicio + CHECKPOINT_EVERY]
                queries = []
                for c in lote:
                    su = c.get("url") or (c.get("external_urls") or {}).get("spotify") or ""
                    queries.append(su if su else _nombre(c))

                if total > 1:
                    _ui(lambda n=inicio + 1: data["lbl_title"].configure(
                        text=f"📋 {safe_pl}  ({n}/{total})"))

                # Cola de descargas: el lote espera su turno para bajar
                try:
                    turno = self._yt_tomar_turno(data, "Descargando desde Spotify...")
                except _YtDetenido:
                    if not self._yt_hilo_vigente(data, hilo):
                        return
                    _ui(lambda d=done_count: data["lbl_status"].configure(
                        text=f"⛔ Detenido en {d}/{total}", text_color="orange"))
                    break

                try:
                    hechas, sin_m = _correr_spotdl(queries, destino, total, offset=inicio)
                    done_count += hechas
                    sin_match.extend(sin_m)
                except Exception as de:
                    print(f"[Spotify] Error en el lote desde {inicio + 1}: {de}")
                finally:
                    self._yt_soltar_turno(turno)
                    turno = None

                self.update_global_progress()

                if data["status"] in ("cancelled", "paused") or data["cancel_flag"]:
                    _ui(lambda d=done_count: data["lbl_status"].configure(
                        text=f"⛔ Detenido en {d}/{total}", text_color="orange"))
                    break

                siguiente = inicio + CHECKPOINT_EVERY
                if siguiente < total:
                    # --- CHECKPOINT (igual que en las playlists de YouTube) ---
                    restantes = total - siguiente
                    cont = self._en_ui_espera(
                        messagebox.askyesno,
                        "Continuar descarga de Spotify",
                        f"Van {done_count} canciones descargadas.\n"
                        f"Quedan {restantes} canción(es).\n\n"
                        f"¿Deseas continuar con la descarga?"
                    )
                    if not cont:
                        _ui(lambda d=done_count: data["lbl_status"].configure(
                            text=f"⏹ Detenido por usuario ({d}/{total})", text_color="orange"))
                        data["status"] = "finished"
                        _ui(lambda: data["btn_pause"].configure(state="disabled"))
                        self.update_global_progress()
                        shutil.rmtree(temp_dir, ignore_errors=True)
                        return
                    # Sin pausa entre lotes acá a propósito: en Spotify cada
                    # lote ya es UN solo proceso de spotDL para varias
                    # canciones (no una descarga por canción), así que no
                    # aplica la misma lógica anti-bloqueo que en YouTube.

            shutil.rmtree(temp_dir, ignore_errors=True)

            # --- 4. FINALIZACIÓN ---
            if data["status"] not in ("cancelled", "paused"):
                _ui(lambda: data["prog_bar"].set(1.0))
                if sin_match and done_count == 0:
                    _ui(lambda: data["lbl_status"].configure(
                        text="⚠️ No se encontró match en YouTube", text_color="orange"))
                elif sin_match:
                    _ui(lambda d=done_count, s=len(sin_match): data["lbl_status"].configure(
                        text=f"✅ {d}/{total} descargadas  (sin match: {s})", text_color="#f1c40f"))
                else:
                    _ui(lambda d=done_count: data["lbl_status"].configure(
                        text=f"✅ {d}/{total} descargadas", text_color="#2ecc71"))
                data["status"] = "finished"
                _ui(lambda: data["btn_pause"].configure(state="disabled"))

        except Exception as e:
            # Se pausó y se reanudó mientras este hilo seguía: la tarea (y su
            # carpeta temporal) ya es de otro hilo. Este sale sin tocar nada.
            if not self._yt_hilo_vigente(data, hilo):
                return
            _tmp_sp = locals().get("temp_dir")
            if _tmp_sp:
                shutil.rmtree(_tmp_sp, ignore_errors=True)
            # Pausada o cancelada mientras esperaba turno: el botón ya puso el estado
            if isinstance(e, _YtDetenido) or data["status"] in ("cancelled", "paused"):
                return
            print(f"[Spotify] Error: {e}")
            msg_err = str(e)[:50]   # 'e' se borra al salir del except; el lambda corre después
            try:
                _ui(lambda m=msg_err: data["lbl_status"].configure(text=f"❌ Error: {m}", text_color="red"))
                data["status"] = "finished"
                _ui(lambda: data["btn_pause"].configure(state="disabled"))
            except Exception:
                pass

        finally:
            self._yt_soltar_turno(turno)
            self.update_global_progress()

    def run_single_yt_download(self, task_id):
        data = self.yt_downloads[task_id]
        url = data["url"]

        def _estado(texto, color):
            """Los widgets solo se tocan desde el hilo de la interfaz."""
            self._en_ui(data["lbl_status"].configure, text=texto, text_color=color)

        # 1. LEER CONFIGURACIÓN GUARDADA (FIX: NO CAMBIAR AL REANUDAR)
        # Se congeló al presionar AGREGAR: no cambia aunque el usuario mueva los controles
        mode = data["cfg_mode"]
        quality = data["cfg_quality"]
        container = data["cfg_container"]
        save_folder = data["cfg_path"]
        embed_meta = data.get("cfg_metadata", False)  # Estado aislado: no cambia aunque el usuario mueva el checkbox
        if not os.path.exists(save_folder): os.makedirs(save_folder, exist_ok=True)

        # Carpeta temporal
        temp_dir = os.path.join(save_folder, f"temp_{task_id}")
        if not os.path.exists(temp_dir): os.makedirs(temp_dir, exist_ok=True)

        if hasattr(self, 'yt_active_temps'):
            self.yt_active_temps.append(temp_dir)

        # --- FIX BUG 1: VARIABLE LOCAL DE PROTECCIÓN ---
        # Usamos esto para que el hilo recuerde si FUE PAUSADO,
        # sin importar si el usuario ya le dio a "Reanudar" en la interfaz.
        thread_keeping_files = False

        # Turno en la cola de descargas (máximo YT_MAX_DESCARGAS bajando a la vez)
        turno = None
        hilo = threading.current_thread()

        # --- A. DEFINIR EL OBJETIVO (TARGET) ---
        limit_height = 0
        target_bitrate = 0

        ydl_opts = {
            'noplaylist': True,
            'quiet': True,
            'no_warnings': True,
            'overwrites': True,
            'progress_hooks': [lambda d: self.hook_yt_progress(d, task_id, hilo)],
        }

        # Asegurar Deno/curl_cffi disponibles (mejor compatibilidad con
        # YouTube/TikTok/etc.). No bloquea nada si no se puede: yt-dlp sigue
        # funcionando igual que hoy en ese caso.
        try:
            asegurar_deno_disponible(status_cb=lambda m: _estado(m, "#aaaaff"))
        except Exception as _deno_e:
            print(f"[YT] asegurar_deno_disponible no crítico: {_deno_e}")
        ydl_opts.update(_yt_opts_robustos())
        ydl_opts.update(_yt_opts_diagnostico())  # imprime en consola si curl_cffi/Deno se usaron de verdad

        # Mapear el label de calidad a modo interno (homologado con el Convertidor de Audio)
        if   "Optimizado" in quality: audio_mode = "optimized"
        elif "Estándar"   in quality: audio_mode = "standard"
        elif "Ligero"     in quality: audio_mode = "light"
        else:                          audio_mode = "original"

        # Bitrate aproximado por modo: usado SOLO para el chequeo de duplicados
        _MODE_KBPS = {"original": 256, "optimized": 192, "standard": 128, "light": 64}
        target_bitrate = _MODE_KBPS.get(audio_mode, 256) * 1000

        if mode == "Audio":
            ydl_opts['format'] = 'bestaudio/best'
        else:
            limit_height = 1080
            if "4K" in quality: limit_height = 2160
            elif "2K" in quality: limit_height = 1440
            elif "720p" in quality: limit_height = 720
            elif "480p" in quality: limit_height = 480

            ydl_opts['merge_output_format'] = container.lower()  # remuxear directo al contenedor pedido (antes: fijo a 'mkv')
            if 'postprocessor_args' in ydl_opts: del ydl_opts['postprocessor_args']
            ydl_opts['format'] = f'bestvideo[height<={limit_height}]+bestaudio/best[height<={limit_height}]'

        try:
            # --- COLA: si ya hay YT_MAX_DESCARGAS bajando, espera su turno ---
            turno = self._yt_tomar_turno(data)

            # --- B. EXTRACCIÓN Y LIMPIEZA DE NOMBRE ---
            _estado("Analizando...", "yellow")

            # ── Pre-detección por URL ─────────────────────────────────────
            import urllib.parse as _uparse
            _parsed  = _uparse.urlparse(url)
            _qparams = _uparse.parse_qs(_parsed.query)
            _list_id = _qparams.get('list', [''])[0]

            _is_mix_url = bool(
                _list_id.startswith('RD')
                or _list_id.startswith('RDMM')
                or 'start_radio=1' in url
            )
            _treat_as_playlist = bool(_list_id) and not _is_mix_url
            # ─────────────────────────────────────────────────────────────

            pl_entries    = None
            original_title = 'Video_Sin_Nombre'

            if _treat_as_playlist:
                # ── RAMA PLAYLIST: extraer con URL de playlist directa ────
                _pl_url  = f"https://www.youtube.com/playlist?list={_list_id}"
                _pl_opts = {
                    'quiet': True, 'no_warnings': True,
                    'extract_flat': True, 'socket_timeout': 15,
                }
                _pl_opts.update(_yt_opts_robustos())
                try:
                    with yt_dlp.YoutubeDL(_pl_opts) as _ydl_pl:
                        _pl_info = _ydl_pl.extract_info(_pl_url, download=False)
                    pl_entries     = [e for e in _pl_info.get('entries', []) if e]
                    original_title = _pl_info.get('title', 'Lista_Reproduccion')
                except Exception as _pe:
                    print(f"[YT] Error extrayendo playlist: {_pe}")
                    # Si falla la extracción de playlist → tratar como video individual
                    _treat_as_playlist = False
                    pl_entries = None
                # ─────────────────────────────────────────────────────────

            if not _treat_as_playlist:
                # ── RAMA VIDEO INDIVIDUAL (incluye mixes) ─────────────────
                # Sin extract_flat para obtener el título y metadatos completos
                _sv_opts = {
                    'quiet': True, 'no_warnings': True,
                    'noplaylist': True, 'socket_timeout': 15,
                }
                _sv_opts.update(_yt_opts_robustos())
                try:
                    with yt_dlp.YoutubeDL(_sv_opts) as _ydl_sv:
                        info = _ydl_sv.extract_info(url, download=False)
                    original_title = info.get('title') or 'Video_Sin_Nombre'
                except Exception as _sve:
                    print(f"[YT] Error extrayendo info individual: {_sve}")
                    info = {}
                    original_title = 'Video_Sin_Nombre'
                # ─────────────────────────────────────────────────────────

            forbidden_chars = '<>:"/\\|?*\n\r\t'
            safe_title = original_title[:100]
            safe_title = "".join([c for c in safe_title if c not in forbidden_chars]).strip(". ")
            if not safe_title: safe_title = f"Video_{task_id[:8]}"

            display_name = safe_title + "..." if len(original_title) > 100 else safe_title
            self._en_ui(data["lbl_title"].configure, text=display_name)

            # --- CAPTURA DE METADATOS (solo video individual) ---
            yt_meta = {}
            if embed_meta and not _treat_as_playlist:
                # info ya tiene extracción completa desde la rama de video individual
                yt_meta = self._yt_build_meta(info, original_title, url)
            # -------------------------------------------------------

            # --- REDIRECCIÓN A PLAYLIST (sale del flujo normal) ---
            if _treat_as_playlist and pl_entries is not None:
                # Cada video de la playlist pide su propio turno en la cola
                self._yt_soltar_turno(turno)
                self.run_playlist_yt_download(
                    task_id        = task_id,
                    entries        = pl_entries,
                    pl_title_raw   = original_title,
                    mode           = mode,
                    quality        = quality,
                    container      = container,
                    save_folder    = save_folder,
                    embed_meta     = embed_meta,
                    audio_mode     = audio_mode,
                    limit_height   = limit_height,
                    ydl_opts_base  = dict(ydl_opts),
                )
                return
            # -------------------------------------------------------

            # --- C. VERIFICACIÓN DE EXISTENCIA ---
            ext_final = container.lower()
            final_filename = f"{safe_title}.{ext_final}"
            final_path = os.path.join(save_folder, final_filename)

            ydl_opts['outtmpl'] = os.path.join(temp_dir, f"{safe_title}.%(ext)s")

            if os.path.exists(final_path):
                msg_user = ""
                if mode == "Audio":
                    existing_br   = self.get_media_info(final_path, "audio")
                    existing_kbps = int(existing_br / 1000)

                    # Rangos lógicos según el modo elegido por el usuario
                    _mode_labels = {
                        "light":     "Ligero",
                        "standard":  "Estándar",
                        "optimized": "Optimizado",
                        "original":  "Original",
                    }
                    if audio_mode == "light":
                        already_ok = existing_kbps <= 80
                    elif audio_mode == "standard":
                        already_ok = 96 <= existing_kbps <= 160
                    else:  # optimized / original
                        already_ok = existing_kbps >= 165

                    if already_ok:
                        self.mark_as_skipped(data, f"⚠️ Ya existe ({existing_kbps} kbps).")
                        return
                    else:
                        mode_label = _mode_labels.get(audio_mode, audio_mode.capitalize())
                        msg_user = f"Existe ({existing_kbps}kbps). ¿Reemplazar con modo {mode_label}?"
                else:
                    existing_h = self.get_media_info(final_path, "video")
                    if abs(existing_h - limit_height) < 20:
                        self.mark_as_skipped(data, f"⚠️ Ya existe ({existing_h}p).")
                        return
                    else:
                        msg_user = f"Existe ({existing_h}p). ¿Reemplazar con {limit_height}p?"

                if msg_user:
                    # Mientras espera tu respuesta no ocupa lugar en la cola
                    self._yt_soltar_turno(turno)
                    self.ask_user_overwrite(task_id, msg_user)
                    if not self.wait_for_decision(task_id, temp_dir): return
                    try: os.remove(final_path)
                    except: pass
                    self.restore_ui_after_decision(task_id)
                    turno = self._yt_tomar_turno(data, "Descargando...")

            # --- [BLOQUE D] PROCESAMIENTO MAESTRO ---
            if data["status"] == "active":

                run_manual_process = True
                _estado("Bajando fuentes...", "white")

                # 1. DESCARGA
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])

                    # Ya bajó: el turno queda libre para la siguiente de la cola
                    # mientras esta convierte / empaqueta
                    self._yt_soltar_turno(turno)

                    # === 2. PROCESAMIENTO / REMUX (helper compartido con playlist) ===
                    if run_manual_process and data["status"] == "active":

                        # --- FIX BUG 2: BLOQUEAR PAUSA DURANTE PROCESAMIENTO ---
                        # Evita que el usuario reinicie el proceso por error
                        self._en_ui(data["btn_pause"].configure, state="disabled")
                        # -------------------------------------------------------

                        self._en_ui(data["prog_bar"].configure, progress_color="#F39C12")
                        self._en_ui(data["prog_bar"].set, 0)
                        _estado("Analizando codecs...", "#F39C12")

                        final_path = os.path.join(save_folder, final_filename)

                        def _single_should_abort():
                            return data["status"] != "active"

                        def _single_on_tick(frac, is_copy_only):
                            action_txt = "Empaquetando..." if is_copy_only else "Convirtiendo..."
                            self._en_ui(data["prog_bar"].set, frac)
                            _estado(f"{action_txt} {int(frac * 100)}%", "#F39C12")

                        def _single_on_thumb_start():
                            _estado("Incrustando carátula...", "#aaaaff")

                        self._yt_convertir_meta_caratula(
                            temp_dir=temp_dir, final_path=final_path, ext_final=ext_final,
                            mode=mode, container=container, audio_mode=audio_mode,
                            embed_meta=embed_meta, yt_meta=yt_meta, data=data,
                            should_abort=_single_should_abort, on_tick=_single_on_tick,
                            on_thumb_start=_single_on_thumb_start,
                        )
                        # -----------------------------------------------------

            # --- FINALIZACIÓN ---
            if data["status"] == "active":
                self._en_ui(data["prog_bar"].set, 1)
                _estado("✅ Completado", "#2ecc71")

                # Mover archivo
                files_in_temp = os.listdir(temp_dir)
                if files_in_temp:
                    src_path = os.path.join(temp_dir, files_in_temp[0])
                    moved = False
                    for _ in range(5):
                        try:
                            if os.path.exists(final_path) and os.path.getsize(final_path) > 0:
                                moved = True; break
                            else:
                                shutil.move(src_path, final_path)
                                moved = True; break
                        except: time.sleep(1)

                    if moved:
                        data["status"] = "finished"
                        _estado("✅ Terminado", "#2ECC71")
                        self._en_ui(data["prog_bar"].set, 1.0)
                        self._en_ui(data["prog_bar"].configure, progress_color="#FF0000")
                        self._en_ui(data["btn_pause"].configure, state="disabled")
                    else:
                        raise Exception("No se pudo verificar el archivo final.")
                else:
                    if os.path.exists(final_path):
                         data["status"] = "finished"
                         _estado("✅ Terminado", "#2ECC71")
                    else:
                         raise Exception("Error: Archivo no generado.")

        except Exception as e:
            # Ya no está bajando: el turno se libera cuanto antes
            self._yt_soltar_turno(turno)

            # Se pausó y se reanudó mientras este hilo seguía: la tarea ya es de
            # otro hilo, que usa la misma carpeta temporal. Este sale sin tocar nada.
            if not self._yt_hilo_vigente(data, hilo):
                thread_keeping_files = True
                return

            # CHEQUEO DE ESTADO (PAUSA / CANCELACIÓN)
            if data["status"] in ["paused", "cancelled", "skipped"]:

                # --- FIX BUG 1: ACTIVAR BANDERA DE PROTECCIÓN ---
                if data["status"] == "paused":
                    thread_keeping_files = True
                return

            err_txt = str(e)
            print(f"DEBUG ERROR: {err_txt}")

            # ── Clasificación de errores de descarga ────────────────────────
            _err_low = err_txt.lower()

            # Errores de autenticación/bot — YouTube bloquea sin importar la
            # versión de yt-dlp. Ninguna actualización puede resolver esto.
            _BOT_HINTS = ["sign in to confirm", "confirm you're not a bot"]

            # Señales que indican GENUINAMENTE que yt-dlp está desactualizado
            # (firma de extracción rota, mensaje explícito de PyPI/YouTube).
            _UPDATE_HINTS = [
                "nsig extraction failed",
                "please update",
                "is outdated",
            ]

            if any(h in _err_low for h in _BOT_HINTS):
                # Error de bot-detection: informar sin intentar actualizar
                _estado("❌ YouTube bloqueó — se requieren cookies", "#ff7f00")

            elif any(h in _err_low for h in _UPDATE_HINTS):
                # ── yt-dlp genuinamente desactualizado: actualizar y reintentar ──
                # Solo se intenta UNA vez. Si el reintento también falla, el error
                # posterior caerá en los elif/else de abajo como error normal.
                if data.get("_yt_retry_count", 0) == 0:
                    data["_yt_retry_count"] = 1

                    # Informar en el widget del video
                    _estado("🔄 Actualizando yt-dlp...", "gray")

                    # Actualizar de forma BLOQUEANTE — ya estamos en hilo secundario,
                    # exactamente igual a lo que hace el botón manual pero sin el
                    # threading.Thread extra (innecesario aquí).
                    # Si otra descarga ya lanzó la actualización, esperamos a que
                    # termine antes de reintentar.
                    if getattr(self, '_yt_updating', False):
                        while getattr(self, '_yt_updating', False):
                            time.sleep(0.5)
                    else:
                        # Misma función, mismos widgets que usa el botón manual.
                        # force=False: si ya es la última versión, no reinstala.
                        self._yt_do_update(self.yt_upd_lbl, self.yt_upd_btn, False)

                    # Señalizar reintento en el widget del video
                    _estado("🔁 Reintentando...", "yellow")
                    data["status"] = "active"

                    # Proteger temp_dir para que el finally no lo elimine mientras
                    # el reintento ya arrancó (usa la misma ruta de temp).
                    thread_keeping_files = True

                    # Relanzar con la misma configuración guardada en data["cfg_*"].
                    # El hilo nuevo queda registrado como el dueño de la tarea.
                    t = threading.Thread(
                        target=self.run_single_yt_download,
                        args=(task_id,),
                        daemon=True
                    )
                    data["thread"] = t
                    t.start()
                    return  # finally corre pero no limpia (thread_keeping_files=True)
                else:
                    # Ya se intentó actualizar antes y sigue fallando → error real
                    short_err = err_txt[:40] + "..." if len(err_txt) > 40 else err_txt
                    _estado(f"❌ Error tras actualizar: {short_err}", "red")

            elif "getaddrinfo failed" in err_txt or "11001" in err_txt:
                 _estado("❌ Sin Internet (DNS)", "red")
            elif "timed out" in err_txt.lower() or "transport error" in err_txt.lower():
                 _estado("❌ Conexión inestable", "red")
            elif "is not a valid URL" in err_txt or "Unsupported URL" in err_txt:
                 _estado("❌ URL no válida", "red")
            else:
                 short_err = err_txt[:30] + "..." if len(err_txt) > 30 else err_txt
                 _estado(f"❌ Error: {short_err}", "red")

            data["status"] = "error"

        finally:
            self._yt_soltar_turno(turno)
            # --- FIX BUG 1: USAR LA BANDERA LOCAL 'thread_keeping_files' ---
            # Si esta variable es True, significa que ESTE HILO ESPECÍFICO fue pausado.
            # No importa si el usuario ya le dio a 'Reanudar' (y cambió data["status"] a 'active'),
            # este hilo viejo respetará los archivos y no los borrará.
            if not thread_keeping_files:
                if os.path.exists(temp_dir):
                    try: shutil.rmtree(temp_dir, ignore_errors=True)
                    except: pass

                if hasattr(self, 'yt_active_temps') and temp_dir in self.yt_active_temps:
                    try: self.yt_active_temps.remove(temp_dir)
                    except: pass

            self.update_global_progress()

    # =========================================================================
    # HELPERS DE METADATOS
    # =========================================================================

    @staticmethod
    def _yt_release_year(info, is_music):
        """
        Año correcto según tipo de contenido.
        - Música: release_year → release_date[:4] → vacío (NO usar upload_date)
        - Video:  release_year → release_date[:4] → upload_date[:4]
        """
        year = (
            str(info.get('release_year') or '')[:4]
            or (info.get('release_date') or '')[:4]
        )
        if not year and not is_music:
            year = (info.get('upload_date') or '')[:4]
        return year

    @staticmethod
    def _yt_get_best_thumb(info, is_music=False):
        """
        Selección de thumbnail:
        - YouTube Music (is_music=True): se mantiene la cuadrada (carátula de
          álbum) igual que antes — ahí sí es la miniatura "oficial" correcta.
        - Cualquier otro tipo de descarga: la miniatura oficial que el propio
          extractor de yt-dlp ya resolvió como la mejor (info['thumbnail']),
          sin heurística de cuadrada ni recortes.
        """
        thumbs = info.get('thumbnails') or []

        if is_music:
            def _score(t):
                w, h = t.get('width'), t.get('height')
                if w and h:
                    return (abs(w / h - 1.0), -w)
                # Sin width/height: buscar una pista de tamaño en la propia
                # URL (típico de googleusercontent.com: "=wN-hN"/"-wN-hN",
                # usado para carátulas de álbum de YouTube Music). Si N
                # coincide en ambos, es cuadrada.
                m = re.search(r'[=-]w(\d+)-h(\d+)', t.get('url', ''))
                if m and m.group(1) == m.group(2):
                    return (0.0, -int(m.group(1)))
                return (999.0, 0)  # sin ninguna pista de tamaño

            candidatos = [t for t in thumbs if t.get('url')]
            if candidatos:
                mejor = min(candidatos, key=_score)
                return mejor['url']

        # Miniatura oficial ya resuelta por el propio extractor de yt-dlp
        oficial = info.get('thumbnail')
        if oficial:
            return oficial

        # Fallback si por lo que sea no viene 'thumbnail': mayor resolución disponible
        valid = [t for t in thumbs if t.get('url')]
        if valid:
            return max(
                valid,
                key=lambda t: (t.get('width') or 0) * (t.get('height') or 0)
            )['url']

        return ''

    def _yt_build_meta(self, info, fallback_title='', url=''):
        """
        Construye el dict yt_meta.
        is_music = True si el video es de YouTube/YouTube Music (por
        extractor o por URL de music.youtube.com) Y yt-dlp encontró campos
        de música (track/artist). El chequeo del extractor es necesario:
        TikTok también rellena 'track'/'artist' con el audio de fondo del
        video (no es una canción "descargable" en ese sentido), así que sin
        esto se activaba el recorte cuadrado de portada también ahí,
        deformando una miniatura que en TikTok debe quedar tal cual.
        """
        _extractor = (info.get('extractor_key') or info.get('extractor') or '').lower()
        _es_youtube = 'youtube' in _extractor

        _urls = (url or '', info.get('webpage_url') or '', info.get('original_url') or '')
        is_music = _es_youtube and (
            bool(info.get('track') or info.get('artist')) or
            any('music.youtube.com' in u for u in _urls)
        )
        year      = self._yt_release_year(info, is_music)
        thumb_url = self._yt_get_best_thumb(info, is_music)

        if is_music:
            return {
                'title':      info.get('track') or info.get('title', ''),
                'artist':     info.get('artist') or info.get('uploader', ''),
                'album':      info.get('album', ''),
                'track':      str(info.get('track_number') or ''),
                'date':       year,
                '_thumbnail': thumb_url,
                '_is_music':  True,
            }
        else:
            return {
                'title':      fallback_title or info.get('title', ''),
                'artist':     info.get('uploader') or info.get('channel', ''),
                'date':       year,
                '_thumbnail': thumb_url,
                '_is_music':  False,
            }

    def _yt_download_thumb(self, thumb_url, dest_path, crop_square=False):
        """
        Descarga la thumbnail y la deja como JPEG real en dest_path, usando
        el propio mecanismo de red de yt-dlp (headers, impersonation, proxy,
        etc.) en vez de una petición manual aparte.

        La URL "oficial" casi nunca es un .jpg de verdad — YouTube/TikTok/etc.
        suelen servirla en WebP (o algo genérico sin extensión clara), así
        que se normaliza con ffmpeg sin importar el formato real de origen
        (mismo criterio que usa yt-dlp internamente con su propio
        FFmpegThumbnailsConvertor). Sin este paso, ffmpeg detecta el formato
        real al leerla y el muxer rechaza el mux por "codec no soportado en
        el contenedor" aunque el archivo se llame .jpg.

        crop_square=True (YouTube Music): recorta al centro dejándola
        cuadrada, que es como debe verse una carátula de álbum. Para esos
        videos YouTube normalmente NO entrega ninguna miniatura cuadrada en
        la lista de candidatas —todas son 16:9—, así que la única forma de
        obtener la carátula cuadrada es recortarla nosotros.
        """
        global yt_dlp
        raw_path = dest_path + ".raw"
        ok_download = False
        try:
            _mod = yt_dlp
            if _mod is None:
                import importlib as _il
                _mod = _il.import_module("yt_dlp")
                yt_dlp = _mod
            opts = {'quiet': True, 'no_warnings': True}
            opts.update(_yt_opts_robustos())
            with _mod.YoutubeDL(opts) as _ydl:
                data = _ydl.urlopen(thumb_url).read()
            with open(raw_path, 'wb') as f:
                f.write(data)
            ok_download = True
        except Exception as e:
            print(f"[Thumb] Error descargando (nativo yt-dlp): {e}")
            # Respaldo no crítico: si el mecanismo nativo falla por lo que
            # sea, se intenta una vez con urllib para no perder la carátula.
            try:
                import urllib.request as _ureq
                _ureq.urlretrieve(thumb_url, raw_path)
                ok_download = True
            except Exception as e2:
                print(f"[Thumb] Error descargando (fallback urllib): {e2}")

        if not ok_download:
            return False

        try:
            cmd = ["ffmpeg", "-y", "-i", raw_path]
            if crop_square:
                # Recorte centrado al lado más corto -> carátula cuadrada
                cmd.extend(["-vf", "crop='min(iw,ih)':'min(iw,ih)'"])
            cmd.extend(["-frames:v", "1", dest_path])
            subprocess.run(
                cmd,
                startupinfo=self.get_startup_info(),
                check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
            )
            return True
        except Exception as e:
            print(f"[Thumb] Error normalizando a JPEG: {e}")
            return False
        finally:
            try: os.remove(raw_path)
            except Exception: pass

    # =========================================================================
    # FIN HELPERS DE METADATOS
    # =========================================================================

    def _yt_convertir_meta_caratula(self, *, temp_dir, final_path, ext_final,
                                     mode, container, audio_mode,
                                     embed_meta, yt_meta, data,
                                     should_abort, on_tick=None, on_thumb_start=None):
        """
        Paso compartido entre la descarga individual y cada item de playlist:
          1) localiza el archivo recién descargado en temp_dir,
          2) arma el comando ffmpeg — copiando los streams que ya sean
             compatibles con el contenedor pedido en vez de recodificar
             (mismo criterio que ya se usaba para M4A, ahora también para
             el audio del modo Video cuando el contenedor es MP4),
          3) lo corre reportando avance vía on_tick(frac, is_copy_only),
          4) incrusta la carátula si corresponde (no-fatal si falla).

        should_abort(): sin argumentos, True si hay que matar el ffmpeg en
            curso. Cada llamador pasa su propia condición de pausa/cancelación
            para no cambiar el comportamiento que ya tenía cada uno.
        on_tick(frac, is_copy_only): opcional; cada llamador decide qué
            widgets actualiza con ese avance (el modo individual también
            cambia el texto de estado; el de playlist solo mueve la barra,
            igual que antes).

        Devuelve True si el archivo final quedó listo, False si se abortó a
        media conversión.

        El archivo se arma DENTRO de temp_dir y solo se mueve a final_path
        cuando está completo (conversión + carátula). Así, si se cancela a
        medias, en la carpeta de destino nunca queda un archivo corrupto: lo
        incompleto se borra junto con temp_dir.
        """
        temp_files = [f for f in os.listdir(temp_dir)
                      if os.path.isfile(os.path.join(temp_dir, f))
                      and not f.endswith(('.part', '.ytdl', '.json'))
                      and not f.startswith(('_dmt_', '_cover'))]
        if not temp_files:
            raise Exception("Error interno: Archivo no encontrado.")
        temp_files.sort(key=lambda f: os.path.getsize(os.path.join(temp_dir, f)), reverse=True)
        temp_input = os.path.join(temp_dir, temp_files[0])

        # Detectar Codec de audio de la fuente
        src_codec = "unknown"
        try:
            cmd_probe = ["ffprobe", "-v", "error", "-select_streams", "a:0", "-show_entries",
                         "stream=codec_name", "-of", "default=noprint_wrappers=1:nokey=1", temp_input]
            src_codec = subprocess.check_output(
                cmd_probe, startupinfo=self.get_startup_info()
            ).decode().strip().lower()
        except Exception:
            pass

        dur = self.get_duration(temp_input)
        if not dur or dur <= 0: dur = 1

        # Construir Comando FFMPEG
        cmd = ["ffmpeg", "-y", "-i", temp_input]

        if mode == "Audio":
            cmd.append("-vn")

            # ── MP3 ──────────────────────────────────────────────────
            if container == "MP3":
                if audio_mode == "original":
                    cmd.extend(["-acodec", "libmp3lame", "-q:a", "2"])
                elif audio_mode == "optimized":
                    cmd.extend(["-acodec", "libmp3lame", "-q:a", "4"])
                elif audio_mode == "standard":
                    cmd.extend(["-acodec", "libmp3lame", "-q:a", "5"])
                else:  # light
                    cmd.extend(["-acodec", "libmp3lame", "-b:a", "64k", "-ar", "22050", "-ac", "1"])

            # ── M4A (AAC) ─────────────────────────────────────────────
            elif container == "M4A":
                if audio_mode in ("original", "optimized") and "aac" in src_codec:
                    cmd.extend(["-acodec", "copy"])
                elif audio_mode == "original":
                    src_kbps = self.get_audio_bitrate(temp_input)
                    if   src_kbps <= 192: final_br = "192k"
                    elif src_kbps <= 256: final_br = "256k"
                    else:                 final_br = "320k"
                    cmd.extend(["-c:a", "aac", "-b:a", final_br])
                elif audio_mode == "optimized":
                    cmd.extend(["-c:a", "aac", "-b:a", "192k"])
                elif audio_mode == "standard":
                    cmd.extend(["-c:a", "aac", "-b:a", "128k"])
                else:  # light
                    cmd.extend(["-c:a", "aac", "-b:a", "64k", "-ar", "22050", "-ac", "1"])

            # ── OPUS ──────────────────────────────────────────────────
            elif container == "OPUS":
                if audio_mode in ("original", "optimized") and "opus" in src_codec:
                    cmd.extend(["-acodec", "copy"])
                elif audio_mode in ("original", "optimized"):
                    cmd.extend(["-acodec", "libopus", "-b:a", "128k"])
                elif audio_mode == "standard":
                    cmd.extend(["-acodec", "libopus", "-b:a", "96k"])
                else:  # light
                    cmd.extend(["-acodec", "libopus", "-b:a", "32k", "-ac", "1"])

            # ── WAV — lossless ─────────────────────────────────────────
            elif container == "WAV":
                cmd.extend(["-acodec", "pcm_s16le"])

            # ── Fallback ────────────────────────────────────────────────
            else:
                cmd.extend(["-acodec", "libmp3lame", "-q:a", "2"])
        else:
            if container == "MP4":
                if "aac" in src_codec:
                    # Fuente de audio ya es AAC → copiar en vez de recodificar
                    # (mismo criterio que ya se usaba para M4A). El bitstream
                    # filter es el mismo que ffmpeg aplica solo cuando hace
                    # falta; ponerlo explícito no rompe nada si el audio ya
                    # viene en formato MPEG-4 ASC.
                    cmd.extend(["-c:v", "copy", "-c:a", "copy", "-bsf:a", "aac_adtstoasc"])
                else:
                    cmd.extend(["-c:v", "copy", "-c:a", "aac", "-b:a", "192k"])
            else:
                cmd.extend(["-c", "copy"])

        # --- METADATOS DE TEXTO (título, artista, año, etc.) ---
        if embed_meta and yt_meta:
            for _mk, _mv in yt_meta.items():
                if not _mk.startswith('_') and _mv:  # '_thumbnail' se salta aquí
                    cmd.extend(['-metadata', f'{_mk}={_mv}'])

        tmp_out = os.path.join(temp_dir, f"_dmt_salida.{ext_final}")
        cmd.append(tmp_out)
        is_copy_only = "copy" in cmd

        def _borrar(*rutas):
            for _r in rutas:
                try:
                    if _r and os.path.exists(_r):
                        os.remove(_r)
                except OSError:
                    pass

        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True,
            encoding='utf-8',
            errors='ignore',
            startupinfo=self.get_startup_info()
        )
        data["process_handle"] = process

        aborted = False
        ultimas = []
        for line in process.stdout:
            if should_abort():
                process.kill()
                aborted = True
                break

            if line.strip():
                ultimas.append(line.strip())
                del ultimas[:-12]
            tm = re.search(r"time=(\d+):(\d+):(\d+\.\d+)", line)
            if tm:
                h, m, s = tm.groups()
                sec = int(h) * 3600 + int(m) * 60 + float(s)
                frac = min(1.0, sec / dur)
                if on_tick:
                    on_tick(frac, is_copy_only)

        process.wait()
        data["process_handle"] = None

        # --- CANCELADO A MEDIA CONVERSIÓN: se descarta lo incompleto ---
        if aborted or should_abort():
            _borrar(tmp_out)
            return False
        if process.returncode != 0 or not os.path.exists(tmp_out):
            _borrar(tmp_out)
            raise Exception(f"FFmpeg falló: {self._vid_linea_error(ultimas)[:60]}")

        # --- INCRUSTAR CARÁTULA (paso separado, no-fatal) ---
        if embed_meta and yt_meta and yt_meta.get('_thumbnail'):
            thumb_path = os.path.join(temp_dir, "_cover.jpg")
            thumb_tmp  = os.path.join(temp_dir, f"_dmt_cover.{ext_final}")
            try:
                if on_thumb_start:
                    try: on_thumb_start()
                    except Exception: pass

                if not self._yt_download_thumb(
                        yt_meta['_thumbnail'], thumb_path,
                        crop_square=bool(yt_meta.get('_is_music'))):
                    raise ValueError("No se pudo descargar la thumbnail")

                if ext_final == "opus":
                    # OGG/Opus no usa el mecanismo de "attached_pic" de
                    # ffmpeg -map/-disposition (eso es específico de
                    # mp4/mov/m4a) — el estándar para Ogg/Opus es
                    # METADATA_BLOCK_PICTURE (Vorbis Comments), vía mutagen.
                    import base64
                    from mutagen.oggopus import OggOpus
                    from mutagen.flac import Picture
                    with open(thumb_path, 'rb') as _imf:
                        img_bytes = _imf.read()
                    pic = Picture()
                    pic.type = 3
                    pic.mime = "image/jpeg"
                    pic.data = img_bytes
                    tags = OggOpus(tmp_out)
                    tags["metadata_block_picture"] = [base64.b64encode(pic.write()).decode("ascii")]
                    tags.save()

                else:
                    tc = ["ffmpeg", "-y", "-i", tmp_out, "-i", thumb_path]
                    if ext_final == "mp3":
                        tc.extend([
                            "-map", "0:0", "-map", "1:0",
                            "-c", "copy",
                            "-id3v2_version", "3",
                            "-metadata:s:v", "title=Album cover",
                            "-metadata:s:v", "comment=Cover (front)"
                        ])
                    elif ext_final == "m4a":
                        tc.extend([
                            "-map", "0:a", "-map", "1:v",
                            "-c", "copy",
                            "-disposition:v:0", "attached_pic"
                        ])
                    elif ext_final == "mp4":
                        tc.extend([
                            "-map", "0", "-map", "1",
                            "-c", "copy",
                            "-disposition:v:1", "attached_pic"
                        ])
                    else:
                        raise ValueError(f"Carátula no soportada para .{ext_final}")

                    tc.append(thumb_tmp)
                    # Con process_handle, "Cancelar" también detiene este paso
                    proc_cover = subprocess.Popen(
                        tc,
                        startupinfo=self.get_startup_info(),
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL
                    )
                    data["process_handle"] = proc_cover
                    try:
                        rc_cover = proc_cover.wait()
                    finally:
                        data["process_handle"] = None
                    if rc_cover != 0:
                        raise RuntimeError(f"FFmpeg código {rc_cover}")
                    os.replace(thumb_tmp, tmp_out)

            except Exception as _te:
                if not should_abort():
                    print(f"[Metadatos] Carátula omitida (no fatal): {str(_te)[:120]}")
                _borrar(thumb_path, thumb_tmp)

        # Cancelado mientras se incrustaba la carátula: no se entrega nada
        if should_abort():
            _borrar(tmp_out)
            return False

        # --- ENTREGA: el archivo aparece en el destino ya completo ---
        ultimo_err = None
        for _ in range(10):
            try:
                os.replace(tmp_out, final_path)     # misma unidad: instantáneo
                return True
            except OSError as _me:
                ultimo_err = _me
                time.sleep(0.5)                     # p. ej. destino abierto en un reproductor
        try:
            shutil.move(tmp_out, final_path)        # respaldo (otra unidad)
            return True
        except Exception as _me:
            ultimo_err = _me
        _borrar(tmp_out)
        raise Exception(f"No se pudo guardar el archivo final: {ultimo_err}")

    # =========================================================================
    # PLAYLIST: ORQUESTADOR + DESCARGA INDIVIDUAL
    # =========================================================================

    def run_playlist_yt_download(self, task_id, entries, pl_title_raw,
                                  mode, quality, container, save_folder,
                                  embed_meta, audio_mode, limit_height,
                                  ydl_opts_base):
        """
        Maneja la descarga completa de una playlist.
        Corre dentro del hilo daemon iniciado por add_yt_to_queue. Cada video
        pide su propio turno en la cola de descargas (_yt_procesar_un_item).
        """
        CHECKPOINT_EVERY = 50   # Preguntar al usuario cada N videos completados
        data  = self.yt_downloads[task_id]
        total = len(entries)
        ext_final = container.lower()
        hilo = threading.current_thread()

        def _estado(texto, color):
            self._en_ui(data["lbl_status"].configure, text=texto, text_color=color)

        def _titulo(texto):
            self._en_ui(data["lbl_title"].configure, text=texto)

        # --- 1. LIMPIAR NOMBRE DE PLAYLIST ---
        forbidden_chars = '<>:"/\\|?*\n\r\t'
        safe_pl = pl_title_raw[:80]
        safe_pl = "".join([c for c in safe_pl if c not in forbidden_chars]).strip(". ")
        if not safe_pl: safe_pl = f"Playlist_{task_id[:8]}"

        # --- 2. POPUP INICIAL (se muestra en el hilo de la interfaz; este hilo espera) ---
        confirm = self._en_ui_espera(
            messagebox.askyesno,
            "Playlist detectada",
            f"Se detectó una playlist de {total} video(s):\n\n"
            f"\"{pl_title_raw[:80]}\"\n\n"
            f"Los archivos se guardarán en una subcarpeta.\n"
            f"¿Deseas continuar con la descarga?"
        )
        if not confirm:
            data["status"] = "finished"
            _estado("Cancelado por usuario.", "orange")
            self._en_ui(data["btn_pause"].configure, state="disabled")
            self.update_global_progress()
            return

        # --- 3. CREAR SUBCARPETA ---
        pl_folder = os.path.join(save_folder, safe_pl)
        os.makedirs(pl_folder, exist_ok=True)

        # --- 4. ACTUALIZAR UI ---
        _titulo(f"📋 {safe_pl}  (0/{total})")
        self._en_ui(data["prog_bar"].set, 0)
        self._en_ui(data["prog_bar"].configure, progress_color="#FF0000")

        # --- 5. LOOP DE DESCARGA ---
        done_count  = 0
        total_bytes = 0

        for i, entry in enumerate(entries):

            # Se pausó y se reanudó en otro hilo: ese sigue la playlist, este sale
            if not self._yt_hilo_vigente(data, hilo):
                return

            # Chequeo de cancelación antes de cada item
            if data["status"] in ["cancelled", "paused"] or data["cancel_flag"]:
                _estado(f"⛔ Detenido en {done_count}/{total}", "orange")
                break

            # Construir URL del item
            item_url = (entry.get('webpage_url')
                        or entry.get('url')
                        or (f"https://www.youtube.com/watch?v={entry['id']}"
                            if entry.get('id') else None))
            if not item_url:
                print(f"[Playlist] Item {i+1} sin URL, omitiendo.")
                continue

            item_title_raw = entry.get('title') or f"Video_{i+1}"
            short = item_title_raw[:45] + "..." if len(item_title_raw) > 45 else item_title_raw

            # Actualizar UI con video actual
            texto_item = f"({i+1}/{total}) {short}"
            _estado(texto_item, "white")
            _titulo(f"📋 {safe_pl}  ({i+1}/{total})")

            # Descargar + convertir + metadata el item
            item_path = self._yt_procesar_un_item(
                task_id        = task_id,
                item_url       = item_url,
                item_title_raw = item_title_raw,
                item_index     = i + 1,
                pl_folder      = pl_folder,
                mode           = mode,
                container      = container,
                embed_meta     = embed_meta,
                audio_mode     = audio_mode,
                limit_height   = limit_height,
                ydl_opts_base  = ydl_opts_base,
                texto_estado   = texto_item,
            )

            if not self._yt_hilo_vigente(data, hilo):
                return

            # Acumular tamaño y conteo
            if item_path and os.path.exists(item_path):
                total_bytes += os.path.getsize(item_path)
                done_count  += 1

            # Barra de progreso: avance general de la playlist
            self._en_ui(data["prog_bar"].set, (i + 1) / total)
            self.update_global_progress()

            # --- CHECKPOINT PERIÓDICO ---
            if done_count > 0 and done_count % CHECKPOINT_EVERY == 0 and (i + 1) < total:
                remaining = total - (i + 1)
                size_mb  = total_bytes / (1024 * 1024)
                size_str = (f"{size_mb:.1f} MB" if size_mb < 1024
                            else f"{size_mb / 1024:.2f} GB")

                cont = self._en_ui_espera(
                    messagebox.askyesno,
                    "Continuar playlist",
                    f"Van {done_count} videos descargados\n"
                    f"Ocupando aproximadamente {size_str}\n"
                    f"Quedan {remaining} video(s).\n\n"
                    f"¿Deseas continuar con la descarga?"
                )
                if not cont:
                    data["status"] = "finished"
                    _estado(f"⏹ Detenido por usuario ({done_count}/{total})", "orange")
                    self._en_ui(data["btn_pause"].configure, state="disabled")
                    self.update_global_progress()
                    return

            # --- ESPERA ENTRE ITEMS (menos probabilidad de bloqueos anti-bot) ---
            if (i + 1) < total:
                _esperar_entre_items(
                    random.uniform(2, 5),
                    lambda: (data.get("cancel_flag") or data.get("status") in ("cancelled", "paused")
                             or not self._yt_hilo_vigente(data, hilo)),
                    on_tick=lambda s: _estado(f"⏳ Esperando {s}s antes del siguiente...", "#888")
                )

        # --- 6. FINALIZACIÓN ---
        if data["status"] not in ["cancelled", "paused"] and self._yt_hilo_vigente(data, hilo):
            size_mb  = total_bytes / (1024 * 1024)
            size_str = (f"{size_mb:.1f} MB" if size_mb < 1024
                        else f"{size_mb / 1024:.2f} GB")
            data["status"] = "finished"
            self._en_ui(data["prog_bar"].set, 1.0)
            _estado(f"✅ {done_count}/{total} videos  ({size_str})", "#2ecc71")
            _titulo(f"📋 {safe_pl}  ({done_count}/{total})")
            self._en_ui(data["btn_pause"].configure, state="disabled")

        self.update_global_progress()

    # -------------------------------------------------------------------------

    def _yt_procesar_un_item(self, task_id, item_url, item_title_raw, item_index,
                              pl_folder, mode, container, embed_meta,
                              audio_mode, limit_height, ydl_opts_base, texto_estado=None):
        """
        Descarga, convierte e incrusta metadatos de un único item de playlist.
        Devuelve la ruta del archivo final terminado, o None si falló/se canceló.
        Antes de bajar espera su turno en la cola de descargas y lo suelta al
        terminar de bajar: la conversión no frena a las demás descargas.
        """
        data      = self.yt_downloads[task_id]
        ext_final = container.lower()
        forbidden_chars = '<>:"/\\|?*\n\r\t'

        # Limpiar título del item
        safe_title = item_title_raw[:100]
        safe_title = "".join([c for c in safe_title if c not in forbidden_chars]).strip(". ")
        if not safe_title: safe_title = f"Item_{item_index}"

        final_filename = f"{safe_title}.{ext_final}"
        final_path = os.path.join(pl_folder, final_filename)
        temp_dir   = os.path.join(pl_folder, f"_tmp_{task_id[:8]}_{item_index}")
        os.makedirs(temp_dir, exist_ok=True)

        turno = None
        try:
            # --- COLA: turno para bajar (máximo YT_MAX_DESCARGAS a la vez) ---
            turno = self._yt_tomar_turno(data, texto_estado)

            # --- A. OBTENER METADATOS DEL ITEM (solo si embed_meta activado) ---
            yt_meta = {}
            if embed_meta:
                try:
                    meta_opts = {'quiet': True, 'no_warnings': True, 'socket_timeout': 15}
                    meta_opts.update(_yt_opts_robustos())
                    with yt_dlp.YoutubeDL(meta_opts) as ydl_m:
                        full_info = ydl_m.extract_info(item_url, download=False)
                    yt_meta = self._yt_build_meta(full_info, item_title_raw, item_url)
                except Exception as me:
                    print(f"[Playlist] Metadatos no obtenidos (item {item_index}): {me}")

            # --- B. SALTAR SI YA EXISTE ---
            if os.path.exists(final_path) and os.path.getsize(final_path) > 0:
                print(f"[Playlist] Ya existe, saltando: {final_filename}")
                return final_path

            # --- C. DESCARGAR CON yt-dlp ---
            ydl_opts = dict(ydl_opts_base)
            ydl_opts['outtmpl']    = os.path.join(temp_dir, f"{safe_title}.%(ext)s")
            ydl_opts['noplaylist'] = True   # Forzar descarga individual
            ydl_opts.update(_yt_opts_robustos())
            ydl_opts.update(_yt_opts_diagnostico())

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([item_url])

            # Ya bajó: el turno queda libre mientras este convierte / empaqueta
            self._yt_soltar_turno(turno)

            if data["status"] in ["cancelled"] or data["cancel_flag"]:
                return None

            # --- D-G. CONVERTIR/REMUXEAR + METADATA + CARÁTULA ---
            # (helper compartido con la descarga individual: mismo armado de
            # comando ffmpeg, mismo criterio de "copiar si ya es compatible")
            def _item_should_abort():
                return data["status"] in ["cancelled"] or data["cancel_flag"]

            def _item_on_tick(frac, is_copy_only):
                self._en_ui(data["prog_bar"].set, frac)

            self._yt_convertir_meta_caratula(
                temp_dir=temp_dir, final_path=final_path, ext_final=ext_final,
                mode=mode, container=container, audio_mode=audio_mode,
                embed_meta=embed_meta, yt_meta=yt_meta, data=data,
                should_abort=_item_should_abort, on_tick=_item_on_tick,
            )

            return final_path if os.path.exists(final_path) else None

        except Exception as e:
            print(f"[Playlist] Error en item {item_index} ({item_title_raw[:40]}): {e}")
            return None

        finally:
            self._yt_soltar_turno(turno)
            # Limpiar carpeta temporal del item siempre
            try: shutil.rmtree(temp_dir, ignore_errors=True)
            except: pass

    # =========================================================================
    # FIN PLAYLIST
    # =========================================================================

    # --- LOGICA DE DECISIÓN Y UI ---
    def wait_for_decision(self, task_id, temp_dir):
        data = self.yt_downloads[task_id]
        while data["user_response"] is None:
            if data["cancel_flag"]:
                shutil.rmtree(temp_dir, ignore_errors=True)
                return False
            time.sleep(0.5)

        if data["user_response"] == "no":
            data["status"] = "finished" # Finalizado sin error

            def _saltado():
                data["lbl_status"].configure(text="Saltado por usuario.", text_color="orange")
                # OCULTAR BOTONES DE DECISIÓN AL SALTAR
                data["decision_frame"].pack_forget()
                data["prog_row"].pack(fill="x", padx=10, pady=(0,10))
            self._en_ui(_saltado)

            shutil.rmtree(temp_dir, ignore_errors=True)
            return False
        return True

    def mark_as_skipped(self, data, msg):
        data["status"] = "skipped"  # Marcar como omitido (el hilo lo lee enseguida)
        self._en_ui(data["lbl_status"].configure, text=msg, text_color="#f39c12")
        self._en_ui(data["prog_bar"].set, 1)
        self.update_global_progress()  # Actualizar progreso general sin este item

    def ask_user_overwrite(self, task_id, msg):
        data = self.yt_downloads[task_id]
        data["user_response"] = None   # una respuesta vieja (antes de pausar) no vale

        def _mostrar():
            data["prog_row"].pack_forget()
            f = data["decision_frame"]
            f.pack(fill="x", padx=10, pady=5)
            for w in f.winfo_children(): w.destroy()

            ctk.CTkLabel(f, text=msg, text_color="yellow", font=("Arial", 11, "bold")).pack(side="left", padx=5)
            ctk.CTkButton(f, text="Sí", width=50, height=25, fg_color="#27ae60",
                          command=lambda: self.set_user_response(task_id, "yes")).pack(side="right", padx=2)
            ctk.CTkButton(f, text="No", width=50, height=25, fg_color="#c0392b",
                          command=lambda: self.set_user_response(task_id, "no")).pack(side="right", padx=2)
        self._en_ui(_mostrar)

    def set_user_response(self, task_id, response):
        self.yt_downloads[task_id]["user_response"] = response

    def restore_ui_after_decision(self, task_id):
        data = self.yt_downloads[task_id]

        def _restaurar():
            data["decision_frame"].pack_forget()
            data["prog_row"].pack(fill="x", padx=10, pady=(0,10))
            data["lbl_status"].configure(text="Descargando...", text_color="white")
        self._en_ui(_restaurar)

    def toggle_pause_yt(self, task_id):
        if task_id not in self.yt_downloads: return
        data = self.yt_downloads[task_id]
        if data["status"] == "active":
            data["status"] = "paused"
            data["cancel_flag"] = True
            # Por la cola de la interfaz: así queda DESPUÉS de cualquier "Bajando: X%"
            # que el hilo de descarga haya dejado pendiente y no lo pisa
            self._en_ui(data["lbl_status"].configure, text="Pausado", text_color="orange")
            data["btn_pause"].configure(text="▶", fg_color="#27AE60", hover_color="#2ECC71")
            self._yt_despertar_cola()   # si estaba en cola, sale de la fila ya
        elif data["status"] == "paused":
            data["status"] = "active"
            data["cancel_flag"] = False
            data["lbl_status"].configure(text="Reanudando...", text_color="yellow")
            data["btn_pause"].configure(text="⏸", fg_color="#F39C12", hover_color="#D35400")
            target_fn = self.run_spotify_download if data.get("es_spotify") else self.run_single_yt_download
            t = threading.Thread(target=target_fn, args=(task_id,))
            self.yt_downloads[task_id]["thread"] = t
            t.start()

    def cancel_single_yt(self, task_id):
        if task_id in self.yt_downloads:
            data = self.yt_downloads[task_id]
            data["status"] = "cancelled"
            data["cancel_flag"] = True
            data["lbl_status"].configure(text="Cancelado", text_color="red")

            # NUEVO: Matar el proceso específico de esta tarea si existe
            if "process_handle" in data and data["process_handle"]:
                try:
                    data["process_handle"].kill()
                except:
                    pass

            data["frame"].pack_forget() # Ocultar
            self._yt_despertar_cola()   # si estaba en cola, deja su lugar ya
            self.update_global_progress()

    def cancel_all_yt(self):
        for task_id in list(self.yt_downloads.keys()):
            self.cancel_single_yt(task_id)

    def hook_yt_progress(self, d, task_id, hilo=None):
        data = self.yt_downloads.get(task_id)
        if not data: return
        # Pausada/cancelada, o reanudada en otro hilo: esta descarga se corta
        if (data["cancel_flag"] or data["status"] in ["paused", "cancelled"]
                or (hilo is not None and not self._yt_hilo_vigente(data, hilo))):
            raise Exception("Detenido por usuario")

        if d['status'] == 'downloading':
            total = d.get('total_bytes') or d.get('total_bytes_estimate')
            downloaded = d.get('downloaded_bytes', 0)
            if total:
                p = min(1.0, downloaded / total)
                pct = int(p * 100)
                # La interfaz solo se actualiza cuando cambia el porcentaje
                if pct != data.get("_ult_pct"):
                    data["_ult_pct"] = pct
                    self._en_ui(data["prog_bar"].set, p)
                    self._en_ui(data["lbl_status"].configure, text=f"Bajando: {pct}%", text_color="white")
                    if pct % 5 == 0: self.update_global_progress()

        elif d['status'] == 'finished':
            data["_ult_pct"] = None
            self._en_ui(data["lbl_status"].configure, text="Procesando...", text_color="#F39C12")
            self._en_ui(data["prog_bar"].set, 0.99)

    def update_global_progress(self):
        # Lee y mueve barras: solo en el hilo de la interfaz
        if threading.current_thread() is not threading.main_thread():
            self._en_ui(self.update_global_progress)
            return
        # Excluir cancelados y omitidos del cálculo de progreso general
        active_items = [v for v in self.yt_downloads.values() if v["status"] not in ["cancelled", "skipped"]]
        if not active_items:
            self.yt_global_prog.set(0)
            return
        total_prog = 0
        for item in active_items:
            total_prog += item["prog_bar"].get()
        avg = total_prog / len(active_items)
        self.yt_global_prog.set(avg)


    # ==============================================================================
    #   MOTOR DE VIRTUALIZACIÓN (SOLUCIÓN LAG Y TEARING)
    # ==============================================================================

    def init_row_pool(self, num_rows):
        """Crea un número fijo de widgets que reciclaremos."""
        self.ren_canvas.delete("all")
        self.visible_rows = []
        
        # Restaurar placeholder si está vacío
        if self.total_data_count == 0:
            self.on_virtual_resize(None) # Llama al recentrado
            return

        # --- CORRECCIÓN AQUÍ ---
        # Definimos la función local SIN 'self' como argumento,
        # ya que accede al 'self' del padre automáticamente.
        def _child_mousewheel_wrapper(event):
            try:
                self.on_virtual_mouse_wheel(event)
            except Exception:
                pass
            return "break"

        for i in range(num_rows):
            f = ctk.CTkFrame(self.ren_canvas, corner_radius=6, fg_color="#222", height=self.ROW_HEIGHT - 4)
            
            lbl_old = ctk.CTkLabel(f, text="", text_color="#aaa", anchor="e", font=("Arial", 11))
            lbl_arrow = ctk.CTkLabel(f, text="➜", text_color="#a29bfe", font=("Arial", 16))
            lbl_new = ctk.CTkLabel(f, text="", text_color="white", font=(self.main_font, 12, "bold"), anchor="w")
            
            f.grid_columnconfigure(0, weight=1)
            f.grid_columnconfigure(2, weight=1)
            lbl_old.grid(row=0, column=0, padx=10, sticky="ew")
            lbl_arrow.grid(row=0, column=1, padx=5)
            lbl_new.grid(row=0, column=2, padx=10, sticky="ew")
            
            # --- CORRECCIÓN AQUÍ ---
            # Usamos _child_mousewheel_wrapper directamente (sin self.)
            for w in [f, lbl_old, lbl_arrow, lbl_new]:
                w.bind("<Button-1>", self.on_virtual_row_click)
                w.bind("<MouseWheel>", _child_mousewheel_wrapper) # Windows
                w.bind("<Button-4>", _child_mousewheel_wrapper)   # Linux Up
                w.bind("<Button-5>", _child_mousewheel_wrapper)   # Linux Down

            
            win_id = self.ren_canvas.create_window(0, -100, window=f, anchor="nw", width=800, height=self.ROW_HEIGHT-4)
            
            row_data = {
                "id": win_id, "frame": f, "lbl_old": lbl_old, "lbl_new": lbl_new, "data_index": -1
            }
            f.virtual_ref = row_data
            lbl_old.virtual_ref = row_data
            lbl_arrow.virtual_ref = row_data
            lbl_new.virtual_ref = row_data
            
            self.visible_rows.append(row_data)

    def render_virtual_rows(self):
        """Renderizado con BUFFER (Pre-carga filas arriba y abajo para eliminar glitches)"""
        if not self.renamer_files: return

        # 1. Dimensiones
        canvas_h = self.ren_canvas.winfo_height()
        if canvas_h < 50: canvas_h = 500
        canvas_w = self.ren_canvas.winfo_width()
        
        total_pixels = len(self.renamer_files) * self.ROW_HEIGHT
        
        # 2. Configurar Scrollregion
        self.ren_canvas.configure(scrollregion=(0, 0, canvas_w, total_pixels))

        # 3. Obtener posición del scroll (Protegida)
        try:
            raw_top = self.ren_canvas.yview()[0]
            rel_top = max(0.0, min(1.0, raw_top)) # Clampeamos entre 0.0 y 1.0 estrictamente
        except: rel_top = 0.0

        # --- LÓGICA DEL BUFFER (TU SOLUCIÓN) ---
        BUFFER_ROWS = 15  # Cargamos 15 filas extra arriba y abajo
        
        # Índice donde EMPIEZA la pantalla visualmente
        visual_start_idx = int((rel_top * total_pixels) // self.ROW_HEIGHT)
        
        # Índice donde EMPEZAMOS A DIBUJAR (15 filas antes)
        draw_start_idx = max(0, visual_start_idx - BUFFER_ROWS)
        
        # Cuántas filas caben en la pantalla real
        rows_on_screen = int(canvas_h // self.ROW_HEIGHT) + 2
        
        # Tamaño total del pool necesario (Buffer Arriba + Pantalla + Buffer Abajo)
        total_needed = rows_on_screen + (BUFFER_ROWS * 2)
        
        # Expandir pool si la ventana es gigante o cambiamos el buffer
        if len(self.visible_rows) < total_needed:
            self.init_row_pool(total_needed)

        c_width = max(100, canvas_w - 4)

        # 4. BUCLE DE RENDERIZADO (Usando el pool extendido)
        for i, row_obj in enumerate(self.visible_rows):
            # El índice de datos real es: Donde empezamos a dibujar + el contador del pool
            data_idx = draw_start_idx + i
            
            # Solo dibujamos si el índice existe en los datos reales
            if 0 <= data_idx < len(self.renamer_files):
                item = self.renamer_files[data_idx]
                y_pos = data_idx * self.ROW_HEIGHT
                
                # Mover
                self.ren_canvas.coords(row_obj["id"], 2, y_pos + 2)
                self.ren_canvas.itemconfigure(row_obj["id"], width=c_width, state="normal")
                
                # Actualizar Textos (Solo si cambiaron para ahorrar CPU)
                current_old = row_obj["lbl_old"].cget("text")
                new_old_val = os.path.basename(item['path'])
                if current_old != new_old_val:
                    row_obj["lbl_old"].configure(text=new_old_val)

                current_new = row_obj["lbl_new"].cget("text")
                if current_new != item['new_name']:
                    row_obj["lbl_new"].configure(text=item['new_name'])
                # Nombre repetido en la misma carpeta: en rojo
                color_nuevo = "#ff5555" if item.get('dup') else "white"
                if row_obj.get("_color_nuevo") != color_nuevo:
                    row_obj["_color_nuevo"] = color_nuevo
                    row_obj["lbl_new"].configure(text_color=color_nuevo)

                row_obj["data_index"] = data_idx

                # Estilo Selección
                is_sel = (data_idx == self.renamer_selected_index)
                bg = "#4a2c5a" if is_sel else "#222"
                
                # Optimización de color (evita parpadeo)
                if row_obj["frame"].cget("fg_color") != bg:
                     row_obj["frame"].configure(fg_color=bg)
                     row_obj["frame"].configure(border_width=1 if is_sel else 0)
                     if is_sel: row_obj["frame"].configure(border_color="#a29bfe")

            else:
                # Si sobra pool (estamos al final de la lista), lo mandamos al infierno (-5000)
                # para que no estorbe visualmente
                self.ren_canvas.coords(row_obj["id"], 0, -5000)
                row_obj["data_index"] = -1

    def on_virtual_scroll_bar(self, *args):
        """Conecta Scrollbar -> Canvas"""
        self.ren_canvas.yview(*args)
        self.render_virtual_rows()

    def on_virtual_mouse_wheel(self, event):
        """Scroll blindado + debounce para evitar tearing y renders repetidos."""
        # 1. Calcular alturas
        content_h = len(self.renamer_files) * self.ROW_HEIGHT
        canvas_h = self.ren_canvas.winfo_height()

        # 2. Si el contenido cabe, no scrollear
        if content_h <= canvas_h:
            return "break"

        # 3. Scroll normal (normalizar pasos)
        try:
            if os.name == 'nt':
                steps = int(-1 * (event.delta / 120))
            else:
                # event.num: 4 = up, 5 = down
                steps = -1 if getattr(event, "num", None) == 4 else 1
        except Exception:
            steps = -1 if getattr(event, "num", None) == 4 else 1

        # limitar pasos para que no salte mucho
        if steps > 3: steps = 3
        if steps < -3: steps = -3

        self.ren_canvas.yview_scroll(steps, "units")
        self.ren_v_scrollbar.set(*self.ren_canvas.yview())

        # 4. Debounce render: programar solo 1 render cuando haya CPU libre
        if getattr(self, "_render_scheduled", False) is False:
            self._render_scheduled = True
            self.after_idle(self._delayed_render_virtual_rows)

        return "break"

    def _delayed_render_virtual_rows(self):
        """Helper: llamado por after_idle para batch de renders."""
        self._render_scheduled = False
        try:
            self.render_virtual_rows()
        except Exception:
            pass


    def on_virtual_resize(self, event):
        """Al redimensionar ventana, ajustar ancho, recalcular filas y CENTRAR TEXTO."""
        
        # 1. Ajustar filas existentes
        self.render_virtual_rows()
        
        # 2. Centrar dinámicamente el texto de 'Arrastra aquí'
        if hasattr(self, 'ren_empty_id') and self.ren_empty_id:
            # Obtener dimensiones actuales del canvas
            w = self.ren_canvas.winfo_width()
            h = self.ren_canvas.winfo_height()
            
            # Si el canvas aun no se dibuja, usar valores por defecto seguros
            if w < 50: w = 800
            if h < 50: h = 400
            
            # Mover el texto al centro exacto
            self.ren_canvas.coords(self.ren_empty_id, w // 2, h // 2)

    def on_virtual_row_click(self, event):
        """Maneja el click en una fila virtual."""
        # Buscar el widget padre que tiene la referencia
        w = event.widget
        # A veces el click cae en el label, a veces en el frame. Buscamos atributo.
        while w:
            if hasattr(w, "virtual_ref"):
                idx = w.virtual_ref["data_index"]
                if idx != -1:
                    self.select_renamer_item(idx)
                break
            w = w.master

    def check_click_empty(self, event):
        """Si haces click en el área vacía, abrir diálogo"""
        if not self.renamer_files:
            self.select_renamer_files_dialog()
        
      
        
if __name__ == "__main__":
    multiprocessing.freeze_support()
    # Si el .exe se relanzó para correr spotDL (u otro módulo permitido), se
    # ejecuta aquí y el proceso termina sin abrir la interfaz.
    _dmt_despachar_modulo_si_corresponde()

    # Registro para builds sin consola y carpeta temporal propia de esta sesión
    _dmt_preparar_stdio_app()
    _dmt_activar_faulthandler()
    _dmt_iniciar_temporales()
    print(f"[DMT] Python {sys.version.split()[0]} | compilado={_is_frozen_build()} | {sys.executable}")

    try:
        import ctypes
        ctypes.windll.shcore.SetProcessDpiAwareness(1) 
    except: pass

    # 1) Root invisible (Se inicia PRIMERO para mostrar ventana rápido)
    root = tk.Tk()
    root.withdraw()
    root.overrideredirect(True)

    # 2) Splash
    splash = SplashScreen(parent=root)
    
    # 3) Lógica optimizada
    def check_splash_and_start_app():
        
        if getattr(splash, "ready_to_exit", False):
            
            # --- FASE 1: CONFIGURACIÓN TÉCNICA ---
            try:
                configurar_ffmpeg_local() 
            except Exception as e:
                print(f"Error en setup inicial ffmpeg_local {e}")

            try:
                configurar_deno_local()  # Solo detecta/registra Deno si ya existe; no descarga nada aquí.
            except Exception as e:
                print(f"Error en setup inicial deno_local {e}")

            # --- FASE 2: CONSTRUIR APP (oculta y transparente) ---
            app = App()

            # Cancelar los center_window automáticos del __init__ para evitar
            # el double-show que causaba el flash tardío
            try:
                for _aid in getattr(app, '_auto_center_ids', []):
                    app.after_cancel(_aid)
            except: pass

            # Posicionar en pantalla sin revelarla (show=False)
            app.center_window(show=False)
            app.attributes("-alpha", 0.0)

            try:
                import tkinter as tk
                tk._default_root = app
            except Exception:
                pass

            # --- FASE 3: TRANSICIÓN SUAVE (fade-out splash → fade-in app) ---
            _STEPS = 6   # pasos totales de cada fade
            _DELAY = 14   # ms entre pasos (~250ms total cada fade)

            def _fade_out_splash(step=0):
                """Desvanece el splash. Al terminar, destruye y arranca el fade-in."""
                if step <= _STEPS:
                    try: splash.attributes("-alpha", 1.0 - step / _STEPS)
                    except: pass
                    root.after(_DELAY, lambda: _fade_out_splash(step + 1))
                else:
                    # Splash en alpha=0 (invisible) → mostrar app y arrancar fade-in
                    # ANTES de destruir root para que no haya hueco entre las dos ventanas
                    try:
                        app.attributes("-alpha", 0.0)
                        app.deiconify()
                        app.lift()
                    except: pass
                    app.after(0, lambda: _fade_in_app(0))
                    # Destruir splash/root con pequeño delay — ya son invisibles, no se nota
                    root.after(60, _destroy_temps)

            def _destroy_temps():
                try: splash.destroy()
                except: pass
                try: root.destroy()
                except: pass

            def _fade_in_app(step=0):
                """Aparece la app desde transparente hasta opacidad total."""
                if step <= _STEPS:
                    try: app.attributes("-alpha", step / _STEPS)
                    except: pass
                    app.after(_DELAY, lambda: _fade_in_app(step + 1))
                else:
                    # Totalmente visible → restaurar estado normal
                    try:
                        app.attributes("-alpha", 1.0)
                        app.attributes("-topmost", True)
                        app.after(50, lambda: app.attributes("-topmost", False))
                        app.focus_force()
                    except: pass

            # Disparar el fade-out (root.mainloop sigue activo hasta que root muere)
            root.after(_DELAY, lambda: _fade_out_splash(0))
            app.mainloop()

        else:
            # Si el splash aún no termina su animación, esperar 50ms
            root.after(50, check_splash_and_start_app)

    # Arrancar el ciclo de chequeo
    root.after(50, check_splash_and_start_app)
    root.mainloop()