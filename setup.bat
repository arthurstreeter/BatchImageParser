@echo off

set "script_dir=%~dp0"

:: Create a virtual environment directory
mkdir %script_dir%.venv %script_dir%images %script_dir%extracted

:: Install pipenv
pip install pipenv --user

:: Use pipenv to install dependencies
python -m pipenv install