# 001-C — Executable Invariants, Golden Fixtures & Architecture Conformance Tests

**Status:** Planned

## Goal

Turn DMTZ's highest-value architecture rules into executable guardrails before adapters/persistence make incorrect assumptions expensive.

## Conformance library

Create deterministic validators/test helpers for at least these rules:

1. name equality cannot establish Entity Identity;
2. timestamp proximity cannot establish deployment/run/source identity;
3. missing evidence cannot become `false`, `zero`, `no event`, `not exposed` or another negative fact;
4. current state cannot be projected backward into an earlier knowledge cut;
5. copied/common-derived evidence is not automatically independent corroboration;
6. source availability does not grant Assertion Authority;
7. Responsibility/title/admin privilege does not grant Assertion Authority or Capability Authorization;
8. Observation cannot directly carry Assessment truth;
9. Expectation cannot be derived silently from Baseline regularity;
10. successful execution cannot imply freshness or data quality;
11. Lineage reachability cannot imply exposure/Impact;
12. correlation/deployment timing cannot confirm cause;
13. unknown/conflicting/unavailable cannot be normalized to a benign default;
14. renderer/model output cannot strengthen Statement IR;
15. current requester authorization cannot rewrite retained historical evidence/communication.

Only the subset with implemented primitive types needs a production validator in 001; all rules should have fixture/test representation or explicit deferred mapping.

## Golden fixtures

Create human-readable + machine-readable fixtures for:

- entity rename same identity with evidence;
- same name but new/recreated entity;
- observation known at event time but collected late;
- corrected observation superseding an earlier record;
- no observation because acquisition failed;
- fresh observation against freshness Expectation;
- stale observation against freshness Expectation;
- successful job execution plus stale data;
- current retrospective evidence unavailable at earlier `K`;
- unsupported source capability.

## Scenario manifest

Create a manifest that maps fixture/test IDs to design contract/scenario references and expected semantic result.

Example shape:

```yaml
id: IMP001-FRESH-004
contracts: [REF-004, REF-006, HLTH-030]
input_fixture: late_observation.yaml
expected:
  as_known_by_k1: unknown
  retrospective_k2: stale
```

Exact contract IDs must be verified against the accepted docs when implemented.

## Test design rule

Expected results should compare structured semantic objects/IR. Prose snapshots are secondary and should not be the primary correctness oracle.

## Acceptance gates

- fixture suite runs in CI with no Databricks dependency;
- every 001 semantic non-negotiable has at least one adversarial test;
- deliberately illegal states are rejected or represented as explicit unresolved/error state;
- test names/metadata contain traceability to accepted design contracts;
- model/search/network outages are irrelevant to the deterministic conformance suite.
