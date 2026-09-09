# OPS-059 — Lead Exclusion, Narrowing & Negative Evidence

**Status:** Accepted — Phase 007 Group 05

## Purpose

Define when Investigation may legitimately exclude or narrow a lead without treating missing evidence as exoneration.

## Contract

Excluding a lead is a bounded investigation conclusion about a specific proposition, not a global statement that the subject could not have contributed in any way.

An exclusion/narrowing basis must identify:

- the lead/proposition being excluded or narrowed;
- the evidence mechanism capable of observing the relevant condition;
- bounded opportunity and coverage under REF-002/003;
- applicable temporal/version/population/metric scope;
- decisive contradiction or discriminating evidence;
- remaining limitations and alternate propositions not excluded.

Examples of valid narrowing can include sufficient evidence that a suspected version was not consumed, that a candidate condition occurred only after the effect, or that a controlled/repeated comparison contradicts the proposed mechanism.

## Invariants

- `no deviation observed` ≠ `no deviation occurred` without coverage.
- lack of support ≠ rejection/exclusion.
- `A did not change in metric M` ≠ `A cannot be causal through another dimension`.
- exclusion of one causal proposition does not exclude compatible alternatives.
- restricted/unavailable evidence cannot become reassuring negative evidence.
