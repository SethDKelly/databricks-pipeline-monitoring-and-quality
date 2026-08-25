# OPS-014 — Realized Change Proposition, Before/After State & Transition Binding

**Status:** Accepted — Phase 007 Group 02

## Purpose

Make realized Change precise enough to compare with intended modification without turning Deployment activation, raw difference, health Assessment or causal explanation into Change truth.

## Contract

A material realized Change proposition binds, where applicable:

- changed subject/relationship Entity Identity;
- changed facet/type;
- before-state/evidence/reference;
- after-state/evidence/reference;
- semantic grain/population/field/interface/context/version needed for the comparison;
- supported transition time or interval;
- direction/magnitude/equivalence information where meaningful;
- comparison/derivation semantics and limitations;
- provenance/evidence basis;
- framework knowledge time and correction/supersession history;
- optional contextual links to Change Intent and Deployment without importing their truth.

## Implementation-state Change versus downstream effect Change

An activated configuration transition can itself be a realized Change of implementation state when its before/after state is established.

That does **not** create downstream Change automatically. For example:

- `filter F2 became active` can be established;
- `C population decreased` requires its own evidence;
- `C null rate increased` requires its own evidence;
- whether F2 caused either effect belongs to Causal Claim.

## Meaningful Change

A difference becomes a retained Change only when it is meaningful under the relevant semantic/comparison rules. Phase 006 Baseline/Assessment semantics remain separate; not every run-to-run numerical difference becomes a Change record.

## Resolution limitations

Non-comparable, missing, conflicting, restricted or time-misaligned before/after evidence yields an appropriately limited Change result rather than fabricated state.

## Invariants

- Change Intent ≠ realized Change;
- Deployment activation can be a configuration/code state Change but does not manufacture downstream data/schema/topology Change;
- difference ≠ meaningful Change;
- Change ≠ health/degradation;
- Change ≠ intent conformance;
- Change ≠ cause;
- missing before-state ≠ zero/default;
- current state does not overwrite historical transition state.

## Handoff

OPS-015 provides derived comparison of this evidence-established state against exact intent components.