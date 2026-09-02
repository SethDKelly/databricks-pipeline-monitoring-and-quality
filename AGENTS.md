# Repository Agent / Developer Instructions

## Authority and live state

Canonical DMTZ product/design semantics live in `docs/`. Design-phase progression is owned by `docs/README.md`; implementation-program progression is owned by `docs/implementation/README.md`; Agentic Development Foundation progression is owned by `docs/agentic_development_foundation/README.md`.

**ADF status mirror: COMPLETE ADF-A–ADF-F; IN EXECUTION ADF-G.**

Phase 010 — Technical Architecture is complete and **ARCH-001–ARCH-500 are frozen**. Implementation 001 remains blocked until the Agentic Development Foundation passes its full execution exit review.

Use `knowledge/index.md` for portable discovery only when the needed canonical resource is not already known. `knowledge/` is routing, not semantic authority. Use `docs/implementation/agent_reference_index.md` as a secondary compact bridge for contract-family/path lookup.

Tool adapters are thin by design:

- Cursor: this file + scoped `.cursor/rules/*.mdc` + canonical `.agents/skills/`;
- Claude Code: `.claude/CLAUDE.md` imports this file; `.claude/commands/` bridges to `.agents/skills/`;
- Codex: this file + `.agents/skills/` natively;
- provider runtime compatibility remains ADF-G evidence, not an inference from repository configuration.

## Shared authority precedence

When instructions conflict, preserve:

1. accepted DMTZ contracts and canonical `docs/`;
2. root `AGENTS.md`;
3. live ADF / implementation status and active package/group;
4. accepted Agentic Development Foundation mechanics;
5. tool-specific repository adapters;
6. personal/user-level preferences and tool memory.

A human request establishes the current task and requested action, but does not weaken higher authority.

## Human-directed action classes

The accepted foundation is human-directed, not autonomous:

- **A1 — read/review/plan:** inspect, resolve, validate and report; do not edit unless changes are also requested.
- **A2 — change/build/fix:** perform in-scope edits, directly necessary tests/fixtures/status/traceability, and safe non-destructive validation without repetitive permission prompts.
- **A3 — external/destructive/scope-expanding:** requires explicit task-specific human authorization plus normal repository/team/environment gates.
- **A4 — architecture/semantic change:** follows DMTZ change control; never weaken accepted semantics silently.

Do not create unrelated follow-on work, reprioritize the backlog, delegate repository implementation to other agents, merge/deploy unattended, or reopen architecture autonomously. Completing one group authorizes reporting the next eligible step, not starting it.

Tool memory, auto-memory, chat history and generated summaries are advisory only. Correctness-critical facts must live in repository artifacts.

## Context and stable-reference discipline

Use the shortest authoritative path:

`human task → live authority → explicit path/ID if known; otherwise one OKF route → canonical resource → exact IDs/tests as needed`.

Do not ceremonially traverse every routing layer and do not preload all skills, knowledge concepts, phases or contract families.

Stable accepted ranges are machine-readable in `docs/agentic_development_foundation/stable_id_registry.json`:

- SYN-001–SYN-035;
- REF-001–REF-030;
- AUTH-001–AUTH-053;
- HLTH-001–HLTH-066;
- OPS-001–OPS-123;
- EXPL-001–EXPL-160;
- INTG-001–INTG-270;
- ARCH-001–ARCH-500.

Use `scripts/agentic/resolve_stable_id.py` when exact occurrence discovery is useful. Search results are **candidates**, not authority-by-search-order. Definition-like formatting does not itself establish canonical ownership. If a reference cannot be resolved, report the failure; do not reconstruct it from memory or infer that no constraint exists.

Public web is for current external/vendor facts when material, not a substitute for repository-owned DMTZ semantics.

## Knowledge and workflow discipline

The OKF bundle follows `docs/agentic_development_foundation/okf_profile.md` and maintenance rules in `okf_maintenance_policy.md` / `knowledge_maintenance_workflow.md`.

- canonical resources win over OKF summaries;
- OKF trust/lifecycle/provenance metadata is not DMTZ authority, health, evidence sufficiency or causality;
- canonical changes may create routing review candidates, not automatic OKF rewrites;
- generated or agent-facing artifacts never push semantic changes back into canonical DMTZ authority.

Canonical human-directed workflows live under `.agents/skills/<name>/SKILL.md`:

- `resolve-context` — A1 minimum context resolution;
- `implement-group` — A2 one human-selected group/task, then stop;
- `resolve-contract` — A1 accepted stable-ID/semantic lookup;
- `run-conformance` — A1 safe checks/reporting by default;
- `review-change` — A1 substantive review;
- `update-traceability` — evidence-backed A2 supporting update;
- `exit-review` — A1 evaluation; bounded A2 only when recording the requested review/status artifact.

Selecting or auto-matching a skill inside an existing human task does not create new work or permission.

## Agentic conformance

ADF-F establishes the canonical repository-owned command:

```bash
python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md
```

It validates documentation consistency, OKF routing, tool adapters, portable skills, agent-facing references, ADF status drift, fixture integrity, context budgets, ADF-G compatibility-evidence integrity and negative controls. The generated report describes **agentic configuration conformance only**. It is not DMTZ domain health, data quality, source health or production readiness.

Repository byte budgets are defined in `docs/agentic_development_foundation/context_budget.json`. Budget failure does not authorize deleting required semantics; move detail to on-demand artifacts instead.

## Frozen semantic invariants

Implementation and agent configuration must preserve at minimum:

- ecosystem ≠ repository;
- logical pipeline ≠ Databricks job;
- Entity Identity ≠ source-local identity/name;
- Monitoring Scope ≠ Assertion Authority ≠ Capability Authorization;
- evidence sufficiency ≠ authority ≠ authorization ≠ enforcement;
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
- model/search output cannot manufacture truth, authority, evidence sufficiency, causal confirmation, Impact or control decisions;
- unknown/conflicting/stale/partial/unavailable/withheld states remain first-class and must not collapse to benign defaults.

Exact semantics remain in accepted contract documents and should be cited by stable ID rather than copied into new parallel definitions.

## Implementation engineering and tests

Application/product code is not authorized merely because ADF work is active. Product implementation begins only inside an explicitly active implementation package after the foundation exit.

When implementation begins:

- prefer a modular Python package initially; split deployables only for demonstrated runtime/security/failure-domain needs;
- keep canonical contracts vendor-neutral; preserve source-native IDs/provenance in adapters;
- use deterministic code for truth/coverage/authority/control decisions;
- treat graph/search/vector/cache/read models as rebuildable projections;
- do not use Delta time travel as the sole definition of historical/as-known replay;
- do not infer identity/correlation from names or timestamp proximity;
- do not turn source outage, denial, throttle, schema failure or unknown coverage into a negative domain fact;
- keep optional model/search dependencies removable from deterministic MVP answerability.

Design-scenario PASS is not executable proof. Use the lowest appropriate executable level: unit/property, contract/schema, persistence, adapter, integration, product scenario, then end-to-end only when the cross-boundary behavior itself is under test. Maintain stable-ID → executable-test traceability.

## Security and change control

- no credentials/secrets in source control or checked-in agentic artifacts;
- least privilege and workload identities for automation;
- current Capability Authorization/disclosure at serving boundaries;
- sensitive telemetry minimized/redacted;
- agent knowledge, skills, rules, memory and tool configuration are never authorization sources.

When target reality conflicts with implementation plans:

1. adjust concrete technology/configuration within frozen contracts;
2. explicitly narrow deployment capability if necessary;
3. add instrumentation/attestation when the stronger proposition is required;
4. raise architecture change only when no compliant realization exists;
5. reopen functional semantics only for an intentional product requirement change or a truly unrepresentable required scenario.

Never silently weaken a contract in code, routing, adapter, skill or test and then treat that behavior as the new architecture.
