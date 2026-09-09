# HLTH-063 — Exact-Use Readiness Suitability of Health Evidence

**Status:** Accepted — Phase 006 Group 06

## Purpose

Define whether a specific health/result state is suitable evidence for a particular readiness criterion/opportunity without turning that suitability into readiness or control state.

## Suitability binding

A readiness-suitability evaluation binds:

- exact readiness criterion/profile/version;
- downstream opportunity/use and environment/context;
- exact component/result version being considered;
- required current-cycle/input/output identity;
- evidence sufficiency/coverage;
- availability and conflict state;
- required comparability/reference state;
- result/evidence age and permitted freshness window;
- required analytical horizon/maturity;
- evaluation and knowledge time.

## Rules

- Suitability asks whether the result may legitimately participate in that readiness evaluation; it is independent from whether the underlying result says `meets` or `violates`.
- A fresh, sufficiently evidenced violation can be suitable evidence for `not ready`.
- A stale `meets` result can be unsuitable for the current opportunity.
- A non-comparable relative result, unresolved current-cycle identity, or unavailable required evidence can make suitability unresolved/unavailable.
- Readiness criteria can legitimately require only a narrow operational predicate while broader DQ remains pending, as preserved by REF-024.
- If a readiness criterion explicitly requires a health component, that component must satisfy the exact criterion's evidence/freshness/maturity requirements.
- Suitability does not grant permission to configure or operate a gate.
- Suitability does not itself evaluate the complete readiness criterion when multiple predicates remain.

## Invariant

**health outcome ≠ evidence suitability for readiness ≠ readiness result ≠ gate decision ≠ enforcement ≠ execution**.