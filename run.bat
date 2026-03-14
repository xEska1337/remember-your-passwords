@echo off
setlocal

:: Determine the directory where this script is located
cd /d "%~dp0"

:: 1. Check/Create Virtual Environment
if not exist ".venv" (
    echo [INFO] First run detected. Setting up environment...
    echo [INFO] Creating virtual environment...
    python -m venv .venv

    if errorlevel 1 (
        echo [ERROR] Python not found. Please ensure Python is installed and added to PATH.
        pause
        exit /b 1
    )

    echo [INFO] Installing requirements...
    .venv\Scripts\pip install -r requirements.txt
)

:: 2. Compile Resources and UI
:: This ensures updates to .ui or .qrc files are always applied
if exist ".venv\Scripts\pyside6-rcc.exe" (
    echo [INFO] Compiling resources...
    .venv\Scripts\pyside6-rcc resources.qrc -o resources_rc.py
    .venv\Scripts\pyside6-uic form.ui -o ui_form.py
) else (
    echo [WARNING] PySide6 tools not found. Skipping compilation.
)

:: 3. Run the Application
echo [INFO] Starting Remember Your Passwords...
:: Use pythonw.exe to run without keeping a console window open,
:: or python.exe if you want to see debug output.
.venv\Scripts\pythonw.exe main.py

endlocal