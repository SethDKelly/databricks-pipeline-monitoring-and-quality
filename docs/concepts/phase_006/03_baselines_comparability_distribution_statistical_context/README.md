# Phase 006 Group 03 — Baselines, Comparability, Distribution & Statistical Context

**Status:** Accepted — HLTH-019–HLTH-029; H03-01–H03-32 pass

## Goal

Define descriptive reference behavior and empirical comparability over the exact measurement identity from Group 01 and structural/consumer context from Group 02, without turning Baselines into normative Expectations or introducing an opaque anomaly/confidence score.

## Accepted handoff from Groups 01–02

- HLTH-001–HLTH-008 bind metric/check identity, subject/grain/window, applicability and provenance;
- HLTH-009–HLTH-018 bind structural/interface version, field identity, key/grain transitions, consumer-specific compatibility and scoped review triggers;
- same display metric name does not establish definition continuity;
- same column names/types do not establish same grain/meaning;
- structural compatibility alone does not establish historical metric comparability;
- prospective/planned state never substitutes for realized historical state;
- AUTH-020 can govern intended Baseline use/review but cannot manufacture empirical comparability.

## Accepted contracts

- **HLTH-019 — Baseline Reference Set, Regime, Population & Window Binding**;
- **HLTH-020 — Empirical Comparability Dimensions & Result States**;
- **HLTH-021 — Baseline Classes, Fixed/Rolling Reference & Version Semantics**;
- **HLTH-022 — Seasonality, Cadence, Business Calendar & Cohort Context**;
- **HLTH-023 — Structural/Semantic Breaks, Segmentation & New Reference Regimes**;
- **HLTH-024 — Reference Sufficiency, Coverage, Representativeness & Low-Volume Limits**;
- **HLTH-025 — Approximation, Sampling & Measurement-Uncertainty Comparability**;
- **HLTH-026 — Distribution, Quantile, Category-Share & Shape Reference Semantics**;
- **HLTH-027 — Explicit Normalization & Transformed Comparison Semantics**;
- **HLTH-028 — Baseline Refresh, Adaptation, Exclusion & Contamination Control**;
- **HLTH-029 — Comparable-Baseline Resolution, Ambiguity & Descriptive Assessment**.

## Core reference model

Preserve:

**Observation ≠ reference-set membership ≠ Baseline summary/version ≠ comparative Assessment ≠ normative Expectation/health**.

A Baseline is a descriptive, provenance-bearing summary/reference over a bounded eligible evidence population. Its membership, operating regime, calendar/cohort context, metric definition, grain/population and structural/interface semantics are part of the reference meaning.

No new concept is required. Baseline remains the accepted truth owner for descriptive reference behavior; Observation supplies evidence; Assessment interprets a current Observation against a comparable Baseline; Expectation remains independent normative truth.

## Comparability

Comparability is evaluated against the proposition being compared, not a universal score. Material dimensions include subject identity, metric definition/version, units/denominator, grain/population, field/key/interface state, operating context, calendar/cohort, measurement method/approximation, evidence coverage and temporal alignment.

Possible bounded states include:

- directly comparable;
- comparable under an explicit normalization/transformation;
- non-comparable;
- insufficient reference;
- ambiguous reference context;
- conflicting reference/evidence;
- unavailable;
- unknown/unresolved;
- not applicable.

A governance decision may stop use of a Baseline but cannot convert empirically non-comparable evidence into comparable evidence.

## Baseline classes and contexts

Functional reference classes can include fixed/reference-period, rolling/adaptive, seasonal/cadence-stratified, cohort-segmented and post-change/new-regime references. These are semantic classes, not algorithms, and can compose.

Recency is never an automatic substitute for context. Month-end, quarter-end, holiday, weekday/weekend, batch-cycle position or governed cohorts can require separate reference populations when they materially change the measurement distribution.

A narrow segment with insufficient evidence remains insufficient unless an explicit valid broader comparison exists; the product does not silently fall back to a convenient global Baseline.

## Structural/semantic breaks

Realized changes to metric definition, grain, population, key, field meaning, denominator, interface, operating mode or measurement method can segment affected references. The break is scoped: unrelated dimensions can continue to use existing Baselines when their measurement semantics remain comparable.

Change Intent can register a prospective break but cannot activate it or populate the future Baseline. New-regime Baselines are derived from sufficient realized post-change Observations. Transitional periods can remain separately identified instead of being forced into either regime.

## Sufficiency and low volume

Reference sufficiency is conclusion-relative. Number of observations, temporal coverage, missing periods, cohort/calendar coverage, population/denominator size, sampling/approximation and operating variability all can constrain the strength of a comparison.

There is no universal minimum sample count. Two observations can support a literal descriptive statement about those observations without necessarily supporting a stable p95, category-share envelope or tail-distribution claim.

`0% of 2` and `0% of 2,000,000` are not equally informative reference evidence merely because the rate matches.

## Approximation and sampling

Approximate/sampled metrics can be valid Baseline evidence when their method identity and material uncertainty are retained. Exact and approximate observations are not automatically interchangeable. Differences smaller than material method uncertainty must not be presented with false precision.

Changing approximation algorithms/parameters can itself create a comparability break where error behavior/meaning changes materially.

## Distribution/shape references

Purpose-driven distribution references can use selected quantiles, category shares, stable bins, shape descriptors or other explicit summaries. Quantiles require semantically ordered data. Tail claims may require stronger reference sufficiency than central summaries.

Distribution change is descriptive `different/atypical relative to reference` until a normative Expectation separately determines acceptability. No universal drift/divergence score is required.

## Explicit normalization

Raw observations can be non-comparable while a separately defined normalized measure remains comparable. Legitimate normalization requires stable numerator/denominator meaning, an explicit transformation/version, source provenance and evidence that the transformation addresses the relevant scale difference.

Examples can include errors per million eligible records, duration per processed unit or other semantically justified rates. Ad-hoc post-outlier rescaling does not automatically create comparability.

## Refresh/adaptation

Rolling/adaptive Baselines remain versioned and auditable. Reference membership, lag/holdout behavior, exclusion rules and refresh semantics are explicit.

A current Observation must not silently redefine the reference used to judge itself. Likewise, `looks anomalous` is not enough reason to exclude a historical Observation; known incident/test/transition/incomplete-load exclusions require a provenance-bearing reference-population basis.

Repeated abnormal behavior can eventually become descriptively typical under a legitimate Baseline while still violating a normative Expectation. Baseline adaptation never approves the behavior.

## Multiple Baselines and descriptive Assessment

One subject can legitimately have several Baselines for different contexts. Newest, largest, narrowest, broadest or numerically closest does not automatically win. If multiple material contexts apply and the definitions do not provide a valid matching/composition rule, the comparison remains ambiguous.

Baseline-based Assessment can report within/outside reference behavior, atypical/material shift or unresolved states. `Within Baseline` does not mean healthy; `outside Baseline` does not mean failed/degraded.

## Scenario review

See [`scenario_review.md`](scenario_review.md). H03-01–H03-32 pass.

## Exit result

- no new concept;
- HLTH-019–HLTH-029 accepted;
- HLTH-001–HLTH-018 remain accepted;
- concept count remains 24;
- SYN-001–SYN-035, REF-001–REF-030 and AUTH-001–AUTH-053 remain unchanged;
- no statistical/anomaly algorithm, Metric View/DQX realization, storage or compute architecture selected;
- **Group 04 — Expectations, Thresholds, Margins, Waivers & Assessment Semantics is next and has not started.**