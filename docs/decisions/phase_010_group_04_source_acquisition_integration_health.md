# Phase 010 Group 04 — Source Acquisition, Adapter, Synchronization & Integration-Health Decisions

### D-1383 — Source adapters own acquisition mechanics, not product truth
**Status:** Accepted

Adapters preserve prior identity/scope/authority/authorization semantics.

### D-1384 — Every collection plan binds a verified capability instance
**Status:** Accepted

Public vendor documentation alone cannot activate a tenant source.

### D-1385 — Source surfaces are revisioned architecture records
**Status:** Accepted

Endpoint/table/webhook/export identity is distinct from proposition meaning.

### D-1386 — Acquisition plans are versioned and effective-dated
**Status:** Accepted

Cadence/mode/query/scope changes do not rewrite old collection history.

### D-1387 — Acquisition supports multiple explicit modes
**Status:** Accepted

Snapshot, pull, stream, webhook, export, on-demand and backfill remain distinct.

### D-1388 — Reconciliation-first hybrid is the reference posture
**Status:** Accepted

Incremental/push paths accelerate freshness; reconciliation supports coverage/recovery.

### D-1389 — Snapshot reconciliation binds exact population/window
**Status:** Accepted

Discoverability does not define Monitoring Scope.

### D-1390 — Incremental continuation state is source-provenance-bearing
**Status:** Accepted

Cursor progress does not itself prove completeness.

### D-1391 — Streaming is an accelerator with backlog/retention health
**Status:** Accepted

A stalled/lapped stream becomes degraded, not negative evidence.

### D-1392 — Webhooks require idempotency and reconciliation
**Status:** Accepted

Webhook silence/failure cannot prove no event.

### D-1393 — Vendor exports/files are first-class timed acquisition surfaces
**Status:** Accepted

Export arrival is evidence availability time.

### D-1394 — Demand retrieval/backfill cannot backfill historical knowledge
**Status:** Accepted

Later discovery changes retrospective evidence, not earlier K.

### D-1395 — Acquisition run/attempt identity is durable
**Status:** Accepted

Retries/resumptions remain traceable.

### D-1396 — Checkpoints persist in canonical structured storage
**Status:** Accepted

Checkpoint state is integration state, not source truth.

### D-1397 — Overlap is preferred to silent gap where source ordering is imperfect
**Status:** Accepted

Overlap duplicates are deduplicated without strengthening evidence.

### D-1398 — Pagination completion is explicit
**Status:** Accepted

First-page success or missing ambiguous token cannot prove complete enumeration.

### D-1399 — Monitoring Scope supplies expected population, not connector visibility
**Status:** Accepted

Unresolved/inaccessible entities remain in the denominator where scope says they belong.

### D-1400 — Material requests/responses retain operational provenance
**Status:** Accepted

Sensitive query/detail is minimized/disclosure-governed.

### D-1401 — Source envelope and normalized evidence remain separate
**Status:** Accepted

Normalization never replaces what the source returned.

### D-1402 — Reprocessing is idempotent and common derivation explicit
**Status:** Accepted

API/webhook/export copies of one event are not independent corroboration.

### D-1403 — Additive source schema evolution is tolerated
**Status:** Accepted

Unknown new fields can be preserved without assigned semantics.

### D-1404 — Breaking schema/parser failure is explicit and quarantinable
**Status:** Accepted

No guessed field mapping or silent discard.

### D-1405 — Partial batches may persist usable evidence while remaining partial
**Status:** Accepted

Usable subset does not upgrade coverage.

### D-1406 — Checkpoints advance only after durable evidence/provenance commit
**Status:** Accepted

Crash recovery replays uncertain work safely.

### D-1407 — Retry behavior is error- and idempotency-specific
**Status:** Accepted

No universal retry-everything policy.

### D-1408 — Authentication failure is an integration-health state
**Status:** Accepted

It never means source/domain absence.

### D-1409 — Permission and observer-relative not-found are not absence
**Status:** Accepted

Exact principal/action/surface context is retained.

### D-1410 — Rate limiting uses vendor reset/retry guidance and backoff
**Status:** Accepted

Throttle state cannot become a no-event window.

### D-1411 — Acquisition is quota-aware and source-selective
**Status:** Accepted

Use filtering/partitioning/system-table bulk paths where propositionally valid.

### D-1412 — Source publication lag is first-class
**Status:** Accepted

Recent missing records may be unpublished.

### D-1413 — Observed event/availability/collection/persistence lag remains separate
**Status:** Accepted

Acquisition timing never changes event truth.

### D-1414 — Scheduling binds service classes rather than one global cadence
**Status:** Accepted

SC-01–SC-06 can have different acquisition objectives.

### D-1415 — Integration health is multidimensional
**Status:** Accepted

Authn/authz/reachability/quota/lag/checkpoint/pagination/schema/parser/persistence/coverage/freshness remain separable.

### D-1416 — No universal integration-health scalar is accepted
**Status:** Accepted

Summaries cannot hide proposition-relevant dimensions.

### D-1417 — Collection coverage manifests are canonical architecture records
**Status:** Accepted

Population/window/pages/partitions/failures/unresolved segments remain inspectable.

### D-1418 — Strong negatives require coverage + health + prior evidence burden
**Status:** Accepted

HTTP success or empty result alone is insufficient.

### D-1419 — Native source retention expiry remains explicit
**Status:** Accepted

Product-retained evidence and source replayability are distinct.

### D-1420 — Optional source absence is bounded capability degradation
**Status:** Accepted

No benign defaults are created.

### D-1421 — Acquisition cost/volume is observable
**Status:** Accepted

Cost can optimize plans but cannot silently reduce promises.

### D-1422 — Databricks uses bulk/system-table paths where sufficient and targeted APIs where needed
**Status:** Accepted

Streaming remains deployment-bound accelerator, not universal completeness source.

### D-1423 — GitHub uses webhook freshness plus REST reconciliation
**Status:** Accepted

GitHub App/conditional request patterns are preferred where verified.

### D-1424 — Collibra remains optional and tenant-throttle/license aware
**Status:** Accepted

Public defaults are not tenant facts.

### D-1425 — Immuta remains optional and sync/export configuration aware
**Status:** Accepted

Audit absence is evaluated against exact coverage/schedule/retention.

### D-1426 — Group 04 selects no universal event bus
**Status:** Accepted

No evaluated source justifies making one stream the canonical completeness plane.

### D-1427 — Group 04 selects no final orchestration/service topology
**Status:** Accepted

Any runtime must preserve the acquisition protocol; Group 08 owns packaging/deployment.

### D-1428 — GAP-009-32 through GAP-009-37 receive concrete acquisition architecture
**Status:** Accepted

Latency, integration health, Databricks/GitHub quota and Collibra/Immuta operational discovery are architecturally addressed.

### D-1429 — GAP-009-39 and GAP-009-40 receive concrete capability-aware degradation/discovery treatment
**Status:** Accepted

Optional absence and deployment-specific capability inventories feed acquisition planning directly.

### D-1430 — GAP-009-38 acquisition-cost portion is advanced, not fully closed
**Status:** Accepted

Whole-system cost attribution remains Group 08.

### D-1431 — Group 05 consumes acquisition evidence with coverage/health context
**Status:** Accepted

Runtime/health/lineage/Impact logic cannot infer domain absence from connector silence.

### D-1432 — Group 04 accepts ARCH-133–ARCH-190 and promotes Group 05
**Status:** Accepted — Group 04 closure

AHI04-01–AHI04-96 pass. Group 04 closes with reconciliation-first hybrid acquisition, durable checkpoint/pagination/coverage records, multidimensional integration health and source-specific quota/latency strategies. Group 05 — Runtime Provenance, Health, Lineage & Impact Evidence Architecture is next.
