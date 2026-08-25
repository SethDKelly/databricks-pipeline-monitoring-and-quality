# Phase 006 Group 03 — Baselines, Comparability, Distribution & Statistical Context

**Status:** Next — not yet started

## Goal

Define descriptive reference behavior and empirical comparability over the exact measurement identity from Group 01 and the structural/consumer context from Group 02, without turning Baselines into normative Expectations or introducing an opaque anomaly/confidence score.

## Accepted handoff from Groups 01–02

- HLTH-001–HLTH-008 provide exact metric-definition/version, subject/grain/window binding, applicability and provenance;
- HLTH-009–HLTH-018 provide structural/interface version, field identity, key/grain transitions, consumer-specific compatibility and scoped metric/Baseline review triggers;
- a field/schema/grain/type change can make some historical measurements non-comparable while leaving unrelated dimensions valid;
- same display metric name does not establish definition continuity;
- same column names/types do not establish same grain/meaning;
- supported rename/identity continuity can preserve some measurement relationships but still requires comparability review;
- prospective/planned structural state must not be substituted for realized historical state;
- `compatible` structural state does not itself establish metric/Baseline comparability;
- AUTH-020 may govern intended Baseline use/review, but authority cannot manufacture empirical comparability.

## Review scope

- Baseline classes and explicit reference population/window/cohort semantics;
- rolling versus fixed/reference-period behavior;
- comparable metric definition/grain/population/schema/interface requirements;
- exact continuity versus bounded normalization/transformation where comparison remains meaningful;
- seasonality, cadence and cohort segmentation;
- low-volume/sample-size limitations;
- exact versus approximate/sampled observations and uncertainty;
- numeric/categorical distribution comparison;
- selected quantiles, category shares and drift semantics;
- structural/semantic changes that break, weaken or segment comparability;
- sparse/new metrics with insufficient historical reference;
- `comparable`, `non-comparable`, `insufficient reference`, `unknown/conflicting/unavailable` states;
- whether historical reference needs replacement, segmentation or bounded reset after change;
- preservation of original Observations when a new Baseline begins.

## Questions to resolve

1. What exactly is a Baseline reference set versus a current Observation?
2. When are two metric observations sufficiently comparable to participate in one Baseline?
3. Which material definition/grain/population/schema changes require segmentation rather than adjustment?
4. How should seasonality/cadence/cohort context be represented without creating one opaque anomaly score?
5. How should small sample sizes or rare populations limit comparative claims?
6. How do approximate quantiles/distinct counts/sampled distributions carry uncertainty into comparison?
7. When can a transformed/normalized comparison be legitimate without pretending the raw observations have the same meaning?
8. How should the framework represent insufficient history for a new metric or post-change regime?

## Boundaries

Do not promote typicality to health. Do not define threshold severity, warning/failure, waiver or normative Assessment semantics yet; those belong to Group 04. Do not define A+B→C propagation/reconciliation yet; that belongs to Group 05. Do not select anomaly algorithms, statistical libraries, storage, Metric Views/DQX realization, or compute architecture.

**Group 03 has not started.**