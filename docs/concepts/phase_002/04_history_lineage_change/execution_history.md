# Concept: Execution History

**Status:** Accepted — Phase 002 Group 04

## Later refinement — Phase 007 Group 04

Phase 007 Group 04 keeps **Execution History** as the actual execution truth owner and refines it through [`../../phase_007/04_execution_reconstruction_dependency_sequence/README.md`](../../phase_007/04_execution_reconstruction_dependency_sequence/README.md), **OPS-034–OPS-049**.

The refinement makes explicit that:

- expected work/opportunity/Gate state do not create execution instances;
- lifecycle evidence may remain partial;
- logical executions can be assembled from lower-level jobs/tasks only with sufficient identity/correlation evidence;
- retry/restart/rerun/backfill continuity is evidence/source-semantics dependent;
- actual temporal precedence, evidenced waiting and specific version consumption are different propositions;
- execution success and output existence/version are independent;
- Deployment active-at-time constrains but does not universally prove run-specific implementation state;
- specific input/output/implementation versions require run-specific binding evidence;
- duplicate/common-derived telemetry is not independent corroboration;
- `no run`, `no output` and `no consumption` require bounded negative evidence;
- historical execution reconstruction is bitemporal and non-rewriting.

The preliminary Phase 002 phrase `reconstruction confidence/ambiguity` is interpreted through the accepted Phase 004 evidence vocabulary: applicability, coverage/opportunity-to-observe, corroboration/common derivation, conflict, conclusion-specific sufficiency and explicit limitations. No universal execution-reconstruction confidence score is accepted.

## Purpose

Let users reconstruct which execution instances actually occurred, how their lifecycle progressed, and what operational outcome/context was established over time.

## Operational principle

A user asks what happened around Table C's volume shift. Execution History reconstructs the logical pipeline's executions from applicable run evidence: the last pre-deployment run, the first run after a new Deployment became active, and subsequent runs where ordering evidence supports those labels. It preserves start/completion/outcome and lower-level job/task association where evidence supports it. It can also retain run-specific implementation/input/output version associations where established. It does not decide whether output was healthy, whether an expected run should have existed, whether an Execution Gate should admit a future run, or whether the deployment caused the data change.

## Actors

- Monitoring framework
- Data Engineer / Pipeline Maintainer
- Data Platform Administrator
- Databricks / orchestration sources

## State

- execution-instance identity or bounded identity evidence;
- identified logical pipeline/job/task subject references;
- execution lifecycle states/transitions actually evidenced;
- attempt/retry/restart/rerun/backfill relationships when established;
- actual start/completion/event times when known;
- terminal outcome/state when known;
- parent/child or orchestration context established by evidence;
- actual sequence/ordering relationships when supportable;
- run-specific active implementation-state association when supported;
- consumed input/entity/version context when supported;
- produced output/entity/version context when supported;
- source/provenance and collection/knowledge time;
- evidence applicability/coverage/conflict/limitations for logical executions assembled from lower-level evidence;
- correction, duplication/common-derivation resolution, reassembly, and late-arriving evidence history.

## Actions

### `recordState`
- **Intent:** record a provenance-bearing execution lifecycle state/event for an execution instance.
- **State effect:** extends the execution history without asserting data health or fabricating missing transitions.

### `associateExecution`
- **Intent:** associate lower-level job/task/run evidence with a logical execution when sufficient identity/provenance evidence exists.
- **Failure / unknown behavior:** ambiguous association remains unresolved rather than manufacturing one logical run.

### `associateImplementationState`
- **Intent:** associate a specific implementation-state facet with an execution where run-specific evidence supports the binding.
- **Important:** Deployment active-at-time is context, not universal proof of run-specific use.

### `associateInputVersion`
- **Intent:** record that a bounded execution actually encountered/consumed a specific input/version where applicable evidence supports it.
- **Important:** Lineage/latest-output/timing alone is insufficient.

### `associateOutputVersion`
- **Intent:** associate produced/materialized output/version evidence with the execution/attempt that produced it where supportable.
- **Important:** successful terminal state does not manufacture output existence.

### `correctState`
- **Intent:** record a correction/supersession/reassembly to earlier execution evidence while retaining prior knowledge history.

### `resolveAt`
- **Intent:** reconstruct executions, lifecycle/attempt state, ordering and available run-specific version associations for a subject/time window.
- **Observable result:** execution sequence plus provenance, partial/ambiguous/conflicting/unavailable/unauthorized context, or insufficient evidence.

## Invariants / behavioral expectations

- Execution History represents actual execution evidence, not scheduled/expected work or an Execution Gate's prospective admission opportunity.
- A successful execution does not imply qualifying output, fresh/complete/valid data, or otherwise healthy output.
- Expected-but-never-started work is evaluated through **Expectation + sufficient absence evidence + Assessment**, not by inventing an execution instance.
- A gate-held execution opportunity is not represented as a failed execution merely because it did not start.
- Gate admission or override does not create an execution instance; an actual start/run requires separate execution evidence.
- Missing telemetry is not evidence that no execution/output/consumption occurred.
- A logical pipeline is not assumed identical to one Databricks job or task.
- Reconstructed logical execution retains the evidence supporting lower-level associations.
- Retry/restart/rerun/backfill identity/continuity is not inferred from naming/time alone.
- Effective Lineage or intended dependency order does not prove actual runtime waiting or consumed-version use.
- Deployment active-state does not automatically prove a run's implementation-state facets.
- Latest upstream output is not automatically the output consumed by a downstream run.
- Output existence is independent of terminal execution outcome and remains below publication/current-cycle/freshness/health/readiness claims.
- Event/effective time and record/knowledge time remain distinguishable where late evidence matters.
- Duplicate/common-derived/conflicting source events are not silently flattened when the conclusion would change.
- Execution History does not own Deployment, Observation, Assessment, Lineage, Change Intent, Impact, Causal Claim, or Execution Gate state.

## Ambiguity and missing evidence

Run evidence can be late, duplicated/common-derived, partial, conflicting, unavailable, unauthorized, clock-misaligned, or insufficient for logical assembly/version binding. The concept reports those conditions. If a source cannot establish whether an execution/output/consumption occurred over a period, the history remains incomplete rather than synthesizing a negative fact.

An external gate/control source may say a run was admitted or held while the orchestration source provides incomplete evidence about whether the run actually started. Those states remain separate rather than inferring execution from gate intent.

A long-running execution may span Deployment activation/rollback. Unless runtime binding evidence establishes how code/config/schema/transformation facets were selected, start-time or completion-time active state is not chosen by convenience.

## Synchronizations

- **Entity Identity** supplies pipeline/job/task/execution and data/interface referents.
- **Monitoring Scope** provides monitoring-responsibility context without creating executions.
- **Change Intent** provides planned context that may be relevant to executions after activation but does not create run/version facts.
- **Deployment** supplies active implementation-state intervals; SYN-009/OPS-041 determine whether run-specific association is supportable.
- **Observation** may record measurements/facts about an execution or its produced data; it does not own execution-instance continuity.
- **Expectation** defines expected execution cadence/conditions where normative requirements exist.
- **Assessment** can evaluate execution evidence against expectations without mutating the history.
- **Lineage** represents logical/topological dependencies separately from actual runtime sequence and version consumption.
- **Execution Gate** may hold/admit/override a downstream execution opportunity, but Execution History records the actual run only once execution evidence exists.
- **Change** can use execution timing/version context for realized changes.
- **Impact** may later consume run-specific version encounter evidence when evaluating actual exposure.
- **Investigation** uses execution sequence/version evidence while **Causal Claim** remains the owner of causal propositions.

## Security / privacy / governance considerations

Execution metadata may expose schedules, environment topology, job names, failure details, operational incidents, implementation versions, input/output versions, restricted dependencies, or gate decisions. Authorized abstraction may expose a run outcome or known version relationship without revealing sensitive implementation details.

## Evidence / provenance considerations

Every execution state and run-specific association should retain source, source event time, collection/knowledge time where relevant, subject/execution identity, common-derivation/conflict limitations, and correction history. Logical execution reconstruction must be explainable from underlying evidence. When a gate or Deployment was involved, the run may reference that context without making it the source of execution/version truth.

## Representative scenarios

### Successful run with unhealthy output
A run succeeds. Separate Observations/Assessments later show its output violated completeness. Execution History remains successful; it is not rewritten as a failed run.

### Successful run with output existence unknown
A terminal source establishes success, but no applicable output/version evidence is available. The run remains successful while output existence/version stays unresolved.

### Failed run with material output
A run fails after committing a partial output. Execution History preserves both the failed terminal state and the produced output/version evidence; neither erases the other.

### Expected run did not occur
A freshness/operational Expectation says a run should occur by 06:00. Complete applicable coverage establishes no qualifying run occurred. The negative Observation plus Expectation can produce a violation Assessment; Execution History does not create a phantom failed run.

### Gate-held execution opportunity
C is scheduled for 07:00 but an enabled Execution Gate holds it until A's current output is ready. No C execution instance is created merely because the opportunity existed or was held. If C later starts after admission, that actual start becomes Execution History.

### Gate override without run
An authorized operator overrides a gate, but the scheduler never starts C because of a separate platform issue. Execution Gate records the override; Execution History does not invent a run.

### First run after planned change
A Change Intent is linked to a Deployment activated at 10:00. Ordering evidence identifies the first execution after activation. Run-specific implementation binding remains independently evidenced; `after activation` alone does not prove which composite state the run used.

### Stale upstream version consumed
A new upstream output exists before C starts, but run-specific evidence shows C consumed the prior output. Execution History records the actual version rather than assuming the latest output.

### Cross-job logical execution
One logical pipeline spans several Databricks tasks/jobs. Execution History can represent the logical execution only where association evidence is sufficient; otherwise it preserves partial lower-level executions.

### Retry and rerun
One failed attempt is explicitly retried within a logical execution and later succeeds. A subsequent operator rerun of the same data interval is a separate execution. Earlier failed attempts remain historical.

### Conflicting terminal states
Two sources disagree whether a run was cancelled or failed. The conflict remains visible until accepted evidence/authority semantics resolve it.

### Late reconstruction
A run event arrives after an incident review and establishes an execution that was unknown at the time. Current retrospective reconstruction includes it while the incident-time knowledge cut still shows that the run was not known then.

## Non-goals

- defining schedules or execution Expectations;
- deciding whether a future execution should be admitted/held;
- declaring data-health/readiness status;
- recording Deployment intent;
- root-cause attribution;
- replacing an orchestration system;
- assuming every logical pipeline maps to one job;
- selecting source-specific run/version-attestation or telemetry-normalization implementation.

## Deferred questions

Concrete source support, canonical normalization mappings, source-specific version/consumption evidence, telemetry latency/retention and cost belong to Phase 009. Event/run persistence and reconstruction architecture belong to Phase 010. MVP source/coverage acceptance and exact timing objectives remain later-phase decisions.