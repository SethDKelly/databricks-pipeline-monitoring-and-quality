# Repository Agent / Developer Instructions

## Authority and current mode

The `docs/` tree remains the product/design system of record.

Live **design-phase** progression is declared only in [`docs/README.md#current-state`](docs/README.md#current-state). Phase 010 — Technical Architecture is complete and **ARCH-001–ARCH-500 are frozen**.

Live **implementation-program** progression is declared only in [`docs/implementation/README.md`](docs/implementation/README.md).

The immediate enabling work is the **Agentic Development Foundation**, whose accepted design and execution sequence live in [`docs/agentic_development_foundation/README.md`](docs/agentic_development_foundation/README.md). Implementation 001 follows only after the implemented foundation passes its execution exit review.

For implementation-specific engineering rules, read [`docs/implementation/AGENTS.md`](docs/implementation/AGENTS.md) before adding product code. For compact task-to-contract routing, use [`docs/implementation/agent_reference_index.md`](docs/implementation/agent_reference_index.md); ADF execution will integrate this with a portable OKF v0.2 knowledge plane.

Cursor project rules under `.cursor/rules/` are deliberately scoped and reference-driven. They are not a second system of record. Future Claude/Codex adapters must follow the same rule: tool-specific mechanics may not become competing semantic authority.

## Shared agent authority

The accepted shared agent scope policy is [`docs/agentic_development_foundation/authority_scope_policy.md`](docs/agentic_development_foundation/authority_scope_policy.md).

When repository/tool instructions conflict, preserve this precedence:

1. canonical DMTZ contracts and `docs/` authority;
2. root `AGENTS.md`;
3. live implementation/active-package or active-ADF status;
4. accepted Agentic Development Foundation mechanics;
5. tool-specific repository adapters;
6. personal/user-level tool preferences and tool memory.

A human request establishes the current task and requested action, but does not silently weaken higher repository/contract authority.

## Current agentic boundary

The accepted Agentic Development Foundation is **human-directed**, not autonomous.

Use these action classes:

- **A1 — read/review/plan:** inspect and report; do not edit unless the human also requests changes.
- **A2 — change/build/fix:** perform in-scope repository edits, directly necessary tests/fixtures/status/traceability updates, and safe non-destructive validation without repetitive permission prompts.
- **A3 — external/destructive/scope-expanding:** require explicit task-specific human authorization plus applicable repository/team gates.
- **A4 — architecture/semantic change:** follow DMTZ change control; never weaken contracts silently.

Agents may inspect, edit and run safe/non-destructive validation within a task a human explicitly requests. They must not infer authority to create unrelated follow-on work, spawn implementation agents, reprioritize the backlog, merge/deploy unattended, or reopen architecture autonomously.

Completing a requested group authorizes reporting the next eligible step; it does **not** authorize starting that step automatically.

During ADF-A–ADF-H execution, repository changes may add agent configuration, OKF routing knowledge, portable workflow/skill definitions and deterministic validation helpers. Product/application implementation remains planned under Implementation 001 unless the user explicitly advances it separately.

Tool memory, auto-memory, chat history and generated summaries are advisory only. A fact required for future correctness must be promoted into an appropriate repository artifact.

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
- active-control callbacks/commands authenticated and replay-protected when that implementation is enabled;
- agent knowledge, skills, rules, memory and tool configuration are never independent authorization sources.

## Change-control order

When target-environment reality conflicts with implementation plans:

1. adjust concrete technology/configuration inside frozen contracts;
2. explicitly narrow the deployment/product capability if the source cannot support the stronger proposition;
3. add instrumentation/attestation when the stronger proposition is required;
4. raise an architecture change request only when no compliant realization exists;
5. reopen functional semantics only when the product requirement itself intentionally changes or a required real-world scenario truly cannot be represented.

Never silently weaken a contract in code or agent configuration and then treat that behavior as the new architecture.
