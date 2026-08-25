# Phase 006 Group 06 — Composite Health, Readiness Suitability & Progressive Result Timing

**Status:** Accepted — HLTH-055–HLTH-066; H06-01–H06-44 pass

## Goal

Define how dimension-specific and transformation-reconciliation Assessments compose into bounded health summaries without hiding disagreement or uncertainty, and define when health evidence is sufficiently fresh, mature, comparable and cycle-aligned for an exact readiness/high-consequence use without turning health into gate state.

## Accepted contracts

- **HLTH-055 — Composite Health Proposition, Profile, Scope & Use Binding**;
- **HLTH-056 — Component Eligibility, Required/Optional Roles & Explicit Composition Logic**;
- **HLTH-057 — Structured Composite Health Vocabulary & Decisive-State Semantics**;
- **HLTH-058 — Unresolved State, Conflict, Waiver & Exception Preservation in Composite Health**;
- **HLTH-059 — Severity, Criticality, Priority & Health-Truth Separation in Composition**;
- **HLTH-060 — Technical, Business, Executive & Consumer Health Projection over One Truth**;
- **HLTH-061 — Health Result Age, Evidence Freshness & Use-Specific Staleness**;
- **HLTH-062 — Progressive Health Result Maturity, Pending Evidence & Analytical Horizons**;
- **HLTH-063 — Exact-Use Readiness Suitability of Health Evidence**;
- **HLTH-064 — High-Consequence Control-Use Suitability & AUTH-023 Composition**;
- **HLTH-065 — Late Evidence, Progressive Summary Revision & Non-Rewriting History**;
- **HLTH-066 — Historical Composite Health, Suitability & Readiness Replay**.

## Core model

Preserve:

**component Assessment ≠ composite health Assessment ≠ result freshness/suitability ≠ readiness result ≠ gate decision ≠ enforcement ≠ actual execution**.

No new Composite Health, Readiness Suitability, Health Score, Result Maturity or Timing concept is required. Assessment can own bounded composite/suitability evaluations while existing concepts retain their domain truth.

## Composite profile and scope

Composite health is never an unqualified intrinsic scalar property. Bind the subject, consumer/use/context, composite profile/version, required/optional/conditional/alternative component set, current-cycle/window and evaluation/knowledge time.

Different legitimate consumer/use profiles can therefore produce different bounded health propositions while sharing the same underlying component facts.

## Explicit composition logic

Component role and logic are part of the profile. Required, optional, conditional, alternative and informational components remain distinct.

No universal majority, weighted average, numeric score, severity-weighted score or convenient `worst child` algorithm is accepted. AND/OR/conditional/alternative behavior exists only when explicit.

For a conjunctive profile:

- all applicable required components `meet` with no unresolved state → **healthy**;
- the healthy condition plus warning/proximity → **healthy with warning**;
- a required `violates` result → **degraded**, while other unresolved qualifiers remain visible;
- no decisive violation but required indeterminate/conflicting/unavailable state → preserve the corresponding unresolved composite state;
- genuine non-applicability follows the accepted profile rule and is not counted as a pass.

These labels are derived shorthand; component detail/provenance remains authoritative.

## Waiver, conflict and unresolved state

`violates + waived response` remains a violation and cannot become healthy. A bounded exception that makes a criterion genuinely non-applicable is different.

Required conflict, indeterminate evidence or unavailability does not disappear during composition. A known violation can coexist with unresolved qualifiers. Restricted component detail may be hidden from an audience, but a hidden required problem cannot be translated into a clean health result.

## Severity and criticality

Severity, criticality, priority and health truth remain separate. A low-severity required violation still degrades the relevant composite. A high-criticality component that meets remains met. Criticality can influence governed profile membership, escalation and presentation without becoming evidence or Impact truth.

## One health truth, multiple projections

Technical/business/executive/audit/consumer views remain authorized projections over the same underlying component/composite state. A business view can hide exact metrics while still preserving degraded/unresolved/warning/waived semantics.

Consumer-specific profiles can legitimately differ because the bounded proposition differs; that is not permission to rewrite the same profile result for different audiences.

## Result age and freshness

Health-result timing preserves Observation event/window time, source availability, framework knowledge time, Assessment evaluation time, evidence age and the intended operational opportunity.

A recent recalculation over old evidence can be stale for current-cycle use. An older result can still be suitable where the exact use permits that age. No universal TTL is accepted.

`stale for use` is a suitability result, not automatically a normative health failure unless a freshness Expectation itself is violated.

## Progressive analytical maturity

Functional horizons are:

1. immediate operational facts;
2. fast core/schema/current-cycle health;
3. enriched DQ/reconciliation/distribution health;
4. diagnostic/Investigation support;
5. retrospective/post-operations review.

These are not fixed time delays or architecture stages. A result matures when its required evidence is sufficient. Elapsed time never upgrades maturity.

Emit the narrowest trustworthy result as soon as its evidence standard is satisfied. Slower pending evidence can keep a broader composite incomplete without invalidating an already supported narrow fact.

## Readiness suitability

A result is suitable for a readiness use only relative to an exact criterion/opportunity/profile. Suitability can depend on evidence sufficiency, availability, conflict state, comparability/reference validity, current-cycle alignment, allowed evidence age and required analytical horizon.

Suitability is outcome-neutral:

- a fresh well-evidenced violation can be suitable evidence for `not ready`;
- a stale `meets` result can be unsuitable and cannot support `ready`.

REF-024 remains intact: a readiness criterion may require only an operational predicate and legitimately resolve while broader DQ is pending, or may explicitly require a health condition.

## High-consequence use

AUTH-023 control-use eligibility and Phase 006 evidence suitability are both required where applicable, but neither substitutes for the other.

**eligible ≠ fresh/mature/comparable/suitable ≠ ready ≠ authorized to operate control ≠ gate decision ≠ enforcement ≠ execution**.

Evidence unsuitable for an active control remains unresolved according to the governing readiness/control rule. Fail-open/fail-closed/hold/release fallback is separately governed; Group 06 does not invent one.

Passive monitoring remains non-blocking for ungated production.

## Progressive revision and history

Late/enriched/corrected evidence may revise a broader composite without rewriting earlier narrow results. Corrected evidence produces reassessment/supersession provenance.

Historical replay binds the then-effective composite profile, components, Baselines/Expectations/reconciliation definitions, warnings/waivers, evidence/current-cycle state, freshness/suitability rule, readiness criterion and knowledge cut. Current rules are never projected backward.

Historical readiness suitability remains separate from historical gate decision/enforcement/execution.

## Scenario review

See [`scenario_review.md`](scenario_review.md). H06-01–H06-44 pass.

## Exit result

- no new concept;
- HLTH-055–HLTH-066 accepted;
- HLTH-001–HLTH-054 remain accepted;
- concept count remains 24;
- SYN-001–SYN-035, REF-001–REF-030 and AUTH-001–AUTH-053 remain unchanged;
- no universal health/confidence score;
- no concrete TTL/latency SLA, streaming/cache strategy, DQX/Metric View placement, scheduler/gate mechanism or control architecture selected;
- **Group 07 — Consolidation / Exit Review is next and has not started.**