# Propagation Safeguard

**Canonical key:** `concept.propagation_safeguard`

**Kind:** CONCEPT

**Authority:** CANDIDATE / NOT CURRENT AUTHORITY

**Migration record:** `concept.propagation_safeguard`

**Owns current question:** What output/publication/consumption protection was proposed, authorized, requested, effectively enforced, extended, expired, or released for a bounded state/path/cohort/time?

**Stable IDs:** N/A

## Current semantics

Propagation Safeguard owns exact suspect/protected state or missing-output/current-cycle context; protection surface/path/cohort/environment; proposal, authorization, request, enforcement, extension, expiry and release propositions; evidence/provenance/knowledge time; overlapping safeguard relationships; and history/limitations. Convenience lifecycle labels are summaries over these evidence-backed facts.

## Actions

- `propose` — request consideration of a bounded protective hold/quarantine.
- `activate` — establish active protection only when authority plus effective-enforcement evidence support it.
- `release` — end protection explicitly while preserving the protected interval/evidence.
- `cancel` — withdraw a proposal that never became active.
- `resolveAt` — return bounded protection/enforcement state with provenance/ambiguity.

## Invariants / boundaries

- Propagation Safeguard is protective control state, not Assessment, defect proof, causal truth, or safety proof.
- Proposal ≠ authorization ≠ request ≠ effective enforcement.
- `active` requires sufficient evidence that the bounded protection actually operated; partial enforcement remains partial.
- Missing output is not a quarantined object; protection may hold downstream advancement/current-state presentation instead.
- Safeguard enforcement ≠ prevented exposure. Prevention requires separate Impact/negative-consumption/path-coverage evidence under the accepted REF-028 discipline.
- Safe-prior-state serving, staleness, held advancement, delay and non-delivery remain separate source-owned facts.
- Release ≠ recovered/healthy. Post-release recovery belongs to Observation/Assessment/Impact.
- Execution Gate controls whether execution starts; Propagation Safeguard controls output/current-state propagation/consumption. Gate HOLD/ADMIT and Safeguard activate/release never substitute for one another.
- Safeguard authority ≠ Gate authority ≠ raw-data access.
- Event/effective and knowledge/record time remain distinct; late evidence does not rewrite what protection was believed active then.

## Ambiguity / evidence

Configured/requested protection without external enforcement proof remains activation-unknown. Conflicting/unavailable control telemetry does not prove fallback behavior.

## Synchronizations / related canonical resources

Assessment/Investigation may motivate protection; Lineage/Impact help bound candidate surfaces; Capability Authorization governs actions; Gate remains independent; Execution/Observation/Impact expose consequences; Causal Claim owns broader control-effect attribution; Explanation exposes authorized protection state.

## Non-goals

Health determination, causal attribution, Gate/start-admission control, incident policy, access control, rollback, data deletion, or enforcement-product selection.

## Provenance

- `docs/concepts/phase_002/addenda/propagation_safeguard.md`
- `docs/concepts/phase_007/07_propagation_safeguard_scope_enforcement_recovery/`
