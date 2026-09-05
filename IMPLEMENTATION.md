# DMTZ Implementation — Start Here

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED; IMPLEMENTATION 001-A NEXT.**

**CKR status mirror: COMPLETE CKR-A–CKR-J; NEXT CKR-K; IMPLEMENTATION 001-A BLOCKED ON CKR EXIT.**

CKR-A–J are complete/accepted. CKR-K is next/ready but unstarted. Product implementation remains blocked until CKR-K.

## Current semantic routing

1. `docs/canonical_knowledge_retrofit/README.md` — live CKR state.
2. ownership inventory — exact current semantic owner.
3. `docs/canonical/` — canonical current owners.
4. known stable ID — `scripts/agentic/resolve_stable_id.py <ID>` returns `owner_path::ID`.
5. `knowledge/` — optional bounded discovery when semantic location is unknown.
6. design history / phase corpus — provenance/rationale/history after migration.
7. `docs/implementation/README.md` — implementation block.
8. root `AGENTS.md` — shared instructions.

Use `--history` only for explicit provenance/historical stable-ID inspection. Routing helpers do not own semantics or prove implementation.

**Implementation 001-A — BLOCKED until CKR-K.**
