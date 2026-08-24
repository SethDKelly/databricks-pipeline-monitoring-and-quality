# REF-026 — Gate Enforcement Evidence and Degraded Control State

**Status:** Accepted — Phase 004 Group 04

## Purpose

Define what evidence is needed to say an Execution Gate decision was actually enforced, and how to represent degraded/unknown control integration without inventing production behavior.

## Enforcement binding

Gate-enforcement evidence is bound to:

- the specific gate/configuration and downstream target;
- the relevant execution opportunity/window;
- the decision/action being enforced;
- the control boundary/mechanism in effect;
- the effective enforcement interval;
- the evidence source and knowledge time.

## Evidence patterns

Applicable evidence may include a control-plane acknowledgement tied to the exact opportunity, scheduler/admission state, downstream start suppression/release evidence, Execution History, or another implementation-appropriate control fact. No single vendor mechanism is assumed.

## Rules

- A configured/enabled gate is not proof that a particular opportunity was enforced.
- A decision emitted by the monitoring framework is not proof an external scheduler honored it.
- A generic `control healthy` signal is insufficient when the proposition is enforcement for a specific opportunity.
- Hold enforcement requires enough evidence that the relevant downstream opportunity remained blocked while the hold applied; reliable contradictory run evidence defeats that conclusion.
- Admission enforcement means the gate no longer blocked the opportunity; it does not require proving the downstream job subsequently ran.
- `control source unavailable`, `decision delivery unknown`, `enforcement unknown`, and `enforcement contradicted` remain distinct states.
- Control-plane degradation does not itself prove fail-open, fail-closed, or production outage.
- A configured fallback policy is evidence of intended behavior under unavailable/unknown conditions; actual fallback application/outcome requires separate evidence.
- Ungated production remains independent of gate-control availability under the accepted passive-monitoring boundary.

## Historical behavior

Later control telemetry can revise retrospective enforcement understanding without rewriting the actual decision recorded at the time or the actual downstream Execution History.

## Non-goals

- gate implementation selection;
- universal control availability SLO;
- fallback-policy definition;
- assuming a scheduler acknowledgement is always sufficient enforcement proof.
