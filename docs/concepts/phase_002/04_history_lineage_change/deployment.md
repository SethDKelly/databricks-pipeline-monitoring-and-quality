# Concept: Deployment

**Status:** Accepted — Phase 002 Group 04; refined by Phase 007 Group 02 (OPS-011–OPS-013, OPS-016, OPS-018–OPS-019)

## Purpose

Let users reconstruct which source/configuration state was attempted and which state was actually active for a runtime target at a relevant time.

## Operational principle

A registered Change Intent is implemented in a repository revision and a deployment workflow attempts to apply it to production. Deployment records the attempt and later activation evidence. Table C's first post-activation execution shows a volume shift. Deployment establishes which revision/configuration was active and when; it does not prove the intended filter actually produced the shift or that the shift was acceptable.

## Actors

- Data Engineer / Pipeline Maintainer
- Data Platform Administrator
- Monitoring framework
- Git/source-control and deployment-system sources
- Databricks/runtime configuration sources

## State

- deployment identity;
- source revision/configuration reference(s);
- identified deployment target/environment;
- deployment attempt time/status/outcome;
- activation/effective time when established;
- supersession/deactivation/rollback context;
- provenance/evidence source and knowledge time;
- relationship to earlier/later active deployments;
- associated Change Intent reference(s) when known;
- ambiguity/conflict about active state or configuration.

## Actions

### `recordAttempt`
- **Intent:** record a deployment attempt and source/target context without assuming activation.

### `recordActivation`
- **Intent:** establish from evidence that a deployment/configuration became active for a target at a relevant time.
- **State effect:** creates activation history; workflow success alone is insufficient unless it is the accepted activation evidence.

### `supersede`
- **Intent:** end effective activation because another deployment/configuration became active, including rollback/reversion cases.
- **State effect:** preserves historical activation intervals.

### `associateIntent`
- **Intent:** link deployment evidence to a registered Change Intent when sufficient source/revision/context evidence establishes the relationship.
- **Important:** association does not prove that the intended effect occurred.

### `resolveActiveAt`
- **Intent:** determine which deployment/configuration state was known active for a target/time.
- **Observable result:** active deployment(s), unknown, ambiguous/conflicting, unauthorized, or unavailable.

## Invariants / behavioral expectations

- Deployment attempt is not Deployment activation.
- Deployment/workflow success is not proof of healthy output.
- Deployment activation is not proof that a Change Intent's anticipated effect occurred.
- Temporal proximity between Deployment and data Change is correlation, not causation.
- Deployment history is distinct from data Lineage and Execution History.
- Configuration-only changes are representable even when source revision is unchanged.
- Rollback/reversion creates historical deployment state; it does not erase the intervening activation.
- Repository is provenance context, not the logical pipeline boundary.
- Event/effective time and knowledge/record time remain distinguishable where evidence arrives late.

## Phase 007 Group 02 refinement

OPS-011 rejects a universal deployment/version token. A deployment may reference source revision, build/package, job/transformation definition, configuration, schema/interface version and other source-defined implementation facets. These retain their own identity/provenance rather than being collapsed into the current repository commit.

The active state may be composite, for example **code R2 + configuration K7 + schema S3 + transformation T5**. Facets can activate independently and several Deployments can collectively establish the then-active operating state.

OPS-012 sharpens Deployment into separate propositions:

**attempt → attempt outcome → target/facet activation → active-state interval → supersession/deactivation**.

A successful deployment mechanism outcome is not activation unless the evidence standard for that exact target pattern establishes it. Active-state resolution preserves `established`, sufficiently evidenced `not established`, `unknown`, `conflicting`, and `unavailable` as applicable; missing telemetry is not a negative fact.

OPS-013 binds intent association to an exact intent revision/component, target and implementation facet with provenance-bearing linkage. Association is many-to-many and can concern an attempt even when activation later fails.

OPS-016 keeps canary/region/cohort/target activation slice-specific. One successful slice does not globally activate every target and no percent-complete value is inferred merely from target counts.

OPS-018 separates supersession/deactivation, rollback action/intent, realized reversion, bounded restoration/equivalence and roll-forward. Reactivating a prior revision creates a new activation interval and does not erase the superseded interval. Code/configuration rollback does not itself restore data, topology, schema migrations, exposure or health.

OPS-019 requires event/effective time plus framework knowledge time. Late evidence may correct active-state intervals retrospectively while preserving what was known at an earlier cutoff.

Specific implementation/version use by an actual execution remains separate and is refined in Phase 007 Group 04.

## Ambiguity and missing evidence

A workflow may report completion while runtime activation remains unknown. Different sources may disagree about the active revision/configuration. The product preserves ambiguity rather than guessing activation from commit/merge/workflow timestamps alone.

## Synchronizations

- **Entity Identity** identifies repository, target, logical pipeline, and related entities.
- **Change Intent** supplies planned modification context and can be associated to realizing deployments.
- **Execution History** can resolve the active Deployment for a run when evidence permits.
- **Change** can describe a realized code/configuration transition or later data/schema/topology differences without making Deployment itself the change's cause.
- **Lineage** remains separate; deployment provenance must not be silently encoded as data-derivation edges.
- **Observation/Assessment** can show post-activation behavior while retaining independent evidence/status.
- **Investigation/Causal Claim** later use Deployment as temporal/provenance evidence.

## Security / privacy / governance considerations

Deployment metadata can expose repository names, revisions, environment topology, feature/configuration flags, security controls, or sensitive change context. Viewer disclosure may need abstraction.

## Evidence / provenance considerations

Attempt, activation, target, revision/configuration, supersession, rollback, intent association, source event time, and knowledge time should remain provenance-bearing. Historical replay must identify what was believed active at incident time and any later corrections.

## Representative scenarios

### Planned change activated
A registered filter Change Intent maps to revision R2. Deployment evidence establishes R2 active at 10:00. The first post-activation run can be identified without asserting that R2 caused its data state.

### Workflow success, activation unknown
GitHub Actions succeeds but no trustworthy runtime evidence confirms the Databricks target changed. The deployment remains attempted/successful-at-workflow but activation is unknown.

### Configuration-only change
A runtime configuration value changes without a new code revision. Deployment records the configuration state transition and activation context.

### Rollback
R2 becomes active, later R1-equivalent configuration is restored. Historical reconstruction preserves both activation intervals rather than rewriting R2 away.

### Unregistered deployment
A deployment occurs without Change Intent. The deployment is still recorded; lack of intent is contextual absence, not proof of an invalid deployment.

## Non-goals

- executing/approving deployments;
- source-code review;
- proving business/data effects;
- causal attribution;
- data derivation lineage;
- choosing GitHub Actions as a permanent required deployment architecture.

## Deferred questions

- authoritative/sufficient activation evidence for representative Databricks deployment patterns belongs to Phase 009 source mapping;
- concrete configuration/build/runtime identity extraction belongs to Phase 009/010;
- how one deployment maps to multiple jobs/pipelines/targets is functionally supported by OPS-011/OPS-016, while source realization remains later work;
- minimal linkage to pull requests/releases/change tickets for MVP remains Phase 009 integration design.
