# DMTZ Implementation Program

**Status:** BLOCKED — CKR-A–CKR-C COMPLETE / CKR-D NEXT

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED; IMPLEMENTATION 001-A NEXT.**

**CKR status mirror: COMPLETE CKR-A–CKR-C; NEXT CKR-D; IMPLEMENTATION 001-A BLOCKED ON CKR EXIT.**

Product implementation remains blocked while CKR completes current-documentation authority migration. CKR-C is complete/accepted; CKR-D is next/ready but unstarted.

Current semantic routing uses the ownership inventory. CKR-B foundation/glossary plus CKR-C concepts/SYN resolve to `docs/canonical/`; `reference.authority_vocabulary` and REF/AUTH/HLTH/OPS/EXPL/INTG/ARCH remain legacy-authoritative.

Current work:

- CKR-A–C — COMPLETE / ACCEPTED;
- CKR-D — NEXT / READY / NOT STARTED;
- Implementation 001-A — NOT ACTIVE / BLOCKED until CKR-K.

Accepted stable ranges remain SYN-001–035, REF-001–030, AUTH-001–053, HLTH-001–066, OPS-001–123, EXPL-001–160, INTG-001–270 and ARCH-001–500. SYN is canonicalized; later families retain their assigned current owners.

ADF/provider/Databricks residuals remain unchanged. Reviewed vendor skills remain operational guidance only.

```bash
python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md
```
