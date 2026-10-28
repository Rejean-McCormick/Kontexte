# Local Scenario Studio (Kontexte 0.4)

The Studio is a **teacher/developer rehearsal tool running on localhost**, not an authenticated classroom website and not an Orgo replacement.

## Launch

On Windows, unzip Kontexte and double-click `START_KONTEXTE.bat`. On macOS/Linux, execute `./start_kontexte.sh`. Or run:

```bash
PYTHONPATH=src python -m kontexte doctor
PYTHONPATH=src python -m kontexte lab --port 8769
```

The browser opens `http://127.0.0.1:8769/`. Python 3.10+ is required; no Docker, Node.js, network account or Internet connection is required.

## Explore

- **60 scenarios:** browse the neutral frame beside the Québec Grade 3 overlay and both fictional information fragments. The exercise checker is enabled only when the overlay has a reviewed arithmetic fixture; other tasks require human evaluation.
- **Solo mission:** the witch measures 2, 4 or 8 fictional 125 mL vials, based on a private adaptation setting. Arithmetic feedback is practice-only.
- **Two-person rehearsal:** manually reveal the witch and messenger's clues in one browser. The UI only *depicts* a join; it is not Orgo-controlled collaboration.
- **38 roles:** browse reusable role actions, objects and tensions.
- **36 weeks / school-wide event:** browse indicative Québec Grade 3 planning and a kindergarten-to-Grade 6 event design.
- **Tools:** calculate fictional Klownkoins and validate privacy refusal.
- **Evidence:** store synthetic practice events under `demo-001` or `demo-002` in `.local/studio-demo.sqlite`. No mastery or validated status can be recorded by the Studio.

## Operational safety

The lab is restricted to `127.0.0.1` and **has no login**. Do not enter real child names, media, personal records or secrets. Never open it to a classroom network. The `/api/scenario` endpoint exposes **both** fictitious clues for authoring and must not be used as a student channel.

To operate real classroom activities, Orgo needs authenticated individual task permissions, fragment release and conditional joins; Ekole needs reviewed curriculum mappings and an authorized evidence service.

See [Orgo Synthetic Workflow](Orgo-Synthetic-Workflow), [Privacy and Media](Privacy-and-Media), and [Roadmap](Roadmap-and-Limitations).
