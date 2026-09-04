# CKR-B Semantic Conservation Matrix

**Status:** CUTOVER COMPLETE — CLOSURE VALIDATION PENDING

**Scope:** the nine records assigned to CKR-B in `canonical_ownership_inventory.json`.

## Review rule

CKR-B accepts a canonical resource only when it:

- answers its bounded current question without chronological reconstruction;
- preserves accepted durable meaning from its legacy owner and material later refinements;
- excludes only historical progression, obsolete future-phase language, resolved open questions, or superseded implementation speculation;
- does not absorb semantic ownership assigned to CKR-C–I;
- retains bounded provenance to the prior owner/refinement sources;
- passes deterministic semantic-coverage and authority-state validation.

Textual identity is not required. **Semantic conservation is required.**

## Record-by-record disposition

| Record | Prior owner | Canonical owner | Durable meaning preserved | Historical / independently owned detail not promoted | Disposition |
|---|---|---|---|---|---|
| `foundation.product_definition` | `docs/foundation/001_product_definition.md` | `docs/canonical/reference/product-definition.md` | product purpose; evidence-grounded current/historical/causal/Impact/semantic/policy answer outcome; nine capability families; product stance/non-goals; success characteristics | early-phase sequencing and implementation speculation | canonicalized |
| `foundation.actors_stakeholders` | `docs/foundation/002_actors_and_stakeholders.md` | `docs/canonical/reference/actors-and-stakeholders.md` | eight human roles; external-system roles; separation of goals, responsibility, visibility, policy/authority/control capability | unresolved historical actor questions; IAM/UI mappings | canonicalized |
| `foundation.terminology` | `docs/foundation/003_terminology.md` | `docs/canonical/reference/terminology.md` | foundational ecosystem/evaluation/change/time/authorization/Investigation/Impact/governance terms and non-equivalences | stale future-phase statements; detailed concept/stable-family ownership | canonicalized |
| `foundation.concept_design_method` | `docs/foundation/004_concept_design_method.md` | `docs/canonical/reference/concept-design-method.md` | concept criteria; one-purpose heuristic; spec fields; state/actions; synchronization; ambiguity/change discipline; anti-patterns | historical sequencing/external reference material not required for current method | canonicalized |
| `foundation.architectural_principles` | `docs/foundation/005_architectural_principles.md` | `docs/canonical/invariants/architectural-principles.md` | **AP-01–AP-32** and their current cross-cutting constraints | detailed ARCH-001–500 realization remains CKR-I-owned | canonicalized |
| `foundation.security_governance_policy` | `docs/foundation/006_security_governance_and_policy_model.md` | `docs/canonical/policies/security-governance.md` | trust boundaries; **SP-01–SP-15**; minimization; authorization-aware questioning; raw/analytical/control separation; historical disclosure; Impact disclosure; passive/active control security; conflict rules; threat themes | exact AUTH/INTG/ARCH contracts and implementation mechanics remain later-owned | canonicalized |
| `foundation.ecosystem_lifecycles` | `docs/foundation/007_ecosystem_lifecycles.md` | `docs/canonical/reference/ecosystem-lifecycles.md` | all **14 lifecycles** plus non-rewriting/bitemporal ledger principle | exact concept action/state contracts remain CKR-C–I-owned | canonicalized |
| `foundation.mvp_boundary` | `docs/foundation/008_mvp_boundary.md` | `docs/canonical/policies/mvp-boundary.md` | thirteen required MVP capability areas; **Scenarios A–K**; unresolved/multi-causal outcomes; historical reconstruction; policy-aware Explanation; explicit non-goals | package sequencing remains implementation authority; optional systems/control remain non-required | canonicalized |
| `reference.glossary` | `docs/reference/glossary.md` | `docs/canonical/reference/glossary.md` | current compact ecosystem, authority, governance, health, evidence/time, change/control, replay, causal, Impact, safeguard, Explanation/provenance and Concept Design vocabulary | exact concept/refinement/authority contracts remain with later CKR owners | canonicalized |

## Cross-record ownership boundaries

### Product definition vs MVP boundary
`product-definition.md` owns enduring product purpose/outcome. `mvp-boundary.md` owns what the first proof must demonstrate. MVP scope does not redefine the full product.

### Terminology vs glossary
`terminology.md` owns foundational naming discipline/non-collapse rules. `glossary.md` is the broader compact lookup surface. Neither replaces detailed concept/stable-ID owners.

### Concept Design method vs concept catalog
`concept-design-method.md` owns decomposition/change methodology. The 24 concept definitions remain CKR-C-owned records.

### Architectural principles vs ARCH contracts
`architectural-principles.md` owns AP-01–AP-32. ARCH-001–500 remain Phase-010 legacy authority until CKR-I.

### Security/governance vs detailed authority/integration/architecture
`security-governance.md` owns durable product-security/governance policy. Exact Assertion Authority/Capability Authorization contracts remain CKR-D; integration/source authority CKR-H; technical security/control realization CKR-I.

### Lifecycles vs concept state/actions
`ecosystem-lifecycles.md` summarizes cross-concept temporal behavior; it does not become the authoritative state/action definition for participating concepts.

## Historical material deliberately not promoted

These remain design history/provenance:

- `docs/foundation/009_initial_roadmap.md` — historical sequencing;
- `docs/foundation/010_open_questions.md` — historical/unresolved register, including items later answered elsewhere;
- `docs/foundation/011_phase_006_exit_phase_007_handoff.md` — historical handoff;
- old “Phase 00X must define…” statements where later accepted contracts now exist;
- technical implementation speculation superseded by Phase 010 and `docs/implementation/`.

Leaving this material outside current canonical truth is **not semantic loss**; promoting it would reintroduce chronology/drift.

## Contradiction review

No CKR-B resource required A4 semantic change. Differences were classified as:

1. **later accepted refinement** — current wording uses accepted later semantics rather than preserving obsolete future tense;
2. **historical progression** — roadmap/open-question/handoff text remains provenance;
3. **ownership narrowing** — detailed concept/stable-family semantics are referenced instead of duplicated.

A genuine contradiction discovered later must still follow A4 change control; canonicalization is not blanket authorization to resolve it editorially.

## Candidate-stage proof

PR #7 candidate head `a1ee4af445f3c94fbc237b205d39fb613c1e2445` passed:

- Documentation consistency #182 — SUCCESS;
- Agentic conformance #64 — SUCCESS;
- canonical inventory — 34 records / 24 concepts / 0 canonicalized / 9 candidates;
- CKR-B semantic coverage — 9 records / `candidate_ready` / 0 errors;
- fixture catalog — 158 scenarios;
- negative controls — 19/19;
- secret scan — 175 governed text files / 0 errors;
- all persistent context budgets — PASS.

This proved candidates could be reviewed without changing current authority.

## Cutover disposition

The nine targets now declare `CANONICAL CURRENT AUTHORITY`, their inventory records are `canonicalized`, and living foundation/reference/canonical routing points current questions to them. Phase-001 sources and the pre-CKR glossary remain available as provenance.

Cutover-state conformance must pass before CKR-B is marked complete.
