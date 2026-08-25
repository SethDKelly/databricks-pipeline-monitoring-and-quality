# Concept: Execution Gate

**Status:** Accepted — Phase 002 post-exit addendum discovered before Phase 003 Group 06

## Purpose

Let an authorized control integration decide whether a downstream execution opportunity may start, must wait, may be explicitly overridden, or expires based on evidence-backed prerequisite readiness, without turning passive monitoring into a mandatory runtime dependency or conflating readiness, health, scheduling, authorization, and execution history.

## Operational principle

Pipeline C depends on a current qualifying output from upstream pipeline A. A time-based scheduler would normally start C at 07:00 even if A is still running, which can cause C to consume yesterday's state and publish stale results. When an **Execution Gate** is explicitly enabled for C, the gate evaluates the declared prerequisite readiness evidence before C starts. If A's required current output is not yet ready, C is held. When the prerequisite becomes ready, the gate releases/admit the downstream execution. If an authorized operator overrides the gate, the override is recorded without pretending the prerequisite was satisfied.

Execution Gate is optional active control. The monitoring framework's default observation mode remains out-of-band and must not require production jobs to wait for monitoring. Baseline monitoring should prefer platform/source metadata integrations that do not require embedding framework code or workflow steps into every production repository.

## Actors

- Data Engineer / Pipeline Maintainer
- Data Platform Administrator
- Incident responder / authorized operator
- Monitoring framework
- Databricks or another orchestration/control source
- External scheduler/control integration

## State

- gate identity;
- identified downstream pipeline/job/execution target;
- optional execution opportunity, trigger window, or schedule context;
- declared prerequisite dependencies and applicable readiness criteria;
- gate lifecycle/configuration state, such as configured/enabled/disabled/retired;
- current admission state, such as evaluating, ready/admitted, held, overridden, expired/cancelled, unknown, or conflicting;
- readiness evidence references for each prerequisite;
- explicit fallback/timeout/override policy reference where configured;
- authorizing actor/source and Capability Authorization context;
- hold/release/override reason and provenance;
- effective/event time and recorded/knowledge time;
- correction/supersession history;
- visibility/security context.

## Actions

### `register`
Records that a downstream execution target is subject to a named gate and declared prerequisite/readiness criteria. Registration does not itself block anything unless an accepted control integration makes the gate effective.

### `evaluate`
Resolves prerequisite readiness from the applicable Lineage, Execution History, Observation, Expectation, Assessment, and other allowed evidence. The result may be ready, not ready, unknown, conflicting, unavailable, or unauthorized.

### `hold`
Records/establishes that the downstream execution is not admitted while the applicable gate condition requires waiting. Active hold requires explicit configured authority/control semantics; a readiness Assessment alone does not create an active hold.

### `admit`
Records/establishes that the downstream execution is permitted to proceed because the gate's declared admission condition is satisfied.

### `override`
Records an authorized bypass of the normal readiness result for the specific context. Override does not transform `not ready` or `unknown` into `ready`; it records that execution was allowed despite that state.

### `retire`
Ends the applicability of a gate configuration prospectively while preserving history.

### `resolveAt`
Returns the gate configuration/admission state for a downstream target and relevant time/context with provenance and ambiguity.

## Invariants / behavioral expectations

- Passive monitoring is not an Execution Gate and must not become a production critical-path dependency merely because monitoring exists.
- A gate is opt-in active control. No Lineage edge or readiness Assessment silently creates a gate.
- Execution Gate readiness/admission state is not Execution History. Execution History records what actually ran after admission/override.
- `held` is not an execution failure because the execution may not have started.
- `admitted` does not prove the upstream data is healthy beyond the gate's explicit prerequisite criteria.
- `override` does not prove readiness and must preserve the unmet/unknown condition.
- A successful upstream run does not automatically satisfy every gate; the declared criterion may require current-cycle output availability, freshness, version, or another explicit readiness condition.
- Missing readiness evidence is not automatically `ready`. Each enabled gate must have explicit behavior for unknown/unavailable evidence rather than inheriting a universal fail-open or fail-closed assumption.
- Gate-induced waiting/delay is operationally observable and may itself violate completion/delivery Expectations.
- Capability Authorization for configuring, overriding, or operating a gate is separate from raw-data access and from ordinary analytical visibility.
- Gate configuration must not silently propagate across environments, consumers, or downstream targets.
- Current gate configuration must not be projected backward into historical execution decisions.
- Execution Gate does not select scheduler/orchestrator technology and does not require production repository modification as a concept-level assumption.

## Ambiguity and missing evidence

A gate can know that a prerequisite relationship exists while lacking enough evidence to determine current readiness. That state remains `unknown`/`unavailable` unless the configured gate policy explicitly defines how such a state is handled. Conflicting upstream state, restricted dependencies, late telemetry, or uncertain current-output identity remain visible.

An external scheduler may report that a gate decision was requested but not prove that the downstream start was actually blocked or released. Requested decision and enforced admission state remain distinguishable where evidence requires it.

## Synchronizations

- **Lineage** supplies the historical operational/data dependency set relevant to the downstream execution.
- **Execution History** and **Observation** supply actual upstream execution/output timing and availability facts.
- **Expectation** may define normative readiness/freshness/completion requirements.
- **Assessment** can state whether prerequisite evidence satisfies or violates those requirements; it does not activate the gate by itself.
- **Capability Authorization** determines whether a principal/control source may register, enable, override, or otherwise operate a gate.
- **Execution History** later records whether a downstream execution actually occurred after admission/override.
- **Propagation Safeguard** remains separate: it protects output/consumption propagation, while Execution Gate controls whether a downstream execution starts.
- **Impact**, **Observation**, and **Assessment** can represent delays/non-delivery caused by an active gate.
- **Causal Claim** owns any proposition that the gate or upstream readiness condition caused a downstream operational consequence.
- **Explanation** may state that a run was intentionally held/released/overridden when authorized.

## Security / privacy / governance considerations

Gate configuration can reveal sensitive dependencies, schedules, client-delivery paths, or control policy. Visibility and operational authority are separately governed. An analyst may be allowed to see that a downstream run is waiting on a restricted prerequisite without seeing the upstream identity or raw data.

## Evidence / provenance considerations

Gate decisions retain the target, prerequisite set, readiness criteria, evidence basis, authority, decision/action, effective time, record time, fallback/override context, and correction history. Historical replay must distinguish what readiness evidence existed at the decision time from evidence learned later.

## Representative scenarios

### Upstream not ready
A is still running when C's scheduled window arrives. The enabled gate holds C until the qualifying current A output becomes available, preventing C from blindly recomputing against yesterday's state.

### Ready and admitted
A completes and its required current output is evidenced before C starts. The gate admits C. C's actual run is still separately recorded by Execution History.

### Unknown readiness
The monitoring/control source cannot establish whether A produced the required current output. The gate follows its explicitly configured unknown-evidence behavior; the framework does not invent a universal fail-open/fail-closed rule.

### Authorized override
A dependency is known late, but an authorized operator decides C should run anyway for a documented operational reason. The gate records `override`; A remains not-ready and subsequent stale/quality consequences remain observable.

### Passive monitoring only
No Execution Gate is enabled. The framework observes that C started before A was ready and reports readiness/freshness risk without delaying C.

### Gate causes delivery delay
Holding C prevents stale recomputation but causes a client delivery deadline to be missed. The prevention and the latency consequence are both represented; neither hides the other.

## Non-goals

- replacing Databricks or another scheduler/orchestrator;
- requiring every production pipeline to be gated;
- making the monitoring framework a mandatory production dependency;
- selecting a control-plane implementation;
- embedding framework code into every ETL repository;
- deciding all prerequisite/readiness policies;
- data-quality Assessment;
- Propagation Safeguard/quarantine state;
- causal attribution;
- automatic rollback.

## Deferred questions

- minimum gate lifecycle/admission vocabulary for MVP;
- which dependency/readiness criteria are safe for automatic gating;
- authoritative source for active gate configuration;
- explicit fail-open/fail-closed/hold/escalate behavior by gate class when evidence/control integration is unavailable;
- maximum wait, timeout, escalation, and override semantics;
- whether scheduling opportunities need first-class identity beyond target + expected window;
- how gate control can be realized with minimal or zero production-repository changes;
- whether Databricks-native task/job dependencies, external orchestration, or another mechanism best realizes accepted semantics later;
- audit and recovery behavior when a control integration itself is degraded.

## Later refinement — Phase 007 Group 08

Phase 007 Group 08 accepts OPS-105–OPS-123 and sharpens this concept without changing its ownership.

- Every Gate proposition binds exact configuration/profile revision, downstream target/environment, execution opportunity/cycle/window, criterion profile, decision/evaluation time and knowledge cut.
- Gate configuration/enabled state is distinct from opportunity-specific decision state.
- Descriptive Gate-family labels never replace exact criterion logic. Multi-prerequisite membership/composition is explicit rather than inferred from Lineage fan-in.
- Phase 006 health/result evidence participates only through exact-use suitability and explicit criterion membership: **health outcome ≠ evidence suitability ≠ readiness ≠ Gate decision ≠ enforcement ≠ execution**.
- Normal `hold`/`admit` decisions remain distinct from `override`, timeout/fallback and escalation bases.
- `override` is an AUTH-036-governed opportunity-specific exception; it preserves the underlying `not ready`/`unknown`/`conflicting`/`unavailable` result.
- Fallback is pre-authorized policy behavior for a declared trigger and remains separate from override. `configured fallback ≠ trigger occurred ≠ fallback applied ≠ action enforced`.
- Decision issuance, delivery, acknowledgement/acceptance and effective Gate enforcement are separately evidenced under REF-025/026.
- HOLD enforcement is contradicted by reliable downstream start during an applicable unsuperseded hold. Conversely, no run proves HOLD only with sufficient opportunity/Execution History coverage.
- ADMIT means this Gate barrier was removed; it does not prove a run occurred or that the Gate caused execution.
- A prerequisite becoming ready does not automatically ADMIT a held opportunity unless explicit control semantics establish automatic reevaluation/action.
- Timeout, opportunity expiry, SLA deadline and cancellation remain different facts. An expired/cancelled opportunity with no started run is not an execution failure.
- Escalation does not itself HOLD/ADMIT unless a separate explicit Gate action follows.
- Missing/conflicting control telemetry does not prove fail-open/fail-closed or fallback behavior, and control restoration does not automatically reevaluate/admit.
- Multiple Gates applying to one opportunity keep independent barriers; no universal `most restrictive wins`, source precedence or Gate-effectiveness score is accepted.
- Execution Gate and Propagation Safeguard remain independent: Gate HOLD does not protect published state, ADMIT does not release a Safeguard, and Safeguard release does not ADMIT a held execution.
- Gate-induced delay, skipped cycle, stale prior-state use and non-delivery remain source-owned Execution/Observation/Assessment/Impact evidence. Broader control-effect attribution remains Causal Claim under REF-013–REF-020/REF-030.
- Historical Gate configuration/readiness/decision/enforcement/execution replay is bitemporal and non-rewriting.

See [`../phase_007/08_execution_gate_fallback_override_control_effects/README.md`](../phase_007/08_execution_gate_fallback_override_control_effects/README.md) for the accepted refinement.
