# Causal Claim

**Canonical key:** `concept.causal_claim`

**Kind:** CONCEPT

**Authority:** CANONICAL CURRENT AUTHORITY

**Migration record:** `concept.causal_claim`

**Owns current question:** What explicit causal/contributing/enabling/preventing proposition is being asserted for a defined outcome, and what is its evidence-backed epistemic status?

**Stable IDs:** N/A

## Current semantics

Causal Claim owns proposition identity; cause condition(s); effect/outcome; causal role; event-time scope; accepted epistemic state (`proposed`, `supported`, `weakened`, `unresolved`, `rejected`, `confirmed`); supporting/contradicting/alternative evidence; rationale/limitations; proposer/reviewer/confirmation provenance; governing evidence/authority basis; and non-rewriting status history.

## Actions

- `propose` — record causal proposition under evaluation.
- `support` — link supporting evidence/rationale without taking ownership of it.
- `contradict` — link weakening/contradicting evidence.
- `reviseStatus` — preserve epistemic-state evolution.
- `confirm` — record confirmation only when accepted evidence and authority gates are satisfied.
- `reject` — record sufficiently contradicted/rejected status while preserving history.

## Invariants / boundaries

- Causal Claim is a proposition, not Observation, Assessment, Change, Investigation lead, or independent fact.
- Temporal proximity, Lineage reachability, Deployment activation, first deviation, or intent consistency do not establish causation.
- Multiple contributing/competing claims may coexist; a single root cause is not required.
- Supporting and contradicting evidence can coexist; lack of contradiction is not proof.
- `confirmed` requires the accepted REF-017 evidence gate and AUTH-034 authority gate; Investigation closure, human title, model ranking, service identity, or operational resolution cannot manufacture it.
- Previously confirmed state remains challengeable/supersedable when later evidence changes the picture, without rewriting what was known/confirmed then.
- No universal numeric confidence score is accepted.

## Ambiguity / evidence

Claims may remain proposed/supported/unresolved indefinitely. Restricted evidence can constrain visible rationale without strengthening the status.

## Synchronizations / related canonical resources

Investigation organizes claims; source concepts provide evidence/context; Impact uses separate Causal Claims for attribution; Explanation must preserve exact causal role/status and limitations.

## Non-goals

Hypothesis-generation algorithms, correlation-as-cause, numerical confidence model, source-state mutation, or universal legal/audit causal guarantees.

## Provenance

- `docs/concepts/phase_002/05_investigation_impact_explanation/causal_claim.md`
- `docs/concepts/phase_004/`
- `docs/concepts/phase_005/`
- `docs/concepts/phase_007/05_investigation_localization_causal_handoff/`
