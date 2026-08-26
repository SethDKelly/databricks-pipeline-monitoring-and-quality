# Phase 010 Group 02 — Exit Review

**Status:** COMPLETE / ACCEPTED

## Accepted range

- ARCH-033–ARCH-080 accepted.
- Cumulative Phase 010 architecture range: ARCH-001–ARCH-080.
- EPT02-01–EPT02-72 pass.
- D-1299–D-1336 accepted.

## Exit conclusion

The evidence/time/persistence architecture is sufficiently concrete for identity/authority/authorization architecture to begin without making storage technology determine source truth.

The selected shape is:

**Delta Lake canonical structured journals/manifests + selectively retained cloud-object payloads + derived rebuildable graph/search/serving projections**.

Unity Catalog managed assets are a preferred verified deployment realization, not a universal prerequisite.

## Retention conclusion

Group 02 explicitly resolves the `history is valuable but unlimited accumulation is noisy/costly` concern through independent lifecycle dimensions:

- possession/TTL;
- detail/resolution tier;
- reporting/retrieval relevance;
- dependency/hold pinning.

The ordinary reference profile keeps a quarter-plus recent detailed window (~120d), approximately one year-plus detailed replay (~400d), and can retain longer approved trend aggregates (~24m), while multi-year exact material is opt-in/pinned by product, incident, recurrence, audit, security, legal or other explicit need.

These are policy defaults, not evidence semantics or universal mandates.

## Architecture safeguards

1. Delta time travel is not the product replay model.
2. Source copies never become newly authoritative/independent.
3. Late evidence does not backfill prior K.
4. Corrections/supersessions do not rewrite prior history.
5. Physical compaction is not semantic downsampling.
6. Exact basis promises block lossy lifecycle transitions.
7. Payload expiry remains distinguishable from source absence.
8. Derived graph/search/cache state cannot become a competing truth store.
9. Public vendor features are not assumed present in every deployment.
10. Cost pressure cannot silently weaken a promised retention/evidence burden.

## Residual risks / later ownership

- Group 03: exact identity crosswalk, Monitoring Scope, Assertion Authority, authorization/disclosure and historical authorization records.
- Group 04: ingestion/checkpoint/acquisition health and publication-lag capture.
- Group 05: exact runtime/input/output/measurement/Lineage/consumer persistence schemas.
- Group 06: Investigation/claim persistence details, historical replay query engine, retained Explanation composition and basis inspection.
- Group 08: backup/DR implementation, storage lifecycle automation, cost controls and operational SLOs.

## Group 03 entry

Group 03 may now design identity/scope/authority/authorization using ARCH-001–ARCH-080. It must preserve stable evidence identity, canonical/derived store roles, time/history semantics and retention/disclosure boundaries.
