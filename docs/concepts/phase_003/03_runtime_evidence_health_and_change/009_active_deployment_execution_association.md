# SYN-009 — Active Deployment ↔ Execution Context Association

**Status:** Accepted — Phase 003 Group 03

## Later refinement — Phase 007 Group 04

OPS-041–OPS-042 refine this synchronization: Deployment active-state history is **execution context**, not universal proof that a run used every active code/config/schema/transformation facet. Run-specific implementation binding requires sufficient evidence for the exact facet. A long-running execution spanning activation/rollback may remain on the prior state, bind later tasks differently, observe dynamic configuration selectively, or remain indeterminate.

There is no universal rule that `active at run start`, `active at completion`, or `latest active deployment` defines the run's implementation state.

## Outcome

Reconstruct which source/configuration state was active for an actual execution and, where evidence supports it, which implementation-state facets the execution actually used, without treating deployment timing as output health or causation.

## Participating concepts and actions

- **Execution History** — `resolveAt`, `associateExecution`, `associateImplementationState`.
- **Deployment** — `resolveActiveAt`.

## Trigger / initiating condition

An execution is recorded/reconstructed or a runtime-health/investigation inquiry needs deployment context for a run.

## Preconditions

Execution identity/time and deployment target context are sufficiently resolved for the proposition being asked.

## Coordination semantics

1. Resolve the actual execution lifecycle/time window under Execution History/OPS-034–OPS-048.
2. Resolve Deployment state applicable to the target at relevant execution boundaries.
3. Treat active Deployment state as context/constraining evidence rather than automatic run-version proof.
4. Associate an execution with a specific implementation facet only where run-specific/runtime binding semantics and evidence support the mapping.
5. Preserve `active at launch/submission`, `active at start`, `active during execution`, `activation changed while running`, and run/task-specific binding distinctions when material.
6. If deployment context or run-specific binding is unknown, retain the valid execution rather than discarding or guessing it.
7. Preserve composite state: code/build, job/transformation definition, configuration, schema/interface and target facets may resolve independently.

## State and evidence effects

Execution History owns execution continuity and run-specific implementation association. Deployment owns activation state. The synchronization owns no run-health, intended-effect or cause state.

## Ambiguity / failure propagation

A long-running execution that spans a configuration/deployment transition may be ambiguous unless runtime evidence establishes which state/facet it actually used. A run queued under one state but started after another activates may still use the earlier state if applicable evidence establishes that binding. Conflicting deployment/runtime sources remain conflict. Missing Deployment evidence does not invalidate run evidence.

## Temporal semantics

Execution submission/start/completion and Deployment activation/supersession intervals remain separate event times with independent knowledge times. Run-specific binding time may differ by implementation facet/task and should not be collapsed when material.

## Provenance / traceability

The association retains evidence for execution identity, target, active-state context, run-specific implementation binding and any ambiguity/conflict.

## Security / authorization

A user may be shown that a changed configuration applied without seeing restricted revision/configuration detail.

## Invariants

- Deployment attempt ≠ activation;
- activation ≠ execution;
- active-at-time ≠ run-specific use by default;
- one known implementation facet ≠ complete run implementation state;
- execution success ≠ output health;
- association ≠ intended-effect conformance/causation;
- current active deployment is not projected backward onto historical runs.

## Scenarios

First post-change run; queued-before-activation run; rollback interval; run spanning activation; dynamic configuration change; missing deployment context; cross-job logical execution.

## Non-goals

Run scheduling, quality evaluation, root cause, deployment implementation, or selecting runtime attestation/fingerprinting sources.