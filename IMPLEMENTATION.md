# DMTZ Implementation — Start Here

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED.**

**CKR status mirror: COMPLETE CKR-A–CKR-K; CKR EXIT ACCEPTED.**

**DPTN status mirror: COMPLETE DPTN-A; IN EXECUTION DPTN-B; IMPLEMENTATION 001-A BLOCKED ON DPTN EXIT.**

ADF and CKR exits are accepted. DPTN-B is IN EXECUTION as a history/provenance topology phase. **Implementation 001-A is BLOCKED / NOT STARTED until DPTN-G exit acceptance.**

## Current semantic routing

1. `docs/canonical_knowledge_retrofit/README.md` — accepted CKR exit/current ownership model.
2. ownership inventory — exact current semantic owner; lifecycle `ckr_complete`.
3. `docs/canonical/` — current semantic owners throughout DPTN-B.
4. known stable ID — `scripts/agentic/resolve_stable_id.py <ID>` returns the current `owner_path::ID`.
5. `knowledge/` — optional bounded discovery when semantic location is unknown.
6. `docs/history/` — provenance/history only after the DPTN-B relocation cutover; never current semantic authority.
7. `docs/documentation_topology_normalization/README.md` — active topology-normalization status and move authority.
8. `docs/implementation/README.md` — implementation program state.
9. root `AGENTS.md` — shared instructions.

DPTN-B authorizes only MOVE-001 through MOVE-006 historical relocation and directly necessary history-role/routing validation. It does not authorize canonical promotion, stable-ID current-locator rebinding, mixed ADF/CKR decomposition, or implementation.

**Implementation 001-A — BLOCKED / NOT STARTED ON DPTN EXIT.** DPTN exit will return 001-A to NEXT / READY / NOT STARTED; it will not start implementation.
