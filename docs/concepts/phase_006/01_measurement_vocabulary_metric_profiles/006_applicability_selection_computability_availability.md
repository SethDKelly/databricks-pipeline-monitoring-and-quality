# HLTH-006 — Applicability, Selection, Computability & Availability Separation

**Status:** Accepted — Phase 006 Group 01

## Purpose

Prevent non-results and non-applicable measurements from being collapsed into pass/fail or zero-value health conclusions.

## Orthogonal dimensions

### Semantic applicability
Does the metric/check make sense for this exact subject, field/relationship, grain, transformation, consumer and context?

Accepted functional states include:

- `applicable`;
- `not applicable`;
- `applicability unknown`;
- `applicability conflicting`.

### Profile selection
Is the metric/check currently governed for routine or diagnostic use?

Representative states include:

- `selected`;
- `not selected`;
- `diagnostic/on-demand`;
- `suspended/retired` where governed history requires it.

### Technical computability/support
Can the required definition be produced from available source capabilities in principle?

Representative states include:

- `supported`;
- `unsupported`;
- `support unknown`.

This is functional source capability, not current runtime availability and not architecture selection.

### Current evidence/evaluation availability
Was a qualifying metric/check Observation actually available/evaluated for the requested window/cut?

Representative states include:

- `observed/evaluated`;
- `pending/not yet evaluated`;
- `unavailable`;
- `evaluation failed/incomplete` where the distinction is evidence-relevant.

### Assessment outcome
Only after an applicable observation/comparison basis exists can a later Assessment resolve normative/comparative health status.

## Invariants

- `not applicable` ≠ `pass`.
- `not selected` ≠ `healthy` and ≠ `not applicable`.
- `unsupported` ≠ `unavailable`.
- `unavailable` ≠ `zero`, `empty`, `false`, or `pass`.
- `pending` ≠ `unavailable` and ≠ `pass`.
- `applicability unknown/conflicting` must remain unresolved rather than being evaluated under guessed semantics.
- A profile-selected metric can still be non-applicable after a structural/semantic change; profile governance and health applicability are separate.
- A semantically applicable metric may be intentionally unselected to control bloat/cost.
- Runtime/source failure does not prove an adverse or clean business condition; it limits the evidence that can be evaluated.

## Examples

- Quantiles for an opaque identifier can be `not applicable` even if the platform can compute them.
- Null rate for a critical field can be `applicable + selected + supported + unavailable` when telemetry is temporarily inaccessible.
- A high-cardinality diagnostic distribution metric can be `applicable + diagnostic/on-demand` without routine evaluation.
- A metric removed from the governed profile can remain historically observed while current selection is `retired`.
