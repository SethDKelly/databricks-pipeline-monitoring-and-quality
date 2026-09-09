# DMTZ Implementation — Start Here

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED.**

**CKR status mirror: COMPLETE CKR-A–CKR-K; CKR EXIT ACCEPTED.**

**DPTN status mirror: COMPLETE DPTN-A–DPTN-D; NEXT DPTN-E; IMPLEMENTATION 001-A BLOCKED ON DPTN EXIT.**

ADF and CKR exits are accepted. DPTN-A–D are complete/accepted; DPTN-E is NEXT / READY / NOT STARTED. **Implementation 001-A is BLOCKED / NOT STARTED until DPTN-G exit acceptance.**

## Current semantic routing

1. `docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json` — exact current semantic owner; lifecycle `ckr_complete`.
2. Current semantic owners — first-class `docs/concepts`, `docs/architecture`, `docs/authority`, `docs/contracts`, `docs/experience`, `docs/invariants`, `docs/policies`, and `docs/reference`.
3. Known stable ID — `scripts/agentic/resolve_stable_id.py <ID>` returns the current `owner_path::ID` selected by the ledger.
4. `knowledge/` — optional bounded discovery while DPTN-E has not yet converged the discovery roots.
5. `docs/history/` — provenance/history only; completed CKR evidence is under `history/retrofits/ckr/`, completed ADF program evidence under `history/foundations/adf/`.
6. `docs/documentation_topology_normalization/README.md` — live topology-normalization status and move authority.
7. `docs/implementation/README.md` — implementation program state.
8. root `AGENTS.md` — shared instructions.

DPTN-D completed MOVE-015 and MOVE-016. It does not authorize DPTN-E/F/G or product implementation.

**Implementation 001-A — BLOCKED / NOT STARTED ON DPTN EXIT.** DPTN exit will return 001-A to NEXT / READY / NOT STARTED; it will not start implementation.
