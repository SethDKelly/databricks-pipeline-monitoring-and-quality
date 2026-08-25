# OPS-080 — Consequence Categories: Technical, Analytical & Business

**Status:** Accepted — Phase 007 Group 06

## Purpose

Provide useful consequence classification without inventing a universal harm/severity score or merging consequence with downstream health.

## Contract

Impact may classify provenance-bearing consequence evidence into one or more descriptive categories:

- **technical/operational consequence** — availability, delivery, processing, interface/application behavior or operational disruption;
- **analytical consequence** — report/metric/result interpretation, analysis usability or decision-support degradation;
- **business/process consequence** — process, client/customer/user, decision, contractual/operational business outcome or other established business use consequence.

Categories organize evidence; they do not by themselves assert severity, causality, compliance or monetary loss.

A downstream effect may exist without a consequence in another category, and consequence evidence can sometimes be established even while origin attribution remains unresolved.

## Invariants

- Criticality/Classification ≠ consequence occurrence.
- exposed ≠ consequence.
- downstream violation ≠ business harm automatically.
- consequence category ≠ severity score.
- policy sensitivity ≠ compliance breach.
