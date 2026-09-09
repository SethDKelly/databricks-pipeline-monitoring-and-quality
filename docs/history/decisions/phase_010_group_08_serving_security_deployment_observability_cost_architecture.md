# Phase 010 Group 08 — Serving, Security, Deployment, Observability & Cost Architecture Decisions

## D-1603 — Serving is a governed projection/orchestration boundary
**Status:** Accepted

User-facing serving never becomes an alternative canonical truth source.

## D-1604 — Service goals bind SC-01–SC-06
**Status:** Accepted

No universal DMTZ freshness/latency/completeness SLO.

## D-1605 — Canonical writes use governed command/persistence paths
**Status:** Accepted

UI/read-model convenience cannot bypass identity/provenance/time/authorization rules.

## D-1606 — Read models/indexes/caches are rebuildable
**Status:** Accepted

Projection loss degrades serving, not canonical history.

## D-1607 — Material requests carry full governance context
**Status:** Accepted

Tenant/principal/purpose/scope/time/detail/export context is explicit.

## D-1608 — Responses retain an epistemic envelope
**Status:** Accepted

Partial/unknown/stale/withheld states and material limitations survive transport/UI rendering.

## D-1609 — Exact retrieval precedes semantic assistance
**Status:** Accepted

Semantic/vector recall remains candidate discovery only.

## D-1610 — Replay, basis inspection and communication retain dedicated paths
**Status:** Accepted

Their time/disclosure/authenticity contracts cannot be collapsed into generic reads.

## D-1611 — Active control receives isolated operational priority
**Status:** Accepted

Optional UI/model pressure cannot silently govern SC-06 outcomes.

## D-1612 — Mutating commands are idempotent where applicable
**Status:** Accepted

Retries create attempts, not duplicate semantic actions.

## D-1613 — API/event schemas are versioned independently of physical tables
**Status:** Accepted

Breaking client reinterpretation is rejected.

## D-1614 — Pagination/resource limits remain explicit partiality
**Status:** Accepted

A response limit is not population coverage.

## D-1615 — Authorization-sensitive caches bind material policy context
**Status:** Accepted

Post-hoc UI hiding cannot make a broad cache safe.

## D-1616 — Cache validity binds watermark/applicability, not one TTL
**Status:** Accepted

Cache freshness depends on the proposition/service class.

## D-1617 — UI must preserve accepted epistemic states
**Status:** Accepted

Unknown/conflicting/unavailable/withheld cannot be flattened into stronger status.

## D-1618 — Authentication is distinct from DMTZ authorization/authority
**Status:** Accepted

Login success grants no domain authority by itself.

## D-1619 — Human identities bind enterprise auth claims to canonical Principals
**Status:** Accepted

Vendor aliases remain evidence-bound identity mappings.

## D-1620 — Workloads use distinct least-privilege identities where practical
**Status:** Accepted

One omnipotent shared credential is rejected as default.

## D-1621 — Short-lived credentials are preferred when supported
**Status:** Accepted

Static credentials are explicit governed exceptions.

## D-1622 — Secret values remain outside canonical evidence and routine telemetry
**Status:** Accepted

Only minimum safe references/provenance survive.

## D-1623 — Service processing permission remains separate from requester visibility
**Status:** Accepted

Internal workload access cannot be inherited by users.

## D-1624 — Runtime authorization is request-context specific
**Status:** Accepted

Material reads/exports/actions are re-evaluated under current policy.

## D-1625 — Actual authorization decisions retain provenance
**Status:** Accepted

Replay-derived decisions remain distinguishable.

## D-1626 — Active-control authorization has bounded freshness
**Status:** Accepted

Revocation/expiry/material policy change may require enforcement-time revalidation.

## D-1627 — Tenant and residency boundaries apply end to end
**Status:** Accepted

Derived stores, indexes, caches and telemetry are included.

## D-1628 — Network reachability never substitutes for authorization
**Status:** Accepted

Private connectivity is defense in depth, not policy truth.

## D-1629 — Material callbacks require authenticity and replay defense
**Status:** Accepted

Unauthenticated/replayed callbacks cannot create canonical/control success.

## D-1630 — Observability is data-minimized
**Status:** Accepted

Logs/traces cannot become a hidden evidence/secret exfiltration channel.

## D-1631 — Security dependency degradation is explicit
**Status:** Accepted

No hidden permit/deny/domain default.

## D-1632 — MVP is Databricks-centered for canonical Delta state
**Status:** Accepted

This does not require every runtime component to run inside Databricks.

## D-1633 — Interactive serving uses a thin stateless façade
**Status:** Accepted

UI direct unrestricted canonical-table access is not the reference pattern.

## D-1634 — External edge/control services are allowed when justified
**Status:** Accepted

External hosting does not transfer truth ownership.

## D-1635 — Heavy workers/orchestration are separated from synchronous requests
**Status:** Accepted

No universal queue/workflow product is selected.

## D-1636 — Active-control failure domain is independently protected
**Status:** Accepted

Passive/model workload saturation cannot silently alter control behavior.

## D-1637 — Deployment environments isolate credentials/data/control
**Status:** Accepted

Lower environments cannot mutate production evidence/control.

## D-1638 — Runtime configuration is revision-addressed
**Status:** Accepted

Historical behavior binds the effective revision.

## D-1639 — Rollback changes runtime, not canonical history
**Status:** Accepted

Actions/evidence from superseded deployment remain.

## D-1640 — Capability inventory is verified at startup and periodically
**Status:** Accepted

Stale deployment assumptions are not permanent facts.

## D-1641 — Optional integrations are capability-gated
**Status:** Accepted

Absence degrades only dependent propositions/features.

## D-1642 — Runtime health is multidimensional
**Status:** Accepted

No universal platform/integration/control health score.

## D-1643 — Integration-health telemetry operationalizes Group 04 dimensions
**Status:** Accepted

Authn/authz/quota/lag/checkpoint/pagination/schema/parser/persistence/coverage/freshness remain distinct.

## D-1644 — Canonical persistence and projection health are separate
**Status:** Accepted

Healthy API/index cannot mask persistence failure and vice versa.

## D-1645 — Reasoning health is separate from evidence sufficiency
**Status:** Accepted

Runtime failure is not epistemic status.

## D-1646 — Model/search health is optional and independently observable
**Status:** Accepted

Outage degrades convenience rather than canonical truth/basic answerability.

## D-1647 — Active-control health exposes each stage
**Status:** Accepted

Decision/delivery/acceptance/enforcement/execution/prevention are not one status.

## D-1648 — SLOs are service-class and deployment-profile specific
**Status:** Accepted

Numeric targets belong to measured deployment ADRs.

## D-1649 — Acquisition/serving/control latency is decomposed
**Status:** Accepted

Source publication lag is not collector or UI latency.

## D-1650 — Capacity models bursty service-class workloads
**Status:** Accepted

Averages alone are insufficient.

## D-1651 — Backpressure sheds eligible optional work first
**Status:** Accepted

Required evidence/control promises cannot disappear silently.

## D-1652 — Source/API quota state is first-class operational telemetry
**Status:** Accepted

Quota state cannot become domain absence.

## D-1653 — Databricks acquisition is bulk/reconciliation/selective where possible
**Status:** Accepted

Exact limits remain target capability facts.

## D-1654 — GitHub acquisition combines scoped incremental paths with reconciliation
**Status:** Accepted

Webhook silence remains insufficient for completeness.

## D-1655 — Quota exhaustion degrades coverage/freshness explicitly
**Status:** Accepted

Strong negatives are withheld when required coverage is lost.

## D-1656 — Product costs are attributable by bounded operational dimensions
**Status:** Accepted

Acquisition/compute/storage/model/control drivers are observable where measurable.

## D-1657 — Budget policy cannot redefine evidence/control semantics
**Status:** Accepted

Cost optimization is explicit policy, never epistemic shortcut.

## D-1658 — Retention/archive cost remains subordinate to promised evidence obligations
**Status:** Accepted

Pinned exact evidence cannot be downsampled by convenience.

## D-1659 — Backup/DR restores canonical state and rebuilds derived stores
**Status:** Accepted

Restoration cannot rewrite missing history.

## D-1660 — GAP-009-32–40 have explicit Group 08 treatment
**Status:** Accepted

Operational feasibility gaps are resolved/scoped without weakening prior contracts.

## D-1661 — No new product concept is required
**Status:** Accepted

Existing concepts and ARCH contracts are sufficient for serving/runtime packaging.

## D-1662 — Group 08 accepts ARCH-421–ARCH-500 and promotes Group 09
**Status:** Accepted — Group 08 closure

SSO08-01–SSO08-120 pass. Group 09 — Architecture Consolidation, Validation & Phase 010 Exit is next.
