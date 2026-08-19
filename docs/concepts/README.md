# Concept Catalog

## Status

**Phase 002 concept review complete. All 20 retained concepts are Accepted.**

The project uses Concept Design to define independently understandable units of functionality. Concepts remain implementation-neutral and synchronize rather than collapse into vendor, service, storage, schema, or UI boundaries.

Use [`concept_template.md`](concept_template.md) as the specification checklist. The completed Phase 002 review is in [`phase_002/README.md`](phase_002/README.md).

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
- [`Explanation`](phase_002/05_investigation_impact_explanation/explanation.md) — authorization- and time-aware evidence-grounded communication with statement-to-basis traceability.

## Accepted boundary changes from Phase 001 discovery

- `Monitored Scope` → **Monitoring Scope**.
- `Asset Identity` → **Entity Identity**.
- `Description / Semantics` → **Semantic Definition**.
- `Ownership` → **Responsibility Assignment**.
- **Classification** and **Policy Context** are separate.
- **Baseline** is separate from normative Expectation.
- **Observation** is separate from Assessment.
- `Deployment Record` → **Deployment**.
- **Change Intent** is introduced separately from realized Change.
- **Causal Claim** is introduced rather than hiding causal hypotheses/confirmation inside Investigation.
- `Annotation / Confirmation` → **Annotation** plus explicit confirmation/rejection actions on Causal Claim.
- `Report / Explanation` → **Explanation**; report/chat/dashboard forms are presentation realizations, not foundational concepts.

## Cross-cutting accepted model

The functional reasoning chain can now distinguish:

**identified subject → monitoring responsibility → meaning/governance → normative/reference context → observed fact → assessment → planned intent → active deployment → execution → realized change/topology → investigation → causal claim → downstream impact → human context → authorized explanation**

This is a reasoning model, not a proposed service topology or persistence schema.

## Domain entities that are not automatically concepts

Logical pipelines, jobs, tasks, runs, tables, views, Metric Views, repositories, workflows, columns, business metrics, reports, applications, business processes, teams, people, source revisions, and deployment targets may participate in concepts without becoming giant concepts themselves.

## Phase 003 synchronization work

Detailed synchronization design belongs to Phase 003. Priority chains are listed in [`phase_002/README.md`](phase_002/README.md), including planned-change realization, health evaluation, Investigation/Causal Claim evolution, Impact refinement, authorized Explanation, and historical replay.
