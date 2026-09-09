# Documentation Physical Topology Normalization (DPTN)

**Program status:** ACTIVE — DPTN-A IN EXECUTION / IMPLEMENTATION 001-A BLOCKED ON DPTN EXIT

**DPTN status mirror: IN EXECUTION DPTN-A; IMPLEMENTATION 001-A BLOCKED ON DPTN EXIT.**

DPTN is a bounded pre-implementation documentation-topology normalization program. It changes where accepted knowledge and preserved history live; it does **not** change accepted DMTZ meaning, stable IDs, architecture, authority semantics, implementation behavior, source integrations, schemas, product tests or deployment configuration.

## Authority boundary

DPTN operates under the completed CKR authority model. Until a later DPTN cutover explicitly moves an accepted owner, the current semantic owner remains the path selected by `docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json`.

A path proposed by DPTN-A is a **future physical destination**, not current semantic authority. Search order, planned destination, directory name and move-map presence never establish current meaning.

DPTN-A is inventory/planning only: **no current semantic owner, historical corpus, implementation plan, OKF route or agent adapter is physically moved in this phase.**

## Program sequence

- **DPTN-A — Topology Authority, Inventory & Move Map: IN EXECUTION.**
- **DPTN-B — Historical Namespace Preparation & Collision Removal: PLANNED.**
- **DPTN-C — Canonical Knowledge Promotion: PLANNED.**
- **DPTN-D — Foundation, CKR & Operational-Policy Decomposition: PLANNED.**
- **DPTN-E — OKF / Documentation Root Convergence: PLANNED.**
- **DPTN-F — Stable References, Agent Routing & Drift Rebinding: PLANNED.**
- **DPTN-G — Conservation Audit, Legacy-Path Retirement & Exit Review: PLANNED.**

Implementation 001-A remains blocked until DPTN-G accepts the normalization exit. DPTN exit will return implementation to NEXT / READY / NOT STARTED; it will not itself start implementation.

## DPTN-A deliverables

- [`topology_authority.md`](topology_authority.md) — allowed changes, invariants and cutover rules;
- [`topology_inventory.json`](topology_inventory.json) — complete subtree-level lifecycle inventory with mixed-lifecycle exceptions;
- [`move_map.json`](move_map.json) — dependency-safe future source-to-target topology plan;
- [`collision_register.md`](collision_register.md) — occupied target paths and required resolution order;
- [`dptn_a_execution_review.md`](dptn_a_execution_review.md) — acceptance evidence and handoff.

## DPTN-A exit criteria

DPTN-A may complete only when:

1. every in-scope documentation/routing surface is covered by an inventory rule or explicit exception;
2. every planned physical move has one target role and one execution phase;
3. current semantic owners remain unchanged;
4. target-path collisions are explicitly registered and dependency ordered;
5. mixed ADF/CKR lifecycle material is deferred to file-level decomposition rather than bulk moved;
6. stable-ID ranges and accepted concept/architecture counts remain unchanged;
7. Implementation 001-A is mechanically blocked on DPTN exit;
8. repository conformance validates DPTN-A and rejects premature physical moves or authority promotion.
