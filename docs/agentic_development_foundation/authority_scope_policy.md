# Agentic Authority & Human-Directed Scope Policy

**Status:** ACCEPTED — ADF-A shared policy

## Purpose

This policy is the shared operating contract for coding-agent activity in DMTZ. It defines how human task intent, repository authority, tool-specific instructions, memory, edits, validation and external actions interact.

It is intentionally tool-neutral. Cursor, Claude Code, Codex and future adapters must inherit this policy rather than create independent scope or authority models.

## Authority precedence

When instructions or context conflict, use this precedence:

1. **Canonical DMTZ product/design/architecture authority** — accepted SYN/REF/AUTH/HLTH/OPS/EXPL/INTG/ARCH contracts and the canonical `docs/` artifacts that own them.
2. **Root repository constitution** — `AGENTS.md`.
3. **Live program authority** — `docs/implementation/README.md`, the active implementation package, and the active Agentic Development Foundation group where applicable.
4. **Agentic Development Foundation mechanics** — this policy, ADF knowledge/workflow/conformance artifacts and their accepted successors.
5. **Tool-specific repository adapters** — `.cursor/`, `CLAUDE.md`, `.claude/`, Codex-specific configuration or equivalent mechanics.
6. **Personal/user-level tool preferences and tool memory** — convenience preferences only where they do not conflict with repository authority.

A lower layer may specialize mechanics or presentation. It may not weaken, redefine or silently supersede a higher layer.

### Human task intent

A human request establishes the **current task scope and requested action**, but does not silently rewrite the authority hierarchy above.

A request to implement a bounded group authorizes the in-scope repository work necessary to complete that group. A request to review does not authorize edits. A request to change architecture must still follow DMTZ change control and identify the affected contracts.

## Scope envelope

For each human-directed task, the agent should resolve a practical scope envelope from:

- requested objective;
- active ADF/implementation group;
- files/domains directly owned by the task;
- tests/validation required to prove the change;
- directly impacted status, traceability, index or reference artifacts;
- explicit exclusions in the request or repository authority.

### Necessary supporting changes

For `change/build/fix` work, the agent may make supporting changes without repetitive approval when they are directly necessary to complete the requested task, such as:

- tests and fixtures for changed behavior;
- immediately affected status/index/reference updates;
- schema/configuration changes owned by the same active group;
- documentation needed to keep the changed behavior accurately represented;
- non-destructive local/static validation helpers owned by the active task.

This does **not** authorize unrelated cleanup, backlog expansion, the next implementation group, broad refactoring without need, or speculative features.

## Action classes

### A1 — Read / review / plan

Examples: review, inspect, assess, compare, explain, plan, design, audit.

Default behavior:

- read/search repository and approved references;
- run read-only/non-destructive inspection when useful;
- report findings, recommendations, risks and next steps;
- **do not edit repository files unless the human request also asks for changes**.

### A2 — Change / build / fix

Examples: implement, create, update, refactor, fix, execute an accepted ADF/implementation group.

Default behavior:

- make in-scope repository edits;
- add/update tests, fixtures, traceability and directly impacted documentation;
- run safe, non-destructive local/static validation;
- report assumptions, failures and residual work;
- stop at completion of the requested scope rather than automatically beginning unrelated follow-on work.

The human should not be asked for repetitive permission for ordinary in-scope repository edits or safe validation already implied by the task.

### A3 — External / destructive / scope-expanding

Examples include:

- merge/rebase/force-push to protected/shared branches where not already part of the normal approved process;
- deploy/promote/release to an external environment;
- create/delete cloud or external-service resources;
- send external messages or mutate external systems outside the explicitly requested workflow;
- delete or destructively rewrite substantial repository history/state;
- access or expose secrets/sensitive data beyond the task's established permissions;
- start unrelated groups, features or backlog work;
- spawn/delegate repository implementation to other agents under this foundation.

Required behavior:

- obtain explicit human authorization for the specific external/destructive/scope-expanding action;
- continue to respect mandatory repository/team approval gates even when a human asks for the action;
- do not infer authorization from a broader implementation request.

### A4 — Architecture / semantic change

Any proposed change to accepted DMTZ semantics or frozen architecture is governed by the existing DMTZ change-control order:

1. adjust implementation/configuration within frozen contracts;
2. explicitly narrow deployment/product capability if necessary;
3. add instrumentation/attestation when a stronger proposition is required;
4. raise an architecture change request only when no compliant realization exists;
5. reopen functional semantics only when the product requirement intentionally changes or the accepted model cannot represent a required real-world scenario.

A coding agent may identify, analyze and draft an architecture change request within human-directed scope. It may not silently change contract meaning because implementation is difficult.

## Human-directed vs autonomous

**Human-directed agentic development** means:

- a human initiates the bounded task;
- the agent may execute the requested A1/A2 work to completion within scope;
- the agent may determine necessary implementation details and supporting edits inside that envelope;
- the human/team remains the source of new work selection, scope expansion and externally consequential approvals.

This is distinct from autonomy. The current foundation does not authorize agents to:

- choose the next backlog item;
- reprioritize work;
- automatically continue into the next group;
- delegate implementation to additional agents;
- operate an unattended task queue;
- merge/deploy merely because validation passes.

Deferred autonomy is tracked only in `autonomous_backlog.md`.

## Tool neutrality

No supported coding agent is semantically privileged.

Repository acceptance is based on:

- resulting files/artifacts;
- executable validation;
- contract/scenario traceability;
- security/change-control compliance;
- review evidence.

A tool-native feature may improve ergonomics but cannot lower these requirements.

## Memory and conversational context

Tool memory, auto-memory, chat history, generated summaries and local conversational assumptions are advisory context only.

When a fact is required for future correctness, it must be represented in an appropriate repository artifact, for example:

- canonical documentation/decision;
- active program status;
- code/schema/configuration;
- executable test/fixture;
- accepted OKF routing entry;
- compatibility manifest;
- traceability record.

When memory conflicts with repository authority, repository authority wins.

## Conflict behavior

If a tool adapter, skill, memory or user-level preference conflicts with this policy or higher authority:

1. do not follow the lower-precedence conflicting instruction;
2. use the higher-precedence repository authority;
3. surface the conflict when it materially affects the task;
4. correct the repository adapter/configuration when that correction is within the requested scope, otherwise record it as follow-up.

## Review-only invariant

A request whose operative action is review/inspect/audit/assess remains A1 unless the human also requests edits. Finding a defect during review does not itself authorize changing the repository.

## Completion invariant

Completing the requested group or task authorizes reporting the next dependency or recommended step. It does not authorize starting that next step automatically.
