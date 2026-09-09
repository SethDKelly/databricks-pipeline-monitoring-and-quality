# Identity, Scope, Governance, Authority & Authorization Sources

**Canonical key:** `integration.group-02`

**Kind:** INTEGRATION CONTRACT

**Authority:** CANONICAL CURRENT AUTHORITY

**Migration record:** `stable_family.INTG`

**Stable IDs:** INTG-023–INTG-050

**Owns current question:** Which evaluated sources can evidence identity, scope, semantics, governance, Assertion Authority and Capability Authorization, and where do their authority/history/access boundaries stop?

## Canonical source findings

- Unity Catalog / Databricks is strong for Databricks-local object/principal identity and current access state; platform identifiers are not automatically ecosystem Entity Identity and Information Schema visibility is observer-relative.
- Collibra can be authoritative for explicitly assigned semantic, responsibility and classification facets; Collibra UUIDs remain source-local identity, ordinary tags are not automatically governed Classification, and operating-model scope is not framework Monitoring Scope.
- Immuta can establish Immuta-managed policy decisions inside registered scope; effective authorization with Unity Catalog can be a composed principal/population/path-specific proposition.
- GitHub is strong for repository-local identity, review responsibility, repository governance and bounded audit history; these facts do not automatically become data/business ownership or Databricks authorization.
- External IAM/IdP state remains environment-specific. Synchronized identities/groups retain upstream identity provenance.

No evaluated vendor natively supplies the framework's Monitoring Scope or full Assertion Authority merely through a role/owner field. Cross-system Entity Identity requires explicit governed mapping. Current governance ≠ historical governance. Optional-source absence is an explicit gap, never a benign default.

## Stable contracts

### INTG-023 — Source Family Presence & Environment Profile
Record which source families/surfaces are actually installed, enabled, licensed, scoped and verified in the environment; unevaluated or optional presence remains unknown rather than assumed.

### INTG-024 — Unity Catalog Object & Principal Identity
Treat Unity Catalog identifiers as strong Databricks-local object/principal identity, not automatic ecosystem Entity Identity across governance, repository or policy systems.

### INTG-025 — Collibra Resource Identity
Treat Collibra resource UUIDs as Collibra-local identity and require an explicit governed crosswalk to associate them with DMTZ/Databricks entities.

### INTG-026 — GitHub Repository & Path Identity
Treat repository/ref/path identifiers as strong repository-local identity only; code/repository identity does not automatically establish data-asset identity.

### INTG-027 — IAM Principal Source Projection
Treat synchronized Databricks/Immuta principals/groups/attributes as projections whose upstream IAM/IdP provenance and synchronization context remain material.

### INTG-028 — Cross-System Asset Identity Crosswalk
Require explicit cross-system mapping evidence for UC↔Collibra↔Immuta↔GitHub identities; names, aliases and timestamp proximity cannot substitute.

### INTG-029 — Monitoring Scope Declarative Source
No evaluated platform natively owns framework Monitoring Scope; a deliberately governed registry/property/configuration is required where the proposition matters.

### INTG-030 — Semantic Facet Source Ownership
Semantic authority is facet-specific and must be explicitly assigned; comments, glossary terms, business definitions and technical metadata do not inherit universal semantic authority.

### INTG-031 — Technical Schema/Comment vs Business Definition Separation
Technical schema/comment metadata and governed business definition remain separate assertion classes and may have different authorities.

### INTG-032 — Responsibility Assignment Source Semantics
Responsibility evidence is responsibility-type/context specific; source roles/owners do not automatically create broader authority, permission or fault.

### INTG-033 — Classification Scheme Source Semantics
Classification remains scheme/context specific; tags or labels count only under the governed classification scheme/authority that gives them meaning.

### INTG-034 — Policy Context Source Semantics
Policy text/applicability/context can have different source owners and must not be inferred from generic tags, roles or permissions.

### INTG-035 — Assertion Authority Registry Requirement
No evaluated vendor role automatically implements full Assertion Authority; explicit claim-class/context authority rules require a governed source when needed.

### INTG-036 — Unity Catalog Privilege, Ownership & Authorization
Unity Catalog privileges/ownership evidence the exact Databricks privilege plane; ownership does not automatically grant semantic/assertion authority and current privilege state is not historical enforcement.

### INTG-037 — Unity Catalog ABAC Tag Enforcement
ABAC/governed-tag evidence is meaningful only for the exact configured policy/tag/principal/data scope and enforcement plane; tag existence alone is not enforcement proof.

### INTG-038 — Immuta Policy Authorization
Immuta policy decisions are strong within registered/covered scope; they do not automatically describe alternate paths, unregistered populations or other enforcement planes.

### INTG-039 — Collibra Permission vs Governance Responsibility
Permission to view/edit/govern a Collibra resource remains distinct from the responsibility/semantic authority represented by the resource model.

### INTG-040 — GitHub CODEOWNERS, Rulesets, Custom Properties & Roles
CODEOWNERS, rulesets, repository roles and custom properties retain repository-governance meanings and do not automatically become data ownership, Assertion Authority or platform authorization.

### INTG-041 — Current vs Historical Governance Snapshot
Current governance/ownership/permission state cannot be projected backward without qualifying history evidence for the exact proposition and time.

### INTG-042 — Databricks Audit / Information Schema History Boundary
Information Schema is principal-filtered/current-oriented while audit history can provide bounded historical action evidence; neither surface is a universal history ledger.

### INTG-043 — Collibra Resource History Boundary
Collibra history is facet/configuration/permission dependent; history for one characteristic does not prove complete history for all governed facets.

### INTG-044 — Immuta Audit / Identity History Boundary
Immuta identity/policy/audit history is integration/version/registration/retention bound and cannot support broader historical claims outside that envelope.

### INTG-045 — GitHub Audit History Boundary
GitHub audit/repository history has event-class/retention/export limitations; current repository state is not arbitrary-cut historical governance.

### INTG-046 — Disclosure Filtering & Observer-Relative Metadata
Metadata hidden from the current observer/requester remains restricted/unavailable for that view, not nonexistent; visibility must not become negative evidence.

### INTG-047 — Authority Conflict, Co-Authority & Fallback Sources
Conflicting/co-authoritative/fallback sources follow accepted AUTH standing and precedence rules; source availability, recency or specificity creates no hidden winner.

### INTG-048 — Optional Source Absence & Degraded Governance
Absent Collibra/Immuta or other optional sources produce explicit proposition-specific capability gaps, never inferred benign/default governance state.

### INTG-049 — Capability Authorization Composition Across Enforcement Planes
Where effective authorization depends on Unity Catalog + Immuta/IAM/other planes, compose the exact principal/population/policy path; one plane's permission does not universally establish effective access.

### INTG-050 — Group 02 Source Matrix & Group 03 Handoff
Pass identity/governance/authority evidence forward only with explicit source identity, joins, standing, history/access and residual gaps; it does not prove revision→deployment→run→version association.

## Architecture boundary

This contract selects no identity store, authority-rule store, synchronization architecture, IAM product, adapter, cache, persistence schema or policy engine.

## Provenance

- `docs/concepts/phase_009/02_identity_scope_governance_authority_authorization_sources/README.md`
- Phase 009 Group 02 accepted INTG-023–INTG-050.
