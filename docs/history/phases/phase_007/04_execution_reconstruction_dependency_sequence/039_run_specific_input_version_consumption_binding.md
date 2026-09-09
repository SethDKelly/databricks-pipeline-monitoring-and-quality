# OPS-039 — Run-Specific Input / Version Consumption Binding

**Status:** Accepted — Phase 007 Group 04

## Purpose

Define what it means to say an execution actually used a specific upstream/input state rather than merely having a reachable Lineage path or nearby upstream run.

## Contract

A positive input-consumption proposition binds, where applicable:

- consuming execution identity;
- input Entity Identity and semantic role;
- specific input/output/data/interface version or bounded state identity;
- relevant partition/window/population where material;
- encounter/use time or execution context;
- applicable Lineage relationship/version where it helps interpret meaning;
- provenance/evidence basis and limitations;
- knowledge time.

The evidence must support actual run-specific encounter/use. Lineage reachability, latest available version, last completed upstream run, or timestamp proximity alone is insufficient.

## Result discipline

For a bounded input/version proposition, the framework may establish use, preserve unknown/indeterminate/conflicting/unavailable state, or support a negative only under REF-003/REF-023-grade opportunity and coverage appropriate to the source/use mechanism.

## Cross-boundary rule

Run-specific consumption can later support Impact exposure reasoning when the consumed state is the affected/suspect state, but this contract itself does not assert Impact or consequence.

## Invariants

- reachable input ≠ consumed input;
- newest upstream output ≠ consumed output;
- upstream run before downstream run ≠ consumption;
- run occurrence ≠ consumed-version proof;
- consumption ≠ downstream degradation/cause.