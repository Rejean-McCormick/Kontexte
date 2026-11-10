# Final-system education boundary — Kontexte

**Scope:** `FC-10` / source-side of the **synthetic teacher-preview** chain. **Evidence:** executable local code and tests in this repository; no Orgo, Moodle or pupil deployment is established.

## State ownership and contracts

- Kontexte owns fictional/localized situation definitions and roles. It does not own Orgo Cases, Tasks, teacher authorization or student mastery records.
- The existing `kontexte.mission/1` source is used to export `ekole.tandem-teacher-preview/1.0` through `src/kontexte/tandem.py`.
- The exporter now requires explicit synthetic safety: `real_spending=false`, `real_taxes=false`, `publication_default=private`, plus a bounded, unique list of role references. Absence of safety rules is not interpreted as permission.
- The preview contains only permitted metadata, task identifiers, role identifiers and initial `ready` or `waiting` states; no clues, media, pupil identifiers or live effects.
- Kompose independently checks the preview against the original mission, including order, dependencies, initial states and empty fragment references. Akor later invokes the **real** Kompose and Ékole checks, not a copied school authority.

## Validation and remaining gates

Run `PYTHONPATH=src python -m unittest discover -s tests -v`. In the supplied branch test harness, synthetic real-owner tests also exercise Kontexte→Kompose→Ékole→Akor. There is no accepted Orgo runtime execution boundary in this snapshot. Real dispatch would require the Branch 05 Orgo owner, a signed/adopted exact command profile, authenticated identity/WorldRelease, teacher authorization and terminal receipts. Do **not** promote a successful preview to a child-facing activity or grade.
