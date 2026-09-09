# EXPL-016 — Question Relevance, Materiality & Statement Selection

**Status:** Accepted — Phase 008 Group 02

## Requirement

Select material answer statements relative to the bounded Group 01 question/subquestion rather than returning every available fact about the subject.

Materiality may depend on:

- directness to the requested conclusion;
- necessary qualification/limitation;
- evidence needed to distinguish competing interpretations;
- context required to understand the conclusion correctly;
- downstream consequence/control/governance relevance explicitly requested;
- temporal relevance to the requested event/window/knowledge cut.

Materiality is not evidence strength and does not create truth.

## Invariants

- nearby fact ≠ material answer statement;
- Lineage reachability/path count ≠ materiality by default;
- Criticality/priority may raise presentation relevance but cannot strengthen evidence;
- omission of a non-material fact is valid when it does not alter the meaning/epistemic status of the answer.
