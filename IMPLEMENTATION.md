# DMTZ Implementation — Start Here

Phase 010, the Agentic Development Foundation, its execution exit, and the Databricks Agent Skills Integration Addendum are complete/accepted.

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED; IMPLEMENTATION 001-A NEXT.**

**CKR status mirror: COMPLETE CKR-A–CKR-B; NEXT CKR-C; IMPLEMENTATION 001-A BLOCKED ON CKR EXIT.**

CKR-A and CKR-B are complete/accepted. CKR-C is the next eligible documentation-authority group; it is not active until explicitly selected. Product implementation remains blocked until CKR-K.

## Current semantic routing

1. `docs/canonical_knowledge_retrofit/README.md` — live CKR state.
2. `docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json` — current ownership.
3. `docs/canonical/README.md` — canonical namespace.
4. `docs/design_history/README.md` — provenance/history.
5. `docs/implementation/README.md` — implementation block.
6. root `AGENTS.md` — shared instructions.

CKR-B canonicalized product definition, actors, terminology, Concept Design method, AP-01–32, SP-01–15, lifecycles, MVP boundary and shared glossary. The 24 concepts and all stable-ID families remain with their later-group legacy owners.

## Current work

**CKR-C — Concept Catalog: NEXT / READY.**

**Implementation 001-A — BLOCKED until CKR-K.**

`ADF-G-XT01` remains open provider-runtime verification debt. `DBX-SKILL-RUN-01` remains a future 001-A environment obligation after CKR unlocks implementation.

## Conformance

```bash
python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md
```

PASS describes repository agentic/documentation-authority conformance, not product/runtime readiness.
