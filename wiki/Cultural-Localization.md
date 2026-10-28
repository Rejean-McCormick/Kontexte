# Cultural Localization

The purpose of localization is **not to translate a story word by word**. It is to preserve a reusable problem while adapting its setting, materials, practices, languages, expectations and educational references to a real community.

## Two-layer model

```text
Neutral frame: Why is a task difficult? Which dependencies create the tension?
                      +
Locale / grade overlay: Which setting, artifacts, participants, supports and goals fit here?
                      +
Role skin: Which fictional or professional identity makes the experience meaningful?
```

The neutral frame `fete-commune` can support a celebration of original student inventions, a local school exhibition, or a fictional village festival. No particular religious or cultural occasion should be presumed to represent everyone in Québec.

## Source and inheritance

The neutral file is `data/trames/catalogue-neutral-v0.2.json`. The Québec Grade 3 collection has 60 items under `data/locales/qc/fr-CA/grade3/overlays-60.json`, each with:

- an `overlay_id` unique to the localized variant;
- a `base_trame_id` linking back to a neutral frame;
- `neutral_parent` checksums identifying the exact reviewed source version;
- `localisation_id`, grade and suggested stage;
- localized context, activities, objects, learning goals and safety constraints.

The `inheritance` convention is **overlay by parent ID, do not mutate the neutral source**. The catalogue checksum prevents accidentally applying a reviewed adaptation to a changed parent without migration review.

## What may change?

**Usually variable:** setting, language, traditional and contemporary objects, materials, weather, measures, accessible activities, relevant professions, local events, narrative skin, presentation style and optional learning support.

**Must be preserved or explicitly reviewed:** the central problem, the participant dependencies, the purpose of information fragmentation and the type of successful outcome. Otherwise the writer has created a substantially different scenario.

## Cultural and historical safeguards

Localization for Québec should account for **urban, rural, coastal and northern settings**, many linguistic communities, and diverse family circumstances. Indigenous peoples and their traditions must not be flattened into a generic “Québec culture,” treated as interchangeable, or turned into make-believe without relevant permission and contextual review. A culturally neutral frame does not by itself confer authority to reproduce protected knowledge.

## Important implementation status

The v0.3 repository contains well-structured **overlay data, hashes and review documentation**, but its Python CLI does **not yet expose** a general `resolve(base_id, locale, grade)` subcommand that creates a full Orgo experience. The original Québec overlay package included a separate offline verifier; the integrated repo retains the localized JSON and tests. Do not claim live runtime localization merely from the presence of files.

Review [Québec Grade 3](Quebec-Grade-3) and [HTML and Languages](HTML-and-Languages).
