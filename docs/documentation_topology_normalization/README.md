# Documentation Physical Topology Normalization (DPTN)

**Program status:** ACTIVE — DPTN-A–C COMPLETE / ACCEPTED — DPTN-D NEXT / READY — IMPLEMENTATION 001-A BLOCKED ON DPTN EXIT

**DPTN status mirror: COMPLETE DPTN-A–DPTN-C; NEXT DPTN-D; IMPLEMENTATION 001-A BLOCKED ON DPTN EXIT.**

DPTN is a bounded pre-implementation documentation-topology normalization program. It changes where accepted knowledge and preserved history live; it does **not** change accepted DMTZ meaning, stable IDs, architecture, authority semantics, implementation behavior, source integrations, schemas, product tests or deployment configuration.

## Authority boundary

DPTN operates under the completed CKR authority model. DPTN-C completed the path-only current-owner promotion authorized by MOVE-007 through MOVE-014. Current semantic authority is now selected by `docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json` at the first-class `docs/<family>/` paths.

Search order, directory name, path vacancy, planned destination, history occurrence, redirect presence and move-map presence never establish current meaning.

DPTN-A accepted the topology inventory and dependency-safe move plan. DPTN-B accepted the historical namespace and executed MOVE-001 through MOVE-006. DPTN-C promoted the eight accepted current semantic roots and rebound the ownership ledger atomically without semantic change.

## Program sequence

- **DPTN-A — Topology Authority, Inventory & Move Map: COMPLETE / ACCEPTED.**
- **DPTN-B — Historical Namespace Preparation & Collision Removal: COMPLETE / ACCEPTED.**
- **DPTN-C — Canonical Knowledge Promotion: COMPLETE / ACCEPTED.**
- **DPTN-D — Foundation, CKR & Operational-Policy Decomposition: NEXT / READY.**
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

The original source roots were vacated. COL-001 through COL-005 were resolved for their DPTN-B responsibilities. Vacancy is **not** authority.

Accepted evidence: [`dptn_b_relocation_manifest.json`](dptn_b_relocation_manifest.json), [`fixtures/dptn_b_history_scenarios.yaml`](fixtures/dptn_b_history_scenarios.yaml) and [`dptn_b_execution_review.md`](dptn_b_execution_review.md).

## Accepted DPTN-C result

DPTN-C completed the eight current semantic-owner promotions using exact accepted Git trees and one path-only authority cutover:

1. `docs/canonical/concepts/** → docs/concepts/**` — MOVE-007;
2. `docs/canonical/architecture/** → docs/architecture/**` — MOVE-008;
3. `docs/canonical/authority/** → docs/authority/**` — MOVE-009;
4. `docs/canonical/contracts/** → docs/contracts/**` — MOVE-010;
5. `docs/canonical/experience/** → docs/experience/**` — MOVE-011;
6. `docs/canonical/invariants/** → docs/invariants/**` — MOVE-012;
7. `docs/canonical/policies/** → docs/policies/**` — MOVE-013;
8. `docs/canonical/reference/** → docs/reference/**` — MOVE-014.

The CKR ownership inventory now selects those first-class owner paths. All 24 concepts, all 1,237 stable IDs across eight families, ARCH-001–ARCH-500 and the frozen reference architecture retain their accepted content and meaning.

`docs/canonical/README.md` remains a routing/compatibility surface pending DPTN-E. Any `docs/canonical/<family>` compatibility redirects are non-authoritative, are not ownership-ledger targets, and remain subject to later DPTN-F/G rebinding and retirement. `docs/history/` remains provenance-only.

Accepted evidence: [`dptn_c_promotion_manifest.json`](dptn_c_promotion_manifest.json), [`fixtures/dptn_c_promotion_scenarios.yaml`](fixtures/dptn_c_promotion_scenarios.yaml) and [`dptn_c_execution_review.md`](dptn_c_execution_review.md).

## DPTN-D handoff boundary

**DPTN-D is NEXT / READY / NOT STARTED.** DPTN-C acceptance does not authorize it automatically. Until DPTN-D is explicitly human-selected:

- the eight first-class `docs/<family>/` roots remain current semantic owners;
- mixed `docs/agentic_development_foundation/` and `docs/canonical_knowledge_retrofit/` directories remain in place;
- `knowledge/` remains the derived routing plane pending DPTN-E;
- broad legacy-link/agent rebinding remains deferred to DPTN-F;
- Implementation 001-A remains blocked.
