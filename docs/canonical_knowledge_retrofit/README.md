# Canonical Knowledge & Documentation Authority Retrofit

**Status:** CKR-A–CKR-I COMPLETE / ACCEPTED — CKR-J NEXT / READY — IMPLEMENTATION 001-A BLOCKED ON CKR EXIT

**CKR status mirror: COMPLETE CKR-A–CKR-I; NEXT CKR-J; IMPLEMENTATION 001-A BLOCKED ON CKR EXIT.**

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
- **CKR-I — Technical Architecture: COMPLETE / ACCEPTED.**
- **CKR-J — OKF, Stable References, Agent Routing & Drift Enforcement: NEXT / READY.**
- **CKR-K — Consolidation, Provenance Validation & Exit Review: PLANNED.**

## Current canonical scope through CKR-I

Foundation/glossary, all 24 concepts, SYN-001–SYN-035, authority vocabulary, REF-001–REF-030, AUTH-001–AUTH-053, HLTH-001–HLTH-066, OPS-001–OPS-123, EXPL-001–EXPL-160, INTG-001–INTG-270 and **ARCH-001–ARCH-500** resolve to canonical owners.

The frozen reference architecture resolves to `docs/canonical/architecture/reference-architecture.md`; it composes ARCH-001–ARCH-500 and owns no additional stable-ID range.

ARCH is canonical across eight bounded resources under `docs/canonical/architecture/`, plus the separately inventoried reference architecture. Phase 010 is design history/provenance for these meanings and retains all 500 original atomic ARCH files, group reviews, ADRs, matrices and implementation handoff.

CKR-I preserves deployment-bound capability verification; Delta-first framework history without source-authority transfer; organization-owned identity/scope/authority/authorization; reconciliation-first acquisition with explicit coverage/integration health; exact/partial runtime/version/Lineage/Impact evidence; deterministic-first reasoning/historical replay; Statement/Answer IR before rendering; independent Gate/Safeguard control chains; and authorization-aware serving/security/SLO/cost/resilience boundaries.

See [`ckr_i_semantic_conservation_matrix.md`](ckr_i_semantic_conservation_matrix.md) and [`ckr_i_execution_review.md`](ckr_i_execution_review.md).

## Remaining progression

**CKR-J is next/ready but is not active until explicitly selected by the human.** Completing CKR-I does not authorize CKR-J. CKR-K remains planned.

## Implementation gate

**Implementation 001-A remains BLOCKED until CKR-K accepts the retrofit.**
