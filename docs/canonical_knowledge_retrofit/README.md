# Canonical Knowledge & Documentation Authority Retrofit

**Status:** CKR-A–CKR-E COMPLETE / ACCEPTED — CKR-F IN EXECUTION — IMPLEMENTATION 001-A BLOCKED ON CKR EXIT

**CKR status mirror: COMPLETE CKR-A–CKR-E; IN EXECUTION CKR-F; IMPLEMENTATION 001-A BLOCKED ON CKR EXIT.**

## Purpose

CKR separates current accepted DMTZ meaning from chronological design history. It changes documentation ownership/routing/provenance without silently changing accepted product semantics.

> **A current semantic question resolves to one current owner.**

Ownership is declared in [`canonical_ownership_inventory.json`](canonical_ownership_inventory.json); atomic cutover/no-dual-authority rules are in [`migration_contract.md`](migration_contract.md).

## Program sequence / state

- **CKR-A — Authority Model, Migration Contract & Canonical Ownership Inventory: COMPLETE / ACCEPTED.**
- **CKR-B — Foundation, Terminology & Cross-Cutting Invariants: COMPLETE / ACCEPTED.**
- **CKR-C — Concept Catalog: COMPLETE / ACCEPTED.**
- **CKR-D — Evidence, Time, Authority & Governance: COMPLETE / ACCEPTED.**
- **CKR-E — Health, Quality, Metrics & Timing: COMPLETE / ACCEPTED.**
- **CKR-F — Lineage, Change, Investigation, Impact & Control: IN EXECUTION.**
- **CKR-G — Questioning, Explanation & Experience Contracts: PLANNED.**
- **CKR-H — Integration, Source Authority & Evidence Availability: PLANNED.**
- **CKR-I — Technical Architecture: PLANNED.**
- **CKR-J — OKF, Stable References, Agent Routing & Drift Enforcement: PLANNED.**
- **CKR-K — Consolidation, Provenance Validation & Exit Review: PLANNED.**

## Current canonical scope through CKR-E

Foundation/glossary, all 24 concepts, SYN-001–SYN-035, authority vocabulary, REF-001–REF-030, AUTH-001–AUTH-053 and HLTH-001–HLTH-066 resolve to canonical owners. Phase 001–006 sources are design history/provenance for migrated meanings.

## CKR-F execution boundary

CKR-F owns exactly **OPS-001–OPS-123** from accepted Phase 007. The candidate topology is eight bounded resources under `docs/canonical/contracts/operations/` for Lineage/topology, Change realization, prospective review, execution reconstruction, Investigation/causality, Impact/exposure, Propagation Safeguard and Execution Gate/control.

All CKR-F targets currently declare `CANDIDATE / NOT CURRENT AUTHORITY`; the ownership inventory marks OPS `candidate_ready`, so **Phase 007 remains current semantic authority until atomic cutover**.

CKR-F preserves Lineage/reachability ≠ exposure/Impact/cause; Change Intent ≠ Deployment ≠ Change; candidate ≠ exposure ≠ effect ≠ consequence ≠ cause; expected work/opportunity/Gate state ≠ execution; localization ≠ cause; `confirmed` remains REF-017 + AUTH-034 gated; Safeguard request/configuration ≠ enforcement ≠ prevented exposure ≠ recovery; health/suitability ≠ readiness ≠ Gate decision ≠ enforcement ≠ execution; Gate ≠ Safeguard; and actual retained history ≠ as-known-at-cut reconstruction ≠ current retrospective interpretation.

See [`ckr_f_semantic_conservation_matrix.md`](ckr_f_semantic_conservation_matrix.md) and [`ckr_f_execution_review.md`](ckr_f_execution_review.md).

## Scope isolation

EXPL-001–160, INTG-001–270 and ARCH-001–500 remain legacy-authoritative until CKR-G–I respectively. CKR-F may reference but cannot absorb them.

## Implementation gate

**Implementation 001-A remains BLOCKED until CKR-K accepts the retrofit.**
