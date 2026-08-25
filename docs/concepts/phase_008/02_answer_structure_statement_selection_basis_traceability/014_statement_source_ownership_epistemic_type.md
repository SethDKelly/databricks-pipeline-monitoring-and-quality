# EXPL-014 — Statement Source Ownership & Epistemic Type

**Status:** Accepted — Phase 008 Group 02

## Requirement

Every answer-bearing material statement preserves the accepted truth owner and epistemic type of the proposition it communicates.

Examples include:

- Observation fact;
- Assessment outcome;
- registered Change Intent;
- Deployment/Execution History fact;
- Lineage relationship/relevance;
- Investigation lead/localization;
- Causal Claim with its accepted status;
- Impact candidate/exposure/effect/consequence;
- Safeguard/Gate action or enforcement state;
- Semantic Definition/Responsibility/Classification/Policy Context;
- Capability Authorization decision;
- Annotation;
- explicit unknown/conflicting/unavailable/insufficient state owned by the relevant source semantics.

Explanation may attach presentation metadata, but it does not relabel a source proposition into a stronger type for readability.

## Invariants

Observation ≠ Assessment ≠ Change Intent ≠ Change ≠ Causal Claim ≠ Impact ≠ control state ≠ Annotation.

`Supported` Causal Claim cannot become `confirmed`; reachable cannot become exposed; active Safeguard cannot become prevented exposure; Gate HOLD cannot become execution failure merely because the rendered answer is concise.
