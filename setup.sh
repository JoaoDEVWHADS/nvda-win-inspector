#!/bin/bash
set -e


echo "Warning: NVDA addons are typically developed on Windows."
echo "This script sets up a Linux-based environment for tooling and logic validation."

echo "Checking prerequisites..."

if ! command -v python3 &> /dev/null; then
    echo "Error: python3 is not installed."
    exit 1
fi

if ! command -v git &> /dev/null; then
    echo "Error: git is not installed."
    exit 1
fi

echo "Prerequisites met."

PYTHON_CMD="python3"
VENV_DIR=".venv"

if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment in $VENV_DIR..."
    $PYTHON_CMD -m venv $VENV_DIR
else
    echo "Virtual environment already exists."
fi

source $VENV_DIR/bin/activate
echo "Virtual environment activated."

echo "Installing dependencies..."
pip install --upgrade pip


echo "Dependencies installed."

echo "Runnning integrity checks..."
python3 --version
pip --version

echo "Setup complete! Run 'source .venv/bin/activate' to start working."
