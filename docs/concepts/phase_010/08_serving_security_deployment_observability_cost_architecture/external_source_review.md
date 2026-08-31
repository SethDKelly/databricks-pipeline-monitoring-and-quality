# Group 08 External Source Review

**Reviewed:** 2026-08-31

Public vendor documentation is architecture input only. Group 01 target-environment verification remains required before any deployment-specific capability is assumed.

## Databricks

Current public documentation supports the architecture’s conditional use of service principals/OAuth for workload identity, secret facilities, private-connectivity/network controls, system tables for operational/billing evidence, and Jobs/API surfaces. Publicly documented source/system-table publication characteristics differ by source, reinforcing the SC-01–SC-06 service-class SLO model rather than one universal freshness number.

Databricks system/administrative telemetry can contain sensitive account/workspace-wide information. DMTZ therefore serves governed projections rather than granting UI/API consumers broad raw administrative-table access.

Exact endpoint quotas, system-table availability, cloud/region support, networking and identity features remain capability-instance facts.

## GitHub

Current GitHub documentation supports GitHub App installation authentication/rate-limit state, Actions OIDC for short-lived cloud credentials, webhook/incremental event patterns, and environment/deployment-protection behavior used by Group 07.

Architecture interpretation: prefer scoped workload identities and efficient incremental/reconciliation acquisition, but retain observed rate/secondary-limit state and never treat webhook silence or quota exhaustion as absence.

## Collibra / Immuta

Tenant licensing, API surfaces, capacity and operational limits remain environment/contract specific. Group 08 therefore keeps both capability-gated/optional unless a target deployment verifies the exact required feature.

## Vendor neutrality

No vendor operational feature becomes DMTZ source authority, Monitoring Scope, Assertion Authority, evidence sufficiency, control effectiveness or historical truth merely because it is selected as the deployment realization.