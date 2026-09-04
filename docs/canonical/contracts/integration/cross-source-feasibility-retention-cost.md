# Cross-Source Coverage, Latency, Retention, Cost & Consolidated Feasibility

**Canonical key:** `integration.group-08`

**Kind:** INTEGRATION CONTRACT

**Authority:** CANONICAL CURRENT AUTHORITY

**Migration record:** `stable_family.INTG`

**Stable IDs:** INTG-239–INTG-270

**Owns current question:** Across all evaluated source families, which accepted propositions are natively supported, conditionally composable, unsupported out of box or environment-specific, and what residual architecture obligations follow?

## Canonical feasibility conclusion

The accepted framework is technically feasible to architect without weakening its semantics, but the evaluated source set does not natively satisfy every enterprise proposition.

Recurring feasibility classes remain:

- strong/native support;
- conditional/composed support;
- unsupported out of box;
- environment-specific / unknown until discovery.

A bounded Databricks/GitHub-centered MVP is feasible with deliberate organization-owned Monitoring Scope, Assertion Authority, identity and correlation records where required. Collibra and Immuta remain optional integrations; their absence narrows specific capabilities and is never a benign default.

Identity/join reliability, authority applicability, T/K/clock quality, strong-negative coverage, latency, retention/replay/communication durability, disclosure/inspectability, quota/cost and integration health remain separate. Latency changes knowledge eligibility, not event truth. Native vendor retention is heterogeneous and cannot be treated as one indefinite ledger. Quota/cost is operational feasibility, not evidence authority. Integration failure/permission denial/throttling/lag/pagination/schema drift/retention expiry/optional-source absence never becomes monitored-product absence.

No universal source-support, confidence, completeness, health, Impact, control-effectiveness or replay score is accepted.

## Stable contracts

### INTG-239 — Consolidated Feasibility Classification
Classify each accepted proposition against its exact source set/context as native, conditional/composed, unsupported or environment-specific/unknown; never convert feasibility into truth/confidence.

### INTG-240 — Source-Family Responsibility Composition
Compose source families by proposition/evidence responsibility rather than choosing one vendor-wide system of record; each surface retains its narrow authority/coverage.

### INTG-241 — Cross-System Identity & Join Feasibility
Treat governed joins as explicit architecture requirements for UC↔governance identities, revision↔deployment↔run, run↔version, consumer↔state and evidence↔Explanation basis; names/timestamps remain insufficient.

### INTG-242 — Governance & Authority Coverage
Governance/authority support remains facet/claim-class/context specific and can require organization-owned registries where vendors do not natively encode Monitoring Scope or Assertion Authority.

### INTG-243 — Change / Deployment / Run Correlation Feasibility
Exact change/deployment/run association is conditional on explicit immutable correlation/attestation across systems; workflow/deploy success or proximity is not enough.

### INTG-244 — Run Implementation-Version Coverage
Run-specific implementation state can be partial/composite; direct-Git revision support does not automatically cover bundle/workspace-source code, config, runtime and target facets.

### INTG-245 — Input / Output Version Coverage
Output version binding can be conditional/per-output; generic exact multi-input consumed-version manifests remain unsupported out of the box for arbitrary workloads without instrumentation.

### INTG-246 — Health & Measurement Source Coverage
Health support composes structural, metric, check, Baseline, Expectation, reconciliation and freshness sources while retaining their definition/grain/current-cycle gaps.

### INTG-247 — Lineage / Encounter / Impact Coverage
Lineage topology is comparatively strong while exact consumer-state exposure, external use, business consequence and strong non-exposure require additional path/version/population evidence.

### INTG-248 — Investigation & Causal Coverage
Sources can support inquiry/localization/causal evidence, but no evaluated source automatically confirms Causal Claims; REF-017 + AUTH-034 remain decisive.

### INTG-249 — Safeguard / Gate / Control Coverage
Control support is path/opportunity/implementation specific; universal Safeguard, prevention, Gate enforcement and historical control proof remain conditional or unsupported where lifecycle telemetry is absent.

### INTG-250 — Explanation / Replay / Basis Coverage
Source replay, availability-by-K, retained communication, historical authorization and current `inspectBasis` have different durability requirements and cannot be collapsed into one history capability.

### INTG-251 — Common Derivation & Conflict Composition
Preserve common derivation and explicit conflicts across sources/exports; duplicates and fallback endpoints do not become independent support or hidden precedence.

### INTG-252 — Temporal Ordering & Clock Quality
Record source clock semantics, precision, timezone, lag and known skew where sequence/knowledge cuts matter; temporal proximity is not exact association or causality.

### INTG-253 — Latency Envelope Classification
Classify latency by use/source surface and evidence availability; slower publication delays knowledge eligibility but does not change effective-time truth.

### INTG-254 — Strong-Negative Coverage Feasibility
Strong negatives remain expensive: exact opportunity/population/path/window, sufficient collection/query coverage and known source health are mandatory.

### INTG-255 — Integration-Health Observability Requirement
Enterprise trust requires explicit visibility into auth success/failure, permission denial, throttling, outage/timeout, delayed publication, pagination, API/schema drift, parser failure, retention expiry and optional integration state.

### INTG-256 — Retention-Horizon Composition
Historical capability is limited by the shortest material unretained dependency unless required evidence is independently retained; no source family implies a universal retention horizon.

### INTG-257 — Long-Horizon Provenance Durability Requirement
Where enterprise replay exceeds vendor-native history, Phase 010 must decide which identity/provenance/source facts require product-owned or exported long-horizon durability.

### INTG-258 — Availability-by-K Durability Requirement
As-known replay requires durable evidence of when basis became reliably available, not merely retained event timestamps or current retrievability.

### INTG-259 — Retained Explanation Communication Requirement
Proving actual prior Explanation content/audience/limitations requires retained communication snapshots/equivalent evidence; source replay alone is insufficient.

### INTG-260 — Historical Authorization Durability Requirement
Historical access/authorization claims require retained authority/policy/principal state appropriate to the exact time/population/path; current authorization is not historical authorization.

### INTG-261 — Basis Disclosure Durability & Sensitivity
Long-horizon basis inspection must preserve exact provenance and sensitivity/authorization metadata while allowing restricted detail to remain restricted.

### INTG-262 — Databricks System-Table Economics
System-table use/cost characteristics affect collection/query strategy only; current free-table availability plus query compute cost does not alter evidence semantics.

### INTG-263 — Databricks API & Lineage Quota Envelope
Endpoint/scope-specific Databricks API and lineage limits constrain feasible refresh/coverage and must be observable; throttling cannot become a negative domain fact.

### INTG-264 — GitHub API Quota Envelope
GitHub primary/secondary/audit API limits constrain collection frequency/coverage and require operational handling without weakening evidence burden.

### INTG-265 — GitHub Actions Usage-Cost Boundary
Actions minutes/storage/overage affect operational feasibility if later used for collection/control workflows; they create no evidence authority or control truth.

### INTG-266 — Collibra Throttling, License & Capacity Boundary
Collibra throttling/license/capacity constraints are environment/contract operational limits and may reduce feasible coverage/latency without changing semantic requirements.

### INTG-267 — Immuta Operational Cost / Quota Boundary
Immuta API/retention/pricing/quota characteristics remain environment/contract specific where no stable universal value is verified; unknown stays unknown until discovery.

### INTG-268 — Optional-Integration Degradation Contract
If an optional integration is absent/unhealthy, only the propositions depending on it degrade; the framework must surface explicit gaps instead of synthesizing benign defaults.

### INTG-269 — MVP Source-Sufficiency Boundary
A Databricks/GitHub-centered MVP is acceptable only within the bounded proposition set its sources support, plus deliberate organization-owned scope/authority/identity/correlation records where required.

### INTG-270 — Phase 010 Handoff & Phase 009 Exit
Phase 010 receives stable source-capability facts and residual gaps as architecture obligations; it may choose technical realization but may not reopen/weaken accepted source semantics for convenience.

## Accepted residual obligations

Architecture must explicitly address long-horizon provenance, availability-by-K, retained communication, historical authorization, basis sensitivity, cross-system identity/correlation, generic input-version gaps, exact consumer-state exposure, integration-health observability and quota/cost-aware collection where the committed proposition requires them.

These are architecture inputs, not reopened semantic questions.

## Architecture boundary

This resource does not choose storage, graph, streaming, service, LLM, control, deployment, adapter or retention architecture. It records what any later architecture must preserve.

## Provenance

- `docs/concepts/phase_009/08_cross_source_coverage_latency_retention_cost_consolidation_exit/README.md`
- Phase 009 Group 08 accepted INTG-239–INTG-270 and Phase 009 exit.
