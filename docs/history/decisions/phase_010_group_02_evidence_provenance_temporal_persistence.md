# Phase 010 Group 02 — Evidence, Provenance, Temporal & Persistence Decisions

### D-1299 — Group 02 selects a lakehouse-first canonical evidence persistence plane
**Status:** Accepted

Framework-owned structured evidence/history uses Delta Lake as the canonical persistence substrate; large/opaque payloads are selectively retained in governed object storage.

### D-1300 — The framework persistence plane is not a new source authority
**Status:** Accepted

It is authoritative for what the framework captured/retained and when, while retained source evidence keeps its original source/authority role and limitations.

### D-1301 — Durable framework evidence identity is separate from source-local identity and physical location
**Status:** Accepted

Evidence identity survives compaction, archival movement, restore and payload lifecycle transitions.

### D-1302 — Source locator/revision and payload integrity digest are retained where feasible/safe
**Status:** Accepted

Digest equality supports integrity/deduplication only; it does not manufacture source independence.

### D-1303 — Proposition and basis-link identity is durable
**Status:** Accepted

Statement-to-basis traceability cannot depend on report rendering or transient query plans.

### D-1304 — Material history uses multiple time coordinates
**Status:** Accepted

Event/effective, source recorded/available, collected, persisted, correction/supersession and communication times remain distinct where applicable.

### D-1305 — Historical state is represented explicitly in rows/journals rather than by current-state back-projection
**Status:** Accepted

Effective intervals/versioned state remain reconstructable independently of latest convenience views.

### D-1306 — Availability-by-K is retained where the product promises as-known replay
**Status:** Accepted

Earlier event time alone cannot qualify evidence for an earlier knowledge cut.

### D-1307 — Late evidence remains late
**Status:** Accepted

Later evidence can change retrospective reasoning without appearing in earlier as-known cuts.

### D-1308 — Corrections and supersessions are non-rewriting linked history
**Status:** Accepted

Material prior state is retained where replay promises require it.

### D-1309 — Physical file rewrite is not semantic historical rewrite
**Status:** Accepted

Delta compaction/clustering/checkpoint maintenance is allowed when the logical record set/IDs remain stable.

### D-1310 — Normalized facts retain source-evidence and parser/normalizer provenance
**Status:** Accepted

Reprocessing creates a new derivation lineage, not new independent source evidence.

### D-1311 — Common derivation is persisted explicitly
**Status:** Accepted

Duplicate/common-derived rows cannot become independent corroboration through storage cardinality.

### D-1312 — Physical payload deduplication may coexist with distinct logical evidence occurrences
**Status:** Accepted

Context/source/time identity controls logical occurrence identity, not byte equality alone.

### D-1313 — Evidence capture is data-minimized by default
**Status:** Accepted

Capture classes range from metadata/hash-only through bounded exact payload/object retention according to evidence need and sensitivity.

### D-1314 — Delta Lake is the canonical structured persistence format
**Status:** Accepted

Delta provides scalable structured history close to Spark/Databricks workloads without requiring a separate canonical relational/event/graph store.

### D-1315 — Unity Catalog managed tables are preferred only when verified and policy-compatible
**Status:** Accepted

Managed-table availability/lifecycle is deployment-specific and cannot be presumed universally.

### D-1316 — External Delta over governed organization-controlled object storage is a supported realization
**Status:** Accepted

This preserves portability/lifecycle control when managed assets are unavailable or inappropriate.

### D-1317 — Large/opaque payloads use a separately governed object plane
**Status:** Accepted

Unity Catalog volumes are preferred where verified but are not a universal dependency.

### D-1318 — Canonical semantics do not require FILE, VARIANT or other preview/runtime-specific features
**Status:** Accepted

Verified deployments may use them as optimizations while portable baseline representations remain valid.

### D-1319 — Graph databases/projections are derived, not canonical
**Status:** Accepted

Typed traversal can be materialized later without making reachability truth or creating a second system of record.

### D-1320 — Search/vector indexes and serving caches are derived, rebuildable projections
**Status:** Accepted

Ranking/cache state cannot strengthen evidence or overwrite canonical history.

### D-1321 — Canonical schemas and parsers are revisioned
**Status:** Accepted

Older evidence cannot be silently reinterpreted under newer schema/parser semantics.

### D-1322 — Storage migrations preserve evidence identity/provenance/history
**Status:** Accepted

Representation may change physically without rewriting what was collected/known.

### D-1323 — Retention policy is explicit, versioned and effective-dated
**Status:** Accepted

Policy identity/history remains observable when lifecycle rules change.

### D-1324 — Storage retention and reporting relevance are independent
**Status:** Accepted

Retained old history does not automatically surface in routine reports; excluded old evidence is not thereby deleted or universally irrelevant.

### D-1325 — Lifecycle states distinguish recent detail, warm replay, summary eligibility, cold pinning, provenance stub and expiry
**Status:** Accepted

Lifecycle state is operational metadata, not evidence strength or severity.

### D-1326 — The ordinary reference retention profile is configurable rather than semantic
**Status:** Accepted

A practical starting profile is ~120 days recent full detail, ~400 days detailed replay, and up to ~24 months approved trend aggregates, with longer exact history opt-in by explicit need.

### D-1327 — Service classes bind independent retention obligations
**Status:** Accepted

SC-01–SC-06 need not share one history horizon or resolution.

### D-1328 — Active dependencies can pin evidence beyond ordinary TTL
**Status:** Accepted

Investigations, Causal Claims, retained Explanations/basis promises and control/audit records may extend required retention.

### D-1329 — Legal/regulatory/contract/security holds override ordinary TTL for scoped material
**Status:** Accepted

Hold release returns material to lifecycle evaluation; it does not itself imply immediate deletion.

### D-1330 — Lossy downsampling is allowed only where future exact evidence is not promised
**Status:** Accepted

Older metrics may become coarser trend rollups, but exact execution/causal/control/communication/basis evidence cannot be silently summarized away.

### D-1331 — Exact basis promises require non-lossy material for the promised horizon or an explicit limitation
**Status:** Accepted

A summary cannot substitute for expired exact evidence.

### D-1332 — Payload bytes/detail may expire while a provenance stub remains
**Status:** Accepted

The stub records permitted identity/time/digest/lifecycle metadata but cannot reconstruct expired content.

### D-1333 — Archived, expired, source-expired, restricted and currently inspectable basis states remain distinct
**Status:** Accepted

A surviving citation cannot imply current raw-basis inspectability.

### D-1334 — Archive restore preserves original identity and provenance
**Status:** Accepted

Restore creates availability of old evidence, not a new observation.

### D-1335 — Multi-year detailed accumulation is not the default architecture posture
**Status:** Accepted

History beyond ordinary replay/trend horizons requires explicit product, recurrence, incident, audit, security, legal or analytical value; cost/minimization are legitimate lifecycle inputs but cannot weaken promised evidence obligations.

### D-1336 — Group 02 accepts ARCH-033–ARCH-080 and promotes Group 03
**Status:** Accepted — Group 02 closure

EPT02-01–EPT02-72 pass. Group 02 closes with Delta Lake canonical structured persistence, selective object payload retention, explicit bitemporal/provenance semantics and tiered retention/relevance lifecycle. Group 03 — Identity, Scope, Authority, Authorization & Disclosure Architecture is next.
