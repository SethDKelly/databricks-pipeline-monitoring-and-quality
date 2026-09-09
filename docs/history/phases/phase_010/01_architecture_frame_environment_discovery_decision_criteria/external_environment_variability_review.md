# Phase 010 Group 01 — External Environment Variability Review

**Verified:** 2026-08-26

## Purpose

This review verifies the architecture premise that vendor-documented capabilities are not automatically available or usable in every enterprise deployment. It records public documentation as **vendor/public facts only**. No statement below is a fact about a particular customer environment until environment discovery verifies it.

## Databricks

Current Databricks documentation directly confirms deployment variability:

- Databricks runs across AWS, Azure and GCP and publishes cloud-specific supported-region documentation.
- Databricks' AWS and GCP region pages explicitly state that some features are available only in a subset of regions.
- The current limited-regional-availability matrices enumerate differences for serverless compute, Apps, default storage, Data Quality Monitoring, AI Search, predictive optimization and other capabilities.
- Databricks documents that only a subset of system tables is available in AWS GovCloud.
- System-table coverage can be regional or global by table; workspace-level data is commonly regional while selected account-level tables are global.
- Databricks previews can be enabled at account or workspace scope, and preview availability/default state varies by release type.
- Databricks Designated Services use Geos; some services are not natively available in every Geo and can require cross-Geo processing enablement.

Architecture implication: `Databricks documentation describes feature X` is not enough. Discovery must bind at least cloud, region/Geo, account/workspace/metastore scope, feature/release status, enablement, permissions and the exact source surface needed.

## GitHub

Current GitHub documentation also confirms deployment and plan variability:

- GitHub environment/deployment-protection capabilities vary by repository visibility and plan.
- GitHub Enterprise Cloud with data residency (GHE.com) documents feature differences from GitHub.com; some preview features can be unavailable until GA and selected audit-streaming options are unavailable.
- GitHub Enterprise Server capability depends on deployed GHES version and support lifecycle; documentation is versioned accordingly.
- Enterprise Managed Users and enterprise deployment choices can change available user/repository capabilities and audit semantics.

Architecture implication: GitHub.com documentation, a current GitHub Enterprise Cloud feature, and a particular GHES/GHE.com deployment are not interchangeable capability facts.

## Collibra

Current Collibra documentation publishes explicit environment/deployment differences:

- The feature-availability comparison distinguishes commercial cloud, AWS UAE, Collibra Platform for Government and older/self-hosted offerings.
- Some features are unavailable in Government or self-hosted deployments, while others require explicit enablement.
- Collibra Cloud Edge sites support fewer connections/capabilities than customer-managed Edge sites and some data sources are unavailable.
- Release calendars differ between commercial, government and self-hosted offerings.

Architecture implication: Collibra availability must bind deployment offering, version, enabled capabilities, Edge/site model, licensing and exact connection/capability configuration.

## Immuta

Phase 009 found that exact Immuta API, licensing, audit-export and deployment constraints are environment/contract specific and that no universal public limit/package should be assumed. Group 01 therefore keeps Immuta capability details `unknown / environment discovery required` until the target deployment and contract are known.

Architecture implication: absence of a verified universal public matrix is itself a reason to require deployment discovery, not a reason to assume equivalence across Immuta deployments.

## Accepted cross-vendor rule

For every vendor and source surface:

**documented possibility ≠ deployment presence ≠ licensed entitlement ≠ enabled/configured state ≠ principal authorization ≠ network/API reachability ≠ observable coverage ≠ proposition-specific usability**.

A later architecture group may rely on a capability only to the extent that the relevant dimensions have been verified for the target environment or are explicitly carried as assumptions/unknowns with a safe degraded path.

## Public sources reviewed

- Databricks: `Databricks clouds and regions` (AWS/GCP), current 2026 regional-support pages.
- Databricks: `Features with limited regional availability` (AWS/GCP), updated 2026-08-20.
- Databricks: `System tables reference`, including AWS GovCloud and regional/global scope notes.
- Databricks: `Manage Databricks previews`, updated 2026-07-24.
- Databricks: `Databricks Designated Services`, updated 2026-08-18.
- GitHub: Enterprise Cloud data-residency feature overview; versioned GitHub Enterprise Server environment/deployment documentation.
- Collibra: `Feature availability comparison`, current 2026 release documentation; Edge/Cloud-site deployment documentation.

These references constrain architecture assumptions but do not replace target-environment discovery.
