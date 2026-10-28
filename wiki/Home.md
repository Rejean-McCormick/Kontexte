# Kontexte Wiki

**Code snapshot status (October 27, 2026):** Version 0.4 includes local teacher-only Studio and a synthetic Tandem P1 handoff; it neither dispatches Orgo tasks nor authorizes classroom usage. See [Source-verified code status — October 27, 2026](Code-Status-2026-10-27) for source evidence and limitations.


**Design reusable situations. Adapt them to cultures and learners. Let Orgo orchestrate the work, and let Ekole document the learning.**

Kontexte is an experimental authoring and integration framework for role-based, interdisciplinary experiences. It is intentionally **not** another workflow engine, school management platform, or official Québec curriculum.

## Release 0.4: executable local Studio

Open [Local Scenario Studio](Local-Scenario-Studio) for an interactive teacher-only rehearsal of all 60 localized frames, solo/duo exercises, fictional accounting and demonstration evidence. The [Orgo Synthetic Workflow](Orgo-Synthetic-Workflow) defines what can be validated by the real Orgo injector. Neither surface is a production classroom application.

## Start here

| If you want to… | Read |
| --- | --- |
| Run the code and generate a preview | [Getting Started](Getting-Started) |
| Understand the three-system separation | [Architecture](Architecture) |
| Understand scenarios, roles, fragments and missions | [Core Concepts](Core-Concepts) |
| Create a reusable scenario idea | [Scenario Catalogue](Scenario-Catalogue) |
| Author a role or a mission | [Roles and Missions](Roles-and-Missions) |
| Adapt the same scenario to another culture | [Cultural Localization](Cultural-Localization) |
| Explore the existing Grade 3 Québec pack | [Québec Grade 3](Quebec-Grade-3) |
| See a cross-subject pilot | [Witch Celebration Walkthrough](Witch-Celebration-Walkthrough) |
| Connect Kontexte to a real orchestrator | [Orgo Integration](Orgo-Integration) |
| Relate activities to learning evidence | [Ekole Curriculum and Evidence](Ekole-Curriculum-and-Evidence) |
| Assess privacy and child safety | [Privacy and Media](Privacy-and-Media) |
| Review what works and what is missing | [Roadmap and Limitations](Roadmap-and-Limitations) |

## Version map

- **Python package / local Studio `0.4.0`:** 38 roles; 11 mission definitions; HTML previews and local utilities.
- **Culturally neutral catalogue `0.2.0`:** 60 concise problem frames in ten families, explicitly marked as **non-executable scenario ideas**.
- **Québec Grade 3 overlay `0.3.0`:** 60 localized overlays, 83 internal candidate objectives, a suggested 36-week plan and 34 micro-situations. Not a verified Grade 3 curriculum.

These are separate versioned artifacts, not a single uniform maturity level.

## The central responsibility split

```text
KONTEXTE  definitions, roles, content and design projections
ORGO      Cases, Tasks, Signals, timing, recipients and state transitions
EKOLE     knowledge, exercises, curriculum mappings and evidence
```

An individual activity and a school-wide event use the **same Orgo orchestration principles**. Kontexte deliberately creates and simulates problems so that these principles can be tested in a controlled learning setting, without claiming that the integration is production-ready.

## Important caution

The current repository contains demonstrations and design records only. It has **no authenticated classroom system, no production media gallery and no permission to publish children's records**. Do not use the static site generator to distribute teacher answers or real multi-user secrets.

For implementation and wiki-publication instructions, see [Development and Testing](Development-and-Testing) and [Publishing the Wiki](Publishing-the-Wiki).
