# REF-021 — Exposure Proposition and Encounter Binding

**Status:** Accepted — Phase 004 Group 04

## Purpose

Make every exposure question precise enough that evidence can prove or fail to prove an actual encounter rather than relying on generic downstream reachability or timing.

## Bound exposure proposition

An exposure proposition identifies, where material:

- the originating/affected subject and specific state, output, version, condition, or bounded event window;
- the downstream candidate/consumer being evaluated;
- the historical Lineage/relationship context that makes encounter possible;
- the **encounter mode** relevant to that consumer, such as execution input, refresh/materialization, publication/serving, query/application use, or business-process use;
- the consumer opportunity/time window being evaluated;
- the exact conclusion, such as `exposed to affected version V`, `not exposed to affected state during W`, or `encounter unknown`.

## Rules

- Reachability identifies a candidate but does not satisfy encounter binding.
- A downstream execution/refresh after an upstream event is timing context, not proof that the affected state was consumed.
- Exposure to a table/output and exposure to a business process are different propositions when an intermediate report/application must actually be used.
- Version/state ambiguity remains explicit. Evidence that a consumer used `some C output` does not establish exposure to affected C version V unless the association is sufficiently resolved.
- The encounter mode determines what evidence is relevant; the framework does not assume one universal consumption mechanism across jobs, Metric Views, reports, applications, and business processes.
- Restricted consumer/path detail may remain opaque while the internal proposition remains sufficiently bound.

## Temporal behavior

The affected-state interval, consumer encounter opportunity, source availability, framework knowledge time, and evaluation time remain distinct under REF-006–REF-012.

## Non-goals

- selecting consumer-specific integration technology;
- defining downstream health or business consequence;
- treating reachability as exposure;
- requiring every consumer to expose a version identifier.
