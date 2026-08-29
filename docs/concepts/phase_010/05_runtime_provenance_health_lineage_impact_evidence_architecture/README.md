# Phase 010 Group 05 — Runtime Provenance, Health, Lineage & Impact Evidence Architecture

**Status:** COMPLETE / ACCEPTED

## Result

Group 05 accepts **ARCH-191–ARCH-274** and **RHI05-01–RHI05-108**. Decisions **D-1433–D-1490** are accepted.

The selected evidence chain is:

**source-owned runtime facts + deployment/run attestation where required → exact/partial implementation and input/output manifests → source-owned measurements + governed health derivation → typed historical Lineage → actual consumer encounter/version state → bounded exposure → separately evidenced effect → separately evidenced consequence → Group 06 causal/reasoning handoff**.

No stage automatically creates the next.

## Architecture shape

Group 05 adds five canonical record families to the Group 02 evidence plane:

1. **Runtime provenance journals** — Change/deployment/activation/run/task/attempt/trigger correlations and implementation facets.
2. **Input/output manifests** — exact consumed/produced versions where evidenced, with explicit partial/unknown completeness.
3. **Measurement/Assessment journals** — metric/check/expectation/baseline/reconciliation observations bound to exact target/window/definition/profile revisions.
4. **Lineage and encounter journals** — typed topology plus actual query/read/display/cache/materialization encounters.
5. **Impact journals** — exposure, technical/analytical effects and business/customer/financial consequences kept distinct.

All records retain source/acquisition provenance, event/effective/knowledge coordinates, canonical/source identities, authority/disclosure context where material, and Group 04 coverage/health constraints.

## Contracts

### Runtime/change/deployment — ARCH-191–ARCH-216

- ARCH-191 Runtime Evidence Envelope
- ARCH-192 Run Identity
- ARCH-193 Task-Run Identity
- ARCH-194 Retry / Repair Attempt Identity
- ARCH-195 Git Revision Identity
- ARCH-196 Change Intent Correlation
- ARCH-197 GitHub Workflow-Run Identity
- ARCH-198 GitHub Deployment Identity
- ARCH-199 Cross-System Correlation Token
- ARCH-200 Correlation Attestation
- ARCH-201 Correlation Status & Conflict
- ARCH-202 Direct-Git `used_commit` Binding
- ARCH-203 Workspace-Source Provenance Limitation
- ARCH-204 Bundle Deployment Revision Manifest
- ARCH-205 Workspace Content Attestation
- ARCH-206 Deployment Activation Record
- ARCH-207 Run-Specific Implementation Manifest
- ARCH-208 Code-Facet Binding
- ARCH-209 Job / Task Configuration Revision Binding
- ARCH-210 Parameter Binding
- ARCH-211 Runtime / Compute Binding
- ARCH-212 Library / Dependency Binding
- ARCH-213 Environment / Feature Binding
- ARCH-214 External Configuration Reference
- ARCH-215 Incomplete Implementation State
- ARCH-216 Trigger / Parent-Child Binding

### Input/output/current-cycle — ARCH-217–ARCH-229

- ARCH-217 Input Consumption Manifest
- ARCH-218 Exact Table-Version Consumption
- ARCH-219 File / Object Input Version
- ARCH-220 Stream Offset / Checkpoint Input
- ARCH-221 Multi-Input Consumption Manifest
- ARCH-222 Input-Manifest Completeness
- ARCH-223 Current / Latest Input Rejection
- ARCH-224 Output Production Manifest
- ARCH-225 Output Table-Version Binding
- ARCH-226 Output File / Object Binding
- ARCH-227 Output Non-Existence Burden
- ARCH-228 Current-Cycle Alignment
- ARCH-229 Runtime Binding Conflict

### Health/measurement — ARCH-230–ARCH-246

- ARCH-230 Measurement Identity
- ARCH-231 Measurement Target Binding
- ARCH-232 Measurement Definition Revision
- ARCH-233 Health-Profile Revision
- ARCH-234 Measurement Window & Grain
- ARCH-235 Measurement → Run Attribution
- ARCH-236 Measurement → Output-Version Attribution
- ARCH-237 Event-Time Freshness Evidence
- ARCH-238 Ingestion / Processing Latency Evidence
- ARCH-239 Completeness / Volume Observation
- ARCH-240 Structural / Compatibility Observation
- ARCH-241 Data-Quality Expectation Observation
- ARCH-242 Baseline / Typicality Observation
- ARCH-243 Reconciliation Observation
- ARCH-244 Health-Assessment Composition
- ARCH-245 Health Conflict Preservation
- ARCH-246 Health Negative-Coverage Requirement

### Lineage/encounter — ARCH-247–ARCH-259

- ARCH-247 Lineage Edge Identity
- ARCH-248 Lineage Relationship Type
- ARCH-249 Lineage Temporal Binding
- ARCH-250 Lineage Acquisition Provenance
- ARCH-251 Lineage Coverage & Inference Limitation
- ARCH-252 Lineage Identity Continuity
- ARCH-253 Statement / Query Encounter Join
- ARCH-254 Direct vs Indirect Lineage
- ARCH-255 Lineage Does Not Equal Consumption
- ARCH-256 Consumer Encounter Identity
- ARCH-257 Consumer Use Context
- ARCH-258 Cache / Materialization / Result State
- ARCH-259 Exact Consumed / Affected Version

### Impact — ARCH-260–ARCH-274

- ARCH-260 Exposure State
- ARCH-261 Multi-Hop Exposure Path
- ARCH-262 Alternate-Path Coverage
- ARCH-263 Downstream Effect Record
- ARCH-264 Technical Effect
- ARCH-265 Analytical / Decision Effect
- ARCH-266 Business / Customer / Financial Consequence
- ARCH-267 Impact Evidence Boundary
- ARCH-268 Effect / Consequence Does Not Establish Cause
- ARCH-269 Strong Non-Exposure Coverage
- ARCH-270 No-Effect / No-Consequence Coverage
- ARCH-271 Partial / Unknown Impact
- ARCH-272 Historical Impact Replay
- ARCH-273 Derived Operational Graph Projection
- ARCH-274 Group 05 Handoff Readiness

## Runtime attestation strategy

Group 05 uses **native evidence first, selective attestation second, unknown otherwise**.

Qualifying remote-Git Lakeflow Jobs expose a run-owned `git_snapshot.used_commit`; that is strong code-revision evidence within the supported source/task scope. Bundle/workspace-source deployments do not generically provide the same run-owned Git binding, so DMTZ defines a framework deployment manifest and optional run-start attestation for environments that require exact revision/reproducibility claims.

The attestation contract can carry:

- DMTZ correlation ID;
- source repository + commit;
- bundle/artifact/content digest;
- deployment attempt and target resource IDs;
- effective configuration revision;
- safe parameter/configuration references;
- runtime/library/environment facets;
- input consumption and output production events where exact native evidence is unavailable.

Instrumentation does not become Assertion Authority and does not make an unevidenced event true.

## Exact consumed-version boundary

Databricks table history provides write/version provenance. It does not, by itself, prove which table version an arbitrary job/query consumed.

Exact input-version claims therefore require a qualifying native query/runtime source or DMTZ workload attestation. Where only dependency/Lineage evidence exists, DMTZ may answer that the source was read/reachable but must leave the exact consumed version unresolved.

Likewise, output table-version binding requires exact write/transaction evidence or attestation; timestamp adjacency is not enough.

## Health architecture

Measurements preserve:

**measurement ID + exact target + definition revision + profile/applicability + window/grain + observed values/source status + run/output/version binding where supported + acquisition coverage/lag + derived Assessment link**.

Lakeflow expectation counts, data-quality monitoring results, profiling/drift metrics, job health metrics and organization-owned checks can all contribute without being flattened into one source of truth.

Vendor health/downstream-impact labels remain vendor-owned Assessments. Baseline/anomaly output remains descriptive unless an accepted Expectation/Assessment rule makes it normative.

## Lineage and consumer evidence

Lineage is stored as typed historical edge evidence. Databricks system lineage is valuable but documented as incomplete; missing lineage is therefore not a universal negative.

Where `statement_id` exists, Lineage may join to query history for a stronger query encounter. For non-SQL/native paths, entity/run metadata or workload instrumentation may supply equivalent evidence.

A derived graph projection can accelerate traversal, but the canonical journals remain truth/provenance owners.

## Impact architecture

Impact preserves the Phase 007 chain:

**candidate/reachable → opportunity/availability → encounter → exact affected-version exposure → downstream effect → technical/analytical/business consequence → optional Causal Claim**.

Databricks data-quality monitoring's current downstream-impact field may be retained as a vendor source result, but its dependency/query-derived severity/counts do not become DMTZ realized exposure/effect/consequence, and the field is currently documented for deprecation.

External BI/application display/use and business/customer/financial consequence remain environment-specific integrations when those propositions are in scope.

## Strong negative rule

Before asserting `no run`, `no output`, `no measurement`, `no dependency`, `not exposed`, `no effect` or `no consequence`, the exact proposition must have:

- bounded expected population/path/opportunity;
- sufficient source/runtime/consumer instrumentation;
- complete enough Group 04 collection coverage;
- acceptable source publication lag for the window;
- known integration health;
- proposition-specific negative evidence required by REF/HLTH/OPS.

No single `200 OK`, empty result, healthy job status, safe path, or absent lineage record satisfies this by itself.

## Phase 009 gap treatment

Group 05 materially addresses the architecture side of **GAP-009-04–GAP-009-18**:

- explicit CI/deployment/run correlation and attestation;
- exact source/bundle/content revision strategy;
- composite implementation manifest;
- optional exact multi-input consumption instrumentation;
- consumer compatibility and measurement-definition binding;
- event-time freshness and measurement→run/output provenance;
- durable historical Lineage;
- exact consumer-version/cache/result-state evidence where instrumented;
- external consumer/consequence integration hooks;
- bounded strong multi-hop negative-coverage model.

Not every deployment will support every exact proposition. Group 01 capability profiles and Group 04 health/coverage determine the actual supported surface.

## Technology choices intentionally not made

Group 05 does not select a graph database, tracing vendor, telemetry SDK language, schema-registry product, external BI telemetry product, incident/business system, stream bus, service topology, LLM/retrieval stack, or control implementation.

The canonical record/attestation interfaces are selected. Packaging and serving remain later architecture work.

## Group 06 handoff

Group 06 may now persist and reason over Investigations/Causal Claims and produce historical/current Explanations using exact/partial runtime, health, Lineage, encounter and Impact evidence.

It must preserve missing bindings as missing, retain basis/source/acquisition/authority limitations, and never allow graph traversal or model output to manufacture run/version/exposure/effect/cause facts.
