# CKR-D Execution Review — Evidence, Time, Authority & Governance

**Status:** ACCEPTED — CKR-D COMPLETE

**Reviewed:** 2026-09-03

## Objective

Canonicalize `reference.authority_vocabulary`, REF-001–REF-030 and AUTH-001–AUTH-053 without weakening evidence burdens, conflating authority with authorization, or importing HLTH/OPS/EXPL/INTG/ARCH ownership.

## Accepted result

CKR-D canonicalized exactly:

- shared authority vocabulary → `docs/canonical/authority/vocabulary.md`;
- REF-001–REF-030 → four bounded documents under `docs/canonical/contracts/evidence-time-causality/`;
- AUTH-001–AUTH-053 → six bounded documents under `docs/canonical/authority/`.

Phase 004/005 are now design history/provenance for these migrated meanings. The 24 concepts and SYN remain canonical from CKR-C. HLTH/OPS/EXPL/INTG/ARCH remain with later CKR groups.

## Semantic conservation

The accepted [`ckr_d_semantic_conservation_matrix.md`](ckr_d_semantic_conservation_matrix.md) preserves:

- applicability ≠ coverage ≠ conclusion-specific sufficiency;
- missing/unavailable/restricted telemetry ≠ negative evidence;
- event/effective time ≠ source availability ≠ framework recorded/knowledge time ≠ derived evaluation;
- actual retained historical state ≠ replay-derived reconstruction;
- causal proposed/supported/weakened/unresolved/rejected/confirmed semantics;
- REF-017 confirmation evidence gate + independent AUTH-034 confirmation authority;
- reachability ≠ exposure and bounded evidence burdens for non-exposure;
- readiness ≠ Gate decision ≠ delivery/acceptance ≠ enforcement ≠ execution;
- Safeguard request/configuration ≠ effective enforcement ≠ REF-028 prevented exposure ≠ recovery;
- Assertion Authority ≠ Capability Authorization ≠ Responsibility Assignment ≠ evidence sufficiency ≠ enforcement;
- governed schema meaning ≠ normative schema compatibility ≠ realized schema ≠ Assessment;
- metric meaning/profile/threshold/severity/waiver/control-use eligibility as separate governance layers;
- unknown/conflicting/unavailable authorization ≠ permission;
- requester disclosure permission ≠ framework/service processing permission;
- approval/authorization ≠ issuance ≠ enforcement ≠ domain outcome;
- safe abstraction cannot strengthen truth or hide material epistemic limitations;
- current disclosure ≠ historical authorization ≠ retained historical communication.

No A4 semantic change was required.

## Deterministic protection

`scripts/agentic/validate_ckr_d_evidence_authority.py` requires:

- authority vocabulary + REF + AUTH move atomically;
- exact REF-001–REF-030 coverage once each;
- exact AUTH-001–AUTH-053 coverage once each;
- target topology and authority markers match inventory state;
- Phase 004/005 provenance retention;
- all 24 concepts and SYN remain canonicalized;
- HLTH/OPS/EXPL/INTG/ARCH remain legacy-authoritative during CKR-D;
- core evidence/authority/authorization/disclosure separations remain present.

`fixtures/ckr_d_evidence_authority_scenarios.yaml` adds **CKRD-01–CKRD-40**, bringing unified fixture validation to **230 scenarios**. The conformance guard suite contains **29 negative controls**.

## Validation history

### First candidate gate — stale prior-group progression guard caught

PR #9 candidate head `ac6a2fa045d4c19f53de17fe65fe5cb84d52bc37`:

- Documentation consistency **#242 — SUCCESS**;
- CKR-D semantic validation **PASS** with REF **30/30**, AUTH **53/53**, state `candidate_ready`;
- canonical authority validation **PASS** with 34 ownership records, 24 concepts, 33 canonicalized records, one candidate record, one canonicalized stable family and two candidate stable families;
- fixture catalog **230**;
- negative controls **29/29 PASS**;
- context budgets PASS;
- Agentic conformance **#124 — FAILURE** solely because the CKR-C validator still required every later family to remain `legacy_authoritative` forever, incorrectly rejecting legitimate CKR-D progression of REF/AUTH.

The CKR-C validator was corrected to preserve CKR-C's own 24-concept/SYN atomicity while allowing a later family to progress only under its preassigned CKR group. CKR-D's own validator continues to prohibit HLTH/OPS/EXPL/INTG/ARCH ownership theft.

### Corrected candidate gate

PR #9 head `f9c4e5134fcd8dc107ce8afd4b250901ebedfcbb` passed:

- Agentic conformance **#125 — SUCCESS** (run ID `33839108052`);
- Documentation consistency **#243 — SUCCESS** (run ID `33839108048`);
- REF **30/30**, AUTH **53/53**, state `candidate_ready`;
- **230 scenarios**;
- **29/29 negative controls**;
- all context budgets PASS.

This established a reviewable complete candidate corpus while Phase 004/005 still remained current authority.

### Atomic authority cutover

After candidate validation succeeded, commit `ff00e76e3fdba296c3e1be5ea8eb0f46ee91d538` atomically changed:

1. authority vocabulary inventory state and marker to canonical;
2. REF stable-family state and all four target markers to canonical;
3. AUTH stable-family state and all six target markers to canonical;
4. Phase 004/005 inventory classification to design history/provenance for migrated meaning;
5. live routes to the new canonical current owners.

No concept/SYN or later stable-family ownership changed.

Cutover-state PR #9 passed:

- Agentic conformance **#126 — SUCCESS** (run ID `33839296259`);
- Documentation consistency **#244 — SUCCESS** (run ID `33839296175`);
- CKR-D semantic validation REF **30/30**, AUTH **53/53**, state `canonicalized`;
- all unified conformance layers and negative controls green.

## Acceptance criteria

- exact CKR-D scope — **PASS**;
- REF-001–030 exact coverage — **PASS**;
- AUTH-001–053 exact coverage — **PASS**;
- candidate review before authority change — **PASS**;
- atomic authority vocabulary + REF + AUTH cutover — **PASS**;
- evidence/authority/authorization separation — **PASS**;
- temporal/non-rewriting semantics — **PASS**;
- causal confirmation dual gate preserved — **PASS**;
- exposure/control evidence boundaries preserved — **PASS**;
- governance/normative/disclosure boundaries preserved — **PASS**;
- Phase 004/005 provenance retained — **PASS**;
- later-domain ownership isolation — **PASS**;
- unified conformance / 29 negative controls — **PASS**;
- implementation remains blocked — **PASS**;
- no A4 semantic change — **PASS**.

## Exit decision

**CKR-D — ACCEPTED / COMPLETE.**

No new DMTZ concept, stable-ID family, semantic rule, authority boundary or architecture requirement was introduced by CKR-D.

**Next eligible group: CKR-E — Health, Quality, Metrics & Timing.**

CKR-E remains unstarted until explicitly selected by the human. Implementation 001-A remains blocked until CKR-K.

The final closure head still requires the normal post-status synchronization CI gate; that operational check does not reopen the accepted semantic cutover unless it identifies a real defect.
