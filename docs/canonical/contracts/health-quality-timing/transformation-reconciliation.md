# Transformation Reconciliation & Metric Relevance

**Canonical key:** `health.transformation-reconciliation`

**Kind:** CONTRACT

**Authority:** CANONICAL CURRENT AUTHORITY

**Migration record:** `stable_family.HLTH`

**Owns current question:** When do upstream/downstream measurements participate in a valid transformation-specific reconciliation without blindly propagating metric values, health status or causality through Lineage?

**Stable IDs:** HLTH-041–HLTH-054

## Current semantics

### HLTH-041 — Reconciliation Vocabulary, Transformation Binding & Derived Measurement Identity
A reconciliation binds exact transformation/version, inputs/roles/output, fields/keys/measures, grain/population/window/current-cycle context and derivation rule. Derived reconciliation measurements have their own identity and provenance.

### HLTH-042 — Join Eligibility, Match/Unmatched Population & Directionality
Join reconciliation uses exact eligible populations, direction-specific match/unmatched measures and join semantics. Left and right match rates are distinct and generic input/output row equality is invalid.

### HLTH-043 — Join Cardinality, Fan-Out, Key Integrity & Duplicate Effects
Join cardinality/fan-out, zero/one/many-match populations and observed duplicate/key integrity remain explicit. Many-to-many joins may legitimately amplify output; declared key role does not prove uniqueness.

### HLTH-044 — Filter Selection, Inclusion/Exclusion & Population Reconciliation
Filter reconciliation relates eligible input, included/output and excluded populations only when exact filter/grain semantics justify it. Selection effects create new downstream completeness/distribution evidence rather than inherited status.

### HLTH-045 — Aggregation, Conservation & Non-Composable Measure Semantics
Conservation is measure-specific. Additive totals can reconcile only under justified semantic/filter/duplicate/unit/grouping conditions; row counts, averages, ratios, percentages, distinct counts and quantiles are not generically composable.

### HLTH-046 — Deduplication, Survivor Selection & Uniqueness Reconciliation
Deduplication binds duplicate-equivalence and survivor-selection rules. Successful downstream uniqueness does not rewrite upstream non-uniqueness, and survivor choice may alter other measurement distributions.

### HLTH-047 — Union, Merge/Upsert, Source Contribution & Overlap Semantics
Append/bag union, distinct union and merge/upsert have different contribution/overlap/action semantics. Input row count alone does not determine resulting target population when dedupe, overlap, updates or deletes apply.

### HLTH-048 — Null, Default, Cast & Derived-Value Transformation Semantics
Transformations may preserve, introduce, remove, replace or reinterpret null/value state. Lower downstream null rate does not prove upstream completeness improvement; defaults/sentinels can mask physical missingness while violating business validity.

### HLTH-049 — Freshness, Current-Cycle & Multi-Input Version Alignment
Multi-input reconciliation binds exact versions/windows actually consumed and criterion-specific cadence expectations. A downstream completion does not prove every input was current; missing consumption/version evidence remains unresolved.

### HLTH-050 — Distribution, Quantile, Unit & Normalization Preservation Boundaries
Distribution/quantile status is not generically propagated through joins, filters, unions or aggregations. Deterministic unit transforms or explicit normalization can support derived comparison only where population/grain semantics remain valid.

### HLTH-051 — Reconciliation Evidence, Provenance, Uncertainty & Restriction Propagation
Derived reconciliation evidence preserves every material source Observation, transformation/reconciliation version, input/output version, coverage, uncertainty, approximation, restriction and time limitation. Derivation cannot upgrade evidence quality or declassify restricted inputs automatically.

### HLTH-052 — Multi-Hop Composition, Path-Specific Relevance & No Blind Status Propagation
Transformation-local rules do not automatically compose into direct multi-hop equations. Lineage never recursively copies metric values, Baseline status, warning, violation, severity or waiver; relevance is field/population/version/path specific.

### HLTH-053 — Historical Transformation Version, Rule Binding & Reassessment
Historical reconciliation binds then-valid Lineage, transformation/version, input/output versions, reconciliation definition, current-cycle context, Expectations/Baselines and knowledge cutoff. Later corrected evidence may cause reassessment without rewriting earlier state.

### HLTH-054 — Reconciliation Relevance, Localization, Downstream Assessment & Causal Separation
Reconciliation may establish mismatch, downstream relevance or localization to a transformation boundary but not cause. Upstream violation can coexist with healthy downstream criteria after isolation/repair, and downstream failure can originate in transformation logic despite healthy inputs.

## Invariants / boundaries

Local Observation ≠ downstream-relevant upstream context ≠ reconciliation definition/check ≠ derived reconciliation Observation ≠ reconciliation Assessment ≠ Causal Claim.

Lineage is relationship context, not a metric equation or health-status propagation mechanism. Causal propositions continue to use REF-013–REF-020; exposure/Impact remains independently evidenced.

## Provenance

- `docs/concepts/phase_006/05_transformation_reconciliation_metric_propagation/README.md`
- Phase 006 Group 05 accepted HLTH-041–HLTH-054.
