# DMTZ Agent Reference Index

**Purpose:** compact bridge from a task to current semantic authority, CKR state, stable IDs, implementation status and reviewed platform dependencies.

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED; IMPLEMENTATION 001-A NEXT.**

**CKR status mirror: COMPLETE CKR-A; IN EXECUTION CKR-B; IMPLEMENTATION 001-A BLOCKED ON CKR EXIT.**

## Universal start

| Need | Read first |
|---|---|
| CKR status / active group | `docs/canonical_knowledge_retrofit/README.md` |
| Current semantic owner / target | `docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json` |
| CKR-B semantic comparison | `docs/canonical_knowledge_retrofit/ckr_b_semantic_conservation_matrix.md` |
| Authority / cutover rules | `authority_model.md` / `migration_contract.md` under CKR |
| Target/current canonical namespace | `docs/canonical/README.md` |
| Design history | `docs/design_history/README.md` |
| Implementation status | `docs/implementation/README.md` |
| Shared instructions | root `AGENTS.md` |
| Optional OKF routing | `knowledge/index.md` |
| Stable ID discovery | `stable_id_registry.json` / `scripts/agentic/resolve_stable_id.py` |
| Conformance | `scripts/agentic/run_conformance.py` |

## Current authority rule

| Inventory state | Current owner |
|---|---|
| `legacy_authoritative` | inventoried legacy source |
| `candidate_ready` | legacy source; candidate review-only |
| `canonicalized` | inventoried `docs/canonical/` target |
| `history_only` | provenance/rationale only |

Search order, phase recency, OKF summaries and canonical-path presence do not establish authority.

## CKR progression

- **CKR-A — Authority model / migration contract / ownership inventory: COMPLETE / ACCEPTED**
- **CKR-B — Foundation / terminology / cross-cutting invariants: IN EXECUTION**
- CKR-C — 24 concepts + SYN: PLANNED
- CKR-D — REF/AUTH: PLANNED
- CKR-E — HLTH: PLANNED
- CKR-F — OPS: PLANNED
- CKR-G — EXPL: PLANNED
- CKR-H — INTG: PLANNED
- CKR-I — ARCH: PLANNED
- CKR-J — OKF / deterministic stable owners / routing enforcement: PLANNED
- CKR-K — consolidation / provenance validation / exit: PLANNED

CKR-B currently owns nine foundation/glossary candidates. Their legacy sources remain current authority until atomic cutover.

Implementation 001-A remains blocked until CKR-K.

## Stable IDs

Accepted ranges remain SYN-001–035, REF-001–030, AUTH-001–053, HLTH-001–066, OPS-001–123, EXPL-001–160, INTG-001–270 and ARCH-001–500.

CKR-A established family-level current/target ownership. Exact occurrence lookup remains non-authoritative until CKR-J makes migrated exact owner/anchor resolution deterministic.

## Residuals

ADF-EX-17 remains deferred; `ADF-G-XT01` remains open and Cursor/Claude Code/Codex remain runtime-`unverified`. `DBX-SKILL-RUN-01` remains a future 001-A obligation after CKR unlock. Autonomous development remains deferred/not authorized.

Core workflows remain in `.agents/skills/`; Databricks overlays remain environment discovery, acquisition, persistence, Lineage, runtime provenance and governance. Workflow selection does not authorize product implementation or automatic CKR continuation.
