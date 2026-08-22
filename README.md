# F82 | Agentic Quantum Computing | L3 Gold Standard | v1.0

A governed multi-agent reference system for quantum algorithm analysis, circuit architecture, backend and noise assumptions, evidence review, uncertainty, reproducibility, and qualified human synthesis.

## Research pipeline

- Problem formulation
- Circuit architecture
- Noise and error analysis
- Evidence review
- Human scientific review

Tools and skills cover problem decomposition, circuit reasoning, error reasoning, evidence discipline, human review, assumption tracking, circuit registration, noise modeling, evidence registration, and review gating.

## Gold-standard research governance

F82 is fail closed. Research release requires reviewed problem formulation, circuit architecture, backend assumptions, noise modeling, verified simulation or hardware results, evidence provenance, uncertainty review, reproducibility review, and explicit qualified human approval.

Release is blocked for backend mismatch, inadequate noise models, failed circuit verification, unreproduced results, missing provenance, uncharacterized uncertainty, missing classical baselines for comparative claims, or unsupported quantum-advantage claims.

The reference system cannot autonomously claim quantum advantage or experimental confirmation, fabricate evidence, hide uncertainty, or execute unreviewed quantum hardware jobs.

## Verification gates

CI runs on Python 3.10, 3.11, and 3.12 and requires:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python run.py
```

The behavioral verification layer includes eight direct governance tests and a 10-scenario held-out quantum research suite.

Author: Mahsa Keikha
