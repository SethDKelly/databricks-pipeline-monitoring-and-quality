# EXPL-027 — Answer Coverage / Completeness Without Confidence-Score Substitution

**Status:** Accepted — Phase 008 Group 02

## Requirement

Evaluate answer coverage relative to the bounded Group 01 question/subquestions and the set of material statements needed to respond safely.

Coverage can record, per subquestion/material proposition, whether the answer is for example:

- answered at the requested/narrower supported scope;
- partially answered;
- unresolved/insufficient;
- conflicting;
- unavailable/not integrated;
- restricted from current disclosure;
- not applicable under the resolved semantics.

These are composition/coverage descriptors over source states, not a new global truth model.

## Invariants

- partial answer coverage is valid;
- one fully answered subquestion does not make the compound answer complete;
- a percentage of answered fields cannot substitute for epistemic confidence;
- no universal answer completeness/confidence score is accepted;
- missing material subquestion coverage must remain visible when its omission could make the answer misleading.
