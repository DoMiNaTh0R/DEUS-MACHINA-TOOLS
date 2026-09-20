@echo off
setlocal EnableExtensions EnableDelayedExpansion

:: ====================================================================
::  Crea (o repara) el venv de DEUS MACHINA con el stack CUDA 12.9.
::  Funciona con rutas que tienen espacios y parentesis.
::  Ajusta estas dos lineas si tu setup es distinto:
:: ====================================================================
set "VENV_DIR=%~dp0build_env_DMT"
set "PY_VERSION=3.13"
:: ====================================================================

set "SCRIPT_DIR=%~dp0"
set "LOG=!SCRIPT_DIR!instalacion_venv_dmt.log"
set "PY=!VENV_DIR!\Scripts\python.exe"

if not exist "!SCRIPT_DIR!constraints.txt" (
    echo ERROR: no encuentro constraints.txt junto a este .bat.
    echo Pon los dos archivos en la misma carpeta y vuelve a correrlo.
    pause
    exit /b 1
)

echo.
echo ==================================================================
echo  Venv: !VENV_DIR!
echo  Log de pip: !LOG!
echo ==================================================================

if exist "!PY!" (
    echo.
    echo Ya existe un venv en esa ruta.
    choice /c SN /m "Reutilizarlo y completar o reparar la instalacion"
    if errorlevel 2 exit /b 0
) else (
    echo.
    echo === 1/10 Creando venv con Python !PY_VERSION! ===
    py -!PY_VERSION! -m venv "!VENV_DIR!"
    if errorlevel 1 (
        echo ERROR creando el venv. Revisa versiones instaladas con: py -0
        pause
        exit /b 1
    )
)

"!PY!" -c "import sys; sys.exit(0 if sys.version_info[:2]==(3,13) else 1)"
if errorlevel 1 (
    echo ERROR: el venv no es Python 3.13.
    pause
    exit /b 1
)

echo.
echo === 2/10 Protegiendo el venv: constraints.txt + pip.ini ===
copy /Y "!SCRIPT_DIR!constraints.txt" "!VENV_DIR!\constraints.txt" >nul
if errorlevel 1 goto :error
:: pip parte el valor de 'constraint' en los espacios, incluso con comillas.
:: Por eso la ruta se escribe como URI file:///...%%20... (sin espacios).
:: Lo escribe Python para que el formato quede exacto.
"!PY!" -c "import pathlib,sys; v=pathlib.Path(sys.argv[1]); (v/'pip.ini').write_text('[install]\nconstraint = '+(v/'constraints.txt').as_uri()+'\n', encoding='utf-8')" "!VENV_DIR!"
if errorlevel 1 goto :error
type "!VENV_DIR!\pip.ini"

echo.
echo === 3/10 Actualizando pip ===
call :pip install --upgrade pip || goto :error

echo.
echo === 4/10 torch 2.8.0 + CUDA 12.9 - descarga grande ===
call :pip install "torch==2.8.0+cu129" --index-url https://download.pytorch.org/whl/cu129 || goto :error

echo.
echo === 5/10 setuptools actual ===
call :pip install --upgrade setuptools || goto :error

echo.
echo === 6/10 CTranslate2 + faster-whisper ===
call :pip install ctranslate2==4.8.2 faster-whisper==1.2.1 || goto :error

echo.
echo === 7/10 ONNX Runtime + RapidOCR ===
call :pip install onnxruntime==1.30.0 rapidocr==3.9.2 || goto :error

echo.
echo === 8/10 PaddlePaddle GPU + PaddleOCR ===
call :pip install paddlepaddle-gpu==3.3.1 -i https://www.paddlepaddle.org.cn/packages/stable/cu129/ --extra-index-url https://pypi.org/simple || goto :error
call :pip install paddleocr==3.7.0 || goto :error

echo.
echo === 9/10 Resto de dependencias de DMT ===
call :pip install customtkinter tkinterdnd2 pillow piexif mutagen python-docx openpyxl python-pptx pymupdf PyPDF2 pyaudio rembg "yt-dlp[default,curl-cffi]" yt-dlp-ejs spotdl || goto :error

echo.
echo === 10/10 Quitando paquetes nvidia-* de pip - chocan con las DLLs de torch ===
set "LISTA=!VENV_DIR!\nvidia_pip_respaldo.txt"
"!PY!" -m pip freeze | findstr /b /i "nvidia-" > "!LISTA!"
for %%A in ("!LISTA!") do set "TAM=%%~zA"
if "!TAM!"=="0" (
    echo No hay paquetes nvidia-* instalados.
) else (
    type "!LISTA!"
    for /f "usebackq tokens=1 delims==" %%P in ("!LISTA!") do "!PY!" -m pip uninstall -y %%P
    > "!VENV_DIR!\revertir_nvidia_pip.bat" echo @echo off
    >> "!VENV_DIR!\revertir_nvidia_pip.bat" echo "!PY!" -m pip install --no-deps -r "!LISTA!" -i https://www.paddlepaddle.org.cn/packages/stable/cu129/ --extra-index-url https://pypi.org/simple
    >> "!VENV_DIR!\revertir_nvidia_pip.bat" echo pause
    echo Respaldo: nvidia_pip_respaldo.txt y revertir_nvidia_pip.bat dentro del venv.
)

echo.
echo ==================================================================
echo  VERIFICACION
echo ==================================================================
"!PY!" -c "import torch, ctranslate2, faster_whisper, onnxruntime, rapidocr, paddle, paddleocr, cv2, numpy, customtkinter, setuptools; print('torch', torch.__version__, '| CUDA:', torch.cuda.is_available(), '|', torch.cuda.get_device_name(0) if torch.cuda.is_available() else '-'); print('paddle', paddle.__version__, '| GPUs:', paddle.device.cuda.device_count(), '| cuDNN en uso:', paddle.device.get_cudnn_version()); print('ctranslate2', ctranslate2.__version__, '| GPUs:', ctranslate2.get_cuda_device_count()); print('faster-whisper', faster_whisper.__version__, '| onnxruntime', onnxruntime.__version__, '| paddleocr', paddleocr.__version__); print('numpy', numpy.__version__, '| opencv', cv2.__version__, '| customtkinter', customtkinter.__version__, '| setuptools', setuptools.__version__)"
if errorlevel 1 goto :error

echo.
echo Prueba de proteccion 1: pedir numpy 2.4.0 debe ser RECHAZADO...
"!PY!" -m pip install --dry-run --no-deps -q numpy==2.4.0 >nul 2>&1
if errorlevel 1 (
    echo   [OK] constraints.txt esta activo.
) else (
    echo   [FALLO] pip acepto numpy 2.4.0: el pip.ini no se esta aplicando.
    goto :error
)
echo Prueba de proteccion 2: actualizar yt-dlp debe seguir funcionando...
"!PY!" -m pip install --dry-run --no-deps -q --upgrade yt-dlp >nul 2>&1
if errorlevel 1 (
    echo   [FALLO] pip no puede actualizar yt-dlp.
    goto :error
) else (
    echo   [OK] las actualizaciones de yt-dlp y spotDL no se bloquean.
)

echo.
echo pip check - es normal que diga que paddlepaddle-gpu pide paquetes nvidia:
"!PY!" -m pip check
"!PY!" -m pip freeze > "!VENV_DIR!\freeze_venv_dmt.txt"

echo.
echo ==================================================================
echo  LISTO. Venv protegido por constraints.txt y sin paquetes nvidia.
echo  Lista de versiones: freeze_venv_dmt.txt dentro del venv.
echo ==================================================================
pause
exit /b 0

:: --------------------------------------------------------------------
:pip
"!PY!" -m pip %* --log "!LOG!"
exit /b !errorlevel!

:error
echo.
echo ERROR: la instalacion se detuvo. Revisa el mensaje de arriba y el log:
echo !LOG!
pause
exit /b 1
