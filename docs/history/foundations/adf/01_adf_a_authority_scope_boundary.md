# ADF-A — Authority, Scope & Human-Directed Operating Boundary

**Status:** COMPLETE / ACCEPTED

## Objective

Establish one authoritative behavioral model for coding agents before any tool-neutral knowledge bundle or portable workflow is introduced.

The foundation must make it impossible to interpret tool choice as permission to change project semantics, execution scope, review requirements or approval boundaries.

## Required outcomes

### 1. Shared authority hierarchy

Codify and preserve this precedence:

1. canonical DMTZ contracts and `docs/`;
2. root `AGENTS.md`;
3. live implementation status/package or active ADF status;
4. Agentic Development Foundation mechanics;
5. tool-specific adapters;
6. personal/user-level tool preferences and tool memory.

A lower layer may add mechanics or presentation guidance but may not weaken a higher layer.

The accepted implementation is [`authority_scope_policy.md`](authority_scope_policy.md).

### 2. Human-directed execution contract

For this foundation, an agent acts only within a task a human explicitly starts and scopes.

Allowed without additional approval once a human requests implementation/review work:

- inspect repository files and history;
- follow canonical references;
- edit files within the requested change/build/fix scope;
- make directly necessary supporting test/fixture/status/traceability/reference changes;
- run non-destructive local/static tests and validation;
- report assumptions, failures and residual work.

Not authorized by this foundation:

- inventing or reprioritizing work beyond the requested task;
- starting unrelated follow-on tasks automatically;
- spawning other agents to implement portions of the work;
- merging or deploying without the normal explicit human/team process;
- changing product/architecture contracts because implementation is difficult;
- performing destructive/external actions merely because a tool technically permits them.

### 3. Agent/tool neutrality

The repository does not define one agent as semantically privileged. A developer may select Cursor, Claude Code or Codex according to personal/team needs.

Tool-specific capabilities may improve ergonomics, but acceptance remains repository-based: files changed, tests, traceability and review—not which agent produced them.

Actual Claude/Codex native adapter realization remains ADF-C; cross-tool execution proof remains ADF-G.

### 4. No hidden memory authority

Tool memory, auto-memory, chat history and generated summaries are advisory context only.

A fact needed for future implementation correctness must be promoted into the canonical repository artifact appropriate to its type: code, test, ADR, implementation status, OKF routing entry or documentation.

### 5. Explicit action classes

ADF-A established four shared action classes:

- **A1 — read/review/plan** — inspect and report; no implementation unless asked;
- **A2 — change/build/fix** — perform in-scope repository edits plus directly necessary supporting changes and safe validation;
- **A3 — external/destructive/scope-expanding** — require explicit task-specific human approval plus applicable repository/team gates;
- **A4 — architecture/semantic change** — follow DMTZ change control regardless of tool.

## Delivered artifacts

- [`authority_scope_policy.md`](authority_scope_policy.md) — accepted shared policy;
- [`tool_adapter_authority_checklist.md`](tool_adapter_authority_checklist.md) — adapter conformance checklist and initial surface audit;
- [`fixtures/adf_a_boundary_scenarios.yaml`](fixtures/adf_a_boundary_scenarios.yaml) — reusable behavioral fixtures;
- synchronized root `AGENTS.md`;
- synchronized `.cursor/rules/00-implementation-routing.mdc`;
- [`adf_a_execution_review.md`](adf_a_execution_review.md) — execution evidence and exit decision.

## Acceptance scenarios

ADF-A acceptance was evaluated against the shared policy and fixture set:

- review does not silently become edit — **PASS**;
- requested implementation permits safe in-scope edits/tests without repetitive permission prompts — **PASS**;
- tool-specific instructions cannot override frozen DMTZ semantics — **PASS at shared/root + current Cursor authority layer**;
- impossible architecture constraints route through existing change control — **PASS**;
- persistent tool memory is noncanonical — **PASS**;
- completing a group does not authorize the next group — **PASS**;
- autonomous delegation/merge/deploy remains excluded — **PASS**.

Native Claude/Codex adapter conformance is deliberately not claimed here; ADF-C/G own that downstream realization.

## Non-goals

ADF-A does not select coding models, automate task assignment, define concurrent-agent locks, introduce autonomous agents, build the OKF knowledge plane, or implement Claude/Codex adapter mechanics.

## Exit

**ADF-A COMPLETE / ACCEPTED.** See [`adf_a_execution_review.md`](adf_a_execution_review.md).

Next eligible groups: **ADF-B** and **ADF-C**.
