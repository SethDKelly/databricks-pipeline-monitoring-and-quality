# DMTZ Agent Reference Index

**Purpose:** compact secondary bridge from a task to current semantic authority, migration state, stable-ID families, implementation status and reviewed platform-development dependencies.

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED; IMPLEMENTATION 001-A NEXT.**

**CKR status mirror: IN EXECUTION CKR-A; IMPLEMENTATION 001-A BLOCKED ON CKR EXIT.**

The ADF exit is accepted. The **Canonical Knowledge & Documentation Authority Retrofit** is now the active pre-implementation dependency; 001-A is not active.

## Universal start

| Need | Read first |
|---|---|
| Live CKR status / migration sequence | `docs/canonical_knowledge_retrofit/README.md` |
| Current semantic owner / target owner | `docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json` |
| CKR authority model | `docs/canonical_knowledge_retrofit/authority_model.md` |
| CKR migration/cutover rules | `docs/canonical_knowledge_retrofit/migration_contract.md` |
| Target canonical knowledge namespace | `docs/canonical/README.md` |
| Design-history/provenance layer | `docs/design_history/README.md` |
| Live implementation status | `docs/implementation/README.md` |
| Foundation exit decision | `docs/agentic_development_foundation/execution_exit_review.md` |
| Shared constitution | root `AGENTS.md` |
| Portable routing | `knowledge/index.md` |
| Stable-ID occurrence discovery | `stable_id_registry.json` / `scripts/agentic/resolve_stable_id.py` |
| Agentic/CKR conformance | `scripts/agentic/run_conformance.py` |
| Implementation 001 package after CKR exit | `docs/implementation/001_executable_foundations_walking_skeleton/README.md` |

## Current authority rule

For a semantic record:

| Inventory state | Current owner |
|---|---|
| `legacy_authoritative` | inventoried legacy source |
| `candidate_ready` | inventoried legacy source; candidate is review-only |
| `canonicalized` | inventoried `docs/canonical/` target |
| `history_only` | no current semantic ownership; provenance/rationale only |

Do not treat the newest phase, first search result, OKF summary or mere presence under `docs/canonical/` as authority.

## CKR progression

| Group | Scope | State |
|---|---|---|
| CKR-A | Authority model, migration contract, ownership inventory | **IN EXECUTION** |
| CKR-B | Foundation, terminology, cross-cutting invariants | PLANNED |
| CKR-C | 24-concept catalog + SYN synchronization | PLANNED |
| CKR-D | REF/AUTH evidence, time, authority, governance | PLANNED |
| CKR-E | HLTH health/quality/metrics/timing | PLANNED |
| CKR-F | OPS Lineage/change/investigation/Impact/control | PLANNED |
| CKR-G | EXPL questioning/explanation/experience | PLANNED |
| CKR-H | INTG integration/source/evidence availability | PLANNED |
| CKR-I | ARCH technical architecture | PLANNED |
| CKR-J | OKF, stable owners, agent routing, drift enforcement | PLANNED |
| CKR-K | Consolidation/provenance validation/exit | PLANNED |

**Implementation 001-A remains blocked until CKR-K exit acceptance.**

## Accepted stable-ID families

Accepted ranges remain unchanged:

- SYN-001–SYN-035;
- REF-001–REF-030;
- AUTH-001–AUTH-053;
- HLTH-001–HLTH-066;
- OPS-001–OPS-123;
- EXPL-001–EXPL-160;
- INTG-001–INTG-270;
- ARCH-001–ARCH-500.

CKR-A inventories each family by current legacy root and future canonical domain. Exact occurrence discovery remains non-authoritative until CKR-J introduces deterministic canonical-owner resolution for migrated IDs.

## Agentic foundation / platform residuals

- ADF execution exit — ACCEPTED;
- ADF-EX-17 — DEFERRED / WAIVED as bounded verification debt;
- `ADF-G-XT01` — OPEN; Cursor/Claude Code/Codex runtime state remains `unverified`;
- Databricks Agent Skills addendum — ACCEPTED;
- `DBX-SKILL-RUN-01` — future Implementation 001-A obligation after CKR unlock;
- autonomous development — DEFERRED / NOT AUTHORIZED.

## Workflow map

Core workflows remain `resolve-context`, `implement-group`, `resolve-contract`, `run-conformance`, `review-change`, `update-traceability`, and `exit-review`. DMTZ Databricks overlays remain environment discovery, acquisition, persistence, Lineage, runtime provenance and governance.

During CKR, use these workflows only inside the human-selected documentation-migration task. They do not authorize product implementation or automatic group continuation.
