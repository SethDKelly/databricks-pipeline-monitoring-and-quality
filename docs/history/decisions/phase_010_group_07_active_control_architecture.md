# Phase 010 Group 07 — Active-Control Architecture Decisions

## D-1545 — Active control remains opt-in over passive monitoring
**Status:** Accepted

Execution Gate/Propagation Safeguard availability is not required for passive monitoring/RCA truth.

## D-1546 — Gate and Safeguard use independent state machines
**Status:** Accepted

Shared infrastructure does not merge semantics.

## D-1547 — Control mechanisms bind deployment-verified capability instances
**Status:** Accepted

Public vendor feature documentation alone is insufficient.

## D-1548 — Control profiles/criteria are immutable by revision
**Status:** Accepted

Historical decision semantics bind exact revisions.

## D-1549 — Control opportunity is a durable first-class identity
**Status:** Accepted

Configuration without opportunity does not create decision/enforcement.

## D-1550 — Gate criteria consume exact proposition/Assessment identities
**Status:** Accepted

Rendered prose/model output is not a criterion.

## D-1551 — Evidence suitability precedes readiness
**Status:** Accepted

Source availability alone is insufficient.

## D-1552 — Readiness remains separate from Gate decision
**Status:** Accepted

A ready state does not itself admit execution.

## D-1553 — Gate decision is opportunity specific
**Status:** Accepted

Enabled configuration is not a decision.

## D-1554 — HOLD and ADMIT remain normal decision states
**Status:** Accepted

Override/fallback are explicit alternative paths.

## D-1555 — Decision issuance, delivery, acceptance and enforcement are separate
**Status:** Accepted

Transport success cannot manufacture enforcement.

## D-1556 — Actual execution is reconciled independently
**Status:** Accepted

HOLD ≠ failed run; ADMIT ≠ run.

## D-1557 — HOLD prevention/non-execution requires opportunity coverage
**Status:** Accepted

No run under missing telemetry is insufficient.

## D-1558 — Overrides retain normal readiness state
**Status:** Accepted

Override admission does not mean prerequisites became ready.

## D-1559 — Override requires exact Capability Authorization
**Status:** Accepted

Platform admin power is not automatic DMTZ authority.

## D-1560 — Overrides are bounded and expiring/revocable
**Status:** Accepted

Expiry is an effective state transition.

## D-1561 — Fallback is explicit policy-as-data
**Status:** Accepted

Configuration ≠ trigger ≠ decision ≠ enforcement.

## D-1562 — Timeout and escalation do not create control decisions
**Status:** Accepted

Any action requires explicit policy.

## D-1563 — Multi-Gate composition requires explicit policy
**Status:** Accepted

No hidden first/last/deny/allow precedence.

## D-1564 — Concurrent Gate opportunities are isolated by identity/revision
**Status:** Accepted

Late decisions cannot govern a different opportunity.

## D-1565 — Gate delivery/enforcement should be idempotent where supported
**Status:** Accepted

Retries are common-derived attempts.

## D-1566 — Gate decisions have explicit applicability horizons where needed
**Status:** Accepted

Stale decisions require rejection/re-evaluation.

## D-1567 — Control decisions retain actual knowledge cut and basis manifest
**Status:** Accepted

Later evidence cannot rewrite historical action.

## D-1568 — GitHub environments can be strong pre-start Gate adapters
**Status:** Accepted

Only for exact protected Actions job/deployment opportunity and verified target capability.

## D-1569 — GitHub custom protection rules are optional deployment-verified adapters
**Status:** Accepted

Preview/plan constraints prevent universal dependency.

## D-1570 — GitHub environment secret withholding strengthens only exact job boundary
**Status:** Accepted

It does not prove Databricks non-execution.

## D-1571 — GitHub Gate → Databricks control requires durable correlation
**Status:** Accepted

Name/time proximity is insufficient.

## D-1572 — A governed Databricks trigger broker can realize pre-start admission
**Status:** Accepted

Only where alternate trigger/bypass paths are governed.

## D-1573 — Databricks `run-now` idempotency can reduce duplicate launch ambiguity
**Status:** Accepted

The token is correlation/idempotency evidence, not truth authority.

## D-1574 — Databricks If/else/Run-if may realize bounded in-DAG Gates
**Status:** Accepted

Only under explicit DMTZ criterion/opportunity mapping.

## D-1575 — Databricks cancellation is asynchronous interruption
**Status:** Accepted

It cannot be labeled pre-start HOLD after execution began.

## D-1576 — Gate degraded-dependency behavior is explicit profile policy
**Status:** Accepted

No universal fail-open/fail-closed default.

## D-1577 — Models/search/graph cannot issue active-control decisions
**Status:** Accepted

Deterministic accepted propositions/rules govern control.

## D-1578 — Safeguard profiles bind exact protected state/path/cohort
**Status:** Accepted

Protected/suspect/stale-safe/defective remain separate.

## D-1579 — Safeguard proposal/authorization/request/attempt/enforcement are separate
**Status:** Accepted

No configuration-to-enforcement shortcut.

## D-1580 — Safeguard effective enforcement is path/cohort specific
**Status:** Accepted

Partial protection remains partial.

## D-1581 — Alternate paths are first-class prevention evidence inputs
**Status:** Accepted

One blocked route cannot prove global protection.

## D-1582 — Exposure opportunity is required for prevention credit
**Status:** Accepted

No opportunity means no prevention credit.

## D-1583 — REF-028 prevention uses a conclusion-specific manifest
**Status:** Accepted

No universal control-effectiveness score.

## D-1584 — `not exposed` remains distinct from `prevented by Safeguard`
**Status:** Accepted

Control nexus must be evidenced.

## D-1585 — Safe stale serving remains health/currentness distinct
**Status:** Accepted

Protection can be effective while freshness is not.

## D-1586 — Configured expiry ≠ effective expiry
**Status:** Accepted

Actual enforcement cessation needs evidence.

## D-1587 — Release request ≠ effective release
**Status:** Accepted

Release is an independently observed transition.

## D-1588 — Effective release ≠ recovery
**Status:** Accepted

Recovery requires Group 05 health/currentness/use evidence.

## D-1589 — Overlapping Safeguards retain independent evidence
**Status:** Accepted

No first-control-wins attribution.

## D-1590 — Narrow prevention attribution is REF-028 bounded
**Status:** Accepted

Broader control-effect claims remain Causal Claim work.

## D-1591 — Historical control replay is non-rewriting
**Status:** Accepted

Actual action, as-known reconstruction and current retrospective remain distinct.

## D-1592 — Current policy cannot backfill historical enforcement
**Status:** Accepted

Counterfactual preferred action is not actual action.

## D-1593 — Control evidence persists in Group 02 canonical journals
**Status:** Accepted

Derived dashboards/caches are not control truth.

## D-1594 — Control evidence retention follows value/obligation rather than forever accumulation
**Status:** Accepted

Exact audit basis can be pinned; low-value transport traces may age.

## D-1595 — GAP-009-21 resolved architecturally via pluggable Safeguard state/adapters
**Status:** Accepted

No universal vendor-native safeguard assumed.

## D-1596 — GAP-009-22 resolved architecturally through opportunity/enforcement/alternate-path prevention manifest
**Status:** Accepted

Wide coverage remains deployment/evidence intensive.

## D-1597 — GAP-009-23 consumes Group 05 cross-system correlation
**Status:** Accepted

Uncorrelated GitHub Gate cannot become Databricks Gate.

## D-1598 — GAP-009-24 represented as organization-owned control policy
**Status:** Accepted

Criterion/override/fallback/multi-Gate semantics are not vendor defaults.

## D-1599 — Group 08 must observe passive and active paths separately
**Status:** Accepted

One service-health score cannot hide control-path degradation.

## D-1600 — Group 08 may optimize latency/cost but not reuse stale unsafe decisions
**Status:** Accepted

Control decision TTL and evidence burdens are hard constraints.

## D-1601 — No new product concept is required
**Status:** Accepted

Existing Execution Gate, Propagation Safeguard and Capability Authorization semantics are sufficient.

## D-1602 — Group 07 accepts ARCH-351–ARCH-420 and promotes Group 08
**Status:** Accepted — Group 07 closure

ACS07-01–ACS07-120 pass. Group 07 closes with independent Gate/Safeguard state machines, deployment-verified GitHub/Databricks adapters, explicit degraded-control policy, REF-028 prevention manifests and non-rewriting historical control replay. Group 08 — Serving, Security, Deployment, Observability & Cost Architecture is next.
