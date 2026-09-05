# Canonical Knowledge & Documentation Authority Retrofit

**Status:** CKR-A–CKR-I COMPLETE / ACCEPTED — CKR-J IN EXECUTION — IMPLEMENTATION 001-A BLOCKED ON CKR EXIT

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

## Current canonical semantic scope through CKR-I

Foundation/glossary, all 24 concepts, SYN-001–SYN-035, authority vocabulary, REF-001–REF-030, AUTH-001–AUTH-053, HLTH-001–HLTH-066, OPS-001–OPS-123, EXPL-001–EXPL-160, INTG-001–INTG-270 and **ARCH-001–ARCH-500** resolve to canonical owners.

The frozen reference architecture resolves to `docs/canonical/architecture/reference-architecture.md`; it composes ARCH-001–ARCH-500 and owns no additional stable-ID range.

Phase 001–010 sources are design history/provenance for migrated meanings. They remain available for origin, rationale, historical-state and change analysis but are not alternate current owners.

## CKR-J execution boundary

CKR-J is migrating the **routing layer**, not semantic authority. Its candidate work covers:

- canonical-first OKF domain routing after CKR-I;
- deterministic exact stable-ID resolution from the accepted range registry + ownership inventory + unique canonical definition heading;
- renderer-neutral stable locators in the form `owner_path::STABLE-ID`;
- explicit secondary historical-occurrence discovery rather than mixing history into default current resolution;
- shared agent-routing updates for direct exact-ID lookup and bounded progressive disclosure;
- deterministic drift enforcement for stable-reference coverage, OKF routes and agent-routing surfaces.

The candidate manifest is [`ckr_j_routing_manifest.json`](ckr_j_routing_manifest.json). Its `candidate_ready` state does **not** switch live routing by itself. Current semantic meaning remains wholly owned by the already-canonical CKR-B–I resources.

See [`ckr_j_routing_conservation_matrix.md`](ckr_j_routing_conservation_matrix.md) and [`ckr_j_execution_review.md`](ckr_j_execution_review.md).

## Remaining progression

CKR-J must pass candidate validation, atomic routing cutover, closure synchronization and final exact-head validation. **CKR-K remains planned/unstarted until CKR-J is accepted.**

## Implementation gate

**Implementation 001-A remains BLOCKED until CKR-K accepts the retrofit.**
