# DMTZ Implementation — Start Here

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED; IMPLEMENTATION 001-A NEXT.**

**CKR status mirror: COMPLETE CKR-A–CKR-K; CKR EXIT ACCEPTED; IMPLEMENTATION 001-A NEXT.**

The Canonical Knowledge Repository retrofit is complete/accepted. Implementation 001-A is NEXT / READY / NOT STARTED and requires explicit human selection before implementation begins.

## Current semantic routing

1. `docs/canonical_knowledge_retrofit/README.md` — accepted CKR exit state.
2. ownership inventory — exact current semantic owner; lifecycle `ckr_complete`.
3. `docs/canonical/` — canonical current owners.
4. known stable ID — `scripts/agentic/resolve_stable_id.py <ID>` returns `owner_path::ID`.
5. `knowledge/` — optional bounded discovery when semantic location is unknown.
6. design history / phase corpus — provenance/rationale/history.
7. `docs/implementation/README.md` — implementation program state.
8. root `AGENTS.md` — shared instructions.

Use `--history` only for explicit provenance/historical stable-ID inspection. Routing helpers do not own semantics or prove implementation.

**Implementation 001-A — NEXT / READY / NOT STARTED.** CKR exit removed the documentation-authority blocker; it did not start implementation.
