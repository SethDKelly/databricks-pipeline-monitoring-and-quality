# OPS-114 — Timeout, Wait Deadline, Opportunity Expiry & Cancellation

**Status:** Accepted — Phase 007 Group 08

## Purpose

Separate time-triggered control conditions from the actions that may follow them.

## Distinctions

Keep separate:

- readiness/evaluation age;
- Gate wait timeout or decision deadline;
- execution opportunity/schedule-window expiry;
- business/completion SLA deadline;
- explicit opportunity cancellation;
- fallback/escalation action triggered by a timeout.

## Rules

- timeout occurrence is a fact/trigger, not an automatic ADMIT/HOLD/escalation unless the declared policy says and evidence shows so;
- configured timeout duration does not prove timeout was detected/applied;
- opportunity expiry while held means no execution occurred for that opportunity; it is not a failed run;
- cancellation can occur for reasons independent of Gate state;
- a missed business deadline may coexist with a still-valid hold and requires separate Observation/Assessment/Impact evidence;
- no universal maximum wait or timeout value is selected in Phase 007.