# Implementation Agent / Developer Instructions

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED.**

**CKR status mirror: COMPLETE CKR-A–CKR-K; CKR EXIT ACCEPTED.**

**DPTN status mirror: COMPLETE DPTN-A; IN EXECUTION DPTN-B; IMPLEMENTATION 001-A BLOCKED ON DPTN EXIT.**

ADF and CKR are complete/accepted. DPTN-B is IN EXECUTION. **Implementation 001-A is BLOCKED / NOT STARTED** until DPTN-G exit acceptance and a later explicit human-selected implementation task.

Use the existing CKR ownership inventory and current canonical owners for semantic authority throughout DPTN-B. For a known stable ID, `scripts/agentic/resolve_stable_id.py <ID>` returns the current canonical locator; `--history` is provenance-only. The new history namespace, once created, must never satisfy current semantic resolution.

DPTN routing, manifests, validators and conformance results are not product semantics or implementation evidence.

Do not create product source/schemas/tests/deployment configuration during DPTN. DPTN-B authorizes only MOVE-001 through MOVE-006 and directly necessary history-role/routing validation.
