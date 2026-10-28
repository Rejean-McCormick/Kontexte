# Orgo Integration

**Orgo is the single source of operational truth.** Kontexte defines situations and integration intent; it must not maintain a competing Case, Task, Signal or Workflow state machine.

## What you can test now

The Python CLI can export a **synthetic** `orgo.scenario.v1` fixture for `fete-sorciere`:

```bash
PYTHONPATH=src python -m kontexte orgo-fixture fete-sorciere --out /tmp/witch.scenario.json
```

From a separate compatible Orgo checkout (based on the referenced snapshot):

```bash
node tools/scenario-injector/cli.mjs validate /tmp/witch.scenario.json
node tools/scenario-injector/cli.mjs plan /tmp/witch.scenario.json
```

The fixture creates **one synthetic Case and one preparation Task**. Its metadata identifies it as a simulation and does not instruct real-world school activity. Kontexte does **not** automatically apply the fixture. Any `--apply` action is mutating and belongs only in an explicitly authorized test world.

A second command exports a **blueprint of intentions**, not an executable Orgo Workflow:

```bash
PYTHONPATH=src python -m kontexte orgo-blueprint fete-sorciere --out /tmp/witch.blueprint.json
```

## Existing adapter code

`src/kontexte/orgo_http.py` contains server-side HTTP utilities for reading Tasks/Cases and proposing an explicit status change with revision checks, bearer authentication, and idempotency. It rejects nonlocal hosts by default and is **not a browser-facing authenticated classroom integration**. The actual API and its permissions must be revalidated against whichever Orgo version is deployed.

## Missing generic Orgo primitives

- A reviewed, versioned path from mission designs to executable workflows/processes.
- Secure, recipient-specific release of an information fragment based on an Orgo decision and version.
- A verifiable join of facts A+B with deduplication and fallback when a partner is absent.
- Scheduling, availability, delay, cancellation and safe resumption for solo or cooperative missions.
- School-specific identities and authorization with explicit teacher approval for real actions.
- Secure observation events to an Ekole evidence service; `Task COMPLETED` cannot mean “mastered.”
- Repeatable tests for races, replay, expiration and isolation with a running Orgo instance.

Build such primitives **in Orgo**, where they also apply to organizations and professional simulations. Kontexte should continue expressing domain scenarios as data.

## Orgo_Worlds

The separately supplied `Orgo_Worlds` snapshot represents versioned worlds/releases. A world/release can bind a reviewed pack of scenario materials; it is **not** a replacement owner for live Tasks and Cases.

## Security boundaries

Never let a student browser claim its own authorized fragment IDs based on a role string, a URL query, or a local toggle. Orgo's future trusted server must authorize which content can reach each recipient. The `--demo-fragments` rendering flag is **fiction-only** and does not authorize live disclosure.

Read [Architecture](Architecture), [Adaptive Participation](Adaptive-Participation), and [Roadmap and Limitations](Roadmap-and-Limitations).
