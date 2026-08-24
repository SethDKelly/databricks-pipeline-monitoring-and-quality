# REF-003 — Negative, Absence, and Exclusion Evidence

**Status:** Accepted — Phase 004 Group 01

## Outcome

Define when evidence can legitimately support a negative proposition such as `no qualifying run occurred`, `no output exists`, `consumer was not exposed`, `condition was absent`, or `candidate cause is excluded`, while preventing missing telemetry from becoming false reassurance.

## Negative evidence principle

A negative conclusion requires both:

1. a mechanism with an adequate **opportunity to observe** the event/state if it occurred; and
2. sufficient bounded **coverage** of the relevant opportunities/universe for the requested conclusion.

An empty result is not, by itself, evidence of absence.

## Negative-evidence classes

### Observed absence
A successful, applicable observation process positively establishes zero qualifying events/states across a sufficiently covered bounded universe.

Example: a complete query of all qualifying executions for C between the start of the required window and its deadline returns zero runs.

### Non-exposure
Sufficient consumer refresh/version/consumption evidence establishes that the relevant affected state was not encountered during the bounded exposure interval.

### Exclusion / contradiction
Applicable evidence rules out or materially contradicts a proposition within the covered scope—for example, reliable timing evidence establishing that an alleged cause occurred after the outcome had already begun.

### Evidence not found
The framework did not retrieve evidence supporting the proposition. This is **not** automatically observed absence, non-exposure, contradiction, or exclusion.

## Invariants

- No telemetry ≠ no event.
- Query failure ≠ zero results.
- Monitoring outage ≠ no execution/output/refresh/change.
- Restricted evidence ≠ evidence of absence.
- Out-of-scope entity ≠ nonexistent entity.
- No observed contradiction ≠ causal confirmation.
- A negative conclusion must state the scope for which the evidence is adequate; it cannot silently generalize beyond its covered universe.
- Negative evidence may be strong for one dimension and irrelevant to another. Evidence that no refresh occurred can support non-exposure while saying nothing about whether the downstream report remained fresh for business use.
- A historical evidence cut lacking an item does not by itself prove that no actor/system knew it then; exact `not known by cutoff` semantics are refined in Group 02.

## Strength asymmetry

Positive and negative propositions often require different coverage.

- One directly observed qualifying output can be sufficient to support `at least one output existed`.
- Proving `no qualifying output existed` generally requires coverage of every relevant output opportunity in the bounded universe.
- One recorded refresh from version V can establish exposure to V.
- Proving `not exposed to V` requires enough refresh/consumption coverage to rule out relevant encounter paths.

This is a logical asymmetry, not a rule that positive evidence is always stronger.

## Causal exclusion

To reject or weaken a causal hypothesis using negative/exclusion evidence, the exclusion evidence must be applicable to the causal proposition and adequately cover the relevant causal window/mechanism.

Examples:

- reliable evidence that Deployment D activated after the degradation began can contradict a claim that D initiated the degradation;
- evidence that A remained stable can weaken an A-related hypothesis only when the monitored A dimensions and interval sufficiently cover the proposed mechanism;
- lack of an observed A anomaly does not exclude A if the relevant A property was not measured.

## Security / authorization

A requester may be authorized to see a safe negative conclusion and its coverage limitation without seeing restricted evidence details. If the framework itself cannot access the evidence needed to establish the negative, the result remains insufficient/unavailable.

## Non-goals

- defining exact exposure evidence for every consumer class;
- defining exact gate-readiness proof;
- causal confirmation;
- universal source authority;
- legal/compliance absence certification.
