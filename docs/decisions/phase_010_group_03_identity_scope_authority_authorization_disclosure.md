# Phase 010 Group 03 — Identity, Scope, Authority, Authorization & Disclosure Decisions

### D-1337 — DMTZ owns a canonical ecosystem Entity registry
**Status:** Accepted

Canonical tenant-scoped entity identity is framework/organization state; vendor-local IDs remain linked source identities.

### D-1338 — Canonical identity is tenant scoped
**Status:** Accepted

Cross-tenant equality requires explicit federation evidence; matching IDs/names never merge tenants by convenience.

### D-1339 — Source identity bindings are evidence-bearing records
**Status:** Accepted

Bindings retain source capability instance, stable ID, mapping basis, assertion provenance and time.

### D-1340 — Rename continuity and delete/recreate are distinct
**Status:** Accepted

Stable identity/evidence governs continuity; visible path reuse cannot silently preserve identity.

### D-1341 — Cross-system identity requires explicit mapping evidence
**Status:** Accepted

Names, owners, emails, paths and timestamp proximity may nominate candidates but cannot alone verify identity.

### D-1342 — Identity mappings can remain conflicting or unresolved
**Status:** Accepted

No universal confidence score or forced winner is introduced.

### D-1343 — Human/group/service/application principals are normalized but distinct
**Status:** Accepted

Source-local principal IDs and upstream IdP provenance remain material.

### D-1344 — Run-as, impersonation and delegation do not merge actors
**Status:** Accepted

Acting relationships are explicit and do not transfer authority/permission automatically.

### D-1345 — Membership is temporal evidence
**Status:** Accepted

Current group/role membership cannot prove historical membership.

### D-1346 — Upstream IdP provenance is retained where known
**Status:** Accepted

Synchronized vendor identity does not silently become the original authoritative identity source.

### D-1347 — Monitoring Scope is an organization-owned registry
**Status:** Accepted

No evaluated vendor natively owns the complete framework Monitoring Scope proposition.

### D-1348 — Monitoring Scope is revisioned and bitemporal
**Status:** Accepted

Add/remove changes do not rewrite earlier expected coverage.

### D-1349 — Scope supports explicit membership and governed selectors
**Status:** Accepted

Selector logic/version is inspectable and preserves input authority/limitations.

### D-1350 — Bounded negative claims can use scope materialization
**Status:** Accepted

Materialization establishes expected population context, not successful observation coverage.

### D-1351 — Unknown scope membership is not exclusion
**Status:** Accepted

Unavailable selector/identity evidence cannot shrink the scope denominator silently.

### D-1352 — Monitoring Scope and authorization are independent
**Status:** Accepted

In-scope does not grant access; technically accessible does not imply in-scope.

### D-1353 — Assertion Authority is a canonical policy-as-data registry
**Status:** Accepted

Authority rules are structured, versioned organization state realizing AUTH-001–AUTH-008.

### D-1354 — Authority targets exact proposition/facet/context/time dimensions
**Status:** Accepted

Authority over one semantic facet does not transfer to health, cause, Impact, control or compliance.

### D-1355 — Precedence, co-authority and fallback are explicit rule data
**Status:** Accepted

No latest/specificity/majority/source-order resolver exists by default.

### D-1356 — Authority conflicts and resolutions are retained separately
**Status:** Accepted

Resolution does not erase the conflicting source assertions.

### D-1357 — Authority history is non-rewriting
**Status:** Accepted

Later authority policy can change current/retrospective resolution without pretending it governed the earlier cut.

### D-1358 — Vendor roles/ownership are not automatic Assertion Authority
**Status:** Accepted

UC owner, GitHub owner/reviewer, Collibra responsibility and Immuta permission require explicit organization mapping for any DMTZ authority target.

### D-1359 — Causal confirmation has an explicit authority profile
**Status:** Accepted

Eligibility is resolved separately; `confirmed` remains REF-017 + AUTH-034 gated.

### D-1360 — Capability Authorization is versioned policy-as-data
**Status:** Accepted

Framework action permission binds principal/action/subject/context/time/detail independently from source IAM.

### D-1361 — Authorization uses a granular canonical action vocabulary
**Status:** Accepted

Inspect/query/view/export/publish/review/approve/confirm/control actions are not one generic access permission.

### D-1362 — Authorization binds exact principal, action, subject and context
**Status:** Accepted

Audience, purpose, delivery, environment and detail are included when material.

### D-1363 — Authorization preserves allowed/denied/conditional/unknown/conflicting/unavailable
**Status:** Accepted

Missing policy or membership never becomes allow by convenience.

### D-1364 — Membership and inheritance composition are explicit
**Status:** Accepted

Vendor hierarchy/transitivity is not generalized across sources.

### D-1365 — There is no universal deny-wins or allow-wins rule
**Status:** Accepted

Conflict composition is capability/context specific and governed.

### D-1366 — Material authorization evaluations may persist actual decision records
**Status:** Accepted

A record retains rule/input manifest and proves evaluation occurred, not enforcement/action success.

### D-1367 — Current and historical authorization are independent evaluations
**Status:** Accepted

Historical permission is not current permission; current permission is not historical evidence.

### D-1368 — Actual retained authorization decision differs from replay-derived evaluation
**Status:** Accepted

Reconstruction cannot prove an authorization check actually occurred at the time.

### D-1369 — Authorization does not prove enforcement
**Status:** Accepted

Request/delivery/acceptance/enforcement/action/outcome remain separate evidence.

### D-1370 — Service processing authorization is separate from requester access
**Status:** Accepted

Application/service-principal permissions are never inherited by end users.

### D-1371 — Source acquisition prefers dedicated least-privilege workload identities
**Status:** Accepted

Human/admin credentials are not the reference integration posture where service identity is available.

### D-1372 — Break-glass/delegation are bounded, expiring and auditable
**Status:** Accepted

Emergency capability does not create universal superuser authority or strengthen truth.

### D-1373 — Disclosure binds requester, audience, purpose and delivery context
**Status:** Accepted

Authentication alone is insufficient to determine visible content.

### D-1374 — Conclusion/context/limitation/basis/provenance/detail are separately authorized
**Status:** Accepted

Result visibility never automatically grants raw basis visibility.

### D-1375 — Disclosure projection supports exact/coarse/redacted/opaque/withheld
**Status:** Accepted

Projection form is detail authorization, not epistemic strength.

### D-1376 — Safe abstraction is epistemically monotone
**Status:** Accepted

A projection may say less but cannot strengthen, broaden, merge subjects or remove material limitations.

### D-1377 — Basis inspection is itemwise
**Status:** Accepted

Internal basis traceability remains complete while each visible basis item is independently projected.

### D-1378 — Hidden basis existence/count/type/provenance can be sensitive
**Status:** Accepted

Opaque references and withheld counts are disclosure-governed.

### D-1379 — Disclosure evaluation may defend against mosaic/differencing leakage
**Status:** Accepted

Repeated query context can narrow projection without becoming a truth change.

### D-1380 — Tenant/residency boundaries constrain governance metadata and evidence movement
**Status:** Accepted

Cross-shard decision exchange minimizes data movement; evidence is not centralized solely for authorization convenience.

### D-1381 — Canonical policy/rule state lives in Group 02 structured persistence; projections are derived
**Status:** Accepted

No external policy engine, IdP, cache or serving view becomes a competing truth/authority store by implementation convenience.

### D-1382 — Group 03 accepts ARCH-081–ARCH-132 and promotes Group 04
**Status:** Accepted — Group 03 closure

IAD03-01–IAD03-84 pass. Group 03 closes with organization-owned identity/scope/authority/authorization/disclosure architecture. Group 04 — Source Acquisition, Adapter, Synchronization & Integration-Health Architecture is next.