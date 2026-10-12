$ErrorActionPreference = 'Stop'
Set-Location (Split-Path $PSScriptRoot -Parent)
$env:PYTHONPATH = 'src'
python -m kontexte validate
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
python -m unittest discover -s tests -v
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
python -m kontexte site --out examples/site
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
python -m kontexte orgo-fixture fete-sorciere --out integrations/orgo/fete-sorciere.scenario.json
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
Write-Output 'Qualification Kontexte terminée.'
