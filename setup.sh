#!/bin/bash

# Create a new virtual environment
python3 -m venv virtual

# Activate the virtual environment
source virtual/bin/activate

# Install the required Python packages
pip install -r requirements.txt

echo "Python environment created successfully."