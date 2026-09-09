# AUTH-029 — Normative Governance Action Capabilities

**Status:** Accepted — Phase 005 Group 04

## Purpose

Separate permission to interact with normative health state from Assertion Authority over the resulting rule.

## Capability actions

Where governance distinguishes them, independently authorize:

- view metric profile / Expectation / threshold / severity / schema compatibility rule;
- propose a new rule/profile entry;
- edit a draft or non-authoritative assertion;
- establish/approve an authoritative rule;
- revise/supersede an authoritative rule;
- grant a bounded exception/waiver/suspension;
- retire a rule/profile item;
- approve high-consequence-use eligibility.

## Two-key semantic boundary

A governance action can require both:

1. **Capability Authorization** — may this principal perform the action?; and
2. **Assertion Authority** — does this principal/source/process have authoritative standing for the resulting assertion/action class?

Permission without authority can produce a proposal/advisory assertion but not silently authoritative state. Authority standing without the required action capability does not grant the principal permission to perform the action.

## Invariants

- `Can edit` ≠ `can approve` ≠ `can waive` ≠ `can retire`.
- Permission to view a threshold does not imply permission to change it.
- Metric/profile ownership or technical responsibility does not grant these capabilities automatically.
- High-consequence-use eligibility authority from Group 03 does not grant production-control capability.
- Historical authorizations/actions remain reconstructable after later revocation.
