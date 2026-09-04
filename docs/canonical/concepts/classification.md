# Classification

**Canonical key:** `concept.classification`

**Kind:** CONCEPT

**Authority:** CANONICAL CURRENT AUTHORITY

**Migration record:** `concept.classification`

**Owns current question:** Which categories in a named governance, sensitivity, or criticality vocabulary are asserted for a subject/facet/context/time?

**Stable IDs:** N/A

## Current semantics

Classification records subject/facet, named scheme, source category, scheme meaning/context, effective interval, provenance/authority, optional governed crosswalk evidence, revision history, and conflicts. Source labels remain preserved even when normalized.

## Actions

- `classify` — record a category assertion under a named scheme.
- `reclassify` — prospectively supersede a category while preserving history.
- `resolveAt` — return applicable labels, unknown, explicitly unclassified, conflicting, unauthorized, or unavailable.

## Invariants / boundaries

- Classification ≠ Policy Context ≠ Capability Authorization ≠ Assertion Authority ≠ compliance.
- Authority for one scheme does not transfer to another.
- Business, operational, consumer, and delivery criticality may legitimately differ by context/scheme.
- Criticality may influence priority but is not evidence of actual exposure, effect, consequence, health failure, or causality.
- Missing Classification is unknown—not non-sensitive, unclassified, or low criticality.
- Crosswalks/normalizations are provenance-bearing governed assertions, not replacement source truth.
- Lineage, schema/tag similarity, containment, or parent classification does not automatically propagate Classification.
- No universal criticality score is accepted.

## Ambiguity / evidence

Multiple independent schemes may coexist; conflict is scheme/context-specific. Restricted labels may be safely abstracted.

## Synchronizations / related canonical resources

Policy Context may consume Classification as applicability evidence but cannot be manufactured from it. Impact may use criticality only as prioritization context. Explanation can expose authorized sensitivity/importance context.

## Non-goals

Access enforcement, policy applicability, compliance, health/Impact proof, legal interpretation, or universal score/vocabulary.

## Provenance

- `docs/concepts/phase_002/02_semantics_governance_policy/classification.md`
- `docs/concepts/phase_005/02_semantic_responsibility_classification_policy_criticality_governance/`
