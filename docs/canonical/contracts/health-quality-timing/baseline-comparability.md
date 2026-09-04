# Baselines, Comparability & Statistical Context

**Canonical key:** `health.baseline-comparability`

**Kind:** CONTRACT

**Authority:** CANONICAL CURRENT AUTHORITY

**Migration record:** `stable_family.HLTH`

**Owns current question:** Which historical Observations form a valid descriptive reference and when is a current measurement empirically comparable to that reference?

**Stable IDs:** HLTH-019–HLTH-029

## Current semantics

### HLTH-019 — Baseline Reference Set, Regime, Population & Window Binding
A Baseline is a descriptive provenance-bearing summary over a bounded eligible reference population whose regime, metric definition, grain/population, window/calendar/cohort and structural/interface context are part of its meaning.

### HLTH-020 — Empirical Comparability Dimensions & Result States
Comparability is conclusion-relative across identity, definition/version, unit/denominator, grain/population, structural/semantic state, context/calendar/cohort, method/approximation, coverage and time alignment. States can include directly comparable, comparable under explicit normalization, non-comparable, insufficient reference, ambiguous, conflicting, unavailable, unknown/unresolved and not applicable.

### HLTH-021 — Baseline Classes, Fixed/Rolling Reference & Version Semantics
Fixed/reference-period, rolling/adaptive, seasonal/cadence, cohort and post-change/new-regime Baselines are semantic classes that remain versioned and provenance-bearing rather than prescribing one algorithm.

### HLTH-022 — Seasonality, Cadence, Business Calendar & Cohort Context
Material calendar, cadence and cohort context constrains reference membership. Recency alone never substitutes for a valid month-end, quarter-end, weekday/weekend, holiday, batch-position or governed-cohort comparison.

### HLTH-023 — Structural/Semantic Breaks, Segmentation & New Reference Regimes
Realized changes to definition, grain, population, key, field meaning, denominator, interface, operating mode or measurement method may segment affected references. New regimes use realized post-change evidence; planned/target state cannot populate a Baseline.

### HLTH-024 — Reference Sufficiency, Coverage, Representativeness & Low-Volume Limits
Reference sufficiency is conclusion-specific and may depend on observation count, temporal/cohort coverage, missing periods, population/denominator size, variability and evidence limitations. No universal minimum sample count is accepted.

### HLTH-025 — Approximation, Sampling & Measurement-Uncertainty Comparability
Approximate/sampled evidence can participate only with method identity and material uncertainty retained. Exact and approximate results are not automatically interchangeable, and method changes may create a comparability break.

### HLTH-026 — Distribution, Quantile, Category-Share & Shape Reference Semantics
Purpose-driven distribution references may use meaningful quantiles, shares, bins or shape descriptors when data semantics and reference sufficiency support them. Descriptive distribution change is not automatically normative failure.

### HLTH-027 — Explicit Normalization & Transformed Comparison Semantics
Raw values may be non-comparable while an explicitly defined/versioned normalization supports a valid derived comparison. Normalization requires stable semantic numerator/denominator and evidence that it addresses the material scale difference.

### HLTH-028 — Baseline Refresh, Adaptation, Exclusion & Contamination Control
Rolling/adaptive Baselines use explicit membership, lag/holdout, exclusion and refresh/version rules. A current Observation cannot silently redefine the reference judging itself; apparent anomaly alone is not sufficient exclusion basis.

### HLTH-029 — Comparable-Baseline Resolution, Ambiguity & Descriptive Assessment
Multiple Baselines may coexist by context. Newest, largest, narrowest, broadest or numerically closest does not implicitly win; unresolved material context yields ambiguity. Within-reference behavior is not synonymous with healthy, and outside-reference behavior is not synonymous with failure.

## Invariants / boundaries

Observation ≠ reference-set membership ≠ Baseline summary/version ≠ comparative Assessment ≠ normative Expectation/health.

Repeated abnormal behavior can become descriptively typical without becoming acceptable. Authority may govern intended Baseline use but cannot manufacture empirical comparability.

## Provenance

- `docs/concepts/phase_006/03_baselines_comparability_distribution_statistical_context/README.md`
- Phase 006 Group 03 accepted HLTH-019–HLTH-029.
