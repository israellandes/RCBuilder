#!/bin/bash

echo "Creating a virtual environment..."
python3 -m venv ~/my_venv
source ~/my_venv/bin/activate
pip install beautifulsoup4

clear 

echo "Open env with 'source ~/my_venv/bin/activate' "
