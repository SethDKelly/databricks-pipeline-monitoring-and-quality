# Documentation Physical Topology Normalization (DPTN)

**Program status:** ACTIVE — DPTN-A–E COMPLETE / ACCEPTED — DPTN-F NEXT / READY — IMPLEMENTATION 001-A BLOCKED ON DPTN EXIT

**DPTN status mirror: COMPLETE DPTN-A–DPTN-E; NEXT DPTN-F; IMPLEMENTATION 001-A BLOCKED ON DPTN EXIT.**

DPTN is a bounded pre-implementation documentation-topology normalization program. It changes where accepted knowledge, operational policy, routing projections and preserved history live; it does **not** change accepted DMTZ meaning, stable IDs, architecture, authority semantics, implementation behavior, source integrations, schemas, product tests or deployment configuration.

## Authority boundary

Current semantic authority remains selected by `docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json` at first-class `docs/<family>/` paths. `docs/index.md`, OKF, history, redirects, move maps and generated routing output are never semantic owners.

## Program sequence

- **DPTN-A — Topology Authority, Inventory & Move Map: COMPLETE / ACCEPTED.**
- **DPTN-B — Historical Namespace Preparation & Collision Removal: COMPLETE / ACCEPTED.**
- **DPTN-C — Canonical Knowledge Promotion: COMPLETE / ACCEPTED.**
- **DPTN-D — Foundation, CKR & Operational-Policy Decomposition: COMPLETE / ACCEPTED.**
- **DPTN-E — OKF / Documentation Root Convergence: COMPLETE / ACCEPTED.**
- **DPTN-F — Stable References, Agent Routing & Drift Rebinding: NEXT / READY.**
- **DPTN-G — Conservation Audit, Legacy-Path Retirement & Exit Review: PLANNED.**

Implementation 001-A remains blocked until DPTN-G accepts the normalization exit. DPTN exit will return implementation to NEXT / READY / NOT STARTED; it will not itself start implementation.

## Accepted DPTN-A–D baseline

DPTN-A accepted [`topology_authority.md`](topology_authority.md), [`topology_inventory.json`](topology_inventory.json), [`move_map.json`](move_map.json) and the collision register. DPTN-B relocated history through MOVE-001–006. DPTN-C promoted the eight semantic owner families through MOVE-007–014. DPTN-D decomposed mixed CKR/ADF lifecycle roots through MOVE-015/016. Their accepted manifests, scenarios and execution reviews remain phase evidence.

## Accepted DPTN-E result

DPTN-E executed MOVE-017 and MOVE-018 without semantic-authority change:

- [`../index.md`](../index.md) is now the **single authored human/tool-neutral discovery root**.
- `docs/README.md` remains the separate sole living authority for completed Phase 002–010 design progression.
- The complete pre-DPTN-E authored `knowledge/` tree is preserved unchanged at `docs/history/routing/okf-pre-dptn-e/`.
- Live top-level `knowledge/` is now a **deterministically generated OKF v0.2 compatibility projection**.
- [`../routing/okf_projection.json`](../routing/okf_projection.json) is the bounded derived-routing specification; it is not another ownership ledger.
- `scripts/agentic/generate_okf_projection.py --check` enforces generated-tree reproducibility.
- Seven domain and nine project OKF concepts remain available; workflow and implementation catalogs are generated directly from `.agents/skills/` and `docs/implementation/` rather than duplicated as authored concept files.
- `docs/canonical/README.md` is compatibility/orientation only and points to `docs/index.md`; family redirects remain pending DPTN-F/G.

COL-008 and COL-013 are resolved by DPTN-E. COL-011 and the remaining COL-009 routing cleanup are deliberately retained for DPTN-F. COL-012 remains active through DPTN-G.

Accepted evidence: [`dptn_e_convergence_manifest.json`](dptn_e_convergence_manifest.json), [`fixtures/dptn_e_convergence_scenarios.yaml`](fixtures/dptn_e_convergence_scenarios.yaml) and [`dptn_e_execution_review.md`](dptn_e_execution_review.md).

## Conservation baseline

DPTN-E preserves 24 concepts, all 1,237 stable IDs across eight families, SYN-001–035, REF-001–030, AUTH-001–053, HLTH-001–066, OPS-001–123, EXPL-001–160, INTG-001–270, ARCH-001–500, the frozen reference architecture, accepted ADF/CKR exits and the Implementation 001-A blocker.

Generated OKF metadata is routing only. It cannot strengthen truth, authority, authorization, evidence, causal, health, implementation or deployment status.

## DPTN-F handoff boundary

**DPTN-F — Stable References, Agent Routing & Drift Rebinding: NEXT / READY / NOT STARTED.** DPTN-E acceptance does not authorize it automatically.

Until DPTN-F is explicitly human-selected:

- first-class `docs/<family>/` roots remain current semantic owners;
- `docs/index.md` is the authored discovery root;
- `knowledge/` is generated compatibility only;
- legacy canonical family redirects may remain;
- broad agent/rule/link rebinding is not yet complete;
- Implementation 001-A remains blocked.
