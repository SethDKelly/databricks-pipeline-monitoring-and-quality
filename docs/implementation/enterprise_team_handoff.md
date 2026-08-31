# Enterprise Team Handoff

**Status:** Ready for team onboarding

## What the team receives

The repository now contains:

- complete functional semantics and concept synchronizations;
- evidence/time/causality/governance/health/operational/Explanation contracts;
- source-specific integration feasibility and residual-gap analysis;
- frozen ARCH-001–ARCH-500 technical architecture;
- target/MVP/enterprise topology and trust/data-store ownership models;
- an implementation sequence through production graduation;
- a fully designed Implementation 001 walking skeleton.

The team should not need to rediscover the product truth model before coding.

## Minimum team roles

A small pilot can combine roles, but responsibilities should exist explicitly:

| Responsibility | Typical owner |
|---|---|
| Architecture/contract stewardship | Principal/Staff engineer or architect |
| Python/domain implementation | Senior backend/data-platform engineer |
| Databricks/Delta/source integration | Data/platform engineer |
| GitHub/CI/CD/automation | Platform/DevOps engineer |
| Automated scenario/contract testing | SDET/quality engineer or shared engineering responsibility |
| Security/IAM/review | Security/platform engineer |
| UI/API product experience | Backend + frontend engineers during Implementation 006 |
| Operational readiness/SLO/cost | SRE/platform team |
| Pilot subject-matter validation | Data owners/engineers/business analyst representatives |

For Implementation 001, one strong senior engineer plus architecture review can start; enterprise execution benefits from at least a platform/data engineer and a quality-minded reviewer.

## Required access before coding

The team should obtain:

- repository write/PR access;
- a non-production Databricks workspace/account target;
- a dedicated DMTZ development catalog/schema namespace;
- permission to inspect the exact Databricks system/API surfaces selected for the pilot;
- a service principal/workload identity suitable for CI/CD;
- representative Databricks jobs/pipelines/data assets;
- representative GitHub repositories/workflows used by the pilot pipelines;
- organization contacts able to define pilot Monitoring Scope, Assertion Authority and disclosure rules;
- a path to create test data/fixtures without exposing restricted production data.

## Recommended pilot topology

Choose a deliberately small topology:

```text
SOURCE_A ─┐
          ├── TRANSFORM_C ──> CONSUMER_D
SOURCE_B ─┘

SOURCE_E ──> TRANSFORM_F
```

The pilot should make it possible to demonstrate:

- normal successful execution;
- stale upstream input;
- successful execution with poor data quality;
- a known deployment/change event;
- downstream reachability versus actual consumption/exposure;
- at least one late-arriving or corrected piece of evidence;
- a business-facing and engineering-facing Explanation over the same underlying evidence by Implementation 006/008.

## First-week onboarding sequence

1. Read Phase 010 `implementation_handoff.md`, `target_reference_architecture.md`, `mvp_topology.md`, `build_vs_integrate_decisions.md`, `data_store_ownership_map.md`, `adr_summary.md`, `architecture_risk_assumption_register.md`, and the original MVP boundary.
2. Read `docs/implementation/README.md`, `AGENTS.md`, and Implementation 001 README.
3. Verify the development Databricks/GitHub capability inventory rather than assuming public documentation equals deployment capability.
4. Select and record the concrete Python/runtime/tooling baseline for the target environment.
5. Execute 001-A before adding domain/application behavior.
6. Establish the initial scenario-fixture catalog and contract traceability before implementing adapters.

## What not to do on day one

Do not begin with:

- a polished UI;
- an LLM/chat interface;
- a graph/vector database;
- active Gate/Safeguard enforcement;
- every Databricks system table;
- Collibra/Immuta integration;
- microservice decomposition;
- broad production infrastructure.

The first objective is to prove the evidence-to-answer spine end to end.

## Escalation contract

If target-environment reality prevents an accepted architecture from being realized, document the exact constraint and follow implementation change control. Do not replace an unsupported strong proposition with a weaker source while continuing to label it as the original proposition.
