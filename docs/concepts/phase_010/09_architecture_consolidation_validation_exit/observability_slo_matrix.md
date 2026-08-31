# Phase 010 Group 09 — Observability / SLO Matrix

**Status:** ACCEPTED — numeric objectives remain deployment ADR values

Phase 010 freezes **what must be measured and bounded**, not universal numeric targets. Numeric SLOs are set only after actual target-environment source publication lag, quotas, workload volume, compute behavior and product commitments are measured.

## Service-class SLO matrix

| Service class | Primary SLI families | SLO boundary | Required limitation/degradation behavior |
|---|---|---|---|
| SC-01 Near-current operational facts | source publication lag; acquisition delay; persistence delay; projection delay; API latency; source/integration availability | Bound each material latency stage rather than one opaque freshness number | Return narrow current facts with explicit pending/unavailable enrichment; do not strengthen negatives under delayed coverage |
| SC-02 Periodic core health & quality | scheduled collection completion; expected-population coverage; check/evaluation completion; measurement→target attribution; evaluation freshness | Bound evaluation completion relative to the profile/window and required evidence | Required missing evidence keeps composite/use conclusion unresolved rather than positive by timeout |
| SC-03 Investigation / RCA enrichment | retrieval latency; graph/query completion; reasoning-run latency; evidence-watermark age; optional model/search latency | Slower asynchronous enrichment allowed; correctness and evidence provenance dominate | Partial leads/statements remain valid; model/search failure degrades convenience only |
| SC-04 Historical / as-known replay | archive lookup; restore queue/wait; restore completion; replay query latency; basis availability; historical policy/source coverage | RPO/RTO/restore target depends on promised history tier | Current state cannot fill missing historical material; unavailable/expired basis is explicit |
| SC-05 Retained communication / basis inspection | snapshot lookup latency; basis resolution; disclosure evaluation; archive restore; payload availability | Usually not operational fast path; exact target follows audit/product promise | Prior exact wording/projection only returned if authentic retained evidence exists |
| SC-06 Active control | opportunity detection; criterion retrieval/evaluation; authorization; decision issuance; delivery; enforcement acknowledgement/observation; decision age vs applicability horizon | Must complete within the controlled opportunity’s explicit latency/applicability budget | Degraded dependency follows profile policy; stale decisions rejected; passive monitoring remains independent |

## Platform observability dimensions

Do not collapse these into one global score:

### Acquisition / integration

- authentication state;
- authorization/permission state;
- reachability;
- source/API status;
- throttle/quota/rate state;
- publication lag;
- checkpoint/cursor progress;
- pagination/partition/window completion;
- schema/API drift;
- parser/normalizer health;
- quarantine volume;
- persistence success;
- expected-population/collection coverage;
- freshness by source/surface/service class.

### Canonical persistence

- write success/latency;
- transaction/commit failures;
- schema/migration version;
- storage/object availability;
- lifecycle/archive/pin execution;
- backup completion and restore test state;
- retention/purge failures.

### Derived projections

- source/canonical watermark;
- projection revision;
- lag/staleness;
- rebuild status;
- query latency/errors;
- index coverage where applicable.

### Serving

- authentication latency/failures;
- authorization/disclosure evaluation latency/results;
- request/error/timeout rate;
- query latency;
- cache hit/miss/stale rejection;
- response projection/render validation failures;
- export/communication delivery state where applicable.

### Reasoning / replay

- plan/run identity and duration;
- canonical/source watermarks used;
- rule revision;
- unresolved dependency counts by reason (without leaking protected metadata to unauthorized audiences);
- historical restore/replay status;
- deterministic render success;
- optional model/search/tool invocation health separately.

### Active control

- opportunity detection;
- evidence suitability/readiness evaluation latency;
- decision issuance;
- delivery/acceptance;
- enforcement attempt/result;
- actual execution reconciliation;
- decision applicability age;
- override/fallback use;
- Safeguard path/cohort enforcement;
- prevention-manifest sufficiency;
- release/expiry/recovery transitions.

### Cost / quota

- source requests/pages/bytes;
- compute/query duration/units where observable;
- storage by tier/pin/retention class;
- model/search usage where enabled;
- control invocations;
- quota headroom/exhaustion;
- cost attribution by tenant/source/service class/component where measurable.

## SLO governance

Every numeric SLO ADR must state:

1. service class and exact workload/proposition family;
2. target environment/capability instance;
3. SLI definition and measurement point;
4. percentile/window/error-budget semantics where applicable;
5. dependencies and source publication assumptions;
6. degraded behavior after breach;
7. whether the SLO is product-facing, internal operational or control-safety critical;
8. review/revision trigger.

## Critical non-equivalences

- SLO breach ≠ monitored pipeline/data health failure.
- Source publication lag ≠ DMTZ acquisition lag.
- API latency ≠ evidence freshness.
- model latency ≠ reasoning correctness.
- Gate service availability ≠ effective enforcement.
- backup success ≠ complete historical replay coverage.
- platform green ≠ sufficient negative-evidence coverage.
