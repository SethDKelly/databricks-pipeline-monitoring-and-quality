# Documentation Index

The `docs/` tree is the repository system of record for DMTZ semantics, documentation authority, design provenance and implementation planning.

This file is the **sole living authority for completed design-phase progression**. Current semantic lookup is ownership-oriented rather than chronology-oriented.

**CKR state:** CKR-A–CKR-K COMPLETE / ACCEPTED — CKR EXIT ACCEPTED — IMPLEMENTATION 001-A NEXT / READY / NOT STARTED.

## Documentation authority architecture

Current semantic ownership is resolved through [`canonical_knowledge_retrofit/canonical_ownership_inventory.json`](canonical_knowledge_retrofit/canonical_ownership_inventory.json). The ownership inventory lifecycle is `ckr_complete`; all required current semantic records/families are canonicalized and resolve to substantive owners under `docs/canonical/`.

Governing rules: [`canonical_knowledge_retrofit/authority_model.md`](canonical_knowledge_retrofit/authority_model.md), [`canonical_knowledge_retrofit/migration_contract.md`](canonical_knowledge_retrofit/migration_contract.md), and [`design_history/README.md`](design_history/README.md).

> **A current semantic question should resolve to one current owner. Design chronology explains why that rule exists; it should not be required to reconstruct current meaning after canonicalization.**

## Current state

- **Phase 002 — Concept Specifications: COMPLETE with four accepted post-exit addenda.** Current catalog: 24 concepts.
- **Phase 003 — Concept Synchronizations and Ecosystem Scenarios: COMPLETE.** SYN-001–SYN-035 accepted; E-01–E-22 pass.
- **Phase 004 — Evidence, Time, and Causality Refinement: COMPLETE.** REF-001–REF-030 accepted.
- **Phase 005 — Governance, Authority, Semantics, Policy, and Capability Refinement: COMPLETE.** AUTH-001–AUTH-053 final; G07-01–G07-26 pass.
- **Phase 006 — Health, Freshness, Quality, Metrics, and Result-Timing Refinement: COMPLETE.** Groups 01–07 accepted; HLTH-001–HLTH-066 final; H07-01–H07-36 pass.
- **Phase 007 — Lineage, Change, Investigation, Impact, Safeguard, and Execution-Control Refinement: COMPLETE.** Groups 01–09 accepted; OPS-001–OPS-123 final; L01-01–L01-18, C02-01–C02-24, P03-01–P03-30, X04-01–X04-32, I05-01–I05-34, IM06-01–IM06-36, SG07-01–SG07-36, GT08-01–GT08-36 and HR09-01–HR09-36 pass; Phase 007 exit review accepted.
- **Phase 008 — Business Questioning and Explanation: COMPLETE.** Groups 01–08 accepted; EXPL-001–EXPL-160 final; BQ01-01–BQ01-24, AS02-01–AS02-30, HCE03-01–HCE03-36, ICG04-01–ICG04-48, UNC05-01–UNC05-40, AUD06-01–AUD06-44, PMR07-01–PMR07-44 and HCX08-01–HCX08-48 pass; Phase 008 exit review accepted; no EXPL-161 required.
- **Phase 009 — Integration Contracts, Source Authority, and Evidence Availability: COMPLETE.** Groups 01–08 accepted; INTG-001–INTG-270 final; IC01-01–IC01-40, GOV02-01–GOV02-48, RTE03-01–RTE03-54, HME04-01–HME04-56, LIE05-01–LIE05-60, ICE06-01–ICE06-72, EBR07-01–EBR07-64 and XRC08-01–XRC08-64 pass; Phase 009 exit review accepted; no INTG-271 required.
- **Phase 010 — Technical Architecture: COMPLETE.** Groups 01–09 accepted; ARCH-001–ARCH-500 final; AFE01-01–AFE01-60, EPT02-01–EPT02-72, IAD03-01–IAD03-84, AHI04-01–AHI04-96, RHI05-01–RHI05-108, IRE06-01–IRE06-120, ACS07-01–ACS07-120, SSO08-01–SSO08-120 and ACV09-01–ACV09-120 pass; D-1263–D-1700 accepted; Phase 010 exit review accepted; no ARCH-501 required.

The catalog contains **24 accepted concepts**. ADF and CKR exits are accepted; **Implementation 001-A is NEXT / READY / NOT STARTED** and requires explicit human selection before implementation begins.

## CKR state

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
- **CKR-K — Consolidation, Provenance Validation & Exit Review: COMPLETE / ACCEPTED.**
- **CKR EXIT: ACCEPTED.**
- **Implementation 001-A: NEXT / READY / NOT STARTED.**

Current CKR authority and exit evidence: [`canonical_knowledge_retrofit/README.md`](canonical_knowledge_retrofit/README.md) and [`canonical_knowledge_retrofit/ckr_k_execution_review.md`](canonical_knowledge_retrofit/ckr_k_execution_review.md).

## Current semantic lookup

1. Open a known canonical owner directly; otherwise consult the ownership inventory or one bounded OKF route.
2. For a known stable ID, use `python3 scripts/agentic/resolve_stable_id.py <ID>` to resolve its deterministic canonical locator `owner_path::STABLE-ID`.
3. Use `--history` only for explicit provenance/rationale/history work; historical occurrences never compete with current ownership.
4. Search order, recency, Git history, OKF summaries, vendor guidance and model/tool memory are not semantic authority.

Current canonical scope:

- foundation/glossary and all 24 concept definitions;
- SYN-001–SYN-035;
- authority vocabulary and REF-001–REF-030 / AUTH-001–AUTH-053;
- HLTH-001–HLTH-066;
- OPS-001–OPS-123;
- EXPL-001–EXPL-160;
- INTG-001–INTG-270;
- ARCH-001–ARCH-500 plus the frozen reference architecture.

Phase 001–010 is design history/provenance/supporting rationale for migrated meanings, not an alternate current semantic owner.

## Documentation authority discipline

- Design-phase completion lines live only in `## Current state` above.
- `docs/phase_status.md` is generated from those lines and must match.
- CKR exit/current authority lives in `canonical_knowledge_retrofit/README.md` and the completed ownership inventory.
- Implementation progression lives in `implementation/README.md`.
- `canonical_ownership_inventory.json` is the machine-readable current-owner/cutover ledger.
- Historical records remain preserved; living guidance must not create a second current owner.

CKR semantic migration preserves, among other boundaries, Baseline ≠ Expectation, Observation ≠ Assessment, missing evidence ≠ negative truth, Change Intent ≠ Deployment ≠ Change, Lineage ≠ exposure ≠ Impact ≠ cause, Investigation closure ≠ causal confirmation, Assertion Authority ≠ Capability Authorization, Gate ≠ Safeguard, current ≠ historical/as-known state, and agent/model/vendor output ≠ canonical truth or authorization. Genuine contradictions require explicit change control.
