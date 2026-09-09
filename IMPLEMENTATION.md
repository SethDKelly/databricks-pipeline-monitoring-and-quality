# DMTZ Implementation — Start Here

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED; IMPLEMENTATION 001-A NEXT.**

**CKR status mirror: COMPLETE CKR-A–CKR-K; CKR EXIT ACCEPTED; IMPLEMENTATION 001-A NEXT.**

DPTN status mirror: COMPLETE DPTN-A; NEXT DPTN-B; IMPLEMENTATION 001-A BLOCKED ON DPTN EXIT.

The Canonical Knowledge Repository retrofit and DPTN-A planning phase are complete/accepted. DPTN-B is NEXT / READY / NOT STARTED. **Implementation 001-A — BLOCKED ON DPTN EXIT.**

## Current semantic routing

1. `docs/canonical_knowledge_retrofit/README.md` — accepted CKR exit state.
2. ownership inventory — exact current semantic owner; lifecycle `ckr_complete`.
3. `docs/canonical/` — current canonical owners until later DPTN cutovers.
4. known stable ID — `scripts/agentic/resolve_stable_id.py <ID>` returns `owner_path::ID`.
5. `knowledge/` — optional bounded discovery when semantic location is unknown.
6. design history / phase corpus — provenance/rationale/history.
7. `docs/documentation_topology_normalization/README.md` — accepted DPTN-A plan and live DPTN progression.
8. `docs/implementation/README.md` — implementation program state.
9. root `AGENTS.md` — shared instructions.

Use `--history` only for explicit provenance/historical stable-ID inspection. Routing helpers and DPTN move maps do not own semantics or prove implementation.

DPTN-A completion does not authorize physical documentation moves. DPTN-B must be explicitly selected before relocation begins. Implementation returns to NEXT / READY / NOT STARTED only after accepted DPTN exit and still requires a subsequent explicit human-selected implementation task.
