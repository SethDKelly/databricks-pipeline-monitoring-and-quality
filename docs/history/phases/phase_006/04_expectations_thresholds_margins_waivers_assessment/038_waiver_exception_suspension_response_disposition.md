# HLTH-038 — Waiver, Exception, Suspension & Response-Disposition Semantics

## Purpose

Represent bounded normative exceptions without rewriting underlying evidence or criterion outcome.

## Rule

Where a criterion remains applicable for evaluation but an authorized waiver/exception changes required response, Assessment preserves both:

- the underlying criterion result; and
- the effective waiver/exception/suspension disposition and scope.

A governing rule can alternatively make a criterion explicitly non-applicable for a bounded context; that is distinct from `violates but response waived` and must be represented according to the rule's actual semantics.

Waiver state binds subject/criterion/context/effective interval and any relevant conditions/expiry.

## Invariants

- `violates + waived` is not `meets`.
- Waiver does not change Observation, Baseline, structural compatibility evidence or historical fact.
- Expired/revoked waivers do not apply prospectively and do not rewrite earlier legitimate waived periods.
- A waiver for alerting does not automatically waive Execution Gate eligibility or another consequence unless explicitly scoped.
- Missing/unknown waiver evidence is not a waiver.
- Waiver can affect escalation, response or control eligibility only according to its explicit governed scope.

## Non-goals

- authority to create/approve waivers;
- alert/workflow implementation;
- universal exception hierarchy.