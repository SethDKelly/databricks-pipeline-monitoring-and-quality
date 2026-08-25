# EXPL-094 — Execution and Control Negative Language

**Status:** Accepted — Phase 008 Group 05

## Requirement

Missing execution/control telemetry must remain a limitation rather than become `did not run`, `Gate failed open`, `Gate failed closed`, `Safeguard failed`, `not enforced`, or `no fallback`.

Preserve decision/enforcement/execution independence. A run during degraded control proves the run; no run proves non-execution where evidenced; neither alone establishes the degraded-control mechanism.

Strong no-run/no-output/no-enforcement claims require bounded coverage.