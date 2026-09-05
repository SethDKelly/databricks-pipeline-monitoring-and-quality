# Evidence, Provenance, Temporal & Persistence Architecture

**Canonical key:** `architecture.evidence_provenance_temporal_persistence`

**Kind:** TECHNICAL ARCHITECTURE CONTRACT

**Authority:** CANONICAL CURRENT AUTHORITY

**Migration records:** `stable_family.ARCH`, `architecture.evidence_provenance_temporal_persistence`

**Stable IDs:** ARCH-033–ARCH-080

**Stable ID index:** `ARCH-033`, `ARCH-034`, `ARCH-035`, `ARCH-036`, `ARCH-037`, `ARCH-038`, `ARCH-039`, `ARCH-040`, `ARCH-041`, `ARCH-042`, `ARCH-043`, `ARCH-044`, `ARCH-045`, `ARCH-046`, `ARCH-047`, `ARCH-048`, `ARCH-049`, `ARCH-050`, `ARCH-051`, `ARCH-052`, `ARCH-053`, `ARCH-054`, `ARCH-055`, `ARCH-056`, `ARCH-057`, `ARCH-058`, `ARCH-059`, `ARCH-060`, `ARCH-061`, `ARCH-062`, `ARCH-063`, `ARCH-064`, `ARCH-065`, `ARCH-066`, `ARCH-067`, `ARCH-068`, `ARCH-069`, `ARCH-070`, `ARCH-071`, `ARCH-072`, `ARCH-073`, `ARCH-074`, `ARCH-075`, `ARCH-076`, `ARCH-077`, `ARCH-078`, `ARCH-079`, `ARCH-080`

**Owns current question after cutover:** How does DMTZ durably retain evidence, provenance, time, correction and replay state without turning storage or copied evidence into source truth?

## Canonical contract

DMTZ uses a **lakehouse-first framework evidence plane**:

1. Delta Lake tables are the canonical durable structured persistence substrate for evidence manifests, normalized journals, temporal/provenance links, basis/common-derivation relationships and lifecycle metadata.
2. A separately governed cloud-object payload plane retains only large/opaque artifacts whose exact retention is justified.
3. Unity Catalog managed tables/volumes are preferred only when deployment verification and policy permit them; external Delta/object storage remains a valid portability realization.
4. Graph, search, vector, cache and serving stores are derived rebuildable projections, never competing truth stores.
5. Delta transaction-log time travel is infrastructure convenience, not the DMTZ historical replay contract.

The evidence chain is:

**source-owned occurrence → durable evidence identity + source/provenance locator → multi-coordinate time envelope → minimized retained payload/material → normalized typed derivation → proposition/basis/common-derivation links → non-rewriting correction/supersession journal → lifecycle/retention state → derived projections**.

## Truth and provenance boundary

The framework evidence plane is authoritative for **what DMTZ collected or retained and when**. Copying evidence does not transfer domain Assertion Authority or create independent corroboration.

Retained evidence preserves source identity, source-native revision/locator where available, authority role/limitations, common derivation, capture/processing provenance, integrity digest where safe and material temporal coordinates.

Physical deduplication may share bytes while logical evidence occurrences remain distinct.

## Temporal architecture

Preserve independently where material:

- event/effective time;
- source-recorded time;
- source-available time;
- framework collection time;
- framework persistence time;
- correction/supersession time;
- communication time.

Late evidence remains late for an earlier knowledge cut. Current-state views do not project latest state backward. Correction/supersession is non-rewriting.

## Data minimization and lifecycle

Capture classes distinguish metadata/hash-only, minimized structured payload, complete bounded source event and separately governed large/opaque artifact. Retain the minimum class that can satisfy the promised proposition, replay and basis requirement.

Storage retention, retained resolution/detail and reporting/retrieval relevance are independent. Supported lifecycle states include `RECENT_FULL`, `WARM_REPLAY`, `SUMMARY_ELIGIBLE`, `COLD_PINNED`, `PROVENANCE_STUB` and `EXPIRED`.

Ordinary deployment defaults may use bounded horizons, but exact product/audit/legal/security commitments override ordinary age-only TTL. Active Investigations, Causal Claim basis, retained Explanation/basis promises and Gate/Safeguard audit evidence can pin dependent material.

Lossy rollup cannot silently replace exact run/version evidence, causal basis, control enforcement evidence, authentic retained communication or evidence needed for strong negatives.

Payload expiry may leave a provenance stub. A stub can establish that a reference existed and detail expired; it cannot recreate expired contents.

## Security and deployment variability

Logical evidence may be physically sharded by tenant, region, residency or security boundary. Cross-boundary links exist only where authorized and semantically valid.

Delta Lake is the structured architecture contract; platform-specific capabilities remain conditional on verified target support.

## Architecture boundary

This segment does not select acquisition polling/streaming, a final event bus, graph/search/vector product, serving cache, final backup vendor, lifecycle orchestrator, identity/authorization implementation, model stack or active-control runtime.

## Provenance

- `docs/concepts/phase_010/02_evidence_provenance_temporal_persistence_architecture/README.md`
- atomic ARCH-033–ARCH-080 files under that Phase 010 group
- Phase 010 decisions D-1299–D-1336 and EPT02-01–EPT02-72 review evidence
