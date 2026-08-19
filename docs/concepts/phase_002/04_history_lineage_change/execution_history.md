# Concept: Execution History

**Status:** Accepted — Phase 002 Group 04

## Purpose

Let users reconstruct which execution instances actually occurred, how their lifecycle progressed, and what operational outcome/context was established over time.

## Operational principle

A user asks what happened around Table C's volume shift. Execution History reconstructs the logical pipeline's executions from authoritative run evidence: the last pre-deployment run, the first run after a new Deployment became active, and subsequent runs. It preserves start/completion/outcome and lower-level job/task association where evidence supports it. It does not decide whether output was healthy, whether an expected run should have existed, or whether the deployment caused the data change.

## Actors

- Monitoring framework
- Data Engineer / Pipeline Maintainer
- Data Platform Administrator
- Databricks / orchestration sources

## State

- execution-instance identity;
- identified logical pipeline/job/task subject references;
- execution lifecycle states/transitions;
- actual start/completion/event times when known;
- terminal outcome/state when known;
- parent/child or orchestration context established by evidence;
- consumed/produced entity/run context when supported by evidence;
- source/provenance and collection/knowledge time;
- reconstruction confidence/ambiguity for logical executions assembled from lower-level evidence;
- correction, duplication-resolution, and late-arriving evidence history.

## Actions

### `recordState`
- **Intent:** record a provenance-bearing execution lifecycle state/event for an execution instance.
- **State effect:** extends the execution history without asserting data health.

### `associateExecution`
- **Intent:** associate lower-level job/task/run evidence with a logical execution when sufficient identity/provenance evidence exists.
- **Failure / unknown behavior:** ambiguous association remains unresolved rather than manufacturing one logical run.

### `correctState`
- **Intent:** record a correction/supersession to earlier execution evidence while retaining prior knowledge history.

### `resolveAt`
- **Intent:** reconstruct executions and lifecycle state for a subject/time window.
- **Observable result:** execution sequence plus provenance, ambiguity, unavailable/unauthorized context, or insufficient evidence.

## Invariants / behavioral expectations

- Execution History represents actual execution evidence, not scheduled/expected work.
- A successful execution does not imply fresh, complete, valid, or otherwise healthy output.
- Expected-but-never-started work is evaluated through **Expectation + sufficient absence evidence + Assessment**, not by inventing an execution instance.
- Missing telemetry is not evidence that no execution occurred.
- A logical pipeline is not assumed identical to one Databricks job or task.
- Reconstructed logical execution retains the evidence supporting lower-level associations.
- Event/effective time and record/knowledge time remain distinguishable where late evidence matters.
- Duplicate/conflicting source events are not silently flattened when outcome would change.
- Execution History does not own Deployment, Observation, Assessment, Lineage, or Change Intent state.

## Ambiguity and missing evidence

Run evidence can be late, duplicated, partial, conflicting, unavailable, or unauthorized. The concept reports those conditions. If a source cannot establish whether an execution occurred over a period, the history remains incomplete rather than synthesizing a missing-run fact.

## Synchronizations

- **Entity Identity** supplies pipeline/job/task/execution referents.
- **Monitoring Scope** provides monitoring-responsibility context without creating executions.
- **Change Intent** provides planned context that may be relevant to executions after activation but does not create run facts.
- **Deployment** can identify which active deployment/configuration applied to an execution when evidence supports the association.
- **Observation** may record measurements/facts about an execution or its produced data; it does not own execution-instance continuity.
- **Expectation** defines expected execution cadence/conditions where normative requirements exist.
- **Assessment** can evaluate execution evidence against expectations without mutating the history.
- **Lineage** can represent execution dependencies separately from execution lifecycle state.
- **Change** can use execution timing as context for realized changes.
- **Investigation** later uses execution sequence as evidence.

## Security / privacy / governance considerations

Execution metadata may expose schedules, environment topology, job names, failure details, operational incidents, or restricted dependencies. Authorized abstraction may expose a run outcome without revealing sensitive implementation details.

## Evidence / provenance considerations

Every execution state should retain source, source event time, collection/knowledge time where relevant, subject/execution identity, and correction history. Logical execution reconstruction must be explainable from underlying evidence.

## Representative scenarios

### Successful run with unhealthy output
A run succeeds. Separate Observations/Assessments later show its output violated completeness. Execution History remains successful; it is not rewritten as a failed run.

### Expected run did not occur
A freshness/operational Expectation says a run should occur by 06:00. A complete authoritative query establishes no qualifying run occurred. The negative Observation plus Expectation can produce a violation Assessment; Execution History does not create a phantom failed run.

### First run after planned change
A Change Intent is linked to a Deployment activated at 10:00. The first execution after activation is reconstructed and later used to compare observed behavior with planned context.

### Cross-job logical execution
One logical pipeline spans several Databricks tasks/jobs. Execution History can represent the logical execution only where association evidence is sufficient; otherwise it preserves partial lower-level executions.

### Conflicting terminal states
Two sources disagree whether a run was cancelled or failed. The conflict remains visible until evidence/authority resolves it.

## Non-goals

- defining schedules or execution Expectations;
- declaring data-health status;
- recording Deployment intent;
- root-cause attribution;
- replacing an orchestration system;
- assuming every logical pipeline maps to one job.

## Deferred questions

- minimum logical-execution identity model for MVP;
- which run lifecycle states need canonical normalization versus source-specific preservation;
- what evidence is sufficient to associate tasks/jobs into one logical execution;
- how long knowledge-time correction history must be retained/displayed.
