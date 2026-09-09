# Phase 005 Group 03 — Normative Health, Metric & Threshold Governance

**Status:** Accepted — AUTH-016–AUTH-023

## Goal

Define who/what has authoritative standing to establish, revise, waive, retire, or approve high-consequence use of normative health, metric-profile, threshold, and structural/schema rules without taking metric/statistical/schema-health computation away from Phase 006.

## Accepted handoff from Groups 01–02

- Assertion Authority is the authority truth owner and AUTH-001–AUTH-015 are accepted;
- Semantic Definition authority is facet-specific, including governed technical schema meaning, grain, field role, and key/identifier role;
- declared/governed schema meaning ≠ normative schema contract ≠ realized schema state;
- Responsibility Assignment, Classification/criticality, and Policy Context do not grant normative health authority;
- derived/inherited governance state does not automatically propagate authority or normative requirements;
- criticality may influence priority and policy but is not evidence of health failure;
- schema/DDL changes can require scoped metric/Baseline/Expectation review without automatically resetting all health context;
- Phase 004 evidence sufficiency and control-enforcement rules remain authoritative and cannot be waived by governance convenience.

## Accepted contracts

- **AUTH-016 — Expectation-Class and Normative Authority**
- **AUTH-017 — Metric Profile Selection, Purpose, and Critical-Metric Authority**
- **AUTH-018 — Threshold, Margin, Tolerance, and Severity Authority**
- **AUTH-019 — Structural / Schema Compatibility Expectation Authority**
- **AUTH-020 — Metric Applicability, Baseline Use, and Structural-Change Review Authority**
- **AUTH-021 — Exception, Waiver, Suspension, and Retirement Governance**
- **AUTH-022 — Normative Conflict, Business/Technical Coexistence, and Rule Composition**
- **AUTH-023 — High-Consequence Metric / Expectation Use Eligibility**

## Core accepted distinctions

### Normative authority is layered

These questions may resolve to different authoritative holders:

- what a metric/schema field **means**;
- whether a metric/check belongs in the governed profile;
- what value/condition is normatively acceptable;
- what warning/failure margin applies;
- what severity/classification attaches to a violation;
- whether a bounded waiver/exception applies;
- whether the condition is eligible for an Execution Gate/safeguard/other high-consequence use.

No one layer implies the others.

### Metric profiles are governance structures, not truth concepts

A metric profile selects purposeful metrics/checks for an asset/context. It should retain purpose, applicability, use/audience, authority/owner, and lifecycle/retirement context. It does not own the measured values or statistical method and does not justify computing every available statistic.

### Baseline remains descriptive

Baseline-derived ranges remain descriptive until an authoritative Expectation explicitly adopts a normative criterion. Authority can decide that an old Baseline should no longer be used after a structural Change, but cannot make empirically non-comparable evidence comparable.

### Schema expectations are normative

Technical schema meaning and observed schema remain separate from structural compatibility Expectations. Required/optional columns, allowed type/nullability/key/grain evolution, additive-change policy, and consumer-specific compatibility are explicit normative rules under scoped authority.

### Waivers do not rewrite evidence

A bounded exception/waiver/suspension can change normative applicability or required response for a stated context/time. It does not mutate Observations, realized schema, Baseline deviation, or historical evidence and should not create a false `pass`.

### Normative conflicts stay explicit

`Strictest wins`, `business wins`, `technical wins`, `highest severity wins`, and latest-record wins are not implicit conflict resolvers. Distinct dimensions/contexts can coexist; same-target co-authoritative conflicts remain conflict until AUTH-001–AUTH-008 resolves them.

### High-consequence use is separately eligible

An authoritative/business-critical metric or Expectation does not automatically become a gate/safeguard predicate. Explicit high-consequence-use eligibility is required. Eligibility still does not grant control capability, prove evidence availability/sufficiency, or prove enforcement.

## Scenario result

[`scenario_checks.md`](scenario_checks.md) passes the representative cases for technical/business normative authority, Baseline non-promotion, metric bloat, schema compatibility, structural-change review, bounded waivers, normative conflict, criticality, and high-consequence control eligibility.

No new Concept is required. The accepted concept catalog remains **24 concepts**.

## Phase boundaries preserved

Group 03 does **not** define:

- actual metric families/calculations;
- quantile/distribution/statistical methods;
- Baseline derivation/comparability algorithms;
- schema-diff/compatibility algorithms;
- composite/overall health aggregation;
- Metric Views/DQX implementation;
- where GitHub Actions, Unity Catalog, or monitoring checks execute;
- who may configure/activate/override gates or safeguards;
- RBAC/ABAC/IAM implementation.

Phase 006 owns metric/statistical/schema-health semantics; Phase 007 owns Lineage-aware propagation/change behavior; Phase 009 owns concrete evidence/source capabilities and latency; Phase 010 owns technical placement/architecture.

## Exit

**Group 03 is accepted with AUTH-016–AUTH-023. AUTH-001–AUTH-023 are accepted overall. Group 04 — Capability Authorization & Restricted Analytical Visibility is next and has not started.**