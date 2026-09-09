# Group 03 — Runtime Evidence, Health & Realized Change

**Status:** Review complete — synchronizations accepted; later Execution Gate extension accepted before Group 06

## Goal

Define how active Deployment context, actual executions, operational timing/dependency evidence, data Observations, time-valid Expectations/Baselines, Assessments, realized Change, analyst handoff, protective Propagation Safeguard coordination, and optional dependency-aware execution gating work together without reducing ecosystem health to table-level data-quality statistics or making passive monitoring a universal production dependency.

## Accepted synchronizations

- [`SYN-009 — Active Deployment ↔ Execution Context Association`](009_active_deployment_execution_association.md)
- [`SYN-010 — Execution Lifecycle → Operational Timing Observations`](010_execution_lifecycle_operational_observations.md)
- [`SYN-011 — Operational Dependency Timing → Readiness and Latency Assessment`](011_dependency_timing_readiness_assessment.md)
- [`SYN-012 — Runtime Observation + Time-Valid Reference → Assessment`](012_runtime_observation_reference_assessment.md)
- [`SYN-013 — Runtime Evidence → Realized Change`](013_runtime_evidence_realized_change.md)
- [`SYN-014 — Material Assessment → Investigation Initiation`](014_material_assessment_investigation_initiation.md)
- [`SYN-015 — Runtime Risk Context → Propagation Safeguard`](015_runtime_risk_propagation_safeguard.md)
- [`SYN-032 — Dependency Readiness Evidence → Execution Gate Admission`](032_dependency_readiness_execution_gate.md) — accepted later as a Group 03 extension before Phase 003 Group 06.

## Phase 002 boundary reopens

Group 03 originally exposed one behavior no accepted concept owned: protective hold/quarantine/release of data propagation. Rather than overloading Assessment, Investigation, Impact, or Policy Context, Phase 002 was narrowly reopened through the accepted **Propagation Safeguard** addendum.

Later, after Group 05, dependency-readiness control exposed a second runtime-control behavior that neither Execution History, Assessment, nor Propagation Safeguard owns cleanly: whether a downstream execution opportunity itself may start or must wait. Phase 002 was therefore narrowly reopened again through the accepted **Execution Gate** addendum, and Group 03 gained SYN-032 as an explicit active-control extension.

Analyst research does not need another concept: Investigation already owns bounded human/system inquiry. Exact automatic escalation/notification policy remains deferred rather than becoming hidden synchronization logic.

## Boundary decisions

### 1. Ecosystem health includes operational timing
Run duration, start/completion timing, queue/wait behavior, dependency latency, and delivery readiness are first-class operational Observations/Assessments. A run can succeed while being too slow; data can be statistically valid while arriving too late to be useful.

### 2. Execution success, timeliness, freshness, and data quality remain separate
A successful downstream run can consume stale state or miss a client deadline. One dimension never masks another.

### 3. Dependency delay requires historical topology plus timing evidence
Operational/data Lineage identifies the relevant dependency path. Execution/Observation evidence establishes actual timing. A delayed upstream is not automatically the cause of downstream degradation, and downstream success does not prove current upstream data was consumed.

### 4. Missing output requires coverage-bearing absence evidence
No telemetry is not `no output`. If authoritative coverage establishes that no qualifying output/run occurred, the absence can be assessed normatively. Where nothing was produced, protective response can hold downstream advancement rather than fabricate a quarantined object.

### 5. Group 02 reference transitions govern runtime comparison
Every runtime Assessment resolves the correct time-valid Expectation/Baseline context. Post-change runs cannot be compared with a superseded/non-comparable Baseline merely because it is the newest stored reference.

### 6. Ordinary variation does not become alert noise
Baselines describe expected empirical variation. Raw run-to-run difference is not automatically Change, atypicality, degradation, or an intervention trigger. Exact statistical/significance methods remain later refinement.

### 7. Analysts remain first-class investigators
A durable Assessment may be investigated manually even if causality is insufficient or no normative criterion exists. Automatic Investigation initiation requires an explicit later-accepted response rule; Baseline atypicality alone does not mandate intervention.

### 8. Propagation Safeguard is separate protective truth
Assessment may motivate a safeguard but cannot activate one automatically. Proposed versus active protection, placement, authority/enforcement evidence, and release history are explicit.

### 9. Quarantine placement is contextual
The right protective boundary may be the originating output, an environment/cohort, a downstream publication edge, or a particular client/consumer. Lineage and Impact inform the choice; they do not decide it automatically.

### 10. Safeguards can create their own health effects
Holding suspect data may be correct while causing latency/non-delivery. Those operational consequences remain observable and assessable rather than being hidden because the safeguard was intentional.

### 11. Passive monitoring is non-blocking by default
SYN-011 remains observational. It can determine that an upstream dependency was not ready when a downstream execution started without blocking that execution. Monitoring or framework degradation must not become a production delay merely because monitoring exists.

### 12. Execution gating is explicit opt-in control
SYN-032 applies only when an explicit Execution Gate is enabled for the downstream subject/context. Lineage, schedules, and readiness Assessments do not automatically create control state.

### 13. Readiness criteria are stronger than clock ordering
A gate may require more than `upstream job ran`. Depending on its explicit criterion, a qualifying prerequisite may require current-cycle output availability, freshness, expected version, or another accepted readiness condition. A successful upstream run does not silently prove current usable data.

### 14. Gate hold/admission remains separate from actual execution
A held execution opportunity has not necessarily failed because it may not have started. Admission does not prove the downstream run actually occurred. Execution History remains the owner of actual run evidence.

### 15. Execution Gate and Propagation Safeguard protect different boundaries
Execution Gate controls downstream start admission. Propagation Safeguard controls output/consumption propagation. A gate may prevent stale recomputation before execution; a safeguard may protect consumers after output exists or hold publication/consumption when output is missing/suspect.

### 16. Gate-induced delay is itself health evidence
Waiting on a prerequisite can be correct while separately causing start/completion/client-delivery delay. That delay remains observable/assessable and may participate in Impact/Causal Claim reasoning.

### 17. Unknown gate evidence requires explicit fallback semantics
Missing readiness or control evidence is not automatically `ready`. The framework does not invent one universal fail-open/fail-closed policy; enabled gates require explicit unavailable/unknown behavior, timeout/escalation, and override semantics in later refinement.

## Scenario review

### E-01 — A+B→C unplanned degradation
Pass. Runtime Observations/Assessments identify C's condition; meaningful before/after evidence can become Change; analysts can open Investigation without a forced cause.

### E-03 — Planned change with unintended violation
Pass. The post-change volume can satisfy its revised Expectation while completeness independently violates another Expectation; both survive the runtime chain.

### E-05 — Stale upstream with successful downstream execution
Pass. Execution success, upstream readiness/freshness, consumed-state evidence, and downstream health remain distinct.

### E-06 — Deployment-correlated shift
Pass. Execution can be associated with an active Deployment while causal interpretation remains deferred to Causal Claim.

### E-10 — Historical correction
Pass. Late run/activation/Observation/reference evidence creates corrected/reassessed history without rewriting the contemporaneous view.

### E-11 — Long-running upstream threatens delivery
Pass. Run duration is an Observation, may be atypical versus Baseline and/or violate a duration/completion Expectation, and can create downstream readiness risk even when the job ultimately succeeds.

### E-12 — Missing output and protective hold
Pass. Sufficient absence evidence can establish a missing-output violation. A downstream boundary may be held without claiming a nonexistent output was quarantined.

### E-13 — Ordinary variation needs no intervention
Pass. Small run-to-run movement inside a comparable Baseline does not generate a material Change or Investigation merely because the number changed.

### E-14 — Material atypicality with analyst research
Pass. A client-critical table may be materially atypical without a normative volume Expectation; an analyst can open Investigation while the Assessment remains comparative rather than being mislabeled failure.

### E-15 — Safeguard creates delivery delay
Pass. Quarantine can protect consumers while independently causing a delivery-latency Assessment; both are valid and explainable.

### E-21 — Dependency gate prevents stale downstream run
Pass after extension. A current upstream prerequisite is not ready at C's schedule time; the enabled gate holds C. When qualifying readiness evidence arrives, C is admitted. The held interval remains distinct from an execution failure.

### E-22 — Gate/control degradation and production continuity
Pass after extension. Passive/ungated jobs are unaffected by monitoring degradation. Explicitly gated jobs follow their configured unavailable-control behavior rather than inheriting a hidden global fail-open/fail-closed rule.

## Deferred questions

- first-MVP execution timing dimensions and canonical lifecycle normalization;
- exact run-duration/latency Baseline comparison methods and statistical uncertainty;
- explicit response/urgency rules for automatic Investigation initiation;
- safeguard authority, enforcement evidence, lifecycle vocabulary, and implementation candidates;
- minimum evidence for version-level downstream consumed-state proof;
- significance rules for promoting raw Observation differences into durable Change records;
- minimum Execution Gate readiness criteria and lifecycle vocabulary;
- explicit gate timeout/fallback/escalation/override policies;
- evidence required to prove external gate enforcement;
- gate availability/latency requirements if a gate becomes production-critical;
- how to realize dependency gating with minimal or zero production-repository changes.

## Group exit gate

**Satisfied, including the later SYN-032 extension.** Runtime reasoning now covers execution timing, dependency readiness, data health, correct reference context, realized Change, human investigation handoff, protective propagation control, and optional dependency-aware start admission without conflating execution success, DQ, atypicality, causality, quarantine, or passive monitoring with mandatory control.

Groups 04–05 remain accepted. **Group 06 — Historical Replay & Phase 003 Consolidation is next and has not started.**
