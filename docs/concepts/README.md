# Concept Catalog

## Status

**Phase 002 active working catalog.** Groups 01–03 are accepted. Groups 04–05 remain **Candidate** until reviewed and explicitly accepted.

The project uses Concept Design to discover independently understandable units of functionality. A concept is retained only when it has a clear primary purpose, operational principle, state, actions, invariants, ambiguity behavior, security/provenance considerations, and explicit synchronizations.

Use [`concept_template.md`](concept_template.md) as the specification checklist. The strategic Phase 002 review plan is in [`phase_002/README.md`](phase_002/README.md).

## Current grouped concepts

### Group 01 — Scope & Identity — Accepted

- [`Monitoring Scope`](phase_002/01_scope_and_identity/monitoring_scope.md) — which identified entities the product is responsible for monitoring at a relevant time.
- [`Entity Identity`](phase_002/01_scope_and_identity/entity_identity.md) — how logical entities are recognized across source-specific references and time while preserving ambiguity and correction.

### Group 02 — Semantics, Governance & Policy — Accepted

- [`Semantic Definition`](phase_002/02_semantics_governance_policy/semantic_definition.md) — what an identified entity means in a relevant business/technical context.
- [`Responsibility Assignment`](phase_002/02_semantics_governance_policy/responsibility_assignment.md) — who bears a named responsibility for an identified subject at a relevant time.
- [`Classification`](phase_002/02_semantics_governance_policy/classification.md) — category membership in a named governance/sensitivity vocabulary without policy, access, or compliance implications.
- [`Policy Context`](phase_002/02_semantics_governance_policy/policy_context.md) — which declared policies/handling expectations are asserted to apply in a relevant subject/context/time without claiming enforcement or compliance.

### Group 03 — Health Evaluation — Accepted

- [`Expectation`](phase_002/03_health_evaluation/expectation.md) — normative criteria describing what should be true/acceptable for a subject/context/time.
- [`Baseline`](phase_002/03_health_evaluation/baseline.md) — descriptive reference behavior derived from comparable evidence without asserting normative correctness.
- [`Observation`](phase_002/03_health_evaluation/observation.md) — provenance-bearing measured/retrieved facts that do not interpret health or cause.
- [`Assessment`](phase_002/03_health_evaluation/assessment.md) — dimension-scoped interpretation of Observation evidence against explicit Expectation and/or Baseline context.

### Group 04 — History, Lineage & Change — Candidate

- [`Execution History`](phase_002/04_history_lineage_change/execution_history.md) — what ran, when, and with what operational outcome.
- [`Deployment`](phase_002/04_history_lineage_change/deployment.md) — which source/configuration deployment was active at a relevant time.
- [`Lineage`](phase_002/04_history_lineage_change/lineage.md) — typed upstream/downstream relationships, including historical topology.
- [`Change`](phase_002/04_history_lineage_change/change.md) — meaningful differences across time without asserting health or cause.

### Group 05 — Investigation, Impact & Explanation — Candidate

- [`Investigation`](phase_002/05_investigation_impact_explanation/investigation.md) — a bounded inquiry that organizes evidence.
- [`Causal Claim`](phase_002/05_investigation_impact_explanation/causal_claim.md) — an explanation under evaluation with explicit epistemic status.
- [`Impact`](phase_002/05_investigation_impact_explanation/impact.md) — downstream exposure and affected-consumer reasoning.
- [`Annotation`](phase_002/05_investigation_impact_explanation/annotation.md) — human context without rewriting source evidence.
- [`Explanation`](phase_002/05_investigation_impact_explanation/explanation.md) — evidence-grounded, audience-appropriate communication.

## Accepted boundary changes from Phase 001 discovery

- `Monitored Scope` → **Monitoring Scope**: monitoring responsibility applies to identified entities; known relationships may cross a scope boundary.
- `Asset Identity` → **Entity Identity**: identity behavior applies beyond data assets to the broader ecosystem.
- `Description / Semantics` → **Semantic Definition**: meaning is represented through provenance-bearing semantic facets/context rather than one canonical description string.
- `Ownership` → **Responsibility Assignment**: technical ownership, business accountability, stewardship, and other named responsibilities are distinct assignment types and do not confer universal authority.
- **Classification** is retained but narrowed to category membership; classification is not policy or access.
- **Policy Context** is accepted separately from Classification: declared policy applicability/handling context is distinct from category membership, authorization, enforcement, and compliance.
- **Baseline** is accepted separately from Expectation because descriptive reference behavior is not a normative requirement.
- **Observation** and **Assessment** remain separate so measured facts are not mutated by interpretation.
- **Assessment** carries explicit normative/comparative basis; typicality and health are not synonyms.

## Candidate boundary changes for later groups

- `Deployment Record` → **Deployment**.
- introduce **Causal Claim** rather than hiding hypotheses/confirmation inside Investigation.
- `Annotation / Confirmation` → **Annotation** plus confirmation/rejection actions on reviewable causal claims.
- `Report / Explanation` → **Explanation**; reports are treated as possible presentation artifacts rather than the foundational concept.

## Domain entities that are not automatically concepts

These nouns may participate in many concepts without owning the related behavior:

- logical pipeline;
- Databricks job;
- task;
- run;
- table;
- view;
- Metric View;
- repository;
- GitHub Actions workflow;
- column;
- business metric;
- dashboard/report;
- team/person.

## Synchronization work

Phase 002 identifies likely synchronizations only to protect concept boundaries. Detailed synchronization design belongs to Phase 003.

Examples to test later include:

1. Observation + Expectation/Baseline → basis-explicit Assessment.
2. violated/atypical/unresolved Assessment → Investigation without asserting cause.
3. Investigation + Lineage/Change/Execution History/Deployment → evidence discovery.
4. Investigation + Causal Claim → explicit causal reasoning.
5. Lineage + Impact → downstream exposure candidates.
6. Responsibility Assignment/Semantic Definition/Policy Context + Explanation → business-facing context.
7. Classification + Policy Context → policy-applicability evidence without collapsing classification into policy.
8. Classification/Policy Context + authorization-aware presentation → safe disclosure.
9. Annotation + Investigation/Causal Claim → human context without evidence mutation.
