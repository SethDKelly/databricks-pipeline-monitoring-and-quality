# Decision Records — Pre-Group-05 Capability Authorization Addendum

This file continues the numbered durable decisions. D-001–D-039 remain in [`README.md`](README.md); D-040–D-046 remain in [`phase_003_group_03_runtime_health_and_safeguard.md`](phase_003_group_03_runtime_health_and_safeguard.md); D-047–D-055 remain in [`phase_003_group_04_lineage_investigation_causality.md`](phase_003_group_04_lineage_investigation_causality.md).

### D-056 — Add Capability Authorization as a narrow post-Phase-002 concept addendum

**Status:** Accepted — discovered before Phase 003 Group 05

The accepted model repeatedly depended on an `authorized evidence view` but no concept independently owned whether a principal may perform a named capability on a subject/context/time. **Capability Authorization** is therefore accepted as the 22nd concept through an explicit post-exit addendum.

The concept defines authorization semantics without selecting authentication, IAM, RBAC/ABAC, Databricks ACLs, Immuta, or another enforcement architecture.

### D-057 — Raw-data, analytical, metadata, operational, and safeguard capabilities are independent

**Status:** Accepted — pre-Group-05 refinement

Direct/raw data read, derived health/Assessment visibility, governance/metadata visibility, Lineage/RCA participation, job/run operational control, and Propagation Safeguard authority must be independently resolvable capabilities.

Permission in one category does not silently imply another. In particular, job-operation authority does not grant raw-data access, and denial of raw-data access does not automatically prohibit approved metadata/health/RCA analysis.

### D-058 — Restricted-data analysts can reason over authorized derived evidence

**Status:** Accepted — pre-Group-05 refinement

An analyst may perform useful Investigation/root-cause analysis without direct row/column access by using an authorized projection of aggregate health metrics, Assessments, execution timing, freshness, historical Lineage, policy/restriction summaries, responsibility context, Causal Claim state, Impact, and safeguard state.

Derived or metadata evidence is not automatically unrestricted. Sensitive thresholds, metrics, topology, identities, policy details, or causal evidence can remain redacted/opaque while the product communicates limitations honestly.

### D-059 — Policy Context and Responsibility Assignment do not become authorization

**Status:** Accepted — pre-Group-05 refinement

Policy Context describes applicable policies/restrictions; Responsibility Assignment describes named responsibility. Neither concept grants or denies access or operational capability. Classification and Monitoring Scope likewise remain separate from Capability Authorization.

Authorization decisions may consume policy/classification context through later explicit authority rules, but synchronization order or role/title never creates permission.

### D-060 — Analysis permission and production-control permission remain separate through Group 05

**Status:** Accepted — pre-Group-05 refinement

Explanation and Investigation must operate over the actor's authorized evidence projection. A principal permitted to analyze health/root cause may still be unable to update/retry a job or activate a safeguard. Conversely, an explicitly authorized job operator may perform an operational action without obtaining raw-data read access.

Group 05 must preserve this separation while defining downstream Impact and audience-specific Explanation. The exact IAM/enforcement mechanisms and job-update action vocabulary remain deferred.

## Current phase state

This refinement **does not start Phase 003 Group 05**. Groups 01–04 remain accepted; Group 05 — Downstream Impact, Annotation & Explanation remains next.
