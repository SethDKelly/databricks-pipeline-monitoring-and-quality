# CKR-A Execution Review — Authority Model, Migration Contract & Canonical Ownership Inventory

**Status:** ACCEPTED — CKR-A COMPLETE

**Reviewed:** 2026-09-03

## Objective

Establish the repository authority mechanics required to progressively separate current canonical knowledge from preserved design history before product implementation begins.

## Result

CKR-A establishes the authority layer without performing substantive semantic cutover.

The accepted model now distinguishes:

- **canonical knowledge** — current semantic authority after explicit record cutover;
- **design history** — provenance, rationale, scenario/decision history and accepted-at-the-time evolution;
- **routing/operational guidance** — OKF, agent instructions, skills and implementation indexes that locate authority without becoming it.

The migration contract prevents the presence of a new `docs/canonical/` path from manufacturing authority. Current ownership remains state-driven and record-specific.

## Accepted authority mechanics

### Migration states

- `legacy_authoritative` — inventoried legacy source remains current authority;
- `candidate_ready` — canonical candidate exists for review but is explicitly non-authoritative;
- `canonicalized` — canonical target is sole current authority and legacy source becomes provenance/history for that record;
- `history_only` — provenance/rationale only.

### Atomic cutover

A semantic record cuts over only when canonical authority marker, ownership inventory, required routing, provenance and conformance change together. Partial cutover is a defect.

### No-dual-authority invariant

A legacy owner and canonical target may not simultaneously claim current authority. Search order, file age, OKF summary, phase number or path under `docs/canonical/` does not independently establish ownership.

### Semantic conservation

CKR changes documentation ownership/routing, not accepted DMTZ meaning. SYN/REF/AUTH/HLTH/OPS/EXPL/INTG/ARCH meanings and ranges remain frozen. Genuine semantic contradictions discovered during migration require explicit A4 change control rather than documentation-cleanup inference.

## Ownership inventory evidence

The accepted `canonical_ownership_inventory.json` contains:

- **34 explicit ownership records**;
- **24/24 accepted concepts** with exact legacy current owners and unique target canonical files;
- foundation/reference owner mappings for CKR-B/D;
- all eight accepted stable-ID families with frozen ranges, current legacy roots, future canonical domains and migration groups;
- the eight accepted Phase 010 architecture segments that exactly partition **ARCH-001–ARCH-500**;
- the accepted Phase 010 reference-architecture owner;
- logical design-history source classifications without bulk-moving the phase corpus.

At CKR-A exit the substantive migration state is intentionally:

- **0 canonicalized records**;
- **0 candidate-ready records**.

This is the correct baseline: CKR-A establishes the destination and authority machinery but does not pretend that substantive current truth has already been consolidated.

## Structural canonical namespace

`docs/canonical/` now contains structural indexes for:

- concepts;
- contracts;
- policies;
- invariants;
- authority;
- experience;
- architecture;
- reference.

These indexes explicitly state that authority changes only through the migration ledger and atomic cutover contract.

`docs/design_history/README.md` establishes the logical provenance layer while leaving the existing phase/decision paths intact. Physical historical relocation is not required for CKR success.

## Stable-reference treatment

Accepted stable-ID ranges remain unchanged. The stable-ID registry now references the CKR ownership inventory, and `resolve_stable_id.py` exposes the family-level CKR migration state/current-root/target-root while continuing to treat exact occurrences as retrieval candidates rather than authority.

CKR-J remains responsible for deterministic exact canonical owner/anchor resolution after substantive migration has occurred.

## Routing / implementation treatment

Living repository routing now uses current-owner-first discovery rather than a long chronology-first reading order.

The completed ADF exit remains accepted; CKR does not reopen it. A separate CKR mirror now blocks product implementation:

> `IMPLEMENTATION 001-A BLOCKED ON CKR EXIT`

`ADF-G-XT01` remains open provider-runtime verification debt. `DBX-SKILL-RUN-01` remains a future Implementation 001-A obligation once CKR-K unlocks implementation.

## Scenario evidence

`fixtures/ckr_a_authority_scenarios.yaml` defines **CKRA-01–CKRA-16**, covering:

- legacy authority before migration;
- candidate non-authority;
- atomic cutover;
- dual-authority rejection;
- missing canonical target rejection;
- future canonical-first Lineage lookup;
- preserved historical Lineage rationale;
- history preservation;
- stable-ID meaning preservation;
- contradiction/change-control behavior;
- OKF routing non-authority;
- implementation blocking;
- logical rather than physical history separation;
- 24-concept inventory coverage;
- ARCH-001–500 coverage;
- prohibition on manufacturing semantics through refactor.

Unified fixture validation passed with **138 total ADF/addendum/CKR scenarios**.

## Deterministic conformance evidence

PR #6 initial validation head `94b595d33cfad1ce9af93b99dc85b55ce1d68b1f` produced:

- **Documentation consistency #167 — SUCCESS**;
- **Agentic conformance #49 — SUCCESS**;
- documentation consistency: PASS;
- OKF structure/resources: PASS, 0 errors / 0 warnings;
- tool adapters: PASS, with the expected three provider-runtime-pending warnings;
- 13 registered DMTZ skills/overlays: PASS;
- 30 operational stable-ID references checked: PASS;
- ADF status drift: PASS;
- canonical knowledge authority: **PASS — 34 ownership records, 24 concepts, 0 canonicalized, 0 candidates**;
- CKR status drift: PASS — CKR-A IN EXECUTION and Implementation 001-A blocked;
- fixture catalog: **PASS — 138 scenarios**;
- context budgets: PASS;
- provider compatibility evidence: PASS with Cursor/Claude Code/Codex still runtime-`unverified`;
- Databricks Agent Skills addendum: PASS with expected future local-materialization warning;
- agentic/authority secret scan: **PASS — 163 governed text files scanned, 0 errors**;
- ADF-H governance: PASS with expected provider-runtime warnings;
- negative controls: **PASS — 15/15 defects rejected**;
- OKF deprecated entries: 0;
- OKF stale entries: 0.

Representative context measurements remained comfortably bounded:

- root `AGENTS.md`: **10,280 / 16,384 bytes**;
- Cursor rules aggregate: **19,472 / 32,768 bytes**;
- Cursor routing rule: **3,961 / 6,144 bytes**;
- Claude root baseline: **11,334 / 18,432 bytes**;
- Codex root baseline: **10,280 / 16,384 bytes**;
- knowledge root index: **1,016 / 4,096 bytes**.

The retrofit therefore improved authority routing without reintroducing persistent-context bloat.

## Negative-control evidence

The existing ADF/Databricks controls continue to pass. CKR-A adds and successfully detects:

1. fabricated canonicalization of `concept.lineage` without canonical target evidence;
2. canonical target moved outside `docs/canonical/`;
3. stale CKR implementation-blocking status.

These controls demonstrate that canonical authority cannot be created merely by changing an inventory field, moving a path or forgetting to synchronize implementation gating.

## Acceptance criteria review

- canonical-vs-history authority explicit — **PASS**;
- migration states and atomic cutover/no-dual-authority rule — **PASS**;
- structural canonical target without premature authority — **PASS**;
- all 24 concepts inventoried — **PASS**;
- stable-ID families inventoried with frozen ranges/current roots/target domains/groups — **PASS**;
- ARCH-001–ARCH-500 partitioned completely — **PASS**;
- design history preserved — **PASS**;
- implementation deterministically blocked — **PASS**;
- unified conformance integrated — **PASS**;
- authority negative controls — **PASS**;
- context remains bounded — **PASS**;
- ADF/provider/Databricks residuals preserved — **PASS**.

## Residual work intentionally handed forward

CKR-A does not create substantive canonical semantic resources.

- **CKR-B** owns foundation, terminology and cross-cutting invariant canonicalization.
- **CKR-C** owns all 24 concept canonical resources and SYN synchronization ownership.
- **CKR-D–I** progressively canonicalize the accepted stable-ID semantic domains and architecture.
- **CKR-J** changes OKF/current semantic routing and exact stable-ID resolution to canonical-first behavior after the corpus is migrated.
- **CKR-K** validates complete coverage/provenance/current-question lookup and unlocks Implementation 001-A if accepted.

## Exit decision

**CKR-A — ACCEPTED / COMPLETE.**

No semantic change, new DMTZ concept, new stable ID or architecture requirement was introduced by CKR-A.

**Next eligible group: CKR-B — Foundation, Terminology & Cross-Cutting Invariants.**

Implementation 001-A remains blocked until CKR-K. Completion of CKR-A does not authorize beginning CKR-B automatically.
