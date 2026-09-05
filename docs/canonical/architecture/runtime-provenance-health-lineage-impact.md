# Runtime Provenance, Health, Lineage & Impact Evidence Architecture

**Canonical key:** `architecture.runtime_health_lineage_impact`

**Kind:** TECHNICAL ARCHITECTURE CONTRACT

**Authority:** CANDIDATE / NOT CURRENT AUTHORITY

**Migration records:** `stable_family.ARCH`, `architecture.runtime_health_lineage_impact`

**Stable IDs:** ARCH-191–ARCH-274

**Owns current question after cutover:** How are exact/partial runtime provenance, consumed/produced versions, measurements, typed historical Lineage, consumer encounter, exposure, effect and consequence represented?

## Canonical contract

The evidence chain is:

**source-owned runtime facts + deployment/run attestation where required → exact/partial implementation and input/output manifests → source-owned measurements + governed health derivation → typed historical Lineage → actual consumer encounter/version state → bounded exposure → separately evidenced effect → separately evidenced consequence → causal/reasoning handoff**.

No stage automatically creates the next.

Canonical record families include runtime provenance journals; exact/partial input/output manifests; measurement/Assessment journals; Lineage and encounter journals; and Impact journals. All retain source/acquisition provenance, material time coordinates, identity, authority/disclosure context and collection coverage/health constraints.

## Stable contracts

### Runtime/change/deployment — ARCH-191–ARCH-216

`ARCH-191` Runtime Evidence Envelope; `ARCH-192` Run Identity; `ARCH-193` Task-Run Identity; `ARCH-194` Retry / Repair Attempt Identity; `ARCH-195` Git Revision Identity; `ARCH-196` Change Intent Correlation; `ARCH-197` GitHub Workflow-Run Identity; `ARCH-198` GitHub Deployment Identity; `ARCH-199` Cross-System Correlation Token; `ARCH-200` Correlation Attestation; `ARCH-201` Correlation Status & Conflict; `ARCH-202` Direct-Git `used_commit` Binding; `ARCH-203` Workspace-Source Provenance Limitation; `ARCH-204` Bundle Deployment Revision Manifest; `ARCH-205` Workspace Content Attestation; `ARCH-206` Deployment Activation Record; `ARCH-207` Run-Specific Implementation Manifest; `ARCH-208` Code-Facet Binding; `ARCH-209` Job / Task Configuration Revision Binding; `ARCH-210` Parameter Binding; `ARCH-211` Runtime / Compute Binding; `ARCH-212` Library / Dependency Binding; `ARCH-213` Environment / Feature Binding; `ARCH-214` External Configuration Reference; `ARCH-215` Incomplete Implementation State; `ARCH-216` Trigger / Parent-Child Binding.

### Input/output/current-cycle — ARCH-217–ARCH-229

`ARCH-217` Input Consumption Manifest; `ARCH-218` Exact Table-Version Consumption; `ARCH-219` File / Object Input Version; `ARCH-220` Stream Offset / Checkpoint Input; `ARCH-221` Multi-Input Consumption Manifest; `ARCH-222` Input-Manifest Completeness; `ARCH-223` Current / Latest Input Rejection; `ARCH-224` Output Production Manifest; `ARCH-225` Output Table-Version Binding; `ARCH-226` Output File / Object Binding; `ARCH-227` Output Non-Existence Burden; `ARCH-228` Current-Cycle Alignment; `ARCH-229` Runtime Binding Conflict.

### Health/measurement — ARCH-230–ARCH-246

`ARCH-230` Measurement Identity; `ARCH-231` Measurement Target Binding; `ARCH-232` Measurement Definition Revision; `ARCH-233` Health-Profile Revision; `ARCH-234` Measurement Window & Grain; `ARCH-235` Measurement → Run Attribution; `ARCH-236` Measurement → Output-Version Attribution; `ARCH-237` Event-Time Freshness Evidence; `ARCH-238` Ingestion / Processing Latency Evidence; `ARCH-239` Completeness / Volume Observation; `ARCH-240` Structural / Compatibility Observation; `ARCH-241` Data-Quality Expectation Observation; `ARCH-242` Baseline / Typicality Observation; `ARCH-243` Reconciliation Observation; `ARCH-244` Health-Assessment Composition; `ARCH-245` Health Conflict Preservation; `ARCH-246` Health Negative-Coverage Requirement.

### Lineage/encounter — ARCH-247–ARCH-259

`ARCH-247` Lineage Edge Identity; `ARCH-248` Lineage Relationship Type; `ARCH-249` Lineage Temporal Binding; `ARCH-250` Lineage Acquisition Provenance; `ARCH-251` Lineage Coverage & Inference Limitation; `ARCH-252` Lineage Identity Continuity; `ARCH-253` Statement / Query Encounter Join; `ARCH-254` Direct vs Indirect Lineage; `ARCH-255` Lineage Does Not Equal Consumption; `ARCH-256` Consumer Encounter Identity; `ARCH-257` Consumer Use Context; `ARCH-258` Cache / Materialization / Result State; `ARCH-259` Exact Consumed / Affected Version.

### Impact — ARCH-260–ARCH-274

`ARCH-260` Exposure State; `ARCH-261` Multi-Hop Exposure Path; `ARCH-262` Alternate-Path Coverage; `ARCH-263` Downstream Effect Record; `ARCH-264` Technical Effect; `ARCH-265` Analytical / Decision Effect; `ARCH-266` Business / Customer / Financial Consequence; `ARCH-267` Impact Evidence Boundary; `ARCH-268` Effect / Consequence Does Not Establish Cause; `ARCH-269` Strong Non-Exposure Coverage; `ARCH-270` No-Effect / No-Consequence Coverage; `ARCH-271` Partial / Unknown Impact; `ARCH-272` Historical Impact Replay; `ARCH-273` Derived Operational Graph Projection; `ARCH-274` Group 05 Handoff Readiness.

## Runtime attestation and version boundary

Use native evidence first, selective attestation second, unknown otherwise. Qualifying direct-Git runs may expose strong run-owned commit evidence; bundle/workspace-source patterns require framework deployment manifests or run-start attestation when exact reproducibility is promised.

Table history proves writes/version history but does not by itself prove the exact version an arbitrary run consumed. Exact input/output-version claims require qualifying native evidence or explicit workload attestation. Names and timestamp adjacency are not sufficient.

## Health, Lineage and Impact

Measurements bind exact target, definition/profile revision, window/grain, source state and run/output/version where supported. Vendor health/impact labels remain vendor-owned Assessments; Baseline/anomaly output is descriptive unless a governing normative rule applies.

Lineage is typed historical edge evidence. Missing Lineage does not prove no dependency. Query/statement identity can strengthen encounter evidence; graph projections accelerate traversal but remain rebuildable.

Impact preserves:

**candidate/reachable → opportunity/availability → encounter → exact affected-version exposure → downstream effect → technical/analytical/business consequence → optional Causal Claim**.

Effect/consequence does not establish cause.

## Strong negative rule

`no run`, `no output`, `no measurement`, `no dependency`, `not exposed`, `no effect` and `no consequence` require bounded expected opportunity/population/path, sufficient source/runtime/consumer instrumentation, adequate acquisition coverage, compatible source lag, known integration health and the proposition-specific REF/HLTH/OPS burden.

## Architecture boundary

This segment selects canonical record/attestation interfaces but not a graph database, tracing vendor, telemetry language, external BI telemetry product, incident/business system, stream bus, service topology, model/retrieval stack or active-control implementation.

## Provenance

- `docs/concepts/phase_010/05_runtime_provenance_health_lineage_impact_evidence_architecture/README.md`
- atomic ARCH-191–ARCH-274 files under that Phase 010 group
- Phase 010 decisions D-1433–D-1490 and RHI05-01–RHI05-108 review evidence
