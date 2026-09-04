# Lineage, Consumer Use, Exposure, Effect & Impact Evidence

**Canonical key:** `integration.group-05`

**Kind:** INTEGRATION CONTRACT

**Authority:** CANDIDATE / NOT CURRENT AUTHORITY

**Migration record:** `stable_family.INTG`

**Stable IDs:** INTG-120–INTG-153

**Owns current question:** What can lineage, query, dashboard, cache, external-client and business evidence establish about topology, actual encounter, exact-state exposure, downstream effect and consequence?

## Canonical source findings

Preserve the encounter ladder:

**bounded originating state → effective/candidate Lineage → encounter opportunity + publication/availability → observed consumer-mode encounter → exact state/version binding where available → exposure → downstream effect → consequence → optional Causal Claim attribution**.

Captured lineage event ≠ continuously effective relationship ≠ encounter opportunity ≠ encounter ≠ suspect-state exposure. `direct_access` is relationship context, not exposure/causal strength. Query history can establish bounded reads but not universally the exact Delta/table version. Dashboard access ≠ dataset query execution ≠ query-result receipt; cache/snapshot paths can expose safe stale, affected or unresolved alternate state. External BI/platform query ≠ report view ≠ human/business reliance.

Exposure is non-transitive across multi-hop topology. One safe path cannot establish global non-exposure. View/delivery ≠ comprehension ≠ decision reliance ≠ changed action ≠ consequence. Vendor popularity/impact views are prioritization/context evidence only.

## Stable contracts

### INTG-120 — Unity Catalog Table-Lineage Event Surface
Use captured table-lineage events as relationship/event evidence within documented capture scope; they do not prove a permanent continuously effective relationship.

### INTG-121 — Unity Catalog Column-Lineage Grain
Column-level lineage may narrow field relevance where captured, but it retains source capture/identity/history limits and does not establish consumer exposure by itself.

### INTG-122 — Lineage Event vs Effective Relationship
A captured read/write relationship event and an effective topology relationship are different propositions; neither automatically implies encounter opportunity or exposure.

### INTG-123 — `direct_access` & Intermediate Dependency Semantics
`direct_access` distinguishes direct reference from intermediate discovery; it is not a relevance, causal-strength, exposure-strength or Impact score.

### INTG-124 — Lineage Entity Metadata & Consumer Identity
Bind lineage entities/consumers using explicit metadata and Entity Identity rules; names or client labels alone cannot establish ecosystem consumer identity.

### INTG-125 — Lineage History & Retention Surface Split
System-table, API/catalog and other lineage surfaces have different history windows and semantics; they are complementary rather than one historical ledger.

### INTG-126 — Lineage Rename & Identity-Continuity Gap
Rename/path/recreate continuity requires stable identifiers or governed reconciliation; missing continuity remains an identity/history gap.

### INTG-127 — Path/Table Identity in Lineage
Path-based and table/object identity require explicit reconciliation where both can represent the same or changing data surface; path equality is not universal object identity.

### INTG-128 — Lineage Capture Coverage & Negative Boundary
Missing lineage cannot establish no dependency/relationship/encounter when lineage capture, supported workloads, permissions, history or source health are incomplete.

### INTG-129 — Publication / Availability State Evidence
Publication/availability determines whether a state could be encountered through a path; availability alone does not prove any consumer actually encountered it.

### INTG-130 — Query-History Statement Encounter
A qualifying query-history record can establish a bounded platform query/read encounter for the exact statement/principal/context within source coverage.

### INTG-131 — Lineage `statement_id` ↔ Query-History Join
Use documented `statement_id` joins where available to bind captured lineage to exact SQL statement execution/context; preserve missing/unsupported join cases.

### INTG-132 — Query Source, Client Application & Consumer Context
Client/query-source metadata supplies bounded consumer-mode context but does not prove external report view, application processing success or human/business reliance.

### INTG-133 — Query Result Cache Encounter
Cached result delivery is an alternate-state encounter path and may represent safe stale, affected or unresolved state independently of current source data.

### INTG-134 — Dashboard Query Execution & Result Receipt
Separate dashboard-triggered query execution from query-result receipt; each is a different encounter stage and neither is equivalent to dashboard definition access.

### INTG-135 — Dashboard Access vs Dataset Encounter
Dashboard access/view evidence does not prove that every underlying dataset executed, refreshed or was seen in its current state.

### INTG-136 — Dashboard Cache & Safe/Stale State
Dashboard caching can preserve prior safe or affected state after producer changes; cache state must be resolved explicitly before exposure conclusions.

### INTG-137 — Dashboard Schedule, Snapshot & Subscription Encounter
Scheduled refresh/snapshot/subscription evidence can establish generation/delivery where evidenced; delivery does not prove human reading or decision reliance.

### INTG-138 — External BI Query vs Report Use
A covered platform query from BI tooling is not proof that an external report/visualization was viewed or used; external telemetry is required when that proposition matters.

### INTG-139 — JDBC/API/Application Read Encounter
JDBC/API/application read evidence can establish a bounded platform read but does not automatically prove downstream application processing, presentation or reliance.

### INTG-140 — Job/Notebook Run Consumption
Run/notebook source evidence can establish consumption only where exact input/source association is evidenced; execution itself is not input-version proof.

### INTG-141 — Exact Table-Version Consumption Gap
Generic lineage/query-history sources do not universally emit the exact Delta/table version consumed; exact suspect-state exposure remains conditional where version binding is absent.

### INTG-142 — Explicit Time-Travel / Version-Read Evidence
Explicit version/time-travel selection can strongly bind an exact state when retained statement/parameter/source semantics and execution identity support it.

### INTG-143 — Refresh / Materialization Consumption Evidence
Refresh/materialization creates an alternate consumption/state boundary; later consumer exposure may be to that materialized state rather than current upstream state.

### INTG-144 — Copy, Export, Cache & Snapshot Alternate-State Evidence
Copies, exports, extracts, caches and snapshots are explicit alternate-state paths that can remain safe or affected independently of repaired/current producer state.

### INTG-145 — Multi-Hop Exposure Is Non-Transitive
A→B and B→C topology/encounters do not automatically prove C encountered A's suspect state; each hop/state transition requires its own evidence.

### INTG-146 — Alternate Paths & Population Coverage
Exposure/non-exposure claims bind the actual consumer population and material paths; one observed safe or protected path cannot close unresolved alternate paths.

### INTG-147 — Positive Exposure Evidence Contract
Positive exposure requires a bounded consumer/path encounter plus reliable binding to the suspect state/version or equivalent affected-state evidence.

### INTG-148 — Non-Exposure Negative Claim Coverage
`Not exposed` requires bounded encounter opportunity/population/path/window, sufficient source/query coverage and source health; missing telemetry is not non-exposure.

### INTG-149 — Downstream Effect Evidence Binding
Downstream technical/analytical effect evidence must bind the exact consumer/output/dimension/window and remains distinct from exposure and consequence.

### INTG-150 — Technical, Analytical & Business Consequence Sources
Technical, analytical and business consequences require progressively different source families; platform runtime/quality evidence cannot by itself prove business/customer consequence.

### INTG-151 — View / Delivery / Decision-Reliance Boundary
Preserve **view/delivery ≠ comprehension ≠ decision reliance ≠ changed action ≠ consequence** and require evidence appropriate to the requested layer.

### INTG-152 — Vendor Impact/Popularity Context ≠ Realized Impact
Vendor impact-analysis/popularity/downstream labels can prioritize candidates or provide context but do not establish version-bound exposure, realized consequence, causal attribution or universal severity.

### INTG-153 — Group 05 Source Matrix & Group 06 Handoff
Pass lineage/encounter/exposure/effect/consequence evidence forward only with path/version/population/time/coverage/authorization limits; none of these layers automatically establishes Causal Claim or control effectiveness.

## Architecture boundary

This contract selects no lineage ingestion/storage, query parsing, cache/version attestation, BI connectors, application/business telemetry, graph traversal implementation, Impact scoring, event streaming/polling or UI.

## Provenance

- `docs/concepts/phase_009/05_lineage_consumer_use_exposure_impact_evidence/README.md`
- Phase 009 Group 05 accepted INTG-120–INTG-153.
