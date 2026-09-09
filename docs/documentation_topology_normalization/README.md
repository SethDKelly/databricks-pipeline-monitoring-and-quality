# Documentation Physical Topology Normalization (DPTN)

**Program status:** ACTIVE — DPTN-A COMPLETE / ACCEPTED — DPTN-B IN EXECUTION — IMPLEMENTATION 001-A BLOCKED ON DPTN EXIT

**DPTN status mirror: COMPLETE DPTN-A; IN EXECUTION DPTN-B; IMPLEMENTATION 001-A BLOCKED ON DPTN EXIT.**

DPTN is a bounded pre-implementation documentation-topology normalization program. It changes where accepted knowledge and preserved history live; it does **not** change accepted DMTZ meaning, stable IDs, architecture, authority semantics, implementation behavior, source integrations, schemas, product tests or deployment configuration.

## Authority boundary

DPTN operates under the completed CKR authority model. Until a later DPTN cutover explicitly moves an accepted owner, the current semantic owner remains the path selected by `docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json`.

A path proposed by DPTN-A is a **future physical destination**, not current semantic authority. Search order, planned destination, directory name and move-map presence never establish current meaning.

DPTN-A is complete/accepted as an inventory/planning phase. DPTN-B has now been explicitly human-selected and is authorized to execute **MOVE-001 through MOVE-006 only**: historical namespace preparation, relocation of history/provenance subtrees, and removal of the corresponding first-class path collisions. No current semantic owner is authorized to move in DPTN-B.

## Program sequence

- **DPTN-A — Topology Authority, Inventory & Move Map: COMPLETE / ACCEPTED.**
- **DPTN-B — Historical Namespace Preparation & Collision Removal: IN EXECUTION.**
- **DPTN-C — Canonical Knowledge Promotion: PLANNED.**
- **DPTN-D — Foundation, CKR & Operational-Policy Decomposition: PLANNED.**
- **DPTN-E — OKF / Documentation Root Convergence: PLANNED.**
- **DPTN-F — Stable References, Agent Routing & Drift Rebinding: PLANNED.**
- **DPTN-G — Conservation Audit, Legacy-Path Retirement & Exit Review: PLANNED.**

Implementation 001-A remains blocked until DPTN-G accepts the normalization exit. DPTN exit will return implementation to NEXT / READY / NOT STARTED; it will not itself start implementation.

## Accepted DPTN-A baseline

- [`topology_authority.md`](topology_authority.md) — allowed changes, invariants and cutover rules;
- [`topology_inventory.json`](topology_inventory.json) — accepted subtree-level lifecycle inventory with mixed-lifecycle exceptions;
- [`move_map.json`](move_map.json) — accepted dependency-safe future source-to-target topology plan;
- [`collision_register.md`](collision_register.md) — occupied target paths and required resolution order;
- [`dptn_a_execution_review.md`](dptn_a_execution_review.md) — DPTN-A acceptance evidence.

## DPTN-B authorized work

DPTN-B may create the explicit non-current `docs/history/` namespace and execute only the accepted historical relocations:

1. `docs/concepts/** → docs/history/phases/**` (MOVE-001);
2. `docs/reference/** → docs/history/reference-legacy/**` (MOVE-002);
3. `docs/foundation/** → docs/history/foundation/**` (MOVE-003);
4. `docs/planning/** → docs/history/planning/**` (MOVE-004);
5. `docs/decisions/** → docs/history/decisions/**` (MOVE-005);
6. `docs/design_history/** → docs/history/design-history/**` (MOVE-006).

The accepted move map remains planning authority; DPTN-B records actual relocation evidence separately so the move map does not become a second semantic ownership ledger.

## DPTN-B forbidden work

DPTN-B may not promote anything from `docs/canonical/`, update canonical ownership targets, rebind stable-ID current locators, bulk-move mixed ADF/CKR directories, converge `knowledge/`, perform DPTN-F agent/OKF rebinding, or start product implementation.

## DPTN-B exit criteria

DPTN-B may complete only when:

1. `docs/history/` exists with an explicit provenance-only/non-current authority contract;
2. MOVE-001 through MOVE-006 are represented by bounded relocation evidence and their source paths are vacated;
3. the relocated historical material remains preserved without semantic rewriting;
4. COL-001 through COL-005 are closed for their DPTN-B responsibilities, making `docs/concepts/`, `docs/reference/` and `docs/decisions/` available for later phases without assigning them current authority;
5. `docs/canonical/` and CKR ownership targets remain unchanged;
6. all 1,237 accepted stable IDs, 24 concepts and ARCH-001–500 remain unchanged;
7. mixed ADF/CKR directories remain in place for DPTN-D;
8. Implementation 001-A remains blocked on DPTN exit;
9. exact-head repository conformance rejects history-as-authority, partial relocation, premature canonical promotion and collision regression.
