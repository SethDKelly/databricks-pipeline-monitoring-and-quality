# DMTZ Implementation — Start Here

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED.**

**CKR status mirror: COMPLETE CKR-A–CKR-K; CKR EXIT ACCEPTED.**

**DPTN status mirror: IN EXECUTION DPTN-A; IMPLEMENTATION 001-A BLOCKED ON DPTN EXIT.**

ADF and CKR exits are accepted. DPTN-A is now the active pre-implementation documentation-topology task. **Implementation 001-A is BLOCKED / NOT STARTED until DPTN-G exit acceptance.**

## Current semantic routing

1. `docs/canonical_knowledge_retrofit/README.md` — accepted CKR exit/current ownership model.
2. ownership inventory — exact current semantic owner; lifecycle `ckr_complete`.
3. `docs/canonical/` — current semantic owners until a later DPTN cutover moves them.
4. known stable ID — `scripts/agentic/resolve_stable_id.py <ID>` returns the current `owner_path::ID`.
5. `knowledge/` — optional bounded discovery when semantic location is unknown.
6. design history / phase corpus — provenance/rationale/history.
7. `docs/documentation_topology_normalization/README.md` — active topology-normalization status and move authority.
8. `docs/implementation/README.md` — implementation program state.
9. root `AGENTS.md` — shared instructions.

DPTN-A move-map destinations are planning only. Do not route current semantic questions to proposed future locations until the relevant later DPTN cutover is accepted. Use `--history` only for explicit provenance/historical stable-ID inspection.

**Implementation 001-A — BLOCKED / NOT STARTED ON DPTN EXIT.** DPTN exit will return 001-A to NEXT / READY / NOT STARTED; it will not start implementation.
