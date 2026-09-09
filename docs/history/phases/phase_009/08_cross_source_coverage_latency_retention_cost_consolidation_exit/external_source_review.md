# External Source Review — Phase 009 Group 08

**Verified:** 2026-08-26

This review records current public operational facts used only for Group 08 latency/retention/quota/cost consolidation. It does not substitute for environment-specific discovery, contracts, negotiated pricing, enabled product editions, actual source volumes, current tenant settings or organizational architecture.

## Databricks system-table availability, retention and cost

- [System tables reference](https://docs.databricks.com/aws/en/admin/system-tables/) — system tables are a Databricks-hosted read-only analytical store in the `system` catalog. Current documentation states that **system tables are free to use and customers are charged for the compute used to query them**.
- The same current reference states that system-table data is not necessarily real-time and that updates occur throughout the day. This is material to as-known/current monitoring latency and negative evidence.
- Current retention is surface-specific rather than universal. Many Phase 009 material sources—including audit, query history, lineage, Jobs/run/task and alert surfaces—have a **365-day free retention period**, while some system tables have different horizons.
- System-table data can be regional or global depending on the source. Regional scope must remain explicit when evaluating account-wide absence/coverage.
- [Billable usage system table](https://docs.databricks.com/aws/en/admin/system-tables/billing) and [pricing table](https://docs.databricks.com/aws/en/admin/system-tables/pricing) provide account usage and SKU price-history evidence that can support architecture cost observability. They do not eliminate the need to model workload/query/storage cost.

## Databricks API limits

- [Databricks REST API reference](https://docs.databricks.com/api/workspace/) states that Databricks enforces rate limits for all REST API calls, generally per endpoint/workspace, with 429 responses when exceeded.
- [Resource limits](https://docs.databricks.com/aws/en/resources/limits) publishes material endpoint-specific limits. Current lineage examples include table-lineage limits of **300 requests/hour and 1,200/day per account**, and column-lineage limits of **1,500/hour and 6,000/day per account**. Other APIs have different workspace/account rates.
- Group 08 therefore does not accept a generic Databricks API polling frequency. Feasible collection depends on exact endpoint, source volume, query strategy and whether a system-table surface can replace high-volume per-object API calls.
- Rate-limit responses, API outages, token/permission failures and system-table lag remain integration-health evidence, not monitored-domain negatives.

## GitHub API, audit and Actions economics

- [GitHub REST API rate limits](https://docs.github.com/en/enterprise-cloud@latest/rest/using-the-rest-api/rate-limits-for-the-rest-api) currently documents **5,000 requests/hour** for typical authenticated user/token access and **15,000 requests/hour** for qualifying GitHub Apps/OAuth apps owned by an Enterprise Cloud organization. Exact authentication mode matters.
- The enterprise audit-log API currently has a dedicated limit of **1,750 queries/hour per user and IP**. GitHub also documents secondary limits, including concurrency/point/content-generation constraints that can produce 403/429 responses even when the primary hourly budget remains.
- Phase 009 therefore requires integration-health telemetry for GitHub rate-limit state and does not treat API non-return during throttling as absence.
- Current GitHub Enterprise Cloud audit-history documentation retained by Group 07 remains material: ordinary enterprise audit events are available for roughly **180 days**, and Git events for **seven days**, unless exported/streamed externally.
- [Product usage included with each plan](https://docs.github.com/en/enterprise-cloud@latest/billing/reference/product-usage-included) currently lists **50,000 GitHub Actions minutes/month and 50 GB Actions storage** for GitHub Enterprise Cloud, with plan-dependent allowances elsewhere.
- [GitHub Actions billing](https://docs.github.com/en/billing/concepts/product-billing/github-actions) documents metered usage above included quotas for private repositories, storage accounting and runner-dependent costs. Group 08 records this only as a future architecture/control cost surface; it does **not** select GitHub Actions as the Phase 010 ingestion or Gate implementation.

## Collibra throttling and licensing/capacity

- [Collibra Data Governance Center service configuration](https://productresources.collibra.com/docs/collibra/latest/Content/Console/Infrastructure/DGCService/Configuration/ref_environment-settings.htm) documents configurable REST v1, REST v2 and GraphQL throttling. Current documentation describes a default throttle logic threshold of **100 API requests/second**, while actual tenant throttling settings are administrative/environment-specific.
- [OAuth Applications settings](https://productresources.collibra.com/docs/collibra/latest/Content/Settings/OAuth/co_oauth-settings.htm) currently documents a token pool of **5 tokens per client**, replenished at **1 token/minute**, with issued tokens valid for **5 minutes**. Applications should reuse valid tokens rather than repeatedly requesting new ones.
- Current Collibra licensing is also capacity-sensitive. Product documentation exposes plan/license-specific asset entitlements and behavior when entitled asset capacity is exceeded. Exact commercial price, licensed products and tenant limits remain contract-specific.
- Collibra is therefore a conditional/optional source whose API/token/license envelope must be discovered for the target enterprise. No framework semantic requirement is weakened when Collibra is absent.

## Immuta operational constraints

- Current Immuta SaaS API documentation exposes multiple APIs and integration-specific authorization requirements, but Group 08 did **not** identify a stable public generic request-rate or pricing contract appropriate to apply across all Immuta APIs/deployments.
- Group 07's verified audit-retention result remains material: current SaaS guidance describes roughly **90 days** of native audit retention for relevant Immuta audit surfaces, with UAM export recommended/available for longer-lived analysis.
- Integration mode, registered population, deployed version, regional/global API endpoint, audit export configuration and commercial licensing all affect usable capability.
- Exact Immuta API limits, export capacity and pricing therefore remain `unknown / not yet verified` until environment/contract discovery. Group 08 explicitly rejects inventing generic rate/cost assumptions.

## Cost and quota interpretation

Group 08 distinguishes:

- **source availability cost** — whether the platform/edition/source is licensed and accessible;
- **query/API cost** — compute/API/query work needed to retrieve evidence;
- **retention cost** — any product-owned/external storage required beyond native history;
- **processing cost** — correlation, reconciliation, metric or replay computation;
- **control execution cost** — future Gate/Safeguard workflow execution where selected;
- **disclosure/communication retention cost** — preserving authentic Explanation snapshots and basis provenance where required.

A cheaper source does not gain authority. A more expensive source does not gain truth. Quota or cost pressure may force a different feasible collection/retention strategy, but Phase 010 must preserve all accepted evidence, negative-coverage and authorization semantics.

## Environment-specific unknowns retained at Phase 009 exit

- Databricks cloud/region/edition, enabled system tables, compute SKU, source volumes, actual system-table lag and any retention extension/materialization;
- exact Databricks API endpoint mix and rate-limit behavior for the target workspaces/accounts;
- GitHub plan, authentication model, Apps, audit streaming, Actions use, workflow volume and retained external audit history;
- Collibra edition/license, asset entitlement, API throttling configuration, OAuth clients and enabled history settings;
- Immuta deployment/version/license, API limits, audit population/coverage/export and retention contract;
- target long-horizon retention period for provenance, source state, authorization and Explanation communication;
- target SLOs for current monitoring versus investigative/retrospective Explanation;
- actual data/query volumes that will determine cost/throughput architecture;
- organization-owned identity crosswalk, Monitoring Scope, Assertion Authority, correlation/attestation, consequence evidence and communication-retention requirements.

These unknowns are Phase 010/environment-discovery inputs. They are not reasons to reopen the accepted functional model.
