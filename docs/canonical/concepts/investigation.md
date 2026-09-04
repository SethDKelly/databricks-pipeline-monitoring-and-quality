# Investigation

**Canonical key:** `concept.investigation`

**Kind:** CONCEPT

**Authority:** CANDIDATE / NOT CURRENT AUTHORITY

**Migration record:** `concept.investigation`

**Owns current question:** How is a bounded inquiry organized around a question/outcome/scope/time/knowledge cut without becoming source truth or causal truth?

**Stable IDs:** N/A

## Current semantics

Investigation owns inquiry identity, exact question/outcome, subject/scope/time/knowledge cut and scope revision history, linked evidence with inquiry roles, linked Causal Claims/Impact/Annotations, lead/localization organization, lifecycle (`open`, `active`, `paused`, `closed`), material gaps/restrictions/conflicts, and closure/reopen history.

## Actions

- `open` — create a bounded inquiry.
- `linkEvidence` — reference source-owned evidence without copying/mutating it.
- `linkClaim` — associate a Causal Claim without endorsement.
- `linkImpact` — associate downstream Impact analysis.
- `refineScope` — revise inquiry scope non-rewriting.
- `close` — record operational inquiry closure without causal promotion.
- `reopen` — resume after material new evidence/question while preserving prior closure.

## Invariants / boundaries

- Investigation organizes inquiry; it owns neither Observation/Assessment/Impact nor causal truth.
- It may begin from a question even without degraded Assessment.
- No single root cause is required; multiple leads/claims and unresolved closure are valid.
- Lead/localization state is Investigation-owned organization, not Causal Claim epistemic status.
- First observed deviation, earliest evidenced change, reconciliation/transformation boundary, first consumer effect, Lineage distance, shared version, retry/rollback contrast are localization/evidence—not cause.
- Cause/contribution/enabling/triggering/preventing/material-influence language must hand off to Causal Claim.
- Closing Investigation never confirms a claim; operational resolution can coexist with unresolved/non-confirmed causality.
- Evidence contradiction/gaps/common derivation and bitemporal reopen history remain visible.

## Ambiguity / evidence

Missing/conflicting/restricted/late evidence remains explicit; lack of evidence for a lead is not proof it is false, and lack of contradiction is not proof it is true.

## Synchronizations / related canonical resources

All evidence-owning concepts can be linked; Causal Claim owns causal propositions, Impact downstream state, Annotation human context, Explanation authorized synthesis.

## Non-goals

Incident/ticket workflow, automatic causality proof, Impact truth, remediation, authorization widening, or agent implementation.

## Provenance

- `docs/concepts/phase_002/05_investigation_impact_explanation/investigation.md`
- `docs/concepts/phase_007/05_investigation_localization_causal_handoff/`
