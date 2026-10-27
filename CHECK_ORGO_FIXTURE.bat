@echo off
setlocal
cd /d "%~dp0"
set "PYTHONPATH=%CD%\src"
if "%ORGO_ROOT%"=="" (
 echo DEFINIR ORGO_ROOT=chemin vers le depot Orgo; exemple : set ORGO_ROOT=C:\mycode\Orgo\Orgo
 echo Ceci valide une fixture, ne la charge pas dans Orgo.
 pause
 exit /b 2
)
where py >nul 2>nul
if %ERRORLEVEL% EQU 0 (
 py -3 -m kontexte orgo-check fete-sorciere --orgo "%ORGO_ROOT%" --mode validate
) else (
 python -m kontexte orgo-check fete-sorciere --orgo "%ORGO_ROOT%" --mode validate
)
pause
endlocal
