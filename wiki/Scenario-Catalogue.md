# Scenario Catalogue — 60 Neutral Frames

Kontexte v0.2 contains **60 culturally neutral scenario seeds** in `data/trames/catalogue-neutral-v0.2.json`. The source is a French-Canadian JSON record with the format identifier `kontexte.catalogue-trames/1` and status `idees_de_scenarios_non_executables` — literally, **non-executable scenario ideas**.

## Why minimal frames?

An activity should begin with the **problem structure**, not finished prose or illustrations. A frame captures the smallest reusable logic from which different settings, grades, role skins, and participation patterns can be derived.

Example source frame (translated for this Wiki):

| Field | Example: shared celebration |
| --- | --- |
| Scenario ID | `fete-commune` |
| Trigger | A shared celebration is announced |
| Tension | Several teams depend on each other's preparations |
| Information to combine | Needs + available resources |
| Typical actions | Make, invite, organize, deliver |
| Expected outcome | An event and shared productions |
| Possible follow-up | A required material is missing |
| Suggested scope | Whole school, potentially kindergarten through Grade 6 |

The original frame also lists optional roles, possible subject domains, and variation axes. **Its roles are suggestions, not mandatory identities.**

## Ten families

1. **Events** — organize celebrations, performances or markets.
2. **Making and repair** — design, build or fix objects.
3. **Investigations** — combine clues or incomplete messages.
4. **Mutual aid** — support other participants and welcome newcomers.
5. **Environment** — gardens, living things, water and shared resources.
6. **Economy** — budgets, fictional money, allocations and tradeoffs.
7. **Communication** — invitations, news, translation and explanations.
8. **Science** — observations, fair comparisons and measurement.
9. **Movement and orientation** — routes, deliveries and spatial reasoning.
10. **Collective life** — decisions, responsibilities, rules and privacy.

These names describe the catalogue's intended grouping, not a new hard-coded enum in the Python runtime.

## Design checklist

A strong frame answers: *What changed? Who needs to act? What information is missing or split? Why is action difficult but possible? What artifact or observable change will result? What new tension could be released when the group succeeds?*

Do **not** attach specific laws, religions, foods, dates, languages or curricular competency codes to the neutral problem if those belong to a localized variant. Prefer a culturally reviewable overlay for that information.

## From a frame to an experience

1. Keep the `id` and central problem invariant.
2. Apply a cultural/educational overlay keyed by `base_trame_id`.
3. Choose accessible, optionally themed role perspectives.
4. Prepare steps, resources, clue fragments and alternate supports.
5. Have Orgo coordinate actual tasks and approved information release.
6. Have Ekole collect and validate educational evidence.

The existing v0.3 overlay is **data and documentation**; a generalized runtime resolver and full Orgo compiler remain planned. See [Cultural Localization](Cultural-Localization) and [Roadmap and Limitations](Roadmap-and-Limitations).
