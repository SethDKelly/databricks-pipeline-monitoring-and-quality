# Canonical Knowledge & Documentation Authority Retrofit

**Status:** CKR-A COMPLETE / ACCEPTED — CKR-B NEXT / READY — IMPLEMENTATION 001-A BLOCKED ON CKR EXIT

**CKR status mirror: COMPLETE CKR-A; NEXT CKR-B; IMPLEMENTATION 001-A BLOCKED ON CKR EXIT.**

## Purpose

The Canonical Knowledge & Documentation Authority Retrofit separates **current DMTZ truth** from the chronological records that explain how that truth was designed.

The retrofit does not create a new product/concept/architecture phase and does not alter accepted SYN/REF/AUTH/HLTH/OPS/EXPL/INTG/ARCH semantics by itself. It changes documentation authority, ownership, routing, provenance and maintenance so a current semantic question resolves to one bounded canonical resource rather than requiring reconstruction across design chronology.

The target distinction is:

```text
CANONICAL KNOWLEDGE
Current accepted meaning
Concepts / policies / invariants / authority boundaries /
experience contracts / domain contracts / architecture contracts

        │ provenance / accepted origin
        ▼

DESIGN HISTORY
Phase working records / decisions / scenario reviews / exit reviews /
refinement rationale / superseded wording
```

Design history is retained. It is not deleted merely because its accepted current meaning has been promoted into canonical knowledge.

## Governing rule

> **A user, developer or agent asking what DMTZ means today should resolve through canonical knowledge once that semantic record has been canonicalized. Design history is consulted for provenance, rationale, historical comparison, rejected alternatives or explicit change work—not to reconstruct current meaning.**

During migration, records that have not yet been canonicalized continue to use their explicitly inventoried legacy owners. There is never an accepted state in which two independent resources simultaneously own the same current semantic record.

## Program sequence

1. **CKR-A — Authority Model, Migration Contract & Canonical Ownership Inventory** — define authority layers, migration states, canonical topology, ownership inventory, dual-authority prevention and implementation blocking.
2. **CKR-B — Foundation, Terminology & Cross-Cutting Invariants** — canonicalize product foundation, terminology, methodology boundaries and universal semantic invariants.
3. **CKR-C — Concept Catalog** — canonicalize all 24 accepted concepts as independently understandable current-truth resources.
4. **CKR-D — Evidence, Time, Authority & Governance** — canonicalize REF/AUTH semantics and policies.
5. **CKR-E — Health, Quality, Metrics & Timing** — canonicalize HLTH semantics and cross-concept health boundaries.
6. **CKR-F — Lineage, Change, Investigation, Impact & Control** — canonicalize OPS semantics and related concept synchronizations.
7. **CKR-G — Questioning, Explanation & Experience Contracts** — canonicalize EXPL semantics and current experience contracts.
8. **CKR-H — Integration, Source Authority & Evidence Availability** — canonicalize INTG contracts and source/evidence capability boundaries.
9. **CKR-I — Technical Architecture** — promote accepted ARCH contracts and Phase 010 reference architecture into current canonical architecture resources.
10. **CKR-J — OKF, Stable References, Agent Routing & Drift Enforcement** — make canonical-first retrieval deterministic; update OKF routes and stable-ID ownership resolution; prohibit routine current-truth routing into design history.
11. **CKR-K — Consolidation, Provenance Validation & Exit Review** — prove coverage, semantic conservation, provenance, bounded current-truth lookup and implementation handoff.

The sequence is semantic-domain oriented, not phase-order oriented.

## Current execution state

- **CKR-A — Authority Model, Migration Contract & Canonical Ownership Inventory: COMPLETE / ACCEPTED.**
- **CKR-B — Foundation, Terminology & Cross-Cutting Invariants: NEXT / READY.**
- **CKR-C — Concept Catalog: PLANNED.**
- **CKR-D — Evidence, Time, Authority & Governance: PLANNED.**
- **CKR-E — Health, Quality, Metrics & Timing: PLANNED.**
- **CKR-F — Lineage, Change, Investigation, Impact & Control: PLANNED.**
- **CKR-G — Questioning, Explanation & Experience Contracts: PLANNED.**
- **CKR-H — Integration, Source Authority & Evidence Availability: PLANNED.**
- **CKR-I — Technical Architecture: PLANNED.**
- **CKR-J — OKF, Stable References, Agent Routing & Drift Enforcement: PLANNED.**
- **CKR-K — Consolidation, Provenance Validation & Exit Review: PLANNED.**

CKR-A acceptance evidence is recorded in [`ckr_a_execution_review.md`](ckr_a_execution_review.md).

## Authority while CKR is in progress

The accepted ADF exit remains valid. CKR temporarily blocks product implementation because the repository authority topology is intentionally changing before code/test traceability begins.

For each inventory record:

- `legacy_authoritative` — the inventoried legacy owner remains current authority; the target canonical resource is not yet current truth;
- `candidate_ready` — a canonical candidate may exist for review, but the legacy owner remains current authority until cutover;
- `canonicalized` — the target under `docs/canonical/` is current authority and legacy sources become provenance/design history for that record;
- `history_only` — the resource is provenance/rationale and is not a current semantic owner.

Exact rules are in [`migration_contract.md`](migration_contract.md).

## Canonical target topology

`docs/canonical/` is the future current-truth namespace. CKR-A established its structural indexes and authority validation. Substantive resources become authoritative only through later domain-specific atomic cutover.

Target families:

- `docs/canonical/concepts/`
- `docs/canonical/contracts/`
- `docs/canonical/policies/`
- `docs/canonical/invariants/`
- `docs/canonical/authority/`
- `docs/canonical/experience/`
- `docs/canonical/architecture/`
- `docs/canonical/reference/`

The machine-readable ownership/migration ledger is [`canonical_ownership_inventory.json`](canonical_ownership_inventory.json).

CKR-A accepted a baseline of **34 ownership records, including all 24 concepts, with 0 substantive records canonicalized and 0 candidates**. That is intentional: the authority mechanism exists before the corpus begins migration.

## Design-history treatment

Existing `docs/concepts/phase_002` through `phase_010`, decision records, scenario reviews, exit reviews and relevant foundation/planning records remain in place during the retrofit. [`../design_history/README.md`](../design_history/README.md) defines their logical provenance role without requiring a high-risk bulk filesystem move.

Physical relocation of historical files is not required for CKR success. Authority separation matters more than cosmetic path normalization.

## Semantic-conservation rule

CKR is a documentation-authority migration, not permission to revise accepted behavior.

- canonicalization must preserve accepted semantic distinctions and stable-ID meaning;
- omitted meaning is a migration defect, not simplification;
- contradictory legacy sources must be surfaced and adjudicated under existing authority/change control;
- implementation convenience is not a reason to reinterpret a contract;
- no CKR document may manufacture a new concept, contract, stable ID, architecture requirement or authority boundary without explicit A4 change control.

## Implementation gate

**Implementation 001-A is BLOCKED until CKR-K accepts the retrofit.**

The ADF exit remains accepted and its residuals remain open:

- `ADF-G-XT01` — provider runtime verification debt;
- `DBX-SKILL-RUN-01` — still an Implementation 001-A environment obligation once implementation is unlocked.

CKR does not convert either residual into PASS or move them into the documentation migration.

## Next eligible group

### CKR-B — Foundation, Terminology & Cross-Cutting Invariants

CKR-B will perform the first substantive canonical cutovers. Its scope is to consolidate the durable current meaning from the inventoried foundation/reference owners into bounded canonical resources while separating historical roadmap/open-question/handoff material from current truth.

CKR-B should canonicalize, at minimum, the inventoried product definition, actors/stakeholders, terminology, Concept Design method, architectural principles, security/governance foundation, ecosystem lifecycles, MVP boundary and glossary-related foundation meaning, with semantic-conservation/provenance review before each atomic cutover.

Completion of CKR-A does **not** authorize starting CKR-B automatically. CKR-B begins only when explicitly selected by the human.
