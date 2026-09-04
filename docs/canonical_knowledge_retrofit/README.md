# Canonical Knowledge & Documentation Authority Retrofit

**Status:** CKR-A–CKR-G COMPLETE / ACCEPTED — CKR-H IN EXECUTION / CUTOVER VALIDATION — IMPLEMENTATION 001-A BLOCKED ON CKR EXIT

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
- **CKR-H — Integration, Source Authority & Evidence Availability: IN EXECUTION — CUTOVER VALIDATION.**
- **CKR-I — Technical Architecture: PLANNED.**
- **CKR-J — OKF, Stable References, Agent Routing & Drift Enforcement: PLANNED.**
- **CKR-K — Consolidation, Provenance Validation & Exit Review: PLANNED.**

## Current canonical scope through CKR-H cutover

Foundation/glossary, all 24 concepts, SYN-001–SYN-035, authority vocabulary, REF-001–REF-030, AUTH-001–AUTH-053, HLTH-001–HLTH-066, OPS-001–OPS-123, EXPL-001–EXPL-160 and **INTG-001–INTG-270** resolve to canonical owners.

INTG is canonical across eight resources under `docs/canonical/contracts/integration/`: source-capability vocabulary, identity/governance/authority sources, change/deployment/runtime evidence, health/measurement sources, Lineage/exposure/Impact sources, Investigation/causality/control sources, Explanation/replay/disclosure sources, and consolidated feasibility/retention/cost. Phase 009 is design history/provenance for those meanings.

CKR-H preserves available ≠ relevant ≠ eligible ≠ authoritative ≠ sufficient ≠ authorized; source-local identity ≠ ecosystem Entity Identity; timestamp proximity ≠ exact cross-system association; positive support ≠ negative evidence capability; current availability ≠ historical replay; late evidence now ≠ evidence available earlier; common-derived endpoints ≠ independent corroboration; fallback availability ≠ inherited authority; integration failure ≠ product negative; GitHub Actions success ≠ Databricks activation; configured dependency ≠ actual sequence/waiting/version consumption; execution success ≠ output/currentness/health; Lineage ≠ encounter ≠ exposure ≠ effect ≠ consequence ≠ cause; localization ≠ Causal Claim; Safeguard enforcement ≠ prevented exposure; HOLD/ADMIT ≠ execution; source replay ≠ retained communication; and support/latency/quota/cost ≠ truth/authority.

See [`ckr_h_semantic_conservation_matrix.md`](ckr_h_semantic_conservation_matrix.md) and [`ckr_h_execution_review.md`](ckr_h_execution_review.md).

## Remaining ownership

ARCH-001–500 remains legacy-authoritative under Phase 010 until CKR-I. **CKR-I is not active and CKR-H does not select architecture.**

## Implementation gate

**Implementation 001-A remains BLOCKED until CKR-K accepts the retrofit.**
