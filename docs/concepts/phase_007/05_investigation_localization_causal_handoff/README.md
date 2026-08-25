# Phase 007 Group 05 — Investigation Lifecycle, First-Deviation Localization & Causal Handoff

**Status:** Next — not started

## Goal

Refine Investigation as a structured operational inquiry: bind the question/outcome, generate candidates, collect/organize evidence, localize first relevant deviation, preserve competing explanations, and hand only explicit causal propositions into Causal Claim.

## Accepted input from Groups 01–04

Group 05 consumes:

- OPS-001–OPS-009 effective/historical Lineage, semantic relevance and bounded topology completeness;
- OPS-010–OPS-020 exact Change Intent/Deployment/realized Change identity and realization comparison;
- OPS-021–OPS-033 prospective candidate/review semantics without promoting prospective state into actual Impact;
- OPS-034–OPS-049 evidence-backed execution instances, attempt continuity, actual ordering, run-specific implementation/input/output version associations, negative operational claims and historical reconstruction.

Execution reconstruction supplies evidence, not explanation. In particular:

- `first run after deployment` does not prove the deployment caused the outcome;
- `first observed deviation` does not prove root cause;
- a shared consumed version does not prove the version caused the downstream condition;
- temporal precedence/dependency sequence does not prove causal transmission;
- incomplete/ambiguous execution reconstruction must remain visible in Investigation.

## Primary questions

- How is an Investigation bound to an observed outcome/question, scope and time window without assuming a cause?
- How should Lineage, Change, execution reconstruction and Phase 006 health/reconciliation evidence generate candidate hypotheses/leads?
- What constitutes useful first-deviation localization across a multi-stage pipeline?
- How should localization distinguish first observed anomaly, earliest evidenced state change, transformation-boundary mismatch and first consumer effect?
- How should localization uncertainty, execution gaps and multiple simultaneous deviations be represented?
- How should retries/reruns/backfills and mixed input versions affect localization?
- When should an operational hypothesis become an explicit Causal Claim rather than remain an Investigation lead?
- What does Investigation closure mean if causality remains unresolved?

## Required boundaries

Preserve:

- Investigation ≠ truth store;
- Investigation question ≠ presumed cause;
- candidate/lead ≠ supported causal claim;
- first-observed/first-deviation ≠ root cause;
- first post-change run ≠ caused-by-change;
- temporal proximity/precedence ≠ cause;
- shared version/consumption path ≠ cause;
- Lineage/reconciliation/localization ≠ causal confirmation;
- incomplete execution evidence limits localization rather than being silently filled;
- Investigation closure ≠ Causal Claim confirmation;
- multiple competing or compatible contributors remain valid;
- REF-013–REF-020 continue to own causal epistemics.

## Group 05 entry scenarios

Group 05 should explicitly test:

- clear first deviation after several healthy upstream stages;
- two simultaneous upstream deviations with one downstream failure;
- earliest observed deviation differs from earliest later-reconstructed deviation;
- deployment-correlated first failure with no discriminatory causal evidence;
- stale input version consumed successfully before downstream degradation;
- retry/rerun changes the apparent sequence;
- missing run/version evidence prevents exact localization;
- reconciliation mismatch localizes a transformation boundary without proving cause;
- downstream effect occurs despite no upstream health violation;
- Investigation closes operationally while causal status remains unresolved/rejected/supported rather than confirmed.

## Handoff to Group 06

Group 06 should use Investigation and Causal Claim state as context while independently establishing which downstream consumers were reachable, actually encountered relevant state, showed effects, and experienced consequences.

## Deferred

Do not choose RCA algorithms, graph search heuristics, automated hypothesis-ranking models, LLM workflows or Investigation UI in this group.