# Concept: Deployment

**Status:** Candidate (renamed from Deployment Record)

## Purpose

Let users reconstruct which source revision/configuration deployment was active for a runtime target at a relevant time.

## Operational principle

A GitHub Actions workflow deploys a new revision of a Spark pipeline. A data-volume shift begins on the first run after activation. Deployment can show the temporal association, source revision, target, and supersession history without concluding the deployment caused the shift.

## Actors

- Data Engineer
- Data Platform Administrator
- Monitoring framework
- Git/deployment-system sources

## State

- deployment identity;
- source revision/configuration reference;
- target identity/environment context;
- deployment/activation/supersession timing when known;
- deployment outcome/status;
- provenance from deployment system;
- relationship to earlier/later deployments.

## Actions

### `record`
Records a deployment attempt/outcome with provenance.

### `activate`
Marks/observes a deployment as active for a target/time when evidence establishes it.

### `supersede`
Ends effective activation in favor of a later deployment while preserving history.

### `resolveActiveAt`
Returns the deployment known to be active at a target/time, or ambiguous/unknown.

## Invariants / behavioral expectations

- Temporal proximity is correlation, not causation.
- Deployment history is not data lineage.
- Source revision identity is preserved without assuming repository is the logical pipeline boundary.
- Failed/partial/unknown deployment outcomes must be representable.

## Ambiguity and missing evidence

A deployment attempt may be known while activation is unknown; multiple overlapping targets/configurations may make active-at-time resolution ambiguous. Unknown activation must not be guessed from commit timing.

## Synchronizations

- Asset Identity identifies target/logical pipeline/repository references.
- Execution History can resolve deployment active for a run.
- Change can describe configuration/code deployment transitions.
- Investigation/Causal Claim may cite deployment evidence.

## Security / privacy / governance considerations

Deployment metadata may expose repository names, revisions, environment topology, configuration, or security-sensitive operational context. Access should follow source authority.

## Evidence / provenance considerations

Deployment attempt, outcome, activation, target, revision, and supersession facts retain source-system provenance and time semantics. Associations to executions must be evidence-backed.

## Representative scenarios

### Happy path
A run is associated with the deployment known to be active at its start time.

### Degraded path
A workflow reports success but activation evidence is unavailable, so the active deployment remains uncertain.

### Conflicting evidence
GitHub Actions and Databricks metadata imply different active revisions; both are preserved.

### Unauthorized evidence
A business viewer may see that a recent deployment occurred without seeing repository or revision details.

## Non-goals

- performing deployments;
- interpreting source-code diffs as causes;
- deployment authorization/workflow design;
- data derivation lineage.

## Open questions

- What evidence proves activation versus deployment attempt?
- How are configuration-only changes represented when source revision is unchanged?
