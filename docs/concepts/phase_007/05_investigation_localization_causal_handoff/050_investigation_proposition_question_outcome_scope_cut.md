# OPS-050 — Investigation Proposition, Question, Outcome, Scope & Knowledge Cut

**Status:** Accepted — Phase 007 Group 05

## Purpose

Bind every material Investigation to the exact question/outcome being investigated so evidence collection and localization do not silently change the proposition.

## Contract

An Investigation binds, as applicable:

- investigation identity;
- initiating question, symptom, uncertainty or outcome;
- subject/entity/interface/population/use scope;
- event/effective-time window;
- investigation evaluation time and historical knowledge cut when relevant;
- originating trigger/reference;
- authorized visibility context;
- explicit scope limitations.

The question may be operational, comparative, normative, causal-adjacent or user-directed. Opening an Investigation does not assert that a defect, cause or incident exists.

## Scope revision

If evidence changes the question, subject set or time window, record a scope revision with provenance and knowledge time. Do not rewrite the original inquiry into the later one.

A broad question such as `Why did C volume change?` is not equivalent to `Did Deployment D cause C completeness failure?`; the latter contains a causal proposition and requires an explicit Causal Claim if asserted.

## Invariants

- Investigation question ≠ presumed cause.
- Trigger ≠ outcome truth.
- Current scope ≠ historical scope.
- Latest evidence cut ≠ what was known when the Investigation opened.
- Broadening/narrowing scope does not mutate source evidence.
