# OPS-058 — Multiple Deviations, Branching & Competing/Compatible Leads

**Status:** Accepted — Phase 007 Group 05

## Purpose

Allow Investigation to represent concurrent deviations and alternative paths without forcing a single root cause.

## Contract

An Investigation may preserve several branches when:

- multiple upstream entities deviate near the relevant window;
- different dimensions deviate independently;
- one transformation boundary has several plausible contributing conditions;
- mutually exclusive explanations remain non-discriminated;
- compatible contributors may coexist;
- one lead explains only part of the observed outcome.

Lead branches retain their own evidence, gaps, localization results and linked Causal Claims where proposed.

Investigation may narrow branches as evidence discriminates them, but absence of one winner is a valid outcome.

## Invariants

- multiple deviations ≠ multiple causes automatically.
- one leading branch ≠ primary cause.
- supported compatible contributors need not exclude one another.
- mutually exclusive unresolved alternatives can prevent causal confirmation under REF-016/017.
- severity/criticality does not select the winning branch.
