# Phase 010 Group 09 — Unresolved Implementation Decision Register

**Status:** ACCEPTED — intentionally deferred beyond architecture freeze

These items do not represent missing semantics. They are concrete implementation/product-selection decisions that should be made only after the target deployment and workload are known.

| ID | Deferred choice | Phase 010 constraint | Decision trigger / evidence needed |
|---|---|---|---|
| IMP-010-01 | Primary implementation language(s) | Must implement exact schemas/rules and Databricks/GitHub integrations without semantic shortcuts | Team/runtime compatibility, SDK ecosystem, performance and deployment model |
| IMP-010-02 | API/application framework | Stateless/authorization-aware façade preferred; request context and epistemic envelope mandatory | UI/API requirements, hosting profile, auth integration |
| IMP-010-03 | API gateway / ingress | Authentication/routing cannot replace Capability Authorization | Network/security architecture and hosting platform |
| IMP-010-04 | Worker/orchestration runtime | Reconciliation/checkpoints/durable evidence semantics mandatory | Volume, cadence, failure recovery, target Databricks capabilities |
| IMP-010-05 | Queue/event bus | Optional; transport state never canonical truth | Measured burst isolation, replay/distribution need |
| IMP-010-06 | Adapter SDK structure | Exact capability/surface/acquisition-plan provenance required | Language choice and first source implementations |
| IMP-010-07 | Runtime attestation SDK | Required only for stronger propositions lacking source-native evidence | Representative bundle/multi-input/consumer gaps |
| IMP-010-08 | Exact canonical physical schema layout | Must preserve accepted identity/time/provenance/non-rewriting semantics | Schema design phase and representative query workloads |
| IMP-010-09 | Delta table partition/clustering/optimization | Physical performance only; cannot rewrite semantic history | Data volume and query benchmark |
| IMP-010-10 | Canonical payload object-store layout | Selective/minimized retention, pins/holds and residency | Retention/security/cost profile |
| IMP-010-11 | External IdP integration | Authentication must bind canonical Principal; not authorization/authority | Enterprise IdP and federation capabilities |
| IMP-010-12 | Secret manager / federation realization | Short-lived federation preferred; no secrets in canonical/logging | Cloud/security capability inventory |
| IMP-010-13 | Policy authoring workflow/UI/Git model | Must emit explicit revisioned Monitoring Scope/Authority/Authz/disclosure/control rules | Organization operating model |
| IMP-010-14 | Policy-evaluation library/engine | Cannot introduce hidden precedence/defaults | Policy complexity/performance/administration needs |
| IMP-010-15 | Cache technology | Derived/context-keyed/watermarked only | Interactive latency benchmarks and invalidation needs |
| IMP-010-16 | Dedicated graph engine | Not required initially; derived if adopted | Delta/Spark traversal misses measured latency/complexity target |
| IMP-010-17 | Search/vector provider and embedding model | Candidate recall only, pre-retrieval authorization/minimization | Search UX need, sensitivity review, scale |
| IMP-010-18 | LLM/provider/model gateway | Optional; deterministic fallback required | Product UX need, security/cost evaluation |
| IMP-010-19 | Prompt/trace registry product | Invocation provenance/versioning required if model used | Model deployment selection |
| IMP-010-20 | UI framework/design system | Must faithfully represent partial/unknown/conflict/restricted states | Product implementation planning |
| IMP-010-21 | Observability backend | Must retain required multidimensional metrics/correlation and minimize sensitive telemetry | Existing enterprise stack / hosting platform |
| IMP-010-22 | Alerting/on-call integration | Platform alerting must stay separate from monitored-domain truth | Operating model/SLOs |
| IMP-010-23 | Cost attribution backend/chargeback model | Source usage + DMTZ dimensions; no semantic weakening | Cloud/Databricks billing/tagging and org finance model |
| IMP-010-24 | Numeric SC-01–SC-06 SLOs | Service-class specific; source publication constraints explicit | Baseline measurements and product promise |
| IMP-010-25 | Capacity/autoscaling thresholds | SC-06/required work prioritized; optional work degrades first | Load/performance tests |
| IMP-010-26 | Databricks source acquisition exact surfaces/cadence | Bulk/system-table/reconciliation/selective preferred where verified | Target system-table/API enablement, lag, quota |
| IMP-010-27 | GitHub auth/app installation model | Rate/secondary limits and least privilege observable | Org/repo scope and GitHub deployment profile |
| IMP-010-28 | Collibra integration | Optional/capability-gated | Tenant licensing/authority/use case verified |
| IMP-010-29 | Immuta integration | Optional/capability-gated | Tenant licensing/policy/evidence use case verified |
| IMP-010-30 | External BI/application telemetry integrations | Required only for promised exact consumer-use/exposure claims | Material consumer inventory |
| IMP-010-31 | Business/customer/financial consequence integrations | Optional/source-specific | Product scope and authoritative source availability |
| IMP-010-32 | Active-control deployment | Not required for passive MVP; full semantics mandatory if enabled | Pilot/enterprise control requirement |
| IMP-010-33 | GitHub protection adapter | Exact protected opportunity only; cross-system correlation required | Repository plan/capability and deployment path |
| IMP-010-34 | Databricks pre-start control adapter | Alternate trigger paths must be governed | Target deployment/trigger architecture |
| IMP-010-35 | Safeguard enforcement mechanisms | Path/cohort specific; alternate paths explicit | Material propagation/delivery paths |
| IMP-010-36 | Backup/archive products | Promise/residency/RPO/RTO driven | Retention tier and enterprise platform |
| IMP-010-37 | Multi-region/DR topology | Residency and non-rewriting history constraints | Enterprise availability/residency requirements |
| IMP-010-38 | Infrastructure-as-code / deployment automation | Version/config/capability inventory and rollback semantics preserved | Hosting platform/team standards |
| IMP-010-39 | Performance test thresholds for architecture extension | No specialized tech by intuition | Representative volume/latency/concurrency baseline |
| IMP-010-40 | Executable contract/scenario test harness | Must trace prior accepted semantics and Phase 010 boundaries | First implementation phase |

## Deferral rule

An implementation decision may be made locally without reopening Phase 010 if it satisfies every relevant frozen contract and does not create a new canonical truth owner, authority rule, evidence shortcut, historical rewrite, disclosure shortcut or control semantic.

If a product choice cannot satisfy those constraints, the choice is rejected or requires an explicit architecture reopening rather than an implementation workaround.
