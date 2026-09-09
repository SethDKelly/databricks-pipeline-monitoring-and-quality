# Phase 005 Group 02 — Semantic, Responsibility, Classification, Policy & Criticality Governance

**Status:** Accepted — AUTH-009–AUTH-015

## Goal

Apply the accepted Assertion Authority concept and AUTH-001–AUTH-008 to descriptive/governance state without conflating governance authority with normative health authority, Capability Authorization, evidence sufficiency, production-control authority, or Phase 006 metric/statistical behavior.

## Accepted pre-Group-02 schema/DDL handoff

[`../pre_group_02_schema_ddl_validation_handoff.md`](../pre_group_02_schema_ddl_validation_handoff.md) records schema/DDL compatibility as a first-class future validation concern.

The accepted ownership split is:

- governed schema meaning / grain / key roles → **Semantic Definition**;
- structural/schema compatibility requirements → **Expectation**;
- observed schema state → **Observation**;
- realized structural transition → **Change**;
- planned schema evolution → **Change Intent**;
- schema-health/conformance conclusion → **Assessment**;
- downstream reachability/effect → **Lineage / Impact / Investigation / Causal Claim** as applicable.

Group 02 governs who/what is authoritative for the descriptive schema/semantic assertions. It does not define schema-health checks or choose whether they run in GitHub Actions, Unity Catalog/Databricks, or the monitoring application.

## Accepted handoff from Group 01

- authority is bound to category/facet/scheme/type, subject scope, context, effective time, and knowledge time where relevant;
- source assertions remain provenance-bearing regardless of standing;
- authoritative, advisory, explicitly non-authoritative, conditional, unknown, unavailable, authoritative-conflict, and authority-rule-conflict states remain distinct;
- source count, recency, availability, ingestion order, repository ownership, organizational title, responsibility, and apparent specificity do not create precedence;
- co-authoritative disagreements remain authoritative conflict unless an explicit resolver applies;
- fallback authority requires an explicit rule and evidenced activation condition;
- authority-rule provenance/governing basis is required;
- prospective authority changes and later corrections preserve historical/as-known behavior;
- Assertion Authority does not waive Phase 004 evidence burdens or grant Capability Authorization.

## Accepted contracts

### AUTH-009 — Semantic Facet and Schema-Meaning Authority
Authority resolves independently for business definition, technical description/schema declaration, grain, units, populations, calculation meaning, column/field roles, key/identifier roles, and related semantic facets. Declared schema meaning remains separate from normative schema Expectations and realized schema Observation/Change.

### AUTH-010 — Responsibility-Type Authority and Assignment Governance
Technical owner, business accountable party, steward, security/privacy responsibility, operational responsibility, and platform responsibility are independently governed assignment types. Responsibility does not grant semantic, policy, access, metric, gate, safeguard, or confirmation authority.

### AUTH-011 — Classification-Scheme and Criticality Authority
Classification authority is scheme/context specific. Business/operational/client-delivery criticality remains Classification under named schemes/contexts; it influences prioritization but does not prove actual Impact or health.

### AUTH-012 — Policy-Context Applicability Authority
Authority over a policy reference/text and authority to assert its applicability to a subject/context may be separate. Classification can support policy applicability but does not determine it; Policy Context remains separate from access, enforcement, compliance, and legal interpretation.

### AUTH-013 — Contextual Overrides, Local Governance, and Cross-Facet Conflict
Context-specific assertions may legitimately coexist. Narrower scope does not automatically override broader scope. Real conflict requires disagreement for the same bound target/context/time with applicable standing.

### AUTH-014 — Derived, Inherited, and Propagated Governance Assertions
Lineage, repository/container membership, schema/tag inference, or parent governance state does not silently propagate semantics, responsibility, classification, policy, criticality, or authority. Derived/inherited assertions retain provenance and need explicit standing.

### AUTH-015 — Governance State Separation from Normative Health and Operational Truth
Descriptive governance authority cannot become schema-health, data-quality, Impact, Capability Authorization, control-enforcement, or compliance truth. Schema validation composes governed meaning + normative Expectation + realized evidence + Assessment.

## Schema/DDL implications accepted in Group 02

The group explicitly preserves:

**declared/governed schema meaning ≠ normative schema contract ≠ realized schema state**.

Examples:

- a Git-managed schema contract can be authoritative for a declaration without proving what was deployed;
- Unity Catalog/Databricks metadata can evidence realized schema without automatically becoming authoritative business meaning;
- a monitoring application can assess realized conformance without becoming the semantic authority;
- a declared primary/business key does not prove uniqueness;
- a rename cannot be inferred merely from one dropped and one added column;
- schema changes can trigger scoped metric/Baseline/key/join applicability review rather than global reset.

The technical placement of proactive/runtime checks remains Phase 009/010 work.

## Criticality treatment

No separate Criticality concept is required. The existing Classification concept already supports criticality labels under named vocabularies. The project can therefore represent business, operational, consumer, or delivery criticality as distinct schemes/contexts while preserving:

**criticality ≠ exposure ≠ effect ≠ consequence ≠ cause**.

## Scenario result

[`scenario_checks.md`](scenario_checks.md) passes semantic/schema authority, responsibility conflicts, classification/criticality schemes, policy applicability, local overrides, inherited/derived governance, actual-schema mismatch, key-integrity disagreement, and historical-governance cases.

No 25th concept is required.

## Exit decision

**Accepted. Phase 005 Group 02 is complete with AUTH-009–AUTH-015. Group 03 — Normative Health, Metric & Threshold Governance is next and has not started.**

Group 03 must include authority for schema/DDL Expectations, compatibility rules, metric-profile implications, thresholds/margins, and temporary exceptions while leaving detailed schema-health/metric computation to Phase 006.
