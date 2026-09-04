# DMTZ Implementation — Start Here

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED; IMPLEMENTATION 001-A NEXT.**

**CKR status mirror: COMPLETE CKR-A–CKR-C; IN EXECUTION CKR-D; IMPLEMENTATION 001-A BLOCKED ON CKR EXIT.**

CKR-D is in execution. Product implementation remains blocked until CKR-K.

## Current semantic routing

1. `docs/canonical_knowledge_retrofit/README.md` — live CKR state.
2. `docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json` — exact current owner.
3. `docs/canonical/` — canonicalized owners and candidate review material.
4. `docs/design_history/` / phase corpus — provenance/history after cutover.
5. `docs/implementation/README.md` — implementation block.
6. root `AGENTS.md` — shared instructions.

CKR-B foundation/glossary plus CKR-C concepts/SYN are canonical. CKR-D authority vocabulary/REF/AUTH targets are candidates only; Phase 004/005 remain current authority until atomic cutover. HLTH/OPS/EXPL/INTG/ARCH remain later-group legacy authority.

**Implementation 001-A — BLOCKED until CKR-K.**

```bash
python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md
```
