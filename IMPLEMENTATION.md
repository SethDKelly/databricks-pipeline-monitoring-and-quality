# DMTZ Implementation — Start Here

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED.**

**CKR status mirror: COMPLETE CKR-A–CKR-K; CKR EXIT ACCEPTED.**

**DPTN status mirror: COMPLETE DPTN-A–DPTN-F; NEXT DPTN-G; IMPLEMENTATION 001-A BLOCKED ON DPTN EXIT.**

ADF and CKR exits are accepted. DPTN-A–F are complete/accepted; DPTN-G is NEXT / READY / NOT STARTED. **Implementation 001-A is BLOCKED / NOT STARTED until DPTN-G exit acceptance.**

## Current routing

1. `docs/index.md` — repository-native unknown-location discovery.
2. `docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json` — exact current semantic ownership.
3. First-class `docs/concepts`, `docs/architecture`, `docs/authority`, `docs/contracts`, `docs/experience`, `docs/invariants`, `docs/policies`, and `docs/reference` — current semantic owner roots.
4. `scripts/agentic/resolve_stable_id.py <ID>` — deterministic current `owner_path::ID`; `--history` is provenance-only.
5. generated `knowledge/index.md` — OKF v0.2 compatibility only.
6. `docs/history/` — provenance/history only.
7. `docs/documentation_topology_normalization/README.md` — live DPTN status.
8. `docs/implementation/README.md` — implementation program state.
9. root `AGENTS.md` — shared instructions.

DPTN-F completed MOVE-019 broad stable-reference/agent/link rebinding. DPTN-G owns final conservation audit, legacy-path retirement and DPTN exit.

**Implementation 001-A — BLOCKED / NOT STARTED ON DPTN EXIT.** DPTN exit will return 001-A to NEXT / READY / NOT STARTED; it will not start implementation.
