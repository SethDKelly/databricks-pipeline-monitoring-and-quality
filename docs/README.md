# Documentation Index

The `docs/` tree is the repository system of record for DMTZ semantics, documentation authority, design provenance and implementation planning.

This file is the **sole living authority for completed design-phase progression**. Current semantic lookup is ownership-oriented rather than chronology-oriented.

**CKR state:** CKR-A–CKR-K COMPLETE / ACCEPTED — CKR EXIT ACCEPTED.

**DPTN state:** DPTN-A COMPLETE / ACCEPTED — DPTN-B NEXT / READY / NOT STARTED — IMPLEMENTATION 001-A BLOCKED ON DPTN EXIT.

## Documentation authority architecture

Current semantic ownership is resolved through [`canonical_knowledge_retrofit/canonical_ownership_inventory.json`](canonical_knowledge_retrofit/canonical_ownership_inventory.json). The ownership inventory lifecycle is `ckr_complete`; all required current semantic records/families remain canonicalized and resolve to substantive owners under `docs/canonical/` until later DPTN cutovers.

DPTN-A is complete/accepted. It established future physical topology, collision ordering and the dependency-safe move map but performed no physical relocation. Governing DPTN planning authority: [`documentation_topology_normalization/README.md`](documentation_topology_normalization/README.md), [`documentation_topology_normalization/topology_authority.md`](documentation_topology_normalization/topology_authority.md), and [`documentation_topology_normalization/move_map.json`](documentation_topology_normalization/move_map.json).

Governing CKR rules remain [`canonical_knowledge_retrofit/authority_model.md`](canonical_knowledge_retrofit/authority_model.md), [`canonical_knowledge_retrofit/migration_contract.md`](canonical_knowledge_retrofit/migration_contract.md), and [`design_history/README.md`](design_history/README.md).

> **A current semantic question should resolve to one current owner. Design chronology explains why that rule exists; it should not be required to reconstruct current meaning after canonicalization.**

## Current state

- **Phase 002 — Concept Specifications: COMPLETE with four accepted post-exit addenda.** Current catalog: 24 concepts.
- **Phase 003 — Concept Synchronizations and Ecosystem Scenarios: COMPLETE.** SYN-001–SYN-035 accepted; E-01–E-22 pass.
- **Phase 004 — Evidence, Time, and Causality Refinement: COMPLETE.** REF-001–REF-030 accepted.
- **Phase 005 — Governance, Authority, Semantics, Policy, and Capability Refinement: COMPLETE.** AUTH-001–AUTH-053 final; G07-01–G07-26 pass.
- **Phase 006 — Health, Freshness, Quality, Metrics, and Result-Timing Refinement: COMPLETE.** Groups 01–07 accepted; HLTH-001–HLTH-066 final; H07-01–H07-36 pass.
- **Phase 007 — Lineage, Change, Investigation, Impact, Safeguard, and Execution-Control Refinement: COMPLETE.** Groups 01–09 accepted; OPS-001–OPS-123 final; Phase 007 exit review accepted.
- **Phase 008 — Business Questioning and Explanation: COMPLETE.** Groups 01–08 accepted; EXPL-001–EXPL-160 final; Phase 008 exit review accepted; no EXPL-161 required.
- **Phase 009 — Integration Contracts, Source Authority, and Evidence Availability: COMPLETE.** Groups 01–08 accepted; INTG-001–INTG-270 final; Phase 009 exit review accepted; no INTG-271 required.
- **Phase 010 — Technical Architecture: COMPLETE.** Groups 01–09 accepted; ARCH-001–ARCH-500 final; Phase 010 exit review accepted; no ARCH-501 required.

The catalog contains **24 accepted concepts**. ADF and CKR exits are accepted. **DPTN-A is COMPLETE / ACCEPTED, DPTN-B is NEXT / READY / NOT STARTED, and Implementation 001-A is BLOCKED ON DPTN EXIT.**

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

Current CKR authority and exit evidence: [`canonical_knowledge_retrofit/README.md`](canonical_knowledge_retrofit/README.md) and [`canonical_knowledge_retrofit/ckr_k_execution_review.md`](canonical_knowledge_retrofit/ckr_k_execution_review.md).

## DPTN state

- **DPTN-A — Topology Authority, Inventory & Move Map: COMPLETE / ACCEPTED.**
- **DPTN-B — Historical Namespace Preparation & Collision Removal: NEXT / READY / NOT STARTED.**
- **DPTN-C–G: PLANNED.**
- **Implementation 001-A: BLOCKED ON DPTN EXIT.**

DPTN-A changed no current semantic-owner path. Its accepted move map remains **NO OPERATIONS AUTHORIZED** until the relevant later DPTN group is explicitly selected.

## Current semantic lookup

1. Open a known canonical owner directly; otherwise consult the ownership inventory or one bounded OKF route.
2. For a known stable ID, use `python3 scripts/agentic/resolve_stable_id.py <ID>` to resolve its deterministic canonical locator `owner_path::STABLE-ID`.
3. Use `--history` only for explicit provenance/rationale/history work; historical occurrences never compete with current ownership.
4. Search order, recency, Git history, DPTN future-path plans, OKF summaries, vendor guidance and model/tool memory are not semantic authority.

Current canonical scope remains foundation/glossary, all 24 concepts, SYN-001–035, REF-001–030, AUTH-001–053, HLTH-001–066, OPS-001–123, EXPL-001–160, INTG-001–270 and ARCH-001–500 plus the frozen reference architecture.

Phase 001–010 is design history/provenance/supporting rationale for migrated meanings, not an alternate current semantic owner.

## Documentation authority discipline

- Design-phase completion lines live only in `## Current state` above.
- `docs/phase_status.md` is generated from those lines and must match.
- CKR exit/current semantic authority lives in `canonical_knowledge_retrofit/README.md` and the completed ownership inventory.
- DPTN physical-topology progression lives in `documentation_topology_normalization/README.md`; its move map is execution planning, not semantic authority.
- Implementation progression lives in `implementation/README.md`.
- `canonical_ownership_inventory.json` remains the machine-readable current-owner ledger until later DPTN relocation/cutover.
- Historical records remain preserved; living guidance must not create a second current owner.

DPTN cannot alter accepted semantic distinctions through physical relocation. Genuine contradictions require normal explicit DMTZ change control.
