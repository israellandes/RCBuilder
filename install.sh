#!/bin/bash

# Update and upgrade the package list
echo "Updating and upgrading package list..."
sudo apt-get update -y
sudo apt-get upgrade -y

# Install dependencies for Python
echo "Installing dependencies..."
sudo apt-get install -y software-properties-common

# Add deadsnakes PPA to get the latest version of Python
echo "Adding deadsnakes PPA..."
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt-get update -y

# Install Python 3.x (Replace '3.x' with your desired version)
echo "Installing Python..."
sudo apt-get install -y python3.10

# Install pip, the package manager for Python
echo "Installing pip..."
sudo apt-get install -y python3-pip

# Install virtualenv for creating isolated Python environments
echo "Installing virtualenv..."
sudo pip3 install virtualenv
sudo apt -y install python3.12-venv

# Verify Python installation
echo "Verifying Python installation..."
python3 --version
pip3 --version

echo "Python installation complete."