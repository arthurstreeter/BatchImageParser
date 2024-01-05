@echo off

echo Running Batch Image Parser...

set "script_dir=%~dp0"

call %script_dir%.venv\Scripts\python.exe -u %script_dir%main.py %* 2>&1

pause