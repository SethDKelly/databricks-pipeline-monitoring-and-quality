# Canonical Knowledge & Documentation Authority Retrofit

**Status:** CKR-A–CKR-H COMPLETE / ACCEPTED — CKR-I IN EXECUTION — IMPLEMENTATION 001-A BLOCKED ON CKR EXIT

**CKR status mirror: COMPLETE CKR-A–CKR-H; IN EXECUTION CKR-I; IMPLEMENTATION 001-A BLOCKED ON CKR EXIT.**

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
- **CKR-F — Lineage, Change, Investigation, Impact & Control: COMPLETE / ACCEPTED.**
- **CKR-G — Questioning, Explanation & Experience Contracts: COMPLETE / ACCEPTED.**
- **CKR-H — Integration, Source Authority & Evidence Availability: COMPLETE / ACCEPTED.**
- **CKR-I — Technical Architecture: IN EXECUTION.**
- **CKR-J — OKF, Stable References, Agent Routing & Drift Enforcement: PLANNED.**
- **CKR-K — Consolidation, Provenance Validation & Exit Review: PLANNED.**

## Current canonical scope through CKR-H

Foundation/glossary, all 24 concepts, SYN-001–SYN-035, authority vocabulary, REF-001–REF-030, AUTH-001–AUTH-053, HLTH-001–HLTH-066, OPS-001–OPS-123, EXPL-001–EXPL-160 and INTG-001–INTG-270 resolve to canonical owners.

Phase 001–009 sources are design history/provenance for migrated meanings.

## CKR-I candidate state

ARCH-001–ARCH-500 and the accepted Phase 010 reference architecture are now represented by nine bounded candidates under `docs/canonical/architecture/`:

- eight substantive ARCH segment owners covering ARCH-001–ARCH-500 exactly;
- one separately inventoried frozen reference architecture that composes those segments and creates no ARCH-501.

The candidates deliberately consolidate the 500 tiny historical ARCH files into bounded current-owner resources while retaining all 500 source files exactly once as Phase 010 provenance. See [`ckr_i_semantic_conservation_matrix.md`](ckr_i_semantic_conservation_matrix.md) and [`ckr_i_execution_review.md`](ckr_i_execution_review.md).

**Candidate-ready does not transfer current authority.** Phase 010 remains the current ARCH/reference-architecture owner until an atomic CKR-I cutover passes the normal exact-head repository gates.

CKR-I preserves deployment-bound capability verification; Delta-first canonical evidence history without source-authority transfer; organization-owned identity/scope/authority/authorization; reconciliation-first acquisition with explicit coverage/integration health; exact/partial runtime/version/Lineage/Impact evidence; deterministic-first reasoning and historical replay; Statement/Answer IR before rendering; independent Gate/Safeguard control chains; and authorization-aware serving/security/SLO/cost/resilience boundaries.

## Remaining progression

CKR-J and CKR-K remain planned. **CKR-J is not active and is not authorized by CKR-I execution.**

## Implementation gate

**Implementation 001-A remains BLOCKED until CKR-K accepts the retrofit.**
