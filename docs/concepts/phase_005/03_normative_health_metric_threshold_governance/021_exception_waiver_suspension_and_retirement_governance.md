# AUTH-021 — Exception, Waiver, Suspension, and Retirement Governance

**Status:** Accepted — Phase 005 Group 03

## Purpose

Govern bounded exceptions, waivers, suspensions, and retirement of normative health rules without rewriting Observations, Baseline deviations, historical Assessments, or the rule history itself.

## Contract

A governed exception/waiver/suspension should identify:

- target Expectation/rule/profile and affected subject/context;
- action type: bounded exception, waiver, suspension/non-applicability, or retirement;
- effective interval and expiry/termination condition;
- reason/basis and provenance;
- authorizing holder and any required Capability Authorization;
- whether the action changes applicability, required response, severity/escalation, or another explicitly governed consequence;
- historical correction/supersession state where applicable.

## Invariants

- A waiver does not change the observed metric value or schema state.
- A waiver does not transform a violation into `pass`; the system should preserve that the underlying condition occurred while representing the applicable normative exception/suspension accurately.
- An exception does not rewrite the Baseline or make atypical behavior typical.
- An exception/waiver is bounded; silent indefinite suppression is not an acceptable default.
- Expiry returns evaluation to the then-applicable normative rule; it does not require rewriting the old rule.
- A retrospective correction to a waiver is known only from its actual knowledge time and does not rewrite what responders knew earlier.
- Retirement ends future normative/profile applicability while preserving historical rules, Observations, Assessments, and Explanations.
- Authority to establish a rule does not automatically grant authority to waive or retire it when governance separates those actions.
- Emergency/break-glass override of production control is not defined here; Group 05 owns high-consequence action authority.

## Example

A month-end volume threshold is waived for one known migration window. The observed low volume remains recorded; the applicable normative evaluation reflects the bounded exception rather than reporting a false `healthy/pass` measurement.