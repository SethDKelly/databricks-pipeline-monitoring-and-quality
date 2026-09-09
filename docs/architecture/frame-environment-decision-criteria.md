# Architecture Frame, Environment Discovery & Decision Criteria

**Canonical key:** `architecture.frame_environment_decision_criteria`

**Kind:** TECHNICAL ARCHITECTURE CONTRACT

**Authority:** CANONICAL CURRENT AUTHORITY

**Migration records:** `stable_family.ARCH`, `architecture.frame_environment_decision_criteria`

**Stable IDs:** ARCH-001–ARCH-032

**Stable ID index:** `ARCH-001`, `ARCH-002`, `ARCH-003`, `ARCH-004`, `ARCH-005`, `ARCH-006`, `ARCH-007`, `ARCH-008`, `ARCH-009`, `ARCH-010`, `ARCH-011`, `ARCH-012`, `ARCH-013`, `ARCH-014`, `ARCH-015`, `ARCH-016`, `ARCH-017`, `ARCH-018`, `ARCH-019`, `ARCH-020`, `ARCH-021`, `ARCH-022`, `ARCH-023`, `ARCH-024`, `ARCH-025`, `ARCH-026`, `ARCH-027`, `ARCH-028`, `ARCH-029`, `ARCH-030`, `ARCH-031`, `ARCH-032`

**Owns current question after cutover:** What target-environment facts, service classes, hard constraints and decision discipline bound every later DMTZ architecture choice?

## Canonical contract

The architecture decision chain is:

**public/vendor capability statement → deployment-bound capability instance → provenance-bearing environment verification → dimensioned capability facts + unknowns → proposition/service-class usability → hard constraints + decision-specific tradeoffs → MVP/enterprise/gap ownership → reversible implementation ADR**.

No arrow establishes the next by convenience. In particular:

**documented capability ≠ deployment presence ≠ entitlement ≠ enablement ≠ permission ≠ reachability ≠ observable coverage ≠ proposition-specific usability**.

Target capability is bound to the concrete deployment context: vendor/product, hosting/deployment model, cloud/region/Geo, account/tenant/workspace/metastore/repository scope, edition/plan/license/version, preview/feature enablement, permission, reachability, residency/compliance, retention/time, quota/capacity/cost, integration health, provenance and verification time.

Unknown target facts remain unknown. Public documentation can establish possible support; it cannot establish deployment support.

## Scope and architecture quality

Architecture classifies capabilities as MVP-core, enterprise, optional or conditional. Organization-owned capabilities are required where DMTZ promises propositions that no vendor natively owns, including bounded Monitoring Scope, authority/policy and correlation/retention obligations.

Semantic correctness, evidence discipline, security/disclosure, historical non-rewriting and degraded-state honesty are hard constraints. A simpler, faster or cheaper option cannot win by weakening them.

Material ADRs use decision-specific quality attributes such as durability, availability, latency, scalability, operational simplicity, observability/testability, reversibility, quota efficiency, portability, performance, cost and maintainability. No universal architecture score or weighted score becomes architectural truth.

## Service classes

Six use classes constrain later latency, completeness and retention decisions without creating one universal SLA:

1. `SC-01` — near-current operational facts;
2. `SC-02` — periodic core health/quality;
3. `SC-03` — enriched Investigation/RCA;
4. `SC-04` — historical/as-known replay;
5. `SC-05` — retained communication/basis inspection;
6. `SC-06` — active control.

Numeric objectives are deployment-informed ADRs, not semantic defaults.

## Decision and failure discipline

Maintain an assumption/unknown register, provenance-bearing alternative analysis for material choices, supersession/rollback history, explicit GAP-009 ownership, cross-group entry preconditions and deployment-bound cost/quota/retention facts.

Architecture or integration failure never becomes a monitored-domain negative fact. Optional-source absence narrows dependent capability rather than fabricating a benign replacement.

Security, residency, disclosure and sensitive-metadata constraints apply to architecture decisions before optimization.

## Architecture boundary

This segment establishes the frame and does not mandate a persistence engine, graph database, event bus, queue, orchestrator, model/retrieval system, policy engine, API framework, control runtime or deployment platform.

## Provenance

- `docs/concepts/phase_010/01_architecture_frame_environment_discovery_decision_criteria/README.md`
- atomic ARCH-001–ARCH-032 files under that Phase 010 group
- Phase 010 decisions D-1269–D-1298 and AFE01-01–AFE01-60 review evidence
