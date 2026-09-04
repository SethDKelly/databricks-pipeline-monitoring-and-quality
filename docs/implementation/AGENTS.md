# Implementation Agent / Developer Instructions

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED; IMPLEMENTATION 001-A NEXT.**

**CKR status mirror: COMPLETE CKR-A–CKR-B; IN EXECUTION CKR-C; IMPLEMENTATION 001-A BLOCKED ON CKR EXIT.**

The ADF exit remains accepted. CKR-C is in execution; product implementation remains blocked until CKR-K.

## Authority

Use the current semantic owner selected by `docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json`, then root `AGENTS.md`, live CKR/implementation status, accepted ADF mechanics, and only then implementation/vendor guidance.

CKR-B foundation/glossary records resolve to `docs/canonical/`. CKR-C concept/SYN candidates remain non-authoritative until atomic cutover; use Phase 002/003 while their states are `candidate_ready`.

## Current boundary

- CKR-A–B — COMPLETE / ACCEPTED;
- CKR-C — IN EXECUTION / CANDIDATE REVIEW;
- Implementation 001-A — BLOCKED ON CKR-K.

CKR-C owns only the 24 accepted concept records plus SYN-001–SYN-035. Do not migrate later stable families or create product source, schemas, product tests or deployment configuration as CKR work.

## Context / actions

Use `root AGENTS → live CKR authority → ownership inventory when unclear → current semantic owner → matching skill/overlay → exact IDs/contracts`.

OKF is routing only. A1–A4 remains unchanged. Completing CKR-C does not authorize CKR-D.

## Residuals / conformance

ADF-EX-17 remains deferred; `ADF-G-XT01` remains open. `DBX-SKILL-RUN-01` remains future 001-A work. Reviewed Databricks skills are operational guidance only.

```bash
python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md
```

Preserve Observation ≠ Assessment, Expectation ≠ Baseline, Change Intent ≠ Deployment ≠ Change, execution success ≠ data health, missing evidence ≠ negative truth, Lineage ≠ exposure ≠ Impact ≠ cause, Investigation closure ≠ causal confirmation, and authority/authorization/control separations.