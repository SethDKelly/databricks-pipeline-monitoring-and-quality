# Group 02 — Planned Change & Reference Transition

**Status:** Review complete — synchronizations accepted

## Goal

Define how registered Change Intent prepares future Expectation/Baseline context, how intent is associated with Deployment realization evidence, how an actual operating-context transition changes reference applicability, and how post-transition evidence eventually establishes a new empirical Baseline — without allowing the plan to manufacture facts, norms, history, or health conclusions.

## Accepted synchronizations

- [`SYN-004 — Change Intent → Prospective Reference Preparation`](004_change_intent_prospective_reference_preparation.md)
- [`SYN-005 — Change Intent ↔ Deployment Realization Association`](005_intent_deployment_realization_association.md)
- [`SYN-006 — Realization Evidence → Reference Transition`](006_realization_reference_transition.md)
- [`SYN-007 — Post-Transition Observation → Baseline Establishment`](007_post_transition_baseline_establishment.md)

## Boundary decisions

### 1. Planned intent prepares references but does not activate them

A Change Intent can identify that an Expectation should be reviewed and that an existing Baseline may become non-comparable if the change is realized. Those are prospective synchronization results. Registration time, planned effective time, and actual activation/change time remain distinct.

### 2. Expectation and Baseline are independent branches

A planned change can trigger both branches, either branch, or neither:

- an authorized actor/source may explicitly establish or revise a prospective Expectation;
- Baseline may register a prospective comparability break;
- neither action is inferred from the other;
- anticipated effects never become normative Expectations automatically;
- intended values never become empirical Baseline values.

One unresolved branch does not erase a valid result in the other.

### 3. Deployment association is evidence linkage, not intent conformance

Change Intent and Deployment may be associated only when sufficient target/revision/configuration/context evidence supports the relationship. Time proximity or similar naming is insufficient by itself. The relationship can be one-to-many or many-to-one across targets/releases.

Association or activation does not prove that the intended data effect occurred or that resulting behavior is healthy.

### 4. The reference transition follows realized operating context, not workflow success

A prospective reference boundary becomes effective only when evidence is sufficient for the relevant subject/dimension/context to establish that the changed operating state became active. Depending on the change, this may be established by trustworthy Deployment activation evidence for the relevant structural/configuration state, by realized Change evidence, or by both.

A CI/CD workflow reporting success is not automatically that evidence.

### 5. Baseline non-comparability is context/interval scoped

When a structural transition becomes effective, the old Baseline becomes non-comparable for the changed context/interval; it is not deleted or globally invalidated. A rollback or later return to a prior operating context may make an earlier Baseline eligible for comparison again only when comparability is re-established. Rollback does not blindly resurrect a historical Baseline.

### 6. Expectation applicability follows its own normative authority

A prospective post-change Expectation can be prepared before activation and become applicable from an evidence-backed activation/transition boundary when that is how the Expectation was established. If an authority explicitly establishes a fixed-time or independently applicable Expectation, that Expectation follows its own semantics; Change Intent synchronization does not override it.

Withdrawal of an intent does not silently revoke an independently authoritative Expectation.

### 7. Unregistered structural change still transitions descriptive reference context

A realized structural Change may make an old Baseline non-comparable even when no Change Intent exists. The product must not fabricate planned context or a revised Expectation in that case.

### 8. Post-change Baseline is learned from evidence

A new Baseline is derived only after sufficient comparable post-transition Observations exist. Until then, a separately established Expectation can provide immediate normative evaluation while Baseline comparison remains unavailable/insufficient.

### 9. Transition is target/context-specific

Development activation, canary rollout, regional deployment, partial population transition, or one target becoming active does not globally switch reference context for every environment/entity. The applicable boundary resolves for the specific Entity Identity, target, dimension, and context supported by evidence.

### 10. Late knowledge never rewrites what was known then

A Change Intent or activation association recorded after the event can enrich retrospective reasoning while preserving its later recorded/knowledge time. Historical contemporaneous reconstruction must still show that the monitoring ecosystem did not know that planned/activation context earlier.

## Scenario review

### E-02 — Planned structural change with valid outcome

Pass. A filter intent flags the old C-volume Baseline prospectively, an authorized post-change volume Expectation is prepared, the relevant configuration becomes active, the reference boundary takes effect, the first post-change run can be assessed normatively, and a new Baseline is derived later from post-change evidence.

### E-03 — Planned change with unintended violation

Pass. The expected volume transition can occur and satisfy its revised volume Expectation while a separate completeness/uniqueness/reconciliation Expectation fails. Planned context does not suppress independent health dimensions.

### E-04 — Unregistered change

Pass. Realized structural Change can make the old Baseline non-comparable without any registered intent. No planned effect or normative criterion is invented.

### E-06 — Deployment-correlated shift

Pass. Intent association and activation establish chronology/reference context where supported, but they do not prove that the deployment caused the observed shift.

### E-10 — Historical correction

Pass. Late activation evidence can retrospectively establish that a reference boundary occurred earlier and can produce later reassessment/reference interpretation while preserving the Baseline/Expectation context the product actually used at incident knowledge time.

## Additional adversarial scenarios

### Intent withdrawn before activation
The prospective Baseline break remains historical but never becomes effective from that intent. Any independently established Expectation retains its own lifecycle/authority semantics.

### Deployment attempt fails
An attempt can remain associated with the intent, but no activation/reference transition is created.

### Wrong environment activates
A development deployment associated with the intent does not transition production Baseline/Expectation context.

### Partial rollout
Reference boundaries can differ by target/cohort/context until rollout evidence establishes broader activation.

### Rollback
The changed-context interval ends. Prior Baseline/Expectation versions may become applicable/comparable candidates only when their own context/time rules justify it; nothing is silently restored.

### Late intent registration
A team registers after the incident that the change had been planned. Retrospective reasoning can use the intent with its true registration time; contemporaneous explanation still reports that planned context was not known then.

## Deferred questions

- minimum authority/evidence required for an intent to register a prospective Baseline break;
- first-MVP representation of prospective Expectation applicability before exact activation time is known;
- exact evidence threshold for declaring a structural operating-context transition by change type;
- representation of partial/cohort/percentage rollout contexts;
- when prior Baselines may be reused after rollback versus requiring refreshed derivation;
- whether intent-to-realization conformance later needs explicit product semantics beyond Investigation/Assessment context.

## Group exit gate

**Satisfied.** Planned context can prepare future normative/descriptive references; Deployment/Change evidence can establish a target-specific transition without causal overclaim; failed/withdrawn/unregistered/rollback/late-evidence paths remain honest; and empirical post-change history is never manufactured from intent.

The next group is **Group 03 — Runtime Evidence, Health & Realized Change**.
