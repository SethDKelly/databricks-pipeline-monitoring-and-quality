# OPS-116 — Escalation, Human Intervention & Decision Independence

**Status:** Accepted — Phase 007 Group 08

## Purpose

Keep escalation/notification workflow from becoming hidden admission logic.

## Rules

- escalation records that intervention/review is requested under a declared condition;
- escalation alone does not HOLD, ADMIT, override or cancel an opportunity unless explicit policy produces a separate Gate decision/action;
- an escalated opportunity may remain held, remain admission-unknown, expire, or later receive a normal/override/fallback decision;
- human response after escalation is independently authorized under AUTH-036;
- analyst/on-call acknowledgement does not prove external control enforcement;
- escalation urgency/priority is not readiness truth or Gate effectiveness;
- no ticketing/on-call/workflow implementation is selected here.

Any subsequent human override or configuration change retains its own identity, authority and provenance.