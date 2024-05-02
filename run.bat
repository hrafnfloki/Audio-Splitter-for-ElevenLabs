@echo off
echo Checking for Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python to continue.
    pause
    exit /b
)

echo Installing required packages...
python -m pip install -r requirements.txt

echo Running the application...
python split_audio.py
pause
