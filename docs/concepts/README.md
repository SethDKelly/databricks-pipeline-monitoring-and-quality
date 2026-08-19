# Concept Catalog

## Status

**Phase 002 concept review complete. All 20 retained concepts are Accepted. Phase 003 synchronization design is active; Groups 01–02 are accepted.**

The project uses Concept Design to define independently understandable units of functionality. Concepts remain implementation-neutral and synchronize rather than collapse into vendor, service, storage, schema, or UI boundaries.

Use [`concept_template.md`](concept_template.md) for concept shape. The completed Phase 002 review is in [`phase_002/README.md`](phase_002/README.md); active synchronization contracts are in [`phase_003/README.md`](phase_003/README.md).

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

The functional reasoning chain can distinguish:

**identified subject → monitoring responsibility → meaning/governance → planned/normative/descriptive reference context → deployment/execution/observation evidence → assessment/realized change → investigation → causal claim → downstream impact → human context → authorized explanation**

This is a reasoning model, not a proposed service topology or persistence schema.

## Phase 003 synchronization state

### Group 01 — Subject, Scope & Governance Context — Accepted
Entity Identity is resolved before subject-specific state; Monitoring Scope and governance branches remain independent; Classification may support explicit Policy Context applicability without manufacturing policy.

### Group 02 — Planned Change & Reference Transition — Accepted
Change Intent can prepare prospective Expectation/Baseline context without activating it. Intent-to-Deployment association requires evidence. Reference transition follows sufficient realization evidence for the relevant target/context, not workflow success/planned time. Old Baselines remain historical/context-specific rather than being deleted, rollback requires re-resolution, and new Baselines derive only from comparable post-transition Observations.

### Group 03 — Runtime Evidence, Health & Realized Change — Next
Runtime synchronization must consume the correct time-valid reference context established by Groups 01–02 while preserving execution fact, Observation, Assessment, and realized Change as separate truths.
