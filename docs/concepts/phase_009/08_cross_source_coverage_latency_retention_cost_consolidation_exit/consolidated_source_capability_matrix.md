# Phase 009 Consolidated Source Capability Matrix

This matrix consolidates Groups 01–07 under INTG-239–INTG-270. Support remains **proposition + source set + context + time perspective** bound. It is not a vendor scorecard, architecture decision, confidence score or claim that every deployment has enabled the named source.

| Capability / proposition family | Primary evaluated source families | Phase 009 exit result | Material boundary / Phase 010 implication |
|---|---|---|---|
| Exact Databricks object/principal identity | Unity Catalog / system metadata | Supported in platform-local scope | Cross-system Entity Identity still needs governed mapping |
| Ecosystem cross-system identity | UC + GitHub + Collibra + Immuta + IAM | Partially supported / implementation required | Durable identity crosswalk is required; names/timestamps insufficient |
| Monitoring Scope | organization-owned governed metadata/config | Unsupported out of box / design required | No evaluated vendor natively owns DMTZ Monitoring Scope |
| Semantic Definition | UC comments/properties, Collibra governed facets, repository definitions | Conditional / strong with explicit authority | Facet/source authority must be governed; source origin alone is insufficient |
| Responsibility Assignment | Collibra responsibilities, GitHub CODEOWNERS, UC owner, org records | Conditional | Each surface owns narrower responsibility semantics; no blame/authority promotion |
| Classification / Policy Context | governed UC tags, Collibra classes/attributes, Immuta metadata/policies | Conditional | Scheme/context-specific authority; tags/policies do not become compliance truth |
| Assertion Authority registry | organization-owned governance record | Unsupported out of box / required | Vendor owner/role/title does not implement AUTH-001–AUTH-008 |
| Capability Authorization | UC, Immuta, GitHub, Collibra and IAM permissions | Conditional / composed | Effective authorization can require multiple enforcement planes and current requester context |
| Git revision identity | Git/GitHub commit SHA | Supported | Revision identity ≠ Change Intent without governance rule |
| GitHub workflow/run/attempt identity | GitHub Actions | Supported | Workflow success ≠ Databricks activation |
| GitHub deployment request/status | GitHub Deployments | Supported for GitHub proposition | Target activation requires explicit target evidence/correlation |
| CI → Databricks deployment/run association | GitHub + target attestation | Partially supported / explicit correlation required | Shared immutable correlation/manifest/fingerprint needed where native join absent |
| Direct remote-Git Databricks run commit | Lakeflow Jobs `git_snapshot.used_commit` where present | Supported / strong | Applies only to qualifying direct-Git run surface |
| Bundle/workspace-source exact run commit | bundle + workspace-source metadata | Unsupported out of box / instrumentation required | Repository origin/branch does not prove immutable run commit |
| Composite run-specific implementation state | run + job/task config + code + params/runtime/libs | Partially supported | Requires multiple evidence facets; active/current config cannot substitute |
| Run/task lifecycle | Jobs API + Lakeflow system tables | Supported with retention/detail limits | Recent API detail and longer system-table history differ |
| Retry / repair / rerun / backfill | Jobs/workflow/runtime sources | Supported when explicit source identities exist | These remain distinct continuity semantics |
| Actual dependency precedence | task/run timeline | Conditional / strong | Configured dependency ≠ actual precedence ≠ waiting ≠ consumption |
| Output version binding | Delta history + run correlation | Conditional / per output | Run success does not prove output; correlation must be explicit |
| Generic exact multi-input consumed versions | generic Spark/SQL workloads | Unsupported out of box | Workload/query/source instrumentation or manifest required where exact input set matters |
| Current realized schema | Unity Catalog metadata | Supported for visible current state | Current/observer-relative metadata ≠ historical schema or consumer compatibility |
| Consumer-specific structural compatibility | explicit interface/contract + observed structure | Partially supported / org contract required | Engine compatibility and schema equality are insufficient |
| Empirical key/referential integrity | explicit checks/DQ evidence | Conditional | Informational PK/FK declarations do not prove empirical integrity |
| Governed Expectations | DQX/Lakeflow rule + organization authority | Conditional / strong | Rule existence/generated origin ≠ governed Expectation authority |
| DQ observations/results | DQX, Lakeflow expectations | Supported where executed/retained | Skipped/failed/untracked evaluation ≠ clean result |
| Business metric semantics/value | Metric Views + governed semantic version | Conditional / strong | YAML spec version ≠ organization metric revision; join assumptions need evidence |
| Descriptive profile/drift | Databricks profiling | Supported as descriptive source result | Drift ≠ Baseline membership ≠ normative violation |
| Vendor anomaly/freshness/table status | Databricks anomaly detection | Supported as vendor-owned derived assertion | Vendor `Healthy`, root cause or impact labels do not become DMTZ truth |
| Event-time/ingestion-latency freshness | workload/domain telemetry | Partially supported / separate evidence required | Commit freshness is not event-time freshness |
| Baseline membership/comparability | explicit framework/org baseline definition + observations | Conditional | Vendor historical model/reference table does not self-authorize Baseline |
| Reconciliation | exact source/output/key/metric/window evidence | Conditional / strong | Reconciliation result ≠ causal attribution |
| Run/current-cycle health | run/output/measurement/input version joins | Partially supported | Exact multi-input current-cycle state inherits consumed-version gap |
| Effective lineage topology | UC lineage + identity/history | Partially supported | Capture incomplete; rename/path continuity requires reconciliation |
| Observed SQL table encounter | lineage `statement_id` + query history | Conditional / strong | Read encounter may be known while exact data version remains unresolved |
| Exact affected-version consumer exposure | version/state evidence + encounter | Partially supported | Generic object read/query time cannot identify exact consumed version universally |
| Dashboard/report access | dashboard audit/query/snapshot evidence | Conditional | Access ≠ dataset execution ≠ result receipt ≠ reliance |
| Dashboard cache-state exposure | cache/result-state evidence | Partially supported / instrumentation may be required | Cached state can be safe, affected or unresolved independently of current source |
| External BI/application use | Databricks client/query context + external telemetry | Partially supported | Platform read ≠ external report/app display or human/business use |
| Multi-hop exposure | per-hop state propagation + encounter evidence | Partially supported / coverage intensive | Exposure is non-transitive |
| Downstream technical/analytical effect | Group 04 measurements bound to consumer state | Conditional | Effect ≠ consequence ≠ causality |
| Business/customer/financial consequence | application/process/ticket/financial sources | Environment-specific / unsupported from Databricks alone | Requires organization-specific consequence evidence |
| Strong `not exposed` / `no effect` / `no consequence` | exact population/path/version/dimension coverage | Conditional / expensive | One safe path or no record is insufficient |
| Investigation trigger/lead/localization | Groups 03–05 + analyst/model annotations | Supported as inquiry evidence | Localization/lead ≠ Causal Claim |
| Causal support/contradiction | runtime/version/reconciliation/exposure/intervention evidence | Conditional | Claim-relative evidence roles; timing/rollback alone not proof |
| Confirmed Causal Claim | evidence + AUTH-034 authority | Conditional / organization-owned confirmation | No evaluated vendor automatically confirms causality |
| Durable Investigation/Annotation record | issue/ticket/custom case source | Environment-specific | No universal DMTZ case store selected or assumed |
| Databricks control action history | `system.access.audit` | Supported for qualifying events within retention | Request/success response ≠ distributed effective enforcement by default |
| Immuta query-time policy enforcement | Immuta audit for covered population | Conditional / strong | Registration/integration/audit scope and retention bound |
| Propagation Safeguard enforcement | exact path/control + state evidence | Conditional | No universal native Safeguard covers all cache/export/API/application paths |
| REF-028 prevented exposure | opportunity + enforcement + non-exposure + alternate-path coverage | Conditional / highly coverage intensive | Active control + non-exposure is insufficient |
| GitHub environment pre-start Gate | Actions environment protection | Supported for exact protected GitHub job | Does not gate uncorrelated Databricks execution |
| Databricks conditional-task Gate realization | `Run if` / `If/else` + governed criterion mapping | Conditional / strong candidate | Condition/result does not automatically define DMTZ readiness/Gate |
| HOLD enforcement | decision/delivery/barrier + opportunity/start evidence | Conditional | Start contradicts unsuperseded HOLD; no start alone does not prove HOLD |
| ADMIT | barrier/permissive state | Conditional | ADMIT ≠ execution occurrence |
| Override/fallback/multi-Gate composition | explicit organization control contracts | Environment-specific / conditional | No universal precedence or fallback semantics supplied by vendors |
| Historical source-state replay | per-source history | Partially supported | Retention/mutation horizons differ materially |
| Exact as-known-at-K replay | source history + availability-by-K evidence | Partially supported | Event time alone insufficient; first-available time often absent |
| Actual retained Explanation | retained communication/snapshot/channel record | Environment-specific / often unsupported natively | Source reconstruction and delivery metadata do not prove exact prior content |
| Current retrospective Explanation | surviving current/historical evidence | Supported where source basis survives | Must stay distinct from incident-time knowledge and prior communication |
| Internal statement→basis traceability | durable proposition/source identity | Supported by contract / implementation required | Friendly names/current URLs are insufficient durable identity |
| Current `inspectBasis` for historical statement | stable basis + source survives + current authorization | Conditional | Reference may survive while source payload expires |
| Exact prior `inspectBasis` projection | retained prior communication/projection metadata | Environment-specific / generally unsupported natively | Current access/reconstruction cannot prove prior visible detail |
| Safe coarse/redacted/opaque projection | AUTH/EXPL + source disclosure metadata | Conditional | Abstraction may say less, never more; existence/type/count can be sensitive |
| Databricks system-table replay horizon | many material system tables | Supported within documented surface-specific horizon | Many are 365 days; not one indefinite ledger |
| GitHub audit replay | enterprise/org audit | Partially supported | Ordinary events ~180 days; Git events ~7 days unless externally retained |
| Collibra historical governance replay | resource history where enabled | Conditional | Facet-specific gaps and configurable history suppression |
| Immuta audit replay | UAM/application/query audit | Conditional | Native SaaS retention about 90 days; longer horizon depends on export |
| Cross-source time ordering | source-specific timestamps | Partially supported | Different clocks/precision/lag can prevent exact ordering |
| Near-current monitoring | runtime/query/system/API mix | Conditional | Some system tables are delayed and explicitly non-real-time |
| Integration-health observability | HTTP/query/auth/pagination/schema/parser telemetry | Required / implementation-specific | Source failure must stay distinct from monitored-domain negative facts |
| Databricks query economics | system tables + Databricks compute | Supported cost model | System tables are free to use; compute used to query them is billable |
| Databricks API quotas | REST + lineage endpoint limits | Supported as documented constraint | Limits vary by endpoint/scope and must shape collection feasibility |
| GitHub API quotas | REST/audit/secondary limits | Supported as documented constraint | Rate exhaustion/throttling must be observable and retried, never read as absence |
| GitHub Actions future collection/gating cost | plan allowance + metered Actions usage/storage | Conditional / architecture-dependent | Phase 009 does not select Actions as ingestion/control implementation |
| Collibra API/token/capacity limits | REST/GraphQL throttling + OAuth + licensing | Environment-specific / documented defaults exist | Exact tenant config/license must be discovered |
| Immuta API/licensing/cost limits | deployed Immuta contract/config | Unknown / environment-specific | No generic undocumented rate/pricing assumption accepted |
| Optional Collibra/Immuta absence | capability matrix degradation | Supported graceful degradation | Missing optional source creates explicit gaps, not benign defaults |
| Bounded MVP feasibility | Databricks + GitHub + organization-owned governance/correlation | **Feasible for Phase 010 design** | Enterprise completeness still depends on explicit retention/instrumentation/optional sources |

## Exit conclusion

The evaluated source set is sufficient to begin Phase 010 technical architecture **without reopening accepted functional semantics**. The framework does not require Collibra or Immuta as universal MVP dependencies, but organization-owned Monitoring Scope/Assertion Authority/correlation records and several product-owned durability/instrumentation capabilities are necessary if the corresponding enterprise propositions are in scope.

No universal support percentage is produced. Unsupported and partial cells are deliberate Phase 009 results, not defects to hide through architecture language.
