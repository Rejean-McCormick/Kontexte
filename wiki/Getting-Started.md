# Getting Started

Kontexte can validate JSON role and mission files and generate an offline HTML showcase without running Orgo or Ekole. This makes it suitable for local inspection and synthetic tests.

## 1. Requirements

- A checkout or extracted ZIP containing this `Kontexte/` repository.
- Python **3.10 or later**.
- A web browser to open locally generated HTML.
- **Optional:** a separate, compatible Orgo checkout to validate a scenario-injector fixture.

The base package declares no required third-party runtime dependencies. `PYTHONPATH=src` allows running the source without installing it.

## 2. Validate and test

```bash
# macOS / Linux; from Kontexte/
PYTHONPATH=src python -m kontexte validate
PYTHONPATH=src python -m unittest discover -s tests -v
```

On PowerShell:

```powershell
$env:PYTHONPATH = "src"
python -m kontexte validate
python -m unittest discover -s tests -v
```

The base validator checks role records, mission structure, references, and known internal Ekole catalogue IDs. The codebase's tests also cover calculators, render output, consent logic, and localized data checks. Successful tests **do not** mean expert pedagogical approval or secure production integration.

## 3. Generate previews

```bash
PYTHONPATH=src python -m kontexte site --out examples/site --lang en
PYTHONPATH=src python -m kontexte preview fete-sorciere --role sorciere --lang en --out /tmp/witch.html
```

Open `examples/site/index.html` or `/tmp/witch.html`. A generated role preview is a **static presentation**, not a student's authenticated mission session. Not all strings are translated; the current catalogue originated in `fr-CA` and falls back where the `en` value is missing.

## 4. Export integration intent

```bash
PYTHONPATH=src python -m kontexte orgo-blueprint fete-sorciere --out /tmp/witch.blueprint.json
PYTHONPATH=src python -m kontexte orgo-fixture fete-sorciere --out /tmp/witch.scenario.json
PYTHONPATH=src python -m kontexte curriculum fete-sorciere --out /tmp/witch.curriculum.json
```

The **blueprint** is declarative intent. The **fixture** is a synthetic Orgo initializer that creates an initial Case and preparation Task, **not** a fully orchestrated celebration. The **curriculum report** contains candidate links to the experimental Ekole internal catalogue, not official ministry mappings.

## 5. Optional installation

```bash
python -m pip install -e .
kontexte validate
```

Editable installation can simplify local development but is not required. If this project is later published or packaged, follow its final dependency and licensing policy.

## Next steps

Read [Core Concepts](Core-Concepts), [Scenario Catalogue](Scenario-Catalogue), [Roles and Missions](Roles-and-Missions), and [Orgo Integration](Orgo-Integration).
