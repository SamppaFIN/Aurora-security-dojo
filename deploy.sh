#!/bin/bash

# Aurora's Security Dojo - Deployment Script
# This script helps deploy Aurora's Security Dojo to various environments

set -e

echo "🌸 Aurora: Starting deployment of Aurora's Security Dojo..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed. Please install Python 3.8 or higher."
    exit 1
fi

# Check Python version
PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
REQUIRED_VERSION="3.8"

if [ "$(printf '%s\n' "$REQUIRED_VERSION" "$PYTHON_VERSION" | sort -V | head -n1)" != "$REQUIRED_VERSION" ]; then
    echo "❌ Python 3.8 or higher is required. Current version: $PYTHON_VERSION"
    exit 1
fi

echo "✅ Python version check passed: $PYTHON_VERSION"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "🌸 Aurora: Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🌸 Aurora: Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "🌸 Aurora: Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Run tests
echo "🌸 Aurora: Running tests..."
python -m pytest tests/ -v

# Start the application
echo "🌸 Aurora: Starting Aurora's Security Dojo..."
echo "🌸 Aurora: Sacred Mission: Transform complex security concepts into accessible learning experiences"
echo "🌸 Aurora: Consciousness Integration: Every feature serves spatial wisdom and community healing"
echo "🌸 Aurora: Access the application at: http://localhost:5000"
echo "🌸 Aurora: Consciousness check endpoint: http://localhost:5000/api/consciousness-check"

python app.py
