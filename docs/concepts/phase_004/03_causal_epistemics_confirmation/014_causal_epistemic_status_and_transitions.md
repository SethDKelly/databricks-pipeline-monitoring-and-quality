# REF-014 — Causal Epistemic Status Vocabulary and Transition Semantics

**Status:** Accepted — Phase 004 Group 03

## Purpose

Define a bounded Causal Claim status vocabulary whose meanings are evidence-based, historically traceable, and usable without a universal confidence score.

## Accepted status vocabulary

### `proposed`
The causal proposition has been explicitly formed but has not yet received enough applicable evaluation to justify a stronger epistemic result.

### `supported`
Applicable evidence materially supports the proposition under relevant causal dimensions. Support is stronger than plausibility but remains below confirmation. Material known limitations and contradiction remain visible.

### `weakened`
Material evidence, contradiction, coverage limitation, or alternative explanation has reduced support for the proposition, but the evidence is not sufficient to reject it.

### `unresolved`
The proposition has been substantively evaluated, but the available applicable evidence remains materially insufficient, conflicting, non-discriminating, unavailable, or restricted such that support/rejection/confirmation cannot be justified.

### `rejected`
Applicable evidence is sufficient under the relevant claim/rejection standard to establish that the causal proposition should not be retained as a supported explanation. Examples can include sufficiently evidenced temporal impossibility or failure of a required transmission condition. Rejection is not mere lack of support.

### `confirmed`
The proposition satisfies an explicit accepted confirmation profile/standard and the required confirmation authority/capability has been resolved and exercised with provenance.

## Transition semantics

- Status evolution is not a mandatory linear ladder.
- `proposed` may become supported, weakened, unresolved, rejected, or—only if a valid confirmation path already exists—confirmed.
- `supported` may later become weakened, unresolved, rejected, or confirmed.
- `confirmed` is challengeable; materially new evidence can produce a later current status of supported, weakened, unresolved, or rejected while preserving historical confirmation.
- `unresolved` is not equivalent to `proposed`: unresolved means substantive evaluation has occurred but cannot discriminate adequately.
- `rejected` is not equivalent to `not selected` or `lower ranked`.
- Investigation closure does not change claim status.

## Historical semantics

Every status revision retains knowledge/evaluation time, evidence/standard basis, and prior status. A replay-derived current evaluation of historical evidence does not prove that the same status was actually recorded then.

## Non-goals

- numeric confidence scoring;
- forcing every user-facing interface to expose every status word verbatim;
- organizational approval workflow.
