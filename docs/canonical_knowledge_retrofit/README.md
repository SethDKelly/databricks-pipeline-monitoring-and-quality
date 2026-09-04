# Canonical Knowledge & Documentation Authority Retrofit

**Status:** CKR-A–CKR-B COMPLETE / ACCEPTED — CKR-C NEXT / READY — IMPLEMENTATION 001-A BLOCKED ON CKR EXIT

**CKR status mirror: COMPLETE CKR-A–CKR-B; NEXT CKR-C; IMPLEMENTATION 001-A BLOCKED ON CKR EXIT.**

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
- **CKR-B — Foundation, Terminology & Cross-Cutting Invariants: COMPLETE / ACCEPTED.**
- **CKR-C — Concept Catalog: NEXT / READY.**
- **CKR-D — Evidence, Time, Authority & Governance: PLANNED.**
- **CKR-E — Health, Quality, Metrics & Timing: PLANNED.**
- **CKR-F — Lineage, Change, Investigation, Impact & Control: PLANNED.**
- **CKR-G — Questioning, Explanation & Experience Contracts: PLANNED.**
- **CKR-H — Integration, Source Authority & Evidence Availability: PLANNED.**
- **CKR-I — Technical Architecture: PLANNED.**
- **CKR-J — OKF, Stable References, Agent Routing & Drift Enforcement: PLANNED.**
- **CKR-K — Consolidation, Provenance Validation & Exit Review: PLANNED.**

CKR-A evidence is in [`ckr_a_execution_review.md`](ckr_a_execution_review.md). CKR-B evidence is in [`ckr_b_execution_review.md`](ckr_b_execution_review.md).

## Canonicalized in CKR-B

CKR-B established the first substantive canonical current-truth layer for nine records:

1. product definition → `docs/canonical/reference/product-definition.md`;
2. actors/stakeholders → `docs/canonical/reference/actors-and-stakeholders.md`;
3. foundational terminology → `docs/canonical/reference/terminology.md`;
4. Concept Design method → `docs/canonical/reference/concept-design-method.md`;
5. AP-01–AP-32 → `docs/canonical/invariants/architectural-principles.md`;
6. SP-01–SP-15/security-governance → `docs/canonical/policies/security-governance.md`;
7. ecosystem lifecycles → `docs/canonical/reference/ecosystem-lifecycles.md`;
8. MVP boundary → `docs/canonical/policies/mvp-boundary.md`;
9. shared glossary → `docs/canonical/reference/glossary.md`.

Their former Phase-001/glossary owners are provenance/design history for these records. CKR-B intentionally leaves the 24 concept definitions and all stable-ID families with their later-group current owners.

## Semantic-conservation disposition

CKR-B preserved product purpose/non-goals, actor authority separations, foundational non-equivalences, Concept Design discipline, **AP-01–AP-32**, **SP-01–SP-15**, fourteen lifecycle families/non-rewriting history, thirteen MVP capability areas, **Scenarios A–K**, and the shared current vocabulary.

Phase-001 roadmap/open-question/handoff material remains historical. No A4 semantic contradiction was required to complete CKR-B.

## Next eligible group

### CKR-C — Concept Catalog

CKR-C owns canonicalization of the **24 accepted concepts** plus their SYN-001–SYN-035 synchronization ownership. Those records remain `legacy_authoritative` until CKR-C explicitly begins and follows the same candidate-review → atomic-cutover → closure-validation discipline.

Completion of CKR-B does **not** automatically start CKR-C.

## Implementation gate

**Implementation 001-A remains BLOCKED until CKR-K accepts the retrofit.**

The accepted ADF exit remains valid. `ADF-G-XT01` remains provider-runtime verification debt; `DBX-SKILL-RUN-01` remains a future Implementation 001-A obligation after CKR unlock.
