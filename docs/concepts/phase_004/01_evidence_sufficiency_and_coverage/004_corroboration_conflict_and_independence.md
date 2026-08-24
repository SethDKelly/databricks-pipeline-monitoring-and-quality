# REF-004 — Corroboration, Conflict, and Evidence Independence

**Status:** Accepted — Phase 004 Group 01

## Outcome

Refine how multiple applicable evidence items strengthen, weaken, duplicate, or conflict with one another without treating source count as evidence strength or silently resolving conflicts through synchronization order.

## Corroboration principle

Multiple evidence items can strengthen a proposition when they add materially distinct observation opportunities, derivations, or perspectives relevant to the same proposition.

Corroboration is not simply `N sources agree`.

## Evidence relationship classes

Evidence items may be:

- **independently corroborating** — materially distinct collection/derivation paths support the same proposition;
- **partially independent** — sources differ but share meaningful upstream telemetry, transformations, or event identity;
- **duplicated/replicated** — multiple records represent the same underlying observation/event;
- **derived from common evidence** — one or more conclusions/aggregates are computed from the same source facts;
- **complementary** — different evidence items establish different required parts of a proposition, such as execution completion plus output-version availability;
- **contradicting** — applicable evidence supports mutually inconsistent states/propositions;
- **non-comparable** — evidence cannot be directly reconciled because grain, semantics, version, or time context differ;
- **unknown relationship** — provenance is insufficient to know whether apparent corroboration is independent.

## Invariants

- Duplicated telemetry does not gain strength by appearing in several stores or dashboards.
- A Databricks event mirrored into another system is not automatically an independent witness to the underlying event.
- An Assessment and the Observation from which it was derived are not two independent facts supporting the Assessment proposition.
- Independent corroboration can strengthen an evidence set but does not bypass the conclusion-specific sufficiency standard.
- Applicable contradiction is preserved even when most evidence points one way.
- Source authority/precedence is not inferred from number of agreeing sources, recency alone, repository ownership, or synchronization order.
- A conflict can remain unresolved; the framework does not require majority vote.
- Common-cause or common-derivation relationships should be visible enough to avoid false evidence multiplication where provenance permits.

## Conflict handling

When applicable evidence conflicts:

1. preserve each evidence item and its provenance;
2. identify whether the conflict is genuine or caused by subject/version/time/grain mismatch;
3. preserve known derivation/common-source relationships;
4. apply an accepted category-specific source-authority rule only if one exists;
5. otherwise return conflict/indeterminate rather than inventing a winner.

Detailed source authority and precedence belong to Phase 005.

## Examples

### Duplicate execution evidence
A Databricks run event is copied to an audit log and then indexed into a monitoring store. Three records do not constitute three independent confirmations of the run.

### Complementary gate evidence
Job success plus a distinct output-version Observation may jointly satisfy a gate criterion requiring both completion and current qualifying output. Neither alone is sufficient.

### Conflicting row counts
Two applicable measurements disagree for the same C output/version. Both remain evidence until correction or accepted authority semantics resolve the discrepancy.

### Causal support
Timing evidence, realized Change evidence, and consumption evidence may be materially distinct support for one Causal Claim. Their strength comes from covering different causal requirements, not from a raw source count.

## Non-goals

- selecting source-authority rules;
- statistical independence testing;
- Bayesian or numeric confidence-model selection;
- majority-vote conflict resolution;
- removing duplicated evidence from history.
