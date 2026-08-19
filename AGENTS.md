# Repository Agent Instructions

## Project status

This repository is in **Phase 002 — Concept Specifications**.

**Documentation-only rule:** do not add application code, infrastructure code, notebooks, package manifests, schemas, APIs, services, deployment workflows, prototypes, or framework scaffolding unless the user explicitly advances the project into a technical/implementation phase.

Treat this repository as a standalone data-pipeline monitoring and quality product. Do not import terminology, lifecycles, actors, or domain assumptions from unrelated projects.

Markdown documentation and agent/rule files are in scope.

## Read before changing anything

1. `README.md`
2. `docs/README.md`
3. relevant files in `docs/foundation/`
4. `docs/foundation/004_concept_design_method.md`
5. `docs/reference/glossary.md`
6. relevant concept files in `docs/concepts/`
7. `docs/concepts/phase_002/README.md` and the active concept group
8. `docs/decisions/README.md`

Treat `docs/` as the design system of record.

## Concept Design is mandatory

Use Daniel Jackson's Concept Design method for functional design.

- Start from actor need/purpose, not vendor/tool/API shape.
- A concept is an independent unit of functionality, not automatically a service, class, table, endpoint, screen, repository, Databricks job, or vendor feature.
- Each accepted concept needs: name, one primary purpose, operational principle, state, actions, invariants, ambiguity behavior, and synchronizations.
- Prefer synchronization between concepts over merging unrelated purposes.
- Do not map concepts to implementation modules during product discovery.
- Do not invent concepts named after tools such as DQX, Collibra, Immuta, Unity Catalog, or GitHub Actions; model the product purpose first, then evaluate tools as realizations/providers.

## Product invariants

Preserve these distinctions:

- ecosystem ≠ repository;
- logical pipeline ≠ Databricks job;
- successful run ≠ healthy data;
- freshness ≠ execution success;
- expectation ≠ baseline;
- normative requirement ≠ historical regularity;
- observation ≠ assessment;
- missing evidence ≠ observed absence;
- typical ≠ healthy;
- atypical ≠ degraded/defective;
- assessment ≠ root cause;
- anomaly ≠ defect;
- correlation ≠ cause;
- hypothesis ≠ confirmed cause;
- data lineage ≠ deployment lineage;
- classification ≠ authorization;
- policy metadata ≠ compliance;
- current topology ≠ historical topology.

## Evidence and uncertainty

- Separate normative Expectations, descriptive Baselines, observed facts, derived Assessments, hypotheses, attributions, human confirmations, and confirmed causes.
- Preserve provenance and time context for material facts and evaluation references.
- `Unknown`, `conflicting`, `non-comparable`, `unavailable`, `unauthorized`, and `insufficient evidence` are valid outcomes.
- Never infer zero/no-event from missing telemetry.
- Baseline deviation alone never establishes normative failure or root cause.
- Assess health dimensions independently unless an explicit composite aggregation rule is defined.
- Reassessment after corrected/late evidence must preserve prior assessment history.
- Never force a root cause when evidence is incomplete.
- Business summaries must remain traceable to the same evidence used for engineering detail.

## Governance and security

- Monitoring must not broaden access to raw data.
- Treat metadata as potentially sensitive.
- Prefer aggregate/metadata evidence over raw or row-level values.
- Never place real PII, PHI, secrets, tokens, credentials, or production data in this repository.
- Use synthetic examples.
- Never describe a system or asset as HIPAA compliant merely because PHI/HIPAA-related metadata or checks exist.
- Preserve source authority/provenance for responsibility assignments, semantics, classifications, policy context, expectations, lineage, and observations.
- Collibra and Immuta are optional until explicitly made authoritative for a metadata category.

## Tooling stance

- Databricks Metric Views and DQX are strongly favored for later evaluation.
- Do not treat favored tooling as a settled implementation choice.
- Integrate before duplicating when an existing authoritative capability satisfies a product concept.
- Do not introduce a technical architecture during Phase 002.

## Documentation discipline

- Refine existing canonical definitions instead of creating competing definitions.
- Link to the canonical document when possible.
- Label unresolved items as `Open`, implementation possibilities as `Candidate` or `Deferred`, and accepted product principles as `Foundation`/`Accepted`.
- Record meaningful decisions in `docs/decisions/`.
- When changing terminology, update the glossary and affected concept/foundation docs together.
- Avoid implementation-level pseudocode unless the user explicitly requests it; prefer scenarios and operational principles.

## Current canonical scenario

Use the Table A + Table B → Table C join-volume degradation example as a recurring stress test:

- C decreases materially;
- distinguish whether the change is merely atypical versus normatively unacceptable;
- determine whether A, B, both, or join behavior changed;
- consider freshness, schema, quality, run history, deployment changes, and historical lineage;
- identify downstream impact and responsible parties;
- preserve evidence and uncertainty.
