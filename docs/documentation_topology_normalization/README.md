# Documentation Physical Topology Normalization (DPTN)

**Program status:** ACTIVE — DPTN-A–B COMPLETE / ACCEPTED — DPTN-C NEXT / READY — IMPLEMENTATION 001-A BLOCKED ON DPTN EXIT

**DPTN status mirror: COMPLETE DPTN-A–DPTN-B; NEXT DPTN-C; IMPLEMENTATION 001-A BLOCKED ON DPTN EXIT.**

DPTN is a bounded pre-implementation documentation-topology normalization program. It changes where accepted knowledge and preserved history live; it does **not** change accepted DMTZ meaning, stable IDs, architecture, authority semantics, implementation behavior, source integrations, schemas, product tests or deployment configuration.

## Authority boundary

DPTN operates under the completed CKR authority model. Until a later DPTN cutover explicitly moves an accepted owner, the current semantic owner remains the path selected by `docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json`.

Search order, directory name, path vacancy, planned destination, history occurrence and move-map presence never establish current meaning.

DPTN-A accepted the topology inventory and dependency-safe move plan. DPTN-B accepted the historical namespace and executed MOVE-001 through MOVE-006 only. **No current semantic owner moved in DPTN-B.** `docs/canonical/` remains the current semantic root.

## Program sequence

- **DPTN-A — Topology Authority, Inventory & Move Map: COMPLETE / ACCEPTED.**
- **DPTN-B — Historical Namespace Preparation & Collision Removal: COMPLETE / ACCEPTED.**
- **DPTN-C — Canonical Knowledge Promotion: NEXT / READY.**
- **DPTN-D — Foundation, CKR & Operational-Policy Decomposition: PLANNED.**
- **DPTN-E — OKF / Documentation Root Convergence: PLANNED.**
- **DPTN-F — Stable References, Agent Routing & Drift Rebinding: PLANNED.**
- **DPTN-G — Conservation Audit, Legacy-Path Retirement & Exit Review: PLANNED.**

Implementation 001-A remains blocked until DPTN-G accepts the normalization exit. DPTN exit will return implementation to NEXT / READY / NOT STARTED; it will not itself start implementation.

## Accepted DPTN-A baseline

- [`topology_authority.md`](topology_authority.md) — allowed changes, invariants and cutover rules;
- [`topology_inventory.json`](topology_inventory.json) — accepted lifecycle inventory;
- [`move_map.json`](move_map.json) — accepted dependency-safe move plan;
- [`collision_register.md`](collision_register.md) — collision state and phase ownership;
- [`dptn_a_execution_review.md`](dptn_a_execution_review.md) — DPTN-A acceptance evidence.

## Accepted DPTN-B result

DPTN-B established [`../history/README.md`](../history/README.md) as the explicit **HISTORY / PROVENANCE ONLY** root and executed the six accepted relocations using exact pre-DPTN Git trees:

1. `docs/concepts/** → docs/history/phases/**` — MOVE-001;
2. `docs/reference/** → docs/history/reference-legacy/**` — MOVE-002;
3. `docs/foundation/** → docs/history/foundation/**` — MOVE-003;
4. `docs/planning/** → docs/history/planning/**` — MOVE-004;
5. `docs/decisions/** → docs/history/decisions/**` — MOVE-005;
6. `docs/design_history/** → docs/history/design-history/**` — MOVE-006.

The original source roots are vacated. COL-001 through COL-005 are resolved for their DPTN-B responsibilities. Vacancy is **not** authority: the cleared first-class paths remain unassigned until an explicitly selected later DPTN phase reuses them.

Accepted evidence: [`dptn_b_relocation_manifest.json`](dptn_b_relocation_manifest.json), [`fixtures/dptn_b_history_scenarios.yaml`](fixtures/dptn_b_history_scenarios.yaml) and [`dptn_b_execution_review.md`](dptn_b_execution_review.md).

Completed CKR semantic/provenance checks may use an ephemeral legacy-source compatibility projection during validation so their accepted original-path evidence remains executable. That projection is validation-only, leaves no repository path behind and cannot satisfy current semantic routing. Permanent historical-reference rebinding remains later DPTN routing work after physical topology stabilizes.

## DPTN-C handoff boundary

**DPTN-C is NEXT / READY / NOT STARTED.** DPTN-B acceptance does not authorize it automatically. Until DPTN-C is explicitly human-selected:

- `docs/canonical/` remains the current semantic root;
- `docs/concepts/`, `docs/reference/` and `docs/decisions/` remain vacant/unassigned;
- no canonical ownership target or current stable-ID locator moves;
- mixed `docs/agentic_development_foundation/` and `docs/canonical_knowledge_retrofit/` directories remain in place for DPTN-D;
- `knowledge/` remains the current derived routing plane;
- Implementation 001-A remains blocked.
