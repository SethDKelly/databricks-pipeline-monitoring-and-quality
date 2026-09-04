# Canonical Ownership Inventory — Human View

The machine-readable authority ledger is [`canonical_ownership_inventory.json`](canonical_ownership_inventory.json). This page summarizes its migration plan; it is not a second independently maintained ownership registry.

## Baseline result

CKR-A confirms the repository currently contains **distributed legacy authority** rather than one current-truth layer. That is expected given the chronological design process and is the reason for CKR.

At CKR-A baseline:

- all substantive semantic records remain `legacy_authoritative`;
- `docs/canonical/` contains structural indexes only;
- all 24 accepted concepts have an explicit current owner and exact target canonical path;
- all accepted stable-ID families have an inventoried current phase root, target canonical domain and migration group;
- Phase 010 is segmented into eight ARCH ranges plus the accepted reference-architecture owner;
- design-history sources are classified without bulk-moving them.

## Foundation/reference migration

| Area | Current owner | Target | Group |
|---|---|---|---|
| Product definition | `docs/foundation/001_product_definition.md` | `docs/canonical/reference/product-definition.md` | CKR-B |
| Actors/stakeholders | `docs/foundation/002_actors_and_stakeholders.md` | `docs/canonical/reference/actors-and-stakeholders.md` | CKR-B |
| Terminology | `docs/foundation/003_terminology.md` | `docs/canonical/reference/terminology.md` | CKR-B |
| Concept Design method | `docs/foundation/004_concept_design_method.md` | `docs/canonical/reference/concept-design-method.md` | CKR-B |
| Architectural principles | `docs/foundation/005_architectural_principles.md` | `docs/canonical/invariants/architectural-principles.md` | CKR-B |
| Security/governance foundation | `docs/foundation/006_security_governance_and_policy_model.md` | `docs/canonical/policies/security-governance.md` | CKR-B |
| Ecosystem lifecycles | `docs/foundation/007_ecosystem_lifecycles.md` | `docs/canonical/reference/ecosystem-lifecycles.md` | CKR-B |
| MVP boundary | `docs/foundation/008_mvp_boundary.md` | `docs/canonical/policies/mvp-boundary.md` | CKR-B |
| Glossary | `docs/reference/glossary.md` | `docs/canonical/reference/glossary.md` | CKR-B |
| Authority vocabulary | `docs/reference/authority_vocabulary.md` | `docs/canonical/authority/vocabulary.md` | CKR-D |

## Concept migration

All **24** accepted concepts are inventoried individually for CKR-C.

Examples:

| Concept | Current owner | Target |
|---|---|---|
| Monitoring Scope | `docs/concepts/phase_002/01_scope_and_identity/monitoring_scope.md` | `docs/canonical/concepts/monitoring-scope.md` |
| Observation | `docs/concepts/phase_002/03_health_evaluation/observation.md` | `docs/canonical/concepts/observation.md` |
| Lineage | `docs/concepts/phase_002/04_history_lineage_change/lineage.md` | `docs/canonical/concepts/lineage.md` |
| Impact | `docs/concepts/phase_002/05_investigation_impact_explanation/impact.md` | `docs/canonical/concepts/impact.md` |
| Assertion Authority | `docs/concepts/phase_002/addenda/assertion_authority.md` | `docs/canonical/concepts/assertion-authority.md` |
| Execution Gate | `docs/concepts/phase_002/addenda/execution_gate.md` | `docs/canonical/concepts/execution-gate.md` |

The full list lives only in the JSON ledger to avoid inventory drift.

## Stable-ID family migration

| Family | Accepted range | Current topology | Target domain | Group |
|---|---|---|---|---|
| SYN | SYN-001..SYN-035 | distributed under Phase 003 | `docs/canonical/contracts/synchronization/` | CKR-C |
| REF | REF-001..REF-030 | distributed under Phase 004 | `docs/canonical/contracts/evidence-time-causality/` | CKR-D |
| AUTH | AUTH-001..AUTH-053 | distributed under Phase 005 | `docs/canonical/authority/` | CKR-D |
| HLTH | HLTH-001..HLTH-066 | distributed under Phase 006 | `docs/canonical/contracts/health-quality-timing/` | CKR-E |
| OPS | OPS-001..OPS-123 | distributed under Phase 007 | `docs/canonical/contracts/operations/` | CKR-F |
| EXPL | EXPL-001..EXPL-160 | distributed under Phase 008 | `docs/canonical/experience/` | CKR-G |
| INTG | INTG-001..INTG-270 | distributed under Phase 009 | `docs/canonical/contracts/integration/` | CKR-H |
| ARCH | ARCH-001..ARCH-500 | distributed under Phase 010 | `docs/canonical/architecture/` | CKR-I |

CKR-J later converts stable-ID resolution from occurrence discovery plus human ownership resolution into deterministic canonical-owner lookup for records that have completed cutover.

## Design-history roots

The following remain physically in place during the migration:

- `docs/concepts/phase_002/` through `phase_010/`;
- `docs/decisions/`;
- phase scenario/exit/handoff/gap artifacts;
- historical roadmap/open-question/handoff records.

Their current role is mixed because some still own unmigrated current semantics. After each record cuts over, the associated legacy source becomes provenance/history for that record.

## Critical inventory invariant

> **A target path is not authority merely because the inventory names it.**

Until a record reaches `canonicalized`, the inventoried legacy owner remains current authority. This makes the migration progressive without creating an ambiguous authority window.
