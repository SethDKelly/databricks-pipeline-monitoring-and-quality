# Phase 006 Group 02 — Structural / Schema / DDL Compatibility

**Status:** Accepted — HLTH-009–HLTH-018; H02-01–H02-30 pass

## Goal

Define functional structural/schema health and consumer-specific compatibility without selecting whether validation runs in GitHub Actions, Unity Catalog/Databricks, DQX, Metric Views, or the monitoring application.

## Accepted handoff from Group 01

- structural/schema is one canonical metric/check family, but observed structure is not automatically compatibility Assessment;
- every structural Observation remains bound to subject/schema/interface version/window/context;
- `column exists`, observed type/nullability/nesting and similar facts are Observation;
- normative compatibility depends on applicable structural Expectations governed by AUTH-019;
- profile selection/applicability/support/availability remain separate;
- structural change triggers later metric/Baseline applicability review without globally invalidating every metric.

## Accepted contracts

- **HLTH-009 — Structural Observation, Schema Snapshot & Contract-Surface Binding**;
- **HLTH-010 — Structural Change Taxonomy, Field Identity, Add/Drop/Rename & Reordering**;
- **HLTH-011 — Required/Optional Fields, Additive/Removal Compatibility & Consumer Sensitivity**;
- **HLTH-012 — Type, Precision, Scale, Casting & Nested-Shape Compatibility**;
- **HLTH-013 — Nullability, Defaults, Generated Values & Population-Presence Compatibility**;
- **HLTH-014 — Key, Identifier, Grain & Cardinality-Shape Compatibility**;
- **HLTH-015 — Consumer-Specific Contract, Interface Version & Compatibility Scope**;
- **HLTH-016 — Planned, Declared, Proposed & Realized Structural State**;
- **HLTH-017 — Structural Change Impact on Metric/Profile/Baseline Applicability**;
- **HLTH-018 — Structural Compatibility Proposition, Evidence & Result Semantics**.

## Core structural model

Preserve:

**declared/governed schema meaning ≠ normative structural Expectation/contract ≠ proposed/planned structural state ≠ realized structural Observation/Change ≠ compatibility Assessment**.

No new Schema or Schema Contract concept is required. Semantic Definition/Entity Identity own meaning/identity assertions; Expectation owns normative requirements; Change Intent owns proposed structural evolution; Observation/Change own realized structure/change; Assessment owns compatibility conclusions.

## Compatibility is interface- and consumer-specific

A producer table does not have one universal `breaking/non-breaking` label. The proposition is closer to:

> Is producer/interface state S structurally compatible with Consumer C under contract version K at time T?

The relevant surface may be a physical table, a stable view/projection, export interface, stream/message shape, Metric View, application interface, or downstream transformation contract.

Therefore:

- additive field can be safe for a name-based consumer and breaking for positional/strict consumers;
- field reorder can be irrelevant for one consumer and material for another;
- stable views can insulate consumers from backing-table DDL changes;
- producer schema can remain unchanged while compatibility changes because the consumer contract/version changes;
- compatibility is not automatically transitive through intermediate interfaces.

## Structural-change taxonomy and identity

Group 02 distinguishes add, remove, rename, reorder, nested-path movement, type/precision/scale, nullability, default/generated-value, key/grain and nested-shape changes rather than one generic `schema changed` fact.

A rename requires identity evidence. `old_name` disappearing while `new_name` appears is not enough. Conversely, keeping the same field name does not preserve semantic identity when field meaning, population, grain or calculation changes.

## Type and value-presence compatibility

Platform ability to cast or parse values is not structural compatibility by itself. Widening/narrowing, precision/scale, timezone/encoding, nested shape, nullability, defaults and generated values are interpreted against the bound contract.

A field becoming nullable can break a guarantee even when current data contains no nulls. A default such as `UNKNOWN` can preserve physical presence while violating business completeness/validity semantics.

## Key and grain changes

Key/grain change is structurally material even when column names/types stay identical. It can invalidate old row-count, uniqueness, distribution and join/reconciliation assumptions without automatically indicating a defect.

Changing from one row per account to one row per account/day therefore triggers scoped review of measurements tied to the former grain while execution/freshness dimensions may remain unaffected.

## Proposed versus realized validation

Group 02 supports multiple validation horizons without selecting architecture:

1. current realized structural state;
2. declared/governed state;
3. proposed/planned state;
4. prospective compatibility against known consumers;
5. realized compatibility after activation;
6. retrospective structural interpretation.

A pre-deployment validation success does not prove deployment occurred or production matches the candidate. If realized state differs, the prior result remains historical evidence about the proposal and a new realized Assessment is required.

## Structural compatibility result semantics

For a bounded consumer/contract proposition:

- **compatible** requires sufficient applicable evidence that every required predicate in scope is satisfied;
- **incompatible** requires sufficient evidence of at least one required predicate violation;
- **unknown/unresolved**, **conflicting**, **unavailable**, and **not applicable** remain distinct.

`No detected diff` is not automatically compatible if the observation mechanism lacked sufficient coverage.

Structural incompatibility remains one health dimension. It does not prove job failure, exposure, downstream Impact, business consequence, or causality.

## Metric/Baseline consequences

Structural change triggers **scoped** review of affected measurement semantics. Depending on the change, review can affect:

- field/path measurement binding;
- metric definitions/profile selection;
- row-count/population interpretation;
- completeness/null rates;
- uniqueness/key metrics;
- distributions/quantiles;
- join/reconciliation relationships;
- business metrics;
- Baseline eligibility/comparability.

Unrelated dimensions can remain valid. Group 03 owns actual historical Baseline/statistical comparability; AUTH-020 governs who may approve intended review/use decisions.

## Physical DDL boundary

Not every physical DDL/property change is logical schema incompatibility. Clustering, optimization, storage layout, or another physical property belongs in structural compatibility only when the relevant consumer/interface contract actually depends on it. Performance effects may still be operational health evidence elsewhere.

## Scenario review

See [`scenario_review.md`](scenario_review.md). H02-01–H02-30 pass.

## Exit result

- no new concept;
- HLTH-009–HLTH-018 accepted;
- Group 01 HLTH-001–HLTH-008 remains accepted;
- concept count remains 24;
- SYN-001–SYN-035, REF-001–REF-030 and AUTH-001–AUTH-053 remain unchanged;
- no validation architecture selected;
- **Group 03 — Baselines, Comparability, Distribution & Statistical Context is next and has not started.**