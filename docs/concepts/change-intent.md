# Change Intent

**Canonical key:** `concept.change_intent`

**Kind:** CONCEPT

**Authority:** CANONICAL CURRENT AUTHORITY

**Migration record:** `concept.change_intent`

**Owns current question:** What modification was registered as intended, with what anticipated effects, before realization?

**Stable IDs:** N/A

## Current semantics

Change Intent owns intent identity, exact revision/component, target/facet, planned activation context, anticipated effects, monitoring implications, source/config references, provenance/authority, revision/withdrawal history, and conflict. Anticipated effects are descriptive planned context unless an Expectation separately establishes normative meaning.

## Actions

- `register` — record an intended modification/effect without asserting implementation.
- `revise` — version the planned modification/timing/effects.
- `withdraw` — end prospective applicability while retaining historical registration.
- `resolvePlannedAt` — return applicable intent revisions/components, none known, conflicting, withdrawn, unauthorized, or unavailable.

## Invariants / boundaries

- Change Intent ≠ Observation ≠ Deployment ≠ realized Change.
- An anticipated effect is not automatically an Expectation or a post-change Baseline.
- Intent may exist without Deployment/Change; Deployment/Change may exist without registered intent.
- Intent realization/conformance is a derived synchronization result over an exact intent component plus Deployment/Change evidence; it is not a `realized` field on Change Intent.
- `matched`, `partially matched`, `diverged`, `not realized`, `not evidenced`, `indeterminate`, `conflicting`, and `unavailable` are comparison results, not intrinsic intent states.
- No matching registered intent does not prove a change was humanly/process-wise `unplanned`.
- Registration/knowledge time, planned-effective time, and actual activation/change time remain distinct.

## Ambiguity / evidence

Absent intent evidence means no registered intent known, not proof of no intent. Restricted planned details may be safely abstracted.

## Synchronizations / related canonical resources

Expectation and Baseline may receive explicit prospective review/break context; Deployment may associate exact intent components; Change supplies realized differences; Lineage/Impact may support prospective review without promoting planned topology/effects to realized truth.

## Non-goals

Deployment, realization proof, health, causal attribution, automatic Expectation/Baseline mutation, or change-approval workflow.

## Provenance

- `docs/concepts/phase_002/04_history_lineage_change/change_intent.md`
- `docs/concepts/phase_007/02_change_intent_deployment_realization_realized_change/`
