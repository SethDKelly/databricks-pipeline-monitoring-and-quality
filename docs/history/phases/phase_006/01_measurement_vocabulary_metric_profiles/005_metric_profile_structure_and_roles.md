# HLTH-005 — Metric Profile Structure & Profile Roles

**Status:** Accepted — Phase 006 Group 01

## Purpose

Give governed metric profiles a functional shape that supports purposeful routine monitoring without turning profiles into a new truth concept or architecture tier.

## Contract

A metric profile is the provenance-bearing governed selection/applicability structure accepted by AUTH-017. For each selected metric/check it should be able to reference:

- subject/scope;
- metric/check definition and version or compatible definition family;
- purpose / monitored failure mode / business use;
- semantic applicability context;
- profile role(s);
- lifecycle state/effective interval;
- intended evaluation cadence/horizon where functionally relevant without selecting scheduler architecture;
- authority/provenance for inclusion/revision/retirement;
- optional cost/latency sensitivity or diagnostic-only intent as functional metadata.

## Accepted profile roles

### Core operational/table health
A deliberately small routine set with broad value for detecting whether expected execution/output/freshness/basic table state is materially available.

### Critical-field/business health
Metrics/checks selected because a specific field, population or business-defined measure is materially important.

### Transformation-specific reconciliation
Metrics/checks selected because the transformation itself creates a meaningful relationship or invariant, such as join match, fan-out or source-to-target reconciliation.

### Diagnostic/on-demand
Metrics/checks useful for deeper analysis or Investigation but unnecessary for routine computation on every execution.

A metric may have multiple roles when the purposes genuinely overlap; avoid duplicating the Observation simply to assign several labels.

## Non-roles

- `high-consequence/control eligible` — separately governed by AUTH-023;
- `business audience` / `technical audience` — disclosure context, not profile role;
- `criticality` — Classification/governance input, not the metric role itself;
- `expensive` — cost characteristic, not semantic purpose;
- `anomalous` — Assessment/result, not profile role.

## Invariants

- Profile selection does not make a metric semantically applicable if its prerequisites do not hold.
- Profile selection does not guarantee the metric can be computed or is currently available.
- A metric can be semantically applicable but intentionally not profile-selected.
- A diagnostic metric can be evaluated for an Investigation without automatically becoming routine profile state.
- Removing/retiring a metric from a current profile does not erase historical Observations/Assessments.
- Profile changes are governed state and must not silently rewrite historical profile membership.
