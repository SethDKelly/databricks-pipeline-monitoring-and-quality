# Concept Catalog

## Status

**Phase 002 active working catalog.** Groups 01–04 are accepted. Group 05 remains **Candidate** until reviewed and explicitly accepted.

The project uses Concept Design to discover independently understandable units of functionality. Concepts remain implementation-neutral and synchronize rather than collapse into vendor/service/storage boundaries.

Use [`concept_template.md`](concept_template.md) as the specification checklist. The strategic Phase 002 review plan is in [`phase_002/README.md`](phase_002/README.md).

## Current grouped concepts

### Group 01 — Scope & Identity — Accepted
- [`Monitoring Scope`](phase_002/01_scope_and_identity/monitoring_scope.md)
- [`Entity Identity`](phase_002/01_scope_and_identity/entity_identity.md)

### Group 02 — Semantics, Governance & Policy — Accepted
- [`Semantic Definition`](phase_002/02_semantics_governance_policy/semantic_definition.md)
- [`Responsibility Assignment`](phase_002/02_semantics_governance_policy/responsibility_assignment.md)
- [`Classification`](phase_002/02_semantics_governance_policy/classification.md)
- [`Policy Context`](phase_002/02_semantics_governance_policy/policy_context.md)

### Group 03 — Health Evaluation — Accepted
- [`Expectation`](phase_002/03_health_evaluation/expectation.md) — normative criteria.
- [`Baseline`](phase_002/03_health_evaluation/baseline.md) — descriptive reference behavior, including planned/realized structural-break comparability semantics.
- [`Observation`](phase_002/03_health_evaluation/observation.md) — measured/retrieved evidence.
- [`Assessment`](phase_002/03_health_evaluation/assessment.md) — basis-explicit health/typicality interpretation.

### Group 04 — History, Lineage & Change — Accepted
- [`Change Intent`](phase_002/04_history_lineage_change/change_intent.md) — registered intended modification and anticipated effects before realization.
- [`Execution History`](phase_002/04_history_lineage_change/execution_history.md) — actual execution-instance lifecycle history.
- [`Deployment`](phase_002/04_history_lineage_change/deployment.md) — attempted and active source/configuration state for runtime targets.
- [`Lineage`](phase_002/04_history_lineage_change/lineage.md) — typed, temporal, provenance-bearing upstream/downstream relationships.
- [`Change`](phase_002/04_history_lineage_change/change.md) — realized differences/state transitions without health or causal judgment.

### Group 05 — Investigation, Impact & Explanation — Candidate
- [`Investigation`](phase_002/05_investigation_impact_explanation/investigation.md)
- [`Causal Claim`](phase_002/05_investigation_impact_explanation/causal_claim.md)
- [`Impact`](phase_002/05_investigation_impact_explanation/impact.md)
- [`Annotation`](phase_002/05_investigation_impact_explanation/annotation.md)
- [`Explanation`](phase_002/05_investigation_impact_explanation/explanation.md)

## Accepted boundary changes from Phase 001 discovery

- `Monitored Scope` → **Monitoring Scope**.
- `Asset Identity` → **Entity Identity**.
- `Description / Semantics` → **Semantic Definition**.
- `Ownership` → **Responsibility Assignment**.
- **Classification** and **Policy Context** are separate.
- **Baseline** is separate from normative Expectation.
- **Observation** is separate from Assessment.
- `Deployment Record` → **Deployment**.
- **Change Intent** is introduced separately from realized Change so planned effects never masquerade as observed facts.
- **Lineage** is explicitly typed/temporal and graph-compatible without selecting graph storage.
- Group 04 adopts ledger-like append/supersede historical semantics without selecting an event-store/blockchain/persistence technology.

## Candidate boundary changes for Group 05

- introduce **Causal Claim** rather than hiding hypotheses/confirmation inside Investigation;
- `Annotation / Confirmation` → **Annotation** plus confirmation/rejection actions on reviewable claims;
- `Report / Explanation` → **Explanation**.

## Domain entities that are not automatically concepts

Logical pipelines, jobs, tasks, runs, tables, views, Metric Views, repositories, GitHub Actions workflows, columns, business metrics, reports, teams, people, source revisions, and deployment targets may participate in concepts without becoming giant concepts themselves.

## Synchronization work

Phase 002 identifies synchronization boundaries; detailed synchronization design belongs to Phase 003. Key chains now include:

1. Change Intent → explicit prospective Expectation review and/or prospective Baseline comparability break.
2. Change Intent → Deployment realization evidence → Execution History.
3. Observation + Expectation/Baseline → basis-explicit Assessment.
4. Deployment/Execution/Observation/Lineage → realized Change context without causal overclaim.
5. Change Intent + realized Change + Assessment → evidence for later Investigation/Causal Claim.
6. Lineage + Impact → downstream exposure candidates.
7. Governance concepts + Explanation → business-facing context.
