# Contributing

This repository is currently in **Phase 002 — Concept Specifications**.

## Allowed contributions in the current phase

- refine Concept Design specifications group-by-group;
- challenge concept purpose, boundaries, operational principles, state, actions, invariants, ambiguity behavior, and synchronizations;
- document real or synthetic pipeline scenarios;
- identify authoritative metadata sources and conflicts;
- refine governance/security/policy transparency requirements;
- define health, freshness, quality, change, lineage, and RCA semantics;
- refine the MVP boundary and roadmap when concept discoveries require it;
- record open questions, rejected/split concepts, and accepted decisions.

## Out of scope until the project explicitly advances phase

Do not introduce:

- application source code;
- notebooks;
- infrastructure-as-code;
- service/API scaffolding;
- database schemas;
- package manifests chosen only to start coding;
- GitHub Actions for this repository's application deployment;
- Databricks jobs for the monitoring framework;
- architecture diagrams that present unselected implementation technology as settled fact.

## Design method

All functional design follows Daniel Jackson's Concept Design approach described in `docs/foundation/004_concept_design_method.md`.

Before proposing a concept, make sure it has a clear purpose and operational principle and is not merely a vendor feature or implementation component.

## Security and examples

Never commit secrets, credentials, production data, or real PII/PHI. Use synthetic examples. Policy classifications should be described precisely and must not be presented as compliance certifications.
