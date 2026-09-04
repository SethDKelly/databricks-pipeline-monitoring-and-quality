# Change

**Canonical key:** `concept.change`

**Kind:** CONCEPT

**Authority:** CANDIDATE / NOT CURRENT AUTHORITY

**Migration record:** `concept.change`

**Owns current question:** What realized difference or state transition does evidence establish actually occurred for a subject/relationship/facet/time?

**Stable IDs:** N/A

## Current semantics

Change owns a bounded realized proposition: changed subject/relationship and facet, before/after or source event, semantic grain/population/interface/version, direction/magnitude where supportable, transition time/interval, comparability basis, provenance/knowledge time, limitations/corrections, and contextual associations to intent/deployment without absorbing them.

## Actions

- `derive` — compare sufficiently comparable before/after evidence to record a realized difference.
- `recordOccurred` — preserve an explicit source-declared change event without inventing downstream effects.
- `correct` — retain correction/supersession and prior knowledge.
- `resolveWindow` — return realized Changes for a bounded subject/facet/time with limitations.

## Invariants / boundaries

- Change is realized/descriptive; Change Intent is planned/anticipatory.
- Deployment activation can itself be implementation-state Change, but does not manufacture downstream data/schema/topology Change.
- Change is not automatically good/bad/healthy/degraded/expected/unexpected or causal.
- Missing prior evidence is not a zero/default state.
- Different change kinds remain typed and slice-specific.
- Intent-to-realization conformance is derived comparison, not Change state.
- Rollback/reversion does not imply all affected facets returned/recovered.
- Topology relationship truth remains Lineage; Change can describe its transition but not manufacture the edge.
- Event/effective time and knowledge/record time remain independent.

## Ambiguity / evidence

Non-comparable/incomplete/time-misaligned/conflicting/restricted state yields partial/unknown/non-comparable Change rather than fabricated deltas.

## Synchronizations / related canonical resources

Observation supplies before/after evidence; Deployment supplies implementation transitions; Lineage supplies topology history; Expectation/Baseline retain their own lifecycle truth; Assessment interprets health; Causal Claim owns attribution.

## Non-goals

Planned intent, health assessment, causal attribution, anomaly implementation, or ownership of other concepts' state.

## Provenance

- `docs/concepts/phase_002/04_history_lineage_change/change.md`
- `docs/concepts/phase_007/02_change_intent_deployment_realization_realized_change/`
