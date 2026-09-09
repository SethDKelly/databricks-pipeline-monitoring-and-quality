# EXPL-007 — Compound Question Decomposition & Subquestion Identity

**Status:** Accepted — Phase 008 Group 01

## Requirement

Decompose a compound request into independently bounded subquestions when the requested conclusions have different truth owners, scopes, temporal coordinates or evidence burdens.

Example:

`What failed, why, and who was affected?`

may decompose into:

- what execution/health condition occurred?;
- what causal proposition is supported?;
- which consumers encountered the relevant state?;
- what downstream effects/consequences are evidenced?

## Independence

Each subquestion retains its own:

- requested conclusion;
- subject/scope;
- temporal perspective;
- answerability/evidence limitations;
- authorization/disclosure state;
- final epistemic result.

An answered execution subquestion cannot strengthen an unresolved causal subquestion. An exposed consumer does not prove a downstream effect. A confirmed cause does not prove every consumer was exposed.

## Composition

Explanation may present subanswers together for usefulness, but the combined presentation is not a new global truth state or composite confidence score.
