# Group 04 — Integration-Health Model

Integration health answers whether the framework can currently and historically obtain/interpret a required source surface with sufficient operational coverage. It does not answer whether the monitored system is healthy.

## Dimensions

| Dimension | Example states |
|---|---|
| presence/configuration | verified-present, absent-optional, absent-required, unverified |
| authentication | healthy, expired, rejected, unavailable, unknown |
| authorization | sufficient, partial, denied, conflicting, unknown |
| reachability | reachable, timeout, DNS/TLS/network-blocked, source-unavailable, unknown |
| quota | available, constrained, throttled, exhausted, unknown |
| publication | within expected envelope, delayed, lag-unknown |
| checkpoint/progress | current, catching-up, stalled, invalid, gap |
| pagination/partition | complete, partial, failed, unknown, not-applicable |
| schema/API | compatible, additive-drift, breaking-drift, version-unsupported |
| parser/normalizer | healthy, partial/quarantined, failed, unknown |
| persistence/publication | committed, delayed, failed |
| coverage | complete-for-objective, partial, unknown, not-applicable |
| service-class freshness | within-objective, outside-objective, unknown |
| retention reachability | source-available, product-only, expired/unavailable, unknown |

No scalar score is accepted.

## Health events

Each material health transition is versioned/time-aware and linked to capability instance, source surface and acquisition plan.

## Degradation propagation

Integration-health degradation propagates only as an evidence/answerability limitation to propositions that require the affected surface/population/window.

One degraded optional source need not suppress unrelated questions whose required evidence remains sufficient.

## Negative-evidence gate

Before a source contributes to a strong negative, the reasoning layer must be able to inspect the relevant coverage/health manifest. A successful HTTP status alone is insufficient.

## Recovery

A later successful collection does not rewrite an earlier gap. Recovery closes the integration-health interval prospectively; historical questions still see what was unavailable or partial at the earlier knowledge cut.
