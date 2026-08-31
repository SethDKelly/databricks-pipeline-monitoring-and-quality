# Implementation Agent / Developer Instructions

## Authority

Implementation work is governed by:

1. accepted functional/integration architecture contracts through ARCH-500;
2. Phase 010 Group 09 reference architecture and implementation handoff;
3. `docs/implementation/README.md` for live implementation-program status;
4. the active implementation package README/group plan;
5. implementation ADRs that select concrete tools without changing accepted semantics.

If code and accepted contracts disagree, the code is presumptively wrong until an explicit change request is accepted.

## Cursor / agent context discipline

Use `docs/implementation/agent_reference_index.md` as the compact routing surface for implementation agents.

For routine work, prefer this context order:

**root `AGENTS.md` → active scoped `.cursor/rules/*.mdc` rule → active implementation package/group plan → one or two domain architecture/reference documents → exact stable contract IDs/tests as needed.**

Do not preload all SYN/REF/AUTH/HLTH/OPS/EXPL/INTG/ARCH documentation. Search exact stable IDs when deeper semantics are required.

Historical phase-specific Cursor rules have been removed from the active `.cursor/rules` set. Their authoritative semantics remain in `docs/` and their prior rule text remains available through Git history.

## Code is now allowed — within active implementation scope

Phase 010 is complete. Application code, schemas, tests, Databricks resources, CI/CD and infrastructure changes may now be introduced **only when they are within the active implementation package and its acceptance gates**.

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
- control callbacks/commands authenticated and replay-protected where applicable.

## Change escalation

A developer who cannot implement a contract should record:

- exact contract(s) affected;
- target environment facts;
- attempted compliant realizations;
- why they fail;
- whether instrumentation or capability narrowing solves the problem;
- proposed architecture change only if necessary.

Implementation convenience by itself is not sufficient reason to reopen architecture.
