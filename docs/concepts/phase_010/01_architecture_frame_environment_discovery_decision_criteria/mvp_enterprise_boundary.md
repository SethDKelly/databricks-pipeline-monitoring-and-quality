# Phase 010 Group 01 — MVP / Enterprise Extension Boundary

## Purpose

Constrain later architecture without pretending every enterprise deployment exposes the same vendor capabilities.

The boundary is capability/proposition based. A deployment can move a capability between `supported`, `conditional`, and `unavailable` depending on verified environment facts without changing the product semantics.

## Bounded MVP posture

The accepted Phase 009 conclusion remains: a serious **Databricks + GitHub-centered passive monitoring/RCA MVP is feasible**.

The bounded MVP architecture must be able to support, for the source modes and propositions it claims:

- deployment-specific capability discovery and integration-health state;
- organization-owned Monitoring Scope and Assertion Authority where required;
- durable cross-system Entity Identity/correlation needed by supported joins;
- Git/Change Intent/deployment/run association for supported deployment paths;
- run/task/update/output operational provenance;
- run/output-bound health/measurement evidence for promised health questions;
- bounded lineage/topology and consumer evidence that available Databricks surfaces actually support;
- Investigation/lead/Causal Claim persistence without automatic causal confirmation;
- statement-to-basis evidence traceability;
- least-privilege/disclosure-aware access to evidence/basis;
- partial/graceful operation when optional sources or enrichments are unavailable;
- explicit unsupported/unknown results rather than benign defaults.

Passive monitoring remains non-blocking/out-of-band by default.

## Conditional MVP capabilities

These are required only when the MVP explicitly promises the dependent proposition or uses the relevant source mode:

- exact run Git revision for deployment modes without native run commit evidence;
- composite implementation state beyond code revision;
- exact multi-input consumed versions/current-cycle proof;
- consumer-specific compatibility contracts;
- event-time freshness/watermark semantics;
- causal `confirmed` status, which requires explicit confirmation authority/workflow;
- exact historical/as-known replay beyond native retention;
- retained actual Explanation communication;
- prior `inspectBasis` projection history.

If these are not implemented, the dependent question is capability-limited rather than approximated by weaker evidence.

## Enterprise extensions

The following are not universal prerequisites for the bounded passive MVP and can be layered as explicit enterprise capabilities:

- Collibra enrichment/governance integration;
- Immuta policy/enforcement enrichment;
- broad external BI/report/application view/use telemetry;
- business/customer/financial consequence integrations;
- strong multi-hop global non-exposure/no-effect/no-consequence coverage;
- long-horizon product-owned evidence retention beyond the chosen MVP commitment;
- authentic long-horizon communication/projection audit;
- Execution Gate active control;
- Propagation Safeguard active control and REF-028 prevention evidence;
- organization-specific multi-Gate/fallback/override active-control workflows.

Enterprise extension does not mean semantically weaker. Once enabled, the same evidence/authority/control contracts apply.

## Optional vendor rule

Collibra and Immuta are optional vendor integrations, but the organization-owned semantics they might help realize are not optional merely because the vendor is absent.

For example, if the product promises Assertion Authority, the architecture needs an authority source even in a deployment with no Collibra. If it promises protected-path enforcement, the architecture needs a concrete Safeguard realization even in a deployment with no Immuta.

## Reference architecture rule

Phase 010 should produce a reference architecture that states capability prerequisites and degraded modes. It must not publish one monolithic feature list that assumes every enterprise deployment has identical Databricks/GitHub/Collibra/Immuta capabilities.
