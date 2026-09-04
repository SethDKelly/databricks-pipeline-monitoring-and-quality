# CKR-B Execution Review — Foundation, Terminology & Cross-Cutting Invariants

**Status:** IN EXECUTION — CANDIDATE REVIEW

## Objective

Perform the first substantive CKR migration by consolidating the nine accepted foundation/glossary records into bounded canonical candidates, proving semantic conservation, then cutting them over atomically without changing accepted DMTZ meaning.

## Candidate set

CKR-B owns exactly:

- `foundation.product_definition`;
- `foundation.actors_stakeholders`;
- `foundation.terminology`;
- `foundation.concept_design_method`;
- `foundation.architectural_principles`;
- `foundation.security_governance_policy`;
- `foundation.ecosystem_lifecycles`;
- `foundation.mvp_boundary`;
- `reference.glossary`.

At this review stage all nine are `candidate_ready`; their legacy owners remain current authority.

## Semantic-conservation evidence

See [`ckr_b_semantic_conservation_matrix.md`](ckr_b_semantic_conservation_matrix.md).

Mandatory preservation includes:

- product purpose/outcome/non-goals;
- actor authority separation;
- foundational terminology/non-equivalences;
- Concept Design method and synchronization discipline;
- AP-01–AP-32;
- SP-01–SP-15;
- fourteen ecosystem lifecycles and non-rewriting/bitemporal principle;
- thirteen required MVP capability areas and Scenarios A–K;
- current shared glossary vocabulary.

Historical Phase 001 roadmap/open-question/handoff material remains preserved but is intentionally not promoted to canonical current truth.

## Scenario set

`fixtures/ckr_b_foundation_scenarios.yaml` defines CKRB-01 through CKRB-20.

## Deterministic validation required

Candidate-stage acceptance requires:

- generic canonical ownership/authority validation;
- CKR-B semantic-coverage validation;
- CKR status drift with B IN EXECUTION;
- fixture catalog integrity;
- context-budget conformance;
- negative controls for omitted AP/SP/MVP or broken candidate provenance;
- documentation consistency and unified conformance on the candidate-review PR state.

## Candidate-stage result

Pending CI.

## Atomic cutover requirements

After candidate review succeeds, all nine records cut over only in one synchronized closure change that:

1. marks each target `CANONICAL CURRENT AUTHORITY`;
2. changes each inventory record to `canonicalized`;
3. routes current foundation/glossary questions to `docs/canonical/`;
4. classifies the legacy 001–008 foundation owners and old glossary as provenance/history for these records without rewriting their accepted-at-the-time narrative;
5. keeps `reference.authority_vocabulary`, all 24 concepts, and all stable-ID families with their independent existing owners;
6. advances live CKR status to CKR-B complete / CKR-C next only after the cutover passes conformance.

## Exit decision

Pending candidate CI, atomic cutover, final closure CI, and merge verification.
