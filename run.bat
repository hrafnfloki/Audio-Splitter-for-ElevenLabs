@echo off
cls
echo Checking for Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python from https://www.python.org/downloads/
    pause
    exit
)

echo Checking for FFmpeg...
ffmpeg -version >nul 2>&1
if %errorlevel% neq 0 (
    echo FFmpeg is not detected. Download from https://ffmpeg.org/download.html and ensure it is in your system's PATH.
    pause
    exit
)

echo Installing required Python packages...
python -m pip install -r requirements.txt

echo Starting the application...
python split_audio.py
pause