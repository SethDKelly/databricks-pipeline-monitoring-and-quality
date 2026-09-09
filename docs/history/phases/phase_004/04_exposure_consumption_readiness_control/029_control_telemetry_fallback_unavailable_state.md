# REF-029 — Control Telemetry, Fallback, and Unavailable-State Evidence

**Status:** Accepted — Phase 004 Group 04

## Purpose

Prevent degraded or missing control telemetry from being translated into invented production behavior, while preserving what is known about configured fallback semantics and actual outcomes.

## Distinct states

Keep separate where material:

- readiness evidence unavailable/unknown;
- gate/safeguard decision unavailable/unknown;
- decision delivery to external control unknown;
- enforcement state unknown;
- control integration itself degraded/unavailable;
- configured fallback policy known;
- actual fallback application known/unknown;
- downstream execution/publication/consumption outcome known/unknown.

## Rules

- Missing gate/safeguard telemetry does not prove the control failed, succeeded, failed open, or failed closed.
- A known fallback rule describes what should happen under its defined unavailable state; it does not by itself prove that the runtime recognized the condition or applied the rule.
- Actual fallback behavior requires evidence at the decision/enforcement/outcome level appropriate to the control.
- If an explicitly gated production path depends on the control integration, its unavailable-state behavior may have operational consequences; those consequences remain separately observed/assessed.
- Passive monitoring degradation must not be reinterpreted as production-control degradation for ungated jobs.
- Restricted control evidence may yield an authorized abstract state such as `control enforcement unknown` without exposing sensitive dependency/control details.
- Control evidence should preserve knowledge time so post-ops review can distinguish what operators knew during degradation from what later telemetry established.

## Non-goals

- selecting fail-open/fail-closed policy;
- defining control SLOs;
- assuming every integration outage affects production;
- choosing monitoring/control architecture.
