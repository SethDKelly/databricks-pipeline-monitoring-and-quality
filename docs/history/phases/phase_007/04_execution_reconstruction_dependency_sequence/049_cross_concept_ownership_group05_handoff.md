# OPS-049 — Execution Reconstruction Ownership & Group 05 Handoff

**Status:** Accepted — Phase 007 Group 04

## Purpose

Close Group 04 with explicit ownership boundaries so Investigation consumes execution evidence without turning it into causal truth.

## Ownership

**Execution History owns** evidence-backed actual execution instances, lower-level assembly, attempts/retries/restarts/reruns, lifecycle facts, actual execution ordering, run-specific implementation-state association, consumed input/version association and produced output/version association.

Other concepts retain their truth:

- **Expectation / schedule context** — expected cadence/work requirements;
- **Execution Gate** — opportunity-specific HOLD/ADMIT/override/control state;
- **Deployment** — active implementation-state intervals;
- **Lineage** — effective logical/topological relationships;
- **Observation / Assessment** — timing, freshness, health, readiness and other measured/evaluated facts;
- **Change** — realized state transitions;
- **Impact** — candidate/exposure/effect/consequence;
- **Investigation / Causal Claim** — inquiry and causal propositions.

Run-specific consumption evidence can support later exposure analysis, but Execution History does not label the encounter harmful/impactful.

## Group 05 handoff

Group 05 may use:

- evidenced execution sequence and partial/ambiguous sequence;
- first/last ordering claims with OPS-044 limitations;
- implementation/input/output version associations;
- retries/restarts/reruns/backfills;
- missing/negative claims with OPS-045 coverage;
- historical as-known versus retrospective reconstruction.

It must preserve:

**first deviation / first post-change run / temporal proximity / shared version / dependency sequence ≠ root cause**.

Any causal proposition still enters Causal Claim under REF-013–REF-020.