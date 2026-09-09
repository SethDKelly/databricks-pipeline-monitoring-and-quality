# Group 03 — Health Evaluation

**Status:** Review complete — concepts accepted

## Goal

Create a disciplined model for saying **what should be true**, **what reference behavior looks like**, **what was actually observed**, and **what interpretation the evidence supports** without collapsing normative, descriptive, factual, or causal claims.

## Accepted concepts

- [Expectation](expectation.md)
- [Baseline](baseline.md)
- [Observation](observation.md)
- [Assessment](assessment.md)

## Boundary decisions

### 1. Expectation is normative; Baseline is descriptive

Expectation states what **should** be true/acceptable for a subject/context/time. Baseline describes reference behavior derived from evidence for a comparable context.

Historical regularity does not silently become an approved requirement. A Baseline can inform establishment of an Expectation, but the two concepts remain separate.

### 2. Typical is not healthy; atypical is not degraded

A Baseline-only comparison supports descriptive language such as `typical`, `atypical`, `within reference`, `outside reference`, or `non-comparable`.

Normative health/compliance language requires an applicable Expectation or another explicitly normative basis. An historically common bad state may be typical and still violate an Expectation.

### 3. Observation is fact; Assessment is interpretation

Observation preserves a measured/retrieved fact with measurement meaning, subject, time, provenance, and evidence coverage. It does not declare health, anomaly, staleness, or cause.

Assessment interprets authorized Observation evidence against an explicit Expectation and/or comparable Baseline.

### 4. Missing evidence is not observed absence

No telemetry is not the same as an Observation of zero/no event. A negative/absence fact is valid only when sufficient observation coverage positively establishes that absence over a defined interval.

This prevents a monitoring outage from being mislabeled as a pipeline failure.

### 5. Assessment basis must remain explicit

Every Assessment identifies whether its conclusion is normative (Expectation), comparative (Baseline), or explicitly both. Results preserve the referenced versions and evidence used.

The product cannot turn a Baseline deviation into a quality failure or turn Baseline typicality into a health claim without normative evidence.

### 6. Health is dimension-scoped by default

Execution, freshness, completeness, validity, uniqueness, volume, schema, distribution, and other dimensions can disagree. One successful dimension never masks another failed/degraded/unresolved dimension.

Any future overall/composite health status must cite component Assessments and an explicit aggregation rule. There is no implicit average/majority roll-up.

### 7. Reassessment preserves history

Late/corrected evidence or legitimate reference corrections can produce a new Assessment. The new result does not silently rewrite what the product concluded earlier from the evidence then available.

### 8. None of these concepts establishes cause

Expectation, Baseline, Observation, and Assessment provide the evidence/evaluation substrate for later Change and Investigation concepts. A violation or anomaly can trigger investigation but is not a root-cause claim.

## Scenario review

### S-01 — Join-volume degradation

Pass. A, B, and C can each carry row-count/quality Observations. C's 14M rows may be atypical versus its Baseline; an approved volume Expectation, if present, can separately establish a normative violation. Neither result says whether A, B, the join, or another condition caused the change.

### S-02 — Stale upstream with successful downstream execution

Pass. Successful-run evidence and freshness evidence are separate Observations/Assessments. A downstream run can succeed while its input/output violates a freshness Expectation.

### S-03 — Deployment-correlated shift

Pass. Group 03 can establish that a distribution Assessment changed around the same time as a deployment, but it cannot convert temporal proximity into cause.

### S-04 — Cross-repository dependency

Pass. Health evidence attaches through Entity Identity rather than repository boundaries. Upstream/downstream assessments can be considered across repositories when authorized and in Monitoring Scope.

### S-05 — Conflicting governance metadata

Pass. Conflicting Expectations remain conflicts unless an authority rule resolves them. Semantic Definition and Responsibility Assignment can provide context without overwriting health evidence.

### S-06 — Policy-sensitive explanation

Pass. A viewer may receive an authorized Assessment such as `criterion violated` or `atypical` without receiving restricted thresholds, reference distributions, or row-level evidence.

### S-07 — Historical replay

Pass. Observation event/collection time, Expectation effective versions, Baseline versions, and append-only reassessment history allow reconstruction of what happened, what criterion/reference applied, and what the product concluded at the incident time.

## Deferred questions

- first-MVP expectation dimensions and Baseline classes;
- basis-specific Assessment status vocabulary;
- explicit source authority for Expectation maintenance;
- detailed Baseline comparability/structural-break automation;
- statistical uncertainty semantics;
- whether composite/overall health eventually warrants a dedicated concept;
- exact evidence-coverage semantics for observed absence.

## Group exit gate

**Satisfied.** Execution, freshness, quality, volume, schema, distribution, and similar evidence can be expressed without conflating normative criteria, descriptive historical reference, measured facts, or interpreted status. Missing evidence and observed absence are distinct, historical evaluation remains reproducible, and no health evaluation silently asserts root cause.

The next review group is **Group 04 — History, Lineage & Change**.
