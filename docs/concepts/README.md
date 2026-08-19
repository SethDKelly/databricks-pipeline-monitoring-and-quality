# Concept Catalog

## Status

**Phase 002 active working catalog.** Every concept remains **Candidate** until its group is reviewed and explicitly accepted.

The project uses Concept Design to discover independently understandable units of functionality. A concept is retained only when it has a clear primary purpose, operational principle, state, actions, invariants, ambiguity behavior, security/provenance considerations, and explicit synchronizations.

Use [`concept_template.md`](concept_template.md) as the specification checklist. The strategic Phase 002 review plan is in [`phase_002/README.md`](phase_002/README.md).

## Current grouped candidates

### Group 01 — Scope & Identity

- [`Monitored Scope`](phase_002/01_scope_and_identity/monitored_scope.md) — what is intended to participate in monitoring.
- [`Asset Identity`](phase_002/01_scope_and_identity/asset_identity.md) — how logical entities are recognized across sources and time.

### Group 02 — Semantics, Governance & Policy

- [`Semantic Definition`](phase_002/02_semantics_governance_policy/semantic_definition.md) — what an identified entity means and how it should be interpreted.
- [`Ownership`](phase_002/02_semantics_governance_policy/ownership.md) — who is responsible/accountable for a defined responsibility.
- [`Classification`](phase_002/02_semantics_governance_policy/classification.md) — sensitivity/governance categories without access or compliance implications.
- [`Policy Context`](phase_002/02_semantics_governance_policy/policy_context.md) — relevant declared handling/policy context without claiming enforcement/compliance.

### Group 03 — Health Evaluation

- [`Expectation`](phase_002/03_health_evaluation/expectation.md) — what should be true/acceptable.
- [`Baseline`](phase_002/03_health_evaluation/baseline.md) — what reference behavior has been observed/derived historically.
- [`Observation`](phase_002/03_health_evaluation/observation.md) — provenance-bearing measured/retrieved facts.
- [`Assessment`](phase_002/03_health_evaluation/assessment.md) — interpretation of observations against expectations/baselines.

### Group 04 — History, Lineage & Change

- [`Execution History`](phase_002/04_history_lineage_change/execution_history.md) — what ran, when, and with what operational outcome.
- [`Deployment`](phase_002/04_history_lineage_change/deployment.md) — which source/configuration deployment was active at a relevant time.
- [`Lineage`](phase_002/04_history_lineage_change/lineage.md) — typed upstream/downstream relationships, including historical topology.
- [`Change`](phase_002/04_history_lineage_change/change.md) — meaningful differences across time without asserting health or cause.

### Group 05 — Investigation, Impact & Explanation

- [`Investigation`](phase_002/05_investigation_impact_explanation/investigation.md) — a bounded inquiry that organizes evidence.
- [`Causal Claim`](phase_002/05_investigation_impact_explanation/causal_claim.md) — an explanation under evaluation with explicit epistemic status.
- [`Impact`](phase_002/05_investigation_impact_explanation/impact.md) — downstream exposure and affected-consumer reasoning.
- [`Annotation`](phase_002/05_investigation_impact_explanation/annotation.md) — human context without rewriting source evidence.
- [`Explanation`](phase_002/05_investigation_impact_explanation/explanation.md) — evidence-grounded, audience-appropriate communication.

## Boundary changes from Phase 001 discovery

The Phase 001 seed intentionally used broad names. Phase 002 currently tests these refinements:

- `Description / Semantics` → **Semantic Definition**.
- introduce **Policy Context** separately from Classification.
- introduce **Baseline** separately from Expectation.
- `Deployment Record` → **Deployment**.
- introduce **Causal Claim** rather than hiding hypotheses/confirmation inside Investigation.
- `Annotation / Confirmation` → **Annotation** plus confirmation/rejection actions on reviewable causal claims.
- `Report / Explanation` → **Explanation**; reports are treated as possible presentation artifacts rather than the foundational concept.

These changes are not final until reviewed.

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

1. Observation + Expectation/Baseline → Assessment.
2. degraded Assessment → Investigation.
3. Investigation + Lineage/Change/Execution History/Deployment → evidence discovery.
4. Investigation + Causal Claim → explicit causal reasoning.
5. Lineage + Impact → downstream exposure candidates.
6. Ownership/Semantic Definition/Policy Context + Explanation → business-facing context.
7. Classification/Policy Context + authorization-aware presentation → safe disclosure.
8. Annotation + Investigation/Causal Claim → human context without evidence mutation.
