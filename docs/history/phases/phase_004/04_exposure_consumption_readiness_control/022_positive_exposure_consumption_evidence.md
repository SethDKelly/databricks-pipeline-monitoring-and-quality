# REF-022 — Positive Exposure / Consumption Evidence

**Status:** Accepted — Phase 004 Group 04

## Purpose

Define when evidence is sufficient to establish that a downstream candidate actually encountered the affected state relevant to the exposure proposition.

## Principle

Positive exposure requires evidence that materially links the consumer's actual encounter to the affected state/version/window. Reachability, schedule order, or generic activity is insufficient.

## Evidence patterns

Depending on consumer class, applicable evidence may include:

- execution input/output association tied to the affected producer state;
- refresh/materialization provenance identifying the consumed source/version/window;
- query/read/use evidence tied sufficiently to the affected state;
- publication/serving evidence showing the affected output was the state made available through the relevant boundary;
- application/process evidence showing the relevant report/output/result was actually used;
- another provenance-bearing encounter mechanism that is sufficiently specific under REF-001–REF-005.

No one pattern is universally required.

## Rules

- Direct version/state association can be sufficient for `consumer encountered affected state` when identity/time/grain are aligned.
- Evidence that the consumer refreshed or ran is insufficient when the consumed state/version remains ambiguous.
- Evidence that affected data was merely available to a consumer is not proof it was used when the proposition is actual use/consumption.
- Exposure can be established even when downstream health remains acceptable or unmeasured.
- Exposure does not establish that the originating state caused any downstream effect; that attribution belongs in Causal Claim.
- A business process/user exposure claim requires evidence at the process/use boundary when mere report publication is not equivalent to actual use.
- Multiple copied records of the same encounter do not become independent corroboration.

## Ambiguity

If encounter occurred but affected-state association cannot be resolved, record exposure as unknown/insufficient rather than broadening the proposition to make it pass.

## Non-goals

- declaring downstream degradation;
- business consequence inference;
- universal consumer versioning requirements;
- causal confirmation.
