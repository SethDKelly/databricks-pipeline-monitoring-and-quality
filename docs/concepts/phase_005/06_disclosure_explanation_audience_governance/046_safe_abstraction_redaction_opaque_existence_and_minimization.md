# AUTH-046 — Safe Abstraction, Redaction, Opaque Existence, and Minimization

**Status:** Accepted — Phase 005 Group 06

## Purpose
Define disclosure-preserving abstraction so restricted detail can be minimized without creating false absence, false precision, or a materially different conclusion.

## Contract
An authorized projection may use:
- exact state when permitted;
- coarser categorical or range-based state when separately permitted;
- redacted identity/detail;
- opaque existence/reference when existence may be disclosed but identity/detail may not;
- explicit restricted-detail limitation;
- complete omission when even existence is not disclosable.

## Invariants
- Redaction is not declassification.
- Opaque existence may be shown only when existence itself is authorized.
- `restricted upstream evidence exists` must not become `no upstream evidence`.
- A range/category cannot be substituted for an exact value unless the abstraction is semantically valid and authorized.
- Minimization must preserve relevant status distinctions such as unknown versus negative, supported versus confirmed, reachable versus exposed, and configured versus enforced.
- Redaction should avoid revealing hidden identity through unique labels, counts, topology shape, timing, or surrounding detail.
- Group 06 defines functional disclosure semantics, not a redaction technology.
