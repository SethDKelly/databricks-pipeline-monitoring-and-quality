# Canonical Knowledge & Documentation Authority Retrofit

**Status:** CKR-A–CKR-J COMPLETE / ACCEPTED — CKR-K IN EXECUTION — IMPLEMENTATION 001-A BLOCKED ON CKR EXIT

**CKR status mirror: COMPLETE CKR-A–CKR-J; IN EXECUTION CKR-K; IMPLEMENTATION 001-A BLOCKED ON CKR EXIT.**

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
- **CKR-J — OKF, Stable References, Agent Routing & Drift Enforcement: COMPLETE / ACCEPTED.**
- **CKR-K — Consolidation, Provenance Validation & Exit Review: IN EXECUTION.**

## Current canonical semantic scope

Foundation/glossary, all 24 concepts, SYN-001–SYN-035, authority vocabulary, REF-001–REF-030, AUTH-001–AUTH-053, HLTH-001–HLTH-066, OPS-001–OPS-123, EXPL-001–EXPL-160, INTG-001–INTG-270 and ARCH-001–ARCH-500 resolve to canonical owners. Phase 001–010 remains design history/provenance for migrated meanings.

## Accepted CKR-J routing layer

- all seven stable semantic OKF domain routes are canonical-first;
- exact accepted stable IDs resolve deterministically through `scripts/agentic/resolve_stable_id.py <ID>`;
- the stable locator is `owner_path::STABLE-ID`;
- canonical stable-definition coverage is **1,237/1,237**: 737 definition headings, 416 ARCH stable-ID index members and 84 ARCH stable-contract list members;
- `--history` performs separate provenance occurrence discovery and never competes with the current canonical owner;
- known IDs bypass unnecessary OKF traversal; unknown semantic locations use one bounded OKF route before the canonical owner;
- routing drift is enforced through CKR-J validation, 48 fixtures and 12 state-aware negative controls.

The registry, resolver, OKF bundle and routing manifest are derived routing machinery and do not own or reinterpret DMTZ semantics.

## CKR-K exit review

CKR-K validates whole-retrofit ownership closure, provenance/history preservation, deterministic stable references, canonical-first routing, representative current-truth locality, dual-authority exclusion and the final implementation-gate handoff. It adds no semantic owner and does not perform product implementation.

See [`ckr_k_exit_manifest.json`](ckr_k_exit_manifest.json), [`ckr_k_consolidation_provenance_matrix.md`](ckr_k_consolidation_provenance_matrix.md) and [`ckr_k_execution_review.md`](ckr_k_execution_review.md).

## Implementation gate

**Implementation 001-A remains BLOCKED while CKR-K is in execution.** Only accepted CKR-K exit may move 001-A to NEXT / READY / NOT STARTED.
