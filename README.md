# Kontexte

**Reusable situations, adaptive roles, and culturally localized learning experiences — designed for Orgo and Ekole.**

> **NEW in Kontexte 0.4:** run the interactive, teacher-only **Local Scenario Studio** with `START_KONTEXTE.bat` (Windows) or `./start_kontexte.sh` (macOS/Linux). Open `http://127.0.0.1:8769/` to browse the 60 Québec frames, simulate a solo or paired mission, calculate fictional Klownkoins and record synthetic practice evidence. See [Release 0.4](docs/RELEASE_0_4.md) and the [Studio wiki guide](wiki/Local-Scenario-Studio.md). This is **not** an authenticated classroom app or a second Orgo orchestrator.

Kontexte describes *what could happen*: a situation, its actors, competing needs, resources, distributed information, potential actions, and learning opportunities. **Orgo is the sole orchestrator** of the actual work, whether a mission has one participant or an entire school. **Ekole owns educational knowledge, curriculum references, and learning evidence.**

> **Project status:** experimental prototype, not a production classroom system. The Python package identifies as `0.4.0`; the repository also includes the culturally neutral scenario catalogue **v0.2** and the Québec Grade 3 design overlay **v0.3**. These are content/design versions, **not** evidence of certified curriculum coverage or end-to-end multi-student execution.

## The idea in one diagram

```text
Culturally neutral scenario (the reusable problem)
             +
Cultural and educational overlay (e.g., Québec / Grade 3)
             +
Role perspective and presentation (CSS, vocabulary, artifacts)
             |
             v
KONTEXTE -- defines and renders a situation; exports integration intent
             |
     +-------+-------+
     |               |
     v               v
   ORGO             EKOLE
   operational      knowledge, exercises,
   states, timing,   curriculum mapping,
   tasks, signals    and learning evidence
```

A **role is a perspective**, not a computer permission or an ability label. A **scenario is a reusable problem**, not a hard-coded timetable of school subjects. A situation may involve mathematics, languages, art, movement, social coordination, and media creation at once. Learners can share the same outward role while receiving different private scaffolding and challenge levels.

## What is included

| Component | Present in this repository | Important limit |
| --- | --- | --- |
| Role library | **38** JSON role definitions, including witch, baker, origami maker, scientist, messenger, stage manager, and photographer | Educational roles never grant system permissions |
| Mission definitions | **11** mission records: one detailed interdisciplinary pilot, one solo example, nine outlines | Descriptions are not fully compiled Orgo workflows |
| Neutral scenarios | **60** concise, culturally neutral scenario frames across ten families | Design seeds, not ready-to-run activities |
| Québec / Grade 3 overlay | **60** localized frames, **83** internal candidate objectives, **36** proposed planning weeks, and **34** supplemental micro-situations | Planning inventory, **not** ministry-approved Grade 3 coverage |
| Local Studio 0.4 | Loopback teacher/developer rehearsal for 60 overlays, 15 arithmetic checks, solo/duo tasks, imaginary finances and synthetic evidence | No student accounts, real clue security, or task orchestrator |
| Static HTML | Role-based `fr-CA` and `en` previews, escaped text, allowlisted CSS themes | Static pages are not authenticated student sessions |
| Orgo integration | Synthetic `orgo.scenario.v1` fixture and a declarative blueprint | The fixture creates only an initial Case and preparation Task |
| Ekole mapping | Checks internal references from the experimental 202-Kristal catalogue | Official Québec curriculum mappings remain unreviewed |
| Other prototypes | Fictional Klownkoin calculations, consent-aware media manifest, local SQLite evidence example | No real payments, media hosting, student accounts, or official assessments |

## One-click Windows launch

Double-click `START_KONTEXTE.bat` from the extracted repo. It checks Python, starts the local Studio and opens your browser. `TEST_KONTEXTE.bat` runs automated tests; `GENERER_SITE.bat` regenerates the static previews; `CHECK_ORGO_FIXTURE.bat` validates the approved test fixture if `ORGO_ROOT` points to an Orgo checkout. All launchers are included, see [Release 0.4](docs/RELEASE_0_4.md).

## Quick start

**Requirements:** Python **3.10+**. The basic commands use the Python standard library and run locally. From the extracted repository root (`Kontexte/`):

```bash
# macOS / Linux
PYTHONPATH=src python -m kontexte validate
PYTHONPATH=src python -m kontexte list
PYTHONPATH=src python -m kontexte site --out examples/site --lang en
PYTHONPATH=src python -m unittest discover -s tests -v
```

```powershell
# Windows PowerShell
$env:PYTHONPATH = "src"
python -m kontexte validate
python -m kontexte list
python -m kontexte site --out examples/site --lang en
python -m unittest discover -s tests -v
```

Open `examples/site/index.html` locally. Some interface labels and source content remain in Canadian French; `--lang en` selects translated values **where they exist** and may fall back to `fr-CA`. It does not automatically translate or validate text.

Optionally install the package with `python -m pip install -e .` and use `kontexte` instead of `python -m kontexte`.

### Try one mission

```bash
# Show one role's public-safe preview
PYTHONPATH=src python -m kontexte preview fete-sorciere --role sorciere --lang en --out /tmp/witch.html

# Export a proposed workflow blueprint (NOT executable)
PYTHONPATH=src python -m kontexte orgo-blueprint fete-sorciere --out /tmp/witch.blueprint.json

# Export a minimal synthetic fixture recognized by the Orgo scenario injector
PYTHONPATH=src python -m kontexte orgo-fixture fete-sorciere --out /tmp/witch.scenario.json

# Export candidate internal curriculum links; not official PFEQ identifiers
PYTHONPATH=src python -m kontexte curriculum fete-sorciere --out /tmp/witch.curriculum.json
```

The special `preview --demo-fragments` flag exposes **fictional** role-held information for offline development only; **never** use it to serve real participants. Orgo is expected to authorize disclosure in a future secure runtime.

### Run the local utilities

```bash
PYTHONPATH=src python -m kontexte bill --input examples/klownkoins.json --out /tmp/bill.json
PYTHONPATH=src python -m kontexte privacy --input examples/consent-refusal.json --out /tmp/privacy.json

# Fake participant IDs and a development-only SQLite database
PYTHONPATH=src python -m kontexte evidence-add --input examples/evidence-fixture.json --db /tmp/kontexte-dev.sqlite
PYTHONPATH=src python -m kontexte evidence-report --db /tmp/kontexte-dev.sqlite --student eleve-fixture-001 --out /tmp/evidence.json
```

**B5 Québec Grade 3 update (isolated):** new audit/export commands `qc3-audit-b5` and `qc3-pilot-b5` produce a complete traceable candidate index and separate teacher-only/student-preview bakery materials. See [B5 documentation](docs/B5_KONTEXTE_3E.md). No real Orgo execution, student publication, or official program certification.

## The Québec Grade 3 extension

The neutral catalogue remains unchanged at `data/trames/catalogue-neutral-v0.2.json`. The localization layer at `data/locales/qc/fr-CA/grade3/` refers back to each parent scenario by `base_trame_id`, with catalogue and per-scenario checksums.

Its **60 overlays** describe Québec contexts, objects, materials, practical tasks, information fragments, and *candidate* educational goals. An indicative **36-week** planning sequence and **34** supplemental micro-situations are included. This is not 36 weeks of fully scripted lessons, and the internal 83-objective inventory is not an official list of ministry requirements.

Read [README_QC3.md](README_QC3.md) and the [Québec Grade 3 wiki page](wiki/Quebec-Grade-3.md).

## Tandem P1 — export enseignant Ekole (sans Orgo actif)

La commande `ekole-tandem-preview` génère un JSON strict `ekole.tandem-teacher-preview/1.0` pour un **aperçu uniquement synthétique**, sans indice privé ni élève réel. Orgo conserve toute autorité sur la création, l’affectation et les transitions opérationnelles. Voir [le contrat P1](docs/ekole-orgo/TANDEM_P1_EKOLE_PREVIEW_EXPORT.md).

## Orgo and Ekole integration

- **Orgo:** owns `Case`, `Task`, `Signal`, `WorkflowVersion`, release of information, participant coordination, and operational transitions. Kontexte exports synthetic initialization data and design intent; it **does not** run a competing mission state machine.
- **Orgo_Worlds:** provides versioned world/release context, distinct from Orgo task state.
- **Ekole:** supplies the experimental internal Kristal identifiers, exercises, and the future authorized evidence and curriculum mapping service. Completing an Orgo task **does not imply** mastery of a school competency.

To check a generated fixture from the **separate Orgo checkout**:

```bash
node tools/scenario-injector/cli.mjs validate /path/to/witch.scenario.json
node tools/scenario-injector/cli.mjs plan /path/to/witch.scenario.json
```

Applying a fixture mutates Orgo state; never run `--apply` except in an authorized synthetic/test world. No actual Orgo instance is started automatically by Kontexte.

## Repository layout

```text
Kontexte/
├── src/kontexte/                 Python validators, renderers, adapters, utilities
├── schemas/                      Role and mission JSON Schema
├── data/roles/                   38 role definitions
├── data/missions/                11 mission definitions
├── data/trames/                  Neutral v0.2 catalogue (60 frames)
├── data/locales/qc/fr-CA/grade3/  Québec Grade 3 v0.3 overlay and planning
├── data/catalogue/               Experimental Ekole reference data
├── integrations/orgo/            Synthetic fixture and design blueprint
├── integrations/ekole/           Candidate curriculum mappings
├── examples/                     Local demos and fictional fixtures
├── teacher-only/qc3/             Answers / educator materials: NEVER export to students
├── tests/                        Python unit tests
├── docs/                         Technical docs and archived Ekole–Orgo upgrade plan
└── wiki/                         English GitHub Wiki source pages
```

## Documentation

Start with the **[English Wiki](wiki/Home.md)** (a versioned Markdown mirror restored in `wiki/` for standalone clones; synchronize it explicitly with the external GitHub Wiki before publishing) for the conceptual guide, authoring conventions, localization, safety, and the current roadmap. The standalone files in `wiki/` can be pushed to a separate GitHub Wiki repository; GitHub **does not automatically publish** a repository's `wiki/` directory as its Wiki. See [Publishing the Wiki](wiki/Publishing-the-Wiki.md).

Additional materials: [Technical docs](docs/README.md) · [Orgo integration](wiki/Orgo-Integration.md) · [Ekole curriculum and evidence](wiki/Ekole-Curriculum-and-Evidence.md) · [Québec Grade 3](wiki/Quebec-Grade-3.md) · [Contributing](CONTRIBUTING.md).

## Safety and project limitations

**Not ready for real children or production institutions.** There is no authenticated classroom session, real multi-user information-release mechanism, permanent private media service, consent withdrawal/purge workflow, or official ministry reporting. Sample work, identifiers and currency must remain fictional.

Do not export `teacher-only/`, answer keys, student records, or other participants' hidden fragments. Consent denial must prevent **the original file, thumbnails, embedded metadata and identifying tags** from becoming publicly accessible: a CSS blur is not privacy protection. Real-world student movement and physical activity require educator supervision.

## License and contribution status

**No repository-wide license has been granted.** See [LICENSE-POLICY.md](LICENSE-POLICY.md) before copying, redistributing, or accepting third-party contributions. References to Orgo, Orgo_Worlds and Ekole do not grant rights to those projects or their source material.

---

**One sentence:** *Kontexte defines the experience; Orgo orchestrates what happens; Ekole documents what was learned.*
