# CKR-J Execution Review — OKF, Stable References, Agent Routing & Drift Enforcement

**Status:** IN EXECUTION — CANDIDATE REVIEW

**Reviewed:** 2026-09-04

## Objective

Finish the CKR routing layer after all semantic families are canonicalized: make current-truth OKF routes canonical-first, make every accepted stable ID deterministically resolve to its canonical owner/section, separate history discovery from default resolution, align shared agent workflows, and fail conformance when those routing guarantees drift.

CKR-J does not change DMTZ concepts, stable-ID meaning, architecture, product behavior, evidence semantics or implementation state.

## Accepted inputs

- CKR authority model and migration contract;
- canonical ownership inventory after CKR-I;
- accepted ADF-B OKF v0.2 producer profile and maintenance policy;
- accepted ADF-E context discovery/stable-reference policies, frozen stable-ID ranges, resolver and knowledge-impact helper;
- ADF-F integrated conformance path;
- CKR-B–I canonical owners and validators.

## Inventory findings

1. All eight stable-ID families are now `canonicalized`; accepted ranges total **1,237 IDs**.
2. `stable_id_registry.json` still describes the pre-CKR-J state in which exact occurrences are candidates and manual authority resolution is required.
3. `resolve_stable_id.py` still searches all `docs/` occurrences by default and only emits a family-level ownership hint.
4. Several stable OKF domain routes retain pre-CKR-I wording that says ARCH remains or is still unmigrated under Phase 010.
5. `knowledge/domains/active-control.md` and `knowledge/domains/serving-security.md` still use Phase 010 Group 07/08 as their primary `resource` despite CKR-I canonicalization.
6. `knowledge_impact.py` reviews only direct frontmatter `resource` links, so secondary canonical body links are structurally checked but not included in changed-resource review candidates.
7. Shared `resolve-context` and `resolve-contract` workflows still describe occurrence discovery + manual canonicality instead of deterministic current-owner resolution.

These are routing/drift defects, not semantic conflicts.

## Candidate design

### Stable references

CKR-J derives exact owner resolution from existing authority rather than adding a duplicated 1,237-row semantic registry:

`stable_id_registry accepted range` + `ownership inventory family target_documents` + `exact canonical definition heading` → `owner_path::STABLE-ID`.

The path is the inventoried canonical owner and the stable ID token is the renderer-neutral section selector. Line numbers and generated Markdown slugs are derived navigation details, not identity.

Default exact-ID resolution returns the canonical owner only. Historical occurrence discovery becomes an explicit secondary mode.

### OKF

The seven domain entries remain compact routing concepts. CKR-J updates them to canonical ARCH routes and removes pre-CKR-I current-owner language. It does not create one concept per stable ID.

### Agent routing

Shared routing will prefer:

`human task → live authority → direct canonical stable locator when ID known; otherwise one bounded OKF route → canonical owner → exact IDs as needed`.

History is loaded only for explicit provenance/rationale/change work or opt-in historical occurrence discovery.

### Drift enforcement

`validate_ckr_j_routing.py` validates:

- all stable families remain canonicalized;
- exact canonical definition coverage remains 1,237/1,237;
- unique owner-heading resolution inside inventoried family target documents;
- the routing manifest remains non-semantic and range-preserving;
- intended OKF canonical route targets exist;
- after cutover, live OKF resources/body routes match the manifest and stale Phase-current language is absent;
- after cutover, stable-ID registry/resolver and agent surfaces expose deterministic canonical routing and separate history mode;
- CKR-J fixtures remain CKRJ-01–48.

`test_ckr_j_routing_guards.py` supplies state-aware adversarial mutations so the controls remain meaningful before and after cutover.

## Candidate state

The candidate manifest is `candidate_ready`; it does not yet switch live OKF resources or the default stable-ID resolver. Current repository authority remains the CKR-I canonical semantic layer; only the routing implementation is under CKR-J review.

## Candidate gate

Pending exact-head Agentic conformance and Documentation consistency. Atomic routing cutover is prohibited until both succeed.

## Exit boundary

CKR-J may advance only routing/discovery/drift enforcement. CKR-K remains planned/unstarted until CKR-J closure passes. Implementation 001-A remains blocked until CKR-K accepts the whole retrofit.
