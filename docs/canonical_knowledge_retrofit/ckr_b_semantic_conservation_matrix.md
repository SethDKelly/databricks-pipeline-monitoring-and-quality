# CKR-B Semantic Conservation Matrix

**Status:** ACCEPTED — CKR-B COMPLETE

**Scope:** the nine records assigned to CKR-B in `canonical_ownership_inventory.json`.

## Acceptance rule

CKR-B accepts a canonical resource only when it answers its bounded current question without chronological reconstruction, preserves accepted durable meaning, leaves later-domain ownership independent, retains bounded provenance, and passes deterministic semantic-coverage/authority validation. Textual identity with the historical source is not required; **semantic conservation is required**.

## Record disposition

| Record | Canonical owner | Preserved current meaning | Historical / later-owned material not promoted |
|---|---|---|---|
| `foundation.product_definition` | `docs/canonical/reference/product-definition.md` | product purpose/outcome/non-goals; nine capability families; evidence/history/governance/Investigation/Impact/Explanation stance | early sequencing/implementation speculation |
| `foundation.actors_stakeholders` | `docs/canonical/reference/actors-and-stakeholders.md` | eight human roles; external-system roles; responsibility/visibility/authority/control separation | unresolved historical actor questions; IAM/UI mapping |
| `foundation.terminology` | `docs/canonical/reference/terminology.md` | foundational terms and non-equivalences across ecosystem/evaluation/time/control/authority/Impact | stale future-phase wording; detailed concept/stable-family ownership |
| `foundation.concept_design_method` | `docs/canonical/reference/concept-design-method.md` | concept criteria, one-purpose heuristic, spec fields, state/actions/synchronization/ambiguity/change discipline | historical sequencing/external tutorial material |
| `foundation.architectural_principles` | `docs/canonical/invariants/architectural-principles.md` | **AP-01–AP-32** | detailed ARCH-001–500 realization remains CKR-I |
| `foundation.security_governance_policy` | `docs/canonical/policies/security-governance.md` | trust boundaries; **SP-01–SP-15**; minimization/disclosure/control boundaries/conflict rules | exact AUTH/INTG/ARCH contracts remain CKR-D/H/I |
| `foundation.ecosystem_lifecycles` | `docs/canonical/reference/ecosystem-lifecycles.md` | fourteen durable lifecycles and non-rewriting/bitemporal history | exact concept action/state contracts remain later-owned |
| `foundation.mvp_boundary` | `docs/canonical/policies/mvp-boundary.md` | thirteen required MVP capability areas; **Scenarios A–K**; optional/non-required systems/control | implementation-package sequencing remains implementation authority |
| `reference.glossary` | `docs/canonical/reference/glossary.md` | compact current vocabulary and non-equivalences | exact concept/refinement/authority contracts remain later-owned |

## Boundary review

- Product definition owns enduring product purpose; MVP boundary owns first-proof scope.
- Terminology owns naming discipline; glossary is compact lookup; neither replaces detailed concept/stable-ID owners.
- Concept Design method owns decomposition/change discipline; the 24 concept definitions remain CKR-C records.
- AP-01–AP-32 constrain architecture; ARCH-001–500 remain CKR-I records.
- Security/governance foundation owns cross-cutting policy; detailed AUTH/INTG/ARCH mechanics remain later-owned.
- Ecosystem lifecycles summarize cross-concept temporal behavior without owning participating concept state/actions.

## Historical material deliberately not promoted

The following remain provenance/history rather than current truth:

- `docs/foundation/009_initial_roadmap.md`;
- `docs/foundation/010_open_questions.md`;
- `docs/foundation/011_phase_006_exit_phase_007_handoff.md`;
- stale “later phase must define…” wording superseded by accepted design;
- technical speculation superseded by Phase 010 and `docs/implementation/`.

This is not semantic loss; promoting historical unresolved/future-tense text would recreate current-authority drift.

## Contradiction disposition

No CKR-B resource required A4 semantic change. Differences were later accepted refinement, historical progression, or ownership narrowing. A future genuine contradiction still requires A4 adjudication.

## Validation history

Candidate state, PR #7 head `a1ee4af445f3c94fbc237b205d39fb613c1e2445`:

- Documentation consistency #182 — SUCCESS;
- Agentic conformance #64 — SUCCESS;
- 34 records / 24 concepts / 0 canonicalized / 9 candidates;
- CKR-B coverage 9/9 candidate-ready;
- 158 scenarios; 19/19 negative controls.

Initial cutover state, head `4b3cbaff623dafc57915d3503ce4b5859ff35564`:

- Documentation consistency #208 — SUCCESS;
- semantic authority and CKR-B coverage PASS with 9 canonicalized / 0 candidates;
- unified conformance #90 failed only because the CKR README status bullets had been compressed outside the deterministic status grammar.

Corrected cutover state, head `4c21352e1a8f034e2d8587c934133ad8a6ccf94d`:

- Documentation consistency #209 — SUCCESS;
- Agentic conformance #91 — SUCCESS;
- 34 records / 24 concepts / **9 canonicalized / 0 candidates**;
- CKR-B semantic coverage 9/9 canonicalized;
- 158 scenarios;
- 19/19 negative controls;
- 175 governed text files / 0 secret findings;
- all context budgets PASS.

The #90 failure is retained as evidence that status grammar is enforced rather than silently tolerated.
