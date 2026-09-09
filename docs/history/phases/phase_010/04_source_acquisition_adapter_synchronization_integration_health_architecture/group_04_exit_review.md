# Phase 010 Group 04 — Exit Review

**Status:** COMPLETE / ACCEPTED

## Accepted range

- ARCH-133–ARCH-190 accepted.
- Cumulative Phase 010 architecture range: ARCH-001–ARCH-190.
- AHI04-01–AHI04-96 pass.
- D-1383–D-1432 accepted.

## Exit conclusion

The acquisition architecture is sufficiently concrete for runtime/health/lineage/Impact persistence design to begin without allowing connector behavior to redefine evidence semantics.

Selected logical shape:

**verified capability + governed scope → revisioned source-specific acquisition plan → reconciliation-first hybrid collection → durable source/request/page/checkpoint provenance → versioned normalization → multidimensional health/coverage/lag → canonical evidence publication**.

## Gap treatment

- GAP-009-32: resolved architecturally through service-class acquisition/lag objectives rather than one source-latency number.
- GAP-009-33: resolved architecturally through explicit dimensional integration-health journal.
- GAP-009-34: resolved architecturally through endpoint/scope-specific Databricks quota budgets, bulk/selective query strategy and backoff.
- GAP-009-35: resolved architecturally through GitHub App/REST rate state, conditional polling, webhook acceleration and reconciliation.
- GAP-009-36: resolved as environment discovery + optional Collibra adapter contract; exact tenant throttle/license remains deployment data.
- GAP-009-37: resolved as environment discovery + optional Immuta sync/export adapter contract; exact operational limits remain deployment data.
- GAP-009-39: resolved architecturally through proposition-bound optional-source degradation.
- GAP-009-40: Group 01 capability instances now directly drive Group 04 plan/surface availability.
- GAP-009-38: acquisition cost telemetry advanced; whole-system cost remains Group 08.

## Durable safeguards

1. Reconciliation supports completeness; streams/webhooks accelerate freshness.
2. Connector visibility does not define Monitoring Scope.
3. Empty response does not equal negative truth.
4. Pagination/partition completion is explicit.
5. Checkpoints advance only after durable evidence/provenance.
6. Retries/redelivery/overlap are idempotent and common-derived.
7. Publication lag is separate from event time.
8. Authentication/permission/404/throttle/outage are distinct integration states.
9. Schema/parser drift cannot be silently guessed away.
10. Current integration recovery does not rewrite historical evidence gaps.
11. Source retention expiry is distinct from product-retained evidence.
12. Optional source absence narrows exact capability only.
13. Cost/quota optimizations cannot silently relax evidence coverage.
14. No global integration-health score is introduced.
15. Public vendor source behavior remains deployment-verified under Group 01.

## Technology decisions intentionally not made

No universal event bus, queue product, orchestration engine, secret store, worker runtime, observability vendor, API gateway or deployment topology is selected in Group 04.

## Group 05 entry

Group 05 may now use ARCH-001–ARCH-190 to design Git/change/deployment/run/implementation/input/output correlation, health measurement provenance, Lineage, consumer encounter/exposure and downstream Impact evidence.

It must use source evidence together with its acquisition-run, source/capability, checkpoint/window, coverage and integration-health context; connector silence or degraded collection cannot establish operational/health/Impact negatives.
