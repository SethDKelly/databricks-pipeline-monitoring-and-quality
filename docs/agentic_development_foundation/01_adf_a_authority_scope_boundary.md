# ADF-A — Authority, Scope & Human-Directed Operating Boundary

**Status:** PLANNED / READY TO EXECUTE

## Objective

Establish one authoritative behavioral model for coding agents before any tool-neutral knowledge bundle or portable workflow is introduced.

The foundation must make it impossible to interpret tool choice as permission to change project semantics, execution scope, review requirements or approval boundaries.

## Required outcomes

### 1. Shared authority hierarchy

Codify and test this precedence:

1. canonical DMTZ contracts and `docs/`;
2. root `AGENTS.md`;
3. live implementation status/package;
4. Agentic Development Foundation mechanics;
5. tool-specific adapters;
6. personal/user-level tool preferences.

A lower layer may add mechanics or presentation guidance but may not weaken a higher layer.

### 2. Human-directed execution contract

For this foundation, an agent acts only within a task a human explicitly starts and scopes.

Allowed without additional approval once a human requests implementation/review work:

- inspect repository files and history;
- follow canonical references;
- edit files within the requested task scope;
- run non-destructive local/static tests and validation;
- report assumptions, failures and residual work.

Not authorized by this foundation:

- inventing or reprioritizing work beyond the requested task;
- starting unrelated follow-on tasks automatically;
- spawning other agents to implement portions of the work;
- merging or deploying without the normal human/team process;
- changing product/architecture contracts because implementation is difficult;
- performing destructive/external actions merely because a tool technically permits them.

### 3. Agent/tool neutrality

The repository must not define one agent as semantically privileged. A developer may select Cursor, Claude Code or Codex according to personal/team needs.

Tool-specific capabilities may improve ergonomics, but acceptance remains repository-based: files changed, tests, traceability and review—not which agent produced them.

### 4. No hidden memory authority

Tool memory, auto-memory, chat history and generated summaries are advisory context only.

A fact needed for future implementation correctness must be promoted into the canonical repository artifact appropriate to its type: code, test, ADR, implementation status, OKF routing entry or documentation.

### 5. Explicit action classes

ADF execution should encode a compact action policy usable across tool adapters:

- **read/review/plan** — inspect and report; no implementation unless asked;
- **change/build/fix** — perform in-scope repository edits plus safe validation;
- **external/destructive/scope-expanding** — stop for explicit human approval;
- **architecture/semantic change** — follow DMTZ change-control regardless of tool.

## Deliverables

- revised/shared agent authority wording if required;
- an agentic scope policy document usable by all adapters;
- tool-adapter tests/checklist proving no adapter contradicts the shared policy;
- documented distinction between human-directed agentic development and deferred autonomy.

## Acceptance scenarios

ADF-A passes when:

- Cursor, Claude and Codex receive materially equivalent scope/authority instructions;
- a request to review does not silently become a request to edit;
- a request to implement allows safe in-scope edits/tests without repetitive permission prompts;
- a tool-specific instruction cannot override frozen DMTZ semantics;
- an agent encountering an impossible architecture constraint follows the existing change-control order instead of weakening behavior;
- no persistent tool memory is treated as canonical state.

## Non-goals

ADF-A does not select coding models, automate task assignment, define concurrent-agent locks, or introduce autonomous agents.
