# 003 — Pipeline Health, Freshness, and Data Quality

**Status:** Historical discovery input — refined by accepted Phase 002 Group 03 specifications in [`../concepts/phase_002/03_health_evaluation/`](../concepts/phase_002/03_health_evaluation/).

## Goal

Define what health means without reducing the answer to job success or failure and without conflating normative criteria, historical reference behavior, measured facts, or interpreted status.

## Three distinct questions

The framework should keep at least these concerns distinct:

1. **Operational health** — did the expected execution occur and satisfy applicable execution Expectations?
2. **Freshness** — what is the observed currency of the data, and does it satisfy applicable freshness Expectations?
3. **Data quality** — do Observations satisfy explicit quality Expectations relevant to intended use?

A pipeline can be operationally successful while failing freshness or quality Expectations.

## Accepted Group 03 evaluation model

The authoritative Phase 002 concept model now distinguishes four concepts:

- **Expectation** — normative: what should be true/acceptable;
- **Baseline** — descriptive: what comparable reference behavior looks like;
- **Observation** — factual: what was measured/retrieved;
- **Assessment** — interpretive: what Observation evidence means relative to an explicit Expectation and/or Baseline.

Important consequences:

- typical behavior is not automatically healthy;
- atypical behavior is not automatically degraded;
- missing telemetry is not an observed absence;
- one healthy dimension does not imply overall health;
- historical Assessments preserve the evidence/reference versions used;
- none of these concepts establishes root cause.

## Operational health considerations

Discovery should consider signals such as:

- expected versus actual run occurrence;
- latest successful run;
- failure/cancellation state;
- retry behavior;
- duration changes;
- task-level failures;
- missed dependencies;
- schedule delay;
- deployment/run correlation;
- environment-specific differences.

A run status is an Observation/evidence input. Whether the execution was acceptable is an Assessment against applicable Expectations; a duration may also be described as typical/atypical against a Baseline.

## Freshness and staleness

Freshness is contextual rather than based on one global threshold.

Questions include:

- When was the output last materially updated?
- How often is it expected to update?
- Is the current delay unusual for this asset?
- Is upstream data itself stale according to its own applicable Expectation?
- Is a dataset fresh by timestamp but effectively unchanged?
- Is the data timely enough for the downstream business use?

Expected freshness may vary by dataset, consumer, day of week, business calendar, or operating window.

**Staleness is normative:** it means observed freshness violates an applicable freshness Expectation. If no Expectation exists, a Baseline may support `unusually old`/`atypical freshness`, but historical behavior alone does not establish staleness.

## Data quality dimensions

Quality should be extensible but may include:

- completeness;
- validity;
- uniqueness;
- consistency;
- referential integrity;
- volume expectations;
- distribution and drift;
- schema conformance;
- business-rule conformance;
- reconciliation between related datasets;
- timeliness/freshness where treated as a quality dimension.

## Degradation over time

The project should support more than pass/fail checks.

A useful quality history should help answer:

- Did a normatively bad condition worsen gradually or suddenly?
- Which Observation/Assessment dimension changed first?
- Is the latest value outside comparable historical behavior?
- Is the change seasonal, structurally non-comparable, or atypical?
- Did a violated criterion recover without intervention?
- Did the change coincide with a deployment, upstream change, or source-system event?

A Baseline deviation alone is not degradation. Directional/normative meaning is required before calling a change worse.

## Evidence absence

Missing evidence and observed absence must remain distinct. For example:

- a complete authoritative query returning zero qualifying runs can support an Observation of non-occurrence;
- a failed query, disconnected integration, or missing telemetry means insufficient evidence and must not be represented as zero runs.

## Multi-dimensional health

Execution, freshness, completeness, validity, volume, schema, distribution, and other dimensions may disagree. Assessments are dimension-scoped by default.

Any future overall-health roll-up must identify its component Assessments and explicit aggregation rule and must not hide a severe child result.

## Databricks-native considerations

Databricks DQX and Metric Views remain favored capabilities for later technical evaluation because they may provide useful native building blocks for measurement, quality evaluation, and business-facing metrics.

The accepted concepts remain tool-independent. Later phases should evaluate how these tools realize Expectation, Observation, Baseline, and Assessment needs rather than redefining the product around vendor syntax.
