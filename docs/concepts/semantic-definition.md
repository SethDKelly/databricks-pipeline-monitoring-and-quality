# Semantic Definition

**Canonical key:** `concept.semantic_definition`

**Kind:** CONCEPT

**Authority:** CANONICAL CURRENT AUTHORITY

**Migration record:** `concept.semantic_definition`

**Owns current question:** What does an identified entity or facet mean in the relevant business/technical context and time?

**Stable IDs:** N/A

## Current semantics

Semantic Definition records provenance-bearing semantic assertions by facet—such as business definition, technical description, grain, unit, population, calculation meaning, field/key role, and governed schema meaning—together with context, effective time, authority standing, revisions, corrections, and conflicts.

## Actions

- `define` — record/synchronize a semantic assertion.
- `revise` — prospectively supersede an assertion while preserving history.
- `resolveAt` — return applicable assertions, unknown, conflicting, unauthorized, or unavailable.

## Invariants / boundaries

- Meaning is not health, quality, freshness, causality, or realized physical state.
- Business and technical semantic facets may have different authority holders and valid contexts.
- Governed/declared schema meaning ≠ normative schema Expectation ≠ realized schema Observation/Change.
- Names, DDL, SQL, code, schema shape, or synchronization recency do not manufacture authoritative business meaning.
- Missing semantics remain unknown; current semantics do not rewrite historical interpretation.
- Semantic Definition does not own responsibility, Classification, Policy Context, Expectation, authorization, or conformance.

## Ambiguity / evidence

Context-specific definitions may coexist. Same-target incompatibility remains provenance-bearing conflict unless accepted Assertion Authority resolves standing.

## Synchronizations / related canonical resources

Entity Identity supplies the subject; Assertion Authority supplies standing; Responsibility Assignment supplies stewardship context; Observation/Change own realized state; Expectation owns normative compatibility; Explanation uses semantics for audience interpretation.

## Non-goals

Responsibility, policy applicability, access, health criteria, physical-state truth, or universal single-text definitions.

## Provenance

- `docs/concepts/phase_002/02_semantics_governance_policy/semantic_definition.md`
- `docs/concepts/phase_005/02_semantic_responsibility_classification_policy_criticality_governance/`
