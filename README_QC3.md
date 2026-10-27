> **Interactive browsing:** start the [Kontexte 0.4 Local Scenario Studio](docs/RELEASE_0_4.md) to explore the 60 Québec Grade 3 frames. The curricular mappings are still candidates, not approved.

# Kontexte — Québec Grade 3 Extension (v0.3)

This repository extends Kontexte's **60 culturally neutral scenario frames** with a **Québec / Canadian French / Grade 3 design overlay**. It is a localized planning and content layer, not a new mission runtime or an officially certified school curriculum.

## Preserve the neutral parent

```text
data/trames/catalogue-neutral-v0.2.json        Unmodified source catalogue
                     +
data/locales/qc/fr-CA/grade3/                    Québec / Grade 3 overlay
                     +
Orgo                                                 Operational orchestration
Ekole                                                Knowledge and validated learning evidence
```

Each localized scenario carries a `base_trame_id` and hashes for its parent catalogue and source frame. The **underlying problem and dependencies remain intact**, while the cultural setting, language, materials, examples, educational supports, and objectives may change.

## Inventory

| Inventory | Quantity | What it represents |
| --- | ---: | --- |
| Neutral scenario frames | 60 | Reusable problem patterns; no detailed lessons |
| Québec Grade 3 overlays | 60 | One documented localization per frame |
| Candidate internal objectives | 83 | Draft pedagogical tags to be checked against official curricula |
| Pilot scenarios in the annual plan | 32 | Editorial selections, not fixed subjects or class periods |
| Planning weeks | 36 | Indicative distribution across four internal Ekole stages |
| Supplemental micro-situations | 34 | Additional proposed coverage of internal objectives |
| Deterministic calculation exercises | 15 | Numerically checkable exercise fixtures |

The remaining 28 neutral scenarios provide options for extensions, replacements, or remediation. The 36-week plan is **not** a complete set of fully authored and teacher-reviewed lessons.

## Main files

| Path (relative to repository root) | Purpose |
| --- | --- |
| `data/trames/catalogue-neutral-v0.2.json` | Canonical, culturally neutral scenario catalogue |
| `data/locales/qc/fr-CA/grade3/profil-localisation.json` | Language, geographic context, units, inclusion and safety |
| `data/locales/qc/fr-CA/grade3/overlays-60.json` | Localized scenarios and parent identifiers |
| `data/locales/qc/fr-CA/grade3/objectifs-candidats.json` | Internal educational goals with Ekole Kristal references |
| `data/locales/qc/fr-CA/grade3/parcours-36-semaines.json` | Proposed annual sequencing |
| `data/locales/qc/fr-CA/grade3/micro-situations-34.json` | Supplemental activity concepts |
| `data/locales/qc/fr-CA/grade3/exercices-deterministes.json` | Calculation tasks and structured answers; use authorized audience filtering |
| `data/locales/qc/fr-CA/grade3/seances-a-completer.json` | Outstanding educational planning work |
| `docs/locales/qc3/` | Original design, integration and review notes (in French) |
| `teacher-only/qc3/` | Restricted answer keys and educator-only content |

## Example of inheritance

The parent frame `fete-commune` represents **a shared event requiring interdependent teams, distributed information, and constrained resources**. Its Québec overlay (`qc3-fete-commune`) proposes a school setting, locally relevant objects, grade-level problems, and learning evidence candidates. A witch or baker role can be layered on top without changing that core challenge.

```json
{
  "overlay_id": "qc3-fete-commune",
  "base_trame_id": "fete-commune",
  "localisation_id": "ca-qc-fr-primaire-3"
}
```

This excerpt identifies existing fields; it does not contain the entire overlay.

## What has *not* been established

- No claim of official approval by Québec's Ministry of Education.
- No proof that each Grade 3 requirement is covered at the correct depth; every `qc3.*` objective needs expert comparison to the official progression and evaluation frameworks.
- No automatic award of mastery or grades from attendance, task completion, or a generic scenario tag.
- No fully implemented Orgo workflow for distributing fragments or running class-wide missions.
- No student or media account system; no secure permanent gallery.
- No assumption that all Québec communities share the same language practices, celebrations, or cultural perspectives.

Sensitive Culture and Citizenship in Québec (CCQ) content needs appropriate direct teaching and safeguards; roleplay is not an adequate substitute for mandatory instruction. Tax percentages and fictional Klownkoin rates are optional enrichment, **not** automatic Grade 3 outcomes.

## Design and review sequence

1. Check parent-scenario hashes and overlay links before building derived assets.
2. Review local context and inclusion assumptions with relevant educators and communities.
3. Review the internal objective candidates against the applicable official program and progression, **by edition and Grade 3 expectation**.
4. Keep each participant's Orgo-authorized fragments and teacher answer keys out of public student HTML.
5. Create observations in a secure Ekole-controlled service; distinguish *covered*, *practiced*, *mastered*, and *validated*.
6. Conduct accessibility, safety, copyright, and classroom trials before any real deployment.

See the [English Québec Grade 3 Wiki page](wiki/Quebec-Grade-3.md), [Cultural Localization](wiki/Cultural-Localization.md), and [Ekole Curriculum and Evidence](wiki/Ekole-Curriculum-and-Evidence.md).
