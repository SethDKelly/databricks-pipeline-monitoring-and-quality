# Canonical Knowledge & Documentation Authority Retrofit

**Status:** CKR-A–CKR-C COMPLETE / ACCEPTED — CKR-D NEXT / READY — IMPLEMENTATION 001-A BLOCKED ON CKR EXIT

**CKR status mirror: COMPLETE CKR-A–CKR-C; NEXT CKR-D; IMPLEMENTATION 001-A BLOCKED ON CKR EXIT.**

## Purpose

CKR separates current accepted DMTZ meaning from chronological design history. It changes documentation ownership/routing/provenance without silently changing accepted product semantics.

> **A current semantic question resolves to one current owner.**

Ownership is declared in [`canonical_ownership_inventory.json`](canonical_ownership_inventory.json); atomic cutover/no-dual-authority rules are in [`migration_contract.md`](migration_contract.md).

## Program sequence / state

- **CKR-A — Authority Model, Migration Contract & Canonical Ownership Inventory: COMPLETE / ACCEPTED.**
- **CKR-B — Foundation, Terminology & Cross-Cutting Invariants: COMPLETE / ACCEPTED.**
- **CKR-C — Concept Catalog: COMPLETE / ACCEPTED.**
- **CKR-D — Evidence, Time, Authority & Governance: NEXT / READY.**
- **CKR-E — Health, Quality, Metrics & Timing: PLANNED.**
- **CKR-F — Lineage, Change, Investigation, Impact & Control: PLANNED.**
- **CKR-G — Questioning, Explanation & Experience Contracts: PLANNED.**
- **CKR-H — Integration, Source Authority & Evidence Availability: PLANNED.**
- **CKR-I — Technical Architecture: PLANNED.**
- **CKR-J — OKF, Stable References, Agent Routing & Drift Enforcement: PLANNED.**
- **CKR-K — Consolidation, Provenance Validation & Exit Review: PLANNED.**

## Canonicalized in CKR-C

CKR-C atomically canonicalized:

1. all **24 accepted concept records** under `docs/canonical/concepts/`;
2. **SYN-001–SYN-035** across six bounded resources under `docs/canonical/contracts/synchronization/`.

The Phase-002/003 corpus remains provenance/design history for those meanings. `reference.authority_vocabulary` and REF/AUTH/HLTH/OPS/EXPL/INTG/ARCH remain with later groups.

### Conserved boundaries

Expectation ≠ Baseline; Observation ≠ Assessment; Change Intent ≠ Deployment ≠ Change; execution success ≠ output existence ≠ freshness ≠ data health; Lineage/reachability ≠ exposure ≠ Impact ≠ cause; Investigation lead/closure ≠ causal confirmation; Capability Authorization ≠ Assertion Authority ≠ evidence sufficiency ≠ enforcement; Gate readiness ≠ decision ≠ delivery ≠ enforcement ≠ execution; Gate ≠ Safeguard; Explanation/Annotation ≠ independent truth; event/effective time ≠ knowledge/record time.

Detailed evidence: [`ckr_c_semantic_conservation_matrix.md`](ckr_c_semantic_conservation_matrix.md) and [`ckr_c_execution_review.md`](ckr_c_execution_review.md).

## Next eligible group

### CKR-D — Evidence, Time, Authority & Governance

CKR-D owns `reference.authority_vocabulary`, REF-001–REF-030 and AUTH-001–AUTH-053 canonicalization. Those records remain `legacy_authoritative` until CKR-D explicitly begins and follows candidate review → atomic cutover → closure validation.

Completion of CKR-C does **not** automatically start CKR-D.

## Implementation gate

**Implementation 001-A remains BLOCKED until CKR-K accepts the retrofit.**
