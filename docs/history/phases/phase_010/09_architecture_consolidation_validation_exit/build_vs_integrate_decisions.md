# Phase 010 Group 09 — Build-vs-Integrate Decisions

**Status:** ACCEPTED — responsibility freeze, product selection deferred where appropriate

The core rule is to **build DMTZ semantics and integrate commodity/source capabilities**. A vendor product can realize a technical function; it must not silently redefine a DMTZ concept or evidence rule.

| Capability | Default posture | Why | Integration boundary |
|---|---|---|---|
| Canonical evidence/provenance/time schemas | Build | DMTZ-specific evidence/time contracts | Persist using Delta/governed storage |
| Canonical Entity/Principal crosswalk | Build | Ecosystem identity semantics are product-specific | Consume source IDs/IdP identities |
| Monitoring Scope registry/materialization | Build core | No source discoverability rule safely replaces DMTZ scope | Optional policy/source integrations may author/feed rules |
| Assertion Authority evaluation | Build core | Proposition/facet/context/time authority is DMTZ-specific | Optional governance systems provide eligible assertions/rules |
| Capability Authorization/disclosure composition | Build semantic core; integrate enforcement/IAM | DMTZ action/detail/context semantics must remain explicit | IdP, UC, Immuta/policy engines may supply identity/policy/evidence |
| Source authentication/credential storage | Integrate | Commodity security capability | Prefer federation/short-lived identities; use deployment-approved secret facility otherwise |
| Databricks/GitHub source adapters | Build DMTZ adapters over vendor APIs/tables/SDKs | Need exact provenance, coverage, checkpoints and proposition mappings | Vendor clients/SDKs are transport helpers |
| Reconciliation/checkpoint/coverage framework | Build | DMTZ negative-evidence/integration-health semantics depend on it | Scheduler/queue may be integrated |
| Raw/envelope/object storage | Integrate | Commodity storage | DMTZ controls minimization, identity and retention policy |
| Canonical Delta storage engine | Integrate | Delta is selected persistence realization, not something to reimplement | UC managed/external realization is deployment-bound |
| Metric/check computation | Hybrid | Common engines can compute observations; DMTZ owns definitions/provenance/Assessment semantics | DQX/SQL/Spark/Metric Views or other engines may be used where verified |
| Runtime attestation | Build lightweight DMTZ contract/SDK or adapters | Exact bundle/input/output provenance is not universally source-native | Language-specific implementation deferred |
| Lineage collection | Integrate + normalize | Native lineage is useful but incomplete/semantically bounded | DMTZ retains typed/provenance/coverage semantics |
| Derived operational/reasoning graph | Build projection model; integrate compute engine as needed | Edge typing/provenance are DMTZ-specific | Delta/Spark first; specialized graph only after measurement |
| Search/vector retrieval | Integrate optionally | Commodity candidate-recall capability | Never evidence/authority/completeness owner |
| Deterministic evidence/status reasoning | Build | Core DMTZ epistemic logic | May run on general compute/runtime |
| Investigation/Causal Claim state machine | Build | Product-specific lifecycle/evidence semantics | External ticket/case tools may link to canonical identity |
| Historical replay engine | Build | Availability-by-K, policy revision and retained-history semantics are DMTZ-specific | Storage/archive engines are integrated |
| Statement IR / Answer IR | Build | Central Explanation traceability contract | Renderers consume it |
| Deterministic renderer | Build | Required no-model truthful fallback | UI/template technology implementation choice |
| LLM/model rendering/lead assistance | Integrate optionally | Model capability is replaceable/optional | Bounded gateway/tools; no truth/control authority |
| API/service façade | Build DMTZ application layer | Request context, authorization, epistemic envelope and exact operations are product-specific | Framework/gateway/hosting product deferred |
| UI | Build product experience | DMTZ state distinctions and basis flows must be represented faithfully | Component/design system choices deferred |
| Gate decision state machine | Build | DMTZ criterion/readiness/decision semantics | Enforcement adapters integrate GitHub/Databricks capabilities |
| Propagation Safeguard state machine | Build | DMTZ protected-path/prevention semantics | Enforcement mechanisms are path/vendor integrations |
| Observability backend | Integrate | Commodity operational telemetry storage/alerting | DMTZ defines dimensions/correlation/SLO semantics |
| Cost/billing source | Integrate + normalize | Vendor usage data is source evidence | DMTZ adds attribution policy/dimensions |
| Backup/archive mechanism | Integrate | Commodity resilience capability | DMTZ defines which evidence/promises require protection |
| IaC/deployment automation | Integrate/select later | Implementation/runtime concern | Must preserve environment/config/version/provenance boundaries |

## Do not build prematurely

Phase 010 specifically rejects building custom versions of these without a measured reason:

- graph database;
- vector database/search engine;
- secret manager;
- general-purpose IdP;
- general-purpose queue/event bus;
- general-purpose observability backend;
- custom LLM/agent framework;
- custom cloud object store.

## Do not outsource semantically

No integration may own by implication:

- DMTZ Monitoring Scope;
- DMTZ Assertion Authority;
- DMTZ causal confirmation;
- DMTZ negative-coverage sufficiency;
- DMTZ Explanation truth/Statement identity;
- DMTZ Gate readiness/decision semantics;
- DMTZ REF-028 prevention semantics.

A product can be an authoritative source for a bounded underlying facet only under the accepted authority rules.
