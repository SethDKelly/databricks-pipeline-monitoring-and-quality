# Documentation Physical Topology Normalization (DPTN)

**Program status:** ACTIVE — DPTN-A COMPLETE / ACCEPTED — DPTN-B NEXT / READY — IMPLEMENTATION 001-A BLOCKED ON DPTN EXIT

**DPTN status mirror: COMPLETE DPTN-A; NEXT DPTN-B; IMPLEMENTATION 001-A BLOCKED ON DPTN EXIT.**

DPTN is a bounded pre-implementation documentation-topology normalization program. It changes where accepted knowledge and preserved history live; it does **not** change accepted DMTZ meaning, stable IDs, architecture, authority semantics, implementation behavior, source integrations, schemas, product tests or deployment configuration.

## Authority boundary

DPTN operates under the completed CKR authority model. Until a later DPTN cutover explicitly moves an accepted owner, the current semantic owner remains the path selected by `docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json`.

A path proposed by DPTN-A is a **future physical destination**, not current semantic authority. Search order, planned destination, directory name and move-map presence never establish current meaning.

DPTN-A is complete/accepted as an inventory/planning phase. **No current semantic owner, historical corpus, implementation plan, OKF route or agent adapter was physically moved in DPTN-A.** DPTN-B is next/ready but has not started.

## Program sequence

- **DPTN-A — Topology Authority, Inventory & Move Map: COMPLETE / ACCEPTED.**
- **DPTN-B — Historical Namespace Preparation & Collision Removal: NEXT / READY.**
- **DPTN-C — Canonical Knowledge Promotion: PLANNED.**
- **DPTN-D — Foundation, CKR & Operational-Policy Decomposition: PLANNED.**
- **DPTN-E — OKF / Documentation Root Convergence: PLANNED.**
- **DPTN-F — Stable References, Agent Routing & Drift Rebinding: PLANNED.**
- **DPTN-G — Conservation Audit, Legacy-Path Retirement & Exit Review: PLANNED.**

Implementation 001-A remains blocked until DPTN-G accepts the normalization exit. DPTN exit will return implementation to NEXT / READY / NOT STARTED; it will not itself start implementation.

## Accepted DPTN-A deliverables

- [`topology_authority.md`](topology_authority.md) — allowed changes, invariants and cutover rules;
- [`topology_inventory.json`](topology_inventory.json) — accepted subtree-level lifecycle inventory with mixed-lifecycle exceptions;
- [`move_map.json`](move_map.json) — accepted dependency-safe future source-to-target topology plan;
- [`collision_register.md`](collision_register.md) — occupied target paths and required resolution order;
- [`dptn_a_execution_review.md`](dptn_a_execution_review.md) — acceptance evidence and DPTN-B handoff.

## DPTN-A accepted boundary

DPTN-A acceptance establishes the move plan and dependency order only. It does not authorize DPTN-B automatically and does not make any proposed target path current authority. Until DPTN-B is explicitly selected:

1. every in-scope documentation/routing surface remains at its current physical path;
2. `docs/canonical/` remains the current semantic root;
3. `docs/history/` is not yet created as the normalized history namespace;
4. mixed ADF/CKR lifecycle material remains in place;
5. stable-ID ranges and accepted concept/architecture counts remain unchanged;
6. Implementation 001-A remains mechanically blocked on DPTN exit.
