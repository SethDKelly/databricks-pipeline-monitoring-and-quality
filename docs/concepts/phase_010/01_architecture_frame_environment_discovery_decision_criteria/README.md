# Phase 010 Group 01 — Architecture Frame, Environment Discovery & Decision Criteria

**Status:** COMPLETE / ACCEPTED

## Goal

Establish the architecture decision frame and target-environment discovery contract before selecting major technologies.

Group 01 answers **what the architecture must optimize for, what environment facts must be discovered, what assumptions may be made, how alternatives will be evaluated, and what remains intentionally undecided**.

## Accepted result

Accepted architecture range: **ARCH-001–ARCH-032**.

Scenario suite: **AFE01-01–AFE01-60 pass**.

Decision range: **D-1269–D-1298 accepted**.

No final persistence, graph, event-bus/queue, orchestration, LLM/retrieval, policy/control, service or deployment technology is selected by this group.

## Central architecture chain

**public/vendor capability statement → deployment-bound capability instance → provenance-bearing environment verification → dimensioned capability facts + unknowns → proposition/service-class usability → architecture hard constraints + decision-specific tradeoffs → MVP/enterprise/gap ownership → later technology ADR**.

No link automatically creates the next.

In particular:

**documented capability ≠ deployment presence ≠ licensed entitlement ≠ enablement ≠ authorization ≠ reachability ≠ observable coverage ≠ proposition-specific usability**.

## Environment variability is a first-class rule

Current vendor documentation confirms that capability differs materially across enterprise deployment contexts:

- Databricks documents cloud/region-limited features, AWS GovCloud system-table differences, account/workspace preview enablement and Geo/cross-Geo requirements for selected services.
- GitHub capabilities vary across GitHub.com, GHE.com, GHES versions, repository visibility and plans.
- Collibra publishes different feature availability across commercial cloud, UAE, Government and self-hosted/deployment/site models.
- Phase 009 already requires Immuta API/licensing/export limits to be discovered for the target deployment rather than assumed universally.

Therefore the reference architecture cannot use a static vendor-wide capability Boolean.

## ARCH-001–ARCH-032 summary

### Fact and capability model — ARCH-001–ARCH-015

Group 01 establishes:

- explicit architecture fact classes;
- deployment-bound capability instance identity;
- documented capability vs target-environment fact separation;
- multidimensional capability state;
- provenance-bearing verification;
- unknown preservation;
- capability fact freshness/history;
- cloud/region/Geo, plan/license/version, preview/enablement, permission/reachability and residency bindings;
- proposition-specific usability;
- optional-source graceful degradation.

The architecture may never say merely `Databricks supports X` where the decision requires proof that X is usable in a particular enterprise environment.

### Scope and architecture quality — ARCH-016–ARCH-021

Group 01 establishes:

- explicit MVP/enterprise/optional/conditional capability classes;
- organization-owned core capabilities where dependent propositions are promised;
- hard constraints for semantic/evidence/security/degraded-state correctness;
- decision-specific quality-attribute tradeoffs;
- no universal architecture score;
- explicit decision reversibility.

A simpler/faster/cheaper option cannot win by violating an accepted semantic boundary.

### Service classes — ARCH-022–ARCH-023

Six use classes are accepted:

1. SC-01 near-current operational facts;
2. SC-02 periodic core health/quality;
3. SC-03 enriched Investigation/RCA;
4. SC-04 historical/as-known replay;
5. SC-05 retained communication/basis inspection;
6. SC-06 active control.

They constrain completeness/latency/retention needs without inventing one universal freshness SLA. Numeric targets remain later environment-informed ADR work.

### Decision discipline — ARCH-024–ARCH-032

Group 01 establishes:

- assumption/unknown register;
- evidence/alternative requirements for material ADRs;
- supersession/rollback history;
- explicit ownership/treatment for GAP-009-01–GAP-009-40;
- cross-group entry preconditions;
- cost/quota/retention fact binding;
- architecture failure semantics;
- security/disclosure nonfunctional constraints;
- Group 02 entry readiness.

## Target-environment discovery profile

The accepted discovery profile records at least:

- vendor/product and deployment model;
- cloud/hosting and region/Geo;
- account/tenant/workspace/metastore/org/repository scope;
- edition/plan/license/version/release state;
- exact source surface/feature;
- documented support;
- deployment presence;
- enablement/configuration;
- entitlement;
- authorization;
- reachability;
- observable coverage;
- retention/time semantics;
- quota/capacity and cost facts;
- integration health;
- provenance and verification time;
- optional/MVP/enterprise role.

The result is evaluated for an exact proposition/service class rather than flattened into one global status.

See [`environment_capability_profile.md`](environment_capability_profile.md).

## MVP / enterprise boundary

A bounded Databricks/GitHub-centered **passive monitoring/RCA** MVP remains feasible, but capability claims are conditioned on deployment discovery.

MVP-core architecture concerns include capability discovery, integration health, Monitoring Scope/Assertion Authority where required, durable identity/correlation, supported run/output/health provenance, Investigation persistence, evidence/basis traceability and secure graceful degradation.

Optional Collibra/Immuta integrations enrich exact capabilities without becoming universal prerequisites.

External BI/application-use evidence, business consequence integrations, broad multi-hop negative coverage and active Gate/Safeguard control are explicit enterprise extensions unless a deployment intentionally pulls them into its MVP.

Exact input-version attestation, long-horizon replay, authentic Explanation retention and historical inspectBasis are product-commitment dependent: if promised, architecture must support them; if not, the limitation remains explicit.

See [`mvp_enterprise_boundary.md`](mvp_enterprise_boundary.md).

## Quality-attribute frame

Hard constraints are evaluated before optimization. Material later ADRs then compare applicable durability, availability, latency, scalability, operational simplicity, observability/testability, reversibility, quota efficiency, cost, portability, performance and maintainability.

No weighted sum or universal architecture score is accepted.

See [`architecture_quality_attributes.md`](architecture_quality_attributes.md).

## Gap ownership

Every GAP-009-01–GAP-009-40 item now has a primary Phase 010 owner, priority and treatment path. Later groups may share implementation responsibility but may not let assigned gaps disappear without explicit exit treatment.

See [`gap_ownership_matrix.md`](gap_ownership_matrix.md).

## Scenario result

AFE01-01–AFE01-60 pass across region/cloud/deployment/version/plan/license/preview/permission/reachability variability, optional-source degradation, source failure, proposition-specific usability, MVP scoping, service classes, hard constraints, ADR quality, gap ownership and Group 02 readiness.

See [`scenario_review.md`](scenario_review.md).

## External review

The current external review was verified on 2026-08-26 and is intentionally recorded as public/vendor evidence rather than target-environment fact.

See [`external_environment_variability_review.md`](external_environment_variability_review.md).

## Acceptance gate result

Group 01 passes because:

- later groups now have an explicit decision rubric;
- target-environment facts are separated from public defaults, requirements, assumptions and unknowns;
- enterprise deployment variability is modeled at capability-instance/dimension level;
- every GAP-009 item has ownership/priority/treatment;
- MVP vs enterprise-extension scope is explicit enough to constrain design;
- service classes prevent a universal latency/retention target;
- hard failure/degradation/security/history constraints are explicit;
- AFE01-01–AFE01-60 pass;
- no major technology was selected by convention.

## Group 02 handoff

**Phase 010 Group 02 — Evidence, Provenance, Temporal & Persistence Architecture is next.**

Group 02 must consume ARCH-001–ARCH-032, especially the fact/capability model, hard constraints, SC-01–SC-06, ADR rubric, MVP/enterprise boundary and gap ownership. It may select concrete persistence architecture only by tracing alternatives to these inputs and must not assume a source capability merely because public vendor documentation describes it.
