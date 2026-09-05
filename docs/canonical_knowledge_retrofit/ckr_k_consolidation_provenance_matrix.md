# CKR-K Consolidation & Provenance Conservation Matrix

**Status:** CANDIDATE — CKR-K IN EXECUTION

## Purpose

CKR-K is the exit review for the Canonical Knowledge Repository retrofit. It does not add or refine DMTZ semantics. It proves that the semantic migrations already accepted in CKR-B–I and the routing layer accepted in CKR-J form one closed, auditable authority system that can safely hand control to Implementation 001-A.

## Exit conservation rules

| Exit surface | Accepted pre-K state | CKR-K exit requirement | Must not become |
|---|---|---|---|
| Current semantic ownership | Inventory-selected canonical owners for foundation, concepts, stable families and architecture | every required record/family/segment remains canonicalized and uniquely owned | dual authority, search-order authority, convenience fallback |
| Stable references | 1,237 accepted IDs resolve deterministically through CKR-J | exact IDs remain range-valid, uniquely canonical and traceable through `owner_path::ID` | duplicated semantic registry, first-match lookup, history/current mixing |
| OKF / agent routing | canonical-first discovery accepted in CKR-J | current-truth routes remain canonical-first and bounded | Phase 001–010 current-owner route, OKF semantic authority |
| Provenance | canonical targets retain bounded historical references | original/current legacy source remains retrievable and canonical targets retain provenance | deletion of history, chronology required for current meaning |
| Design history | Phase corpus logically classified as provenance/rationale/history | remains accessible without competing with canonical current truth | rewritten pseudo-current history or inaccessible rationale |
| Prior CKR evidence | CKR-A–J accepted independently | every prior execution review remains present and accepted | exit acceptance by aggregate assertion alone |
| Implementation gate | 001-A blocked until CKR-K | stays blocked during candidate/exit validation; becomes NEXT/READY only after CKR-K acceptance | implementation work started by CKR-K, silent early release |

## Whole-retrofit invariants

1. A current semantic question resolves to one current owner.
2. `canonicalized` is the only migration state permitted at CKR exit for required current semantic records, stable families and architecture segments.
3. Canonical resources answer current questions locally; design-history reconstruction is optional provenance work, not a prerequisite for current meaning.
4. Canonical resources preserve bounded provenance to the accepted legacy source/history relevant to their promoted meaning.
5. Phase 001–010 remains historically useful and must remain discoverable; preservation of history does not make it a current owner.
6. Accepted stable-ID ranges remain exactly SYN-001–035, REF-001–030, AUTH-001–053, HLTH-001–066, OPS-001–123, EXPL-001–160, INTG-001–270 and ARCH-001–500.
7. The accepted stable-ID total remains 1,237 and all three CKR-I/CKR-J canonical addressability forms remain valid.
8. Known stable IDs may route directly to current canonical owners. Historical occurrence discovery remains explicit and secondary.
9. OKF, stable-reference registry, resolver, indexes and conformance manifests are routing/evidence machinery; none becomes a semantic owner.
10. No living agent/implementation route may describe a migrated phase owner as current authority.
11. CKR acceptance is documentation-authority acceptance, not product-runtime, source-integration, deployment, production-readiness or implementation evidence.
12. ADF-EX-17 / ADF-G-XT01 and DBX-SKILL-RUN-01 remain outside CKR exit because they are deferred runtime/implementation verification, not unresolved semantic ownership.
13. CKR-K may normalize lifecycle/status metadata needed to close the retrofit, but may not alter accepted DMTZ meaning, stable-ID meaning, canonical architecture or product behavior.
14. Implementation 001-A may become NEXT/READY only after CKR-K is complete/accepted and the final exact-head gates pass; NEXT/READY does not mean started.

## Provenance audit dimensions

### Inventory preservation

For every inventoried record, the legacy `current_owner` path remains retrievable and the canonical `target_owner` remains current authority. For every stable family, the historical phase root remains retrievable and the canonical target document set remains explicit. Architecture segment legacy owners remain retrievable while canonical segment owners remain current.

### Canonical provenance locality

Substantive canonical owners must retain an explicit `## Provenance` section. Record-level targets retain the original source identity; stable-family targets retain their historical phase lineage; architecture targets retain Phase 010 provenance. The audit does not require canonical documents to reproduce chronological design history.

### Historical preservation

`docs/design_history/README.md` remains the logical provenance layer. Physical relocation of the phase corpus is not an exit requirement; avoiding link churn is an accepted design choice.

## Representative current-truth locality

CKR-K samples every stable family and each ARCH definition form, plus representative foundation/concept/current-domain resources. A representative current-truth lookup must terminate in `docs/canonical/` without requiring a Phase 001–010 document to determine current meaning. Historical retrieval may be requested separately.

## Dual-authority audit

The exit review rejects:

- a non-canonicalized required inventory record/family/segment;
- a canonical target missing current-authority status;
- a legacy owner claiming `CANONICAL CURRENT AUTHORITY`;
- a live OKF/current agent route that points to a historical phase as the current semantic source;
- current and historical stable-ID search being combined into one owner-selection path;
- an implementation status that releases 001-A while CKR-K is still incomplete.

## Exit metadata normalization

The top-level ownership-inventory lifecycle marker currently reflects the last semantic cutover (`ckr_i_cutover`). CKR-K may change that marker to `ckr_complete` only in the final accepted exit synchronization after all exit checks pass. This is lifecycle metadata, not a semantic ownership transition.

## Non-goals

CKR-K does not create product code, schemas, migrations, tests for product behavior, deployment configuration, source adapters, new stable IDs, new concepts, new architecture decisions, or new semantic contracts. It does not clear ADF runtime residuals or perform Implementation 001-A.
