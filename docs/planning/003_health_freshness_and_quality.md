# 003 — Pipeline Health, Freshness, and Data Quality

## Goal

Define what “healthy” means without reducing the answer to job success or failure.

## Three distinct questions

The framework should keep at least these concerns distinct:

1. **Operational health** — did the expected execution occur, and did it complete as expected?
2. **Freshness** — is the resulting data recent enough for its intended use?
3. **Data quality** — does the resulting data meet meaningful expectations?

A pipeline can be operationally successful while failing freshness or quality expectations.

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

## Freshness and staleness

Staleness should be contextual rather than based on one global threshold.

Questions include:

- When was the output last materially updated?
- How often is it expected to update?
- Is the current delay unusual for this asset?
- Is upstream data itself stale?
- Is a dataset fresh by timestamp but effectively unchanged?
- Is the data timely enough for the downstream business use?

Expected freshness may vary by dataset, consumer, day of week, business calendar, or operating window.

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

- Did quality degrade gradually or suddenly?
- Which measure changed first?
- Is the latest value outside historical behavior?
- Is the change seasonal or anomalous?
- Did the quality recover without intervention?
- Did the degradation coincide with a deployment, upstream change, or source-system event?

## Quality expectations versus observations

The framework should distinguish:

- **expectation:** what should be true;
- **observation:** what was measured;
- **evaluation:** whether the observation met the expectation;
- **trend:** how observations evolve over time;
- **incident/degradation:** an operational interpretation requiring investigation.

This separation will be important when evaluating Databricks DQX or other quality mechanisms later.

## Databricks-native considerations

Databricks DQX and Metric Views are favored capabilities for later design because they may provide useful native building blocks for quality measurement and business-facing metrics.

At this stage, the project should define the information and reasoning it requires first, then evaluate how well those tools satisfy the requirements.
