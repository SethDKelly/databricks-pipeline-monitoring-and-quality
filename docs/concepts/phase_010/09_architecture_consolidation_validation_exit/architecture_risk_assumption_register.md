# Phase 010 Group 09 — Architecture Risk / Assumption Register

**Status:** ACCEPTED — implementation handoff input

Risks and assumptions remain explicit because Phase 010 deliberately refuses to treat unknown target deployment facts as verified capability.

## Architecture risks

| ID | Risk | Consequence if ignored | Architectural treatment | Implementation validation |
|---|---|---|---|---|
| R-010-01 | Target Databricks capability differs by cloud/region/edition/preview state | Required source/control path unavailable | Revisioned capability inventory and proposition-specific eligibility | Environment discovery before feature enablement |
| R-010-02 | System-table/source publication lag exceeds interactive expectation | Stale/incorrect near-current claims | SC-specific SLOs; distinguish publication/acquisition/serving lag | Measure each enabled source surface |
| R-010-03 | API rate/quota limits constrain reconciliation | Coverage gaps or excessive cost | Quota ledger, bulk/selective collection, priority/backpressure | Load test against target auth/endpoint budget |
| R-010-04 | Monitoring Scope materially exceeds connector discoverability | False negative population | Organization-owned scope + collection coverage manifest | Reconcile expected population against source visibility |
| R-010-05 | Identity mapping collides on names/renames/recreations | Incorrect cross-system joins | Stable source IDs, canonical identity bindings/incarnation history | Adversarial rename/recreate fixtures |
| R-010-06 | Bundle/workspace-source workloads cannot prove exact Git revision | Overclaimed implementation provenance | Exact revision remains partial unless source/attestation exists | Instrument representative deployments or explicitly scope claim |
| R-010-07 | Workloads cannot expose exact multi-input consumed versions | Incorrect current-cycle/exposure claims | Source-specific consumption manifest/attestation interfaces | Instrument material workloads; retain unknown siblings |
| R-010-08 | Native Lineage is incomplete or delayed | Overbroad/no-dependency claims | Coverage-aware typed Lineage + optional attestation | Compare native capture with known fixtures |
| R-010-09 | External consumer/cache state unavailable | Reachability confused with exposure | Separate candidate/encounter/version/effect/consequence | Integrate representative consumer telemetry or limit claims |
| R-010-10 | Business consequence sources are absent/low quality | Technical state narrated as organizational Impact | Consequence remains independent optional evidence family | Select authoritative sources before enabling consequence claims |
| R-010-11 | Policy rules are under-specified | Hidden access/authority precedence | Explicit rule revisions; unknown/conflicting states retained | Organization policy review and policy test fixtures |
| R-010-12 | Authorization cache becomes stale after revocation | Data/control leakage | Context/revision/horizon-aware cache; revalidation for sensitive action | Revocation race testing |
| R-010-13 | Sensitive metadata leaks through logs/search/vector/caches | Confidentiality/residency breach | Pre-index authorization/minimization; sensitive telemetry controls | Security tests for count/type/path/identity leakage |
| R-010-14 | LLM output subtly strengthens/omits limitations | Epistemic overclaim | Statement IR bounded rendering + validation + deterministic fallback | Mutation/adversarial render tests |
| R-010-15 | Delta-backed graph traversal misses interactive latency target at scale | Poor RCA UX | Specialized graph remains reversible measured extension | Benchmark representative depth/concurrency/graph size |
| R-010-16 | Canonical Delta schema evolves incompatibly | History/read/write breakage | Versioned migrations, compatibility window, non-rewriting backfill | Migration rehearsal and rollback test |
| R-010-17 | Archive restore is slower/incomplete vs product promise | Historical replay SLO breach | Tier-specific RPO/RTO, restore provenance, pins/holds | Restore drills with representative retained basis |
| R-010-18 | Cost pressure drives unreviewed evidence reduction | Semantic correctness erodes | Budget policy cannot silently weaken required scope/coverage/retention/control | Cost-failure tests and policy review |
| R-010-19 | Interactive/model workloads starve SC-06 control path | Missed control opportunity | Priority/failure-domain isolation | Concurrency/saturation tests where control enabled |
| R-010-20 | Enforcement adapter semantics differ from assumed Gate/Safeguard behavior | False protection claims | Deployment-verified capability + exact opportunity/path mapping | End-to-end enforcement/reconciliation test |
| R-010-21 | Multiple control paths/bypasses exist outside broker/protection | Global prevention overstated | Alternate-path inventory and prevention manifest | Red-team bypass path inventory |
| R-010-22 | Current authorization/config used during historical replay | Historical rewrite | Bitemporal journals + availability-by-K + historical policy revision | Replay tests before/after policy/config changes |
| R-010-23 | Retained Explanation/basis policy insufficient for audit promise | Cannot prove prior communication | Promise-bound snapshot/basis retention | Retention/expiry test against stated audit use |
| R-010-24 | Backup copies violate residency/disclosure boundary | Security/compliance risk | Residency-aware backup/archive and same disclosure governance | Deployment security review |
| R-010-25 | Documentation and implementation drift after architecture freeze | Semantics silently lost | Contract-to-test traceability and canonical docs status checks | CI architecture/schema/scenario validation |

## Accepted architecture assumptions

| ID | Assumption | Classification | Consequence if false | Required action |
|---|---|---|---|---|
| A-010-01 | A target implementation can use a Delta-compatible governed canonical store | Architecture assumption selected by Phase 010 | Re-evaluate persistence realization without changing semantics | New ADR/architecture review before substitution |
| A-010-02 | Representative MVP deployments include Databricks and Git/GitHub evidence | Product/MVP assumption | MVP proof scenarios need alternate source integration plan | Update deployment profile, not truth model |
| A-010-03 | Organization can provide or govern Monitoring Scope | Product governance requirement | Broad monitoring/negative claims cannot be safely bounded | MVP cannot claim unsupported population completeness |
| A-010-04 | Organization can provide Assertion Authority policy for claims that require it | Product governance requirement | Authority-gated propositions stay unresolved | Do not infer authority from roles/source presence |
| A-010-05 | Identity/authentication infrastructure can expose stable enough principal references for canonical binding | Deployment assumption | User/workload identity correlation degrades | Add mapping/manual governance or limit protected features |
| A-010-06 | At least one worker/runtime can execute reconciliation/evaluation/reasoning near canonical storage | Deployment assumption | Latency/cost topology changes | Select alternative runtime while preserving contracts |
| A-010-07 | UI/API callers can be routed through a governed service boundary | Architecture assumption | Direct table-access deployments need equivalent enforced projection layer | Architecture exception review required |
| A-010-08 | Optional integrations can be absent without invalidating passive core | Accepted architecture property | If a promised use requires them, that deployment feature becomes unavailable | Capability-gate exact feature |
| A-010-09 | Active controls are not mandatory for initial MVP | Accepted MVP boundary | If pilot requires control, implement full SC-06 contracts | Promote control work into implementation scope deliberately |
| A-010-10 | Numeric SLO/capacity/cost values can be set after environment measurement | Phase 010 decision | Premature universal targets avoided | Performance phase records concrete ADR values |

## Exit interpretation

None of the registered risks requires a new product concept or ARCH-501. They are implementation/deployment validation obligations against the frozen architecture.
