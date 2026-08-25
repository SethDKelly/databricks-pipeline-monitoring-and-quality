# EXPL-071 — Gate Override, Fallback, Escalation & Degraded-Control Question

**Status:** Accepted — Phase 008 Group 04

## Requirement

Keep `override`, fallback policy/application, escalation, timeout/expiry/cancellation and degraded control independently answerable.

Override preserves the underlying readiness result. Fallback configured ≠ trigger ≠ applied action ≠ enforcement. Escalation does not itself HOLD/ADMIT. A run during degraded telemetry does not prove fail-open; no run does not prove fail-closed.

Authorization for override/control remains a separate Capability Authorization proposition.