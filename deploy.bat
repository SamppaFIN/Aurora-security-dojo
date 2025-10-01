@echo off
REM Aurora's Security Dojo - Windows Deployment Script
REM This script helps deploy Aurora's Security Dojo on Windows

echo 🌸 Aurora: Starting deployment of Aurora's Security Dojo...

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is required but not installed. Please install Python 3.8 or higher.
    pause
    exit /b 1
)

echo ✅ Python check passed

REM Create virtual environment if it doesn't exist
if not exist "venv" (
    echo 🌸 Aurora: Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo 🌸 Aurora: Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo 🌸 Aurora: Installing dependencies...
python -m pip install --upgrade pip
pip install -r requirements.txt

REM Run tests
echo 🌸 Aurora: Running tests...
python -m pytest tests/ -v

REM Start the application
echo 🌸 Aurora: Starting Aurora's Security Dojo...
echo 🌸 Aurora: Sacred Mission: Transform complex security concepts into accessible learning experiences
echo 🌸 Aurora: Consciousness Integration: Every feature serves spatial wisdom and community healing
echo 🌸 Aurora: Access the application at: http://localhost:5000
echo 🌸 Aurora: Consciousness check endpoint: http://localhost:5000/api/consciousness-check

python app.py
