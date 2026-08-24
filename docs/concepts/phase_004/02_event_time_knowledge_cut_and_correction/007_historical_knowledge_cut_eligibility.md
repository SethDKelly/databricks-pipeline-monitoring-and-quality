# REF-007 — Historical Knowledge-Cut Eligibility

**Status:** Accepted — Phase 004 Group 02

## Purpose

Define exactly when evidence or concept state may contribute to an `as-known` historical view.

## Eligibility rule

For a historical question with event/effective-time target or window `T` and knowledge cutoff `K`, an evidence item may contribute only when:

1. it is applicable to the target proposition under REF-001;
2. its event/effective-time semantics make it relevant to `T`;
3. the monitoring framework's recorded/knowledge time for that evidence is at or before `K`;
4. any correction/supersession state used in the cut was itself known by `K`;
5. the evidence is not excluded by an explicit historical validity boundary;
6. the result preserves any Group 01 coverage/conflict/availability limitations.

## Actual state versus replay-derived state

An Assessment, Causal Claim status, Impact conclusion, gate/safeguard decision, Investigation state, Annotation, or Explanation is **actual historical state** only when evidence establishes that state was recorded by `K`.

A present-day computation over evidence eligible at `K` is a **replay-derived** result with current evaluation time. It cannot be backdated merely because its inputs were historically eligible.

## Source-available but not framework-known

Evidence that was queryable from a source before `K` but was not collected/recorded by the framework by `K` is not part of the framework's `as-known` state. It may support a separately labeled analysis such as `source-available-by-K` when source-availability evidence is sufficient, but it cannot be represented as something the framework knew.

## Current retrieval of historical facts

If the framework retrieves today a source record effective last week, the record may inform the current retrospective view of last week. Its current knowledge time is not silently rewritten to last week.

## Partial cuts

Historical cuts may be partial, conflicting, authorization-limited, or unavailable. Eligibility does not imply evidentiary sufficiency for a requested conclusion.

## Non-goals

- defining database snapshot/query syntax;
- selecting event sourcing or temporal storage;
- treating every source-created timestamp as framework knowledge time;
- inferring historical actor beliefs from merely eligible source facts.
