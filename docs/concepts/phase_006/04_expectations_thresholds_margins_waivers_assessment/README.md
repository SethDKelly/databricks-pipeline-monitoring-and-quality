# Phase 006 Group 04 — Expectations, Thresholds, Margins, Waivers & Assessment Semantics

**Status:** Accepted — HLTH-030–HLTH-040; H04-01–H04-40 pass

## Goal

Define how applicable Observations and descriptive Baseline comparisons are interpreted against explicit normative Expectations while preserving conflict, bounded exceptions, evidence limitations and underlying measurement truth.

## Accepted contracts

- **HLTH-030 — Normative Criterion Binding & Evaluation Basis**;
- **HLTH-031 — Threshold Direction, Boundary, Unit & Denominator Semantics**;
- **HLTH-032 — Warning Bands, Tolerance Margins & Proximity Semantics**;
- **HLTH-033 — Relative / Reference-Based Criterion Semantics**;
- **HLTH-034 — Evidence Suitability, Uncertainty & Boundary Evaluation**;
- **HLTH-035 — Normative Assessment Result Vocabulary & Basis Separation**;
- **HLTH-036 — Baseline and Expectation Coexistence in Assessment**;
- **HLTH-037 — Multiple Expectations, Composition & Normative Conflict**;
- **HLTH-038 — Waiver, Exception, Suspension & Response-Disposition Semantics**;
- **HLTH-039 — Severity, Priority & Escalation Separation from Criterion Outcome**;
- **HLTH-040 — Historical Criterion/Rule Binding, Correction & Reassessment**.

## Core normative model

Preserve:

**Expectation/criterion ≠ Observation evidence ≠ Baseline comparison ≠ normative Assessment outcome ≠ warning/proximity ≠ severity/priority ≠ waiver/response disposition ≠ composite health**.

No new Threshold, Waiver, Severity, Normative Result or Health concept is required. Expectation owns normative rule state; Observation supplies current evidence; Baseline can supply descriptive/reference evidence; Assessment owns evaluation.

## Criterion binding

A normative criterion must bind enough semantics to make evaluation unambiguous: subject/dimension, exact metric/check/structural definition, grain/population/window/context, operator/direction, inclusive/exclusive boundaries, units/denominator and any explicit reference basis.

`<=2%` and `<2%` are different. `2%` without denominator/population meaning is incomplete. Temporal rules preserve calendar/timezone/window semantics. Structural rules bind the exact contract predicate.

Changing operator, denominator, unit, reference basis or material boundary semantics creates a materially revised criterion/version.

## Warning and tolerance semantics

Warning/proximity bands are secondary normative regions, not a replacement for criterion outcome. A value can `meet + warning` when it approaches a hard limit. A violated criterion remains `violates` regardless of low severity or alert treatment.

A tolerance must explicitly say whether it changes the criterion, creates a secondary band or affects only response/escalation. Hidden engine defaults do not create tolerated behavior.

## Relative/reference-based rules

An Expectation may explicitly adopt a relative rule such as `within 10% of Baseline B`. Doing so does not make Baseline normative generally. The criterion binds the reference identity/version and comparison formula.

If the required reference becomes non-comparable, ambiguous, insufficient or unavailable, that relative normative evaluation can become indeterminate. Another convenient Baseline is not silently substituted.

## Evidence suitability and uncertainty

`Meets` and `violates` are evidence-backed conclusions. Authoritative criteria do not overcome sparse, approximate, unavailable or misaligned evidence.

Approximate evidence can support a decisive result when its known limitations cannot plausibly cross the normative boundary. If material uncertainty spans the boundary, preserve indeterminate/insufficient evidence unless the criterion explicitly defines a valid uncertainty treatment.

Missing telemetry is not violation. Sufficient negative/absence coverage can support violation when the criterion requires occurrence.

## Normative result vocabulary

For one bound criterion, Group 04 uses at least:

- **meets**;
- **violates**;
- **indeterminate / insufficient evidence**;
- **conflicting**;
- **unavailable**;
- **not applicable**.

Warning/proximity, Baseline typicality, severity and waiver are separate attributes/basis results. `Degraded` is not introduced as a substitute for criterion outcome; broader dimension/composite semantics remain Group 06.

## Baseline + Expectation coexistence

The same Observation can legitimately be:

- typical + meets;
- atypical + meets;
- typical + violates;
- atypical + violates.

A post-change regime can have insufficient Baseline history while still being immediately evaluable against an independent Expectation. Conversely, without an Expectation there is no normative pass/fail simply because a Baseline exists.

## Multiple rules and conflict

Different dimensions/contexts/consumers can have simultaneous valid rules without conflict. True conflict requires competing applicable criteria for the same bound normative proposition/context/time.

Never resolve normative conflict implicitly by strictest, loosest, newest, business, technical, highest-severity or numerically closest rule. Explicit AND/OR/conditional composition must be part of the rule semantics.

## Waiver/exception behavior

Two patterns remain distinct:

1. **criterion still evaluates, but response/consequence is waived** — preserve e.g. `violates + waived response`;
2. **criterion is explicitly non-applicable for a bounded exception context** — represent `not applicable` according to that rule.

A waiver never mutates Observation/Baseline/structural evidence or creates a fictional `meets`. Alert waiver does not automatically waive gate/control consequences or other response classes.

## Severity and priority

Severity/priority/escalation remain separate from criterion truth. Low-severity violations are still violations; high-severity criteria can currently meet. Criticality may inform priority without changing the threshold or proving Impact.

## Historical evaluation

Every Assessment retains exact rule/version, warning/tolerance structure, waiver state, evidence/reference versions and evaluation times. Later corrections create reassessment while preserving earlier conclusions. Current thresholds/Baselines are not projected backward.

## Scenario review

See [`scenario_review.md`](scenario_review.md). H04-01–H04-40 pass.

## Exit result

- no new concept;
- HLTH-030–HLTH-040 accepted;
- HLTH-001–HLTH-029 remain accepted;
- concept count remains 24;
- SYN-001–SYN-035, REF-001–REF-030 and AUTH-001–AUTH-053 remain unchanged;
- no vendor rule syntax, alert engine, overall-health score, statistical library, storage or compute architecture selected;
- **Group 05 — Transformation Reconciliation & Metric Propagation is next and has not started.**