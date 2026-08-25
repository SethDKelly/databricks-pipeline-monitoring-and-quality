# OPS-113 — Re-evaluation, Hold Transition, Supersession & Revalidation

**Status:** Accepted — Phase 007 Group 08

## Purpose

Define how a Gate can move from one opportunity-specific decision interval to another without treating readiness change as automatic control change.

## Rules

- prerequisite/readiness transition does not itself create HOLD or ADMIT;
- a held opportunity requires an applicable later decision/enforcement change before the Gate barrier is considered removed, unless explicit control semantics establish automatic reevaluation/action;
- each re-evaluation binds the then-applicable evidence/knowledge cut;
- later decisions supersede prospectively for the remaining opportunity and preserve earlier decision/enforcement intervals;
- an ADMIT may be single-shot or subject to pre-start revalidation only if the Gate profile explicitly says so;
- a readiness regression after ADMIT does not retroactively invalidate the historical admit;
- re-evaluation after execution has started cannot rewrite the already-passed start decision.

Historical replay retains every material decision/evidence cut.