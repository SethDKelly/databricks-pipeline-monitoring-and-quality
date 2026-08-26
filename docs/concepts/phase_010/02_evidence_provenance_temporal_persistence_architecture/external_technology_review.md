# Phase 010 Group 02 — External Technology Review

**Verified:** 2026-08-26

This review records technology facts used by the Group 02 ADR. Public documentation remains a `verified_public_vendor_fact`, not proof of any specific enterprise deployment capability.

## Delta Lake retention/history

Current Delta Lake documentation states:

- `delta.logRetentionDuration` controls retained transaction-log history and defaults to about 30 days;
- `delta.deletedFileRetentionDuration` controls deleted-file eligibility for VACUUM and defaults to about 7 days;
- historical time travel requires both the needed log history and data files to remain available;
- increasing retention can increase storage cost;
- table history/time travel is therefore an infrastructure capability, not a safe substitute for a multi-year DMTZ product retention contract.

References:
- https://docs.delta.io/table-properties/
- https://docs.delta.io/delta-batch/
- https://docs.delta.io/delta-utility/

Architecture result: DMTZ persists explicit historical/temporal rows and does not depend on Delta transaction-log time travel to reconstruct product history.

## Databricks managed vs external tables

Current Databricks documentation recommends Unity Catalog managed tables as the default/recommended table type. Managed tables let Unity Catalog control storage lifecycle/optimization while external tables leave underlying storage lifecycle under organization/external control.

References:
- https://docs.databricks.com/aws/en/tables/types
- https://docs.databricks.com/aws/en/tables/managed
- https://docs.databricks.com/aws/en/data-governance/unity-catalog/managed-versus-external

Architecture result: prefer managed Delta tables where the target deployment verifies availability and policy fit; retain external Delta as a valid portability/lifecycle realization.

## Non-tabular object payloads

Databricks documents Unity Catalog volumes as governance for non-tabular data in cloud object storage, with managed and external variants.

References:
- https://docs.databricks.com/aws/en/volumes/
- https://docs.databricks.com/aws/en/volumes/volume-files

Architecture result: volumes are a preferred deployment capability where verified, but DMTZ models a logical cloud-object payload plane so absence of Unity Catalog volumes does not invalidate persistence semantics.

## Runtime-specific semi/unstructured features

Current Databricks documentation recommends `VARIANT` for flexible semi-structured data where supported, but Delta VARIANT support requires sufficiently recent Databricks Runtime and upgrades table protocol capabilities. The newer FILE type for unstructured data is currently Beta.

References:
- https://docs.databricks.com/aws/en/semi-structured/variant-json-diff
- https://docs.databricks.com/aws/en/tables/features/variant
- https://docs.databricks.com/aws/en/unstructured/file

Architecture result: canonical evidence envelopes cannot require VARIANT or FILE. A verified deployment may use them as optimizations while preserving a portable baseline representation.

## Physical optimization

Current Databricks documentation recommends automatic liquid clustering/predictive optimization for appropriate Unity Catalog managed tables, but these features have runtime/account/configuration prerequisites.

Reference:
- https://docs.databricks.com/aws/en/tables/clustering

Architecture result: layout/optimization features remain deployment-specific physical choices. They cannot alter logical evidence identity/history.

## Conclusion

The current platform facts support a Delta Lake-first design while reinforcing Group 01's deployment-variability rule. They do **not** justify assuming every enterprise environment has Unity Catalog managed lifecycle, volumes, VARIANT, FILE, predictive optimization or identical retention settings.
