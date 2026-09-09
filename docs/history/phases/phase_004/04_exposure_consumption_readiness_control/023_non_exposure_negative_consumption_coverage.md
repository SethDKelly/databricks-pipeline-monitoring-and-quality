# REF-023 — Non-Exposure and Negative Consumption Coverage

**Status:** Accepted — Phase 004 Group 04

## Purpose

Define the evidence standard for saying a downstream candidate did **not** encounter an affected state, while preserving the difference among inactivity, safe-version use, unknown version use, inaccessible evidence, and actual non-exposure.

## Principle

`Not exposed` is a negative conclusion. It requires an adequate opportunity to observe the relevant encounter paths plus sufficient bounded coverage under REF-001–REF-005.

## Distinctions

The framework must distinguish at least:

- **no relevant encounter opportunity** — the consumer had no applicable refresh/run/use opportunity in the bounded window;
- **opportunity observed, no encounter** — applicable telemetry sufficiently shows the consumer did not consume/use the affected state;
- **safe/earlier state encountered** — the consumer acted, but evidence identifies a different non-affected state/version;
- **encounter occurred, version/state unknown** — activity is known but affected-state association is unresolved;
- **consumer/path evidence unavailable or restricted** — the framework cannot establish the negative;
- **affected state encountered** — exposure established.

## Rules

- `No refresh` may support non-exposure only when refresh opportunities/history are sufficiently covered for the bounded proposition.
- A consumer using an earlier safe version can be `not exposed to affected version V` while simultaneously stale or unhealthy on another dimension.
- Missing consumer telemetry is not `no refresh` and not `not exposed`.
- Negative coverage must include the material alternate encounter paths relevant to the proposition. If an alternate path is unknown, global `not exposed` is not justified.
- `Not exposed to V` does not mean `no activity`, `fresh`, `healthy`, or `no business consequence`.
- Restricted evidence can yield an authorized safe non-exposure result only if the underlying internal evidence standard is actually satisfied and the conclusion itself is authorized.

## Temporal behavior

Late refresh/version/use evidence may change the current retrospective exposure result without rewriting the earlier knowledge-cut result.

## Non-goals

- defining freshness or quality health;
- universal completeness percentages;
- treating absence from a monitoring dashboard as negative evidence.
