# Implementation Agent / Developer Instructions

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED.**

**CKR status mirror: COMPLETE CKR-A–CKR-K; CKR EXIT ACCEPTED.**

**DPTN status mirror: COMPLETE DPTN-A–DPTN-F; NEXT DPTN-G; IMPLEMENTATION 001-A BLOCKED ON DPTN EXIT.**

ADF and CKR are complete/accepted. DPTN-A–F are complete/accepted and DPTN-G is NEXT / READY / NOT STARTED. **Implementation 001-A is BLOCKED / NOT STARTED** until DPTN-G exit acceptance and a later explicit human-selected implementation task.

Use `docs/index.md` for repository-native discovery and `docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json` for exact current semantic ownership. For a known stable ID, `scripts/agentic/resolve_stable_id.py <ID>` returns the current locator selected by the ledger; `--history` is provenance-only.

Top-level `knowledge/` is generated OKF compatibility output. DPTN-F completed broad stable-reference/agent/link rebinding; current operational routing must not depend on history or `docs/canonical/<family>` compatibility redirects. DPTN-G owns final redirect/scaffolding retirement and exit review.
