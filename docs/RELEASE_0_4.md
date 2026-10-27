# Kontexte 0.4 — Local Scenario Studio and launchers

**Status: working development/lab release, not a deployable classroom platform.**

## What's genuinely new

- Local loopback-only Scenario Studio, standard-library Python HTTP server. Search all 60 culturally neutral scenarios and their Québec Grade 3 overlays. Read the two information fragments **in a teacher rehearsal only**; never send them to actual students from this endpoint.
- 38 role perspectives; 11 mission definitions; suggested 36-week planning; seven-level whole-school example (kindergarten through Grade 6).
- Usable, differentiated solo mathematics exercise and simulated two-person information-combination exercise with immediate *arithmetic practice* feedback. Profiles affect difficulty, but do not label public users.
- 15 existing Québec Grade 3 deterministic problems accessible through scenario views. Other open-ended tasks remain human-reviewed.
- Fictional Klownkoin budgeting with Decimal calculations and imaginary taxes; refuse-first media publication manifest.
- Development-only evidence ledger using synthetic `demo-001` / `demo-002` identifiers and **practice-only** statuses. The solo exercise now references the experimental multiplication Kristal `qc-pri-ma-008` instead of the unrelated addition reference.
- Cross-platform launchers: `START_KONTEXTE.bat`, `.ps1`, `start_kontexte.sh`; test/HTML generation and Orgo fixture Windows launchers.
- An Orgo synthetic review workflow fixture: `publish_workflow`, `create_signal`, `wait_signal`. It creates **review tasks only**; no conditional learning unlocks or real participant assignments.

## Quick test (Windows)

1. Unzip the full repository into a directory named `Kontexte`.
2. Install Python 3.10+ if necessary.
3. Double-click `START_KONTEXTE.bat`; the browser opens `http://127.0.0.1:8769/`.
4. Start with **Mission solo**; then **Mission à deux**; explore **60 trames**, **36 semaines** and **École entière**.
5. Stop the server with `Ctrl+C`. Use `TEST_KONTEXTE.bat` for automated checks.

No npm, Docker or internet connection is required for this *local rehearsal*.

## Command line

```powershell
$env:PYTHONPATH = 'src'
python -m kontexte doctor
python -m kontexte lab --port 8769
python -m unittest discover -s tests -v
python -m kontexte orgo-workflow-fixture fete-sorciere --out examples/orgo-workflow-review.json
```

Real Orgo dry-run, from the installed Orgo checkout (Node.js required):

```powershell
python -m kontexte orgo-check fete-sorciere --orgo C:\mycode\Orgo\Orgo --mode validate --workflow
python -m kontexte orgo-check fete-sorciere --orgo C:\mycode\Orgo\Orgo --mode plan --workflow
```

The above calls do **not** inject anything. Applying a workflow is a separate Orgo-authorized operation and requires Orgo's API and worker.

## Current boundaries

| Supported today | Not implemented as a production feature |
| --- | --- |
| Local scenario browsing and role previews | Authenticated children, teachers or multi-device workspaces |
| Solo numeric feedback and single-browser two-card rehearsal | Real Orgo-controlled private clues and conditional joins |
| Synthetic review workflow accepted by Orgo injector | Complete supervised student task lifecycle in Orgo |
| Fictional accounts and fail-closed manifest decisions | A secure school media gallery, asset storage and consent revocation propagation |
| Internal Ekole candidate links and lab SQLite evidence | Official PFEQ mapping, teacher authorization, grading or school records |
| French source strings; partial English content | Pedagogically reviewed translations across all contents |

## Safety notes

- The Studio binds to loopback, validates Host/Origin, requires a local per-process token for API writes, disables caching and does not allow real student identifiers.
- **The Studio has no user authentication.** Do not use it over a school network, expose its port, use actual child names or photos, or treat its locally simulated gates as access controls.
- `/api/scenario` returns both scenario fragments to the local **teacher lab**. It is not a student-facing endpoint.
- No teacher-only answer keys, confidential child artifacts or physical-media files are part of the public HTML build.
- Privacy isn't fixed by blurring an already published original; refusal blocks export altogether.
- Only Orgo may authorize operational state transitions and distribute private information. Finishing a task is not evidence of mastery.

## Integration phases

1. Orgo: implement participant-bound confidential fragment capabilities, conjunction-based milestone gates, human sign-off and replay-safe evidence links.
2. Ekole: implement an authenticated, versioned official curriculum mapping and teacher-reviewed evidence service.
3. Kontexte: replace its lab authoring inputs with Orgo-authorized task/fragment projections, without introducing another workflow runtime.
4. School pilot: conduct formal privacy, accessibility, curriculum and child-safety review before any real learners participate.

The archive intentionally includes earlier Ekole–Orgo documentation and maintains the culturally neutral catalogue as the independent reference layer.
