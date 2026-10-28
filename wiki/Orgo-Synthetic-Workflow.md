# Orgo Synthetic Review Workflow

Kontexte ships **two distinct Orgo scenario files**:

1. `orgo-fixture` creates one `Case` and one preparation `Task` using Orgo's injector, for a synthetic review. This is the older bootstrap fixture.
2. `orgo-workflow-fixture` publishes an Orgo `WorkflowVersion` and submits a synthetic `Signal`. The worker then creates one `Case` plus one **review-only Task per mission step**, if the authorized scenario is actually applied to a running Orgo. All items are clearly marked synthetic, with no child identities, private fragments or learner assignments.

Both are validated against the original Orgo `orgo.scenario.v1` injector format; **neither** implements dependency gates, automatic student assignment or information release. The Studio itself never changes Orgo state.

## Generate and validate (safe)

```bash
PYTHONPATH=src python -m kontexte orgo-workflow-fixture fete-sorciere --out workflow.json
PYTHONPATH=src python -m kontexte orgo-check fete-sorciere --orgo /path/to/Orgo --mode validate --workflow
PYTHONPATH=src python -m kontexte orgo-check fete-sorciere --orgo /path/to/Orgo --mode plan --workflow
```

Node.js is needed for Orgo's existing injector, but not for the Kontexte Studio. `orgo-check` invokes only `validate` or `plan`, never `inject --apply`. Applying the scenario would modify Orgo and must be performed **separately**, by an authorized Orgo operator in a synthetic world, with worker supervision and rollback procedures.

## What Orgo still needs

Authenticated participant-specific private information; dependency gates; real task acceptance/sign-off; trigger rules based on two independently confirmed clues; absence/reassignment paths; audited callback contracts for Ekole evidence. These generic orchestration capabilities belong in Orgo, not in a new Kontexte workflow engine.
