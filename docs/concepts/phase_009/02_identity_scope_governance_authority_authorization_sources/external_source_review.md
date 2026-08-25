# External Source Review — Phase 009 Group 02

**Verified:** 2026-08-25

This review records current vendor/documentation facts used by Group 02. It is not a substitute for environment-specific feature discovery.

## Databricks / Unity Catalog

- [System tables reference](https://docs.databricks.com/aws/en/admin/system-tables) — system tables are account operational history; `system.access.audit` is documented with 365-day free retention and Public Preview status; system-table access is Unity Catalog governed.
- [Information schema](https://docs.databricks.com/gcp/en/sql/language-manual/sql-ref-information-schema) — privilege-aware current metadata; results are automatically filtered to objects the requester can access.
- [Unity Catalog privileges reference](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/privileges-reference) and [permissions concepts](https://docs.databricks.com/gcp/en/data-governance/unity-catalog/access-control/permissions-concepts) — current privileges, ownership and inheritance for securable objects.
- [TABLE_PRIVILEGES](https://docs.databricks.com/aws/en/sql/language-manual/information-schema/table_privileges) — current Information Schema limitation: `MANAGE` does not currently expose all grants through this relation; SQL/Catalog Explorer is required for the full grant view.
- [Governed tags system table](https://docs.databricks.com/aws/en/admin/system-tables/governed-tags) — Beta; current snapshot includes deleted governed-tag definitions with `deleted_at` and change time.
- [ABAC core concepts](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/core-concepts) and [ABAC overview](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/) — governed tags drive policy matching; changing tags can change access; GRANT policies remain Beta.
- [Identity best practices](https://docs.databricks.com/aws/en/data-governance/unity-catalog/best-practices), [Account SCIM API](https://docs.databricks.com/aws/en/reference/scim-2-1), and [automatic identity management](https://docs.databricks.com/aws/en/admin/users-groups/automatic-identity-management/) — account-level users/groups/service principals are the Unity Catalog principal plane; external IdP synchronization can be identified and audited.

## Collibra

- [Responsibilities](https://productresources.collibra.com/docs/collibra/latest/Content/Responsibilities/to_responsibilities.htm) — resource-role assignments with inheritance through communities/domains.
- [Permissions](https://productresources.collibra.com/docs/collibra/latest/Content/Settings/RolesAndPermissions/Permissions/co_permissions.htm) — global/resource permissions govern Collibra application/resource actions.
- [About tags](https://productresources.collibra.com/docs/collibra/latest/Content/Assets/Tags/co_about-tags.htm) — tags are flexible metadata and explicitly are not strictly governed by Collibra.
- [Data Classification](https://productresources.collibra.com/docs/collibra/latest/Content/Catalog/DataClassification/co_about-data-classification.htm) — controlled data-class capability and REST APIs.
- [Scopes](https://productresources.collibra.com/docs/collibra/latest/Content/Settings/OperatingModel/Scopes/to_scopes.htm) and [asset type assignments](https://productresources.collibra.com/docs/collibra/latest/Content/Settings/OperatingModel/Assignments/to_assignments.htm) — operating-model scope/assignment, distinct from framework Monitoring Scope.
- [Resource history](https://productresources.collibra.com/docs/collibra/latest/Content/History/ref_history-pages.htm) — resource history tracks most resource changes and actors.
- [Release 2026.08](https://productresources.collibra.com/docs/collibra/latest/Content/ReleaseNotes/Archive/ref_release-202608.htm) — history logging can be disabled for selected attribute assignments, so history completeness is configuration-dependent.
- [Resource UUID guidance](https://productresources.collibra.com/docs/collibra/latest/Content/Troubleshooting/ta_find-uuid-metamodel-elements.htm) — assets/domains/communities have UUID resource identifiers.

## Immuta

- [Subscription policies](https://documentation.immuta.com/SaaS/governance/secure-your-data/authoring-policies-in-secure/section-contents/reference-guides/subscription-policies) — grant/guardrail access policy semantics and policy merging.
- [Subscription policy access types](https://documentation.immuta.com/SaaS/governance/secure-your-data/authoring-policies-in-secure/section-contents/reference-guides/subscription-access-types) — integration-specific read/write enforcement; Databricks Unity Catalog supports documented read/write policy enforcement.
- [Attributes and groups](https://documentation.immuta.com/saas/configuration/people/users-index/reference-guides/attribute-and-group-overview) and [identity management](https://documentation.immuta.com/saas/configuration/people/section-contents/reference-guides/index) — user metadata may be local or synchronized from external IAM; group/attribute changes are audited.
- [Data sources in Immuta](https://documentation.immuta.com/saas/configuration/integrations/data-and-integrations/registering-metadata/data-source-overview) — registration/policy behavior differs for Immuta users and remote-platform users.
- [Understanding audit logs](https://documentation.immuta.com/saas/knowledge-base/implementation/audit-and-monitor/understanding-immuta-audit-logs) — policy, approval, identity metadata, tag and query events; documentation recommends export for retention beyond the 90-day default.

## GitHub

- [CODEOWNERS](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners) — code-review responsibility and optional required approval.
- [Repository custom properties](https://docs.github.com/en/organizations/managing-organization-settings/managing-custom-properties-for-repositories-in-your-organization) — organization-managed structured repository metadata; visibility follows repository read access.
- [Rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets) — repository/branch/tag interaction governance, not data governance.
- [Audit log events](https://docs.github.com/en/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/audit-log-events-for-your-organization) and [audit-log API](https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/using-the-audit-log-api-for-your-enterprise) — governance events are audited; Enterprise Cloud documents 180-day general retention and seven-day Git-event retention.

## Environment-specific unknowns retained

- whether Collibra is deployed and which modules/licensing/features are enabled;
- whether Immuta is deployed, which users/data sources are registered, and which integration mode is active;
- which external IAM/IdP is authoritative for users/groups/attributes;
- whether GitHub organization/enterprise custom properties, rulesets and audit-log APIs are available in the target environment;
- which exact Unity Catalog ABAC/preview features are enabled;
- which repository/configuration source, if any, will be governed as the Monitoring Scope and Assertion Authority registry.

These remain `unknown / not yet verified` or conditional support findings rather than assumptions.
