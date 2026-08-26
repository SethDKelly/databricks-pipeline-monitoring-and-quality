# Phase 010 Group 01 — Service / Use Class Matrix

Phase 010 rejects one universal freshness, latency, completeness or retention target. Architecture is evaluated against bounded use classes.

| Class | Primary use | Evidence posture | Latency posture | Retention / time posture | Degraded behavior |
|---|---|---|---|---|---|
| **SC-01 Near-current operational facts** | run/task/update lifecycle, immediate operational facts | source-owned narrow facts may arrive before enriched health evidence | prioritize low-latency sources; exact numeric SLO deferred to environment facts | enough history for recent reconstruction; late events remain late | return narrow facts with explicit pending/unavailable enrichment |
| **SC-02 Periodic core health & quality** | freshness/schema/DQ/reconciliation/profile evaluation | complete required component evidence for the exact profile/use | periodic/asynchronous acceptable where profile permits | retain measurements, definitions, run/output association and evidence time needed for trend/replay | unresolved required evidence prevents positive composite claims |
| **SC-03 Investigation / RCA enrichment** | localization, leads, Causal Claim support, Impact reasoning | heterogeneous evidence with conflict/limitations preserved | slower enrichment acceptable; maturity follows evidence, not elapsed time | enough history for incident window plus comparison/baseline/lineage context | partial leads and unresolved causal status remain valid outputs |
| **SC-04 Historical / as-known replay** | answer what source state/evidence was known by event window and K | time-valid history + availability-by-K where promised | interactive or batch is decision-specific; correctness dominates immediacy | durable source/provenance/history beyond vendor windows where commitment requires | unavailable history is explicit; current state cannot backfill the cut |
| **SC-05 Retained communication / basis inspection** | prove actual prior Explanation and inspect permissible basis | authentic communication snapshot + durable basis identity + current disclosure check | usually not operational fast path; exact target deferred | retention follows audit/product promise, not vendor default alone | surviving reference with expired payload remains inspectability-limited |
| **SC-06 Active control path** | Gate/Safeguard decisions/enforcement | exact criterion/suitability/readiness/control state and enforcement evidence | bounded low-latency requirement defined by controlled opportunity | retain decision/delivery/acceptance/enforcement/execution/opportunity history | failures are observable; unknown telemetry does not imply fail-open/fail-closed |

## Rules

- A source may serve several classes with different sufficiency.
- A class can combine fast and slow sources; the slowest source does not delay unrelated narrow statements.
- Numeric SLOs belong to later ADRs after target-environment publication lag, quotas, cost and control requirements are known.
- Service-class labels do not create truth, authority, maturity or severity.
