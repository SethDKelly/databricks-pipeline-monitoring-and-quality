# Concept Catalog

## Status

**22 concepts are Accepted.** Phase 002 originally exited with 20 accepted concepts. Later Phase 003 work exposed two missing independent behaviors: **Propagation Safeguard** and **Capability Authorization**, each accepted through a narrow post-exit addendum.

The project uses Concept Design to define independently understandable units of functionality. Concepts remain implementation-neutral and synchronize rather than collapse into vendor, service, storage, schema, IAM, or UI boundaries.

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
- [`Capability Authorization`](phase_002/addenda/capability_authorization.md) — principal/capability/subject authorization state separating raw-data visibility, analytical visibility, operational control, and safeguard authority.

## Core access boundary

The concept model explicitly distinguishes:

**responsibility/policy context → Capability Authorization → authorized evidence/action view**

without making Responsibility Assignment or Policy Context themselves authorization sources.

A restricted-data analyst may be permitted to inspect approved aggregate health metrics, execution timing, Assessments, redacted Lineage, policy/restriction summaries, responsibility context, causal status, Impact, safeguards, and Annotation while being denied rows, sensitive columns, thresholds, identities, or other restricted evidence. A job operator can separately be authorized to retry/update/control a job without receiving raw-data read permission.

Derived evidence is not automatically unrestricted; authorization applies to metadata/metrics/topology/causal/consequence detail independently where necessary.

## Cross-cutting reasoning model

The reasoning chain can distinguish:

**identified subject → monitoring/governance context → Capability Authorization / Authorized Analytical Projection → planned intent / prospective downstream profile → active Deployment → execution/timing/dependency evidence → Observation → time-valid Assessment → realized Change → Investigation → Causal Claim → downstream Impact candidate → exposure/non-exposure → observed effect → consequence evidence → Propagation Safeguard prevention/operational effect where applicable → Annotation → Explanation**

Causal attribution from an origin to a downstream effect remains explicit **Causal Claim** rather than becoming an Impact layer.

This is a reasoning/synchronization model, not a service topology, IAM architecture, or persistence schema.

## Domain entities that are not automatically concepts

Logical pipelines, jobs, tasks, runs, tables, views, Metric Views, repositories, workflows, columns, business metrics, reports, applications, business processes, teams, people, source revisions, deployment targets, client-delivery endpoints, roles, and groups may participate in concepts without becoming giant concepts themselves.

## Phase 003 synchronization work

Groups 01–05 are accepted, including Capability Authorization as the pre-Group-05 addendum and SYN-023–SYN-031 for downstream Impact, Annotation, authorized analytical projection, and Explanation. Current synchronization work is documented in [`phase_003/README.md`](phase_003/README.md); **Group 06 — Historical Replay & Phase 003 Consolidation is next.**
