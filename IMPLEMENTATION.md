# DMTZ Implementation — Start Here

Phase 010, the Agentic Development Foundation, its execution exit, and the Databricks Agent Skills Integration Addendum are complete/accepted.

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED; IMPLEMENTATION 001-A NEXT.**

**CKR status mirror: COMPLETE CKR-A; IN EXECUTION CKR-B; IMPLEMENTATION 001-A BLOCKED ON CKR EXIT.**

CKR-B has completed the nine-record foundation/glossary authority cutover and is awaiting closure validation. Product implementation remains blocked until CKR-K. The accepted ADF exit is not reopened.

## Current semantic routing

1. `docs/canonical_knowledge_retrofit/README.md` — live CKR state.
2. `docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json` — record ownership.
3. `docs/canonical/README.md` — current canonical namespace.
4. `docs/design_history/README.md` — provenance/history.
5. `docs/implementation/README.md` — implementation block.
6. root `AGENTS.md` — shared instructions.

CKR-B product definition, actors, terminology, Concept Design method, AP-01–32, SP-01–15, lifecycles, MVP boundary and shared glossary now resolve to `docs/canonical/`. Their legacy foundation/glossary sources are provenance.

The 24 concepts and all stable-ID families remain with their later-group legacy owners.

## Current work

**CKR-A — COMPLETE / ACCEPTED.**

**CKR-B — IN EXECUTION / CUTOVER COMPLETE / CLOSURE VALIDATION PENDING.**

**Implementation 001-A — BLOCKED until CKR-K.**

`ADF-G-XT01` remains open provider-runtime verification debt. `DBX-SKILL-RUN-01` remains a future 001-A environment obligation after CKR unlocks implementation.

## Conformance

```bash
python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md
```

PASS describes repository agentic/documentation-authority conformance, not DMTZ domain health, provider-runtime proof, Databricks capability or production readiness.
