# Canonical Knowledge & Documentation Authority Retrofit

**Status:** CKR-A–CKR-D COMPLETE / ACCEPTED — CKR-E IN EXECUTION — IMPLEMENTATION 001-A BLOCKED ON CKR EXIT

**CKR status mirror: COMPLETE CKR-A–CKR-D; IN EXECUTION CKR-E; IMPLEMENTATION 001-A BLOCKED ON CKR EXIT.**

## Purpose

CKR separates current accepted DMTZ meaning from chronological design history. It changes documentation ownership/routing/provenance without silently changing accepted product semantics.

> **A current semantic question resolves to one current owner.**

Ownership is declared in [`canonical_ownership_inventory.json`](canonical_ownership_inventory.json); atomic cutover/no-dual-authority rules are in [`migration_contract.md`](migration_contract.md).

## Program sequence / state

- **CKR-A — Authority Model, Migration Contract & Canonical Ownership Inventory: COMPLETE / ACCEPTED.**
- **CKR-B — Foundation, Terminology & Cross-Cutting Invariants: COMPLETE / ACCEPTED.**
- **CKR-C — Concept Catalog: COMPLETE / ACCEPTED.**
- **CKR-D — Evidence, Time, Authority & Governance: COMPLETE / ACCEPTED.**
- **CKR-E — Health, Quality, Metrics & Timing: IN EXECUTION.**
- **CKR-F — Lineage, Change, Investigation, Impact & Control: PLANNED.**
- **CKR-G — Questioning, Explanation & Experience Contracts: PLANNED.**
- **CKR-H — Integration, Source Authority & Evidence Availability: PLANNED.**
- **CKR-I — Technical Architecture: PLANNED.**
- **CKR-J — OKF, Stable References, Agent Routing & Drift Enforcement: PLANNED.**
- **CKR-K — Consolidation, Provenance Validation & Exit Review: PLANNED.**

## Current canonical scope through CKR-E cutover

Foundation/glossary, all 24 concepts, SYN-001–SYN-035, authority vocabulary, REF-001–REF-030, AUTH-001–AUTH-053 and **HLTH-001–HLTH-066** now resolve to canonical owners.

HLTH is canonical across six resources under `docs/canonical/contracts/health-quality-timing/`: measurement/applicability, structural compatibility, Baseline/comparability, normative Assessment, transformation reconciliation, and composite health/readiness/timing. Phase 006 is now design history/provenance for those meanings.

CKR-E preserves metric definition ≠ Observation ≠ Assessment; applicability ≠ selection ≠ computability ≠ availability ≠ outcome; declared schema meaning ≠ structural Expectation ≠ planned ≠ realized ≠ compatibility; Baseline typicality ≠ normative acceptability; criterion result ≠ warning/severity/waiver; Lineage ≠ metric/status propagation; component Assessment ≠ composite health; evaluation time ≠ evidence freshness; and eligible ≠ suitable ≠ ready ≠ control authorization ≠ Gate decision ≠ enforcement ≠ execution.

See [`ckr_e_semantic_conservation_matrix.md`](ckr_e_semantic_conservation_matrix.md) and [`ckr_e_execution_review.md`](ckr_e_execution_review.md). CKR-E remains in execution until the post-cutover/closure validation gate succeeds.

## Remaining ownership

OPS-001–123, EXPL-001–160, INTG-001–270 and ARCH-001–500 remain legacy-authoritative until CKR-F–I respectively.

## Implementation gate

**Implementation 001-A remains BLOCKED until CKR-K accepts the retrofit.**
