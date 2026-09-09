# DMTZ Documentation Physical Topology Normalization

**Program status:** DPTN ACTIVE — DPTN-A IN EXECUTION — IMPLEMENTATION 001-A BLOCKED ON DPTN EXIT

**DPTN status mirror: IN EXECUTION DPTN-A; IMPLEMENTATION 001-A BLOCKED ON DPTN EXIT.**

DPTN is a bounded pre-implementation documentation-topology program. It changes where accepted documentation lives and how humans/agents route to it; it does not change DMTZ semantics, accepted stable IDs, technical architecture, source capability conclusions, product code, schemas, integrations, or implementation evidence.

## Program progression

- **DPTN-A — Topology Authority, Inventory & Move Map: IN EXECUTION.**
- **DPTN-B — Historical Namespace Preparation & Collision Removal: PLANNED.**
- **DPTN-C — Canonical Knowledge Promotion: PLANNED.**
- **DPTN-D — Foundation, CKR & Operational-Policy Decomposition: PLANNED.**
- **DPTN-E — OKF / Documentation Root Convergence: PLANNED.**
- **DPTN-F — Stable References, Agent Routing & Drift Rebinding: PLANNED.**
- **DPTN-G — Conservation Audit, Legacy-Path Retirement & Exit Review: PLANNED.**

Implementation 001-A remains **BLOCKED ON DPTN EXIT**. DPTN completion will return implementation to NEXT / READY / NOT STARTED; it will not start product implementation automatically.

## DPTN-A authority boundary

DPTN-A is inventory/planning only.

Allowed:
- classify current documentation surfaces by lifecycle/authority role;
- define the target first-class documentation topology;
- define exact root/file move operations, collision order, split rules and later-phase preconditions;
- add DPTN-only validation, fixtures and status synchronization.

Forbidden:
- physical move, rename, deletion or path cutover of existing documentation;
- semantic rewrite or consolidation of accepted DMTZ meaning;
- stable-ID addition, deletion, renumbering or meaning change;
- technical architecture change;
- product source/schema/test/deployment/integration implementation;
- treating the DPTN inventory/move map as a second semantic authority registry.

Current semantic ownership remains governed by the completed CKR ownership inventory until later DPTN groups perform validated path cutovers.

## DPTN-A artifacts

- `topology_authority.md` — normalization authority and non-semantic invariants.
- `topology_inventory.json` — complete in-scope surface inventory by recursive root/file.
- `move_map.json` — dependency-safe old-path → target-path execution map for DPTN-B–G.
- `target_topology.md` — intended post-DPTN physical shape and collision policy.
- `fixtures/dptn_a_topology_scenarios.yaml` — bounded planning/guard scenarios.
- `dptn_a_execution_review.md` — phase evidence and exit decision.

## Stop rule

No DPTN-B physical relocation is authorized merely because DPTN-A completes. A subsequent explicit human-selected DPTN-B task is required.
