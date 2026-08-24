# Concept Catalog

## Status

**23 concepts are Accepted.** Phase 002 originally exited with 20 accepted concepts. Later Phase 003 work exposed three missing independent behaviors: **Propagation Safeguard**, **Capability Authorization**, and **Execution Gate**, each accepted through a narrow post-exit addendum.

The project uses Concept Design to define independently understandable units of functionality. Concepts remain implementation-neutral and synchronize rather than collapse into vendor, service, storage, schema, IAM, orchestration, temporal-replay, or UI boundaries.

Use [`concept_template.md`](concept_template.md) as the specification checklist. The original review and later addenda are in [`phase_002/README.md`](phase_002/README.md) and [`phase_002/addenda/`](phase_002/addenda/).

## Accepted concepts

### Group 01 — Scope & Identity
- [`Monitoring Scope`](phase_002/01_scope_and_identity/monitoring_scope.md) — time-aware monitoring responsibility for identified entities without implicit propagation or access grant.
- [`Entity Identity`](phase_002/01_scope_and_identity/entity_identity.md) — cross-source/time sameness and separation with ambiguity/correction provenance.

### Group 02 — Semantics, Governance & Policy
- [`Semantic Definition`](phase_002/02_semantics_governance_policy/semantic_definition.md) — facet/context-aware meaning and interpretation.
- [`Responsibility Assignment`](phase_002/02_semantics_governance_policy/responsibility_assignment.md) — named responsibility assignments without universal authority implication.
- [`Classification`](phase_002/02_semantics_governance_policy/classification.md) — category membership in a named governance/sensitivity vocabulary.
- [`Policy Context`](phase_002/02_semantics_governance_policy/policy_context.md) — declared policy/handling applicability without enforcement/compliance claims.

### Group 03 — Health Evaluation
- [`Expectation`](phase_002/03_health_evaluation/expectation.md) — normative criteria for acceptable behavior.
- [`Baseline`](phase_002/03_health_evaluation/baseline.md) — descriptive reference behavior from comparable evidence.
- [`Observation`](phase_002/03_health_evaluation/observation.md) — provenance-bearing measured/retrieved facts.
- [`Assessment`](phase_002/03_health_evaluation/assessment.md) — dimension-scoped interpretation against explicit Expectation/Baseline basis.

### Group 04 — History, Lineage & Change
- [`Change Intent`](phase_002/04_history_lineage_change/change_intent.md) — registered intended modification and anticipated effects before realization.
- [`Execution History`](phase_002/04_history_lineage_change/execution_history.md) — actual execution-instance lifecycle history.
- [`Deployment`](phase_002/04_history_lineage_change/deployment.md) — deployment attempt/activation/active-state/supersession history.
- [`Lineage`](phase_002/04_history_lineage_change/lineage.md) — typed, directed, temporal, provenance-bearing relationships and historical traversal.
- [`Change`](phase_002/04_history_lineage_change/change.md) — realized differences/state transitions without health or causal judgment.

### Group 05 — Investigation, Impact & Explanation
- [`Investigation`](phase_002/05_investigation_impact_explanation/investigation.md) — bounded inquiry that organizes evidence, claims, impact, and context without owning truth.
- [`Causal Claim`](phase_002/05_investigation_impact_explanation/causal_claim.md) — explicit causal proposition with epistemic status and supporting/contradicting evidence.
- [`Impact`](phase_002/05_investigation_impact_explanation/impact.md) — downstream reachability, exposure, observed effect, and business consequence kept distinct.
- [`Annotation`](phase_002/05_investigation_impact_explanation/annotation.md) — attributed human context without source-evidence mutation or hidden structured truth.
- [`Explanation`](phase_002/05_investigation_impact_explanation/explanation.md) — authorization/time-aware evidence-grounded communication with statement-to-basis traceability.

### Post-exit addenda
- [`Propagation Safeguard`](phase_002/addenda/propagation_safeguard.md) — proposed/active/released protective hold or quarantine state for an explicit output/consumption boundary.
- [`Capability Authorization`](phase_002/addenda/capability_authorization.md) — principal/capability/subject authorization state separating raw-data visibility, analytical visibility, operational control, and safeguard/gate authority.
- [`Execution Gate`](phase_002/addenda/execution_gate.md) — optional downstream execution admission/hold/admit/override control based on explicit prerequisite readiness evidence, separate from passive monitoring and output quarantine.

## Core access boundary

The concept model explicitly distinguishes:

**responsibility/policy context → Capability Authorization → authorized evidence/action view**

without making Responsibility Assignment or Policy Context themselves authorization sources.

A restricted-data analyst may be permitted to inspect approved aggregate health metrics, execution timing, Assessments, redacted Lineage, policy/restriction summaries, responsibility context, causal status, Impact, safeguards, gate state, and Annotation while being denied rows, sensitive columns, thresholds, identities, or other restricted evidence. A job operator can separately be authorized to retry/update/control a job without receiving raw-data read permission.

Derived evidence is not automatically unrestricted; authorization applies to metadata/metrics/topology/causal/consequence/control detail independently where necessary.

## Observation versus active control boundary

The default framework mode is observational and should remain out-of-band from production execution. Monitoring evidence collection or framework degradation must not delay production merely because an asset is monitored.

An **Execution Gate** is an explicit opt-in active-control boundary. It can hold a downstream execution until a declared upstream readiness condition is satisfied, admit it when ready, or record an authorized override. It is not implicitly created by Lineage or Assessment and does not replace Execution History.

**Execution Gate ≠ Propagation Safeguard**: a gate controls whether a downstream run starts; a safeguard controls whether output/current state propagates or is consumed. Both can independently create observable latency/delivery consequences.

## Cross-cutting reasoning model

The reasoning chain can distinguish:

**identified subject → monitoring/governance context → Capability Authorization / Authorized Analytical Projection → planned intent / prospective downstream profile → active Deployment → execution/timing/dependency evidence → Observation → time-valid Assessment → optional Execution Gate admission/hold when explicitly enabled → realized execution/Change → Investigation → Causal Claim → downstream Impact candidate → exposure/non-exposure → observed effect → consequence evidence → Propagation Safeguard prevention/operational effect where applicable → Annotation → Explanation**

Causal attribution from an origin, gate, or safeguard to a downstream effect remains explicit **Causal Claim** rather than becoming an Impact or control-state shortcut.

This is a reasoning/synchronization model, not a service topology, IAM architecture, scheduler/orchestration design, persistence schema, or temporal replay implementation.

## Historical replay boundary

Phase 003 Group 06 adds **no 24th concept**. Historical replay is a synchronization view over the existing concept histories.

It preserves:

- **effective/event time ≠ recorded/knowledge time**;
- current state ≠ historical state cut;
- later evidence ≠ evidence known then;
- actual historical state/action/Explanation ≠ replay-derived interpretation/reconstruction;
- actual gate/safeguard action ≠ counterfactual action now preferred;
- historical authorization/control state ≠ current disclosure permission.

A present-day `as-known-then` computation may be useful, but it cannot be presented as an Assessment, belief, decision, or Explanation that actually existed then unless historical state proves that it did.

## Domain entities that are not automatically concepts

Logical pipelines, jobs, tasks, runs, execution opportunities, tables, views, Metric Views, repositories, workflows, columns, business metrics, reports, applications, business processes, teams, people, source revisions, deployment targets, client-delivery endpoints, roles, and groups may participate in concepts without becoming giant concepts themselves.

## Phase 003 synchronization work

**Phase 003 is complete.** Accepted synchronization range: **SYN-001–SYN-035**. E-01–E-22 pass end-to-end consolidation. Current results are documented in [`phase_003/README.md`](phase_003/README.md), with Group 06 in [`phase_003/06_historical_replay_and_consolidation/`](phase_003/06_historical_replay_and_consolidation/).

**Phase 004 — Evidence, Time, and Causality Refinement is next and has not started.**
