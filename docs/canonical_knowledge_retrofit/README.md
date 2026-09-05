# Canonical Knowledge & Documentation Authority Retrofit

**Status:** CKR-A–CKR-I COMPLETE / ACCEPTED — CKR-J IN EXECUTION / ROUTING CUTOVER VALIDATION — IMPLEMENTATION 001-A BLOCKED ON CKR EXIT

**CKR status mirror: COMPLETE CKR-A–CKR-I; IN EXECUTION CKR-J; IMPLEMENTATION 001-A BLOCKED ON CKR EXIT.**

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
- **CKR-J — OKF, Stable References, Agent Routing & Drift Enforcement: IN EXECUTION.**
- **CKR-K — Consolidation, Provenance Validation & Exit Review: PLANNED.**

## Current canonical semantic scope

Foundation/glossary, all 24 concepts, SYN-001–SYN-035, authority vocabulary, REF-001–REF-030, AUTH-001–AUTH-053, HLTH-001–HLTH-066, OPS-001–OPS-123, EXPL-001–EXPL-160, INTG-001–INTG-270 and ARCH-001–ARCH-500 resolve to canonical owners. Phase 001–010 remains design history/provenance for migrated meanings.

## CKR-J routing cutover

The CKR-J routing manifest is active and the live routing layer is under exact-head cutover validation:

- all seven stable semantic OKF domain routes are canonical-first;
- exact accepted stable IDs resolve deterministically through `scripts/agentic/resolve_stable_id.py <ID>`;
- the stable locator is `owner_path::STABLE-ID`;
- canonical stable-definition coverage is 1,237/1,237 using the accepted forms conserved from CKR-B–I: 737 definition headings, 416 ARCH stable-ID index members and 84 ARCH stable-contract list members;
- `--history` performs separate provenance occurrence discovery and never competes with the current canonical owner;
- shared agent workflows use direct exact-ID lookup when the ID is known and one bounded OKF route only when semantic location is unknown;
- routing drift is guarded by CKR-J validation and state-aware negative controls.

The registry, resolver, OKF bundle and routing manifest remain derived routing machinery and do not own or reinterpret DMTZ semantics.

See [`ckr_j_routing_conservation_matrix.md`](ckr_j_routing_conservation_matrix.md) and [`ckr_j_execution_review.md`](ckr_j_execution_review.md).

## Remaining progression

CKR-J cannot close until the activated routing cutover, closure synchronization and final exact-head evidence gates pass. **CKR-K remains planned/unstarted.**

## Implementation gate

**Implementation 001-A remains BLOCKED until CKR-K accepts the retrofit.**
