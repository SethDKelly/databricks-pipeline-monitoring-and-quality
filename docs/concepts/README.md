# Concept Catalog

## Status authority

Current repository phase progression is declared only in [`../README.md#current-state`](../README.md#current-state). This catalog intentionally does **not** maintain an independent current/next-phase declaration.

The accepted concept count is **24**. Phase 002 originally exited with 20 accepted concepts; later narrow addenda added **Propagation Safeguard**, **Capability Authorization**, **Execution Gate**, and **Assertion Authority**.

For the detailed cross-cutting boundary narrative that previously lived in this index, see [`history/concept_catalog_snapshot_pre_phase_006_exit.md`](history/concept_catalog_snapshot_pre_phase_006_exit.md). That file is retained as a **historical snapshot**; any phase-status wording in it reflects status at the time of writing and is superseded by the canonical documentation index.

The project uses Concept Design to define independently understandable units of functionality. Concepts remain implementation-neutral and synchronize rather than collapse into vendor, service, storage, schema, IAM, authority-rule engine, approval-workflow, orchestration, temporal-replay, metric-governance, disclosure, questioning, answer-composition, Explanation-rendering, integration-source, or UI boundaries.

Use [`concept_template.md`](concept_template.md) as the specification checklist. The original Phase 002 review and later addenda are in [`phase_002/README.md`](phase_002/README.md) and [`phase_002/addenda/`](phase_002/addenda/).

## Accepted concepts

### Group 01 — Scope & Identity
- [`Monitoring Scope`](phase_002/01_scope_and_identity/monitoring_scope.md)
- [`Entity Identity`](phase_002/01_scope_and_identity/entity_identity.md)

### Group 02 — Semantics, Governance & Policy
- [`Semantic Definition`](phase_002/02_semantics_governance_policy/semantic_definition.md)
- [`Responsibility Assignment`](phase_002/02_semantics_governance_policy/responsibility_assignment.md)
- [`Classification`](phase_002/02_semantics_governance_policy/classification.md)
- [`Policy Context`](phase_002/02_semantics_governance_policy/policy_context.md)

### Group 03 — Health Evaluation
- [`Expectation`](phase_002/03_health_evaluation/expectation.md)
- [`Baseline`](phase_002/03_health_evaluation/baseline.md)
- [`Observation`](phase_002/03_health_evaluation/observation.md)
- [`Assessment`](phase_002/03_health_evaluation/assessment.md)

### Group 04 — History, Lineage & Change
- [`Change Intent`](phase_002/04_history_lineage_change/change_intent.md)
- [`Execution History`](phase_002/04_history_lineage_change/execution_history.md)
- [`Deployment`](phase_002/04_history_lineage_change/deployment.md)
- [`Lineage`](phase_002/04_history_lineage_change/lineage.md)
- [`Change`](phase_002/04_history_lineage_change/change.md)

### Group 05 — Investigation, Impact & Explanation
- [`Investigation`](phase_002/05_investigation_impact_explanation/investigation.md)
- [`Causal Claim`](phase_002/05_investigation_impact_explanation/causal_claim.md)
- [`Impact`](phase_002/05_investigation_impact_explanation/impact.md)
- [`Annotation`](phase_002/05_investigation_impact_explanation/annotation.md)
- [`Explanation`](phase_002/05_investigation_impact_explanation/explanation.md)

### Post-exit addenda
- [`Propagation Safeguard`](phase_002/addenda/propagation_safeguard.md)
- [`Capability Authorization`](phase_002/addenda/capability_authorization.md)
- [`Execution Gate`](phase_002/addenda/execution_gate.md)
- [`Assertion Authority`](phase_002/addenda/assertion_authority.md)

## Refinement and phase indexes

- [`phase_003/README.md`](phase_003/README.md) — concept synchronizations and ecosystem scenarios.
- [`phase_004/README.md`](phase_004/README.md) — evidence, time, causality, exposure, readiness, and control-evidence refinement.
- [`phase_005/README.md`](phase_005/README.md) — governance, authority, capability, and disclosure refinement.
- [`phase_006/README.md`](phase_006/README.md) — health, metrics, schema, statistical, reconciliation, composite-health, and timing refinement.
- [`phase_007/README.md`](phase_007/README.md) — Lineage, change, Investigation, Impact, safeguard, execution-control, and historical operational replay refinement.
- [`phase_008/README.md`](phase_008/README.md) — business-question, material answer-statement, basis-traceability, and evidence-grounded Explanation refinement.
- [`phase_009/README.md`](phase_009/README.md) — integration-contract, source-role, authority-applicability, evidence-availability, coverage, retention, disclosure and feasibility refinement; consult canonical status above for phase progression.

## Durable boundaries

Across phases, preserve the accepted distinctions recorded in the phase contracts and decision history, including:

- Assertion Authority ≠ Capability Authorization ≠ evidence sufficiency ≠ enforcement;
- governed schema meaning ≠ structural Expectation ≠ realized structure ≠ compatibility Assessment;
- Baseline ≠ Expectation;
- Observation ≠ Assessment;
- Lineage ≠ causality or metric/status propagation;
- Change Intent ≠ Deployment ≠ realized Change;
- Investigation ≠ Causal Claim truth;
- candidate/reachable ≠ exposed ≠ downstream effect ≠ consequence ≠ causal attribution;
- readiness ≠ gate decision ≠ gate enforcement ≠ actual execution;
- Execution Gate ≠ Propagation Safeguard;
- historical retained state ≠ replay-derived reconstruction;
- question/request context ≠ truth/authority/authorization;
- answer statement ≠ independent truth state;
- Explanation ≠ independent truth source;
- source availability ≠ Assertion Authority ≠ evidence sufficiency ≠ disclosure authorization;
- source-local identity ≠ Entity Identity without reconciliation;
- positive source evidence capability ≠ strong-negative evidence capability;
- current source availability ≠ historical replay capability;
- integration support classification ≠ proposition truth or confidence.

Detailed definitions remain in the concept, refinement, decision, and reference documents; this README is a navigation/catalog surface rather than an independent phase-status authority.