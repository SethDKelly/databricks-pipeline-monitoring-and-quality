# Phase 010 Group 09 — Architecture Decision / ADR Summary

**Status:** FROZEN — Phase 010

The `ARCH-###` contracts and Phase 010 decision records are the detailed system of record. This summary identifies the major architectural choices an implementation team must preserve.

| ADR summary | Frozen choice | Primary contract range |
|---|---|---|
| ADR-010-01 Architecture facts | Separate public/vendor facts, target-environment facts, organization requirements, architecture assumptions and unknowns | ARCH-001–032 |
| ADR-010-02 Service classes | Use SC-01–SC-06; reject one universal freshness/latency/retention SLO | ARCH-001–032, 422, 480–484 |
| ADR-010-03 Canonical persistence | Delta-first canonical structured evidence/governance history | ARCH-033–080 |
| ADR-010-04 Payload retention | Selective/minimized object payload retention; no wholesale raw copying | ARCH-033–080 |
| ADR-010-05 Historical semantics | Non-rewriting multi-coordinate history; Delta time travel is not product replay | ARCH-033–080, 300–315 |
| ADR-010-06 Derived stores | Graph/search/vector/serving caches are rebuildable projections | ARCH-033–080, 281–290, 424, 436–439 |
| ADR-010-07 Identity | Canonical tenant-scoped Entity/Principal identities with revisioned source bindings | ARCH-081–132 |
| ADR-010-08 Monitoring Scope | Organization-owned scope/materialization distinct from discoverability/access | ARCH-081–132 |
| ADR-010-09 Assertion Authority | Structured proposition/facet/context/time authority policy-as-data | ARCH-081–132 |
| ADR-010-10 Capability Authorization/disclosure | Exact action/subject/context/time/detail authorization; current/historical and internal/requester permissions distinct | ARCH-081–132, 441–460 |
| ADR-010-11 Acquisition | Reconciliation-first hybrid acquisition; incremental/stream/webhook paths are accelerators | ARCH-133–190 |
| ADR-010-12 Acquisition provenance | Durable run/attempt/request/page/window/checkpoint/parser/coverage records; checkpoint after durable evidence | ARCH-133–190 |
| ADR-010-13 Integration health | Multidimensional source/integration health; no global integration score | ARCH-133–190, 473–479 |
| ADR-010-14 Runtime provenance | Run-specific implementation/input/output manifests with unknown facets preserved | ARCH-191–230 |
| ADR-010-15 Measurements / health | Exact target/definition/window/source attribution; Baseline/Expectation/Assessment remain separate | ARCH-231–250 |
| ADR-010-16 Lineage / Impact | Typed temporal Lineage and hop-specific encounter/exposure/effect/consequence; no transitive Impact | ARCH-251–274 |
| ADR-010-17 Investigation | Canonical Investigation/lead/claim workflow independent from ticket/chat/model session | ARCH-275–280 |
| ADR-010-18 Graph/retrieval | Delta-backed derived graph MVP; exact retrieval before semantic/vector candidate recall | ARCH-281–299 |
| ADR-010-19 Causality | Deterministic Causal Claim state; confirmation remains REF-017 + AUTH-034 gated | ARCH-300-range causal contracts |
| ADR-010-20 Historical replay | Availability-by-K canonical replay; current retrospective and authentic prior communication remain distinct | ARCH-300–330 |
| ADR-010-21 Explanation IR | Statement IR / Answer IR before rendering; exact basis/limitations retained | ARCH-320–340 |
| ADR-010-22 Model assistance | Provider-neutral optional model assistance; no model truth/authority/control role; deterministic fallback | ARCH-340–350 |
| ADR-010-23 Active-control boundary | Gate/Safeguard opt-in over passive monitoring and independently modeled | ARCH-351–420 |
| ADR-010-24 Gate architecture | Opportunity-specific deterministic criteria/readiness/decision/delivery/enforcement/execution with explicit override/fallback | ARCH-351–390 |
| ADR-010-25 Safeguard architecture | Path/cohort-specific enforcement and REF-028 opportunity/alternate-path prevention manifest | ARCH-391–420 |
| ADR-010-26 Serving boundary | Thin/stateless authorization-aware façade over canonical/derived state; UI has no unrestricted raw canonical access | ARCH-421–440 |
| ADR-010-27 Runtime security | Distinct human/workload identities; least privilege; short-lived federation preferred; secret minimization; authenticated callbacks | ARCH-441–460 |
| ADR-010-28 Reference deployment | Databricks-centered canonical evidence + portable stateless service/edge components | ARCH-461–472 |
| ADR-010-29 Active-control isolation | SC-06 protected from optional model/heavy interactive resource/failure domains as required | ARCH-432, 466, 484–487 |
| ADR-010-30 Observability | Separate acquisition, persistence, projection, serving, reasoning/replay, optional model/search and control health | ARCH-473–484 |
| ADR-010-31 Capacity / quota | Priority/backpressure plus explicit Databricks/GitHub quota-aware collection; quota loss affects coverage/freshness, not truth | ARCH-485–491 |
| ADR-010-32 Cost | Attribute acquisition/compute/storage/model/control costs; budget policy cannot silently weaken semantic promises | ARCH-492–497 |
| ADR-010-33 Backup/DR/residency | Protect canonical/promised retained material; derived stores rebuildable; restore gaps/provenance explicit | ARCH-498 |
| ADR-010-34 Optional integrations | Capability-gated Collibra/Immuta/consumer/business/model/search extensions; no fabricated defaults | ARCH-472, 499 |
| ADR-010-35 Group 09 freeze | ARCH-001–500 is final Phase 010 range; no ARCH-501 needed | Group 09 exit |
| ADR-010-36 MVP boundary | Passive Databricks/GitHub-centered monitoring/reasoning/replay MVP; active control/model/graph DB/Collibra/Immuta not mandatory | Group 09 MVP topology |

## Decision precedence

If an implementation ADR conflicts with this Phase 010 summary, the detailed accepted ARCH contract and earlier SYN/REF/AUTH/HLTH/OPS/EXPL/INTG semantic contract take precedence.

A later implementation ADR may select a concrete product/runtime and numeric SLO. It may not redefine the underlying proposition, evidence burden, authority, time, disclosure or control semantics without an explicit architecture/product-design reopening.
