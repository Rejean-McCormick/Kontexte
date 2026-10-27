@echo off
setlocal
cd /d "%~dp0"
set "PYTHONPATH=%CD%\src"
where py >nul 2>nul
if %ERRORLEVEL% EQU 0 (
  py -3 -m kontexte doctor
  if errorlevel 1 goto fail
  py -3 -m kontexte lab
  goto end
)
where python >nul 2>nul
if %ERRORLEVEL% EQU 0 (
  python -m kontexte doctor
  if errorlevel 1 goto fail
  python -m kontexte lab
  goto end
)
echo ERREUR : installer Python 3.10+ depuis python.org, puis relancer.
goto fail
:fail
echo Kontexte n'a pas demarre. Verifier Python et consulter README.md.
pause
:end
endlocal
