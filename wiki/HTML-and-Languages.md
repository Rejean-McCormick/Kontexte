# HTML, CSS Themes and Languages

Kontexte's role layer is **similar to a CSS skin**, but it also carries language, objects, role-specific tasks, and narrative perspective. The aim is to render a controlled HTML experience from semantic fields instead of letting a generative model invent every page independently at runtime.

## Implemented renderer

`src/kontexte/render.py` assembles static HTML from validated role/mission records. Its key protections include escaped text and allowlisted themes. The default role preview does **not** reveal declared hidden fragments.

```bash
PYTHONPATH=src python -m kontexte preview fete-sorciere \
  --role sorciere --lang en --out /tmp/witch.html

PYTHONPATH=src python -m kontexte site \
  --out /tmp/kontexte-site --lang en
```

The currently recognized language choices for these commands are **`fr-CA` and `en`**. A missing translation falls back to the original; this is a visible fallback, **not** a reviewed translation or completed multilingual support.

## What is not implemented

- A general AI-to-HTML authoring and approval pipeline.
- A fully interactive lesson-component system with authenticated student state.
- Arbitrary HTML or JavaScript execution from scenario fields.
- A qualified SemantiK translation pipeline for all languages and texts.
- Live, per-recipient fragment authorization in the static HTML generator.

Any future structured rich content should be limited to reviewed components, safe CSS tokens, accessible semantic markup, and verified translations. Do not render untrusted generated HTML directly into a child-facing session.

## Internationalization guidelines

Keep the **underlying facts, numeric values, and target outcomes** stable while localizing explanatory language. Mark units, calendar conventions, currency conventions, idioms and uncertainty explicitly. A localized task must be reviewed for cultural appropriateness as well as grammatical accuracy.

If a word or scenario has no suitable equivalent in a receiving culture, rewrite the scene under a reviewed overlay rather than pretending the terms are interchangeable. See [Cultural Localization](Cultural-Localization).

## Hidden information is not a CSS effect

Even a hidden HTML element is downloadable source data. The safe approach is **do not send content to that participant until a trusted service authorizes its release**. In the current repository, fragment preview is limited to synthetic offline demonstrations (`--demo-fragments`) and must not be deployed as an authorization control.
