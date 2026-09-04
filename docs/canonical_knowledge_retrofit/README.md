# Canonical Knowledge & Documentation Authority Retrofit

**Status:** CKR-A COMPLETE / ACCEPTED — CKR-B IN EXECUTION / CUTOVER COMPLETE — IMPLEMENTATION 001-A BLOCKED ON CKR EXIT

**CKR status mirror: COMPLETE CKR-A; IN EXECUTION CKR-B; IMPLEMENTATION 001-A BLOCKED ON CKR EXIT.**

## Purpose

CKR separates **current DMTZ truth** from the chronological records that explain how it was designed. It changes documentation ownership, routing and provenance without silently changing accepted SYN/REF/AUTH/HLTH/OPS/EXPL/INTG/ARCH semantics.

> **A current semantic question resolves to one current owner. Once a record is canonicalized, design history explains origin/rationale rather than reconstructing current meaning.**

Current ownership is declared in [`canonical_ownership_inventory.json`](canonical_ownership_inventory.json):

- `legacy_authoritative` — legacy owner is current;
- `candidate_ready` — candidate exists but legacy owner remains current;
- `canonicalized` — inventoried `docs/canonical/` target is sole current owner;
- `history_only` — provenance/rationale only.

See [`migration_contract.md`](migration_contract.md) for atomic cutover/no-dual-authority rules.

## Program sequence / state

- **CKR-A — Authority Model, Migration Contract & Canonical Ownership Inventory: COMPLETE / ACCEPTED.**
- **CKR-B — Foundation, Terminology & Cross-Cutting Invariants: IN EXECUTION — NINE-RECORD CUTOVER COMPLETE; CLOSURE VALIDATION PENDING.**
- CKR-C — Concept Catalog: PLANNED.
- CKR-D — Evidence, Time, Authority & Governance: PLANNED.
- CKR-E — Health, Quality, Metrics & Timing: PLANNED.
- CKR-F — Lineage, Change, Investigation, Impact & Control: PLANNED.
- CKR-G — Questioning, Explanation & Experience Contracts: PLANNED.
- CKR-H — Integration, Source Authority & Evidence Availability: PLANNED.
- CKR-I — Technical Architecture: PLANNED.
- CKR-J — OKF, Stable References, Agent Routing & Drift Enforcement: PLANNED.
- CKR-K — Consolidation, Provenance Validation & Exit Review: PLANNED.

## CKR-B cutover

The following nine records are now `canonicalized` and their targets declare `CANONICAL CURRENT AUTHORITY`:

1. `foundation.product_definition` → `docs/canonical/reference/product-definition.md`;
2. `foundation.actors_stakeholders` → `docs/canonical/reference/actors-and-stakeholders.md`;
3. `foundation.terminology` → `docs/canonical/reference/terminology.md`;
4. `foundation.concept_design_method` → `docs/canonical/reference/concept-design-method.md`;
5. `foundation.architectural_principles` → `docs/canonical/invariants/architectural-principles.md`;
6. `foundation.security_governance_policy` → `docs/canonical/policies/security-governance.md`;
7. `foundation.ecosystem_lifecycles` → `docs/canonical/reference/ecosystem-lifecycles.md`;
8. `foundation.mvp_boundary` → `docs/canonical/policies/mvp-boundary.md`;
9. `reference.glossary` → `docs/canonical/reference/glossary.md`.

Their legacy foundation/glossary sources are now provenance/design history for these records. `docs/foundation/README.md` and `docs/reference/README.md` route current questions accordingly.

The cutover preserves:

- product purpose/outcome/non-goals;
- actor/authority separation;
- foundational vocabulary/non-equivalences;
- Concept Design independence/synchronization/change discipline;
- **AP-01–AP-32**;
- **SP-01–SP-15**;
- 14 ecosystem lifecycles and non-rewriting/bitemporal history;
- MVP required capabilities and **Scenarios A–K**;
- current shared glossary vocabulary.

Candidate-stage semantic comparison is recorded in [`ckr_b_semantic_conservation_matrix.md`](ckr_b_semantic_conservation_matrix.md). Execution evidence is in [`ckr_b_execution_review.md`](ckr_b_execution_review.md).

## Ownership deliberately not changed by CKR-B

These remain with later groups:

- all 24 accepted concepts and SYN-001–035 → CKR-C;
- `reference.authority_vocabulary`, REF-001–030 and AUTH-001–053 → CKR-D;
- HLTH-001–066 → CKR-E;
- OPS-001–123 → CKR-F;
- EXPL-001–160 → CKR-G;
- INTG-001–270 → CKR-H;
- ARCH-001–500 / reference architecture → CKR-I.

Phase-001 roadmap/open-question/handoff material remains historical rather than being promoted into current truth.

## Semantic-conservation rule

- omitted accepted meaning is a migration defect;
- search order / phase recency cannot establish authority;
- genuine contradiction requires explicit A4 change control;
- stable identifiers and accepted concept boundaries survive path migration;
- canonical resources cross-reference rather than creating competing semantic copies.

## Implementation gate

**Implementation 001-A remains BLOCKED until CKR-K accepts the retrofit.**

The accepted ADF exit remains valid. `ADF-G-XT01` remains provider-runtime verification debt; `DBX-SKILL-RUN-01` remains a future Implementation 001-A obligation after CKR unlock.

CKR-B does not become COMPLETE until cutover-state and final closure CI pass. Completion will not auto-start CKR-C.
