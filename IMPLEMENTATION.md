# DMTZ Implementation — Start Here

Phase 010, the Agentic Development Foundation, its execution exit, and the Databricks Agent Skills Integration Addendum are complete/accepted.

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED; IMPLEMENTATION 001-A NEXT.**

**CKR status mirror: COMPLETE CKR-A–CKR-B; IN EXECUTION CKR-C; IMPLEMENTATION 001-A BLOCKED ON CKR EXIT.**

CKR-C is actively migrating the 24 accepted concepts plus SYN-001–SYN-035. Candidate targets do not supersede Phase 002/003 until atomic cutover. Product implementation remains blocked until CKR-K.

## Current semantic routing

1. `docs/canonical_knowledge_retrofit/README.md` — live CKR state.
2. `docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json` — current ownership.
3. `docs/canonical/README.md` — canonical namespace.
4. `docs/design_history/README.md` — provenance/history.
5. `docs/implementation/README.md` — implementation block.
6. root `AGENTS.md` — shared instructions.

CKR-B foundation/glossary resources are canonical. CKR-C concept/SYN resources are candidates only; Phase 002/003 remain current owners while their states are `candidate_ready`.

## Current work

**CKR-C — Concept Catalog: IN EXECUTION / CANDIDATE REVIEW.**

**Implementation 001-A — BLOCKED until CKR-K.**

`ADF-G-XT01` remains open provider-runtime verification debt. `DBX-SKILL-RUN-01` remains a future 001-A environment obligation after CKR unlocks implementation.

## Conformance

```bash
python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md
```

PASS describes repository agentic/documentation-authority conformance, not product/runtime readiness.