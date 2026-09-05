# Source Acquisition, Adapter, Synchronization & Integration-Health Architecture

**Canonical key:** `architecture.source_acquisition_adapter_integration_health`

**Kind:** TECHNICAL ARCHITECTURE CONTRACT

**Authority:** CANDIDATE / NOT CURRENT AUTHORITY

**Migration records:** `stable_family.ARCH`, `architecture.source_acquisition_adapter_integration_health`

**Stable IDs:** ARCH-133–ARCH-190

**Stable ID index:** `ARCH-133`, `ARCH-134`, `ARCH-135`, `ARCH-136`, `ARCH-137`, `ARCH-138`, `ARCH-139`, `ARCH-140`, `ARCH-141`, `ARCH-142`, `ARCH-143`, `ARCH-144`, `ARCH-145`, `ARCH-146`, `ARCH-147`, `ARCH-148`, `ARCH-149`, `ARCH-150`, `ARCH-151`, `ARCH-152`, `ARCH-153`, `ARCH-154`, `ARCH-155`, `ARCH-156`, `ARCH-157`, `ARCH-158`, `ARCH-159`, `ARCH-160`, `ARCH-161`, `ARCH-162`, `ARCH-163`, `ARCH-164`, `ARCH-165`, `ARCH-166`, `ARCH-167`, `ARCH-168`, `ARCH-169`, `ARCH-170`, `ARCH-171`, `ARCH-172`, `ARCH-173`, `ARCH-174`, `ARCH-175`, `ARCH-176`, `ARCH-177`, `ARCH-178`, `ARCH-179`, `ARCH-180`, `ARCH-181`, `ARCH-182`, `ARCH-183`, `ARCH-184`, `ARCH-185`, `ARCH-186`, `ARCH-187`, `ARCH-188`, `ARCH-189`, `ARCH-190`

**Owns current question after cutover:** How does DMTZ collect, normalize and publish source evidence with explicit completeness, lag, quota and failure state?

## Canonical contract

The acquisition chain is:

**deployment-verified capability instance + Monitoring Scope → revisioned acquisition plan → exact source adapter/surface → snapshot/incremental/stream/webhook/export/on-demand/backfill collection → durable request/page/window/checkpoint provenance → minimized capture → versioned normalization → coverage + publication lag + integration-health dimensions → canonical evidence publication → downstream reasoning**.

No collection stage changes source truth or creates a monitored-domain fact from integration success/failure.

## Reconciliation-first hybrid acquisition

Reconciliation is the durability/completeness foundation. Incremental and push paths are accelerators where source capability supports them.

A source may provide bounded reconciliation/enumeration, incremental cursor/window collection, push/stream/webhook freshness, export/archive retrieval and on-demand/backfill. Not every source needs every mode, and no universal event stream is accepted as a completeness source of truth.

## Acquisition provenance

Material attempts retain acquisition-run identity, capability-instance and source-surface/version, plan revision, integration principal, requested population/window, request/page/partition identity, safe query/filter shape and source request IDs, checkpoint/cursor before and after, material source/availability/collection/persistence times, payload/reference/integrity according to capture class, parser/normalizer revision, normalized evidence IDs, safe counts, expected/observed/unresolved coverage, integration-health dimensions, quota/rate state, retry decisions, cost counters and explicit complete/partial/failed/skipped/unknown completion state.

A checkpoint advances only after corresponding evidence/provenance has durably committed. Recovery prefers bounded overlap/replay plus idempotent deduplication over skipping an uncertain interval. Evidence is eligible downstream only after required acquisition provenance is durable.

## Coverage and negative reasoning

Source result emptiness and population coverage are separate. A strong negative requires bounded proposition population/path/window, Monitoring Scope/materialization, sufficient source surfaces, completed pages/partitions, acceptable integration health, publication timing compatibility and the applicable REF/HLTH/OPS burden.

Partial or unknown dimensions narrow the answer or keep it unresolved; they do not become absence.

## Integration health

Integration health is multidimensional, including as applicable installation/configuration, authentication, source permission, reachability, quota/rate capacity, source publication lag, checkpoint/backlog, pagination/partition completion, API/schema compatibility, parser/normalizer state, canonical persistence/publication, scope coverage, service-class freshness, retention/replay reachability and cost/volume observability.

No convenience summary can erase those dimensions or become monitored-domain health.

Distinguish authentication failure, permission denial, observer-relative not-found, throttling, retryable source outage, network/TLS/DNS/proxy/timeout, publication delay, partial pagination/window, checkpoint invalidation, schema drift, malformed payload/parser failure, persistence failure, retention expiry and optional integration absence. None means `no event`, `healthy`, `no exposure`, `no impact` or `no control action`.

## Source strategy and cost

Databricks may use system tables/Delta-readable history for bulk/reconciliation and targeted APIs for bounded near-current facts; streaming remains capability-gated. GitHub may use GitHub App identity, webhooks for freshness and REST reconciliation/conditional retrieval for completeness/repair. Collibra and Immuta remain optional deployment-verified integrations.

Quota/cost may drive adaptive cadence, conditional requests, selective querying, filtering, partitioning and service-class prioritization. It may not silently drop required pages, convert throttled intervals into no-event windows, shrink Monitoring Scope without governed revision, shorten promised retention, change authority or lower evidence burden.

## Architecture boundary

This segment does not select a universal queue/event bus, final orchestrator, secrets product, service topology, observability vendor, API gateway or deployment platform.

## Provenance

- `docs/concepts/phase_010/04_source_acquisition_adapter_synchronization_integration_health_architecture/README.md`
- atomic ARCH-133–ARCH-190 files under that Phase 010 group
- Phase 010 decisions D-1383–D-1432 and AHI04-01–AHI04-96 review evidence
