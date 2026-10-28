# Roadmap and Limitations

## October 27, 2026 — source-verified update

The older sections below are retained for context; read the current code-backed checkpoint: [Source-verified code status — October 27, 2026](Code-Status-2026-10-27).

**Version 0.4 includes local teacher-only Studio and a synthetic Tandem P1 handoff; it neither dispatches Orgo tasks nor authorizes classroom usage.**


The project is a **working prototype of scenario data, static projections and supporting tools**. Several important runtime and institutional capabilities remain design proposals.

## Shipped in the source snapshot

- 38 role definitions and 11 mission definitions, with one detailed interdisciplinary pilot and one solo example.
- 60 neutral scenario frames (v0.2) and 60 Québec Grade 3 localized overlays (v0.3).
- Draft 83-objective index, 36-week planning sequence and 34 supplemental micro-situations.
- JSON validation and static HTML preview for supported `fr-CA`/`en` fields.
- A minimal synthetic Orgo Case/Task injector fixture and a non-executable blueprint.
- Candidate internal Ekole curriculum mappings, deterministic fictional calculations and development evidence tools.
- A restrictive media-manifest publication decision and offline software tests.

## Planned: general Orgo improvements

1. Compile a reviewed situation/mission frame into a **versioned Orgo process or workflow**.
2. Authorize person-specific information fragments and release them at the correct time.
3. Evaluate multi-fragment conditions robustly, including absence, cancellation, replay and duplicate events.
4. Establish identities, teacher permission gates and audit logs for multi-student use.
5. Emit secure observation events for an authorized educational evidence service.
6. Test concurrency, restart and recovery with an actual running Orgo deployment.

These belong to **Orgo as generic orchestration primitives**, so professional simulations can use them too.

## Planned: educational integration

- Educator-reviewed mappings to the correct version and grade columns of official Québec curriculum material.
- Authoring and secure delivery of complete accessible lesson components and controlled translations.
- Authenticated learner sessions, reviewable portfolios and a real institutional evidence service.
- A secure media pipeline with consent by asset and audience, withdrawal, deletion and cache purge.
- Trials with educators and learners to measure accuracy, inclusion and educational outcomes.

## Explicit non-goals

- Duplicating Orgo's mission state machine inside Kontexte or Ekole.
- Giving a fictional role any real system permission.
- Using a fictional tax or Klownkoin balance as a real transaction.
- Inferring medical status or publicly exposing support level.
- Treating completion, a scenario tag or a test pass as official mastery.
- Publishing children's media by default.
- Claiming ministry approval or operating a ministry reporting interface that does not exist.

See [Architecture](Architecture), [Privacy and Media](Privacy-and-Media) and [Ekole Curriculum and Evidence](Ekole-Curriculum-and-Evidence).
