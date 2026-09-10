# Implementation Agent / Developer Instructions

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED.**

**CKR status mirror: COMPLETE CKR-A–CKR-K; CKR EXIT ACCEPTED.**

**DPTN exit: ACCEPTED — Implementation 001-A NEXT / READY / NOT STARTED.**

ADF, CKR and DPTN are complete/accepted. **Implementation 001-A is NEXT / READY / NOT STARTED** and still requires a separate explicit human-selected implementation task before work begins.

Use `docs/index.md` for repository-native discovery and `docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json` for exact current semantic ownership. For a known stable ID, `scripts/agentic/resolve_stable_id.py <ID>` returns the current locator selected by the ledger; `--history` is provenance-only.

Top-level `knowledge/` is generated OKF compatibility output. Current operational routing uses first-class semantic-owner paths and must not depend on retired migration/compatibility namespaces. The completed DPTN record is historical provenance under `docs/history/retrofits/dptn/`.

Do not infer implementation start from readiness. 001-A begins only when the human explicitly selects that implementation task.
