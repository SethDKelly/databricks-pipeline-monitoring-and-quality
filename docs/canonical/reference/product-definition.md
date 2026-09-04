# Product Definition

**Canonical key:** `foundation.product_definition`

**Kind:** REFERENCE

**Authority:** CANDIDATE / NOT CURRENT AUTHORITY

**Migration record:** `foundation.product_definition`

**Owns current question:** What is DMTZ for, what outcome should it provide, and what is it explicitly not?

**Stable IDs:** N/A

## Current semantics

Databricks Pipeline Monitoring and Quality (DMTZ) exists to make a distributed data-pipeline ecosystem **understandable over time**.

The product connects operational state, freshness, data quality, typed temporal Lineage, deployment and execution history, governance, semantics, responsibility, policy/authorization context, Investigation, causal evidence, downstream Impact, and Explanation so a user can move from a symptom or business question to an evidence-grounded answer without manually reconstructing the ecosystem from many tools and repositories.

DMTZ treats pipeline execution facts as necessary but insufficient for data trust. A successful job may still publish late, produce stale data, violate quality expectations, expose an unintended version, or coincide with a later downstream effect. The system therefore preserves the distinction between execution, data state, interpretation, causality, Impact, authorization, and communication.

## Product outcome

For an applicable engineering or business question, DMTZ should be able to provide the narrowest trustworthy answer supported by current authorized evidence, including as relevant:

1. current state;
2. relevant historical/as-known comparison;
3. applicable Expectations and Baselines;
4. upstream conditions and candidate explanations;
5. downstream reachability, exposure, observed effect, and consequence evidence without collapsing them;
6. relevant Responsibility Assignments, semantics, classification/policy context, and authority limits;
7. deployment, execution, code/configuration, and Lineage context for the relevant time window;
8. evidence/basis for each material statement;
9. explicit uncertainty, conflict, incompleteness, restriction, or unavailable evidence;
10. an appropriate investigative or operational handoff without silently taking unsafe remediation action.

## Capability families

DMTZ combines independently motivated concepts and contracts across these product capabilities:

1. **Ecosystem understanding** — represent logical pipelines, repositories, runtime entities, data assets, dependencies, consumers, and their identities without making any one implementation boundary the reasoning boundary.
2. **Operational health** — reason about expected execution, actual runs, timing, duration, completion, and runtime context.
3. **Freshness and staleness** — distinguish observed currency from normative staleness Assessment.
4. **Data quality** — preserve Expectations, Baselines, Observations, and Assessments across relevant quality dimensions.
5. **Change and temporal reasoning** — distinguish intended change, Deployment, realized Change, and historical/as-known state.
6. **Lineage and dependency reasoning** — traverse typed, directed, temporal relationships without treating reachability as exposure, Impact, or cause.
7. **Governance, semantics, and authorization** — carry meaning, responsibility, classification, policy, Assertion Authority, and Capability Authorization into reasoning without collapsing them.
8. **Investigation and causal support** — organize evidence and explicit Causal Claims while allowing unresolved, conflicting, and multi-contributor outcomes.
9. **Business analysis and Explanation** — communicate evidence-consistent, audience-appropriate answers without creating a separate truth source.

## Product stance

DMTZ is:

- an evidence-grounded monitoring, reasoning, Investigation, and Explanation framework;
- historical and bitemporal where the question requires what happened versus what was known then;
- ecosystem-aware rather than repository-bound;
- authorization-aware and data-minimizing;
- deterministic-first for truth, authority, evidence sufficiency, causal confirmation, Impact, and control decisions;
- integration-friendly, leaving source systems authoritative where accepted contracts say they are.

DMTZ is **not**:

- merely an alert aggregator;
- a replacement for Databricks, GitHub, Collibra, Immuta, or other source systems;
- a general BI/raw-data exploration product;
- a legal or compliance certification engine;
- an automatic root-cause oracle;
- a system that treats model/search output as independent truth;
- a requirement that every monitored production pipeline place DMTZ on its critical path.

Optional active-control capabilities such as Execution Gate and Propagation Safeguard remain explicitly separable from passive monitoring.

## Success characteristics

A successful DMTZ deployment is:

- **traceable** — material conclusions retain evidence/provenance;
- **historical** — prior state and prior knowledge remain reconstructable;
- **ecosystem-aware** — cross-repository and cross-pipeline relationships are first-class;
- **semantically useful** — business meaning participates in analysis;
- **policy- and authorization-aware** — visibility and action are capability bounded;
- **uncertainty-aware** — unknown, conflicting, stale, partial, unavailable, and withheld remain legitimate outcomes;
- **integration-friendly** — vendor/source capabilities remain replaceable at accepted concept/contract boundaries;
- **business-accessible** — different audiences may receive different authorized detail without contradictory underlying truth.

## Invariants / boundaries

- execution success ≠ data health;
- freshness ≠ execution success;
- Lineage ≠ cause;
- reachability ≠ exposure ≠ downstream effect ≠ consequence ≠ causal attribution;
- source availability ≠ Assertion Authority;
- authentication ≠ Capability Authorization ≠ Assertion Authority;
- current disclosure permission ≠ historical truth;
- model/search output cannot manufacture truth, evidence sufficiency, authority, causal confirmation, Impact, or control decisions.

## Synchronizations / related canonical resources

- [Actors and stakeholders](actors-and-stakeholders.md)
- [Foundational terminology](terminology.md)
- [Architectural principles](../invariants/architectural-principles.md)
- [Security and governance](../policies/security-governance.md)
- [MVP boundary](../policies/mvp-boundary.md)
- [Shared glossary](glossary.md)

Detailed concept and stable-ID semantics remain owned by the inventory-selected current owners until their later CKR cutovers.

## Provenance

- Original owner: [`../../foundation/001_product_definition.md`](../../foundation/001_product_definition.md)
- Foundation actor/trust context: [`../../foundation/002_actors_and_stakeholders.md`](../../foundation/002_actors_and_stakeholders.md), [`../../foundation/006_security_governance_and_policy_model.md`](../../foundation/006_security_governance_and_policy_model.md)
- MVP refinement: [`../../foundation/008_mvp_boundary.md`](../../foundation/008_mvp_boundary.md)
- Final architecture/implementation boundary: [`../../concepts/phase_010/09_architecture_consolidation_validation_exit/implementation_handoff.md`](../../concepts/phase_010/09_architecture_consolidation_validation_exit/implementation_handoff.md)
