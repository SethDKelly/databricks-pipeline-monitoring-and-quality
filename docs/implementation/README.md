# DMTZ Implementation Program

**Status:** BLOCKED — CKR-A–CKR-C COMPLETE / CKR-D IN EXECUTION

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED; IMPLEMENTATION 001-A NEXT.**

**CKR status mirror: COMPLETE CKR-A–CKR-C; IN EXECUTION CKR-D; IMPLEMENTATION 001-A BLOCKED ON CKR EXIT.**

Product implementation remains blocked while CKR completes documentation-authority migration.

Current semantic routing uses the ownership inventory. CKR-B foundation/glossary plus CKR-C concepts/SYN resolve to canonical owners. CKR-D authority vocabulary/REF/AUTH are `candidate_ready`, so Phase 004/005 remain current authority until atomic cutover.

Current work:

- CKR-A–C — COMPLETE / ACCEPTED;
- CKR-D — IN EXECUTION;
- Implementation 001-A — NOT ACTIVE / BLOCKED until CKR-K.

Accepted ranges remain SYN-001–035, REF-001–030, AUTH-001–053, HLTH-001–066, OPS-001–123, EXPL-001–160, INTG-001–270 and ARCH-001–500.

```bash
python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md
```
