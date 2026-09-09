# Phase 006 Group 02 — Structural / Schema / DDL Compatibility Scenario Review

All scenarios are synthetic and test functional semantics rather than Databricks/GitHub implementation.

| ID | Scenario | Expected reasoning | Result |
|---|---|---|---|
| H02-01 | Producer adds optional field; Spark consumer selects named columns | Addition can be compatible for that consumer when unknown fields are tolerated | **PASS** |
| H02-02 | Same addition feeds a positional fixed-column export | Same producer change can be incompatible for the export contract | **PASS** |
| H02-03 | Producer removes an optional field unused by Consumer C | Removal can be compatible for C when contract does not require/depend on it | **PASS** |
| H02-04 | Producer removes required field used by Consumer D | Sufficient realized-state evidence supports structural incompatibility for D | **PASS** |
| H02-05 | `customer_id` disappears and `customer_identifier` appears with no mapping | Record drop + add; do not infer rename identity | **PASS** |
| H02-06 | Same transition has an authoritative migration mapping preserving field identity | Rename can be represented and evaluated against consumer contracts | **PASS** |
| H02-07 | Field name remains `amount` but meaning changes from transaction amount to account balance | Same name does not preserve semantic identity/metric continuity | **PASS** |
| H02-08 | INT → BIGINT and consumer contract explicitly accepts the wider representation | Compatible for that bound contract when evidence shows transition | **PASS** |
| H02-09 | INT → BIGINT but external fixed-width contract rejects larger representation | Engine cast support does not override consumer incompatibility | **PASS** |
| H02-10 | BIGINT → INT and current values happen to fit | Observed representability does not rewrite a contract that prohibits narrowing | **PASS** |
| H02-11 | DECIMAL(18,2) → DECIMAL(22,4) | Precision/scale transition is independently material and consumer-specific | **PASS** |
| H02-12 | Nested optional field added; tolerant reader versus strict schema reader | Same nested change can be compatible and incompatible for different consumers | **PASS** |
| H02-13 | NOT NULL → nullable but current run contains no nulls | Current data does not preserve the structural non-null guarantee required by contract | **PASS** |
| H02-14 | Required field becomes nullable with default `UNKNOWN` | Physical non-null output can coexist with incompatibility of business presence semantics | **PASS** |
| H02-15 | Column list/types unchanged; grain changes account → account/day | Structural change is material and triggers scoped metric/Baseline review | **PASS** |
| H02-16 | Composite key gains `business_date` | Old uniqueness/join assumptions require review; key-role change does not itself prove quality failure | **PASS** |
| H02-17 | Fields reordered | Name-based consumer may remain compatible; positional consumer may not | **PASS** |
| H02-18 | Backing table changes but stable view preserves prior interface | Evaluate the view/interface consumed; physical-table change does not prove consumer breakage | **PASS** |
| H02-19 | Producer schema unchanged but consumer upgrades to stricter contract | Compatibility can change because consumer contract/version changed | **PASS** |
| H02-20 | CI validates proposed schema successfully; deployment realizes a different partial schema | Prospective result remains scoped to proposal; realized state requires new Observation/Assessment | **PASS** |
| H02-21 | Runtime catalog shows an unplanned column removal | Realized Change does not imply Change Intent/approval; evaluate compatibility separately | **PASS** |
| H02-22 | Diff tool reports no change but nested-field coverage was incomplete | Insufficient coverage cannot justify `compatible` | **PASS** |
| H02-23 | Required schema source is unavailable | Result remains unavailable/unknown, not compatible | **PASS** |
| H02-24 | Structural incompatibility is proven; downstream job has not yet run | Incompatibility does not prove execution failure, exposure, Impact, or causality | **PASS** |
| H02-25 | Type/grain change affects distributions/uniqueness but not execution duration | Trigger scoped metric/Baseline review rather than global reset | **PASS** |
| H02-26 | New optional field appears | Do not automatically add null/cardinality/quantile metrics to routine profile | **PASS** |
| H02-27 | Table clustering/physical layout changes while consumer logical contract is unchanged | Do not call it schema incompatibility unless the relevant interface/consumer contract depends on that property | **PASS** |
| H02-28 | All known consumers passed prospective review; later a previously unknown strict consumer is discovered | Current blast-radius understanding can expand; historical prospective result remains valid only for its known bounded consumer set | **PASS** |
| H02-29 | Two applicable structural contract versions conflict for the same consumer/time | Preserve conflict until authority resolution; do not choose newest/strictest by convenience | **PASS** |
| H02-30 | A schema incompatibility is temporarily waived | Underlying incompatibility remains; waiver response semantics belong to Group 04 | **PASS** |

## Review result

**H02-01–H02-30 pass.**

The existing concepts remain sufficient. Group 02 requires no new Schema, Schema Contract, Schema Version, or Compatibility concept. Structural declarations synchronize with Semantic Definition/Entity Identity and Expectations; realized facts are Observation/Change; compatibility conclusions are Assessment. `HLTH-009–HLTH-018` refine how those existing truths compose.

No validation placement is selected. GitHub Actions, Databricks/Unity Catalog, DQX, Metric Views, and an independent monitoring application remain candidate evidence/evaluation locations for later phases.