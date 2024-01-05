@echo off

:: Create a virtual environment directory
mkdir .venv images extracted

:: Install pipenv
pip install pipenv --user

:: Use pipenv to install dependencies
python -m pipenv install