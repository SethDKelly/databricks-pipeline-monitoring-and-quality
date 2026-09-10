# DMTZ Implementation — Start Here

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED.**

**CKR status mirror: COMPLETE CKR-A–CKR-K; CKR EXIT ACCEPTED.**

**DPTN exit: ACCEPTED — Implementation 001-A NEXT / READY / NOT STARTED.**

ADF, CKR and DPTN exits are accepted. **Implementation 001-A is NEXT / READY / NOT STARTED.** DPTN exit removed the topology blocker; it did not start product implementation. A separate explicit human-selected implementation task is still required.

## Current routing

1. `docs/index.md` — repository-native unknown-location discovery.
2. `docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json` — exact current semantic ownership.
3. First-class `docs/concepts`, `docs/architecture`, `docs/authority`, `docs/contracts`, `docs/experience`, `docs/invariants`, `docs/policies`, and `docs/reference` — current semantic owner roots.
4. `scripts/agentic/resolve_stable_id.py <ID>` — deterministic current `owner_path::ID`; `--history` is provenance-only.
5. generated `knowledge/index.md` — OKF v0.2 compatibility only.
6. `docs/history/` — provenance/history only, including the completed DPTN record.
7. `docs/implementation/README.md` — implementation program state.
8. root `AGENTS.md` — shared instructions.

**Implementation 001-A — NEXT / READY / NOT STARTED.** Do not begin it without explicit human selection.
