# OPS-013 — Change Intent ↔ Deployment Association, Evidence & Cardinality

**Status:** Accepted — Phase 007 Group 02

## Purpose

Refine SYN-005 so an intent/deployment association is exact enough to survive bundled releases, phased rollout, retries, overlapping intents and historical replay.

## Contract

A material association binds, where applicable:

- exact Change Intent identity/revision/component under OPS-010;
- Deployment identity and whether the association concerns an attempt, an activated facet, or both;
- target/environment/context;
- implementation-state references/facets under OPS-011;
- linkage evidence/provenance;
- association knowledge time;
- ambiguity/conflict/authorization limitations.

## Acceptable linkage evidence classes

Functional evidence may include explicit change/release references, source revision/build/configuration provenance, target-specific deployment metadata, governed change records, or another provenance-bearing linkage. Phase 009 decides which concrete sources support which class.

The following are insufficient by themselves:

- temporal proximity;
- similar names/descriptions;
- same repository;
- same actor/team;
- one deployment happening after one intent;
- a workflow successfully completing.

## Cardinality

Many-to-many association is first-class:

- one Deployment can carry several independent intent components;
- one intent can require several deployments/targets/phases;
- a retry/redeployment can relate to the same intent without becoming a new intent;
- overlapping releases can leave association ambiguous for selected facets.

No cardinality implies conformance or causal attribution.

## Negative association claims

`No associated Deployment exists` is stronger than `no association is currently known`. A negative claim requires adequate coverage of the bounded deployment/change-management universe and time interval.

## Invariants

- association ≠ activation;
- association ≠ realized intended state;
- association ≠ intended effect realized;
- association ≠ authorization/approval;
- multiple associated intents do not merge into one intent;
- one deployment carrying several intents does not make their anticipated effects interchangeable;
- ambiguous linkage remains ambiguous rather than selecting the closest timestamp.

## Handoff

OPS-015 compares intent against evidenced activation/Change after association has been resolved as far as the evidence permits.