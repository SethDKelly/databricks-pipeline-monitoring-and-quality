# Phase 007 Group 02 — Change Intent, Deployment Realization & Realized Change

**Status:** Planned — not started

## Goal

Refine how intended modifications, deployment activity and realized Change coordinate without collapsing plan, attempt, activation and observed state into one lifecycle.

## Primary questions

- What evidence establishes that a Change Intent was actually deployed and became effective?
- How should partial realization, mismatched realization, unplanned Change, rollback, reversion and supersession be represented?
- How should source-code/config/schema/transformation versions relate to Deployment and realized runtime/data state without assuming repository identity equals deployed identity?
- How should concurrent or overlapping intents be separated when one Deployment realizes several changes or one intent spans several Deployments?
- How should historical active versions and effective intervals be reconstructed?

## Required boundaries

Preserve:

- Change Intent ≠ Deployment ≠ realized Change;
- deployment attempt ≠ activation;
- activation ≠ successful intended outcome;
- planned state ≠ realized state;
- repository commit ≠ deployed runtime version unless evidenced;
- rollback/reversion ≠ historical erasure;
- realized Change ≠ causal attribution;
- authority over intended/deployed state does not manufacture evidence of realization.

## Handoff to Group 03

Group 03 should consume explicit proposed-change scope and the then-relevant Lineage topology to reason prospectively about blast radius. It must not treat a proposed or deployed-but-not-realized state as actual downstream Impact.

## Deferred

Do not choose Git diffing, CI/CD event ingestion, deployment fingerprinting, CDC, version storage or runtime attestation mechanisms in this group.
