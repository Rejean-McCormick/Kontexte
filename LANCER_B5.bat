@echo off
setlocal EnableExtensions
cd /d "%~dp0"
if errorlevel 1 goto :error
set "PY=py -3"
py -3 -c "import sys; assert sys.version_info >= (3,10)" >nul 2>nul
if not errorlevel 1 goto :python_ok
set "PY=python"
python -c "import sys; assert sys.version_info >= (3,10)" >nul 2>nul
if errorlevel 1 goto :error
:python_ok
set "PYTHONPATH=%CD%\src"
echo [B5] Audit Kontexte 3e annee...
%PY% -m kontexte qc3-audit-b5 --out "sorties\b5-audit"
if errorlevel 1 goto :error
echo [B5] Apercus separes enseignant et eleve...
%PY% -m kontexte qc3-pilot-b5 --out "sorties\b5-pilote"
if errorlevel 1 goto :error
%PY% -m unittest discover -s tests -q
if errorlevel 1 goto :error
echo.
echo Pret. Ouvre "sorties\b5-pilote\student-preview\boulangerie.html" pour apercu eleve.
echo Apercu enseignant : "sorties\b5-pilote\teacher-only\boulangerie-enseignant.html"
pause
exit /b 0
:error
echo.
echo Echec du lancement B5. Python 3.10+ et les sources de Kontexte sont requis.
pause
exit /b 1
