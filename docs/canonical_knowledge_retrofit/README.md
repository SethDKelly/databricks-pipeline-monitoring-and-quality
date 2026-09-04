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

## Current canonical scope through CKR-D

Foundation/glossary, all 24 concepts, SYN-001–SYN-035, the shared authority vocabulary, REF-001–REF-030 and AUTH-001–AUTH-053 are canonicalized. Phase 001–005 sources remain design history/provenance for migrated meanings.

## CKR-E execution boundary

CKR-E owns exactly **HLTH-001–HLTH-066** from accepted Phase 006. The candidate topology is six bounded resources under `docs/canonical/contracts/health-quality-timing/` for measurement/applicability, structural compatibility, Baseline/comparability, normative Assessment, transformation reconciliation, and composite health/readiness/timing.

All CKR-E targets currently declare `CANDIDATE / NOT CURRENT AUTHORITY`; the ownership inventory marks HLTH `candidate_ready`, so **Phase 006 remains current semantic authority until atomic cutover**.

CKR-E preserves metric definition ≠ Observation ≠ Assessment; applicability ≠ selection ≠ computability ≠ availability ≠ outcome; declared schema meaning ≠ structural Expectation ≠ planned ≠ realized ≠ compatibility; Baseline typicality ≠ normative acceptability; criterion result ≠ warning/severity/waiver; Lineage ≠ metric/status propagation; component Assessment ≠ composite health; evaluation time ≠ evidence freshness; and eligible ≠ suitable ≠ ready ≠ control authorization ≠ Gate decision ≠ enforcement ≠ execution.

See [`ckr_e_semantic_conservation_matrix.md`](ckr_e_semantic_conservation_matrix.md) and [`ckr_e_execution_review.md`](ckr_e_execution_review.md).

## Scope isolation

OPS-001–123, EXPL-001–160, INTG-001–270 and ARCH-001–500 remain legacy-authoritative until CKR-F–I respectively. CKR-E may reference but cannot absorb them.

## Implementation gate

**Implementation 001-A remains BLOCKED until CKR-K accepts the retrofit.**
