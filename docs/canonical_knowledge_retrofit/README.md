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

## Current canonical scope through CKR-F cutover

Foundation/glossary, all 24 concepts, SYN-001–SYN-035, authority vocabulary, REF-001–REF-030, AUTH-001–AUTH-053, HLTH-001–HLTH-066 and **OPS-001–OPS-123** now resolve to canonical owners.

OPS is canonical across eight resources under `docs/canonical/contracts/operations/`: Lineage/topology, Change realization, prospective review, execution reconstruction, Investigation/causality, Impact/exposure, Propagation Safeguard and Execution Gate/control. Phase 007 is design history/provenance for those meanings.

CKR-F preserves Lineage/reachability ≠ exposure/Impact/cause; Change Intent ≠ Deployment ≠ Change; candidate ≠ exposure ≠ effect ≠ consequence ≠ cause; expected work/opportunity/Gate state ≠ execution; localization ≠ cause; `confirmed` remains REF-017 + AUTH-034 gated; Safeguard request/configuration ≠ enforcement ≠ prevented exposure ≠ recovery; health/suitability ≠ readiness ≠ Gate decision ≠ enforcement ≠ execution; Gate ≠ Safeguard; and actual retained history ≠ as-known-at-cut reconstruction ≠ current retrospective interpretation.

See [`ckr_f_semantic_conservation_matrix.md`](ckr_f_semantic_conservation_matrix.md) and [`ckr_f_execution_review.md`](ckr_f_execution_review.md). CKR-F remains in execution until post-cutover/closure validation succeeds.

## Remaining ownership

EXPL-001–160, INTG-001–270 and ARCH-001–500 remain legacy-authoritative until CKR-G–I respectively.

## Implementation gate

**Implementation 001-A remains BLOCKED until CKR-K accepts the retrofit.**
