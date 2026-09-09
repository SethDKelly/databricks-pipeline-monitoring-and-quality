# Implementation Agent / Developer Instructions

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED.**

**CKR status mirror: COMPLETE CKR-A–CKR-K; CKR EXIT ACCEPTED.**

**DPTN status mirror: COMPLETE DPTN-A–DPTN-B; NEXT DPTN-C; IMPLEMENTATION 001-A BLOCKED ON DPTN EXIT.**

ADF and CKR are complete/accepted. DPTN-A–B are complete/accepted and DPTN-C is NEXT / READY / NOT STARTED. **Implementation 001-A is BLOCKED / NOT STARTED** until DPTN-G exit acceptance and a later explicit human-selected implementation task.

Use the existing CKR ownership inventory and `docs/canonical/` current owners for semantic authority until a later accepted DPTN cutover. For a known stable ID, `scripts/agentic/resolve_stable_id.py <ID>` returns the current canonical locator; `--history` is provenance-only. `docs/history/` must never satisfy current semantic resolution.

DPTN routing, manifests, validators and conformance results are not product semantics or implementation evidence. Do not start DPTN-C or product implementation without explicit human selection.
