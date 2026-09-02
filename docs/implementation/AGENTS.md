# Implementation Agent / Developer Instructions

**ADF status mirror: COMPLETE ADF-A–ADF-F; IN EXECUTION ADF-G.**

## Authority

Implementation work is governed by:

1. accepted functional/integration/architecture contracts through ARCH-500;
2. Phase 010 Group 09 reference architecture and implementation handoff;
3. root `AGENTS.md` and the ADF authority/scope policies;
4. `docs/implementation/README.md` for live implementation-program status;
5. the active implementation package README/group plan;
6. implementation ADRs that select concrete technology without changing accepted semantics.

If code and accepted contracts disagree, code is presumptively wrong until explicit change control says otherwise.

## Context and action discipline

Use the shortest authoritative context path from ADF-E:

**root `AGENTS.md` → matching `.agents/skills/` workflow when useful → explicit path/stable ID directly when known; otherwise `knowledge/index.md` → one relevant route → active implementation group → canonical source → exact contracts/tests as needed.**

Use `scripts/agentic/resolve_stable_id.py` for exact occurrence discovery when helpful. Do not choose the first search hit as semantic authority; validate accepted range and owning canonical source.

Human-directed action follows ADF-A:

- A1 review/inspect/plan does not authorize edits;
- A2 change/build/fix authorizes in-scope edits plus directly necessary tests/status/traceability and safe validation;
- A3 external/destructive/scope-expanding actions require explicit task-specific human authorization plus normal gates;
- A4 architecture/semantic changes follow DMTZ change control.

Completing one group does not authorize beginning the next group automatically.

## Current implementation boundary

The repository is still completing the Agentic Development Foundation. ADF-A–ADF-F are complete; **ADF-G is in execution with provider runtime smoke evidence still pending**. Product/application implementation begins only after ADF-G, ADF-H, the full foundation exit, and an explicitly active implementation package.

ADF work may change agent configuration, knowledge/workflow routing, validation helpers and related documentation; it does not itself activate product code, Databricks resources, product schemas, or production infrastructure.

## Agentic conformance

For agent-facing repository changes run:

```bash
python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md
```

The result is **agentic configuration conformance**, not DMTZ domain health or product/runtime proof. Provider runtime evidence is recorded independently in `docs/agentic_development_foundation/runtime_compatibility_evidence.json`.

## Engineering discipline once implementation activates

- prefer a modular package/application initially; split services only for demonstrated runtime/security/failure-domain needs;
- keep domain contracts vendor-neutral and source-native IDs/provenance in adapters;
- use deterministic evaluation for truth/authority/coverage/control decisions;
- keep model/search optional and unable to manufacture canonical results;
- treat graph/search/cache/read models as rebuildable projections;
- do not use Delta time travel as the sole historical/as-known definition;
- do not use UI/cache state as canonical truth;
- never encode a negative proposition from adapter error, missing page, permission denial, retention expiry, unsupported surface, or unknown coverage;
- never infer identity/deployment/run association from names or timestamp proximity alone;
- never grant authority because a source arrived first, is newest, most numerous, or technically privileged.

## Test discipline

Every material accepted behavior should have the lowest-cost executable proof appropriate to it: unit/property, contract/schema, persistence, adapter, integration, product scenario, then end-to-end only where the boundary itself is under test.

Design-scenario PASS is not executable proof. Maintain stable-ID/scenario → executable-test traceability.

## Security and change escalation

- no secrets/credentials in source control or agentic artifacts;
- least privilege and workload identities for automation;
- current Capability Authorization/disclosure at serving boundaries;
- sensitive telemetry minimized/redacted;
- agent/tool memory remains noncanonical.

When a contract cannot be implemented, record the exact contracts, target facts, attempted compliant realizations, instrumentation/capability-narrowing options, and raise architecture change only if necessary. Implementation convenience is not sufficient reason to reopen architecture.