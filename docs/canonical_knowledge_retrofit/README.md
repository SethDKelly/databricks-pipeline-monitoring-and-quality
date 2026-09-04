# Canonical Knowledge & Documentation Authority Retrofit

**Status:** CKR-A–CKR-G COMPLETE / ACCEPTED — CKR-H IN EXECUTION — IMPLEMENTATION 001-A BLOCKED ON CKR EXIT

**CKR status mirror: COMPLETE CKR-A–CKR-G; IN EXECUTION CKR-H; IMPLEMENTATION 001-A BLOCKED ON CKR EXIT.**

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
- **CKR-H — Integration, Source Authority & Evidence Availability: IN EXECUTION.**
- **CKR-I — Technical Architecture: PLANNED.**
- **CKR-J — OKF, Stable References, Agent Routing & Drift Enforcement: PLANNED.**
- **CKR-K — Consolidation, Provenance Validation & Exit Review: PLANNED.**

## Current canonical scope through CKR-G

Foundation/glossary, all 24 concepts, SYN-001–SYN-035, authority vocabulary, REF-001–REF-030, AUTH-001–AUTH-053, HLTH-001–HLTH-066, OPS-001–OPS-123 and EXPL-001–EXPL-160 resolve to canonical owners.

Phase 001–008 are design history/provenance for migrated meanings.

## CKR-H candidate scope

`stable_family.INTG` is now `candidate_ready`, but **Phase 009 remains the current INTG authority during candidate review**. Eight bounded non-authoritative candidates exist under `docs/canonical/contracts/integration/` for exactly INTG-001–INTG-270:

- integration vocabulary/source capability — INTG-001–022;
- identity/governance/authority sources — INTG-023–050;
- change/deployment/runtime evidence — INTG-051–083;
- health/quality/measurement sources — INTG-084–119;
- Lineage/exposure/Impact sources — INTG-120–153;
- Investigation/causality/control sources — INTG-154–200;
- Explanation/replay/disclosure sources — INTG-201–238;
- consolidated feasibility/retention/cost — INTG-239–270.

Candidate presence does not change authority. The migration preserves available ≠ relevant ≠ eligible ≠ authoritative ≠ sufficient ≠ authorized; source-local identity ≠ ecosystem Entity Identity; timestamp proximity ≠ exact join; positive support ≠ negative coverage; integration failure ≠ product negative; GitHub Actions success ≠ Databricks activation; configured dependency ≠ actual sequence/waiting/consumption; execution success ≠ output/currentness/health; Lineage ≠ encounter ≠ exposure ≠ effect ≠ consequence ≠ cause; localization ≠ Causal Claim; control decision/configuration ≠ enforcement/prevention/recovery; source replay ≠ retained communication; and support/latency/quota/cost ≠ truth/authority.

See [`ckr_h_semantic_conservation_matrix.md`](ckr_h_semantic_conservation_matrix.md) and [`ckr_h_execution_review.md`](ckr_h_execution_review.md).

## Remaining ownership

ARCH-001–500 remains legacy-authoritative under Phase 010 until CKR-I. **CKR-I is not active and CKR-H does not select architecture.**

## Implementation gate

**Implementation 001-A remains BLOCKED until CKR-K accepts the retrofit.**
