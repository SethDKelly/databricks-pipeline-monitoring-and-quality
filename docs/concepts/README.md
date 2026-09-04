# Concept Catalog

## CKR authority notice

DMTZ is migrating from chronological concept/refinement ownership to a dedicated canonical knowledge layer.

The machine-readable authority ledger is [`../canonical_knowledge_retrofit/canonical_ownership_inventory.json`](../canonical_knowledge_retrofit/canonical_ownership_inventory.json).

**CKR-A accepted all 24 concepts as `legacy_authoritative` at the paths listed below.** CKR-C will promote each concept into an exact target under `docs/canonical/concepts/` using atomic cutover. After a concept becomes `canonicalized`, its phase-era source becomes design provenance for that concept rather than the current definition.

Current design-phase progression remains declared only in [`../README.md#current-state`](../README.md#current-state).

## Accepted concept count

The accepted concept count is **24**: the original 20 plus **Propagation Safeguard**, **Capability Authorization**, **Execution Gate**, and **Assertion Authority**.

Concepts remain independently understandable units of functionality and synchronize rather than collapse into implementation/vendor/schema/IAM/UI boundaries.

## Legacy current concept owners until CKR-C cutover

### Scope & Identity
- [`Monitoring Scope`](phase_002/01_scope_and_identity/monitoring_scope.md)
- [`Entity Identity`](phase_002/01_scope_and_identity/entity_identity.md)

### Semantics, Governance & Policy
- [`Semantic Definition`](phase_002/02_semantics_governance_policy/semantic_definition.md)
- [`Responsibility Assignment`](phase_002/02_semantics_governance_policy/responsibility_assignment.md)
- [`Classification`](phase_002/02_semantics_governance_policy/classification.md)
- [`Policy Context`](phase_002/02_semantics_governance_policy/policy_context.md)

### Health Evaluation
- [`Expectation`](phase_002/03_health_evaluation/expectation.md)
- [`Baseline`](phase_002/03_health_evaluation/baseline.md)
- [`Observation`](phase_002/03_health_evaluation/observation.md)
- [`Assessment`](phase_002/03_health_evaluation/assessment.md)

### History, Lineage & Change
- [`Change Intent`](phase_002/04_history_lineage_change/change_intent.md)
- [`Execution History`](phase_002/04_history_lineage_change/execution_history.md)
- [`Deployment`](phase_002/04_history_lineage_change/deployment.md)
- [`Lineage`](phase_002/04_history_lineage_change/lineage.md)
- [`Change`](phase_002/04_history_lineage_change/change.md)

### Investigation, Impact & Explanation
- [`Investigation`](phase_002/05_investigation_impact_explanation/investigation.md)
- [`Causal Claim`](phase_002/05_investigation_impact_explanation/causal_claim.md)
- [`Impact`](phase_002/05_investigation_impact_explanation/impact.md)
- [`Annotation`](phase_002/05_investigation_impact_explanation/annotation.md)
- [`Explanation`](phase_002/05_investigation_impact_explanation/explanation.md)

### Accepted post-exit addenda
- [`Propagation Safeguard`](phase_002/addenda/propagation_safeguard.md)
- [`Capability Authorization`](phase_002/addenda/capability_authorization.md)
- [`Execution Gate`](phase_002/addenda/execution_gate.md)
- [`Assertion Authority`](phase_002/addenda/assertion_authority.md)

The ownership inventory contains each exact future canonical target; do not independently maintain a second target-path list here.

## Refinement/design-history indexes

These phases remain valuable provenance and, until their stable-ID families migrate, distributed legacy contract authority:

- [`phase_003/README.md`](phase_003/README.md) — SYN synchronization;
- [`phase_004/README.md`](phase_004/README.md) — REF evidence/time/causality;
- [`phase_005/README.md`](phase_005/README.md) — AUTH governance/authority;
- [`phase_006/README.md`](phase_006/README.md) — HLTH health/quality/timing;
- [`phase_007/README.md`](phase_007/README.md) — OPS Lineage/change/investigation/Impact/control;
- [`phase_008/README.md`](phase_008/README.md) — EXPL questioning/Explanation;
- [`phase_009/README.md`](phase_009/README.md) — INTG source/integration/evidence availability;
- [`phase_010/README.md`](phase_010/README.md) — ARCH technical architecture.

After the relevant CKR cutover, these remain provenance/design history rather than normal current-truth lookup surfaces.

## Durable boundaries preserved through migration

- Assertion Authority ≠ Capability Authorization ≠ evidence sufficiency ≠ enforcement;
- Baseline ≠ Expectation;
- Observation ≠ Assessment;
- Lineage ≠ causality, encounter, exposure or Impact;
- Change Intent ≠ Deployment ≠ realized Change;
- Investigation ≠ Causal Claim truth;
- readiness ≠ gate decision ≠ enforcement ≠ actual execution;
- Execution Gate ≠ Propagation Safeguard;
- current state ≠ historical/as-known state;
- source availability ≠ Assertion Authority;
- Explanation/model/search output ≠ independent truth source.

CKR may change the owner path for these meanings; it may not silently change the meanings themselves.
