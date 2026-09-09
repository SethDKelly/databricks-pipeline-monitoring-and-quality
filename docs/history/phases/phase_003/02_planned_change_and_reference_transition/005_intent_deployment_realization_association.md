# SYN-005 — Change Intent ↔ Deployment Realization Association

**Status:** Accepted — Phase 003 Group 02

## Outcome

Associate registered planned modifications with the Deployment attempts/activations that may realize them, so later reasoning can distinguish intended context from what became active without treating temporal proximity or deployment success as proof of intended effect.

## Participating concepts and actions

- **Change Intent** — `resolvePlannedAt`.
- **Deployment** — `recordAttempt`, `recordActivation`, `associateIntent`, `resolveActiveAt`, `supersede`.

## Trigger / initiating condition

Deployment attempt/activation evidence or change-management/source-revision evidence becomes available for a target that may relate to one or more registered Change Intents.

## Preconditions

- involved targets/revisions/configurations/environments resolve to appropriate Entity Identities/context;
- sufficient linkage evidence exists to distinguish genuine realization association from mere timing/name similarity.

## Coordination semantics

1. Record Deployment attempts independently of whether Change Intent exists.
2. Resolve relevant Change Intents for the target/context/time.
3. Use source revision, configuration identity, target/environment, explicit change references, or other provenance-bearing evidence to determine whether `Deployment.associateIntent` is justified.
4. Preserve many-to-many behavior:
   - one Deployment may realize several Change Intents;
   - one Change Intent may require several Deployments/targets/phases.
5. Record activation separately from attempt and association. A successful workflow/attempt is not silently converted into activation.
6. Association + activation establishes that planned implementation context may have become active; it does **not** establish that anticipated data effects occurred, that all intent details were realized, or that the result is healthy.
7. An unregistered Deployment remains fully representable; planned context is absent/unknown rather than fabricated.
8. Rollback/reversion is recorded through Deployment supersession/activation history and does not erase the original association or activation interval.

## State and evidence effects

Change Intent owns planned context. Deployment owns attempts, activation intervals, active configuration/source state, rollback/supersession, and the evidence-backed association to intent. Synchronization owns no deployment-status aggregate.

## Ambiguity / failure propagation

- intent exists but no Deployment evidence → intent remains unrealized/unknown, not activated;
- Deployment exists but no intent → valid unregistered deployment context;
- workflow success + runtime activation unknown → activation remains unknown;
- several plausible intents match one deployment without sufficient linkage → association remains ambiguous rather than selecting the nearest one;
- conflicting active-state sources → preserve Deployment conflict;
- unauthorized change/revision details may be represented as opaque intent/deployment association where permitted.

## Temporal semantics

Preserve attempt time, activation/effective time, intent registration time, intended activation context, association knowledge time, and any later correction. Late intent/deployment linkage can enrich retrospective reasoning but cannot rewrite what the system knew contemporaneously.

## Provenance / traceability

An association must be explainable through its source revision/configuration/target/change references or other accepted linkage evidence. “Occurred near the same time” is not sufficient provenance by itself.

## Security / authorization

Repository/revision names, environments, future changes, and deployment topology can be sensitive. Association visibility may be abstracted without broadening access to source code or runtime configuration.

## Invariants

- attempt ≠ activation;
- association ≠ activation;
- association + activation ≠ intended effect realized;
- temporal proximity ≠ association proof ≠ causation;
- unregistered deployment remains valid evidence;
- environment/target identity constrains association;
- rollback preserves intervening history.

## Scenarios

**Planned production deployment:** intent references R2/config K; evidence establishes deployment D activates that state in production and D is associated with the intent.

**Workflow only:** CI/CD reports success but runtime state is unknown; attempt is recorded, activation remains unknown.

**Wrong environment:** the same revision activates in development; production intent/reference state does not transition from that fact.

**One deployment, multiple intents:** a release bundle realizes filter and schema intents; both may associate with one Deployment without merging their anticipated effects.

**Late association:** an explicit change record is synchronized after the incident and links D to an earlier intent; retrospective context improves while contemporaneous knowledge remains unchanged.

## Non-goals

Deployment execution/approval, source-code diff interpretation, health Assessment, intended-effect conformance, causal attribution, CI/CD/vendor selection.

## Deferred questions

Minimum MVP linkage evidence, configuration identity, phased-release representation, and authoritative activation sources for representative Databricks patterns.
