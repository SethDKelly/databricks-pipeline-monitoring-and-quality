# OPS-069 — Consumer Encounter Modes & Evidence Specificity

**Status:** Accepted — Phase 007 Group 06

## Purpose

Refine REF-021/022 so exposure evidence is appropriate to the consumer/use boundary rather than forcing one universal consumption mechanism.

## Contract

Encounter modes may include, without selecting implementation technology:

- execution input consumption;
- refresh/materialization;
- publication/serving;
- query/read;
- cache/replica/snapshot use;
- application/API use;
- report/dashboard view or analytical use;
- human/business-process or decision use.

Each proposition binds the minimum boundary necessary for the question. Evidence sufficient for an upstream materialization exposure claim may be insufficient for an end-user or business-process use claim.

Consumer modes can compose, but composition is evidence-bearing rather than transitive by topology alone.

## Invariants

- no universal consumer version identifier is required.
- source-specific evidence retains its native semantics/provenance.
- a report refresh does not prove a person viewed it.
- a person viewing a report does not prove a decision relied on it.
- technical availability evidence does not automatically become business-use evidence.
