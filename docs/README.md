# Documentation Index

The `docs/` tree is the repository system of record for DMTZ semantics, documentation authority, design provenance and implementation planning.

This file is the **sole living authority for completed design-phase progression**. Current semantic lookup is ownership-oriented rather than chronology-oriented.

## Documentation authority architecture

The **Canonical Knowledge & Documentation Authority Retrofit (CKR)** is active before product implementation.

Current semantic ownership is resolved through [`canonical_knowledge_retrofit/canonical_ownership_inventory.json`](canonical_knowledge_retrofit/canonical_ownership_inventory.json):

- `legacy_authoritative` / `candidate_ready` → inventoried legacy owner remains current;
- `canonicalized` → inventoried target under [`canonical/`](canonical/) is current;
- `history_only` → provenance/rationale only.

Governing rules:

- [`canonical_knowledge_retrofit/authority_model.md`](canonical_knowledge_retrofit/authority_model.md)
- [`canonical_knowledge_retrofit/migration_contract.md`](canonical_knowledge_retrofit/migration_contract.md)
- [`design_history/README.md`](design_history/README.md)

> **A current semantic question should resolve to one current owner. Design chronology explains why that rule exists; it should not be required to reconstruct current meaning after canonicalization.**

OKF/`knowledge/` remains routing only.

## Current state

- **Phase 002 — Concept Specifications: COMPLETE with four accepted post-exit addenda.** Current catalog: 24 concepts.
- **Phase 003 — Concept Synchronizations and Ecosystem Scenarios: COMPLETE.** SYN-001–SYN-035 accepted; E-01–E-22 pass.
- **Phase 004 — Evidence, Time, and Causality Refinement: COMPLETE.** REF-001–REF-030 accepted.
- **Phase 005 — Governance, Authority, Semantics, Policy, and Capability Refinement: COMPLETE.** AUTH-001–AUTH-053 final; G07-01–G07-26 pass.
- **Phase 006 — Health, Freshness, Quality, Metrics, and Result-Timing Refinement: COMPLETE.** Groups 01–07 accepted; HLTH-001–HLTH-066 final; H07-01–H07-36 pass.
- **Phase 007 — Lineage, Change, Investigation, Impact, Safeguard, and Execution-Control Refinement: COMPLETE.** Groups 01–09 accepted; OPS-001–OPS-123 final; L01-01–L01-18, C02-01–C02-24, P03-01–P03-30, X04-01–X04-32, I05-01–I05-34, IM06-01–IM06-36, SG07-01–SG07-36, GT08-01–GT08-36 and HR09-01–HR09-36 pass; Phase 007 exit review accepted.
- **Phase 008 — Business Questioning and Explanation: COMPLETE.** Groups 01–08 accepted; EXPL-001–EXPL-160 final; BQ01-01–BQ01-24, AS02-01–AS02-30, HCE03-01–HCE03-36, ICG04-01–ICG04-48, UNC05-01–UNC05-40, AUD06-01–AUD06-44, PMR07-01–PMR07-44 and HCX08-01–HCX08-48 pass; Phase 008 exit review accepted; no EXPL-161 required.
- **Phase 009 — Integration Contracts, Source Authority, and Evidence Availability: COMPLETE.** Groups 01–08 accepted; INTG-001–INTG-270 final; IC01-01–IC01-40, GOV02-01–GOV02-48, RTE03-01–RTE03-54, HME04-01–HME04-56, LIE05-01–LIE05-60, ICE06-01–ICE06-72, EBR07-01–EBR07-64 and XRC08-01–XRC08-64 pass; Phase 009 exit review accepted; no INTG-271 required.
- **Phase 010 — Technical Architecture: COMPLETE.** Groups 01–09 accepted; ARCH-001–ARCH-500 final; AFE01-01–AFE01-60, EPT02-01–EPT02-72, IAD03-01–IAD03-84, AHI04-01–AHI04-96, RHI05-01–RHI05-108, IRE06-01–IRE06-120, ACS07-01–ACS07-120, SSO08-01–SSO08-120 and ACV09-01–ACV09-120 pass; D-1263–D-1700 accepted; Phase 010 exit review accepted; no ARCH-501 required. **The ADF exit is accepted; CKR is the active pre-implementation documentation-authority retrofit, and Implementation 001-A is blocked until CKR-K exits.**

The catalog contains **24 accepted concepts**.

## CKR state

- **CKR-A — Authority Model, Migration Contract & Canonical Ownership Inventory: COMPLETE / ACCEPTED.**
- **CKR-B — Foundation, Terminology & Cross-Cutting Invariants: NEXT / READY.**
- Implementation 001-A remains blocked until CKR-K.

CKR-A evidence: [`canonical_knowledge_retrofit/ckr_a_execution_review.md`](canonical_knowledge_retrofit/ckr_a_execution_review.md).

## Current semantic lookup

1. Open a known current owner directly.
2. Otherwise consult the ownership inventory.
3. `canonicalized` → use `docs/canonical/` owner.
4. `legacy_authoritative` / `candidate_ready` → use inventoried legacy owner.
5. Use stable IDs to narrow exact rules; search order is not authority.
6. Use design history when provenance/rationale/history is actually requested.

After relevant cutovers:

- `What is Lineage?` → `docs/canonical/concepts/lineage.md`.
- `What does OPS-005 require?` → canonical contract owner/anchor.
- `Why does Lineage not imply Impact?` → canonical rule first, then design history if rationale is needed.

CKR-A established authority mechanics and the structural canonical namespace with **0 substantive records prematurely canonicalized**. CKR-B is the first eligible substantive migration group.

## Canonical knowledge target

[`canonical/README.md`](canonical/README.md) defines target families:

- concepts;
- contracts;
- policies;
- invariants;
- authority;
- experience;
- architecture;
- reference.

A file under `docs/canonical/` is authoritative only when its ownership record has atomically cut over.

## Design history

The chronological corpus remains preserved in place. Use it for provenance/rationale/change review:

- `concepts/phase_002/` through `concepts/phase_010/`;
- [`decisions/README.md`](decisions/README.md);
- scenario reviews, exits, handoffs and gap registers.

Do not rewrite historical records to make the final design appear contemporaneous with earlier phases.

## Foundation / reference during migration

Unmigrated current owners remain listed in the ownership inventory. CKR-B/D will progressively promote their current meaning from `foundation/` and `reference/` into canonical knowledge while leaving historical-only material as provenance.

## Agentic foundation / implementation

- [`agentic_development_foundation/execution_exit_review.md`](agentic_development_foundation/execution_exit_review.md) — accepted ADF exit;
- [`canonical_knowledge_retrofit/README.md`](canonical_knowledge_retrofit/README.md) — live CKR progression;
- [`implementation/README.md`](implementation/README.md) — live implementation block;
- [`implementation/001_executable_foundations_walking_skeleton/README.md`](implementation/001_executable_foundations_walking_skeleton/README.md) — first implementation package after CKR exit.

ADF-EX-17 remains bounded verification debt; CKR does not reopen or waive it.

## Documentation authority discipline

- Design-phase completion lines live only in `## Current state` above.
- `docs/phase_status.md` is generated from those lines and must match.
- CKR progression lives in `canonical_knowledge_retrofit/README.md` and operational mirrors.
- Implementation progression lives in `implementation/README.md`.
- `canonical_ownership_inventory.json` is the machine-readable owner/cutover ledger during CKR.
- Living guidance must not create a second current owner.

## Semantic conservation

CKR must preserve accepted distinctions including concepts/refinements ≠ architecture ≠ implementation; missing evidence ≠ negative truth; Baseline ≠ Expectation; Observation ≠ Assessment; Lineage/reachability ≠ encounter/exposure/Impact/causality; Investigation ≠ causal confirmation; Assertion Authority ≠ Capability Authorization ≠ evidence sufficiency ≠ enforcement; current ≠ historical/as-known state; and agent/model/vendor output ≠ canonical truth or authorization.

Genuine semantic contradictions require explicit change control, not documentation-cleanup preference.
