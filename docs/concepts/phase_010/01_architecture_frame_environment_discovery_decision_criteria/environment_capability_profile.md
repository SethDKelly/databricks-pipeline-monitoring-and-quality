# Phase 010 Group 01 — Environment Capability Profile

## Purpose

Define the minimum discovery record required before later architecture groups treat a vendor capability as usable in a target enterprise deployment.

This is a logical profile, not a final storage schema.

## Fact classes

Every recorded value is tagged as one of:

- `verified_public_vendor_fact`;
- `target_environment_fact`;
- `organization_requirement_or_policy`;
- `architecture_assumption`;
- `unknown_unverified`.

A value also retains source/provenance and verification time. If an assumption later becomes verified, the new fact supersedes the assumption for current decisions without rewriting the earlier record.

## Capability instance identity

Minimum identity dimensions where applicable:

| Dimension | Examples / notes |
|---|---|
| Vendor/product | Databricks, GitHub, Collibra, Immuta |
| Deployment model | SaaS, Enterprise Cloud, GHE.com, GHES, Government, self-hosted |
| Cloud/hosting | AWS, Azure, GCP, vendor-hosted, customer-hosted |
| Region / Geo / residency zone | exact region/Geo when availability or processing differs |
| Account / enterprise / tenant | source-native stable identifier where possible |
| Workspace / metastore / org / repo scope | exact scope relevant to the capability |
| Edition / plan / license / entitlement | exact known package or unknown |
| Product/version/release | including GHES or self-hosted version where applicable |
| Feature/surface | exact system table, API family, audit surface, workflow feature, connector, etc. |

Names alone are not durable identity where a stable source ID exists.

## Capability dimensions

Record independently rather than collapsing to one `available` field:

| Dimension | Representative states |
|---|---|
| documented support | supported / limited / documented unavailable / not verified |
| deployment presence | present / absent / unknown |
| enablement/configuration | enabled / disabled / partial / unknown |
| release status | GA / preview-beta / private preview / deprecated / unsupported version / unknown |
| license/entitlement | entitled / not entitled / unknown |
| authorization | authorized / denied / partial / unknown |
| reachability | reachable / unreachable / partial / unknown |
| observability/coverage | sufficient for bounded role / partial / unsupported / unknown |
| time/retention | verified horizon/scope / partial / unknown |
| quota/capacity | verified / measured / contract-specific / unknown |
| cost surface | verified public / contract/tenant / measured / unknown |
| integration health | healthy for observed probe / degraded / failed / not observed |
| optionality | MVP required / conditional / enterprise extension / optional enrichment |

## Proposition-specific usability

Do not derive one global capability status. Evaluate usability for an exact requirement:

**capability instance + proposition/evidence role + subject/scope + grain + time horizon + service class + authorization/disclosure context → usable / partially usable / unusable / unknown for that requirement**.

Examples:

- a regional Databricks system table can be usable for one workspace-region operational query while insufficient for an account-wide negative claim;
- GitHub Actions environments can be usable for a GitHub job Gate while insufficient to prove a Databricks run was gated without cross-system correlation;
- Collibra metadata may be usable for a semantic assertion while a feature absent from the deployment offering remains unavailable;
- an installed source can still be unusable to the integration principal because permission or network reachability is missing.

## Discovery checklist — Databricks

At minimum discover where relevant:

- cloud provider and region for every workspace/metastore in scope;
- account/workspace/metastore identifiers and Unity Catalog status;
- relevant SKU/edition/contract restrictions if material;
- system catalog/table presence and access for the integration principal;
- Jobs/Lakeflow/SQL warehouse/serverless/Unity Catalog features used by the architecture;
- enabled preview features and their scope;
- system-table regional/global behavior for required propositions;
- lineage/query/history/audit surfaces and retention observed for the tenant;
- DQX, expectations, metric/data-quality monitoring and anomaly features actually enabled/usable;
- authentication/service-principal configuration and permissions;
- private networking/egress/PrivateLink/firewall restrictions;
- data-residency/Geo/cross-Geo settings when Designated Services are considered;
- API limits or contract-specific constraints where material;
- exact external consumer paths in scope.

## Discovery checklist — GitHub

At minimum discover where relevant:

- GitHub.com/GHE.com/GHES deployment and GHES version if applicable;
- organization/enterprise/repository stable IDs and repository visibility;
- plan/enterprise capabilities relevant to audit/Actions/environments/rules;
- Enterprise Managed Users or other identity model;
- GitHub App/authentication model and granted repository/org permissions;
- audit log and streaming availability/configuration;
- Actions enabled state, runner model, environment/protection-rule availability;
- API version/auth/rate-limit context and network restrictions;
- retention/export configuration used by promised historical propositions.

## Discovery checklist — Collibra

When installed/in scope discover:

- commercial cloud / UAE / Government / self-hosted deployment;
- product version/release channel;
- licensed products/capabilities;
- Edge/customer-managed/Collibra Cloud site model;
- exact connector/capability availability and configuration;
- relevant resource-history/audit settings;
- API authentication, permissions, throttling and tenant-specific limits;
- residency/network constraints.

## Discovery checklist — Immuta

When installed/in scope discover:

- deployment model and version;
- licensed/in-scope capabilities;
- Databricks integration mode and protected population;
- audit configuration, retention and export path;
- policy/action/query evidence available to the integration principal;
- API authentication, permissions, limits and contract constraints;
- network/residency constraints.

## Discovery outputs

A discovery pass must produce:

1. capability instances and dimensions;
2. evidence/provenance for each target-environment fact;
3. unknowns/assumptions with owner and validation route;
4. proposition/service-class usability conclusions;
5. optional-source degraded behavior;
6. decisions blocked by unresolved facts;
7. next revalidation trigger/time where capability drift is material.

A discovery pass is not an assertion that the environment will remain unchanged indefinitely.
