# Implementation Agent / Developer Instructions

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED; IMPLEMENTATION 001-A NEXT.**

**CKR status mirror: COMPLETE CKR-A–CKR-B; IN EXECUTION CKR-C; IMPLEMENTATION 001-A BLOCKED ON CKR EXIT.**

CKR-C concept/SYN cutover is complete and awaiting closure validation. Product implementation remains blocked until CKR-K.

Use the ownership inventory to select the current semantic owner, then root `AGENTS.md`, live CKR/implementation status, accepted ADF mechanics, and only then implementation/vendor guidance.

The 24 concepts and SYN-001–SYN-035 now resolve to `docs/canonical/`. Phase 002/003 are provenance for those records. Later stable families retain their assigned legacy owners.

Do not create product source/schemas/tests/deployment configuration as CKR work. Completing CKR-C does not authorize CKR-D.

```bash
python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md
```
