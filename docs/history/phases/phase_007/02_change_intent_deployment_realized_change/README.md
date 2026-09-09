# Phase 007 Group 02 — Change Intent, Deployment Realization & Realized Change

**Status:** Review complete — accepted

## Goal

Refine how intended modifications, deployment activity and realized Change coordinate without collapsing plan, attempt, activation, active implementation state, observed effect and conformance into one lifecycle.

## Group result

Group 02 retains the existing **Change Intent**, **Deployment** and **Change** concepts as independent truth owners and accepts **OPS-010–OPS-020**. No new concept is required.

The major addition is an explicit **derived intent-to-realization comparison**. It compares an exact intent revision/component against associated Deployment, activation and realized Change evidence while owning no new truth itself.

Preserve the proposition chain:

**registered intent → deployment association → deployment attempt/outcome → target/facet activation → evidence-established realized state/Change → intent-to-realization comparison**

No layer automatically creates the next.

## Accepted OPS contracts

1. [`OPS-010 — Change Intent Proposition Identity, Version & Target Scope`](010_change_intent_proposition_identity_version_target_scope.md)
2. [`OPS-011 — Implementation-State Reference, Version & Deployment Payload Binding`](011_implementation_state_reference_version_deployment_payload_binding.md)
3. [`OPS-012 — Deployment Attempt, Activation & Active-State Resolution`](012_deployment_attempt_activation_active_state_resolution.md)
4. [`OPS-013 — Change Intent ↔ Deployment Association, Evidence & Cardinality`](013_intent_deployment_association_evidence_cardinality.md)
5. [`OPS-014 — Realized Change Proposition, Before/After State & Transition Binding`](014_realized_change_proposition_before_after_transition_binding.md)
6. [`OPS-015 — Intent-to-Realization Comparison Layers & Vocabulary`](015_intent_realization_comparison_layers_vocabulary.md)
7. [`OPS-016 — Partial, Phased, Multi-Target & Overlapping Realization`](016_partial_phased_multi_target_overlapping_realization.md)
8. [`OPS-017 — Unregistered, Outside-Declared-Scope & Unplanned Change Semantics`](017_unregistered_out_of_scope_unplanned_change_semantics.md)
9. [`OPS-018 — Rollback, Reversion, Supersession & Restoration Semantics`](018_rollback_reversion_supersession_restoration_semantics.md)
10. [`OPS-019 — Historical Realization Replay, Correction & Negative Claims`](019_historical_realization_replay_correction_negative_claims.md)
11. [`OPS-020 — Change/Deployment Cross-Concept Ownership & Group 03 Handoff`](020_cross_concept_ownership_group03_handoff.md)

## Three truth owners remain separate

### Change Intent
Owns registered planned modification, intent revision/component, target/facet scope, planned activation context and anticipated effects.

It does not own deployment status, actual activation, realized state or conformance truth.

### Deployment
Owns attempts, source/configuration/payload provenance, target-specific activation/effective intervals, supersession/deactivation and rollback deployment history.

A Deployment can establish implementation state without establishing downstream effect.

### Change
Owns evidence-established realized differences/transitions with before/after state, time, provenance and limitations.

Change does not own plan, health, intent conformance or cause.

## Implementation-state/version model

Group 02 rejects a universal `deployment version` identifier.

The active state can be composite:

**source/build reference + job/transformation definition + configuration + schema/interface version + target context**.

A repository commit may be one provenance reference but is not automatically the deployed runtime identity. Same commit with different configuration can be a different operating state; multiple deployments can collectively produce the active composite state.

Specific version use by an actual execution remains Group 04 work.

## Deployment lifecycle vocabulary

Preserve separately:

**attempt → attempt outcome → activation → active-state interval → supersession/deactivation**.

Activation is target/facet/slice specific. A successful GitHub Actions/CI workflow cannot by itself prove runtime activation unless that source is later established as sufficient activation evidence for the exact target pattern.

## Intent-to-realization comparison

Comparison is derived, not a new concept.

It keeps association, activation, realized state, conformance and limitations as separate layers. For one exact intent component/effect, accepted conformance vocabulary is:

- `matched`;
- `partially matched`;
- `diverged`;
- `not realized` only with sufficient negative evidence;
- `not evidenced`;
- `indeterminate`;
- `conflicting`;
- `unavailable`.

There is no universal realization percentage/confidence score.

`Matched` also does not mean healthy, authorized, or causal. An implementation can match its intent while violating an Expectation; an anticipated effect can match for reasons that remain causally unresolved.

## Partial and overlapping realization

Realization can differ by environment, region, cohort/population, consumer/interface, implementation facet and rollout interval.

One intent can span many deployments; one deployment can carry many intents. Overlapping intents remain distinct even when a realized Change is compatible with several of them.

A global `fully realized` statement requires explicit composition plus coverage of required slices; target count alone does not create percentage completion.

## Unregistered versus unplanned

Group 02 makes a deliberate evidence distinction:

**no matching registered intent known ≠ unregistered change/deployment ≠ outside declared intent scope ≠ proven unplanned change**.

`Unplanned` is a stronger process proposition requiring an applicable planning/governance rule plus sufficient evidence/coverage. Missing Change Intent never automatically means wrongdoing, lack of authorization, or lack of human intent.

Likewise, an effect omitted from anticipated effects is `not declared/anticipated in the registered intent`, not automatically `unintended` human behavior.

## Rollback / reversion

Preserve:

- supersession/deactivation;
- rollback action/intent;
- realized reversion;
- bounded restoration/equivalence;
- roll-forward/fix-forward.

Reactivating R1 after R2 creates a new R1 activation interval; it never erases R2's historical interval.

Code/config rollback also does not automatically restore data already written, schema migrations, topology, materializations, exposure or health state. Each owning concept requires its own evidence.

## Historical behavior

Intent/deployment/change reasoning is bitemporal and non-rewriting.

A late activation observation may establish retrospectively that R2 was active at 09:55 while an incident-time knowledge cut still reports that activation was unknown then. Later association/Change corrections may revise current comparison without rewriting historical evidence/results.

Negative propositions such as `no deployment`, `no activation`, `no matching intent`, or `not realized` require conclusion-specific opportunity/coverage.

## Scenario review

[`scenario_review.md`](scenario_review.md) passes **C02-01–C02-24**, including:

- full/failed/unknown realization;
- activation without intended effect;
- partial/phased rollout;
- mismatched magnitude and undeclared side effects;
- one-to-many/many-to-one intent/deployment linkage;
- overlapping intents;
- configuration-only transitions;
- repository revision versus runtime identity;
- unregistered deployment/source change;
- outside-declared-scope change;
- rollback/reversion with residual data state;
- late activation correction and active-state conflict;
- planned topology versus effective Lineage.

## Durable boundaries

- Change Intent ≠ Deployment ≠ Change.
- Intent revision/component identity matters to comparison.
- repository revision ≠ deployed runtime identity absent evidence.
- attempt ≠ success ≠ activation ≠ effect.
- association ≠ activation ≠ conformance.
- activation ≠ specific execution version use.
- activation ≠ downstream effect.
- `not evidenced` ≠ `not realized`.
- matched intent ≠ healthy/acceptable/authorized/cause.
- partial rollout ≠ global activation.
- no matching intent known ≠ proven unplanned.
- rollback ≠ historical erasure ≠ universal downstream restoration.
- realized topology Change does not own the Lineage edge.
- historical event/effective time ≠ knowledge time ≠ comparison evaluation time.

## Architecture boundary

Group 02 does not select Git diffing, GitHub Actions event ingestion, build/package fingerprinting, Databricks runtime attestation, CDC, deployment telemetry sources, version storage, rollout mechanism, persistence schema or technical architecture.

## Group exit gate

**Satisfied.** OPS-010–OPS-020 and C02-01–C02-24 establish exact intent identity, implementation-reference discipline, target/facet activation, many-to-many association, realized Change binding, derived realization/conformance semantics, partial/overlapping rollout, careful unregistered/unplanned language, rollback/reversion and bitemporal replay without a 25th concept.

**Next: Phase 007 Group 03 — Prospective Blast Radius & Change-Aware Review.**
