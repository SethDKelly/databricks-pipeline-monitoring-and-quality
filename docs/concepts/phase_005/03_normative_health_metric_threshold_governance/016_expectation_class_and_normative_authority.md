# AUTH-016 — Expectation-Class and Normative Authority

**Status:** Accepted — Phase 005 Group 03

## Purpose

Resolve which source, actor, role, or governed process has authoritative standing to establish, revise, except, or retire an **Expectation** for an explicit subject, health/quality dimension, context, and time without turning descriptive behavior, semantic ownership, or responsibility into normative authority.

## Contract

Normative authority is bound to an explicit target that should identify, as applicable:

- subject or bounded subject scope;
- Expectation class/dimension, such as freshness, completeness, uniqueness, volume, structural compatibility, business-semantic validity, or delivery/readiness condition;
- property/metric/schema condition the Expectation governs;
- environment, consumer, business use, population, or other applicability context;
- lifecycle action such as establish, revise, except, or retire when authority differs by action;
- effective interval and knowledge cut where historical resolution matters.

## Invariants

- Semantic Definition authority does not automatically grant Expectation authority.
- Responsibility Assignment does not automatically grant Expectation authority.
- Classification/criticality and Policy Context may inform the need for an Expectation but do not establish one automatically.
- Baseline regularity never self-promotes into an Expectation.
- Change Intent anticipated effects do not become normative requirements without an authoritative Expectation action.
- The source that computes a metric is not automatically authoritative to define what value is acceptable.
- Different Expectation dimensions may legitimately have different authoritative holders.
- An actor may be authoritative to propose/revise one class of Expectation while lacking authority over another class or context.
- Assertion Authority resolves normative standing; Capability Authorization separately determines whether a principal may perform the establish/revise/except/retire action where permission is required.
- Authority over an Expectation does not prove that the criterion is satisfied; Assessment remains evidence-based.

## Example

A pipeline team may be authoritative for a technical freshness requirement while a business-data authority is authoritative for an external-reporting population threshold. Neither authority silently transfers to the other dimension.