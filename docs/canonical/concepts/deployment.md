# Deployment

**Canonical key:** `concept.deployment`

**Kind:** CONCEPT

**Authority:** CANONICAL CURRENT AUTHORITY

**Migration record:** `concept.deployment`

**Owns current question:** Which implementation/configuration facets were attempted and which were evidenced active for a target/time?

**Stable IDs:** N/A

## Current semantics

Deployment owns deployment identity; source revision/build/config/schema/transformation facets; target/environment; attempt/outcome; facet-specific activation/effective interval; deactivation/supersession/rollback; provenance/knowledge time; exact Change Intent associations; and ambiguity/conflict. Active operating state may be composite across independently activated facets.

## Actions

- `recordAttempt` — record attempt + source/target context without activation claim.
- `recordActivation` — establish target/facet activation from sufficient evidence.
- `supersede` — end an active interval, including rollback/reversion, without deleting it.
- `associateIntent` — link exact intent revision/component where provenance supports it.
- `resolveActiveAt` — return established active state, sufficiently evidenced negative where applicable, unknown, conflicting, unauthorized, or unavailable.

## Invariants / boundaries

- Deployment attempt ≠ mechanism outcome ≠ target/facet activation ≠ active interval.
- Workflow success is not activation unless accepted evidence semantics establish it for that target pattern.
- Activation ≠ healthy output ≠ intended-effect realization ≠ causality.
- No universal deployment/version token is accepted; implementation facets retain identity/provenance.
- Phased/canary/region/cohort activation is slice-specific; one slice does not globally activate all targets.
- Rollback/reversion creates new historical state; it does not restore data/topology/schema exposure/health by assertion.
- Active-at-time does not automatically bind the implementation actually used by one run.
- Event/effective time ≠ knowledge/record time.

## Ambiguity / evidence

Completion may be known while activation remains unknown. Conflicting runtime/source evidence remains explicit instead of choosing commit/workflow timestamps by convenience.

## Synchronizations / related canonical resources

Change Intent supplies planned context; Execution History may bind run-specific use; Change owns realized state differences; Observation/Assessment describe behavior; Causal Claim owns causal propositions.

## Non-goals

Deployment execution/approval, source review, business/data effect proof, causal attribution, Lineage ownership, or vendor-specific deployment architecture.

## Provenance

- `docs/concepts/phase_002/04_history_lineage_change/deployment.md`
- `docs/concepts/phase_007/02_change_intent_deployment_realization_realized_change/`
