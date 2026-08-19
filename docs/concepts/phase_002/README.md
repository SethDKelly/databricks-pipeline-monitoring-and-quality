# Phase 002 — Concept Specifications

**Status:** Active

## Purpose

Phase 002 turns the Phase 001 candidate catalog into explicit Concept Design specifications without mapping concepts to services, schemas, APIs, Databricks objects, or vendor products.

The phase is intentionally divided into five concept groups so that related concepts can be reviewed together while preserving the independence of each concept.

## Strategic review order

| Group | Theme | Concepts under review | Why this group comes here |
|---|---|---|---|
| 01 | Scope & Identity | Monitored Scope, Asset Identity | Every later concept needs stable referents and an explicit answer to what is in monitoring scope. |
| 02 | Semantics, Governance & Policy | Semantic Definition, Ownership, Classification, Policy Context | Once an entity can be identified, the system needs meaning, responsibility, sensitivity, and policy context without conflating them. |
| 03 | Health Evaluation | Expectation, Baseline, Observation, Assessment | Monitoring requires a disciplined separation between what should happen, what usually happens, what was observed, and how the evidence is evaluated. |
| 04 | History, Lineage & Change | Execution History, Deployment, Lineage, Change | Root-cause reasoning requires temporal history, topology, provenance, and change descriptions that remain distinct from causal conclusions. |
| 05 | Investigation, Impact & Explanation | Investigation, Causal Claim, Impact, Annotation, Explanation | Only after the evidence concepts are coherent should the product organize RCA, downstream impact, human context, and audience-facing explanations. |

This order is a **review dependency**, not an implementation dependency. Concepts remain independently motivated and should synchronize rather than collapse into a monolith.

## Boundary refinements introduced in Phase 002

Phase 002 is allowed to revise the Phase 001 discovery names when one-purpose-per-concept analysis exposes a better boundary.

Current refinements to test:

- `Description / Semantics` becomes **Semantic Definition**: one concept whose purpose is to make the meaning and interpretation of an identified entity explicit.
- **Policy Context** is introduced separately from `Classification`: sensitivity labels and applicable handling/policy context are related but not the same purpose.
- **Baseline** is introduced separately from `Expectation`: historical/empirical reference behavior does not itself assert what ought to be acceptable.
- `Deployment Record` becomes **Deployment**: the behavior is preserving and resolving deployment state/history, not merely storing a record.
- **Causal Claim** is introduced so hypotheses, attributions, contradictions, and confirmations have an explicit epistemic home rather than being hidden inside Investigation.
- `Annotation / Confirmation` is split: **Annotation** adds human context; confirmation/rejection acts on a Causal Claim or other reviewable claim without rewriting source observations.
- `Report / Explanation` becomes **Explanation**: a report is a possible presentation artifact; the foundational purpose is to communicate evidence-grounded meaning to an audience.

These are **Candidate** refinements until their group is reviewed and accepted.

## Phase-wide rules

Every concept specification must:

1. have one primary purpose;
2. state an operational principle that demonstrates the purpose;
3. define functional state without implementation schemas;
4. define actions in actor/product language;
5. preserve provenance and effective time where material;
6. explicitly describe missing, stale, conflicting, unauthorized, and insufficient evidence behavior;
7. identify security/privacy/governance implications;
8. identify synchronizations without absorbing neighboring concepts;
9. define non-goals that protect the boundary;
10. be stress-tested against representative ecosystem scenarios.

## Cross-cutting distinctions that must survive every group

- monitored scope ≠ authorization;
- identity ≠ name;
- semantic definition ≠ ownership;
- classification ≠ policy ≠ authorization ≠ compliance;
- expectation ≠ baseline;
- observation ≠ assessment;
- assessment ≠ causal explanation;
- execution success ≠ data health;
- deployment correlation ≠ deployment causation;
- lineage ≠ cause;
- change ≠ degradation;
- hypothesis/causal claim ≠ confirmed cause;
- impact candidate ≠ confirmed business impact;
- annotation ≠ source observation;
- explanation ≠ independent truth source.

## Group workflow

Each group should be reviewed as a bounded design session:

1. validate the actor needs and purposes;
2. challenge concept boundaries and names;
3. walk the operational principles;
4. test state/action independence;
5. test ambiguity and security behavior;
6. identify synchronizations with already-reviewed groups;
7. run the canonical and adversarial scenarios;
8. accept, revise, split, merge, or reject each concept;
9. update the catalog/glossary/decision records before advancing.

A group may be reopened if a later group exposes a flawed boundary.

## Required scenario set

At minimum, every group must survive these scenarios:

### S-01 — Join-volume degradation

Table C is produced from Tables A and B. C drops materially in volume. The system must preserve the ability to determine whether the change originated in A, B, both, join behavior, another transformation change, or remains unresolved.

### S-02 — Stale upstream with successful downstream execution

A downstream Spark job completes successfully using an old upstream input. Execution health and data freshness must remain distinguishable.

### S-03 — Deployment-correlated shift

A data distribution changes after a GitHub Actions deployment. The system may establish correlation and relevant change history without automatically asserting causation.

### S-04 — Cross-repository dependency

A pipeline in one Git repository depends on output maintained/deployed from another repository. Repository boundaries must not break ecosystem reasoning.

### S-05 — Conflicting governance metadata

Two sources disagree on ownership, definition, or classification. The system must preserve provenance/conflict rather than silently flattening the disagreement.

### S-06 — Policy-sensitive explanation

A business analyst is authorized to know that a sensitive asset is affected but is not authorized to inspect raw sensitive values. The monitoring experience must remain useful without broadening access.

### S-07 — Historical replay

An investigation asks what was known, expected, deployed, and connected at an earlier incident time. Current metadata must not overwrite the historical view.

## Phase 002 exit gate

Phase 002 is complete when:

- every retained concept has a reviewed specification;
- rejected/split/renamed candidates have rationale recorded;
- each concept has a singular purpose and defensible boundary;
- the concept catalog and glossary match the reviewed specifications;
- synchronizations needed for Phase 003 are identifiable but not prematurely implemented;
- no concept depends semantically on DQX, Metric Views, Collibra, Immuta, GitHub Actions, or a selected technical architecture;
- and the canonical scenarios can be described using the accepted concepts without inventing hidden functionality.
