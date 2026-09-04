# Implementation Agent / Developer Instructions

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED; IMPLEMENTATION 001-A NEXT.**

**CKR status mirror: COMPLETE CKR-A; IN EXECUTION CKR-B; IMPLEMENTATION 001-A BLOCKED ON CKR EXIT.**

The ADF exit remains accepted. CKR-B has completed its nine-record foundation/glossary authority cutover and awaits closure validation. Product implementation remains blocked until CKR-K.

## Authority

Use the current semantic owner selected by `docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json`, then root `AGENTS.md`, live CKR/implementation status, accepted ADF mechanics, and only then implementation/vendor guidance.

CKR-B product/foundation/glossary records now resolve to `docs/canonical/`. Their Phase-001/legacy glossary sources are provenance. Concepts/stable-ID families remain independently legacy-owned until later CKR groups.

## Current boundary

- CKR-A — COMPLETE / ACCEPTED;
- CKR-B — IN EXECUTION / CUTOVER COMPLETE / CLOSURE VALIDATION PENDING;
- Implementation 001-A — BLOCKED ON CKR-K.

Do not create product source, schemas, product tests or deployment configuration as CKR work unless separately authorized.

## Context / actions

Use `root AGENTS → live CKR authority → ownership inventory when unclear → current semantic owner → matching skill/overlay → exact IDs/contracts`.

OKF is routing only. A1–A4 remains unchanged. Completing one CKR group does not authorize the next.

## Residuals / conformance

ADF-EX-17 remains deferred; `ADF-G-XT01` remains open. `DBX-SKILL-RUN-01` remains future 001-A work. Reviewed Databricks skills are operational guidance only.

```bash
python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md
```

Preserve Observation ≠ Assessment, Expectation ≠ Baseline, execution success ≠ data health, current ≠ historical/as-known, missing evidence ≠ negative truth, Lineage ≠ exposure ≠ Impact ≠ cause, and authority/authorization/control separations.
