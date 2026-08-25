# OPS-052 — Investigation Candidate / Lead Generation, Basis & Disposition

**Status:** Accepted — Phase 007 Group 05

## Purpose

Represent candidate investigation leads without making them implicit causal claims or allowing graph/ranking heuristics to become truth.

## Contract

A lead records:

- exact Investigation/question;
- candidate subject/condition/change/execution/version/boundary;
- generation basis and evidence references;
- why the candidate is relevant to the question;
- temporal/topological/semantic scope;
- known limitations, conflicts or restrictions;
- investigation-local disposition/history.

Candidate bases may include Lineage relevance, realized Change, intent-realization divergence, execution/version evidence, Observation/Assessment deviation, reconciliation mismatch, Impact context, analyst research or other applicable evidence.

A lead is inquiry state owned by Investigation. It does not have Causal Claim epistemic status.

## Disposition

A lead may remain active, be deprioritized for the current inquiry, be merged as a duplicate reference, become indeterminate/blocked, or be excluded only under OPS-059. These dispositions organize work; they do not prove or disprove causality.

## Invariants

- candidate/lead ≠ Causal Claim.
- candidate count ≠ probability.
- graph path length/directness ≠ causal rank.
- recency ≠ causal rank.
- Criticality/priority ≠ evidence strength.
- automated or analyst-generated leads use the same evidence/provenance rules.
