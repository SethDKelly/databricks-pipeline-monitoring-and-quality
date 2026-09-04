# MVP Boundary

**Canonical key:** `foundation.mvp_boundary`

**Kind:** POLICY

**Authority:** CANDIDATE / NOT CURRENT AUTHORITY

**Migration record:** `foundation.mvp_boundary`

**Owns current question:** What capability boundary must the first DMTZ MVP prove, and what remains explicitly optional or outside that proof?

**Stable IDs:** N/A

## Current semantics

The DMTZ MVP must prove that a representative fragmented Databricks-centered ecosystem can produce evidence-grounded, historically aware, Lineage-aware, authorization-aware answers about operational/data health, planned and realized change, Investigation/causal context, downstream Impact, and Explanation **without requiring optional systems or unsafe semantic shortcuts**.

The implementation program realizes this MVP through Implementation 001–008. This policy defines the product proof boundary; it does not prescribe package-level implementation order.

## Required MVP capabilities

### 1. Ecosystem inventory
Represent logical pipelines, repositories, Databricks jobs/tasks/runs, data assets, cross-pipeline dependencies, and representative downstream consumers with stable identity/provenance boundaries.

### 2. Planned-change and realization context
Register representative Change Intent, anticipated effects/monitoring implications, and relevant prospective Expectation/Baseline-comparability decisions; relate intent to Deployment/activation evidence without requiring one particular ticket/PR system.

### 3. Deployment/run/data association
Represent source/configuration revision → Deployment attempt/activation → execution → relevant inputs/outputs where evidence supports exact association. Name/time proximity alone is insufficient.

### 4. Freshness/staleness
Answer observed currency, applicable normative freshness Expectation, whether staleness is assessed, and relevant historical/Baseline context without equating successful execution with freshness.

### 5. Core quality evidence
Support a small representative high-value set such as row quantity, completeness/null behavior, uniqueness where relevant, schema/structural compatibility, selected domain checks, and join/match behavior for A+B→C.

### 6. Historical comparison and realized Change
Show evidence over time; distinguish planned intent from realized Change and descriptive atypicality from normative violation. Preserve what was known then versus later retrospective knowledge.

### 7. Typed temporal Lineage
Support historical upstream/downstream traversal across sufficient topology for A+B→C and cross-repository scenarios. Lineage remains typed and distinct from exposure, Impact, and cause.

### 8. Evidence-grounded Investigation and Causal Claims
Organize relevant evidence, competing claims, support/contradiction, alternatives, known unknowns, and authority/evidence limitations. MVP must support unresolved and multi-contributor outcomes; automatic causal confirmation is not required.

### 9. Downstream Impact reasoning
Distinguish candidate/reachability, actual exposure/encounter, observed downstream effect, and consequence evidence for representative consumers. Missing consumer telemetry must not become `not exposed`.

### 10. Governance, semantics, authority, and authorization context
Expose representative Semantic Definition, Responsibility Assignment, criticality, Classification, Policy Context, Assertion Authority, Capability Authorization, provenance, and disclosure limits appropriate to the pilot.

### 11. Human context
Support attributed Annotation without using it as a substitute for structured intent, Expectation, governance, authorization, Impact, or causal confirmation.

### 12. Business/engineering Explanation and basis inspection
Support current questions such as: Is it healthy/stale? What changed? Was the change planned? What became active? Which claims are supported/unresolved? Which downstream assets are reachable versus exposed/affected? Who is responsible? What evidence/basis supports the answer? Business and engineering projections remain authorization-aware and evidence-consistent.

### 13. Historical knowledge reconstruction
Preserve enough non-rewriting state/provenance to distinguish what happened, what was known/believed/authorized/controlled/explained then, and what later evidence changes retrospectively.

## MVP proof scenarios

### Scenario A — Stale upstream
Downstream execution succeeds while a relevant upstream input violates its freshness Expectation.

### Scenario B — Join-volume degradation
C falls because A, B, join behavior, or multiple contributors changed; cause may remain unresolved.

### Scenario C — Successful run, poor quality
Execution succeeds while a quality Expectation fails.

### Scenario D — Deployment-correlated change
Data changes after activation; DMTZ reports chronology/evidence and explicit Causal Claim status without converting timing into cause.

### Scenario E — Planned structural change with valid outcome
A Change Intent predicts a lower volume; an authorized post-change Expectation/comparability transition is explicit; later post-change comparable evidence can form the new Baseline.

### Scenario F — Planned change with unintended violation
An expected change occurs while another quality dimension violates its Expectation; planned context does not suppress the violation or predetermine cause.

### Scenario G — Unregistered change
A source/data/topology Change occurs with no registered intent; monitoring still functions and labels planned context unavailable.

### Scenario H — Reachability versus exposure
One downstream consumer is reachable but did not encounter the affected state; another is exposed. They do not receive the same Impact status.

### Scenario I — Multiple contributing causes
At least two compatible contributors remain plausible/supported; Investigation preserves both rather than forcing a single root cause.

### Scenario J — Historical knowledge correction
Later evidence weakens/revises an earlier leading conclusion; contemporaneous and retrospective state/Explanation remain distinguishable.

### Scenario K — Policy-aware business Explanation
Sensitive/restricted upstream/downstream context is represented at authorized abstraction without raw-data or metadata leakage and without implying withheld facts are absent.

## First proof deployment profile

A reasonable first MVP proof includes:

- one representative Databricks environment with required Unity Catalog/system/source capabilities actually verified for that target;
- a small set of representative pipelines/repos including A+B→C;
- GitHub revision/CI/deployment evidence where used;
- enough Measurement/Expectation/Baseline rules for the representative health scenarios;
- representative temporal Lineage and downstream encounter state;
- organization-owned Monitoring Scope, Assertion Authority, and Capability Authorization policy for the pilot;
- deterministic Investigation/Explanation/replay and basis inspection;
- an authorization-aware API/UI serving boundary.

## Explicitly outside the required MVP

The MVP does **not** require:

- autonomous remediation, rollback, or code fixes;
- mandatory Execution Gate or Propagation Safeguard enforcement;
- mandatory Collibra or Immuta;
- mandatory LLM/model assistance;
- mandatory graph database;
- mandatory event-sourcing/blockchain/ledger technology;
- every DQ dimension or every governance/source integration;
- unrestricted raw-data exploration or production row samples;
- guaranteed fully automatic causal confirmation;
- quantitative percentage causal attribution;
- perfect column-level Lineage;
- universal platform/pattern support;
- replacement of Databricks/GitHub/governance/authorization source systems;
- legal compliance certification.

Optional model/search assistance and active control may be added only after deterministic/passive-monitoring paths satisfy their own gates.

## MVP exit test

A representative business analyst and data engineer can inspect the same representative incident/change outcome and receive appropriately detailed but evidence-consistent and authorization-aware Explanations covering applicable intent, Deployment/execution, historical topology, health/quality state, realized Changes, causal evidence/uncertainty, downstream reachability/exposure/effect/consequence, responsibility/policy context, and statement basis.

The MVP must remain able to say `unknown`, `conflicting`, `insufficient`, `unavailable`, or `withheld` rather than manufacture a stronger conclusion.

## Invariants / boundaries

- MVP proof ≠ production graduation;
- design-scenario PASS ≠ executable MVP proof;
- provider documentation ≠ verified target capability;
- execution success ≠ data health;
- Lineage ≠ Impact ≠ cause;
- model availability ≠ basic answerability;
- active control ≠ required passive-monitoring MVP capability.

## Synchronizations / related canonical resources

- [Product definition](../reference/product-definition.md)
- [Architectural principles](../invariants/architectural-principles.md)
- [Security and governance](security-governance.md)
- [Ecosystem lifecycles](../reference/ecosystem-lifecycles.md)

## Provenance

- Original owner and Scenarios A–K: [`../../foundation/008_mvp_boundary.md`](../../foundation/008_mvp_boundary.md)
- Final architecture/first-proof deployment refinement: [`../../concepts/phase_010/09_architecture_consolidation_validation_exit/implementation_handoff.md`](../../concepts/phase_010/09_architecture_consolidation_validation_exit/implementation_handoff.md)
- Current realization program: [`../../implementation/README.md`](../../implementation/README.md)
