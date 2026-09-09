# Phase 009 Group 02 — Identity, Scope, Semantics, Governance, Authority & Authorization Sources

**Status:** Review complete — accepted

## Result

Group 02 accepts **INTG-023–INTG-050** and **GOV02-01–GOV02-48**. No new product concept is required.

The result is proposition-specific source mapping rather than a universal governance system of record. Source identity, authority, historical coverage, and access remain bounded by the exact surface and context established in Group 01.

## Main findings

- **Unity Catalog / Databricks:** strong for Databricks-local object/principal identity and current Unity Catalog access state. Platform identifiers are not automatically ecosystem Entity Identity. Information Schema is observer-relative, and historical reconstruction depends on qualifying audit/history evidence.
- **Collibra:** strong candidate for governed business semantics, responsibilities, and classifications when the organization explicitly assigns those facets authority. Resource UUIDs remain Collibra-local identity; ordinary tags are not a substitute for governed classification; operating-model scope is not framework Monitoring Scope.
- **Immuta:** strong for Immuta-managed access-policy decisions within its registered scope. Effective authorization with Unity Catalog is a composed proposition whose user population and integration path matter.
- **GitHub:** strong for repository-local identity, review responsibility, repository governance, structured repository metadata, and bounded audit history. These facts do not automatically become data/business ownership or data-platform authorization.
- **External IAM / IdP:** remains environment-specific. Synchronized users, groups, and attributes in Databricks or Immuta retain the upstream identity source as material provenance.

## Accepted gaps

1. No evaluated platform natively owns the framework's **Monitoring Scope** proposition; a deliberately governed registry/property/configuration is required.
2. No vendor role or ownership mechanism automatically implements full **Assertion Authority**; explicit authority rules require a governed source.
3. Cross-system **Entity Identity** requires explicit mapped identity evidence.
4. Long-horizon governance replay is limited by source retention and history configuration unless independently retained.
5. Effective authorization across multiple enforcement planes must preserve the exact principal population and policy path.
6. Metadata hidden from a requester cannot be treated as nonexistent.

## Artifacts

- [`source_capability_matrix.md`](source_capability_matrix.md) — proposition-specific support and residual gaps.
- [`external_source_review.md`](external_source_review.md) — current public documentation verified on 2026-08-25.
- [`scenario_review.md`](scenario_review.md) — GOV02-01–GOV02-48 pass.
- [`../../../decisions/phase_009_group_02_identity_governance_sources.md`](../../../decisions/phase_009_group_02_identity_governance_sources.md) — D-935–D-974.

## Architecture boundary

Group 02 selects no identity store, authority-rule store, synchronization architecture, IAM product, adapter, cache, persistence schema, or policy engine. Phase 010 owns technical realization.

## Handoff

**Group 03 — Change Intent, Deployment, Execution, Version & Runtime Evidence is next.**

Group 03 may consume established source-local identities, explicit cross-system mappings, principal identity provenance, authority rules where defined, and known history/access limitations. It must independently establish repository revision → deployment → execution → run-specific version associations; identity, ownership, naming, or timestamp proximity are insufficient.