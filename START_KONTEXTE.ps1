$ErrorActionPreference = 'Stop'
Set-Location $PSScriptRoot
$env:PYTHONPATH = Join-Path $PSScriptRoot 'src'
if (Get-Command py -ErrorAction SilentlyContinue) {
    & py -3 -m kontexte doctor
    if ($LASTEXITCODE -ne 0) { throw 'Diagnostics failed' }
    & py -3 -m kontexte lab
} else {
    & python -m kontexte doctor
    if ($LASTEXITCODE -ne 0) { throw 'Diagnostics failed' }
    & python -m kontexte lab
}
