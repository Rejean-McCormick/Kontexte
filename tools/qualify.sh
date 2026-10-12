#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
export PYTHONPATH="$PWD/src"
python -m kontexte validate
python -m unittest discover -s tests -v
python -m kontexte orgo-fixture fete-sorciere --out integrations/orgo/fete-sorciere.scenario.json
python -m kontexte orgo-blueprint fete-sorciere --out integrations/orgo/fete-sorciere.blueprint.json
python -m kontexte curriculum fete-sorciere --out integrations/ekole/fete-sorciere.curriculum-links.json
python -m kontexte site --out examples/site
python -m kontexte bill --input examples/klownkoins.json --out examples/reports/klownkoins-result.json
python -m kontexte privacy --input examples/consent-refusal.json --out examples/reports/media-result.json
if [ -n "${ORGO_SRC:-}" ]; then
  node "$ORGO_SRC/tools/scenario-injector/cli.mjs" validate integrations/orgo/fete-sorciere.scenario.json
fi
echo 'Kontexte qualification terminée.'
