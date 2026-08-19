# Concept: Semantic Definition

**Status:** Candidate

## Purpose

Let people understand what an identified entity means and how it should be interpreted in business/data terms.

## Operational principle

A business analyst sees that a downstream metric has degraded. Before interpreting the magnitude, the analyst resolves the underlying asset's definition, grain, units, important inclusion/exclusion semantics, and effective version so the technical change can be understood in business context.

## Actors

- Business Analyst
- Data Steward / Governance
- Data Engineer
- Monitoring framework

## State

- definition/description assertions;
- semantic attributes needed for interpretation, such as grain, unit, domain, or business meaning where relevant;
- scope/subject identity;
- effective time/version context;
- provenance and authority context;
- unresolved or conflicting definitions.

## Actions

### `define`
Creates or synchronizes a semantic assertion for an identified subject.

### `revise`
Supersedes a semantic assertion prospectively while preserving history.

### `resolveAt`
Returns the effective definition for a subject/time, or conflicting/unknown if authority cannot safely resolve it.

## Invariants / behavioral expectations

- A semantic definition describes meaning; it does not assert data health.
- Current definitions do not silently rewrite historical interpretation.
- Definitions from different sources retain provenance.
- A convenient synchronized copy does not automatically become authoritative.
- Technical descriptions and business definitions may coexist without being falsely flattened.

## Ambiguity and missing evidence

Missing semantics should be communicated as missing context, not invented from column/table names. Conflicts remain explicit until authority rules resolve them.

## Synchronizations

- Asset Identity identifies the subject.
- Ownership can identify responsible semantic stewards without owning the definition itself.
- Explanation uses semantics to translate technical evidence into business meaning.
- Change can describe semantic changes without asserting quality degradation.

## Security / privacy / governance considerations

Definitions can reveal sensitive business meaning even without values. Visibility may need restriction.

## Evidence / provenance considerations

Every definition should retain source, asserted-by context, and effective time where available. When an effective definition is selected from several assertions, the selection basis must remain explainable.

## Representative scenarios

### Happy path
A business definition and grain are available from an authoritative source and are shown with the affected asset.

### Degraded path
An asset has only a technical description; the explanation identifies missing business semantics instead of inventing them.

### Conflicting evidence
Two sources define the metric differently; both assertions and the unresolved authority conflict remain visible.

### Unauthorized evidence
A user may see a safe summary of an asset's meaning while restricted semantic details remain hidden.

## Non-goals

- ownership;
- classification or policy;
- data-quality expectation;
- authorization;
- automatic semantic inference from names alone.

## Open questions

- What minimum semantic attributes are necessary for MVP business-facing explanations?
- How should competing technical versus business definitions be presented?
