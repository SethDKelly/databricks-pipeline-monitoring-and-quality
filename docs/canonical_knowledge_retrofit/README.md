# Canonical Knowledge & Documentation Authority Retrofit

**Status:** CKR-A–CKR-B COMPLETE / ACCEPTED — CKR-C IN EXECUTION / CUTOVER COMPLETE / CLOSURE VALIDATION PENDING — IMPLEMENTATION 001-A BLOCKED ON CKR EXIT

**CKR status mirror: COMPLETE CKR-A–CKR-B; IN EXECUTION CKR-C; IMPLEMENTATION 001-A BLOCKED ON CKR EXIT.**

## Purpose

CKR separates current accepted DMTZ meaning from chronological design history. It changes documentation ownership/routing/provenance without silently changing accepted product semantics.

> **A current semantic question resolves to one current owner.**

Ownership is declared in [`canonical_ownership_inventory.json`](canonical_ownership_inventory.json); atomic cutover/no-dual-authority rules are in [`migration_contract.md`](migration_contract.md).

## Program sequence / state

- **CKR-A — Authority Model, Migration Contract & Canonical Ownership Inventory: COMPLETE / ACCEPTED.**
- **CKR-B — Foundation, Terminology & Cross-Cutting Invariants: COMPLETE / ACCEPTED.**
- **CKR-C — Concept Catalog: IN EXECUTION.**
- **CKR-D — Evidence, Time, Authority & Governance: PLANNED.**
- **CKR-E — Health, Quality, Metrics & Timing: PLANNED.**
- **CKR-F — Lineage, Change, Investigation, Impact & Control: PLANNED.**
- **CKR-G — Questioning, Explanation & Experience Contracts: PLANNED.**
- **CKR-H — Integration, Source Authority & Evidence Availability: PLANNED.**
- **CKR-I — Technical Architecture: PLANNED.**
- **CKR-J — OKF, Stable References, Agent Routing & Drift Enforcement: PLANNED.**
- **CKR-K — Consolidation, Provenance Validation & Exit Review: PLANNED.**

## CKR-C authority cutover

CKR-C has atomically cut over:

1. all **24 accepted concept records** to `docs/canonical/concepts/`;
2. **SYN-001–SYN-035** to six bounded resources under `docs/canonical/contracts/synchronization/`.

The Phase-002/003 corpus remains provenance/design history for those meanings. `reference.authority_vocabulary` and REF/AUTH/HLTH/OPS/EXPL/INTG/ARCH remain with later groups.

Cutover is not group closure: CKR-C remains `IN EXECUTION` until the authority-flipped state passes unified conformance and closure status is separately synchronized.

### Conserved boundaries

Expectation ≠ Baseline; Observation ≠ Assessment; Change Intent ≠ Deployment ≠ Change; execution success ≠ output existence ≠ freshness ≠ data health; Lineage/reachability ≠ exposure ≠ Impact ≠ cause; Investigation lead/closure ≠ causal confirmation; Capability Authorization ≠ Assertion Authority ≠ evidence sufficiency ≠ enforcement; Gate readiness ≠ decision ≠ enforcement ≠ execution; Gate ≠ Safeguard; Explanation/Annotation ≠ independent truth; event/effective time ≠ knowledge/record time.

Detailed evidence: [`ckr_c_semantic_conservation_matrix.md`](ckr_c_semantic_conservation_matrix.md) and [`ckr_c_execution_review.md`](ckr_c_execution_review.md).

## Implementation gate

**Implementation 001-A remains BLOCKED until CKR-K accepts the retrofit.**

Completion of CKR-C will not automatically start CKR-D.
