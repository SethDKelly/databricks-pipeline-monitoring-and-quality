# CKR-B Semantic Conservation Matrix

**Status:** CANDIDATE REVIEW — LEGACY OWNERS REMAIN CURRENT AUTHORITY

**Scope:** the nine records assigned to CKR-B in `canonical_ownership_inventory.json`.

## Review rule

CKR-B is successful only if each canonical candidate:

- answers its bounded current question without chronological reconstruction;
- preserves accepted durable meaning from its legacy owner and material later refinements;
- removes only historical progression, obsolete future-phase language, already-resolved open questions, or superseded implementation speculation;
- does not absorb semantic ownership assigned to CKR-C–I;
- retains bounded provenance sufficient to inspect how current wording was derived;
- remains non-authoritative until the atomic cutover is accepted.

Textual identity is not required. **Semantic conservation is required.**

## Record-by-record comparison

| Record | Legacy current owner | Candidate target | Durable meaning preserved | Intentionally left as history / non-owned detail | Review state |
|---|---|---|---|---|---|
| `foundation.product_definition` | `docs/foundation/001_product_definition.md` | `docs/canonical/reference/product-definition.md` | Product purpose; evidence-grounded current/historical/causal/Impact/semantic/policy answer outcome; nine capability families; product stance/non-goals; success characteristics | early-phase framing; implementation-neutral wording that implied architecture had not yet been selected; tool examples not needed to define current product | candidate preserves current product boundary |
| `foundation.actors_stakeholders` | `docs/foundation/002_actors_and_stakeholders.md` | `docs/canonical/reference/actors-and-stakeholders.md` | Eight human actor roles; external-system roles; separation of goals, responsibility, data visibility, policy/authority/control capability; audience-aware but evidence-consistent views | unresolved `Open actor questions` whose later semantics are owned by accepted concept/AUTH contracts; UI/IAM mapping questions | candidate preserves actors without promoting historical questions to policy |
| `foundation.terminology` | `docs/foundation/003_terminology.md` | `docs/canonical/reference/terminology.md` | foundational ecosystem/evaluation/change/time/authorization/Investigation/Impact/governance terms; durable non-equivalences; current terminology for later accepted control and replay semantics | obsolete statements that later phases still need to define already-accepted semantics; detailed stable-family ownership reserved for later CKR groups | candidate supplies current naming discipline without stealing later contract ownership |
| `foundation.concept_design_method` | `docs/foundation/004_concept_design_method.md` | `docs/canonical/reference/concept-design-method.md` | concept criteria; one-primary-purpose heuristic; required specification fields; independent state/actions; synchronizations; ambiguity behavior; discovery/acceptance workflow; vendor/architecture/UI anti-patterns | pre-architecture sequencing language interpreted historically; external tutorial/reference list as methodology provenance rather than product semantics | candidate preserves Concept Design as an ongoing semantic/change discipline |
| `foundation.architectural_principles` | `docs/foundation/005_architectural_principles.md` | `docs/canonical/invariants/architectural-principles.md` | **AP-01–AP-32**, including history, evidence/interpretation separation, provenance, typed Lineage, evaluation separations, security/minimization, tool replaceability, unknown state, causal/Impact boundaries, passive monitoring, repository independence, active-control separation, bitemporal replay | phrases describing architecture as still wholly future; detailed ARCH-001–500 realization remains CKR-I-owned | candidate preserves all 32 principle identities and current constraints |
| `foundation.security_governance_policy` | `docs/foundation/006_security_governance_and_policy_model.md` | `docs/canonical/policies/security-governance.md` | trust boundaries; **SP-01–SP-15**; metadata sensitivity; least privilege/minimization; authorization-aware questioning; separation of raw/analytical/control capabilities; historical disclosure; Impact disclosure; passive vs active-control security; governance/authority categories; conflict/unknown rules; threat themes | implementation-specific IAM/network/secret-store questions; earlier “deferred to technical design” wording now owned by later accepted architecture/implementation; exact AUTH/INTG contracts remain CKR-D/H | candidate preserves policy without becoming detailed AUTH/architecture owner |
| `foundation.ecosystem_lifecycles` | `docs/foundation/007_ecosystem_lifecycles.md` | `docs/canonical/reference/ecosystem-lifecycles.md` | all **14 durable lifecycles** plus ledger/non-rewriting semantics; current bitemporal language; distinct intent/deployment/execution/change/evaluation, Investigation, causal, Impact, control/Explanation history | storage/workflow architecture; exact concept actions/state remain CKR-C–I-owned | candidate preserves lifecycle semantics as cross-cutting reference |
| `foundation.mvp_boundary` | `docs/foundation/008_mvp_boundary.md` | `docs/canonical/policies/mvp-boundary.md` | 13 required MVP capability areas; **Scenarios A–K**; unresolved/multi-causal outcomes; historical knowledge reconstruction; policy-aware Explanation; explicit non-goals | obsolete idea that MVP technical architecture remains wholly undecided; final realization sequencing stays in implementation program; optional model/search/active control remain non-required | candidate aligns foundation proof boundary with accepted Phase 010 passive-monitoring-first handoff without changing MVP meaning |
| `reference.glossary` | `docs/reference/glossary.md` | `docs/canonical/reference/glossary.md` | compact current vocabulary for ecosystem, scope/identity/authority, governance, health, evidence/time, change/control, replay, causal reasoning, Impact/safeguard, Explanation/provenance, Concept Design; key non-equivalences | phase-number narration and stale “Phase X must refine” statements; exact concept/refinement/authority definitions remain with their later CKR owners | candidate becomes compact vocabulary index, not a second detailed contract corpus |

## Cross-record boundary review

### Product definition vs MVP boundary

`product-definition.md` owns the enduring product purpose/outcome and broad capability stance. `mvp-boundary.md` owns what the first proof must demonstrate. MVP scope does not redefine the full product.

### Terminology vs glossary

`terminology.md` owns foundational naming discipline and the most important non-collapse rules. `glossary.md` is the broader compact lookup surface. Neither may replace detailed concept/stable-ID owners.

### Concept Design method vs accepted concept catalog

`concept-design-method.md` owns how functionality is decomposed and changed. It does not own the 24 concept definitions; those remain CKR-C records.

### Architectural principles vs ARCH contracts

`architectural-principles.md` owns AP-01–AP-32 cross-cutting constraints. It does not own the detailed Phase 010 architecture contracts; ARCH-001–500 remain legacy-authoritative until CKR-I.

### Security/governance foundation vs detailed authority/integration architecture

`security-governance.md` owns durable product-security and governance policy. Exact Assertion Authority / Capability Authorization contract semantics remain under CKR-D; source/integration authority mechanics remain CKR-H; technical security/serving/control realization remains CKR-I.

### Lifecycles vs concept state/actions

`ecosystem-lifecycles.md` summarizes cross-concept temporal behavior. It does not become the authoritative state/action definition for the concepts participating in those lifecycles.

## Historical material deliberately not promoted

These remain design history/provenance:

- `docs/foundation/009_initial_roadmap.md` — historical sequencing;
- `docs/foundation/010_open_questions.md` — historical/unresolved question register, many items later answered elsewhere;
- `docs/foundation/011_phase_006_exit_phase_007_handoff.md` — historical handoff;
- old statements such as “Phase 004/005 must define…” where accepted later contracts now exist;
- technical implementation speculation superseded by accepted Phase 010 architecture and `docs/implementation/`.

Leaving this material out of canonical current truth is **not semantic loss**. Promoting it would reintroduce contradictory chronology into the current layer.

## Contradiction review

No CKR-B candidate currently requires an A4 semantic change to reconcile the nine inventoried sources with later accepted design.

Observed differences fall into three non-semantic categories:

1. **later accepted refinement** — canonical wording uses the accepted later terminology/boundaries rather than preserving a stale future-tense statement;
2. **historical progression** — roadmap, open-question, handoff, and “to be decided later” text remains provenance;
3. **ownership narrowing** — detailed concept/stable-family semantics are referenced rather than duplicated into foundation resources.

If later review uncovers a genuine contradiction rather than one of these categories, the affected record must remain `candidate_ready` until explicit A4 adjudication.

## Cutover gate

All nine records may cut over together only after deterministic validation confirms:

- exact nine-record candidate set;
- candidate authority markers and migration-record identity;
- AP-01–AP-32 coverage;
- SP-01–SP-15 coverage;
- 14 lifecycle headings;
- MVP required-capability coverage and Scenarios A–K;
- Concept Design required specification/boundary coverage;
- critical terminology/non-equivalence coverage;
- provenance back to each legacy owner;
- history-only foundation sources remain preserved;
- CKR status and Implementation 001-A block remain synchronized.

After cutover, the legacy 001–008 foundation files and old glossary become provenance/history for these nine records; other foundation/reference/concept/contract domains retain their independent inventory state.
