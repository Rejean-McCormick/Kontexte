@echo off
setlocal
cd /d "%~dp0"
set "PYTHONPATH=%CD%\src"
where py >nul 2>nul
if %ERRORLEVEL% EQU 0 (
 py -3 -m kontexte site --out examples\site --lang fr-CA
) else (
 python -m kontexte site --out examples\site --lang fr-CA
)
if not errorlevel 1 start "" "%CD%\examples\site\index.html"
pause
endlocal
