@echo ON

cd /d %~dp0

call "py3-env.bat"

python3 -m pip install --upgrade --force-reinstall --no-cache-dir pillow