# CKR-A Execution Review — Authority Model, Migration Contract & Canonical Ownership Inventory

**Status:** ACCEPTED — CKR-A COMPLETE

**Reviewed:** 2026-09-03

## Objective

Establish the repository authority mechanics required to progressively separate current canonical knowledge from preserved design history before product implementation begins, without changing accepted DMTZ semantics.

## Accepted result

CKR-A establishes three distinct documentation roles:

1. **canonical knowledge** — current semantic authority after explicit record cutover;
2. **design history** — provenance, rationale, scenario/decision history and accepted-at-the-time evolution;
3. **routing/operational guidance** — OKF, agent instructions, skills and indexes that locate authority without becoming it.

The accepted migration states are:

- `legacy_authoritative` — inventoried legacy source remains current;
- `candidate_ready` — candidate exists but is explicitly not current authority;
- `canonicalized` — canonical target is sole current owner and legacy source becomes provenance/history for that record;
- `history_only` — provenance/rationale only.

Cutover is atomic: canonical authority marker, ownership inventory, required routing, provenance and conformance must change together. A partial cutover or two simultaneous current owners is a migration defect.

CKR changes documentation ownership/routing, not accepted SYN/REF/AUTH/HLTH/OPS/EXPL/INTG/ARCH meaning. Genuine semantic contradictions require explicit A4 change control rather than newest-file or search-order inference.

## Ownership inventory

`canonical_ownership_inventory.json` establishes:

- **34 explicit ownership records**;
- **24/24 accepted concepts**, each with an exact legacy current owner and unique future canonical target;
- foundation/reference owner mappings for CKR-B/D;
- all eight accepted stable-ID families with frozen ranges, legacy roots, target canonical domains and migration groups;
- eight Phase 010 architecture segments exactly partitioning **ARCH-001–ARCH-500**;
- the accepted Phase 010 reference-architecture owner;
- logical design-history classifications without bulk-moving the phase corpus.

At CKR-A exit the substantive state is intentionally:

- **0 canonicalized records**;
- **0 candidate-ready records**.

This is the required safe baseline: the destination and authority machinery exist before substantive current truth begins migration.

## Structural namespace / history preservation

`docs/canonical/` now has structural indexes for concepts, contracts, policies, invariants, authority, experience, architecture and reference. These indexes do not independently claim semantic authority.

`docs/design_history/README.md` defines the provenance layer while Phase 002–010, decision, scenario, exit, handoff and gap records remain physically in place. CKR success does not require a high-risk bulk history move.

Historical records are preserved as accepted-at-the-time design evidence rather than rewritten to make final current truth appear contemporaneous with earlier phases.

## Stable-reference treatment

Accepted stable-ID ranges remain unchanged. `stable_id_registry.json` now links to the CKR ownership inventory, and `resolve_stable_id.py` exposes family-level migration state/current root/target root while continuing to treat occurrences as retrieval candidates.

CKR-J remains responsible for deterministic exact canonical owner/anchor resolution after substantive migration.

## Scenario / negative-control evidence

`fixtures/ckr_a_authority_scenarios.yaml` defines **CKRA-01–CKRA-16**, including legacy ownership, candidate non-authority, atomic cutover, dual-authority rejection, historical provenance, stable-ID conservation, contradiction handling, implementation blocking, 24-concept coverage and ARCH range coverage.

Unified fixture validation passes with **138 ADF/addendum/CKR scenarios**.

The conformance guard suite passes **15/15 negative controls**. CKR-specific controls prove rejection of:

1. fabricated `concept.lineage` canonicalization without canonical target evidence;
2. a canonical target outside `docs/canonical/`;
3. stale CKR/implementation-blocking status.

## Integrated validation history

### Initial CKR-A execution state

PR #6 head `94b595d33cfad1ce9af93b99dc85b55ce1d68b1f`:

- **Agentic conformance #49 — SUCCESS**;
- **Documentation consistency #167 — SUCCESS**;
- canonical knowledge: 34 records / 24 concepts / 0 canonicalized / 0 candidates;
- CKR mirror: `IN EXECUTION CKR-A`; Implementation 001-A blocked;
- 138 scenarios;
- 15/15 negative controls;
- 163 governed text files scanned with 0 secret findings;
- 0 stale / 0 deprecated OKF entries;
- expected provider-runtime and future Databricks-materialization warnings only.

### Accepted CKR-A closure state

PR #6 head `693f572ea8db21c1d59dc3208aacd6affcb49e0b`:

- **Agentic conformance #61 — SUCCESS**;
- **Documentation consistency #179 — SUCCESS**;
- canonical knowledge: **34 records / 24 concepts / 0 canonicalized / 0 candidates**;
- CKR status: **`COMPLETE CKR-A; NEXT CKR-B; IMPLEMENTATION 001-A BLOCKED ON CKR EXIT`**;
- fixture catalog: **138 scenarios**;
- negative controls: **15/15**;
- secret scan: **163 governed text files / 0 errors**;
- OKF: **0 errors / 0 warnings / 0 stale / 0 deprecated**;
- 13 registered DMTZ skills/overlays;
- 30 operational stable-ID references checked;
- Cursor/Claude Code/Codex remain runtime-`unverified`, as required by ADF-EX-17;
- local Databricks vendor-skill materialization remains deferred to future 001-A.

Closure-state context budgets improved materially after routing consolidation:

- root `AGENTS.md`: **6,774 / 16,384 bytes**;
- Cursor root baseline: **6,774 / 20,480 bytes**;
- Claude root baseline: **7,828 / 18,432 bytes**;
- Codex root baseline: **6,774 / 16,384 bytes**;
- Cursor rules aggregate: **17,905 / 32,768 bytes**;
- Cursor routing rule: **2,394 / 6,144 bytes**;
- knowledge root index: **1,016 / 4,096 bytes**.

The authority retrofit therefore reduces persistent routing context while adding stronger deterministic ownership controls.

## Acceptance criteria

- canonical knowledge vs design history explicit — **PASS**;
- migration state machine / atomic cutover — **PASS**;
- no-dual-authority invariant — **PASS**;
- structural canonical target without premature authority — **PASS**;
- 24 accepted concepts inventoried — **PASS**;
- stable-ID families inventoried with frozen ranges/current roots/targets — **PASS**;
- ARCH-001–ARCH-500 completely partitioned — **PASS**;
- history preserved — **PASS**;
- Implementation 001-A deterministically blocked — **PASS**;
- unified conformance / negative controls — **PASS**;
- ADF/provider/Databricks residuals preserved — **PASS**;
- context remains bounded — **PASS**.

## Hand-off

CKR-A intentionally does not create substantive canonical semantic resources.

- **CKR-B** — foundation, terminology and cross-cutting invariants;
- **CKR-C** — all 24 concepts and SYN synchronization ownership;
- **CKR-D–I** — REF/AUTH/HLTH/OPS/EXPL/INTG/ARCH canonicalization;
- **CKR-J** — canonical-first OKF/current routing and exact stable-ID owner/anchor resolution;
- **CKR-K** — complete coverage/provenance/current-question validation and implementation unlock.

## Exit decision

**CKR-A — ACCEPTED / COMPLETE.**

No new DMTZ concept, stable ID, semantic rule or architecture requirement was introduced by CKR-A.

**Next eligible group: CKR-B — Foundation, Terminology & Cross-Cutting Invariants.**

Implementation 001-A remains blocked until CKR-K. CKR-B does not begin automatically.
