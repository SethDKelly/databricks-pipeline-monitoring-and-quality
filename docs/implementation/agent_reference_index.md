# DMTZ Agent Reference Index

**Purpose:** compact bridge from a task to current semantic authority, CKR state, stable IDs, implementation status and reviewed platform dependencies.

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED; IMPLEMENTATION 001-A NEXT.**

**CKR status mirror: COMPLETE CKR-A–CKR-B; IN EXECUTION CKR-C; IMPLEMENTATION 001-A BLOCKED ON CKR EXIT.**

## Universal start

| Need | Read first |
|---|---|
| CKR status | `docs/canonical_knowledge_retrofit/README.md` |
| Current semantic owner | `docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json` |
| Canonical namespace | `docs/canonical/README.md` |
| CKR-C comparison | `docs/canonical_knowledge_retrofit/ckr_c_semantic_conservation_matrix.md` |
| Design history | `docs/design_history/README.md` |
| Implementation status | `docs/implementation/README.md` |
| Shared instructions | root `AGENTS.md` |
| Optional OKF routing | `knowledge/index.md` |
| Stable-ID discovery | `stable_id_registry.json` / `scripts/agentic/resolve_stable_id.py` |
| Conformance | `scripts/agentic/run_conformance.py` |

## CKR state

- CKR-A–B — COMPLETE / ACCEPTED.
- CKR-C — Concept Catalog: IN EXECUTION / candidate review.
- CKR-D–K — planned in CKR authority.
- Implementation 001-A — BLOCKED until CKR-K.

## Current authority during CKR-C candidate review

CKR-B foundation/reference resources remain canonical. The 24 concept targets under `docs/canonical/concepts/` and six SYN targets under `docs/canonical/contracts/synchronization/` are candidates only. While inventory state is `candidate_ready`, current concept/SYN meaning remains in Phase 002/003.

CKR-C owns only these 24 concepts plus SYN-001–SYN-035. `reference.authority_vocabulary` and REF/AUTH/HLTH/OPS/EXPL/INTG/ARCH remain with later groups.

## Stable IDs / residuals

Accepted ranges remain SYN-001–035, REF-001–030, AUTH-001–053, HLTH-001–066, OPS-001–123, EXPL-001–160, INTG-001–270 and ARCH-001–500.

ADF-EX-17 / `ADF-G-XT01` remains deferred runtime verification. `DBX-SKILL-RUN-01` remains future 001-A work. Autonomous development remains deferred/not authorized.