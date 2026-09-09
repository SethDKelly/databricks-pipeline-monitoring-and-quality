# Decision Records — Phase 006 Group 03 Baselines, Comparability, Distribution & Statistical Context

Continues after D-295.

### D-296 — Group 03 requires no new concept
**Status:** Accepted — Phase 006 Group 03
Baseline remains the truth owner for descriptive reference behavior; Observation supplies evidence and Assessment interprets current evidence against a comparable Baseline. No Reference Set, Statistical Profile, Drift Result or Anomaly concept is added.

### D-297 — Baseline reference membership is explicit and provenance-bearing
**Status:** Accepted — Phase 006 Group 03
A Baseline binds subject, metric definition/version, grain/population, structural/interface regime, operating context, reference window, calendar/cohort semantics, evidence coverage and inclusion/exclusion rule. Available history is not automatically eligible history.

### D-298 — Comparability is multidimensional and conclusion-relative
**Status:** Accepted — Phase 006 Group 03
Subject identity, metric definition, unit/denominator, grain/population, structural/interface context, calendar/cohort, measurement method/approximation, coverage and timing are evaluated as applicable. No universal numeric comparability score is accepted.

### D-299 — Bounded comparability states remain richer than yes/no
**Status:** Accepted — Phase 006 Group 03
Comparisons can be directly comparable, comparable under explicit normalization, non-comparable, insufficient reference, ambiguous, conflicting, unavailable, unknown/unresolved or not applicable. These states must not collapse into typical/atypical/health.

### D-300 — Fixed, rolling, seasonal/cohort and post-change Baselines are functional reference classes
**Status:** Accepted — Phase 006 Group 03
Baseline classes describe reference membership/version semantics rather than algorithms. They can compose and do not create implementation modules.

### D-301 — Seasonality/cadence/cohort context can be material to comparability
**Status:** Accepted — Phase 006 Group 03
Recency does not override business-calendar/cycle/cohort context. A narrow context with insufficient evidence remains insufficient unless a valid broader comparison is explicitly defined.

### D-302 — Realized semantic/structural breaks segment affected references only
**Status:** Accepted — Phase 006 Group 03
Metric-definition, grain, population, key, denominator, field meaning, interface, operating-mode or measurement-method changes can create a new reference regime. Unaffected dimensions may retain prior Baselines. Change Intent predicts but does not activate the break.

### D-303 — New-regime Baselines derive from realized post-change evidence
**Status:** Accepted — Phase 006 Group 03
Planned/target values never populate empirical Baselines. Transitional periods can remain explicitly non-representative/segmented until sufficient stable evidence exists.

### D-304 — Reference sufficiency is conclusion-relative and has no universal sample minimum
**Status:** Accepted — Phase 006 Group 03
Observation count, temporal coverage, missing periods, denominator/population size, operating variability, cohort coverage and method limitations constrain comparative claims. Tail/distribution claims can require more evidence than central summaries.

### D-305 — Approximation and sampling uncertainty remain part of comparison semantics
**Status:** Accepted — Phase 006 Group 03
Approximate/sampled metrics may be valid evidence when method identity and material limitations are retained. Exact/approximate values are not automatically interchangeable, and differences within material uncertainty are not presented with false precision.

### D-306 — Distribution references are purpose-driven and non-normative
**Status:** Accepted — Phase 006 Group 03
Quantiles, category shares, stable-bin summaries and shape descriptors can support descriptive comparison when semantically meaningful and sufficiently evidenced. No universal drift/divergence score is required, and distribution change alone does not establish defect.

### D-307 — Explicit normalization can preserve a derived comparison without rewriting raw comparability
**Status:** Accepted — Phase 006 Group 03
A versioned transformation with stable numerator/denominator meaning and provenance can produce a comparable derived rate/measure even when raw values are non-comparable. Ad-hoc post-outlier rescaling is insufficient.

### D-308 — Rolling/adaptive Baselines require explicit refresh and contamination controls
**Status:** Accepted — Phase 006 Group 03
Reference-window progression, lag/holdout semantics, exclusions and derivation version are explicit. A current Observation must not silently redefine the reference used to assess itself.

### D-309 — Anomaly appearance alone cannot justify reference exclusion
**Status:** Accepted — Phase 006 Group 03
Excluding evidence merely because it looks unusual would circularly make the Baseline self-validating. Incident/test/transition/incomplete-load exclusions require an independent reference-population basis and retained provenance.

### D-310 — Historical typicality and normative acceptability remain independent
**Status:** Accepted — Phase 006 Group 03
Repeated bad behavior can become descriptively typical; a current value can be atypical yet normatively acceptable. Baseline adaptation never grants approval or changes an Expectation.

### D-311 — Multiple plausible Baselines do not receive hidden precedence
**Status:** Accepted — Phase 006 Group 03
Newest, largest-history, narrowest, broadest or numerically closest does not automatically win. Different contexts can coexist; unresolved overlap remains ambiguous unless the Baseline definitions provide a valid context matching/composition rule.

### D-312 — Baseline refresh and regime replacement preserve history
**Status:** Accepted — Phase 006 Group 03
New Baseline versions and post-change references do not rewrite supporting Observations, prior Baselines or historical Assessments. Historical replay retains the exact Baseline version and context used at the time.

### D-313 — Group 03 scenario review passes
**Status:** Accepted — Phase 006 Group 03
H03-01–H03-32 pass under HLTH-019–HLTH-029 without a new concept, universal score or statistical architecture choice.

### D-314 — Phase 006 Group 03 exits; Group 04 is next
**Status:** Accepted
HLTH-001–HLTH-029 are accepted. The concept catalog remains 24; SYN-001–SYN-035, REF-001–REF-030 and AUTH-001–AUTH-053 remain unchanged. Phase 006 Group 04 — Expectations, Thresholds, Margins, Waivers & Assessment Semantics is next and has not started.