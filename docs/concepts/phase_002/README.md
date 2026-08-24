# Phase 002 — Concept Specifications

**Status:** **Complete — Groups 01–05 accepted; three explicit post-exit addenda accepted during Phase 003.**

## Purpose

Phase 002 turned the Phase 001 discovery catalog into explicit, implementation-neutral Concept Design specifications. The concepts define product behavior and truth boundaries without mapping them to services, schemas, APIs, Databricks objects, graph databases, ledger/event-store technologies, IAM schemes, orchestration products, language/framework choices, or vendor products.

The original Phase 002 review completed with 20 concepts. Later Phase 003 work exposed three independently motivated behaviors that could not be cleanly owned by those concepts. Phase 002 was therefore narrowly reopened through explicit addenda while preserving the original exit as historical truth.

## Accepted concept groups

| Group | Theme | Accepted concepts | Status |
|---|---|---|---|
| 01 | Scope & Identity | Monitoring Scope, Entity Identity | **Accepted** |
| 02 | Semantics, Governance & Policy | Semantic Definition, Responsibility Assignment, Classification, Policy Context | **Accepted** |
| 03 | Health Evaluation | Expectation, Baseline, Observation, Assessment | **Accepted** |
| 04 | History, Lineage & Change | Change Intent, Execution History, Deployment, Lineage, Change | **Accepted** |
| 05 | Investigation, Impact & Explanation | Investigation, Causal Claim, Impact, Annotation, Explanation | **Accepted** |

## Accepted post-exit addenda

- **Propagation Safeguard** — protective proposed/active/released hold or quarantine state for a defined data output, execution context, propagation boundary, environment/cohort, or consumer set. It does not own health Assessment, Investigation, causal truth, authorization, or implementation enforcement mechanics.
- **Capability Authorization** — provenance-bearing resolution of whether a principal may perform a named capability on a subject/context/time. It separates raw-data read, metadata/health visibility, Lineage/RCA participation, operational job authority, safeguard authority, and other capability categories without selecting an IAM/enforcement implementation.
- **Execution Gate** — optional active control over whether a downstream execution opportunity is admitted, held, admitted after readiness, expired/cancelled, or explicitly overridden based on declared prerequisite readiness evidence. It remains separate from passive monitoring, Execution History, Assessment, Capability Authorization, and Propagation Safeguard.

**23 concepts are currently accepted.**

Review order was a design dependency, not an implementation dependency. Concepts remain independently motivated and compose through synchronizations.

## Accepted boundary refinements

### Group 01
- Monitoring Scope is monitoring responsibility, not authorization.
- Entity Identity is ecosystem-wide and distinct from replacement/succession.

### Group 02
- Semantic Definition is facet/context/provenance/time-aware.
- Responsibility Assignment replaces overloaded Ownership and is not universal authority or authorization.
- Classification is categorical metadata, separate from Policy Context, authorization, and compliance.
- Synchronization order never silently becomes governance authority.

### Group 03
- Expectation is normative; Baseline is descriptive.
- Observation is provenance-bearing fact; Assessment is interpretation against explicit normative/comparative basis.
- Missing telemetry is not observed absence.
- Typical is not automatically healthy; atypical is not automatically degraded.
- Health is dimension-scoped by default.

### Group 04
- Change Intent is separate from realized Change.
- Deployment attempt/activation/active state/supersession are distinct from intended effect.
- Planned values never become empirical Baselines.
- Lineage is typed, directed, temporal, provenance-bearing, graph-compatible, and not causal proof.
- Material history follows ledger-like append/supersede/correction semantics.

### Group 05
- Investigation organizes inquiry; Causal Claim owns causal propositions.
- Correlation, Lineage, Deployment timing, realized Change, and intent consistency cannot silently become confirmed causation.
- Impact separates reachability, exposure, observed effect, and business consequence.
- Annotation is attributed context rather than a catch-all truth mechanism.
- Explanation is authorization/time-aware communication over source concept state and does not become an independent truth source.

### Post-exit addendum — Propagation Safeguard
- Protective propagation state could not be owned by Assessment, Investigation, Impact, or Policy Context.
- A violated Expectation or Baseline atypicality can motivate safeguard review but does not automatically activate quarantine.
- `proposed` ≠ `active`; quarantine ≠ proof of defect; release ≠ proof of health.
- Missing output is not represented as a quarantined object; downstream advancement may be held instead.

### Post-exit addendum — Capability Authorization
- The model repeatedly relied on an `authorized evidence view`, but no concept owned whether a principal may perform a named capability on a subject/context/time.
- Raw-data read authorization, metadata/governance visibility, derived health/metric visibility, Lineage/RCA participation, job/run operational control, and safeguard authority are independent capability categories.
- Denial of raw-data access does not automatically prohibit approved monitoring or RCA.
- Permission to operate/update a job does not grant raw-data read access; analysis permission does not grant production-control authority.
- Responsibility Assignment, Classification, Policy Context, and Monitoring Scope remain separate from authorization.
- Derived evidence can itself be sensitive and remains subject to its own authorized projection.

### Post-exit addendum — Execution Gate
- SYN-011 can assess upstream dependency readiness but explicitly does not own scheduler blocking; Execution History records actual runs; Propagation Safeguard protects output/consumption rather than downstream start admission.
- Execution Gate therefore owns explicit downstream execution admission/hold/admit/override state for enabled dependency-readiness control.
- Passive monitoring remains non-blocking by default; no dependency or readiness Assessment silently creates a gate.
- A gate may require current-cycle output availability/freshness/version or another explicit readiness criterion rather than only successful upstream execution.
- `held` ≠ execution failure; `admitted` ≠ execution occurred; `override` ≠ prerequisite ready.
- Gate-induced delay remains observable/assessable and can create downstream Impact.
- Unknown/unavailable gate evidence requires explicit fallback semantics; no universal fail-open/fail-closed rule is assumed.

## Cross-cutting distinctions accepted by the current model

- Monitoring Scope ≠ ecosystem existence ≠ Capability Authorization;
- Entity Identity ≠ name ≠ replacement/succession;
- Semantic Definition ≠ Responsibility Assignment;
- Responsibility Assignment ≠ universal authority ≠ Capability Authorization;
- Classification ≠ Policy Context ≠ Capability Authorization ≠ compliance;
- raw-data read authorization ≠ metadata/health-analysis authorization ≠ Lineage/RCA authorization ≠ job-operation authorization ≠ safeguard/gate authority;
- passive monitoring ≠ active execution gating;
- dependency readiness Assessment ≠ Execution Gate admission state;
- Execution Gate ≠ Execution History ≠ Propagation Safeguard;
- held execution opportunity ≠ failed execution;
- gate admission ≠ actual run occurrence;
- gate override ≠ readiness;
- Expectation ≠ Baseline;
- normative requirement ≠ historical regularity;
- Observation ≠ Assessment;
- missing evidence ≠ observed absence;
- typical ≠ healthy;
- atypical ≠ degraded/defective;
- Change Intent ≠ Deployment ≠ realized Change;
- successful execution ≠ timely execution ≠ freshness ≠ data quality;
- planned topology ≠ active Lineage;
- Lineage reachability/evidence candidate ≠ cause;
- first-observed localization ≠ root cause;
- Causal Claim ≠ confirmed cause;
- Investigation closure ≠ confirmation;
- Impact candidate ≠ exposure ≠ downstream effect ≠ business consequence;
- downstream consequence ≠ causal attribution;
- criticality/policy sensitivity ≠ actual Impact evidence;
- Propagation Safeguard ≠ health or causal truth;
- safeguard proposal ≠ active safeguard;
- quarantine ≠ proof of defect;
- release ≠ proof of health;
- Annotation ≠ structured operational truth;
- Explanation ≠ independent truth source;
- effective/event time ≠ recorded/knowledge time.

## Scenario implications of the addenda and Phase 003 synchronizations

### Protective hold/quarantine
A suspect or missing output can be protected at an explicit propagation boundary without rewriting the underlying Observation/Assessment or claiming defect/cause. Protected interval, authority, enforcement evidence, release, and safeguard-induced delay remain historical facts.

### Restricted-data analyst
A user may be denied direct Table C rows while being permitted approved aggregate health metrics, runtime/freshness Assessments, redacted Lineage, policy/restriction summaries, responsibility context, Investigation/Causal Claim state, and Impact/safeguard context. RCA remains possible over the authorized evidence view without smuggling restricted data into summaries.

### Job operator without raw-data read
A user may hold an explicit job/run operational capability while lacking permission to inspect the data the job processes. The action's actual outcome remains owned by Deployment/Execution History/Observation rather than being implied by permission.

### Layered downstream Impact
A downstream report can be reachable without exposure, exposed without observed degradation, affected with business consequence still unknown, or protected from a suspect version while becoming late. Causal attribution from the origin to any downstream outcome remains explicit Causal Claim.

### Dependency-gated downstream execution
A downstream pipeline normally scheduled at 07:00 depends on a current upstream output. With no gate enabled, monitoring reports if it starts too early but does not delay it. With an explicit Execution Gate enabled, the downstream execution can be held until the declared readiness condition is met or an explicit fallback/override applies. Gate waiting remains separate operational health evidence.

## Phase 002 exit review and later boundary corrections

D-030 records that the original Phase 002 exit gate was satisfied with 20 concepts. That decision remains historically correct. Later requirements were added explicitly rather than silently overloading accepted concept purposes.

The current model still satisfies the original exit principles: each retained concept/addendum has a singular purpose; state/actions remain implementation-independent; ambiguity/evidence/security/temporal behavior are explicit; and no concept semantically requires DQX, Metric Views, Collibra, Immuta, GitHub Actions, a graph database, event store, quarantine mechanism, IAM model, scheduler/orchestrator, or selected architecture.

## Current synchronization direction

Phase 003 composes all 23 concepts. **Groups 01–05 are accepted; SYN-032 is accepted as a later Group 03 execution-control extension; Group 06 — Historical Replay & Phase 003 Consolidation is next and has not started.** See [`../phase_003/README.md`](../phase_003/README.md).
