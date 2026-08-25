# Concept: Change Intent

**Status:** Accepted — Phase 002 Group 04; refined by Phase 007 Group 02 (OPS-010, OPS-013, OPS-015–OPS-017)

## Purpose

Let the ecosystem register an intended modification and its anticipated effects before the modification becomes active, so later monitoring can distinguish planned context from what was actually deployed, observed, and assessed.

## Operational principle

A pipeline maintainer plans to add a filter to the transformation that produces Table C. The Change Intent records the intended filter change, the targeted pipeline/data asset, the planned activation context, and the anticipated effect that C's output volume will materially decrease. It also records that the current volume Baseline may cease to be comparable after activation and that a prospective post-change Expectation should be reviewed or established.

The intent does not change the current Baseline, prove that a Deployment activated, prove that the filter actually changed C, or establish that the resulting data is healthy. After activation, Execution History, Observations, realized Change, Baseline transition, and Assessment establish what actually happened.

## Actors

- Data Engineer / Pipeline Maintainer
- Data Owner / accountable business party
- Data Steward / Governance Steward
- Data Platform Administrator
- Monitoring framework
- Source-control / change-management integration source

## State

- change-intent identity;
- identified target entity or entities;
- intended change facet/type and functional description;
- registration time and planned effective/activation context when known;
- anticipated effects, including affected entities/dimensions, direction, magnitude/range, topology, cadence, schema, semantics, or other declared consequences when known;
- declared monitoring implications, such as prospective Baseline non-comparability or Expectation review/revision need;
- source revision/configuration references when known, without assuming implementation has occurred;
- provenance, actor/source, and authority context;
- revision/supersession/withdrawal history;
- ambiguity or conflict among competing change-intent assertions.

Anticipated effects are descriptive intent by default. A statement becomes a normative requirement only through an explicit **Expectation**.

## Actions

### `register`
- **Intent:** record an intended modification and the context/effects the actor expects it to have.
- **State effect:** creates a provenance-bearing Change Intent without asserting that implementation or activation occurred.

### `revise`
- **Intent:** update the intended modification, timing, or anticipated effects before/while realization is pending.
- **State effect:** creates a new intent version while preserving prior versions and registration history.

### `withdraw`
- **Intent:** state that the registered intent is no longer planned.
- **State effect:** ends prospective applicability without erasing that the intent was previously registered.

### `resolvePlannedAt`
- **Intent:** determine which Change Intents were registered as relevant to a subject/context/time.
- **Observable result:** applicable intent(s), none known, conflicting, withdrawn, unauthorized, or unavailable with provenance where disclosure is allowed.

## Invariants / behavioral expectations

- Change Intent is planned context, not an Observation of actual state.
- Change Intent is not Deployment evidence and does not prove activation.
- Change Intent is not a realized Change and does not prove that the intended effect occurred.
- Anticipated effect is not automatically an Expectation. Normative post-change behavior must be established/revised explicitly through Expectation.
- A Change Intent can indicate that a Baseline is expected to become non-comparable, but it cannot rewrite the Baseline or manufacture a post-change Baseline from intended values.
- New Baselines remain descriptive and must be derived from sufficient comparable post-change Observation evidence.
- A Change Intent may exist without any eventual Deployment or realized Change.
- A Deployment or realized Change may exist without a registered Change Intent.
- A realized Change may differ from the registered intent, including unintended side effects.
- Registration/revision/withdrawal history is preserved; current intent does not erase what was known before a historical incident.
- Change Intent does not assert health, defect, causation, or compliance.

## Phase 007 Group 02 refinement

OPS-010 makes intent revision/component identity material to realization reasoning. Where one registered intent contains independently realizable target/facet propositions, those components remain separately comparable rather than being flattened into one lifecycle status.

OPS-013 preserves many-to-many association between exact intent components and Deployment attempts/activations. Association requires provenance-bearing linkage and does not imply activation or conformance.

OPS-015 resolves the prior deferred question about intent-to-realization conformance: **no new concept is introduced**. Realization/conformance is a derived synchronization result over the exact intent revision/component plus Deployment activation and Change evidence. Change Intent itself does not acquire a `realized` field that would absorb those concepts.

For one bounded comparison, `matched`, `partially matched`, `diverged`, `not realized`, `not evidenced`, `indeterminate`, `conflicting`, and `unavailable` are comparison results, not intrinsic Change Intent states. `Not realized` requires sufficient negative evidence; lack of realization evidence is only `not evidenced`/unknown as applicable.

OPS-016 keeps phased/multi-target realization slice-specific. OPS-017 further distinguishes `no matching registered intent known`, `unregistered`, `outside declared intent scope`, and the stronger process proposition `unplanned`. Absence of a registered intent never proves lack of human intent, authorization, or proper process by itself.

Anticipated effects remain declarations. An observed effect omitted from intent is only `not declared/anticipated in the registered intent` unless separate evidence establishes the actor's actual intent.

## Ambiguity and missing evidence

Absence of a registered Change Intent does not prove that no human intended a change; it means the product has no registered intent evidence. Conflicting intended effects remain explicit. If a Change Intent is restricted, an authorized user may learn that planned-change context exists without receiving sensitive code/business details.

## Synchronizations

- **Entity Identity** supplies the intended-change targets and related entities.
- **Responsibility Assignment** may identify the parties responsible for the affected pipeline/data or for maintaining related Expectations.
- **Semantic Definition** may provide business meaning needed to interpret anticipated effects.
- **Expectation** may be explicitly established/revised for the post-change context; this is a separate normative action, not an automatic consequence of intent registration.
- **Baseline** may register a prospective comparability break tied to the intent, becoming effective only when realization evidence justifies it; a new Baseline is derived from post-change Observations.
- **Deployment** can later be linked as realization evidence for one or more Change Intents without treating deployment success as proof of intended effect.
- **Execution History** identifies executions occurring before/after an activated realization.
- **Lineage** may later show realized topology differences; planned topology belongs to Change Intent until actual relationship evidence exists.
- **Change** describes realized differences and transitions without assuming they match the intent.
- **Investigation/Causal Claim** may later compare intent, deployment, realized change, and assessments when evaluating explanations.

## Security / privacy / governance considerations

Planned changes can reveal confidential roadmap, source logic, business rules, sensitive filters, future topology, or security controls. Change Intent visibility must be authorization-aware and may need safe abstraction.

Registering intent does not grant authority to deploy the change, revise Expectations, access data, or approve governance decisions.

## Evidence / provenance considerations

A Change Intent should retain who/what registered it, when it was registered, its planned effective context, revision history, and source/change references when available. The product must distinguish:

- **registration/knowledge time** — when the monitoring ecosystem learned the intent;
- **planned effective time** — when the change was intended to become active;
- **actual activation/change time** — established later by Deployment/Change evidence.

These times must not be silently collapsed.

## Representative scenarios

### Planned filter with expected lower volume
A filter is registered as expected to reduce C from roughly 20M rows to a materially lower population. The intent flags the current volume Baseline as prospectively non-comparable after activation. A post-change volume Expectation may be explicitly revised, while the new Baseline waits for sufficient post-change evidence.

### Valid planned change with expected outcome
The planned filter deploys, C's volume falls in the anticipated direction, the new post-change Expectation is satisfied, and later observations establish a stable new Baseline. Monitoring describes a planned structural change rather than treating the difference alone as degradation.

### Planned change with improper side effect
The filter was intended to reduce only one population, but null rate also rises and a completeness Expectation is violated. The registered intent explains why some volume change was expected but does not excuse or hide the unintended quality failure.

### Planned change differs in magnitude
A change intended to lower C modestly instead cuts volume by 70%. The Change Intent remains evidence of the intended outcome; Observations and Assessments show that the realized behavior differed materially.

### Intent never activated
A change is registered but its Deployment fails or is never activated. The existing Baseline remains applicable; the intent alone cannot trigger an effective Baseline transition.

### Unregistered change
A deployment/configuration transition occurs without a Change Intent. Monitoring still records Deployment, Change, Observations, and Assessments; the absence of planned context is itself an evidence limitation, not proof of wrongdoing.

## Non-goals

- implementing source-code review or change-approval workflow;
- performing deployments;
- proving that a planned change was realized;
- defining health or causal attribution;
- automatically revising Expectations;
- directly setting/replacing Baseline values;
- selecting a ticketing, CI/CD, or change-management product.

## Deferred questions

- Which anticipated-effect dimensions are required for the first MVP?
- What minimum concrete linkage is needed between Change Intent and source revision, pull request, ticket, or configuration reference? Phase 009 owns source mapping.
- Which Change Intents are authoritative enough to drive prospective Baseline comparability constraints or Expectation-review prompts?
- Concrete source support for phased realization and plan-registration coverage remains later integration work.
