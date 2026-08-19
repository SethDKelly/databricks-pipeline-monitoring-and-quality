# Concept Catalog

## Status

**21 concepts are Accepted.** Phase 002 originally exited with 20 accepted concepts. Phase 003 Group 03 exposed one missing independent operational-protection behavior, and **Propagation Safeguard** was accepted as a narrow post-exit Phase 002 addendum.

The project uses Concept Design to define independently understandable units of functionality. Concepts remain implementation-neutral and synchronize rather than collapse into vendor, service, storage, schema, or UI boundaries.

Use [`concept_template.md`](concept_template.md) as the specification checklist. The completed original review and later addendum are in [`phase_002/README.md`](phase_002/README.md) and [`phase_002/addenda/`](phase_002/addenda/).

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
- [`Expectation`](phase_002/03_health_evaluation/expectation.md) — normative criteria for what should be acceptable.
- [`Baseline`](phase_002/03_health_evaluation/baseline.md) — descriptive reference behavior derived from comparable evidence.
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

### Post-exit addendum — Operational protection
- [`Propagation Safeguard`](phase_002/addenda/propagation_safeguard.md) — proposed/active/released protective hold or quarantine state for an explicit data-output/consumption boundary; it does not turn protective action into health or causal truth.

## Accepted boundary changes from Phase 001 discovery

- `Monitored Scope` → **Monitoring Scope**.
- `Asset Identity` → **Entity Identity**.
- `Description / Semantics` → **Semantic Definition**.
- `Ownership` → **Responsibility Assignment**.
- **Classification** and **Policy Context** are separate.
- **Baseline** is separate from normative Expectation.
- **Observation** is separate from Assessment.
- `Deployment Record` → **Deployment**.
- **Change Intent** is separate from realized Change.
- **Causal Claim** is explicit rather than hidden inside Investigation.
- `Annotation / Confirmation` → **Annotation** plus explicit Causal Claim confirmation/rejection semantics.
- `Report / Explanation` → **Explanation**; report/chat/dashboard forms are presentation realizations.
- Phase 003 later introduced **Propagation Safeguard** because protective propagation state had no valid owner among the original 20 concepts.

## Cross-cutting accepted model

The reasoning chain can distinguish:

**identified subject → monitoring/governance context → planned intent / prospective downstream profile → active Deployment → execution/timing/dependency evidence → Observation → time-valid Assessment → realized Change → Investigation → Causal Claim → actual downstream Impact → Propagation Safeguard where authorized → Annotation → Explanation**

This is a reasoning/synchronization model, not a service topology or persistence schema.

## Domain entities that are not automatically concepts

Logical pipelines, jobs, tasks, runs, tables, views, Metric Views, repositories, workflows, columns, business metrics, reports, applications, business processes, teams, people, source revisions, deployment targets, and client-delivery endpoints may participate in concepts without becoming giant concepts themselves.

## Phase 003 synchronization work

Groups 01–03 are accepted. Current synchronization work is documented in [`phase_003/README.md`](phase_003/README.md); **Group 04 — Lineage, Investigation & Causal Reasoning is next**.
