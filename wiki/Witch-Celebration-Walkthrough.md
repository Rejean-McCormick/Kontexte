# Witch Celebration — Interdisciplinary Pilot

**Mission ID:** `fete-sorciere`  
**Suggested school year:** Québec elementary **Grade 3**, without treating the grade as an immutable restriction  
**Source:** `data/missions/fete-sorciere.json` and `docs/PILOTE_FETE_SORCIERE.md`

## Scenario

A fictional young witch plans a village celebration. Different participants hold different pieces of information. The group needs to make decorations, invite guests, organize a performance, manage a fictional budget, and decide what can be photographed or published.

| Activity | Observable product | Candidate learning opportunity |
| --- | --- | --- |
| Origami maker folds a witch hat | Paper model and description of shapes | Visual arts, geometry, sequence reading |
| Witch prepares invitations | French invitation | Writing, clarity and audience |
| Translator prepares a short English version | Bilingual invitation | Second-language communication |
| Messenger checks a designated participant's task and delivers invitations | Completed handoff with adult supervision | Communication, cooperation, orientation |
| Two holders exchange paper/invitation information | Joint quantity calculation | Division, subtraction, reasoning |
| Stage team splits four responsibilities | Script, oral reading, staging, decoration | Literacy, oral work, spatial planning |
| Accountant prepares the fictional bill | Klownkoin budget | Arithmetic and financial reasoning |
| Photographer documents work | Internal media candidates and consent records | Metadata, ethics and privacy |

These are **described educational opportunities**, not individually validated student skills.

## Information combination

One participant knows **six invitations are needed**. Another knows **two invitations fit per sheet and only two sheets are available**.

```
Sheets required = ceil(6 / 2) = 3
Sheets on hand = 2
Shortage = 3 - 2 = 1 sheet
```

The information fragmentation creates a cooperation problem. In the current JSON, a `join` describes what could unlock after the facts are combined. That join **does not yet execute** without Orgo's future secure condition mechanism.

## Klownkoin example

Four team contributions cost 6 fictional Klownkoins each, plus 8 for stage decoration:

```
4 × 6 + 8 = 32 Klownkoins
Optional fictional 10% tax = 3.20
Fictional total = 35.20
Starting budget = 55
Remaining = 19.80 Klownkoins
```

This tax rate is **made up for the scenario** and does not represent a Québec tax calculation or a required Grade 3 skill. It may be an educator-approved advanced exercise.

## Adaptable participation

The role name and scene remain outwardly the same. Internally, learners may receive manipulatives, icons, short instructions, supported oral input, normal challenges or richer multi-step tasks. The support profile is not a public indicator of medical status.

## Privacy and actual execution

Photographs are **not** automatically published. Missing or denied consent prevents files, thumbnails and identifying tags from becoming public. Moving furniture, meeting other participants and sharing food always require real adult oversight.

Today the generated Orgo fixture initializes **only a Case and preparation Task**; the complete handoff, fragment joins, staged work and publication lifecycle are **not live**. See [Orgo Integration](Orgo-Integration) and [Privacy and Media](Privacy-and-Media).
