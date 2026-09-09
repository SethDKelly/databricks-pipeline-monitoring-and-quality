# Pre-Group-02 Schema / DDL Validation Handoff

**Status:** Accepted planning refinement before Phase 005 Group 02

## Consideration

Pipeline health must include structural/schema compatibility, not only execution success and value-level metrics. A source can load successfully while an upstream DDL/schema change makes downstream logic invalid, silently changes metric meaning, invalidates Baseline comparability, breaks key joins, or causes a later consumer failure.

Representative structural changes include:

- column addition/removal;
- column rename or semantic replacement;
- data-type changes, including precision/scale/nested-type changes;
- nullability/default/generated-value changes;
- primary/business-key or identifier-role changes;
- grain changes;
- partitioning/structural metadata changes where semantically relevant;
- nested-field changes;
- table/view replacement or other structural transitions affecting consumers.

## Existing concept ownership

No new Schema concept is required at this point.

- **Semantic Definition** owns governed meaning such as technical description, grain, key/identifier role, field meaning, units, population, and declared schema-contract semantics where applicable.
- **Expectation** owns normative structural compatibility rules such as required/optional columns, accepted types/nullability, allowed additive changes, key requirements, or consumer-specific compatibility conditions.
- **Change Intent** owns planned schema evolution and anticipated downstream/Baseline/metric implications.
- **Observation** owns provenance-bearing evidence of an observed schema state.
- **Change** owns the realized schema transition/difference.
- **Assessment** owns conformance/health interpretation against the applicable structural Expectation/Baseline context.
- **Lineage/Impact/Investigation/Causal Claim** own downstream reachability, exposure/effect, inquiry, and causal propositions when a schema change has consequences.

## Three schema truths that must remain separate

1. **Declared/governed schema meaning** — what an authoritative declaration says the schema/field/key/grain means.
2. **Normative schema contract** — what should be structurally acceptable for a given subject/consumer/context.
3. **Realized schema state** — what schema actually exists at runtime and what changed.

A successful CI check proves only what was checked before deployment. A runtime catalog observation proves what it can observe in the deployed environment. Neither one automatically proves the other.

## Validation horizons

Schema validation can reasonably occur at several horizons without one universal enforcement location:

### Proposed-change / pre-deployment
A source-controlled contract or proposed DDL can be compared with declared schema Expectations and known downstream dependency contracts before deployment. GitHub Actions is a candidate integration point, not a selected architecture.

### Activation / realized-state
Databricks/Unity Catalog or other platform metadata can provide evidence of the schema that actually exists after activation. This can detect unexpected/unregistered changes and differences between planned and realized state.

### Independent monitoring / near-real-time
The monitoring framework can compare realized schema evidence with current Expectations, Baseline comparability, metric-profile applicability, key/join semantics, and downstream Lineage without becoming a production dependency for ungated jobs.

### Retrospective / RCA
Historical schema state can be compared with incident-time Lineage, metrics, Baselines, Deployment, and downstream effects when investigating a failure.

## Compatibility is consumer- and semantics-aware

`Schema changed` does not automatically mean `breaking` and `schema unchanged` does not guarantee semantic compatibility.

Examples:

- adding an optional column may be harmless for one consumer and break a positional/export consumer;
- widening one type may be safe while narrowing precision may be unsafe;
- renaming a field can be breaking even when its replacement has the same type;
- changing a declared business key can invalidate join/reconciliation metrics without changing row count;
- dropping a column unused by one downstream path may be safe there but breaking for another consumer;
- a grain change can invalidate counts, null rates, quantiles, uniqueness expectations, and Baseline comparability even if all column names remain.

## Metrics and Baselines interaction

A structural change should trigger applicability review rather than blindly resetting or preserving metrics/Baselines.

Potential consequences include:

- metric definition no longer resolvable because a field was removed/renamed;
- null/uniqueness/distribution metric comparability broken by type/grain/key change;
- new fields require no metrics unless a governed metric profile says they matter;
- existing Baseline may remain valid for unaffected dimensions while becoming non-comparable for affected dimensions;
- join/reconciliation metrics may require new key/relationship semantics;
- a planned structural change may require prospective Expectation changes while new Baselines still require actual post-change evidence.

## Phase ownership

- **Phase 005 Group 02:** authority for technical schema meaning, grain, key semantics, responsibility, Classification/criticality, and policy context; declared schema meaning vs observed state separation.
- **Phase 005 Group 03:** who may establish/revise/waive schema Expectations, compatibility rules, metric-profile implications, and thresholds.
- **Phase 006:** detailed schema-health/DDL compatibility taxonomy, structural checks, metric/Baseline interaction, severity and result-timing semantics.
- **Phase 007:** planned/realized schema change, prospective downstream blast radius, Lineage-aware compatibility and Investigation behavior.
- **Phase 009:** determine what GitHub/GitHub Actions, Databricks/Unity Catalog, repositories, and other sources can actually prove; availability, latency, retention, and authority contracts.
- **Phase 010:** choose where proactive/runtime validations execute and how CI/platform/monitoring paths compose technically.

## Architectural constraint

Do not choose one universal validation point now. A robust future design may use both proactive CI validation and out-of-band runtime monitoring because they answer different temporal questions. Passive runtime monitoring remains non-blocking by default; any schema check used in an Execution Gate becomes explicit active-control evidence with stronger availability semantics.
