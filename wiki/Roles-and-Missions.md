# Roles and Missions

Roles give a common activity many possible perspectives. The scenario remains the same problem, but the learner may view it as a **witch, baker, mechanic, scientist, stage manager, photographer, or origami maker**. A role can be chosen for a single task rather than a whole term.

## A role record

Role definitions live under `data/roles/*.json`, in the `kontexte.role/1` format. The records contain localized names and introductions, a theme ID, actions, objects, typical problems and partners.

```json
{
  "format": "kontexte.role/1",
  "id": "sorciere",
  "name": {"fr-CA": "Sorcière", "en": "Witch"},
  "intro": {
    "fr-CA": "créer des objets imaginaires, enquêter, organiser une fête",
    "en": "You are playing the role of witch in a learning story."
  },
  "theme": "sorciere",
  "actions": ["..."],
  "objects": ["..."],
  "problems": ["..."],
  "partners": ["..."]
}
```

The `...` values above mark an **illustrative abbreviated record**, not a valid file ready for `validate`. Use the complete files and `schemas/role.v1.schema.json` when editing. The theme must be on the renderer's allowlist.

## A mission record

Mission files use `kontexte.mission/1` in `data/missions/`. A mission has a fiction, one or more roles, steps with dependencies, distributed information (`fragments`), possible fragment joins (`joins`), private support profiles, and candidate curriculum links.

The detailed pilot `fete-sorciere` uses **10 roles** and **11 described steps**. The repo also includes `sorciere-solo` and nine more skeletal missions. Only the pilot has extensive authored cross-subject connections; outlines should not be described as turnkey lessons.

Important fields:

- `synthetic`: these examples are deliberately fictional.
- `roles`: roles participating in the scenario, not security principals.
- `steps[*].depends_on`: intended ordering of steps in the authored design.
- `steps[*].curriculum_ids`: internal Ekole catalogue IDs to be reviewed.
- `fragments[*].holder_role`: intended information holder; **not** authentication.
- `joins[*].unlock_step`: desired consequence after a specified combination.
- `adaptation`: assisted, standard and extended support descriptions.

## Three different kinds of “ready”

1. **Structurally valid:** JSON and references satisfy the Kontexte validator.
2. **Pedagogically reviewed:** An educator has checked level, objectives, instructions, support and evaluation.
3. **Executable and safe:** The Orgo process, accounts, guards, disclosures, teacher approvals and evidence flows work under real security controls.

Current mission files largely meet the first description only. The current Orgo fixture creates an initial Case and preparation Task — **not** the complete set of steps.

## Authoring principles

- Every task should produce a meaningful observable artifact or change in the situation.
- Put key information in multiple places *only when* cooperation or discovery is an intentional learning mechanism; include a safe fallback if a partner is absent.
- Use interdisciplinary tasks without claiming every involved subject was mastered.
- Make difficulty and supports private. Keep the same public role and narrative for different learner needs.
- Gate real spending, food, movement, media and physical setups behind an authorized educator.

See [Witch Celebration Walkthrough](Witch-Celebration-Walkthrough), [Adaptive Participation](Adaptive-Participation), and [Development and Testing](Development-and-Testing).
