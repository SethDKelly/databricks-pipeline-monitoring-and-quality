# DMTZ Implementation — Start Here

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED; IMPLEMENTATION 001-A NEXT.**

**CKR status mirror: COMPLETE CKR-A–CKR-B; IN EXECUTION CKR-C; IMPLEMENTATION 001-A BLOCKED ON CKR EXIT.**

CKR-C has completed the 24-concept + SYN-001–SYN-035 authority cutover and is awaiting closure validation. Product implementation remains blocked until CKR-K.

## Current semantic routing

1. `docs/canonical_knowledge_retrofit/README.md` — live CKR state.
2. ownership inventory — exact current semantic owner.
3. `docs/canonical/` — canonicalized owners.
4. `docs/design_history/` and phase corpus — provenance/history.
5. `docs/implementation/README.md` — implementation block.
6. root `AGENTS.md` — shared instructions.

The 24 concepts and SYN family now resolve to canonical resources. REF/AUTH/HLTH/OPS/EXPL/INTG/ARCH remain legacy-authoritative until their assigned CKR groups.

**Implementation 001-A — BLOCKED until CKR-K.**

```bash
python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md
```
