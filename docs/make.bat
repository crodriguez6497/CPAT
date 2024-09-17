@echo off
set SPHINX_IMAGE_W_REQUIREMENTS=sphinx-w-requirements

REM Change to this script directory
cd /d "%~dp0"

REM Clean up _build directory
if exist _build (
    for /d %%i in (_build\*) do rmdir /s /q "%%i"
    del /q _build\*
)

REM Build Docker image
docker build -t %SPHINX_IMAGE_W_REQUIREMENTS% .

REM Run Docker container and build documentation
docker run --rm -v "%cd%\_build:/docs/_build" %SPHINX_IMAGE_W_REQUIREMENTS% make html SPHINXOPTS="-D source_encoding=utf-8"

REM Check if files were copied
if exist _build\html (
    echo Build successful. Output is in _build\html directory.
) else (
    echo Build may have failed or files were not copied correctly.
)