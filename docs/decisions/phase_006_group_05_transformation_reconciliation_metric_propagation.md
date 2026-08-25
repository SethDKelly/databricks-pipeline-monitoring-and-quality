# Decision Records — Phase 006 Group 05 Transformation Reconciliation & Metric Propagation

Continues after D-334.

### D-335 — Group 05 requires no new concept
**Status:** Accepted — Phase 006 Group 05
Lineage, Semantic Definition/check semantics, Observation, Expectation and Assessment already own the required truth. No Reconciliation or Metric Propagation concept is added.

### D-336 — Local measurement, relevant context, reconciliation Observation and Assessment remain distinct
**Status:** Accepted — Phase 006 Group 05
Upstream local metrics retain their identity. Downstream relevance does not clone them into downstream metrics. A derived reconciliation becomes its own provenance-bearing Observation and can be independently assessed.

### D-337 — Lineage never creates a reconciliation formula by itself
**Status:** Accepted — Phase 006 Group 05
Typed time-valid Lineage establishes relationship context/candidates. Conservation/equality/range relationships require explicit transformation semantics.

### D-338 — Reconciliation binds exact transformation/version and cycle context
**Status:** Accepted — Phase 006 Group 05
Input/output identities, roles, fields/keys/measures, grain/population/window, transformation version and relevant current-cycle versions are part of reconciliation meaning.

### D-339 — Join reconciliation uses directional eligible/matched/unmatched populations
**Status:** Accepted — Phase 006 Group 05
Left and right match rates have separate denominators; generic A+B=C row-count arithmetic is rejected.

### D-340 — Join cardinality/fan-out is first-class reconciliation evidence
**Status:** Accepted — Phase 006 Group 05
Zero/one/many matches, duplicate-key effects and fan-out/cardinality shape can explain output amplification or loss without treating it automatically as defect or cause.

### D-341 — Filter reconciliation is predicate- and population-specific
**Status:** Accepted — Phase 006 Group 05
Input/output/excluded conservation applies only to bounded pure-filter semantics that justify it. Filter selection can change downstream distributions and DQ metrics without inheritance.

### D-342 — Aggregation conservation is measure-specific
**Status:** Accepted — Phase 006 Group 05
Additive totals can reconcile only where semantic additivity and transformation conditions support it. Row counts, averages, ratios, percentages, quantiles and distinct counts are not generically composable.

### D-343 — Deduplication reconciliation preserves duplicate and survivor semantics
**Status:** Accepted — Phase 006 Group 05
Removed-record counts, duplicate groups and survivor behavior are bound to an exact dedupe rule. Healthy output uniqueness does not rewrite unhealthy upstream uniqueness.

### D-344 — Union and merge/upsert have different population semantics
**Status:** Accepted — Phase 006 Group 05
Bag union can be additive under explicit conditions; DISTINCT union requires overlap handling; merge/upsert uses action classes and target state rather than simple input-count conservation.

### D-345 — Null/completeness behavior is transformation-derived, not inherited
**Status:** Accepted — Phase 006 Group 05
Joins, filters, defaults, casts and derived-value logic can introduce/remove/replace null/value states. Lower output null rate is not automatic evidence of improved source completeness.

### D-346 — Current-cycle alignment is multi-input and version-specific
**Status:** Accepted — Phase 006 Group 05
Output completion/success does not prove every required input was current. Alignment binds actual consumed versions and permitted cadence/lag semantics.

### D-347 — Distribution and quantile metrics do not propagate generically
**Status:** Accepted — Phase 006 Group 05
Transformation selection, overlap, aggregation and mapping can alter distributions. Only explicit semantics such as valid unit/value transformations or normalization support derived relationships.

### D-348 — Reconciliation carries evidence limitations forward
**Status:** Accepted — Phase 006 Group 05
Availability, coverage, approximation/sampling uncertainty, ambiguity/non-comparability, restriction state and temporal provenance constrain the derived reconciliation; derivation cannot upgrade evidence quality.

### D-349 — Derived reconciliation is not declassification
**Status:** Accepted — Phase 006 Group 05
Restricted input evidence can support independently authorized derived analysis, but aggregates/reconciliation outputs may remain sensitive and subject to Capability Authorization/disclosure governance.

### D-350 — Metric/status propagation through Lineage is prohibited
**Status:** Accepted — Phase 006 Group 05
Metric values, Baseline typicality, warning, normative violations, severity and waivers never recursively copy downstream solely because a Lineage path exists.

### D-351 — Multi-hop reconciliation requires explicit valid composition
**Status:** Accepted — Phase 006 Group 05
Valid A↔B and B↔C reconciliations do not automatically create an A↔C equality/conservation rule. Path-specific relevance and composition must be established.

### D-352 — Consumer/path-specific relevance is first-class
**Status:** Accepted — Phase 006 Group 05
An upstream condition is relevant only where the material downstream path consumes the corresponding field/population/version under semantics that make it material. Asset-level reachability is insufficient.

### D-353 — Upstream health and downstream health remain independent
**Status:** Accepted — Phase 006 Group 05
An upstream violation can coexist with downstream meets after isolation/repair, and upstream meets can coexist with downstream violation introduced by transformation logic.

### D-354 — Reconciliation localization is not causal confirmation
**Status:** Accepted — Phase 006 Group 05
A mismatch or first deviation at a transformation boundary is useful Investigation evidence but not root cause. Causal propositions remain Causal Claim under REF-013–REF-020.

### D-355 — Historical reconciliation is transformation-version and knowledge-cut bound
**Status:** Accepted — Phase 006 Group 05
Current code/reconciliation definitions are never projected backward. Later Lineage/metric corrections can produce retrospective reassessment while preserving the prior historical result.

### D-356 — Group 05 scenario review passes
**Status:** Accepted — Phase 006 Group 05
H05-01–H05-44 pass under HLTH-041–HLTH-054 without a new concept, blind propagation, causal shortcut or architecture choice.

### D-357 — Phase 006 Group 05 exits; Group 06 is next
**Status:** Accepted
HLTH-001–HLTH-054 are accepted. The concept catalog remains 24; SYN-001–SYN-035, REF-001–REF-030 and AUTH-001–AUTH-053 remain unchanged. Phase 006 Group 06 — Composite Health, Readiness Suitability & Progressive Result Timing is next and has not started.
