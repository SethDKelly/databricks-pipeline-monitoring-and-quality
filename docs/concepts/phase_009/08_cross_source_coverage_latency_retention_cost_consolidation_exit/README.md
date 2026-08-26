# Phase 009 Group 08 — Cross-Source Coverage, Latency, Retention, Cost & Consolidation / Exit Review

**Status:** Review complete — accepted; Phase 009 complete

## Result

Group 08 accepts **INTG-239–INTG-270** and **XRC08-01–XRC08-64**. The Phase 009 exit review passes.

No new product concept is required. Final Phase 009 range is **INTG-001–INTG-270**; **no INTG-271** is required; the accepted concept catalog remains 24.

The consolidated feasibility chain is:

**accepted proposition + exact source-set/context → source support classification → identity/join reliability → authority applicability → T/K/clock quality → coverage/negative capability → availability/latency → retention/replay/communication durability → disclosure/basis inspectability → quota/cost → integration observability → explicit residual gap → Phase 010 architecture obligation**.

No stage changes proposition truth or weakens an accepted evidence burden.

## Accepted contracts

1. **INTG-239** — Consolidated Feasibility Classification
2. **INTG-240** — Source-Family Responsibility Composition
3. **INTG-241** — Cross-System Identity & Join Feasibility
4. **INTG-242** — Governance & Authority Coverage
5. **INTG-243** — Change / Deployment / Run Correlation Feasibility
6. **INTG-244** — Run Implementation-Version Coverage
7. **INTG-245** — Input / Output Version Coverage
8. **INTG-246** — Health & Measurement Source Coverage
9. **INTG-247** — Lineage / Encounter / Impact Coverage
10. **INTG-248** — Investigation & Causal Coverage
11. **INTG-249** — Safeguard / Gate / Control Coverage
12. **INTG-250** — Explanation / Replay / Basis Coverage
13. **INTG-251** — Common Derivation & Conflict Composition
14. **INTG-252** — Temporal Ordering & Clock Quality
15. **INTG-253** — Latency Envelope Classification
16. **INTG-254** — Strong-Negative Coverage Feasibility
17. **INTG-255** — Integration-Health Observability Requirement
18. **INTG-256** — Retention-Horizon Composition
19. **INTG-257** — Long-Horizon Provenance Durability Requirement
20. **INTG-258** — Availability-by-K Durability Requirement
21. **INTG-259** — Retained Explanation Communication Requirement
22. **INTG-260** — Historical Authorization Durability Requirement
23. **INTG-261** — Basis Disclosure Durability & Sensitivity
24. **INTG-262** — Databricks System-Table Economics
25. **INTG-263** — Databricks API & Lineage Quota Envelope
26. **INTG-264** — GitHub API Quota Envelope
27. **INTG-265** — GitHub Actions Usage-Cost Boundary
28. **INTG-266** — Collibra Throttling, License & Capacity Boundary
29. **INTG-267** — Immuta Operational Cost / Quota Boundary
30. **INTG-268** — Optional-Integration Degradation Contract
31. **INTG-269** — MVP Source-Sufficiency Boundary
32. **INTG-270** — Phase 010 Handoff & Phase 009 Exit

## Consolidated feasibility conclusion

Phase 009 finds that the accepted framework is **technically feasible to architect without weakening its functional semantics**.

The evaluated source set does not natively satisfy every enterprise proposition. That is an expected and useful result. The source model is strong enough to begin Phase 010 because unsupported, partial and environment-specific requirements are now explicit rather than hidden.

A bounded MVP can center on:

- Databricks / Unity Catalog / Lakeflow Jobs / system tables and relevant measurement sources;
- Git/GitHub and GitHub Actions/deployment/review evidence;
- deliberate organization-owned Monitoring Scope, Assertion Authority, identity and correlation records where the corresponding propositions require them.

Collibra and Immuta remain **optional source families**, not universal MVP dependencies. Their absence narrows specific governance/control/history capabilities and must be reported as such; it never authorizes benign defaults.

## Cross-source support shape

The consolidated matrix intentionally has four recurring result classes rather than one score:

### Strong/native support

Examples include source-local Git revision identity, GitHub workflow/run/attempt identity, many Databricks object/job/run/audit facts, qualifying direct-Git `used_commit`, executed DQ/expectation observations, selected metric/profile/anomaly source results, and qualifying lineage/query encounters.

### Conditional/composed support

Examples include effective authorization across planes, semantic/governance authority, CI→Databricks association, composite implementation state, output version binding, run-specific health, exact consumer exposure, causal support, Safeguard prevention, Gate enforcement and current historical-basis inspection.

### Unsupported out of box

Examples include a universal Monitoring Scope registry, full Assertion Authority registry, generic bundle/workspace-source run commit, generic exact multi-input consumed-version manifest, universal Propagation Safeguard, native proof of business consequence, a universal immutable Explanation archive and generic exact prior `inspectBasis` projection.

### Environment-specific / unknown until discovery

Examples include actual IAM topology, optional Collibra/Immuta deployment and entitlements, API/tenant limits not guaranteed by public documentation, external BI/application use evidence, business consequence sources, long-horizon exports/materializations and organization-specific causal/control authority.

No result is converted into a confidence or completeness percentage.

## Identity and join exit

Identity remains one of the most important architecture requirements.

Source-local identifiers are useful and often strong, but exact cross-system reasoning still requires governed joins for:

- UC object ↔ Collibra/Immuta/governance identities;
- Git revision/change record ↔ deployment ↔ target activation ↔ run;
- run ↔ output/input version;
- consumer/path ↔ actual encounter/state;
- source evidence ↔ durable Explanation basis.

Name equality and timestamp proximity remain rejected as exact join semantics.

## Coverage and negative-evidence exit

Strong negative claims remain deliberately expensive. Group 08 preserves the exact burden for propositions such as:

- no deployment / activation / run / output / consumption;
- no dependency / no encounter / not exposed;
- no downstream effect / no consequence;
- no control enforcement / no prevention;
- no governance assignment / no authorization.

These require bounded opportunity/population/path/window, sufficient source/query coverage and known source health. API throttling, permissions, lag, retention expiry, incomplete lineage, partial pagination, optional-source absence and missing instrumentation invalidate broad negative inference rather than producing a reassuring result.

## Latency and current-monitoring exit

There is no one source-latency contract.

Databricks system-table documentation explicitly describes delayed/non-real-time publication for material sources. API and runtime surfaces can be more immediate but have different quota/coverage semantics. GitHub, Collibra and Immuta expose their own API/audit/history timing characteristics.

Phase 010 should therefore define **use-specific service classes**—for example near-current operational monitoring versus slower investigative/historical Explanation—rather than one universal freshness target for every evidence source.

Latency affects when evidence can enter knowledge cut `K`; it does not change event/effective truth.

## Retention and replay exit

The source ecosystem has no universal indefinite ledger.

Current verified facts include:

- many material Databricks system tables: roughly **365-day** free retention;
- GitHub Enterprise Cloud ordinary audit history: roughly **180 days**;
- GitHub Git audit events: roughly **7 days** without external retention;
- Immuta SaaS relevant audit history: roughly **90 days** by default, with export for longer horizons;
- Collibra history: rich for many facets but permission/configuration dependent and suppressible for selected attributes.

Phase 010 therefore needs an explicit decision about which provenance/source/authorization/communication artifacts must survive longer than native vendor history.

Planned retention remains a future architecture capability and is not counted as current source support in the Phase 009 matrix.

## Explanation and communication exit

Group 08 preserves Group 07's four-view distinction:

1. historical source state;
2. as-known-at-cut Explanation;
3. actual retained communication;
4. current retrospective Explanation.

Current authorized projection remains separate.

A platform may be excellent for retrospective reconstruction while still being unable to prove what was actually communicated. Delivery records do not prove exact wording. Stable citations can outlive retrievable basis. Current source access cannot prove an earlier `inspectBasis` projection.

These are architecture requirements, not reasons to collapse historical views.

## Quota and cost exit

Quota/cost is modeled as operational feasibility, never evidence authority.

Current external review records:

- Databricks system tables are currently free to use, with compute charged for queries;
- Databricks REST limits vary by endpoint/scope, with explicit lineage hourly/daily limits;
- GitHub authenticated/audit/secondary API limits constrain collection frequency;
- GitHub Actions has plan-dependent minutes/storage and metered overage if later used for collection/control workflows;
- Collibra exposes configurable API throttling, OAuth token issuance constraints and license/capacity considerations;
- Immuta exact generic API limits/pricing are environment/contract specific where a stable universal public value was not verified.

Phase 010 must make quota/cost observable and choose efficient collection/retention mechanisms without changing evidence burden.

## Integration-health exit

Integration health is mandatory for enterprise trustworthiness.

The architecture must distinguish at least:

- authenticated/authorized success;
- source permission denial;
- authentication failure;
- throttling/rate exhaustion;
- timeout/outage;
- delayed publication;
- partial pagination;
- schema/API drift;
- parser/transformation failure;
- retention expiry;
- optional integration not installed/enabled.

None of those states may be translated into product-level absence.

## Residual gaps

[`residual_gap_register.md`](residual_gap_register.md) records **40 accepted residual gaps** covering source authority, identity/correlation, runtime provenance, health/current-cycle evidence, consumer/Impact evidence, causal/control realization, historical/Explanation durability, disclosure, integration health, quotas/cost and environment discovery.

The gaps are Phase 010 inputs. They are not reopened semantic questions.

## Scenario consolidation

[`scenario_replay_matrix.md`](scenario_replay_matrix.md) passes **XRC08-01–XRC08-64**, including cross-source identity, deployment joins, direct-Git versus bundle provenance, multi-input gaps, health conflicts, consumer/version exposure, causality, Safeguard/Gate enforcement, T/K replay, retention expiry, communication retention, authorization, rate limiting, cost and optional-source MVP degradation.

## Phase 009 exit

[`phase_009_exit_review.md`](phase_009_exit_review.md) confirms:

- **INTG-001–INTG-270 final**;
- all eight Phase 009 scenario suites pass;
- no new concept is required;
- no INTG-271 is required;
- no universal vendor/support/confidence/health/Impact/control/replay score is created;
- unsupported and unknown capabilities remain explicit;
- no technical architecture has been selected;
- Phase 010 may begin from stable source capability facts.

## Phase 010 handoff

[`phase_010_handoff.md`](phase_010_handoff.md) records the technical problem set Phase 010 must solve without prescribing a storage, graph, streaming, service, LLM, control or deployment architecture.

**Phase 009 is COMPLETE. Phase 010 — Technical Architecture is next.**
