# Phase 009 Group 05 — Lineage, Consumer Use, Exposure, Effect & Impact Evidence

**Status:** Review complete — accepted

## Result

Group 05 accepts **INTG-120–INTG-153** and **LIE05-01–LIE05-60**. No new product concept is required.

The group maps Unity Catalog lineage, Databricks query history, dashboard/audit activity, caching, refresh/snapshot delivery and external-client evidence onto the accepted Lineage/Impact model without turning topology or platform activity into a universal `affected` state.

The central evidence chain is:

**bounded originating state → effective/candidate Lineage → encounter opportunity + availability/publication → observed consumer-mode encounter → exact state/version binding where available → bounded exposure → downstream effect evidence → consequence evidence → optional Causal Claim attribution**.

No link automatically creates the next.

## Accepted contracts

1. **INTG-120** — Unity Catalog Table-Lineage Event Surface
2. **INTG-121** — Unity Catalog Column-Lineage Grain
3. **INTG-122** — Lineage Event vs Effective Relationship
4. **INTG-123** — `direct_access` & Intermediate Dependency Semantics
5. **INTG-124** — Lineage Entity Metadata & Consumer Identity
6. **INTG-125** — Lineage History & Retention Surface Split
7. **INTG-126** — Lineage Rename & Identity-Continuity Gap
8. **INTG-127** — Path/Table Identity in Lineage
9. **INTG-128** — Lineage Capture Coverage & Negative Boundary
10. **INTG-129** — Publication / Availability State Evidence
11. **INTG-130** — Query-History Statement Encounter
12. **INTG-131** — Lineage `statement_id` ↔ Query-History Join
13. **INTG-132** — Query Source, Client Application & Consumer Context
14. **INTG-133** — Query Result Cache Encounter
15. **INTG-134** — Dashboard Query Execution & Result Receipt
16. **INTG-135** — Dashboard Access vs Dataset Encounter
17. **INTG-136** — Dashboard Cache & Safe/Stale State
18. **INTG-137** — Dashboard Schedule, Snapshot & Subscription Encounter
19. **INTG-138** — External BI Query vs Report Use
20. **INTG-139** — JDBC/API/Application Read Encounter
21. **INTG-140** — Job/Notebook Run Consumption
22. **INTG-141** — Exact Table-Version Consumption Gap
23. **INTG-142** — Explicit Time-Travel / Version-Read Evidence
24. **INTG-143** — Refresh / Materialization Consumption Evidence
25. **INTG-144** — Copy, Export, Cache & Snapshot Alternate-State Evidence
26. **INTG-145** — Multi-Hop Exposure Is Non-Transitive
27. **INTG-146** — Alternate Paths & Population Coverage
28. **INTG-147** — Positive Exposure Evidence Contract
29. **INTG-148** — Non-Exposure Negative Claim Coverage
30. **INTG-149** — Downstream Effect Evidence Binding
31. **INTG-150** — Technical, Analytical & Business Consequence Sources
32. **INTG-151** — View / Delivery / Decision-Reliance Boundary
33. **INTG-152** — Vendor Impact/Popularity Context ≠ Realized Impact
34. **INTG-153** — Group 05 Source Matrix & Group 06 Handoff

## Lineage evidence

Unity Catalog table/column lineage is a valuable event/topology source, including read/write events from jobs, notebooks, pipelines, SQL queries, dashboards, Genie and alerts when lineage can be inferred. It remains incomplete by documented design.

Preserve:

**captured lineage event ≠ continuously effective relationship ≠ encounter opportunity ≠ actual encounter ≠ suspect-state exposure**.

`direct_access` describes whether a source was directly referenced versus discovered through an intermediate dependency; it is not a relevance, causal-strength or exposure-strength score.

System-table lineage retains a rolling one-year window, while Catalog Explorer/lineage API retain captured lineage after 2024-09-01 beyond that window. The surfaces are complementary, not identical historical ledgers.

Lineage continuity also has material limitations around renames, path-based access, UDFs, RDDs/checkpointing and some pipeline/run patterns. Missing lineage is therefore not a strong negative.

## Query/read encounter

The most useful concrete association is the documented SQL-warehouse join:

**`system.access.table_lineage.statement_id` → `system.query.history.statement_id`**.

This can bind a captured source read to the exact SQL statement and then add executed-by/executed-as principal, client application, query source, timing, status and read metrics.

That is strong evidence for a bounded platform read. It still does not universally expose the exact Delta/table version consumed.

The correct vocabulary can therefore include:

- encounter established, exact affected version established;
- encounter established, exact state/version unresolved;
- safe/other-state encounter established;
- no relevant encounter opportunity;
- encounter unresolved due coverage/source limitations.

## Dashboard evidence and cache semantics

Databricks dashboard audit evidence separates several propositions:

- `getDashboard` / `getPublishedDashboard` — dashboard definition/view access;
- `executeQuery` — query execution from the dashboard;
- `getQueryResult` — query-result receipt;
- snapshot generation/delivery — exported/scheduled encounter paths.

These must not be collapsed.

Dashboard caching makes the distinction operationally material. AI/BI dashboards can serve cached results up to 24 hours old without executing a fresh warehouse query, and underlying-data changes do not automatically invalidate dashboard cache. A dashboard viewer can therefore see safe stale state, affected cached state or an unresolved cached state.

A dashboard view does not prove that every dataset executed or that the viewer saw the current source state. A scheduled refresh does not prove a later human view. A sent snapshot proves delivery to a destination/recipient where evidenced, not reading or decision reliance.

## External BI / applications

Queries routed through covered Databricks SQL compute can expose client-application context such as Tableau or Power BI and can establish a platform read when joined to lineage.

This does not prove an external BI report was viewed, which visualization displayed the result, that an application processed/fetched it successfully, or that a human/business process relied on it. Those propositions require the relevant external/app/business telemetry when material.

## Exact state/version exposure

Group 05 carries forward Group 03's run-specific input-version problem into consumer exposure.

Generic lineage and query-history records establish objects/statements but do not universally emit the exact Delta/table version read. Exact suspect-state exposure is therefore **unsupported out of the generic source pair / conditional** on explicit version/time-travel selection, retained statement/parameter semantics, run-specific input evidence, snapshot/cache identity or another state attestation.

A source read at 10:03 cannot simply be assigned the latest table version that existed near 10:03.

## Multi-hop, caches and alternate paths

Exposure remains non-transitive. A→B and B→C topology does not prove C saw A's suspect state.

Cache, copy, extract, snapshot, materialized state and export are explicit alternate-state encounter paths. A consumer can remain safely on V-1 after V is affected, or remain exposed through a copied V after the producer has been repaired.

One safe path cannot establish global non-exposure where another material path is unresolved.

## Downstream effect and consequence

Group 04 Observations/Assessments can establish downstream technical/analytical effect only when bound to the exact consumer/output/dimension/window. Exposure can exist without observed degradation; downstream degradation can exist while originating-state exposure remains unresolved.

Technical, analytical and business consequences require progressively different sources. Databricks runtime/query/quality evidence may support technical consequences; analytical consequences may require output/report/model comparisons; business/customer consequences generally require business-process/application/decision/ticket/financial evidence.

**view/delivery ≠ comprehension ≠ decision reliance ≠ changed action ≠ consequence**.

Any assertion that the originating condition caused/contributed to/enabled/triggered/prevented/materially influenced an effect or consequence is handed to Causal Claim.

## Vendor impact/usage context

Catalog lineage impact-analysis views, table insights/popularity and Databricks anomaly-monitoring downstream-impact fields can prioritize candidates and supply query-activity/context evidence.

They do not substitute for actual version-bound exposure, downstream effect, consequence, causal attribution or a universal severity/Impact score.

## Historical replay and strong negatives

Historical Impact reconstruction composes source windows rather than assuming one ledger. Lineage system tables, query history and audit tables generally expose bounded retention; Catalog lineage history has a different longer surface; external BI/application/business-use evidence may have entirely separate retention.

`not exposed`, `no effect` and `no consequence` retain their accepted proposition-specific negative burdens. Missing query history, incomplete lineage, permission filtering, external-client blind spots, unknown cache state or missing business records remain limitations.

## Artifacts

- [`source_capability_matrix.md`](source_capability_matrix.md) — proposition-specific support and residual gaps.
- [`external_source_review.md`](external_source_review.md) — current public documentation verified on 2026-08-25.
- [`scenario_review.md`](scenario_review.md) — LIE05-01–LIE05-60 pass.
- [`../../../decisions/phase_009_group_05_lineage_consumer_impact_sources.md`](../../../decisions/phase_009_group_05_lineage_consumer_impact_sources.md) — D-1072–D-1118.

## Architecture boundary

Group 05 does not choose lineage ingestion/storage, query parsing, cache/version attestation, BI connectors, application telemetry, business-event integration, graph traversal implementation, Impact scoring, event streaming/polling, or UI. Phase 010 owns technical realization.

## Handoff

**Group 06 — Investigation, Causality, Safeguard, Gate & Control Evidence is next.**

Group 06 may consume Group 05 lineage/encounter/exposure/effect/consequence evidence only with its path/version/population/time/coverage/authorization limitations. Topology, query activity, exposure, effect, consequence, priority or temporal proximity do not establish Causal Claim status or control effectiveness.
