# Phase 010 Group 03 — External Identity / Authorization Review

**Verified:** 2026-08-27

These are public vendor facts and architecture inputs, not guarantees about any target enterprise deployment. ARCH-001–ARCH-032 environment verification remains mandatory.

## Databricks

Current Databricks documentation describes service principals as automation identities and notes identity federation is the default for most workspaces, with legacy non-federated workspaces still possible. Unity Catalog securable-object privileges apply to users, groups and service principals; ownership and `MANAGE` can allow privilege management. Workspace entitlements are an additional access plane and some entitlement behavior is plan-dependent.

Architecture consequences:

- Databricks principal/object IDs are strong Databricks-local identity inputs, not automatic ecosystem identity;
- Unity Catalog privileges/ownership are source-native authorization/enforcement facts, not DMTZ Assertion Authority;
- identity-federation, privilege-model version, entitlements and actual integration-principal permissions are deployment facts;
- dedicated service principals fit least-privilege acquisition better than personal-user credentials where supported.

References:
- https://docs.databricks.com/aws/en/admin/users-groups/service-principals
- https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/
- https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/permissions-concepts
- https://docs.databricks.com/aws/en/security/auth/entitlements

## GitHub

GitHub Apps have no requested API permissions by default; permissions are separately repository, organization, enterprise or account scoped. Installation also determines accessible repositories. Enterprise-installed apps receive enterprise permissions but not repository/organization permissions merely through the enterprise installation. Enterprise Managed Users are IdP-managed and have deployment-specific restrictions.

Architecture consequences:

- App identity, installation identity, repository stable ID and user/team identity remain distinct source identities;
- app permission plus installation scope are both material to effective access;
- GitHub repo ownership/reviewer/team facts do not automatically mean data-platform Assertion Authority;
- GitHub.com, GHE.com, GHES and managed-user deployment differences remain capability-profile inputs.

References:
- https://docs.github.com/en/enterprise-cloud@latest/apps/creating-github-apps/registering-a-github-app/choosing-permissions-for-a-github-app
- https://docs.github.com/en/enterprise-cloud@latest/apps/using-github-apps/installing-a-github-app-on-your-enterprise
- https://docs.github.com/en/enterprise-cloud@latest/apps/using-github-apps/reviewing-and-modifying-installed-github-apps
- https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/understanding-iam-for-enterprises/abilities-and-restrictions-of-managed-user-accounts

## Collibra

Current Collibra documentation distinguishes global and resource permissions. Users inherit permissions through roles/responsibilities; responsibilities assign resource roles to users/groups and can be inherited down community/domain resource hierarchies. License type can constrain usable permissions.

Architecture consequences:

- responsibility/role inheritance is useful governed source evidence when the organization assigns it that meaning;
- inherited Collibra responsibility does not automatically become DMTZ responsibility/authority outside its mapped facet;
- permission/license/deployment context is required before relying on a Collibra action capability.

References:
- https://productresources.collibra.com/docs/collibra/latest/Content/Responsibilities/to_responsibilities.htm
- https://productresources.collibra.com/docs/collibra/latest/Content/Settings/RolesAndPermissions/Permissions/co_permissions.htm

## Immuta

Immuta 2026.1 documentation describes system-level permissions/personas for actions in Immuta, and subscription/data policies for data access at local/domain/global scopes. Databricks integration/audit capability depends on exact connection and privileges. Query-time audit can retain user entitlement/policy context for covered activity; SaaS query-audit history is retention-bounded unless exported.

Architecture consequences:

- Immuta permission/persona is source-local action permission, not DMTZ Assertion Authority;
- policy definition is distinct from query-time effective enforcement evidence;
- user/data-source registration or Unity Catalog integration mode affects coverage depending on integration type/version;
- Immuta audit/policy evidence can enrich historical authorization only within verified coverage/retention.

References:
- https://documentation.immuta.com/2026.1/configuration/people/immuta-users/reference-guides/personas-and-permissions
- https://documentation.immuta.com/2026.1/governance/author-policies-for-data-access-control/authoring-policies-in-secure
- https://documentation.immuta.com/SaaS/governance/detect-your-data/audit/reference-guides/query-audit-logs/databricks-uc

## Consolidated conclusion

No evaluated vendor supplies all of:

**cross-system canonical identity + framework Monitoring Scope + proposition-specific Assertion Authority + framework action authorization + current/historical disclosure policy**.

Group 03 therefore uses organization-owned canonical registries/rules while preserving vendor-local identity, IAM, role, policy and enforcement evidence as bounded source facts.