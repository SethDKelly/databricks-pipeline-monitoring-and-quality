# Phase 009 Residual Gap Register

These gaps are accepted Phase 009 findings. A gap can be resolved, reduced, deliberately left partial, or scoped out in Phase 010/product planning, but it cannot be hidden by weakening the functional proposition it affects.

| ID | Residual gap | Current support | Why it matters | Phase 010 handoff requirement |
|---|---|---|---|---|
| GAP-009-01 | Governed Monitoring Scope registry | Unsupported out of box | Monitoring inclusion/exclusion cannot safely be inferred from discoverability | Realize an explicit governed scope source and history |
| GAP-009-02 | Assertion Authority registry | Unsupported out of box | Vendor ownership/roles do not define who may authoritatively assert every proposition category | Realize proposition/category/context/time-specific authority rules |
| GAP-009-03 | Durable cross-system Entity Identity crosswalk | Partial | UC/GitHub/Collibra/Immuta/IAM identifiers do not safely compose by name | Preserve stable mappings, aliases, lifecycle and provenance |
| GAP-009-04 | Generic GitHub CI → Databricks deployment/run correlation | Partial | Workflow success does not prove target activation/run | Retain immutable shared correlation/attestation evidence |
| GAP-009-05 | Bundle/workspace-source exact run Git commit | Unsupported out of box | Repository origin/branch does not prove revision executed | Add immutable deployment/run revision/content attestation where required |
| GAP-009-06 | Composite run-specific implementation state | Partial | Code SHA alone omits job config/params/runtime/libs/environment | Bind exact required implementation facets to each run |
| GAP-009-07 | Generic exact multi-input consumed-version manifest | Unsupported out of box | Current/latest inputs cannot answer exact consumption/current-cycle questions | Add workload/query/source version instrumentation or manifests where required |
| GAP-009-08 | Consumer-specific compatibility contract | Partial | Platform schema/engine support does not define each consumer interface contract | Retain governed interface/compatibility definitions and evaluations |
| GAP-009-09 | Empirical relationship/key integrity where platform declarations are informational | Conditional | Declared PK/FK does not prove uniqueness/referential integrity | Provide observed checks when the proposition matters |
| GAP-009-10 | Governed DQX/Expectation/metric definition revisions | Environment-specific | Rule/metric availability does not establish governed normative semantics or history | Version authoritative definitions and applicability |
| GAP-009-11 | Event-time/ingestion-latency freshness evidence | Partial | Commit freshness does not answer event-latency freshness | Instrument domain timestamps/watermarks where required |
| GAP-009-12 | Exact measurement → run/output attribution | Partial | Latest table/metric state cannot prove run-specific health | Preserve run/output/version keys with measurement results |
| GAP-009-13 | Complete historical lineage / rename continuity | Partial | Native capture is incomplete and rename/path changes can break continuity | Persist/reconcile durable identity and lineage evidence as needed |
| GAP-009-14 | Generic exact consumer-version exposure | Partial | Read encounter may be known while affected version remains unknown | Capture consumed version/state for material consumers/paths |
| GAP-009-15 | Dashboard/query cache state identity | Partial | Cached result can represent safe/affected/unknown prior state | Retain cache/result version provenance where exposure questions require it |
| GAP-009-16 | External BI/report/application display/use telemetry | Environment-specific | Databricks read does not prove external report view or application use | Integrate consumer telemetry for material downstream modes |
| GAP-009-17 | Business/customer/financial consequence evidence | Environment-specific | Platform telemetry does not natively prove organizational consequence | Integrate incident/process/decision/financial sources where in scope |
| GAP-009-18 | Strong multi-hop non-exposure/no-effect/no-consequence coverage | Partial / expensive | Missing telemetry and one safe path cannot support broad negatives | Define populations/paths and retain sufficient negative-coverage telemetry |
| GAP-009-19 | Durable Investigation/Annotation/claim-status record | Environment-specific | Vendor facts do not constitute full Investigation workflow/history | Choose/realize case/annotation persistence later without changing causal semantics |
| GAP-009-20 | Causal confirmation authority | Organization-specific | No vendor automatically owns `confirmed` Causal Claim | Bind REF-017 evidence to AUTH-034 authority source/workflow |
| GAP-009-21 | Universal Propagation Safeguard across all delivery paths | Unsupported as one native feature | ACL/policy/quarantine often covers only selected paths | Design path-specific safeguards and explicit alternate-path coverage |
| GAP-009-22 | REF-028 prevention evidence across alternates | Conditional / expensive | Active control plus safe outcome does not prove prevention | Preserve opportunity + enforcement + negative encounter + alternate-path evidence |
| GAP-009-23 | GitHub Gate → Databricks execution correlation | Partial | GitHub environment can gate its job without proving target run was gated | Reuse explicit deployment/run correlation for cross-system Gate claims |
| GAP-009-24 | Organization-specific Gate criterion/override/fallback/multi-Gate rules | Environment-specific | Vendor conditions do not define DMTZ readiness or composition | Version governed criteria and exceptional-action authority |
| GAP-009-25 | Long-horizon source replay beyond vendor retention | Partial | Major source histories expire at different horizons | Decide which evidence/provenance must be retained product-side or externally |
| GAP-009-26 | Availability-by-K timestamps for exact as-known replay | Partial | Event time alone cannot prove evidence was knowable by K | Capture source-arrival/availability metadata where historically material |
| GAP-009-27 | Authentic retained Explanation communication | Environment-specific / often unsupported natively | Reconstruction cannot prove actual wording/context/audience/basis visibility | Retain authentic Explanation snapshots or authoritative channel content where required |
| GAP-009-28 | Exact prior `inspectBasis` projection | Generally unsupported natively | Current authorization/basis cannot reconstruct old visible projection | Persist prior projection metadata if this historical audit capability is required |
| GAP-009-29 | Long-horizon historical authorization | Partial | Current permissions cannot reconstruct old access indefinitely | Preserve required authorization/policy state over intended audit horizon |
| GAP-009-30 | Basis payload durability under truncation/encryption/deletion | Partial | Stable reference can survive while exact query/comment/history payload is gone | Retain permitted basis content/provenance or surface unavailability explicitly |
| GAP-009-31 | Sensitive-basis disclosure/minimization policy | Organization-specific | Source existence/count/type/query/actor details can themselves be sensitive | Realize independent result/context/limitation/basis/detail authorization |
| GAP-009-32 | Unified source-latency/availability SLO | Unknown until environment discovery | System tables/API/audit sources have different lag and publication behavior | Define service goals by question class, not one source freshness number |
| GAP-009-33 | Integration-health telemetry | Implementation required | Source outage/throttle/permission/partial reads must not become negative facts | Instrument API/query/source health and pagination/schema/parser state |
| GAP-009-34 | Databricks API quota-aware collection | Conditional | Endpoint-specific limits can make naive polling infeasible | Design collection around exact limits, system tables and bounded demand |
| GAP-009-35 | GitHub API quota-aware collection | Conditional | Primary/secondary/audit limits constrain high-volume polling | Use rate state, efficient incremental retrieval and appropriate auth design later |
| GAP-009-36 | Collibra tenant/licensing/throttle discovery | Unknown/environment-specific | API/token/capacity depends on tenant configuration and commercial package | Treat Collibra as optional until target environment is verified |
| GAP-009-37 | Immuta API/licensing/export-capacity discovery | Unknown/environment-specific | No universal public rate/pricing contract applies across deployments/APIs | Treat exact operational limits as environment/contract discovery |
| GAP-009-38 | Cost attribution for product-owned retention/processing | Not yet architected | Durable evidence and communication retention can materially affect storage/compute | Phase 010 must expose and attribute ingestion/query/storage/control costs |
| GAP-009-39 | Optional source graceful degradation | Semantics accepted; implementation required | Collibra/Immuta absence must reduce only exact capabilities, not fabricate defaults | Build capability-aware feature degradation and partial answers |
| GAP-009-40 | Enterprise deployment-specific capability inventory | Unknown until discovery | Phase 009 evaluates documented possibilities, not the user's actual enabled tenant | Phase 010 begins with environment discovery against this matrix |

## Exit treatment

None of these gaps requires reopening `SYN`, `REF`, `AUTH`, `HLTH`, `OPS` or `EXPL` semantics. They are precisely the information Phase 010 needs to decide ingestion, persistence, correlation, retention, authorization and serving architecture.

The gap register deliberately contains both **semantic-support gaps** and **operational feasibility gaps**. Phase 010 should not solve a quota problem by weakening evidence coverage, or solve a retention problem by relabeling reconstruction as authentic history.
