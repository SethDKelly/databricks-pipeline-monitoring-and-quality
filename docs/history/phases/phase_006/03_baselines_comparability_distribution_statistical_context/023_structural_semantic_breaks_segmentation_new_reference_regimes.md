# HLTH-023 — Structural/Semantic Breaks, Segmentation & New Reference Regimes

**Status:** Accepted — Phase 006 Group 03

## Purpose

Define how material change partitions historical reference behavior without globally discarding unaffected evidence.

## Break candidates

A comparability break may arise from:

- metric-definition revision;
- grain/population/key change;
- field semantic identity or denominator change;
- structural/interface transition;
- material source-population or operating-mode change;
- changed measurement method with non-equivalent semantics;
- other realized Change that alters the proposition being compared.

## Contract

When a break is evidenced:

1. preserve the pre-break Baseline and Observations;
2. mark the affected comparison dimensions non-comparable or segmented from the effective boundary;
3. allow unaffected dimensions to retain their existing references;
4. derive any new regime from sufficient post-break evidence;
5. preserve transitional periods explicitly when they are not representative of either stable regime.

## Invariants

- Change Intent can predict a prospective break but does not activate it by itself.
- Realized Change can establish a break even without prior intent.
- A break is scoped to affected measurement semantics, not the whole table/pipeline.
- Supported rename/identity continuity can preserve some comparisons but does not guarantee them.
- New regime derivation does not rewrite or delete prior history.
- A target/planned value is never inserted as empirical post-change history.

## Example

C changes from account grain to account-day grain. Volume, uniqueness and join-related Baselines segment at the realized boundary, while execution duration may remain comparable if its measurement semantics and operating mode are otherwise unchanged.