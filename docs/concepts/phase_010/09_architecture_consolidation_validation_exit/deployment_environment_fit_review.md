# Phase 010 Group 09 — Deployment-Environment Fit & External Source Revalidation

**Status:** PASS — reference architecture remains compatible with currently verified public platform capabilities

**External verification date:** 2026-08-31

This review verifies that the frozen architecture does not depend on a public capability claim that has become inconsistent with current vendor documentation. It does not claim that any specific enterprise tenant has the capability enabled; Group 01 deployment discovery remains authoritative for target-environment facts.

## Databricks system tables

Current Databricks documentation continues to describe system tables as a Databricks-hosted analytical store of account operational data in the `system` catalog, governed through Unity Catalog. Databricks explicitly warns that system-table information can be sensitive and discourages moving it outside the platform without appropriate security controls. System-table availability/retention is table-specific rather than one universal history/latency contract.

Reference:

- https://docs.databricks.com/aws/en/admin/system-tables

Architecture fit:

- supports the Group 04/08 choice to use verified system-table/bulk surfaces where proposition-appropriate;
- reinforces that UI/API users should receive governed DMTZ projections rather than unrestricted raw system-table access;
- supports retention/coverage being source-surface specific;
- does not change the rule that system-table presence is evidence availability, not automatic DMTZ Assertion Authority.

## Databricks billing publication timing

The current `system.billing.usage` reference states that original billable-usage records are typically available within approximately 12 hours, with new workspaces potentially taking longer.

Reference:

- https://docs.databricks.com/aws/en/admin/system-tables/billing

Architecture fit:

This directly supports the Phase 010 rejection of one universal freshness SLO. Billing/cost attribution can legitimately operate on a slower service envelope than SC-01 near-current run facts or SC-06 active control.

## Databricks service principals and workload identity federation

Current Databricks documentation describes service principals as specialized automation identities and recommends OAuth token federation/workload identity federation for automated workloads where supported, eliminating the need to manage Databricks PAT/client-secret credentials for those workloads.

References:

- https://docs.databricks.com/aws/en/admin/users-groups/service-principals
- https://docs.databricks.com/aws/en/dev-tools/auth/oauth-federation

Architecture fit:

- supports separate least-privilege workload identities;
- supports the short-lived/federated credential preference in Group 08;
- does not make federation a universal hard dependency because legacy/target-environment state still requires discovery.

## Unity Catalog governance

Current Databricks documentation continues to describe Unity Catalog as the built-in governance layer for access control, lineage and audit and notes that system-table access is governed through Unity Catalog in applicable workspaces.

References:

- https://docs.databricks.com/aws/en/data-governance/unity-catalog/
- https://docs.databricks.com/aws/en/admin/system-tables

Architecture fit:

Unity Catalog remains a strong conditional realization for canonical table/volume governance and source access. It does not replace DMTZ Monitoring Scope, Assertion Authority or proposition-specific Capability Authorization semantics.

## GitHub deployment environments and protection rules

Current GitHub documentation continues to state that deployment protection rules can require conditions before an environment-referencing job proceeds, including manual approvals and custom GitHub App protection rules. Environment protection occurs before the protected job is sent to a runner, while environment secrets become available only after the job is sent to a runner.

References:

- https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments
- https://docs.github.com/en/actions/concepts/workflows-and-actions/deployment-environments

Architecture fit:

- continues to justify GitHub environments as a strong candidate pre-start Gate adapter for the exact protected GitHub job/deployment opportunity;
- does **not** prove downstream Databricks execution was gated without durable cross-system correlation;
- does not make GitHub custom protection rules a universal dependency because repository/plan/target capability still requires verification.

## Public capability vs target deployment

No current public documentation changes the Phase 010 rule:

**documented capability ≠ target deployment presence ≠ entitlement ≠ enablement ≠ permission ≠ reachability ≠ coverage ≠ proposition-specific usability.**

Before implementation enables a dependent feature, environment discovery must bind the exact capability instance and record known limits.

## Fit conclusion

The frozen architecture remains compatible with current public Databricks/GitHub capabilities and remains appropriately conservative around variable publication latency, system-table sensitivity, credential federation, environment protection and source-specific retention/coverage.

No source revalidation finding requires ARCH-501 or reopening an accepted functional contract.
