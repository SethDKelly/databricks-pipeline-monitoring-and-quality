# Phase 010 Group 02 — Evidence, Provenance, Temporal & Persistence Architecture

**Status:** COMPLETE / ACCEPTED

## Goal

Select the durable representation and persistence architecture for source evidence, proposition/basis identity, provenance, bitemporal coordinates, correction/supersession, common derivation, retention, replay, and durable traceability.

## Accepted entry contract

Group 02 consumes ARCH-001–ARCH-032 and preserves the Group 01 deployment-capability model, hard constraints, SC-01–SC-06 service classes, ADR discipline and GAP-009 ownership.

## Accepted architecture range

**ARCH-033–ARCH-080** is accepted.

**EPT02-01–EPT02-72 pass.**

Decisions **D-1299–D-1336** are accepted.

## Selected persistence architecture

Group 02 selects a **lakehouse-first framework evidence plane**:

1. **Delta Lake tables** are the canonical durable structured persistence substrate for evidence manifests, normalized journals, temporal/provenance links, basis/derivation relationships and retention metadata.
2. A separately governed **cloud-object payload plane** stores only selectively retained large/opaque artifacts when exact payload retention is justified.
3. **Unity Catalog managed tables/volumes are preferred only when the target deployment verifies them and policy permits them.** External Delta/object storage remains a supported realization.
4. Graph/search/vector/serving stores are **derived, rebuildable projections**, not competing truth stores.
5. Delta transaction-log time travel is infrastructure convenience, **not the DMTZ historical replay contract**.

Detailed decision: [`persistence_technology_adr.md`](persistence_technology_adr.md)

Reference architecture: [`persistence_reference_architecture.md`](persistence_reference_architecture.md)

## Governing evidence/persistence chain

**source-owned occurrence → durable evidence identity + source/provenance locator → multi-coordinate time envelope → minimized retained payload/material → normalized typed derivation → proposition/basis/common-derivation links → non-rewriting correction/supersession journal → lifecycle/retention state → derived graph/search/serving projections**.

No link automatically creates the next and no derived projection becomes source truth.

## Temporal architecture

Material state can retain independently, where applicable:

- event/effective time;
- source-recorded time;
- source-available time;
- framework collection time;
- framework persistence time;
- correction/supersession time;
- actual communication time.

Late evidence stays late for earlier knowledge cuts. Current-state convenience views cannot project latest state backward.

See [`temporal_provenance_model.md`](temporal_provenance_model.md).

## Source authority and provenance

The framework evidence plane is authoritative for **what the framework retained/collected and when**. It is not automatically authoritative for the domain proposition represented by that evidence.

Copied evidence retains:

- source identity;
- source-native revision/locator where available;
- authority role/limitations;
- common derivation;
- capture/processing provenance;
- integrity digest where safe;
- time coordinates.

Physical deduplication may share bytes while logical evidence occurrences remain distinct.

## Data minimization

Group 02 accepts explicit capture classes rather than `retain every raw response`:

- metadata/hash-only;
- minimized structured payload;
- complete bounded source event;
- separately governed large/opaque artifact.

The minimum class capable of supporting the promised proposition/replay/basis requirement should be used.

## Retention, relevance and time-to-live

Group 02 explicitly rejects both **retain everything forever** and **delete history merely because it is old**.

It separates:

1. **storage retention** — possession of evidence/payload;
2. **resolution/detail** — full detail, warm detail, aggregate, cold archive or provenance stub;
3. **reporting/retrieval relevance** — whether retained history should normally surface for a bounded question.

Accepted lifecycle states include `RECENT_FULL`, `WARM_REPLAY`, `SUMMARY_ELIGIBLE`, `COLD_PINNED`, `PROVENANCE_STUB` and `EXPIRED`.

### Reference ordinary-deployment profile

These are configurable starting defaults, not semantic requirements:

- roughly **120 days** of routine recent full-detail normalized evidence;
- roughly **400 days** of detailed normalized replay/trend history;
- up to roughly **24 months** of approved aggregate trend history where exact detail is no longer promised;
- large/opaque payloads minimized more aggressively unless pinned;
- incident/claim/control/report/audit evidence retained by dependency/hold rather than ordinary age-only TTL;
- multi-year history beyond the normal trend horizon retained only where explicit product, recurrence, audit, security, legal or analytical value requires it.

See [`retention_relevance_lifecycle.md`](retention_relevance_lifecycle.md).

## Pinning and holds

Ordinary TTL cannot remove evidence required by:

- an active Investigation;
- a Causal Claim review basis;
- an exact retained Explanation/basis promise;
- Gate/Safeguard audit history;
- an incident/evidence preservation workflow;
- legal/regulatory/contract/security hold.

When dependencies close, the material becomes eligible for ordinary policy reevaluation. Pinning does not strengthen truth/evidence status.

## Downsampling and aggregation

Older high-frequency measurements may be safely rolled up when future use is trend-oriented and exact event-level evidence is no longer promised.

Lossy rollup is not allowed to silently replace exact execution/version evidence, Causal Claim basis, control enforcement evidence, actual retained communication or evidence needed for strong-negative coverage.

Physical Delta compaction/optimization is separate and may rewrite files without changing the logical record set.

## Payload expiry and provenance stubs

Payload/detail may expire while a minimal provenance stub remains for its configured horizon. A stub may record evidence/source identity, permitted time coordinates, digest, prior capture class and expiry policy/time.

A surviving stub supports `basis reference retained; exact payload expired`. It does not recreate expired contents.

## Security/residency

The logical evidence plane may be physically sharded by tenant, region, residency or security boundary. Cross-boundary references exist only where authorized and semantically valid.

## Deployment variability

Group 02 preserves Group 01's central rule. Delta Lake is the structured architecture contract; Unity Catalog managed tables, volumes, VARIANT, FILE, predictive optimization or other platform-specific capabilities are used only when the concrete target deployment verifies them.

See [`external_technology_review.md`](external_technology_review.md).

## Gap treatment

Group 02 materially advances:

- GAP-009-25 long-horizon replay — addressed by framework-owned row-level temporal history + policy-bound retention, not vendor time travel;
- GAP-009-26 availability-by-K — represented when obtainable/required through availability/collection coordinates;
- GAP-009-27 retained Explanation — persistence plane supports authentic snapshot storage; final composition in Group 06;
- GAP-009-28 prior inspectBasis projection — durable basis/projection identities supported; authorization finalization in Groups 03/06;
- GAP-009-29 historical authorization — temporal persistence supports it; authority/authorization model owned by Group 03;
- GAP-009-30 basis payload durability — explicit capture, pin, archive, expiry and stub semantics established;
- persistence implications of identity/run/input/measurement/Lineage/Investigation gaps — durable IDs/time/provenance substrate established for later groups.

Group 02 does not claim later groups' domain gaps are resolved merely because storage exists.

## Architecture choices intentionally deferred

Group 02 does not select:

- polling/streaming acquisition;
- event bus/queue;
- final source adapter strategy;
- graph database/product;
- search/vector product;
- low-latency serving database/cache;
- final backup vendor/implementation;
- final lifecycle automation/orchestrator;
- identity/authority/authorization store design;
- LLM/retrieval architecture;
- active control implementation.

## Acceptance result

The group accepts the persistence plane because it preserves accepted evidence/time semantics, gives old history an explicit value/cost lifecycle, does not require indefinite detailed accumulation, remains deployment-aware and leaves derived serving/reasoning technologies replaceable.

See [`group_02_exit_review.md`](group_02_exit_review.md).

## Handoff

**Group 03 — Identity, Scope, Authority, Authorization & Disclosure Architecture is next.**

Group 03 receives stable durable evidence/proposition IDs, bitemporal/multi-time coordinates, non-rewriting journal semantics, basis/common-derivation links, security/residency sharding capability and retention/history semantics. It must not reopen canonical/derived store roles merely to simplify authorization.
