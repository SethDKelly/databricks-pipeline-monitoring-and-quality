# Documentation Physical Topology Normalization (DPTN)

**Program status:** ACTIVE — DPTN-A–D COMPLETE / ACCEPTED — DPTN-E NEXT / READY — IMPLEMENTATION 001-A BLOCKED ON DPTN EXIT

**DPTN status mirror: COMPLETE DPTN-A–DPTN-D; NEXT DPTN-E; IMPLEMENTATION 001-A BLOCKED ON DPTN EXIT.**

DPTN is a bounded pre-implementation documentation-topology normalization program. It changes where accepted knowledge, operational policy and preserved history live; it does **not** change accepted DMTZ meaning, stable IDs, architecture, authority semantics, implementation behavior, source integrations, schemas, product tests or deployment configuration.

## Authority boundary

DPTN operates under the completed CKR authority model. DPTN-C completed the path-only current-owner promotion authorized by MOVE-007 through MOVE-014. DPTN-D completed the mixed-lifecycle decomposition authorized by MOVE-015 and MOVE-016. Current semantic authority remains selected by `docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json` at the first-class `docs/<family>/` paths.

Search order, directory name, path vacancy, planned destination, history occurrence, redirect presence and move-map presence never establish current meaning.

## Program sequence

- **DPTN-A — Topology Authority, Inventory & Move Map: COMPLETE / ACCEPTED.**
- **DPTN-B — Historical Namespace Preparation & Collision Removal: COMPLETE / ACCEPTED.**
- **DPTN-C — Canonical Knowledge Promotion: COMPLETE / ACCEPTED.**
- **DPTN-D — Foundation, CKR & Operational-Policy Decomposition: COMPLETE / ACCEPTED.**
- **DPTN-E — OKF / Documentation Root Convergence: NEXT / READY.**
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

DPTN-B established [`../history/README.md`](../history/README.md) as the explicit **HISTORY / PROVENANCE ONLY** root and executed MOVE-001 through MOVE-006. The former Phase 001–010/foundation/reference/planning/decision/design-history material is preserved under `docs/history/`; vacancy never assigned authority.

Accepted evidence: [`dptn_b_relocation_manifest.json`](dptn_b_relocation_manifest.json), [`fixtures/dptn_b_history_scenarios.yaml`](fixtures/dptn_b_history_scenarios.yaml) and [`dptn_b_execution_review.md`](dptn_b_execution_review.md).

## Accepted DPTN-C result

DPTN-C promoted the eight accepted current semantic roots to first-class paths through MOVE-007 through MOVE-014:

- `docs/concepts/`;
- `docs/architecture/`;
- `docs/authority/`;
- `docs/contracts/`;
- `docs/experience/`;
- `docs/invariants/`;
- `docs/policies/`;
- `docs/reference/`.

The CKR ownership inventory selects those first-class owner paths. All 24 concepts, all 1,237 stable IDs across eight families, ARCH-001–ARCH-500 and the frozen reference architecture retain their accepted content and meaning. `docs/canonical/README.md` remains routing/compatibility only pending DPTN-E; any legacy redirects remain non-authoritative pending DPTN-F/G.

Accepted evidence: [`dptn_c_promotion_manifest.json`](dptn_c_promotion_manifest.json), [`fixtures/dptn_c_promotion_scenarios.yaml`](fixtures/dptn_c_promotion_scenarios.yaml) and [`dptn_c_execution_review.md`](dptn_c_execution_review.md).

## Accepted DPTN-D result

DPTN-D resolved the remaining mixed-lifecycle documentation roots without creating a new authority hierarchy prematurely:

- **MOVE-015 / CKR:** durable ownership/routing mechanics remain under `docs/canonical_knowledge_retrofit/`; completed CKR reviews, conservation matrices, manifests and fixtures are preserved under `docs/history/retrofits/ckr/`.
- **MOVE-016 / ADF:** durable agentic authority/context/workflow/conformance/security/compatibility policy and live residual obligations remain under `docs/agentic_development_foundation/`; completed phase-design documents, execution/exit evidence and fixtures are preserved under `docs/history/foundations/adf/`.

COL-006 and COL-007 are resolved. The CKR ownership ledger remains at its existing durable path because relocating it was unnecessary. ADF-G-XT01 remains deferred verification and its live procedure/evidence remains current. Broad route rebinding is still deferred to DPTN-F, after DPTN-E settles the discovery-root topology.

Accepted evidence: [`dptn_d_decomposition_manifest.json`](dptn_d_decomposition_manifest.json), [`fixtures/dptn_d_decomposition_scenarios.yaml`](fixtures/dptn_d_decomposition_scenarios.yaml) and [`dptn_d_execution_review.md`](dptn_d_execution_review.md).

## DPTN-E handoff boundary

**DPTN-E is NEXT / READY / NOT STARTED.** DPTN-D acceptance does not authorize it automatically. Until DPTN-E is explicitly human-selected:

- first-class `docs/<family>/` roots remain current semantic owners;
- durable CKR and ADF operational roots remain current for their non-semantic authority/policy roles;
- `knowledge/` remains the separate derived routing plane;
- `docs/canonical/README.md` remains the compatibility/orientation surface;
- broad legacy-link/agent rebinding remains deferred to DPTN-F;
- Implementation 001-A remains blocked.
