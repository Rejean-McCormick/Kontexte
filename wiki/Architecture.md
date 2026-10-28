# Architecture

## One orchestrator, multiple domain lenses

The principal architecture decision is **ADR-001: Orgo is the sole orchestrator**. Kontexte must not create its own mission state machine or parallel task lifecycle.

```text
                  VERSIONED SITUATION DESIGN
Neutral trame + locale/grade overlay + role + mission frame
                            |
                     Kontexte adapters
              /             |              \
             v              v               v
   HTML/CSS presentation  Orgo intent     Ekole candidate links
       (authorized)          |                  |
                            v                  v
                         ORGO               EKOLE
                       Cases/Tasks       Knowledge/Kristals
                       Signals/Time      MiniLab/Evidence
                       Workflow state    Curriculum tracking
                            |
                     Operational events
                            |
                Authorized educational observations
```

## Responsibilities

**Kontexte** owns descriptive artifacts: role vocabularies, scenario frames, localizations, synthetic fixtures, static rendering, pedagogical design metadata, fictional accounting calculations, and media-publication decisions on metadata.

**Orgo** owns the state of actual work: participants, Cases, Tasks, Signals, workflow versions, timing, dependencies, transition guards, idempotency, cancellations, and delivery of the right information to the authorized person at the right moment. A solo mission is still an Orgo mission.

**Orgo_Worlds** provides a versioned world/release context distinct from live Case/Task state.

**Ekole** owns educational knowledge and validation authority: Kristals, exercises (MiniLab), official-curriculum mappings when reviewed, evidence records and teacher-facing reports.

## Current code versus intended integration

The existing Kontexte package **can** validate role/mission JSON, create offline HTML, calculate fictional bills, evaluate a metadata-only publication manifest, and generate a **minimal** synthetic `orgo.scenario.v1` fixture. It **cannot** automatically instantiate the entire interdisciplinary mission as a secure Orgo workflow or coordinate real student sessions.

The role is roughly analogous to a CSS skin, but its **descriptive vocabulary and task perspective** are structured data. The CSS theme never becomes an access-control rule.

## Versions and invariants

- Neutral trames are standalone, versioned data with stable IDs.
- A localized overlay references and verifies its parent identity and hash; changing the core problem should create a revised scenario or a reviewed migration.
- Orgo operational state is never inferred from a Kontexte HTML page.
- An Ekole learning outcome is never inferred solely from an Orgo completion signal.
- Teacher-only answers and other learners' fragments are excluded at the **data boundary**, not merely hidden with CSS.

The archived source design documentation is in `docs/ekole-orgo/` and the decision record is `docs/decisions/ADR-001-ORGO-CANONIQUE.md` (both in French).
