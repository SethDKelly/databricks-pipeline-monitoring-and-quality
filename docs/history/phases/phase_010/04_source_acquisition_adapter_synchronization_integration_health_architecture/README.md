# Phase 010 Group 04 — Source Acquisition, Adapter, Synchronization & Integration-Health Architecture

**Status:** COMPLETE / ACCEPTED

## Result

Group 04 accepts **ARCH-133–ARCH-190** and **AHI04-01–AHI04-96**. Decisions **D-1383–D-1432** are accepted.

The architecture implements a reconciliation-first hybrid acquisition plane over the accepted Group 01–03 capability, persistence, identity, scope and authorization foundations.

The central chain is:

**deployment-verified capability instance + Monitoring Scope → revisioned acquisition plan → source-specific adapter/surface → snapshot/incremental/stream/webhook/export/on-demand/backfill collection → durable request/page/checkpoint provenance → raw/minimized capture → versioned normalization → collection coverage + source lag + integration-health dimensions → canonical evidence publication → later domain reasoning**.

No stage turns integration success/failure into monitored-domain truth.

## Accepted contracts

- ARCH-133–ARCH-152: adapter boundary, capability/surface/plan identity, hybrid modes, acquisition-run/checkpoint/window/pagination architecture.
- ARCH-153–ARCH-172: Monitoring-Scope coverage, request/response provenance, raw/normalized evidence, idempotency/common derivation, schema/parser evolution and deterministic/transient failure classification.
- ARCH-173–ARCH-190: quota/backoff/selectivity, source/acquisition latency, service classes, multidimensional integration health, coverage manifests, degraded/optional/expired sources, acquisition cost and Group 05 handoff.

## Reference acquisition posture

### Reconciliation is the durability/completeness foundation

Incremental or push channels are not rejected; they are intentionally treated as accelerators.

A source can therefore expose:

1. a **reconciliation path** for bounded snapshots/enumeration and missed-event repair;
2. an **incremental path** for cursors/windows/change records;
3. a **push/stream path** for lower latency where supported;
4. an **export/archive path** where vendor retention/export is the practical source;
5. an **on-demand/backfill path** for bounded historical or investigative retrieval.

Not every source requires every path.

### Why not universal streaming

The evaluated sources differ materially:

- Databricks system tables are delayed/non-real-time even when streamed and impose runtime/change-retention constraints;
- GitHub webhooks can fail and are not automatically redelivered;
- Collibra and Immuta expose environment/licensing/export-specific operational behavior;
- strong negatives require known coverage rather than mere event arrival.

Therefore no universal event stream is accepted as the completeness source of truth.

## Canonical adapter output

Every material acquisition attempt can persist:

- acquisition run ID;
- capability-instance ID;
- source-surface ID and version;
- acquisition-plan revision;
- integration principal identity;
- mode and requested population/window;
- request/page/partition identities;
- safe filter/query shape and source request IDs;
- cursor/checkpoint before and after;
- source/event/availability/collection/persistence times where available;
- source payload/reference and integrity information according to capture class;
- parser/normalizer revision;
- normalized evidence IDs;
- page/partition/result counts where safe;
- expected/observed/unresolved coverage;
- integration-health dimensional states;
- quota/rate state and retry decisions;
- cost-relevant counters;
- completion state: complete, partial, failed, skipped-by-policy or unknown where applicable.

## Checkpoint and publication rule

The architecture uses durable checkpoints in the Group 02 structured plane.

A checkpoint advances only after corresponding evidence/provenance has durably committed. Crash recovery intentionally prefers overlap/replay plus idempotent deduplication over skipping an uncertain interval.

Evidence is eligible for downstream reasoning only after required acquisition provenance is durable.

## Coverage rule

Source result emptiness and population coverage are separate.

A strong negative requires:

**bounded proposition population/path/window + Monitoring Scope/materialization + sufficient source surfaces + completed pagination/partitions + acceptable integration health + source-publication timing compatibility + earlier REF/HLTH/OPS negative-evidence burden**.

If any required dimension is partial/unknown, the answer narrows or remains unresolved rather than becoming a false negative.

## Integration-health model

Integration health is dimensional, not one score.

Required dimensions include where applicable:

- installation/configuration/presence;
- authentication;
- source authorization/permissions;
- network/reachability;
- quota/rate capacity;
- source publication/lag;
- checkpoint/progress/backlog;
- pagination/partition completion;
- source schema/API compatibility;
- parser/normalizer state;
- canonical persistence/publication;
- Monitoring-Scope collection coverage;
- service-class freshness;
- retention/replay reachability;
- acquisition cost/volume observability.

A convenience summary can exist later, but it cannot erase the dimensions or become evidence of domain health.

## Failure taxonomy

Group 04 explicitly separates:

- unauthenticated/credential failure;
- permission/scope denial;
- observer-relative 404/not-found;
- rate/throttle exhaustion;
- retryable gateway/source unavailability;
- network/TLS/DNS/proxy/timeout failure;
- source publication delay;
- partial pagination/partition/window;
- cursor/checkpoint invalidation;
- additive or breaking schema drift;
- malformed payload/parser failure;
- persistence/publication failure;
- native retention expiry;
- optional integration absent/unlicensed/unconfigured.

None of these is equivalent to `no event`, `no object`, `healthy`, `no exposure`, `no impact`, or `no control action`.

## Source strategy

See [`source_specific_acquisition_strategy.md`](source_specific_acquisition_strategy.md).

The reference MVP posture is:

- Databricks: system tables/Delta-readable history where suitable for bulk/reconciliation, targeted REST/source APIs for bounded near-current or source-specific facts, deployment-verified streaming only as an accelerator;
- GitHub: GitHub App installation identity, webhooks for freshness where useful, REST reconciliation/conditional retrieval for completeness and repair;
- Collibra: optional pull/reconciliation integration using exact tenant permissions/throttle/license facts;
- Immuta: optional API/audit integration, including configured query-audit sync/export paths where present;
- future vendors: must implement the same adapter/coverage/health contract rather than receive special semantic shortcuts.

## Quota and cost

Quota state is collected as operational telemetry.

The architecture permits adaptive cadence, conditional requests, selective source queries, source-side filters, partitioning, request serialization where required, and prioritization by service class.

It rejects solving quota/cost by:

- dropping required pages silently;
- treating throttled intervals as no-event windows;
- reducing Monitoring Scope without a governed scope revision;
- shortening promised evidence history without lifecycle-policy revision;
- changing source authority;
- manufacturing a lower evidence burden.

## Deployment variability

All source strategies remain conditional on Group 01 capability discovery.

A runtime/version/cloud/region/plan-dependent streaming surface, webhook permission, API field, audit export, system table, OAuth mode, or throttle limit is not assumed simply because public documentation describes it.

## Gap treatment

Group 04 materially resolves the architecture side of:

- GAP-009-32 — source/service-class latency architecture;
- GAP-009-33 — integration-health telemetry;
- GAP-009-34 — Databricks quota-aware acquisition;
- GAP-009-35 — GitHub quota-aware acquisition;
- GAP-009-36 — Collibra operational discovery boundary;
- GAP-009-37 — Immuta operational discovery boundary;
- GAP-009-39 — optional-source graceful degradation;
- GAP-009-40 — deployment-specific capability inventory integration into collection plans.

It also advances GAP-009-25/26/30 through product-side acquisition timing/provenance and source-retention awareness, while Group 02/06 continue to own durable replay/Explanation semantics.

GAP-009-38 cost attribution is partially advanced through acquisition cost telemetry; Group 08 still owns whole-system cost architecture.

## Technology choices intentionally not made

Group 04 does **not** select a universal event bus/queue, final orchestration engine, secret store, long-running service topology, observability vendor, API gateway, or deployment topology.

It defines the adapter/acquisition protocol those later choices must satisfy.

## Group 05 handoff

Group 05 may now design Runtime Provenance, Health, Lineage & Impact Evidence Architecture over **ARCH-001–ARCH-190**.

It may rely on acquisition-run identity, durable evidence IDs, exact source/capability identity, checkpoint/window/page provenance, source lag, coverage manifests and integration-health dimensions. It may not interpret connector silence or collection degradation as execution/output/health/lineage/exposure/Impact absence.
