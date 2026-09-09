# Phase 009 Exit Review — Integration Contracts, Source Authority & Evidence Availability

**Status:** Accepted — Phase 009 complete

## Exit result

Phase 009 exits successfully with:

- **INTG-001–INTG-270 final**;
- Group 01 **IC01-01–IC01-40 PASS**;
- Group 02 **GOV02-01–GOV02-48 PASS**;
- Group 03 **RTE03-01–RTE03-54 PASS**;
- Group 04 **HME04-01–HME04-56 PASS**;
- Group 05 **LIE05-01–LIE05-60 PASS**;
- Group 06 **ICE06-01–ICE06-72 PASS**;
- Group 07 **EBR07-01–EBR07-64 PASS**;
- Group 08 **XRC08-01–XRC08-64 PASS**;
- accepted concept catalog remains **24**;
- **no INTG-271 is required**;
- Phase 010 — **Technical Architecture** may begin without reopening the accepted functional semantics.

## What Phase 009 establishes

Phase 009 proves that the completed functional model can be mapped to real source systems without making any one vendor the truth model. The accepted integration chain remains:

**exact source surface/version → bounded accepted proposition → evidence role → authority applicability → identity/join contract → temporal coordinates → grain/context → positive/negative capability + coverage → availability/latency → retention/replay → correction/mutation → disclosure → derivation/conflict → quota/cost → integration observability → proposition-specific support classification + residual gaps**.

No stage strengthens truth automatically.

## Feasibility conclusion

The evaluated source families are sufficient to begin technical architecture for a serious enterprise monitoring/data-quality framework.

A bounded MVP can be designed around:

- Databricks / Unity Catalog / Lakeflow Jobs / system tables and relevant measurement surfaces;
- Git/GitHub and GitHub Actions/deployment evidence;
- explicit organization-owned Monitoring Scope, Assertion Authority and cross-system correlation/identity records where the corresponding propositions require them;
- optional DQX/metric/health source surfaces as available and governed.

Collibra and Immuta are **not universal MVP dependencies**. When absent, the exact semantic/governance/control/history capabilities they would contribute remain partial/unsupported/unknown rather than being replaced with benign defaults.

The MVP conclusion is not a universal completeness claim. Several advanced enterprise capabilities require explicit Phase 010 durability/instrumentation or additional organization-specific sources.

## Major source strengths

### Databricks

Strong evaluated support exists for many platform-local object/principal facts, job/run/task history, current/system metadata, direct-Git run commit evidence where `used_commit` is exposed, DQ/expectation/metric/profile/anomaly observations, audit events, lineage/query encounters, billing/usage data and several historical system-table surfaces.

Its main limits are proposition-specific: system tables are not a real-time universal ledger; retention is surface-specific; query/API/region/permission coverage matters; exact bundle run commit and generic exact multi-input consumption are not universally available; lineage is incomplete; current metadata is not historical state; and vendor health/RCA/impact labels retain their narrower meanings.

### GitHub

Strong evaluated support exists for repository revisions, workflow/run/attempt identity, deployment/review records, environment protection/Gate evidence for the protected GitHub job, issues/comments/review context and audit history within the applicable plan/retention/API envelope.

GitHub does not prove Databricks activation/run without explicit correlation, does not provide data-governance Assertion Authority by role/title, and does not constitute an immutable long-horizon Explanation archive by default.

### Collibra

Collibra can be a strong optional source for governed semantics, responsibilities, classifications and historical resource changes where the exact facet is authoritative and history is enabled. Its identifiers remain source-local; visibility/history is permission/configuration bound; throttling/token/license/capacity is environment-specific.

### Immuta

Immuta can be a strong optional source for Immuta-managed authorization/policy and query-time enforcement within its registered/instrumented population. Its audit can materially support control and basis inspection, while native retention/integration/population coverage and exact operational limits remain deployment-specific.

## Major unsupported or conditional requirements retained

Phase 009 deliberately exits with explicit gaps rather than semantic compromises. The most important are:

- no out-of-box DMTZ Monitoring Scope registry;
- no out-of-box Assertion Authority registry;
- durable cross-system Entity Identity/correlation requirements;
- generic GitHub→Databricks deployment/run correlation where native evidence is absent;
- exact bundle/workspace-source run revision without attestation;
- complete composite run-specific implementation state without multiple source facets;
- generic exact multi-input consumed-version manifests;
- consumer-specific compatibility contracts;
- event-time freshness where only commit/system freshness is available;
- exact measurement→run/output and consumer→affected-version binding in all cases;
- complete lineage/consumer/application/business-consequence evidence;
- broad strong-negative coverage across all material paths/populations;
- automatic Causal Claim confirmation;
- universal Propagation Safeguard coverage;
- authentic prior Explanation retention and exact historical `inspectBasis` presentation;
- indefinite source/provenance/authorization replay under vendor-native retention alone;
- target-specific API/quota/license/cost parameters until environment discovery.

See [`residual_gap_register.md`](residual_gap_register.md) for the full accepted register.

## Time, replay and communication conclusion

Phase 009 confirms that enterprise historical reasoning requires several distinct capabilities:

1. retained historical source state;
2. evidence of when source facts became available/knowable;
3. authentic retained communication where actual historical wording/context matters;
4. current retrospective re-evaluation;
5. current authorized projection of whichever historical/current view is requested.

No vendor-native history should be assumed to satisfy all five indefinitely. Phase 010 must decide which provenance/source state/authorization/communication artifacts require product-owned or externally retained durability, but those future mechanisms are not counted as current source capability.

## Negative-evidence conclusion

Strong negatives remain one of the most demanding enterprise capabilities. `No run`, `no output`, `no dependency`, `not exposed`, `no effect`, `no consequence`, `not enforced`, `no control action` and similar propositions require their exact opportunity/population/path/window and sufficient source/query coverage with source health known.

Rate limiting, retention expiry, permission filtering, system-table lag, incomplete lineage, partial pagination, parser/schema failure, optional-source absence or missing instrumentation cannot become negative truth.

## Cost, quota and operational feasibility conclusion

Phase 009 records cost and quota only as architecture constraints:

- Databricks system tables are currently free to use while compute used to query them is charged; endpoint-specific REST/lineage limits apply.
- GitHub has authentication/endpoint/secondary API limits, plan-dependent Actions usage/storage economics and audit-retention/export considerations.
- Collibra exposes configurable API throttling, OAuth token issuance behavior and license/capacity constraints whose target settings must be discovered.
- Immuta licensing/API/export capacity and exact rate/pricing limits remain environment/contract specific where no stable universal public value was verified.

Cost or quota pressure can influence collection, retention and query architecture. It cannot reduce evidence burden or grant authority.

## Graceful degradation conclusion

The product can legitimately operate with partial source capability if it communicates the limitation faithfully. Graceful degradation means:

- preserve supported sibling statements;
- mark unsupported/unknown/expired/restricted basis explicitly;
- avoid broad negatives when coverage is degraded;
- avoid source-precedence fallbacks that inherit authority;
- avoid converting absent optional governance/control products into benign truth;
- preserve the distinction between current monitoring, slower investigation and historical replay capability.

## Phase 010 architecture obligations

Phase 010 receives a concrete fact set, not an architecture prescription. It must determine how to realize, at minimum:

- source discovery and capability configuration;
- durable Entity Identity/cross-system joins;
- Monitoring Scope and Assertion Authority records;
- GitHub→Databricks correlation/attestation;
- exact run implementation/input/output provenance where required;
- source ingestion/query strategy under latency/quota/cost constraints;
- integration-health observability;
- long-horizon provenance/source/authorization retention where required;
- authentic Explanation communication retention where required;
- basis identity/inspection/disclosure controls;
- graceful degradation and partial answers;
- optional Collibra/Immuta integration boundaries;
- cost attribution and operational SLOs.

It may choose storage, graph, streaming/polling, services, SDKs, credentials, control implementations, UI and deployment topology. It may **not** weaken the accepted proposition/authority/time/coverage/causal/control/Explanation semantics to simplify those choices.

## Exit gate

The Phase 009 exit gate passes because:

- every integration group is accepted;
- all scenario suites pass;
- current external source behavior was verified where Group 02–08 required it;
- support/partial/unsupported/unknown outcomes are explicit;
- residual gaps are concrete enough to drive architecture;
- no new truth/health/confidence/Impact/control/Explanation score was introduced;
- no functional concept had to be added;
- no architecture was prematurely selected;
- Phase 010 can begin from stable integration facts.

**Final Phase 009 range: INTG-001–INTG-270. Phase 009 COMPLETE. Phase 010 — Technical Architecture is next.**
