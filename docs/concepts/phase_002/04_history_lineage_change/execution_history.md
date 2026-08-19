# Concept: Execution History

**Status:** Candidate

## Purpose

Let users reconstruct what logical pipeline/job work ran, when it ran, and what operational outcome/context was observed over time.

## Operational principle

A user asks whether Pipeline P is running. The system shows its recent execution sequence, including the last successful run, a later failed run, and the fact that a subsequent job succeeded while consuming stale upstream input. Execution history remains distinct from data-health assessment.

## Actors

- Monitoring framework
- Data Engineer
- Data Platform Administrator
- Databricks / orchestration sources

## State

- identified execution instances and their subject identities;
- expected/actual start and completion timing when known;
- execution outcome/state;
- relevant parent/dependency/run context when observed;
- execution provenance/source;
- association to produced/consumed entities when supported by evidence;
- historical corrections/late-arriving execution evidence.

## Actions

### `recordExecution`
Records an execution instance/state transition from authoritative evidence.

### `completeExecution`
Records terminal outcome without implying output health.

### `resolveRecent`
Returns execution history for a subject/time range.

## Invariants / behavioral expectations

- Successful execution does not imply fresh or high-quality output.
- Execution history retains source time and provenance.
- A logical pipeline is not assumed identical to a Databricks job.
- Missing executions and missing telemetry are distinguishable where evidence permits.

## Ambiguity and missing evidence

Missing run evidence is distinct from evidence that no run occurred. Late, partial, duplicated, or conflicting run telemetry must remain distinguishable, and an unauthorized run may appear only as an opaque dependency if policy permits.

## Synchronizations

- Asset Identity references logical pipeline/job/task entities.
- Observation can attach execution/data observations to a run context.
- Deployment resolves what deployed state was active for an execution.
- Lineage can relate execution dependencies without merging execution history into lineage.
- Investigation uses execution sequence as evidence.

## Security / privacy / governance considerations

Execution metadata can expose schedules, system names, failure details, and sensitive operational topology. Visibility must be controlled independently from raw data access.

## Evidence / provenance considerations

Each execution state/outcome must retain its source, relevant timestamps, subject identity, and correction history. A reconstructed logical-pipeline run must expose the evidence used to associate lower-level job/task executions.

## Representative scenarios

### Happy path
A user resolves the recent successful and failed executions of a logical pipeline.

### Degraded path
A downstream run succeeds after its upstream expected refresh never occurred.

### Conflicting evidence
Different sources disagree on terminal status; the conflict remains visible.

### Unauthorized evidence
A user can know an upstream prerequisite failed without receiving restricted job details.

## Non-goals

- defining schedules/expectations;
- data-quality assessment;
- deployment history;
- causal attribution.

## Open questions

- What is the minimum logical execution identity model for cross-repository dependencies?
- How should expected-but-never-started execution be represented relative to Expectation?
