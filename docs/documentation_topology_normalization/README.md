# Documentation Physical Topology Normalization (DPTN)

**Program status:** ACTIVE — DPTN-A–B COMPLETE / ACCEPTED — DPTN-C IN EXECUTION — IMPLEMENTATION 001-A BLOCKED ON DPTN EXIT

**DPTN status mirror: COMPLETE DPTN-A–DPTN-B; IN EXECUTION DPTN-C; IMPLEMENTATION 001-A BLOCKED ON DPTN EXIT.**

DPTN is a bounded pre-implementation documentation-topology normalization program. It changes where accepted knowledge and preserved history live; it does **not** change accepted DMTZ meaning, stable IDs, architecture, authority semantics, implementation behavior, source integrations, schemas, product tests or deployment configuration.

## Authority boundary

DPTN operates under the completed CKR authority model. During DPTN-C, current semantic authority remains the ownership selected by `docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json`; the eight MOVE-007–MOVE-014 owners may change path only through one atomic cutover that synchronizes physical trees and the ownership ledger.

Search order, directory name, path vacancy, planned destination, history occurrence, redirect presence and move-map presence never establish current meaning.

DPTN-A accepted the topology inventory and dependency-safe move plan. DPTN-B accepted the historical namespace and executed MOVE-001 through MOVE-006 only. DPTN-C is now explicitly human-selected to execute MOVE-007 through MOVE-014 only.

## Program sequence

- **DPTN-A — Topology Authority, Inventory & Move Map: COMPLETE / ACCEPTED.**
- **DPTN-B — Historical Namespace Preparation & Collision Removal: COMPLETE / ACCEPTED.**
- **DPTN-C — Canonical Knowledge Promotion: IN EXECUTION.**
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

The original source roots were vacated. COL-001 through COL-005 are resolved for their DPTN-B responsibilities. Vacancy is **not** authority.

Accepted evidence: [`dptn_b_relocation_manifest.json`](dptn_b_relocation_manifest.json), [`fixtures/dptn_b_history_scenarios.yaml`](fixtures/dptn_b_history_scenarios.yaml) and [`dptn_b_execution_review.md`](dptn_b_execution_review.md).

## DPTN-C execution boundary

The user explicitly selected DPTN-C. This authorizes only the canonical-owner path promotions MOVE-007 through MOVE-014 and directly necessary ownership/resolver/validation compatibility work:

1. `docs/canonical/concepts/** → docs/concepts/**` — MOVE-007;
2. `docs/canonical/architecture/** → docs/architecture/**` — MOVE-008;
3. `docs/canonical/authority/** → docs/authority/**` — MOVE-009;
4. `docs/canonical/contracts/** → docs/contracts/**` — MOVE-010;
5. `docs/canonical/experience/** → docs/experience/**` — MOVE-011;
6. `docs/canonical/invariants/** → docs/invariants/**` — MOVE-012;
7. `docs/canonical/policies/** → docs/policies/**` — MOVE-013;
8. `docs/canonical/reference/** → docs/reference/**` — MOVE-014.

DPTN-C must preserve the exact semantic trees while atomically rebinding the CKR ownership ledger to the promoted paths. `docs/canonical/README.md` remains an orientation/compatibility surface for DPTN-E; it is not a substantive semantic owner after the cutover. Any temporary legacy-path redirects under `docs/canonical/` are routing compatibility only, must not appear in the ownership ledger, and are subject to later DPTN-F/G rebinding and retirement.

DPTN-C does **not** authorize:

- DPTN-D mixed-lifecycle ADF/CKR decomposition;
- DPTN-E OKF/root convergence;
- complete DPTN-F agent/OKF/link rebinding or legacy-path retirement;
- semantic changes, stable-ID changes or concept changes;
- product implementation.

Until the atomic C cutover is validated, the pre-cutover CKR paths remain the current owners. After an accepted cutover, only the normalized first-class paths selected by the ownership ledger are current semantic owners; redirect paths are non-authoritative compatibility routes.

Implementation 001-A remains blocked throughout DPTN-C.
