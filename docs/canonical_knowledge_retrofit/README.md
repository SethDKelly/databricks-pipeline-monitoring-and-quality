# Canonical Knowledge & Documentation Authority Retrofit

**Status:** CKR-A–CKR-F COMPLETE / ACCEPTED — CKR-G IN EXECUTION — IMPLEMENTATION 001-A BLOCKED ON CKR EXIT

**CKR status mirror: COMPLETE CKR-A–CKR-F; IN EXECUTION CKR-G; IMPLEMENTATION 001-A BLOCKED ON CKR EXIT.**

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
- **CKR-G — Questioning, Explanation & Experience Contracts: IN EXECUTION.**
- **CKR-H — Integration, Source Authority & Evidence Availability: PLANNED.**
- **CKR-I — Technical Architecture: PLANNED.**
- **CKR-J — OKF, Stable References, Agent Routing & Drift Enforcement: PLANNED.**
- **CKR-K — Consolidation, Provenance Validation & Exit Review: PLANNED.**

## Current canonical scope through CKR-F

Foundation/glossary, all 24 concepts, SYN-001–SYN-035, authority vocabulary, REF-001–REF-030, AUTH-001–AUTH-053, HLTH-001–HLTH-066 and OPS-001–OPS-123 resolve to canonical owners. Phase 001–007 are design history/provenance for migrated meanings.

## CKR-G execution boundary

CKR-G owns exactly **EXPL-001–EXPL-160** from accepted Phase 008. The candidate topology is eight bounded resources under `docs/canonical/experience/` for question scope/time, answer/basis structure, operational question semantics, inferential/governance question semantics, epistemic language, authorized projection, progressive refresh/retention and historical/comparative Explanation.

All CKR-G targets currently declare `CANDIDATE / NOT CURRENT AUTHORITY`; the ownership inventory marks EXPL `candidate_ready`, so **Phase 008 remains current semantic authority until atomic cutover**.

CKR-G preserves question ≠ truth ≠ authorization; answer statement ≠ independent truth; basis count ≠ confidence; operational shorthand distinctions; Investigation/localization ≠ Causal Claim; candidate/reachable ≠ opportunity ≠ exposure ≠ effect ≠ consequence ≠ causal attribution; Safeguard/Gate separation; unknown/restricted/unavailable/negative distinctions; safe abstraction that cannot strengthen truth; elapsed time ≠ evidence/maturity; retained actual communication ≠ reconstruction; and historical source state ≠ as-known-at-cut Explanation ≠ retained communication ≠ current retrospective Explanation.

See [`ckr_g_semantic_conservation_matrix.md`](ckr_g_semantic_conservation_matrix.md) and [`ckr_g_execution_review.md`](ckr_g_execution_review.md).

## Scope isolation

INTG-001–270 and ARCH-001–500 remain legacy-authoritative until CKR-H/I respectively. CKR-G may reference but cannot absorb them.

## Implementation gate

**Implementation 001-A remains BLOCKED until CKR-K accepts the retrofit.**
