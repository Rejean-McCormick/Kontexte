# Core Concepts

Kontexte describes **situations**, not subject-specific worksheets. The learning experience may span multiple competencies at once while remaining traceable to the curriculum.

| Concept | Meaning | Authority / location |
| --- | --- | --- |
| **Neutral scenario / frame** | Minimal reusable problem: trigger, tension, participants, information, actions, result | `data/trames/catalogue-neutral-v0.2.json` |
| **Cultural overlay** | Local setting, language, objects and culturally appropriate variations referring to a neutral parent | `data/locales/.../overlays-60.json` |
| **Role** | A narrative identity, vocabulary, activities, objects and CSS presentation | `data/roles/` |
| **Mission definition** | Fiction, steps, fragments, joins, roles and candidate curriculum links | `data/missions/` |
| **Fragment** | A piece of information a participant may hold | Declared by Kontexte; released only by an authorized runtime |
| **Join** | Intended condition where fragments combine to open a step | Design intent; must be implemented within Orgo |
| **Participant** | An actor whose real identity and permissions must be resolved securely | Future authenticated school/Orgo integration |
| **Task / Case / Signal** | Operational assignments, contexts and events | **Orgo**, not Kontexte |
| **Learning evidence** | Observation, practice, mastery review or validation associated with a curriculum target | **Ekole** / authorized educational service |
| **Artifact** | A physical or digital product: invitation, origami, poster, speech, calculation or photo | Mission output; media rights handled separately |

## Neutrality versus localization

A neutral scenario can say, “Several teams must organize a gathering with limited resources.” A Québec adaptation might place it in a school library and gymnasium, use Canadian metric units, propose a Francophone/Bilingual invitation, and link to Grade 3 candidate objectives. A witch-themed role may add hats and imaginary lanterns. The underlying dependency is still **shared resources + missing information + coordination**.

Neutral does **not** mean culturally context-free in an absolute sense. The catalogue aims to avoid unnecessary assumptions, while overlays require local review and respect for community-specific knowledge.

## What changes during execution?

The presence of a scenario definition does not send messages, unlock a new activity or mark a Task completed. **Orgo must decide when, why, and to whom information is released.** The current code describes these intentions but does not yet compile them into secure, durable multi-user workflows.

## Three learning distinctions

- **Covered:** The learner actually encountered a target concept.
- **Practiced:** The learner carried out a task or attempt involving that concept.
- **Mastered / validated:** There is appropriate evidence and an authorized review under documented criteria.

An operational task's `COMPLETED` status is **not** sufficient to infer mastery. See [Ekole Curriculum and Evidence](Ekole-Curriculum-and-Evidence).
