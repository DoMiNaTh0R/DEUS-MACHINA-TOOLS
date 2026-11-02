@echo off
setlocal EnableExtensions EnableDelayedExpansion

:: ====================================================================
::  DEUS MACHINA | TOOLS - compilacion completa (todo junto a este .bat)
::
::   1. Crea el venv si no existe o esta roto  (crear_venv_dmt.bat /auto)
::   2. Regenera imgtype\THIRD_PARTY_NOTICES.txt con las librerias del venv
::      (si esta generar_licencias.py; si no, usa el que ya trae imgtype)
::   3. Compila con PyInstaller (la version sale sola de Deus_machina_tools.py)
::   4. Arma Instalador\DEUS_MACHINA_TOOLS: el build + tools + documentos
::   5. Copia README.txt y EULA.txt a Instalador\ (los muestra el asistente)
::   6. Copia el codigo, los documentos y las imagenes a repo_github
::
::  NO firma nada ni ejecuta Inno Setup. Al terminar, a mano:
::   a) firmar Instalador\DEUS_MACHINA_TOOLS\DEUS_MACHINA_TOOLS.exe
::   b) compilar Instalador\innoF.iss con Inno Setup (toma la version del .exe)
::   c) firmar Instalador\Output\DeusMachinaTools_Setup_vX.Y.exe
::
::  Uso:  compilar_dmt.bat           (pausa al final)
::        compilar_dmt.bat /auto     (sin pausas)
::  .exe CON consola (diagnostico):  set DMT_CONSOLA=1  y luego compilar_dmt.bat
:: ====================================================================
set "BASE=%~dp0"
set "PY=!BASE!build_env_DMT\Scripts\python.exe"
set "INSTALADOR=!BASE!Instalador"
set "DESTINO=!INSTALADOR!\DEUS_MACHINA_TOOLS"
set "REPO=!BASE!Claude Prueba\repo_github"
:: ====================================================================

set "AUTO=0"
if /i "%~1"=="/auto" set "AUTO=1"
pushd "!BASE!"

echo.
echo === 1/6 Entorno virtual ===
set "VENV_OK=0"
if exist "!PY!" (
    "!PY!" -c "import sys, PyInstaller; sys.exit(0 if sys.version_info[:2]==(3,13) else 1)" >nul 2>&1 && set "VENV_OK=1"
)
if "!VENV_OK!"=="0" (
    echo No hay un venv valido con PyInstaller: se crea con crear_venv_dmt.bat
    call "!BASE!crear_venv_dmt.bat" /auto
    if errorlevel 1 goto :error
) else (
    echo OK: !PY!
)

:: La version la decide Deus_machina_tools.py (version = "X.Y")
"!PY!" build_pyinstaller.py --version > "%TEMP%\dmt_version.txt"
if errorlevel 1 goto :error
set /p VER=<"%TEMP%\dmt_version.txt"
del "%TEMP%\dmt_version.txt" >nul 2>&1
echo.
echo ==================================================================
echo  DEUS MACHINA ^| TOOLS  version !VER!
echo ==================================================================

echo.
echo === 2/6 Licencias de terceros (imgtype\THIRD_PARTY_NOTICES.txt) ===
:: generar_licencias.py es una herramienta del autor y no viene en el repositorio
if exist "!BASE!generar_licencias.py" (
    "!PY!" generar_licencias.py --salida "imgtype\THIRD_PARTY_NOTICES.txt" --app "DEUS MACHINA | TOOLS" --extra licencias_extra.json --excluir "pyinstaller-hooks-contrib,altgraph,pefile,pywin32-ctypes"
    if errorlevel 1 goto :error
) else (
    echo Sin generar_licencias.py: se usa el THIRD_PARTY_NOTICES.txt que ya esta en imgtype.
)

echo.
echo === 3/6 PyInstaller ===
"!PY!" build_pyinstaller.py
if errorlevel 1 goto :error
if not exist "!BASE!dist\DEUS_MACHINA_TOOLS\DEUS_MACHINA_TOOLS.exe" (
    echo ERROR: PyInstaller no genero dist\DEUS_MACHINA_TOOLS\DEUS_MACHINA_TOOLS.exe
    goto :error
)

echo.
echo === 4/6 Instalador\DEUS_MACHINA_TOOLS: build + tools + documentos ===
if not exist "!INSTALADOR!" mkdir "!INSTALADOR!"
if exist "!DESTINO!" (
    rmdir /s /q "!DESTINO!"
    if exist "!DESTINO!" (
        echo ERROR: no se pudo borrar el build anterior en !DESTINO!
        echo Cierra la app o el Explorador si lo tienen abierto y vuelve a intentarlo.
        goto :error
    )
)
move "!BASE!dist\DEUS_MACHINA_TOOLS" "!DESTINO!" >nul
if errorlevel 1 goto :error
echo Copiando tools (ffmpeg, ghostscript, paddleocr)...
robocopy "!BASE!tools" "!DESTINO!\tools" /E /NFL /NDL /NJH /NJS /NP /R:1 /W:1 >nul
if errorlevel 8 goto :error
for %%F in (CHANGELOG.md EULA.txt LICENSE-EXCEPTION.txt LICENSE.txt README.md THIRD_PARTY_NOTICES.txt) do (
    copy /Y "!BASE!imgtype\%%F" "!DESTINO!\%%F" >nul || goto :error
)
echo OK: !DESTINO!

echo.
echo === 5/6 Documentos del asistente (Instalador\README.txt y EULA.txt) ===
for %%F in (README.txt EULA.txt) do (
    copy /Y "!BASE!imgtype\%%F" "!INSTALADOR!\%%F" >nul || goto :error
)
echo OK

echo.
echo === 6/6 repo_github: codigo, documentos e imagenes ===
if exist "!REPO!\" (
    for %%F in (Deus_machina_tools.py build_pyinstaller.py compilar_dmt.bat crear_venv_dmt.bat constraints.txt requirements.txt cuda_necesarias.txt) do (
        copy /Y "!BASE!%%F" "!REPO!\%%F" >nul || goto :error
    )
    copy /Y "!BASE!imgtype\LICENSE.txt" "!REPO!\LICENSE" >nul || goto :error
    copy /Y "!BASE!imgtype\LICENSE-EXCEPTION.txt" "!REPO!\LICENSE-EXCEPTION.txt" >nul || goto :error
    robocopy "!BASE!imgtype" "!REPO!\imgtype" /E /NFL /NDL /NJH /NJS /NP /R:1 /W:1 >nul
    if errorlevel 8 goto :error
    echo OK: !REPO!
    echo   ^(el README.md y docs\COMPILAR.md propios del repositorio se editan a mano^)
) else (
    echo No existe !REPO!: se omite.
)

echo.
echo ==================================================================
echo  LISTO: DEUS MACHINA ^| TOOLS !VER!
echo  !DESTINO!\DEUS_MACHINA_TOOLS.exe
echo.
echo  Falta, a mano:
echo   a^) firmar DEUS_MACHINA_TOOLS.exe
echo   b^) compilar Instalador\innoF.iss con Inno Setup
echo   c^) firmar Instalador\Output\DeusMachinaTools_Setup_v!VER!.exe
echo      ^(el buscador de actualizaciones de la app rechaza instaladores sin tu firma^)
echo ==================================================================
popd
if "!AUTO!"=="0" pause
exit /b 0

:error
echo.
echo ERROR: la compilacion se detuvo. Revisa el mensaje de arriba.
popd
if "!AUTO!"=="0" pause
exit /b 1
