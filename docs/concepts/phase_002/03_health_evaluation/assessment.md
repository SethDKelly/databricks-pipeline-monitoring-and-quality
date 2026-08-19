# Concept: Assessment

**Status:** Candidate

## Purpose

Let users understand how observed evidence compares with applicable expectations and/or baselines for a defined subject and time.

## Operational principle

Table C's row count is assessed against its applicable baseline and freshness expectation. The result states that volume is materially below baseline while freshness remains healthy, cites the observations/reference context used, and does not claim why the change occurred.

## Actors

- Monitoring framework
- Data Engineer
- Business Analyst
- Data Steward

## State

- assessed subject/dimension/context/time;
- result/status (for example healthy, degraded, stale, anomalous, unknown) using later-agreed vocabulary;
- supporting observations;
- applicable expectation and/or baseline references;
- evaluation rationale;
- evidence sufficiency/confidence/limitations;
- provenance/version of assessment logic conceptually, without implementation details.

## Actions

### `assess`
Evaluates evidence against applicable reference context.

### `reassess`
Produces a new assessment when evidence/reference context legitimately changes while preserving historical assessments.

### `explainBasis`
Returns the observations, expectations/baselines, and limitations supporting the assessment.

## Invariants / behavioral expectations

- Assessment does not mutate observations or expectations.
- Assessment does not assert root cause.
- Success in one dimension does not imply health in another.
- Unknown/insufficient evidence is preferable to fabricated status.
- Historical assessment basis remains discoverable.

## Ambiguity and missing evidence

If reference context is missing, stale, conflicting, or evidence is insufficient, the result must carry that uncertainty rather than forcing healthy/degraded.

## Synchronizations

- Observation + Expectation/Baseline synchronize to create/revise an Assessment.
- Degraded/unknown Assessment can synchronize with Investigation.
- Explanation presents assessment status with its evidence basis.

## Security / privacy / governance considerations

Assessment must not leak restricted underlying evidence through derived status or explanation. Audience visibility must be based on an authorized evidence view.

## Evidence / provenance considerations

An assessment must retain the exact observations and expectation/baseline context used, plus enough evaluation provenance to reconstruct why the status was produced at that time.

## Representative scenarios

### Happy path
Table C is fresh and within its approved quality expectation.

### Degraded path
C is fresh but materially below baseline in volume; only the volume dimension is degraded.

### Conflicting evidence
Applicable expectations conflict; the assessment returns unresolved/ambiguous rather than a forced rollup.

### Unauthorized evidence
A business analyst can see a degraded status and safe rationale without receiving protected raw evidence.

## Non-goals

- causal reasoning;
- downstream impact;
- incident workflow;
- defining DQX or metric implementations.

## Open questions

- What assessment status vocabulary best supports engineering and business audiences?
- How should multi-dimensional assessments roll up without hiding a severe dimension?
