# SYN-009 — Active Deployment ↔ Execution Context Association

**Status:** Accepted — Phase 003 Group 03

## Outcome

Reconstruct which source/configuration state was active for an actual execution without treating deployment timing as output health or causation.

## Participating concepts and actions

- **Execution History** — `resolveAt`, `associateExecution`.
- **Deployment** — `resolveActiveAt`.

## Trigger / initiating condition

An execution is recorded/reconstructed or a runtime-health inquiry needs deployment context for a run.

## Preconditions

Execution identity/time and deployment target context are sufficiently resolved.

## Coordination semantics

1. Resolve the actual execution lifecycle/time window.
2. Resolve Deployment state applicable to the target at the relevant execution time.
3. Associate the execution with the active source/configuration only where evidence supports the mapping.
4. Preserve `active at start`, `active during execution`, and `activation changed while running` distinctions when material.
5. If deployment context is unknown, retain the valid execution rather than discarding or guessing it.

## State and evidence effects

Execution History owns execution continuity; Deployment owns activation state. The synchronization owns no run-health or cause state.

## Ambiguity / failure propagation

A long-running execution that spans a configuration transition may be ambiguous unless runtime evidence establishes which configuration it actually used. Conflicting deployment sources remain conflict. Missing Deployment evidence does not invalidate run evidence.

## Temporal semantics

Execution start/completion and Deployment activation/supersession intervals remain separate event times with independent knowledge times.

## Provenance / traceability

The association retains evidence for execution identity, target, active configuration, and any ambiguity.

## Security / authorization

A user may be shown that a changed configuration applied without seeing restricted revision/configuration detail.

## Invariants

- Deployment attempt ≠ activation;
- activation ≠ execution;
- execution success ≠ output health;
- association ≠ causation;
- current active deployment is not projected backward onto historical runs.

## Scenarios

First post-change run; rollback interval; run spanning activation; missing deployment context; cross-job logical execution.

## Non-goals

Run scheduling, quality evaluation, root cause, or deployment implementation.
