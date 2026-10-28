# Development and Testing

Kontexte's core is a small Python package (Python **3.10+**) with JSON content, local HTML generation and command-line tools. It is intentionally decoupled from running Orgo/Ekole services for offline authoring and synthetic verification.

## Directory guide

- `src/kontexte/models.py` — role and mission validation.
- `src/kontexte/render.py` — HTML/CSS projection.
- `src/kontexte/orgo.py`, `orgo_http.py` — synthetic integration fixture/intent and server-side HTTP helper.
- `src/kontexte/ekole.py`, `evidence.py` — candidate curriculum links and development evidence store.
- `src/kontexte/economy.py`, `media.py` — fictional accounting and restrictive publication manifest.
- `src/kontexte/cli.py` — command dispatch.
- `schemas/` — JSON Schema records.
- `data/` — source design content (roles, missions, catalogues, localizations).
- `teacher-only/` — restricted education materials, never public student assets.
- `tests/` — unit tests, including Québec overlay consistency checks.

## Local checks

```bash
PYTHONPATH=src python -m kontexte validate
PYTHONPATH=src python -m unittest discover -s tests -v
PYTHONPATH=src python -m kontexte site --out /tmp/kontexte-site
python -m compileall -q src
```

The repository includes `tools/qualify.sh` and `tools/qualify.ps1` for extended checks and exports; the shell script can optionally use `ORGO_SRC` to validate the generated synthetic fixture with the separate Orgo tool. Scripts may write or regenerate local fixture/output files: review diffs before committing.

`pytest` is not required; tests use the Python `unittest` discovery command. Passing software tests is **not** proof of educational effectiveness, language correctness or child-data compliance.

## Creating a role or mission

1. Copy an existing reviewed JSON example in `data/roles/` or `data/missions/`.
2. Give it a stable ID and meaningful source metadata; preserve the expected format.
3. Keep the role theme on the allowlist; give localized labels where available.
4. For a mission, ensure roles exist, dependencies refer to earlier steps and internal curriculum IDs resolve.
5. Keep teacher-only content, future private disclosures and real identities out of public projections.
6. Run `validate`, tests and manual preview; then obtain educational and cultural review.

For neutral frames, work from `data/trames/catalogue-neutral-v0.2.json` and do not silently mutate a parent that existing overlays refer to by checksum. See [Scenario Catalogue](Scenario-Catalogue) and [Cultural Localization](Cultural-Localization).

## Integrating with Orgo

The `orgo-fixture` command exports a recognized **initialization fixture**, not an executable full mission. All API interactions and configuration should use authorized test environments. See [Orgo Integration](Orgo-Integration).

## Static export review checklist

Before releasing any HTML, confirm that no `teacher-only` files, authentic learner IDs, hidden information fragments, localized source answers, media without permission, or internal SQLite development files have been copied. A successful render says nothing about its intended audience's authorization.

## Contributing

Contribution and licensing terms remain unsettled. See the root `CONTRIBUTING.md`, `LICENSE-POLICY.md`, and [Governance and Licensing](Governance-and-Licensing).
