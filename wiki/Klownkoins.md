# Klownkoins — Fictional Classroom Economy

**Klownkoins are an educational, fictional unit.** They are intended to support arithmetic, budgeting, negotiation and resource allocation inside a simulated scenario. They are **not** legal tender, real money, a payment system, or an exchangeable reward for access to essential learning.

## Example

In the Witch Celebration pilot:

```text
4 contributions × 6 Klownkoins    = 24
Stage decoration                  =  8
Subtotal                          = 32
Optional fictional 10% tax        =  3.20
Fictional total                   = 35.20
Available budget                  = 55
Remaining                         = 19.80
```

The tax rate is **fictional for the exercise** and should not be presented as Québec sales tax or assumed to be a normal Grade 3 learning outcome. If a teacher later wants to explore real taxes, real figures and the target grade must be independently checked.

## CLI calculator

```bash
PYTHONPATH=src python -m kontexte bill \
  --input examples/klownkoins.json \
  --out /tmp/klownkoins-result.json
```

The calculator in `src/kontexte/economy.py` performs deterministic operations on a supplied synthetic bill. It does **not** issue real payments, create student accounts or enforce real transactions.

## Educational design

Good fictional economies involve meaningful decisions: how many items to make, whether supplies are enough, which service to request, how to share responsibilities and how to reconcile a budget. Avoid turning Klownkoins into a ranking of children, using them to buy necessary instruction, or making a teacher personally liable for prizes without prior agreement.

Any student-facing economic scenario should pass accessibility, fairness and educator review. See [Witch Celebration Walkthrough](Witch-Celebration-Walkthrough) and [Adaptive Participation](Adaptive-Participation).
