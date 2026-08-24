# SYN-032 — Dependency Readiness Evidence → Execution Gate Admission

**Status:** Accepted — Phase 003 Group 03 extension discovered before Group 06

## Outcome

Allow an explicitly enabled downstream Execution Gate to admit or hold a downstream execution opportunity based on evidence-backed prerequisite readiness, while keeping passive monitoring non-blocking and preserving the distinction among readiness, freshness, health, authorization, gate state, and actual execution.

## Participating concepts and actions

- **Execution Gate** — `register`, `evaluate`, `hold`, `admit`, `override`, `resolveAt`.
- **Lineage** — `traverseAt` for applicable operational/data prerequisites.
- **Execution History** — `resolveAt` for actual upstream/downstream runs.
- **Observation** — upstream completion/output/currentness facts.
- **Expectation** — `resolveApplicable` for explicit readiness/freshness/completion requirements.
- **Assessment** — `assess` for readiness criteria where interpretation is required.
- **Capability Authorization** — `resolveFor` for gate operation/override authority.

## Trigger / initiating condition

A downstream execution opportunity approaches while an explicit Execution Gate is active for that downstream subject/context.

The existence of a dependency, schedule, or monitoring Assessment by itself does not activate gating.

## Preconditions

- the downstream target is identified;
- an applicable gate configuration exists and is enabled;
- prerequisite relationships and readiness criteria are explicitly resolvable enough to evaluate;
- authority for gate operation/override is defined where required.

## Coordination semantics

1. Resolve whether an Execution Gate is applicable for the downstream target, environment, and execution window.
2. If no gate applies, monitoring remains observational and does not delay the execution.
3. If a gate applies, resolve the historical prerequisite dependency set from Lineage.
4. Resolve the explicit readiness criteria for each prerequisite. Criteria may require, for example, qualifying upstream completion, current-cycle output availability, freshness, or another accepted condition; successful execution alone is not assumed sufficient unless the criterion says so.
5. Gather Execution History/Observation evidence and derive any required readiness Assessment.
6. Execution Gate `evaluate` returns ready, not ready, unknown, conflicting, unavailable, or unauthorized for the relevant decision context.
7. When the configured admission rule is satisfied, `admit` permits the downstream execution to proceed.
8. When the rule requires waiting, `hold` prevents admission until release/admission criteria are met, timeout/expiry semantics apply, or an authorized override occurs.
9. `override` requires independent Capability Authorization and records the bypass without rewriting the underlying readiness result.
10. Once an execution actually starts, Execution History records the real run independently of the gate decision.
11. Gate wait duration, missed start/completion windows, or downstream delivery delay become separate runtime Observations/Assessments.
12. If the gate/control evidence is unavailable, behavior follows the explicitly configured fallback for that gate class; no universal fail-open/fail-closed behavior is inferred.

## State and evidence effects

Execution Gate owns gate configuration/admission lifecycle. Lineage owns dependencies; Execution History owns actual runs; Observation owns measured facts; Expectation owns normative criteria; Assessment owns health/readiness interpretation; Capability Authorization owns permission.

The synchronization creates no hidden scheduler, workflow, or orchestration state.

## Ambiguity / failure propagation

Unknown readiness stays unknown unless the gate's explicit fallback semantics map that state to a control outcome. Missing telemetry is not readiness. Restricted prerequisite detail can remain opaque while still supporting an authorized `waiting on prerequisite` result where sufficient safe evidence exists.

Requested admission/hold and actual enforcement may differ when enforcement is external. The system must preserve that distinction when evidence does not prove enforcement.

## Temporal semantics

Dependencies, gate configuration, readiness criteria, evidence, decision, hold/admission/override, and actual execution resolve for the relevant event time. Later evidence may revise retrospective understanding without rewriting what the control plane knew when it acted.

## Provenance / traceability

Every gate decision links to applicable gate configuration, prerequisite relationships, readiness criteria, evidence/Assessment basis, authorization, fallback/override context, and decision time.

## Security / authorization

Gate-operation and override authority are separate from raw-data access, analytical visibility, responsibility, and ordinary job metadata access. Restricted upstream identity/details may be abstracted.

## Invariants

- passive monitoring ≠ active execution gating;
- dependency relationship ≠ enabled gate;
- readiness Assessment ≠ gate hold/admission;
- held execution opportunity ≠ failed execution;
- admitted ≠ actual execution occurred;
- admitted ≠ every upstream health dimension is healthy;
- override ≠ prerequisite ready;
- successful upstream run ≠ current qualifying output unless criterion establishes it;
- missing evidence ≠ ready;
- gate-induced delay remains health/Impact evidence;
- Execution Gate ≠ Propagation Safeguard;
- no universal fail-open/fail-closed rule is invented.

## Scenarios

### E-21 — Dependency gate prevents stale downstream run
A has not produced the current required output when C's scheduled window arrives. C is held. A later produces the qualifying output; the gate admits C. C avoids blindly consuming the older state.

### Passive comparison
The same dependency has no enabled gate. C starts on schedule; monitoring records that A was not ready and later assesses freshness/staleness as evidence permits. The framework does not delay production.

### Unknown readiness
Telemetry needed to prove the current upstream output is unavailable. The enabled gate follows its explicitly configured unknown-evidence behavior rather than assuming readiness.

### Authorized override
An operator with gate-override capability admits C despite the prerequisite remaining not ready. The underlying condition remains visible and any resulting stale-data consequence is assessed independently.

### E-22 — Gate/control degradation and production continuity
The passive monitoring service is degraded. Ungated production jobs continue unaffected. For an explicitly gated job, the gate's predefined unavailable-control fallback governs whether it waits, proceeds, or escalates; the framework does not silently invent a fallback at runtime.

## Non-goals

- selecting Databricks Workflows, an external scheduler, or another orchestration mechanism;
- requiring production repository/GitHub Actions changes;
- enabling gates for all pipelines;
- replacing Propagation Safeguard;
- deciding organization-wide gate policy;
- causal attribution;
- automatic rollback.

## Deferred questions

- minimum readiness criteria and gate classes for MVP;
- explicit timeout/fallback/override semantics;
- evidence needed to prove actual external enforcement;
- how to realize gates with minimal or zero production-code/repository changes;
- gate availability/latency SLOs if gating becomes production-critical;
- whether gate policy itself needs additional structured authority semantics later.
