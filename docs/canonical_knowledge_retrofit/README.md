# Canonical Knowledge & Documentation Authority Retrofit

**Status:** CKR-A–CKR-C COMPLETE / ACCEPTED — CKR-D IN EXECUTION — IMPLEMENTATION 001-A BLOCKED ON CKR EXIT

**CKR status mirror: COMPLETE CKR-A–CKR-C; IN EXECUTION CKR-D; IMPLEMENTATION 001-A BLOCKED ON CKR EXIT.**

## Purpose

CKR separates current accepted DMTZ meaning from chronological design history. It changes documentation ownership/routing/provenance without silently changing accepted product semantics.

> **A current semantic question resolves to one current owner.**

Ownership is declared in [`canonical_ownership_inventory.json`](canonical_ownership_inventory.json); atomic cutover/no-dual-authority rules are in [`migration_contract.md`](migration_contract.md).

## Program sequence / state

- **CKR-A — Authority Model, Migration Contract & Canonical Ownership Inventory: COMPLETE / ACCEPTED.**
- **CKR-B — Foundation, Terminology & Cross-Cutting Invariants: COMPLETE / ACCEPTED.**
- **CKR-C — Concept Catalog: COMPLETE / ACCEPTED.**
- **CKR-D — Evidence, Time, Authority & Governance: IN EXECUTION.**
- **CKR-E — Health, Quality, Metrics & Timing: PLANNED.**
- **CKR-F — Lineage, Change, Investigation, Impact & Control: PLANNED.**
- **CKR-G — Questioning, Explanation & Experience Contracts: PLANNED.**
- **CKR-H — Integration, Source Authority & Evidence Availability: PLANNED.**
- **CKR-I — Technical Architecture: PLANNED.**
- **CKR-J — OKF, Stable References, Agent Routing & Drift Enforcement: PLANNED.**
- **CKR-K — Consolidation, Provenance Validation & Exit Review: PLANNED.**

## CKR-D execution boundary

CKR-D owns exactly:

1. `reference.authority_vocabulary` → `docs/canonical/authority/vocabulary.md`;
2. REF-001–REF-030 → four bounded resources in `docs/canonical/contracts/evidence-time-causality/`;
3. AUTH-001–AUTH-053 → six bounded resources in `docs/canonical/authority/`.

The candidates currently declare `CANDIDATE / NOT CURRENT AUTHORITY`. Phase 004/005 remain current semantic owners while the inventory state is `candidate_ready`.

CKR-D preserves applicability ≠ coverage ≠ sufficiency; event/effective time ≠ framework knowledge; causal confirmation evidence ≠ confirmation authority; Assertion Authority ≠ Capability Authorization; governed meaning ≠ normative health ≠ realized state; permission/approval ≠ issuance/enforcement/outcome; and current disclosure ≠ historical authorization/communication.

See [`ckr_d_semantic_conservation_matrix.md`](ckr_d_semantic_conservation_matrix.md) and [`ckr_d_execution_review.md`](ckr_d_execution_review.md).

## Prior canonicalized scope

CKR-B canonicalized foundation/glossary resources. CKR-C canonicalized all 24 accepted concepts and SYN-001–SYN-035. Phase 001–003 are provenance for those migrated meanings.

## Scope isolation

HLTH-001–066, OPS-001–123, EXPL-001–160, INTG-001–270 and ARCH-001–500 remain legacy-authoritative until CKR-E–I respectively. CKR-D may reference but cannot absorb those contracts.

## Implementation gate

**Implementation 001-A remains BLOCKED until CKR-K accepts the retrofit.**
