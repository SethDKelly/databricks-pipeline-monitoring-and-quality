# Executable Validation Strategy

## Objective

Convert the extensive design scenario corpus into executable evidence that implementation preserves the accepted product/architecture contracts.

## Test pyramid

### Unit / property tests

Use for pure rules such as:

- status transitions;
- time interval containment;
- evidence applicability;
- identity/version constraints;
- unknown/partial/conflict propagation;
- no implicit status strengthening.

### Contract/schema tests

Use for:

- canonical identifiers and envelopes;
- schema-version compatibility;
- Statement IR / Answer IR;
- Monitoring Scope / authority / authorization rules;
- adapter interfaces;
- Gate/Safeguard state machines when enabled.

### Persistence tests

Use for:

- append/correct/supersede;
- late evidence;
- knowledge-cut replay;
- archive/restore;
- idempotent persistence;
- migration compatibility.

### Adapter tests

Use mocked/sandbox vendor surfaces to prove:

- pagination completeness;
- rate limiting/throttle state;
- authentication/authorization failures;
- schema drift;
- redelivery/idempotency;
- delayed publication;
- partial scope/permission filtering;
- retry/checkpoint safety.

### Integration tests

Use real non-production systems for:

- Databricks capability discovery;
- Databricks run/task/data evidence;
- GitHub revision/workflow/deployment evidence;
- cross-source correlation where instrumentation exists;
- workload identity/CI/CD;
- Delta canonical persistence.

### Product scenario tests

Exercise semantic slices such as:

- stale upstream;
- successful run / poor quality;
- deployment-correlated change without causal promotion;
- planned structural change and reference transition;
- reachability versus exposure;
- multiple contributors;
- historical knowledge correction;
- policy-aware Explanation.

### End-to-end tests

Reserve for boundaries that only E2E can prove:

- authenticated requester → authorized Explanation;
- deployment → acquisition → canonical state → answer;
- historical replay with retained/corrected evidence;
- production-like failure/degradation behavior;
- active-control enforcement/correlation when 010 is enabled.

## Scenario traceability

Maintain a machine-readable traceability manifest mapping:

`design scenario / contract IDs → executable test IDs → implementation package → current status → evidence/artifact`.

A scenario may map to multiple tests at different levels. Do not force every design scenario into a slow E2E test.

## Golden fixtures

Fixtures must include positive and adversarial examples. Core fixture families:

- canonical entity rename/recreate/succession;
- source-local identity collisions;
- late and corrected evidence;
- conflicting authority;
- authorization/disclosure variation;
- missing/partial pagination;
- stale source data;
- successful execution with unhealthy data;
- Lineage without exposure;
- exposure without business consequence;
- multiple plausible causes;
- retained versus reconstructed historical Explanation.

Fixture expected results should be semantic states/IR, not prose strings whenever possible.

## Exit evidence

Implementation package exit reviews must identify:

- automated suites run and pass/fail counts;
- real integration targets used;
- known skipped/unsupported scenarios and reasons;
- performance/security/DR evidence where applicable;
- residual implementation debt.

A design document saying `PASS` is not sufficient after implementation begins.
