# Implementation Agent / Developer Instructions

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED; IMPLEMENTATION 001-A NEXT.**

**CKR status mirror: COMPLETE CKR-A–CKR-C; NEXT CKR-D; IMPLEMENTATION 001-A BLOCKED ON CKR EXIT.**

CKR-C is complete/accepted. CKR-D is next/ready but unstarted. Product implementation remains blocked until CKR-K.

Use the ownership inventory to select the current semantic owner, then root `AGENTS.md`, live CKR/implementation status, accepted ADF mechanics, and only then implementation/vendor guidance.

The 24 concepts and SYN-001–SYN-035 resolve to `docs/canonical/`. Phase 002/003 are provenance for those records. `reference.authority_vocabulary` and later stable families retain their assigned legacy owners.

Do not create product source/schemas/tests/deployment configuration as CKR work. Completing CKR-C does not authorize CKR-D.

```bash
python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md
```
