# AUTH-022 — Normative Conflict, Business/Technical Coexistence, and Rule Composition

**Status:** Accepted — Phase 005 Group 03

## Purpose

Define how multiple authoritative normative health rules coexist or conflict without inventing hidden `strictest wins`, `business wins`, or `technical wins` precedence.

## Contract

Before declaring a conflict, resolve whether the rules actually target the same:

- subject or bounded subject scope;
- metric/schema/health dimension;
- population/grain/consumer/use context;
- effective interval;
- normative action or severity layer.

Rules that apply to different dimensions or contexts may coexist legitimately.

## Invariants

- A technical warning threshold and a business failure threshold can both apply when their semantics/contexts are explicit.
- Different consumer-specific schema compatibility rules are not conflicts merely because one consumer is stricter.
- If two co-authoritative rules target the same bound normative proposition and disagree incompatibly, preserve authoritative normative conflict until an explicit AUTH-001–AUTH-008 resolver applies.
- `Strictest`, `most recent`, `highest severity`, `business`, `technical`, `regulatory`, or `closest owner` do not win implicitly.
- Policy Context may constrain or prompt a normative rule but does not automatically become the threshold authority.
- Criticality can affect priority/review requirements but does not silently tighten a threshold.
- A resolved normative conflict preserves the losing/lower-standing rules and provenance rather than erasing them.
- Composite/overall health aggregation is not a conflict resolver; Phase 006 owns any aggregation semantics.

## Example

A platform team defines `warning if freshness > 30m` while a business delivery rule defines `failure if completion > 90m`. Those are compatible layers. Two co-authoritative business rules stating `failure > 60m` and `failure > 120m` for the same subject/context remain normative conflict unless an explicit resolver exists.