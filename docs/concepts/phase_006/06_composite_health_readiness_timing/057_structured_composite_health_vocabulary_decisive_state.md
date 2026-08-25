# HLTH-057 — Structured Composite Health Vocabulary & Decisive-State Semantics

**Status:** Accepted — Phase 006 Group 06

## Purpose

Define useful composite health labels without collapsing component detail or introducing a universal numeric score.

## Structured summary

A composite may expose a primary summary plus retained qualifiers/component detail. For a conjunctive profile, examples include:

- **healthy** — all applicable required components resolve `meets` and no required component is unresolved;
- **healthy with warning** — the healthy condition above holds and one or more applicable warning/proximity conditions are active;
- **degraded** — at least one applicable required component resolves `violates` under the explicit composition logic;
- **indeterminate** — no decisive violation is established, but one or more required components are indeterminate/insufficient;
- **conflicting** — no decisive result can be completed because required component/rule evidence is conflicting;
- **unavailable** — required evidence/result is unavailable and no stronger result is established under the rule;
- **not applicable** — the composite itself is not applicable under the bound profile/context.

## Rules

- These labels are derived shorthand over component Assessments, not replacements for them.
- Explicit OR/conditional/alternative composition can produce different resolution behavior and must be evaluated according to its own rule.
- A known required violation may make the composite `degraded` even while other components remain unresolved; those unresolved states remain visible as qualifiers rather than being erased.
- `healthy` requires positive evidence for all applicable required predicates under the profile; absence of known failure is insufficient.
- A summary must retain drill-down/provenance sufficient to explain which components determined or limited it.
- No universal numeric health/confidence score is accepted.