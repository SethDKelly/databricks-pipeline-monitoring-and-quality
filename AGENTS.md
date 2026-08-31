# Repository Agent / Developer Instructions

## Authority and current mode

The `docs/` tree remains the product/design system of record.

Live **design-phase** progression is declared only in [`docs/README.md#current-state`](docs/README.md#current-state). Phase 010 — Technical Architecture is complete and **ARCH-001–ARCH-500 are frozen**.

Live **implementation-program** progression is declared only in [`docs/implementation/README.md`](docs/implementation/README.md). Implementation 001 is the next executable work package.

For implementation-specific engineering rules, read [`docs/implementation/AGENTS.md`](docs/implementation/AGENTS.md) before adding code.

## Code is now permitted within active implementation scope

The repository has moved beyond documentation-only technical design. Application code, tests, schemas, Databricks resources, CI/CD and implementation infrastructure may now be added when they are explicitly owned by the active implementation package.

Do **not** interpret this as permission to redesign accepted semantics by implementation convenience.

If code conflicts with an accepted functional/integration/architecture contract, the code is presumptively wrong until an explicit change request is accepted.

## Frozen incoming contract stack

Implementation must preserve:

- SYN-001–SYN-035;
- REF-001–REF-030;
- AUTH-001–AUTH-053;
- HLTH-001–HLTH-066;
- OPS-001–OPS-123;
- EXPL-001–EXPL-160;
- INTG-001–INTG-270;
- ARCH-001–ARCH-500.

Use the Phase 010 Group 09 implementation handoff and reference architecture as the immediate technical authority:

- [`docs/concepts/phase_010/09_architecture_consolidation_validation_exit/implementation_handoff.md`](docs/concepts/phase_010/09_architecture_consolidation_validation_exit/implementation_handoff.md)
- [`docs/concepts/phase_010/09_architecture_consolidation_validation_exit/target_reference_architecture.md`](docs/concepts/phase_010/09_architecture_consolidation_validation_exit/target_reference_architecture.md)

## Core invariants

Preserve at minimum:

- ecosystem ≠ repository;
- logical pipeline ≠ Databricks job;
- Entity Identity ≠ source-local ID/name;
- Monitoring Scope ≠ Assertion Authority ≠ Capability Authorization;
- evidence sufficiency ≠ authority ≠ authorization ≠ action/enforcement;
- source assertion ≠ authoritative assertion;
- Observation ≠ Assessment;
- Expectation ≠ Baseline;
- execution success ≠ timely run ≠ freshness ≠ structural compatibility ≠ data quality;
- missing telemetry/evidence ≠ observed absence/negative truth;
- current state ≠ historical state;
- later evidence ≠ evidence known then;
- event/effective time ≠ source availability ≠ framework knowledge/recorded time;
- Lineage ≠ exposure ≠ Impact ≠ cause;
- deployment/correlation timing ≠ causation;
- Investigation/leading hypothesis ≠ confirmed cause;
- reachability ≠ encounter/exposure;
- exposure ≠ downstream effect ≠ business consequence;
- authentication ≠ Capability Authorization;
- Capability Authorization ≠ Assertion Authority;
- current disclosure permission ≠ historical truth/communication;
- passive monitoring ≠ active Execution Gate;
- Gate readiness ≠ Gate decision ≠ enforcement ≠ actual execution;
- Safeguard proposal/configuration ≠ enforcement ≠ prevention ≠ recovery;
- model/search output cannot manufacture canonical truth, authority, evidence sufficiency, causal confirmation, Impact or control decisions;
- unknown/conflicting/stale/partial/unavailable/withheld states remain legitimate and must not be normalized to benign defaults.

Detailed semantics live in their accepted phase documents and should be referenced by stable IDs in implementation tests/ADRs rather than duplicated into new parallel truth definitions.

## Implementation engineering discipline

- Prefer a modular Python package/application initially; split deployable services only for demonstrated scale/security/latency/failure-domain needs.
- Keep canonical domain contracts vendor-neutral. Preserve Databricks/GitHub IDs and payload semantics in provenance/adapter layers.
- Use deterministic code for truth/coverage/authority/control evaluation.
- Treat graph/search/vector/cache/read models as rebuildable derived projections.
- Do not use Delta time travel as the sole product definition of historical/as-known replay.
- Do not use UI/application stores as canonical truth.
- Do not infer identity or deployment/run association from names or timestamp proximity alone.
- Do not advance source checkpoints when pagination/coverage is incomplete.
- Do not turn source outage, permission denial, throttle, schema failure or retention expiry into a negative domain fact.
- Keep optional model/search dependencies removable from deterministic MVP answerability.

## Test discipline

Design-scenario `PASS` from Phases 002–010 is not executable implementation proof.

Use the lowest appropriate executable level:

- unit/property tests for pure invariants;
- contract/schema tests for typed interfaces/state machines;
- persistence tests for correction/supersession/knowledge-cut behavior;
- adapter tests for pagination/quota/auth/schema/failure semantics;
- integration tests for real Databricks/GitHub/Delta boundaries;
- product scenario tests for accepted semantic flows;
- end-to-end tests only when the cross-boundary behavior itself is under test.

Maintain traceability from accepted contract/scenario IDs to executable tests.

## Security discipline

- no credentials/secrets in source control;
- prefer workload identity/service principals for automation;
- least privilege by workload function;
- current Capability Authorization/disclosure at serving boundaries;
- sensitive telemetry minimized/redacted;
- tenant/environment isolation explicit;
- active-control callbacks/commands authenticated and replay-protected when that implementation is enabled.

## Change-control order

When target-environment reality conflicts with implementation plans:

1. adjust concrete technology/configuration inside frozen contracts;
2. explicitly narrow the deployment/product capability if the source cannot support the stronger proposition;
3. add instrumentation/attestation when the stronger proposition is required;
4. raise an architecture change request only when no compliant realization exists;
5. reopen functional semantics only when the product requirement itself intentionally changes or a required real-world scenario truly cannot be represented.

Never silently weaken a contract in code and then treat the implementation as the new architecture.
