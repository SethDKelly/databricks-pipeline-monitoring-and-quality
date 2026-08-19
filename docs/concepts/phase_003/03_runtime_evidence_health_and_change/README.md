# Group 03 — Runtime Evidence, Health & Realized Change

**Status:** Review complete — synchronizations accepted

## Goal

Define how active Deployment context, actual executions, operational timing/dependency evidence, data Observations, time-valid Expectations/Baselines, Assessments, realized Change, analyst handoff, and protective Propagation Safeguard coordination work together without reducing ecosystem health to table-level data-quality statistics.

## Accepted synchronizations

- [`SYN-009 — Active Deployment ↔ Execution Context Association`](009_active_deployment_execution_association.md)
- [`SYN-010 — Execution Lifecycle → Operational Timing Observations`](010_execution_lifecycle_operational_observations.md)
- [`SYN-011 — Operational Dependency Timing → Readiness and Latency Assessment`](011_dependency_timing_readiness_assessment.md)
- [`SYN-012 — Runtime Observation + Time-Valid Reference → Assessment`](012_runtime_observation_reference_assessment.md)
- [`SYN-013 — Runtime Evidence → Realized Change`](013_runtime_evidence_realized_change.md)
- [`SYN-014 — Material Assessment → Investigation Initiation`](014_material_assessment_investigation_initiation.md)
- [`SYN-015 — Runtime Risk Context → Propagation Safeguard`](015_runtime_risk_propagation_safeguard.md)

## Phase 002 boundary reopen

Group 03 exposed one behavior no accepted concept owned: protective hold/quarantine/release of data propagation. Rather than overloading Assessment, Investigation, Impact, or Policy Context, Phase 002 is narrowly reopened through the accepted **Propagation Safeguard** addendum.

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

## Deferred questions

- first-MVP execution timing dimensions and canonical lifecycle normalization;
- exact run-duration/latency Baseline comparison methods and statistical uncertainty;
- explicit response/urgency rules for automatic Investigation initiation;
- safeguard authority, enforcement evidence, lifecycle vocabulary, and implementation candidates;
- whether response prioritization later needs a dedicated normative concept after authority/policy refinement;
- minimum evidence for version-level downstream consumed-state proof;
- significance rules for promoting raw Observation differences into durable Change records.

## Group exit gate

**Satisfied.** Runtime reasoning now covers execution timing, dependency readiness, data health, correct reference context, realized Change, human investigation handoff, and protective propagation control without conflating execution success, DQ, atypicality, causality, or quarantine.

The next group is **Group 04 — Lineage, Investigation & Causal Reasoning**.
