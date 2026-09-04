# Canonical Knowledge & Documentation Authority Retrofit

**Status:** CKR-A COMPLETE / ACCEPTED — CKR-B IN EXECUTION — IMPLEMENTATION 001-A BLOCKED ON CKR EXIT

**CKR status mirror: COMPLETE CKR-A; IN EXECUTION CKR-B; IMPLEMENTATION 001-A BLOCKED ON CKR EXIT.**

## Purpose

The Canonical Knowledge & Documentation Authority Retrofit separates **current DMTZ truth** from the chronological records that explain how that truth was designed.

CKR changes documentation ownership, routing, provenance, and maintenance. It does not create a new product/concept/architecture phase or authorize silent changes to accepted SYN/REF/AUTH/HLTH/OPS/EXPL/INTG/ARCH semantics.

```text
CANONICAL KNOWLEDGE
Current accepted meaning
concepts / contracts / policies / invariants / authority /
experience / architecture / reference

        │ bounded provenance
        ▼

DESIGN HISTORY
phase records / decisions / scenarios / exits /
refinement rationale / superseded wording
```

## Governing rule

> **A current semantic question resolves to one current owner. Once a record is canonicalized, design history explains origin/rationale; it is not required to reconstruct current meaning.**

Current ownership is declared in [`canonical_ownership_inventory.json`](canonical_ownership_inventory.json):

- `legacy_authoritative` — inventoried legacy owner is current authority;
- `candidate_ready` — canonical candidate exists for review, but legacy owner remains current authority;
- `canonicalized` — inventoried `docs/canonical/` target is sole current owner;
- `history_only` — provenance/rationale only.

See [`migration_contract.md`](migration_contract.md) for atomic cutover and no-dual-authority rules.

## Program sequence

1. **CKR-A — Authority Model, Migration Contract & Canonical Ownership Inventory**
2. **CKR-B — Foundation, Terminology & Cross-Cutting Invariants**
3. **CKR-C — Concept Catalog**
4. **CKR-D — Evidence, Time, Authority & Governance**
5. **CKR-E — Health, Quality, Metrics & Timing**
6. **CKR-F — Lineage, Change, Investigation, Impact & Control**
7. **CKR-G — Questioning, Explanation & Experience Contracts**
8. **CKR-H — Integration, Source Authority & Evidence Availability**
9. **CKR-I — Technical Architecture**
10. **CKR-J — OKF, Stable References, Agent Routing & Drift Enforcement**
11. **CKR-K — Consolidation, Provenance Validation & Exit Review**

## Current execution state

- **CKR-A — Authority Model, Migration Contract & Canonical Ownership Inventory: COMPLETE / ACCEPTED.**
- **CKR-B — Foundation, Terminology & Cross-Cutting Invariants: IN EXECUTION.**
- **CKR-C — Concept Catalog: PLANNED.**
- **CKR-D — Evidence, Time, Authority & Governance: PLANNED.**
- **CKR-E — Health, Quality, Metrics & Timing: PLANNED.**
- **CKR-F — Lineage, Change, Investigation, Impact & Control: PLANNED.**
- **CKR-G — Questioning, Explanation & Experience Contracts: PLANNED.**
- **CKR-H — Integration, Source Authority & Evidence Availability: PLANNED.**
- **CKR-I — Technical Architecture: PLANNED.**
- **CKR-J — OKF, Stable References, Agent Routing & Drift Enforcement: PLANNED.**
- **CKR-K — Consolidation, Provenance Validation & Exit Review: PLANNED.**

CKR-A evidence: [`ckr_a_execution_review.md`](ckr_a_execution_review.md).

## CKR-B execution

CKR-B is the first substantive migration group. It owns **nine inventoried records**:

1. `foundation.product_definition`;
2. `foundation.actors_stakeholders`;
3. `foundation.terminology`;
4. `foundation.concept_design_method`;
5. `foundation.architectural_principles`;
6. `foundation.security_governance_policy`;
7. `foundation.ecosystem_lifecycles`;
8. `foundation.mvp_boundary`;
9. `reference.glossary`.

Current candidate targets are under:

- `docs/canonical/reference/`;
- `docs/canonical/invariants/`;
- `docs/canonical/policies/`.

While their inventory state is `candidate_ready`, the original foundation/glossary owners remain current authority. Candidate review must prove semantic conservation before one atomic cutover changes all nine to `canonicalized`.

### CKR-B migration discipline

CKR-B promotes durable current meaning and intentionally leaves behind:

- Phase 001 roadmap sequencing;
- historical open questions already answered or superseded by later accepted phases;
- handoff/progression language;
- obsolete statements that a later phase still needs to decide semantics that are now accepted;
- implementation speculation superseded by Phase 010 / the implementation program.

That excluded material remains design history rather than being erased.

CKR-B must preserve at minimum:

- the product purpose/outcome and non-goals;
- actor goals and non-collapse of technical/business/security/authority roles;
- foundational vocabulary/non-equivalences;
- Concept Design independence/synchronization/change discipline;
- **AP-01–AP-32**;
- **SP-01–SP-15**;
- the 14 durable ecosystem lifecycles and non-rewriting/bitemporal history principle;
- MVP capabilities and **Scenarios A–K**, aligned with the final passive-monitoring-first Phase 010 handoff;
- shared glossary vocabulary updated to current accepted terminology without claiming detailed ownership of later CKR domains.

Semantic comparison is recorded in [`ckr_b_semantic_conservation_matrix.md`](ckr_b_semantic_conservation_matrix.md).

## Canonical target topology

`docs/canonical/` contains the future/current-truth namespace:

- `concepts/`
- `contracts/`
- `policies/`
- `invariants/`
- `authority/`
- `experience/`
- `architecture/`
- `reference/`

A path under `docs/canonical/` is not sufficient for authority; inventory state plus the target authority marker controls cutover.

## Design-history treatment

Existing `docs/foundation/`, `docs/concepts/phase_002`–`phase_010`, decisions, scenario/exit records, and handoffs remain available as provenance. Physical relocation is not required. After cutover, a small banner/index update may point to the canonical owner while preserving accepted-at-the-time narrative.

## Semantic-conservation rule

CKR migration may improve locality, wording, and progressive disclosure, but may not silently alter accepted behavior.

- omitted accepted meaning is a migration defect;
- newest-file/first-search-hit precedence is prohibited;
- genuine contradiction requires explicit A4 change control;
- stable identifiers/accepted concept boundaries survive path migration;
- canonical resources should cross-reference rather than restate other semantic owners in full.

## Implementation gate

**Implementation 001-A remains BLOCKED until CKR-K accepts the retrofit.**

The accepted ADF exit remains valid. `ADF-G-XT01` remains provider-runtime verification debt, and `DBX-SKILL-RUN-01` remains a future Implementation 001-A obligation after CKR unlocks implementation.

Completion of CKR-B will not authorize CKR-C automatically; the next group must still be explicitly selected by the human.
