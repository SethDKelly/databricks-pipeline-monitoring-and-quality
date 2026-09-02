# Implementation Agent / Developer Instructions

## Authority

Implementation work is governed by:

1. accepted functional/integration architecture contracts through ARCH-500;
2. Phase 010 Group 09 reference architecture and implementation handoff;
3. root `AGENTS.md` plus `docs/agentic_development_foundation/authority_scope_policy.md` for shared agent action/scope behavior;
4. `docs/implementation/README.md` for live implementation-program status;
5. the active implementation package README/group plan;
6. implementation ADRs that select concrete tools without changing accepted semantics.

If code and accepted contracts disagree, the code is presumptively wrong until an explicit change request is accepted.

## Agent context and action discipline

Use `docs/implementation/agent_reference_index.md` as the compact routing surface for implementation agents.

For routine work, prefer this context order:

**root `AGENTS.md` → shared ADF-A scope policy when action/scope is material → active scoped tool rule/adapter → active implementation package/group plan → one or two domain architecture/reference documents → exact stable contract IDs/tests as needed.**

Human-directed action follows ADF-A:

- A1 review/inspect/plan does not authorize edits;
- A2 change/build/fix authorizes in-scope edits, directly necessary tests/status/traceability and safe validation;
- A3 external/destructive/scope-expanding actions require explicit task-specific human authorization plus repository/team gates;
- A4 architecture/semantic changes follow DMTZ change control.

Completing one implementation group does not authorize beginning the next group automatically.

Do not preload all SYN/REF/AUTH/HLTH/OPS/EXPL/INTG/ARCH documentation. Search exact stable IDs when deeper semantics are required.

Historical phase-specific Cursor rules have been removed from the active `.cursor/rules` set. Their authoritative semantics remain in `docs/` and their prior rule text remains available through Git history.

## Code is allowed only within active implementation scope

Phase 010 is complete, but the current repository is completing the Agentic Development Foundation before Implementation 001-A begins. Application code, schemas, tests, Databricks resources, CI/CD and infrastructure changes may be introduced **only when they are within an explicitly active implementation package and its acceptance gates**.

ADF execution alone does not activate DMTZ product/application implementation.

Do not use implementation permission as permission to redesign the product model.

## Engineering discipline

- Prefer a modular monolith/package structure initially; split deployable services only for demonstrated runtime/security/failure-domain needs.
- Keep domain contracts free of Databricks/GitHub vendor object shapes.
- Preserve source-native identifiers and provenance separately from DMTZ canonical identities.
- Use deterministic evaluation for truth/authority/coverage/control decisions.
- Make optional model/search code removable without changing canonical results.
- Treat derived graph/search/cache/read-model state as rebuildable.
- Never use Delta time travel as the product's sole historical/as-known semantics.
- Never use UI/application cache state as canonical truth.
- Never encode a negative proposition from an adapter error, missing page, permission denial, retention expiry, unsupported surface or unknown coverage.
- Never infer identity/deployment/run correlation from names or timestamp proximity alone.
- Never grant authority because a source arrived first, is newest, is most numerous, or is technically privileged.

## Test discipline

Every merged behavior that realizes a material accepted contract should have the lowest-cost executable test that proves it:

- unit/property tests for pure invariants;
- contract tests for schemas/state machines;
- persistence tests for bitemporal/correction/replay behavior;
- adapter tests for source coverage/error semantics;
- integration tests for cross-source/canonical flows;
- scenario tests for product semantics;
- end-to-end tests only where the boundary itself is under test.

Design scenario PASS from prior phases is not executable proof. Implementation exit reviews must point to actual automated/manual execution evidence.

## Security discipline

- no long-lived credentials in source control;
- workload identities/service principals for automation;
- least privilege by workload function;
- current Capability Authorization/disclosure at serving boundaries;
- secrets and sensitive telemetry minimized/redacted;
- tenant/environment separation explicit;
- control callbacks/commands authenticated and replay-protected where applicable;
- agent/tool memory remains noncanonical.

## Change escalation

A developer who cannot implement a contract should record:

- exact contract(s) affected;
- target environment facts;
- attempted compliant realizations;
- why they fail;
- whether instrumentation or capability narrowing solves the problem;
- proposed architecture change only if necessary.

Implementation convenience by itself is not sufficient reason to reopen architecture.
