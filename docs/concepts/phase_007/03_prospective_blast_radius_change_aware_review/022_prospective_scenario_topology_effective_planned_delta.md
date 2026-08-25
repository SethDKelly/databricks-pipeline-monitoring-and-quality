# OPS-022 — Prospective Scenario Topology: Effective State + Planned Delta

**Status:** Accepted — Phase 007 Group 03

## Purpose

Support pre-realization topology reasoning without converting planned relationships into effective Lineage.

## Contract

A prospective scenario topology is a derived analytical overlay over:

1. the OPS-001–OPS-009 effective Lineage topology applicable at the review cut; and
2. explicit topology deltas declared by the exact Change Intent component.

Planned deltas may describe:

- relationship addition;
- relationship removal;
- relationship family/role/scope modification;
- producer/publication/consumption-path change;
- field/key/population/consumer/version narrowing or broadening.

The overlay preserves the origin of every relationship as **effective** or **planned-only**.

## Removal semantics

A proposed relationship removal does not erase the effective relationship during pre-deployment review. The current relationship remains historical/effective truth, while the scenario records that the proposal would end/change it if realized.

Consumers dependent on the relationship remain prospective review candidates because loss or modification of a dependency can itself be material.

## Invariants

- scenario topology ≠ Lineage truth;
- planned edge ≠ effective edge;
- planned removal ≠ edge already absent;
- proposed topology cannot rewrite historical topology;
- scenario composition does not establish deployment, Change, exposure or causality;
- topology deltas remain bound to the exact intent revision/component.

## Handoff

OPS-023 uses the scenario topology to identify downstream/path-loss candidates.