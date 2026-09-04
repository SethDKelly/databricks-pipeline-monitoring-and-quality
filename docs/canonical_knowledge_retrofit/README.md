# Canonical Knowledge & Documentation Authority Retrofit

**Status:** CKR-A–CKR-B COMPLETE / ACCEPTED — CKR-C IN EXECUTION — IMPLEMENTATION 001-A BLOCKED ON CKR EXIT

**CKR status mirror: COMPLETE CKR-A–CKR-B; IN EXECUTION CKR-C; IMPLEMENTATION 001-A BLOCKED ON CKR EXIT.**

## Purpose

CKR separates current accepted DMTZ meaning from chronological design history. It changes documentation ownership/routing/provenance without silently changing accepted product semantics.

> **A current semantic question resolves to one current owner. Candidate presence is never authority.**

Ownership is declared in [`canonical_ownership_inventory.json`](canonical_ownership_inventory.json): `legacy_authoritative`, `candidate_ready`, `canonicalized`, or `history_only`. Atomic cutover/no-dual-authority rules are in [`migration_contract.md`](migration_contract.md).

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

## CKR-C candidate review

CKR-C owns one atomic migration set:

1. all **24 accepted concepts** from Phase 002/addenda;
2. **SYN-001–SYN-035** synchronization ownership from Phase 003.

All 24 concept records and the SYN family are currently `candidate_ready`. Therefore **Phase 002/003 remain current authority** for concept/SYN questions until the atomic cutover succeeds.

Candidate concept resources live under [`../canonical/concepts/`](../canonical/concepts/). SYN candidates are six bounded contract resources under `docs/canonical/contracts/synchronization/`; every SYN-001–SYN-035 retains an explicit heading/identity.

### Conservation rules

CKR-C must preserve concept independence and the accepted state/action/boundary model. Synchronization coordinates concepts and **does not create a 25th umbrella concept**. In particular it preserves:

- Expectation ≠ Baseline;
- Observation ≠ Assessment;
- Change Intent ≠ Deployment ≠ Change;
- execution success ≠ output existence ≠ freshness ≠ data health;
- Lineage/reachability ≠ encounter/exposure ≠ Impact ≠ cause;
- Investigation lead/localization/closure ≠ Causal Claim status/confirmation;
- Impact candidate ≠ exposure ≠ effect ≠ consequence ≠ causal attribution;
- Capability Authorization ≠ Assertion Authority ≠ evidence sufficiency ≠ enforcement;
- Gate readiness ≠ decision ≠ delivery ≠ enforcement ≠ execution;
- Execution Gate ≠ Propagation Safeguard;
- Safeguard proposal ≠ enforcement ≠ prevention ≠ release ≠ recovery;
- Explanation/Annotation ≠ independent truth;
- event/effective time ≠ knowledge/record time.

Detailed comparison: [`ckr_c_semantic_conservation_matrix.md`](ckr_c_semantic_conservation_matrix.md).

### Explicit exclusions

CKR-C does **not** migrate `reference.authority_vocabulary` or REF/AUTH/HLTH/OPS/EXPL/INTG/ARCH stable families. It does not create product code, reopen accepted architecture, or promote vendor/tool/model output into DMTZ truth.

## Implementation gate

**Implementation 001-A remains BLOCKED until CKR-K accepts the retrofit.**

Completion of CKR-C will not automatically start CKR-D; the next group requires explicit human selection.
