# DMTZ Documentation Physical Topology Normalization

**Program status:** DPTN ACTIVE — DPTN-A COMPLETE / ACCEPTED — DPTN-B NEXT / READY / NOT STARTED — IMPLEMENTATION 001-A BLOCKED ON DPTN EXIT

**DPTN status mirror: COMPLETE DPTN-A; NEXT DPTN-B; IMPLEMENTATION 001-A BLOCKED ON DPTN EXIT.**

DPTN is a bounded pre-implementation documentation-topology program. It changes where accepted documentation lives and how humans/agents route to it; it does not change DMTZ semantics, accepted stable IDs, technical architecture, source capability conclusions, product code, schemas, integrations, or implementation evidence.

## Program progression

- **DPTN-A — Topology Authority, Inventory & Move Map: COMPLETE / ACCEPTED.**
- **DPTN-B — Historical Namespace Preparation & Collision Removal: NEXT / READY / NOT STARTED.**
- **DPTN-C — Canonical Knowledge Promotion: PLANNED.**
- **DPTN-D — Foundation, CKR & Operational-Policy Decomposition: PLANNED.**
- **DPTN-E — OKF / Documentation Root Convergence: PLANNED.**
- **DPTN-F — Stable References, Agent Routing & Drift Rebinding: PLANNED.**
- **DPTN-G — Conservation Audit, Legacy-Path Retirement & Exit Review: PLANNED.**

Implementation 001-A remains **BLOCKED ON DPTN EXIT**. DPTN completion will return implementation to NEXT / READY / NOT STARTED; it will not start product implementation automatically.

## DPTN-A accepted boundary

DPTN-A established the topology authority, complete in-scope inventory, collision policy and dependency-safe move map. It performed no physical relocation.

Accepted planning results:
- 40 classified documentation/routing/agent surfaces at file or recursive-root granularity;
- 33 bounded future DPTN-B–G operations;
- explicit history-first collision ordering for `docs/concepts/` and `docs/reference/`;
- explicit split requirement for mixed CKR and ADF directories;
- target first-class documentation topology and `docs/history/` namespace;
- 24 DPTN-A scenarios and 11 adversarial topology guards.

Current semantic ownership remains governed by the completed CKR ownership inventory until later DPTN groups perform validated path cutovers.

## DPTN-A artifacts

- `topology_authority.md` — accepted normalization authority and non-semantic invariants.
- `topology_inventory.json` — accepted in-scope surface inventory by recursive root/file.
- `move_map.json` — accepted dependency-safe old-path → target-path execution map for DPTN-B–G; **NO OPERATIONS AUTHORIZED** until the relevant later group is explicitly selected.
- `target_topology.md` — intended post-DPTN physical shape and collision policy.
- `fixtures/dptn_a_topology_scenarios.yaml` — accepted planning/guard scenarios.
- `dptn_a_execution_review.md` — DPTN-A evidence and exit decision.

## Stop rule

DPTN-B is NEXT / READY / NOT STARTED only. No history root, file move, rename, deletion, canonical promotion, resolver rebinding, or other physical topology operation is authorized until a subsequent explicit human-selected DPTN-B task begins.
