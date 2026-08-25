# EXPL-037 — Expectation, Quality, Warning, Waiver & Severity Question

**Status:** Accepted — Phase 008 Group 03

## Requirement

`Did the quality check pass?`, `is this within limits?`, `was it waived?`, and `how severe is it?` remain separate normative/response/priority propositions.

## Rules

- Observation value ≠ criterion result;
- `meets`, `violates`, `indeterminate/insufficient`, `conflicting`, `unavailable`, and `not applicable` retain their source semantics;
- warning/proximity can coexist with `meets`;
- `violates + waived response` remains a violation;
- an exception establishing non-applicability is different from waiver;
- severity/priority/escalation ≠ criterion truth;
- Baseline typicality does not override an explicit Expectation outcome.

Summary wording must not translate waived violation into `healthy`.