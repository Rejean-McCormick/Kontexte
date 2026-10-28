# Québec Grade 3 — Design Overlay v0.3

This is the **first thoroughly inventoried localization layer** for Kontexte: Québec, Canadian French, Grade 3 of elementary school (second cycle). It is intended to sit *above*, not replace, the culturally neutral catalogue.

## Inventory and educational status

| Item | Count | Status |
| --- | ---: | --- |
| Neutral parent frames | 60 | Reusable non-executable scenario ideas |
| Québec overlays | 60 | Authored local design records |
| Internal learning objectives | 83 | **Candidate** objectives to compare with official grade-level progression |
| Main frames in sample annual plan | 32 | Editorial selection |
| Suggested planning weeks | 36 | **Not** an official Québec school calendar |
| Supplemental micro-situations | 34 | Extra concept coverage |
| Calculation exercises | 15 | Structured exercises with deterministic numeric answers |

This is **inventory completeness**, not evidence of exhaustive official curriculum compliance, classroom readiness, or actual student mastery.

## Design resources

- `data/locales/qc/fr-CA/grade3/overlays-60.json` — localized scenario objects.
- `data/locales/qc/fr-CA/grade3/objectifs-candidats.json` — draft education objectives and internal Ekole Kristal references.
- `data/locales/qc/fr-CA/grade3/parcours-36-semaines.json` — non-binding planning distribution across four *internal* Ekole stages.
- `data/locales/qc/fr-CA/grade3/micro-situations-34.json` — targeted supplement ideas.
- `data/locales/qc/fr-CA/grade3/programmes-exigences.json` — selected official-reference notes, especially for Culture and Citizenship in Québec (CCQ).
- `data/locales/qc/fr-CA/grade3/seances-a-completer.json` — topics requiring further lesson planning.
- `data/locales/qc/fr-CA/grade3/exercices-deterministes.json` — checkable mathematical scenarios; **filter by audience**.
- `teacher-only/qc3/` — answer and correction material; never part of a student or public export.
- `docs/locales/qc3/` — the original French implementation, sources and pedagogical validation notes.

## Subjects are tracked, not siloed

A single frame can call for French reading and writing, English greetings or invitations, mathematics, art, science, physical activity and CCQ practices in a coherent event. **The school framework is an assessment map, not a constraint forcing the scenario into one subject per hour.**

Examples of candidate work include counting and grouping quantities, measuring materials, composing invitations, explaining procedures, comparing observations, and coordinating responsibilities. Assigning a candidate objective to a task does **not** prove that the student completed it.

## A whole-school event may have a Grade 3 entry point

A localized Grade 3 overlay may say that other years can participate. That does not make the Grade 3 requirements applicable to kindergarten or Grade 6. An authorized implementation should track **each participant against their own grade-relevant targets**, while Orgo coordinates a single event. Kindergarten and Grade 6 may produce complementary artifacts in the same story.

## Required reviews

1. Check **each** internal objective against the applicable official Québec program, *Progression of Learning*, grade column, and evaluation framework.
2. Distinguish a normal Grade 3 target from optional enrichment. For example, fictional sales tax percentages should not automatically be marked as required Grade 3 mastery.
3. Review CCQ topics with appropriate educator expertise; sensitive mandatory content cannot be replaced by unsupervised roleplay.
4. Verify historical and cultural representation, especially distinctions between Indigenous nations, times and perspectives.
5. Verify the arts subjects that are actually taught at the receiving school.
6. Complete accessibility review, feedback strategies, corrections, safety and classroom trials.

No official ministry affiliation, approval, grading connection or automatic certification is claimed.

Next: [Witch Celebration Walkthrough](Witch-Celebration-Walkthrough), [Ekole Curriculum and Evidence](Ekole-Curriculum-and-Evidence).
