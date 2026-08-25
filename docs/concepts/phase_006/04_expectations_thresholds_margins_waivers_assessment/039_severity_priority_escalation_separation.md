# HLTH-039 — Severity, Priority & Escalation Separation from Criterion Outcome

## Purpose

Prevent consequence/priority metadata from becoming health truth.

## Rule

Severity, priority, escalation class or response urgency may be attached to a criterion/result according to governed semantics, but remain separate from whether the criterion is met or violated.

Examples:

- a low-severity criterion can still be violated;
- a high-severity criterion can currently be met;
- a warning/proximity state can have elevated attention without being a violation;
- criticality can influence priority without changing the threshold or current result.

## Invariants

- Severity does not decide `meets` versus `violates`.
- Highest severity does not resolve conflicting normative rules.
- Criticality Classification does not automatically assign failure severity or prove Impact.
- Escalation/notification state does not prove actual operational consequence.
- Severity changes are versioned/governed and do not rewrite historical criterion outcomes.
- Composite health, if later defined, must not use severity as hidden authority or evidence.

## Non-goals

- incident priority taxonomy;
- notification routing;
- Impact/consequence determination;
- overall health scoring.