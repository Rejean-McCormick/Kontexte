# Ekole Curriculum and Learning Evidence

The Québec school framework is used here primarily as a **reference and evidence register**. It should show educators exactly which targets were encountered, practiced, demonstrated, and reviewed during an interdisciplinary mission, even when the learner's activity did not follow a subject-by-subject timetable.

## What is in the repository

`data/catalogue/202_kristals.json` contains **202 experimental internal Kristals** from the supplied Ekole snapshot; this is **not** a ministry-sanctioned curriculum listing. The CLI's `curriculum` command verifies internal IDs and exports candidate links:

```bash
PYTHONPATH=src python -m kontexte curriculum fete-sorciere --out /tmp/witch.curriculum.json
```

Fields such as `official_pfeq_id` remain `null` until a qualified review establishes an exact mapping to the applicable official program and its version. An authored curriculum tag **is not evidence that teaching occurred**.

## Five evidence statuses

| Status | Interpretation |
| --- | --- |
| `observed` | An observation was recorded |
| `covered` | A concept was actually encountered |
| `practiced` | A learner attempted an activity involving it |
| `mastered` | Evidence of independent or specified performance has been reviewed appropriately |
| `validated` | Criteria-based validation has been recorded by an authorized reviewer |

The prototype's example evidence module rejects `mastered`/`validated` records without a `human_review` flag and reviewer ID. **It cannot verify the reviewer's real-world authority**; that will require an institutional service and access policy.

## Development-only exercise

```bash
PYTHONPATH=src python -m kontexte evidence-add \
  --input examples/evidence-fixture.json \
  --db /tmp/kontexte-dev.sqlite

PYTHONPATH=src python -m kontexte evidence-report \
  --db /tmp/kontexte-dev.sqlite \
  --student eleve-fixture-001 \
  --out /tmp/learner-report.json
```

These commands use **fictional participant identifiers** and SQLite for demonstration. Do not store real children's data in the example database, commit it, or treat it as a production gradebook.

## Future evidence chain

1. Kontexte identifies a **candidate** learning target for a mission step.
2. Orgo orchestrates the action, interaction and artifact handoff.
3. An authorized component records what the learner actually did, including assistance provided and evidence references.
4. Ekole checks the target, applicable grade, evaluation criteria, provenance and permitted reviewer.
5. Teacher-facing reports separate participation and coverage from validated mastery.
6. Institution-facing reporting is subject to explicit authorization and appropriate aggregation; there is no automatic ministry feed.

For multi-grade events, each child receives a grade-appropriate mapping to the **same shared event**, with no assumption that every participant worked on the same objective.

See [Québec Grade 3](Quebec-Grade-3) and [Privacy and Media](Privacy-and-Media).
