#!/usr/bin/env sh
set -eu
cd "$(dirname "$0")"
export PYTHONPATH="$(pwd)/src"
PYTHON_BIN="${PYTHON_BIN:-python3}"
"$PYTHON_BIN" -m kontexte doctor
"$PYTHON_BIN" -m kontexte lab
