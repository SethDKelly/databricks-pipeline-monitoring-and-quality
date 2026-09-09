# Execution Gate

**Canonical key:** `concept.execution_gate`

**Kind:** CONCEPT

**Authority:** CANONICAL CURRENT AUTHORITY

**Migration record:** `concept.execution_gate`

**Owns current question:** For an explicitly configured downstream execution opportunity, what readiness decision/control action/enforcement evidence governs whether this Gate barrier permits start?

**Stable IDs:** N/A

## Current semantics

Execution Gate owns exact gate/config/profile revision, downstream target/environment, execution opportunity/cycle/window, prerequisite/criterion profile, configuration/enabled state, readiness evaluation, normal decision (`hold`/`admit`), override/fallback/escalation bases, decision issuance/delivery/acknowledgement/effective-enforcement evidence, timeout/expiry/cancellation, authority/provenance, event/decision/knowledge time, and history/conflict.

## Actions

- `register` — bind a target/opportunity class to explicit Gate criteria without proving enforcement.
- `evaluate` — resolve prerequisite evidence as ready/not-ready/unknown/conflicting/unavailable/unauthorized.
- `hold` — issue/establish non-admission for the bounded opportunity where control semantics/evidence support it.
- `admit` — remove this Gate barrier under the declared criterion.
- `override` — record an authorized exception without transforming underlying readiness.
- `retire` — end configuration prospectively.
- `resolveAt` — return configuration/decision/enforcement context for target/opportunity/time.

## Invariants / boundaries

- Passive monitoring is not an Execution Gate; gating is opt-in active control.
- Gate configuration/enabled state ≠ opportunity-specific readiness ≠ Gate decision ≠ action delivery/acknowledgement ≠ effective enforcement ≠ actual execution.
- Health outcome ≠ evidence suitability ≠ readiness ≠ Gate decision.
- `held` ≠ failed execution; `admit`/`override` ≠ execution occurred.
- Override preserves `not ready`/`unknown`/`conflicting`/`unavailable` and requires its own Capability Authorization.
- Fallback is pre-authorized declared policy behavior; configured fallback ≠ trigger occurred ≠ fallback applied ≠ enforced.
- HOLD enforcement is contradicted by reliable applicable downstream start; conversely no run proves HOLD only with sufficient opportunity/Execution History coverage.
- ADMIT means this Gate barrier was removed, not that the Gate caused a run.
- Prerequisite becoming ready does not automatically admit unless explicit reevaluation/action semantics say so.
- Timeout, opportunity expiry, SLA deadline, cancellation, and escalation are distinct.
- Multiple Gates retain independent barriers; no universal `most restrictive wins` or Gate-effectiveness score is accepted.
- Execution Gate ≠ Propagation Safeguard. HOLD does not protect published state; Safeguard release does not admit execution.
- Gate-induced delay/non-delivery/stale-state consequences are source-owned evidence; broader causal attribution belongs to Causal Claim.
- No universal fail-open/fail-closed behavior is inferred from missing telemetry.

## Ambiguity / evidence

Requested decision without enforcement proof remains distinct from effective blocking/release. Restricted prerequisites can remain opaque.

## Synchronizations / related canonical resources

Lineage supplies declared dependency context; Execution History/Observation/Assessment supply evidence; Capability Authorization governs Gate actions; Safeguard remains independent; Impact/Assessment record consequences; Explanation exposes authorized decision/enforcement state.

## Non-goals

Scheduler replacement, mandatory critical-path monitoring, data-health Assessment, Safeguard state, causal attribution, or control-plane implementation selection.

## Provenance

- `docs/concepts/phase_002/addenda/execution_gate.md`
- `docs/concepts/phase_007/08_execution_gate_fallback_override_control_effects/`
