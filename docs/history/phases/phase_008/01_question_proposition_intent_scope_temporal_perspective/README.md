# Phase 008 Group 01 — Question Proposition, Intent, Scope & Temporal Perspective

**Status:** Review complete — accepted

## Goal

Define a precise business-question contract that identifies what conclusion is requested, about which subject/scope, under which temporal perspective, and with which material ambiguity before Explanation selects evidence or composes prose.

## Group result

Group 01 accepts **EXPL-001–EXPL-012**. No new concept is required. The existing **Explanation** concept already owns the initiating question/request/reporting context for composition; health, cause, Impact, control, governance, authorization and operational truth remain with their accepted concepts.

The accepted question chain is:

**request/purpose context → requested conclusion type → subject identity → proposition scope → event/effective-time + knowledge perspective → compound decomposition where needed → truth-owner routing → ambiguity/answerability/negative-evidence constraints → Group 02 answer-composition input**.

No step creates source truth or authorization.

## Accepted EXPL contracts

1. [`EXPL-001 — Question Request Proposition & Identity`](001_question_request_proposition_identity.md)
2. [`EXPL-002 — Requested Conclusion Type & Question Family`](002_requested_conclusion_type_question_family.md)
3. [`EXPL-003 — Subject Identity & Target Resolution`](003_subject_identity_target_resolution.md)
4. [`EXPL-004 — Question Scope Dimensions & Boundary`](004_scope_dimensions_boundary.md)
5. [`EXPL-005 — Temporal Perspective: Event Window & Knowledge Cut`](005_temporal_perspective_event_window_knowledge_cut.md)
6. [`EXPL-006 — Current, Historical & Retrospective Question Semantics`](006_current_historical_retrospective_question_semantics.md)
7. [`EXPL-007 — Compound Question Decomposition & Subquestion Identity`](007_compound_question_decomposition_subquestion_identity.md)
8. [`EXPL-008 — Truth-Owner Routing & Cross-Concept Join Boundaries`](008_truth_owner_routing_cross_concept_join_boundaries.md)
9. [`EXPL-009 — Ambiguity, Underspecification & Competing Interpretations`](009_ambiguity_underspecification_competing_interpretations.md)
10. [`EXPL-010 — Answerability, Evidence Availability & Authorization Separation`](010_answerability_evidence_availability_authorization_separation.md)
11. [`EXPL-011 — Question-Bound Negative & Absence Burdens`](011_question_bound_negative_absence_burdens.md)
12. [`EXPL-012 — Group 02 Answer-Composition Handoff`](012_group02_answer_composition_handoff.md)

## Question identity and family

Natural-language strings are presentation/request artifacts, not proposition identity. A question is bounded by requested conclusion, subject, scope and temporal/context coordinates. Question-family labels help route semantics but do not establish truth, evidence sufficiency or authority.

The framework therefore does not need a 25th `Question` concept merely to classify requests.

## Subject and scope

Entity Identity resolves what the question is about. Environment, version, field/metric, execution, consumer, cohort, path, control instance and other dimensions remain explicit when material.

Broad wording is not permission to generalize beyond evidence. `Are consumers safe?` cannot be answered globally from one safe path; `Is C healthy?` cannot become one universal asset score when several use/profile/dimension propositions matter.

## Temporal perspective

Group 01 adopts the Phase 007 three-view discipline for questions:

- current-state;
- as-known-at-cut historical;
- current retrospective interpretation of a historical event.

Event/effective time and knowledge cut remain independent. A past event target without an explicit earlier knowledge cut is treated as a current retrospective question unless the request context clearly says otherwise.

## Compound questions and truth routing

Compound requests are decomposed when their conclusions have different owners or evidence burdens. This prevents an answerable health/execution statement from silently resolving a causal or Impact question.

Explanation routes material propositions to their accepted owners. In particular, causal `why` wording does not authorize Explanation to convert Lineage, timing, Deployment or intent consistency into Causal Claim truth.

## Answerability

Group 01 rejects a global answerability/confidence percentage. A question can be semantically valid but evidence-limited, internally answerable but disclosure-limited, partially answerable across subquestions, historically unreconstructable, or materially ambiguous.

These limitations stay distinct because they imply different user-facing explanations and different later integration requirements.

## Negative questions

Question polarity never changes evidence standards. `Was nobody affected?`, `Did no run happen?`, `Was there no bypass?`, `Was the change unplanned?` and similar negatives retain the exact source-specific negative-evidence burden accepted in REF/HLTH/OPS.

## Scenario review

[`scenario_review.md`](scenario_review.md) passes **BQ01-01–BQ01-24**, including ambiguous health shorthand, environment/name collisions, historical knowledge cuts, compound questions, partial answerability, causal routing, broad downstream negatives, Gate/Safeguard questions, ownership-versus-authorization, version-use questions and restricted-evidence cases.

## Durable boundaries

- question ≠ truth;
- question ≠ authorization;
- wording ≠ proposition identity;
- question family ≠ source authority/evidence sufficiency;
- name ≠ Entity Identity;
- broad wording ≠ broad evidence coverage;
- current retrospective ≠ what was known then;
- compound presentation ≠ composite truth;
- answered sibling subquestion ≠ unresolved sibling answer;
- Investigation evidence ≠ Causal Claim;
- Responsibility Assignment ≠ Capability Authorization;
- asking for a negative ≠ lower negative-evidence burden;
- partial answerability is valid;
- Explanation remains a projection over source-owned truth.

## Architecture boundary

Group 01 does not select NLP intent classification, semantic parsing, LLM/prompting, chat UX, query language, search/index architecture, persistence, retrieval or clarification-dialog implementation.

## Group exit gate

**Satisfied.** EXPL-001–EXPL-012 and BQ01-01–BQ01-24 establish sufficient question identity/scope/time/routing semantics for answer composition without creating a new concept.

**Next: Group 02 — Answer Structure, Statement Selection & Basis Traceability.**
