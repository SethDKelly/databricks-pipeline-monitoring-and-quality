# ADF-G — Developer Tool Compatibility, Onboarding & Operating Model

**Status:** PLANNED / READY TO EXECUTE

## Objective

Prove that a developer can choose Cursor, Claude Code or Codex without changing DMTZ semantics, review requirements or implementation acceptance criteria.

## Supported profile

Initial supported agent profile:

- Cursor Agent for interactive repository work;
- Claude Code for interactive repository work;
- Codex for interactive repository work;
- ordinary IDE/CLI development without an agent remains fully supported.

No tool is required to implement DMTZ.

## Compatibility dimensions

Each supported tool should be checked against:

1. repository instruction loading;
2. scoped/path-specific instruction support;
3. portable workflow/skill invocation or equivalent;
4. repository search/read capability;
5. local edit/test capability;
6. visibility of current implementation authority;
7. progressive knowledge retrieval through `knowledge/`;
8. safe handling of unavailable/unsupported native features;
9. human approval boundary behavior;
10. developer ability to inspect exactly what instructions/workflow were applied.

## Human-directed operating model

A normal development session should look like:

1. developer chooses tool;
2. developer starts from a repository issue/group/task;
3. agent resolves context from shared authority/OKF/canonical docs;
4. developer asks for review, plan or implementation;
5. agent works within that explicit task scope;
6. repository validation, not agent confidence, determines conformance;
7. developer reviews normal diff/test evidence;
8. normal Git/PR/team process governs integration.

No special 'AI branch' semantics are required. Agent-created code is ordinary code subject to ordinary repository controls.

## Tool-specific expectations

### Cursor

Use root `AGENTS.md` plus the existing scoped `.cursor/rules/`. Cursor remains a first-class supported interface but its rules must stay thin and reference-driven.

### Claude Code

Use a thin `CLAUDE.md` that consumes root `AGENTS.md`; use `.claude/rules/` for genuinely Claude-specific path-scoped behavior and skills/native adapters for workflows. Persistent auto-memory is never a substitute for checked-in team knowledge.

### Codex

Use root `AGENTS.md` and portable knowledge/workflows. Codex-specific project configuration may improve execution environment/tool access but may not define semantic requirements absent from shared sources.

## Onboarding

A new developer should be able to complete a short tool-neutral onboarding exercise:

- locate current work;
- resolve one stable contract;
- invoke or follow `resolve-context`;
- run the agentic conformance checks;
- make a harmless fixture/document change through their chosen agent;
- verify the tool used the expected project instructions;
- understand where personal preferences may be configured without entering repository truth.

## Compatibility degradation

If a supported tool temporarily lacks a native feature:

- fall back to manual/shared Markdown workflow instructions;
- do not fork product semantics;
- mark the feature degraded/unverified in the compatibility manifest;
- do not block ordinary development if core repository read/edit/test behavior remains available.

## Evaluation approach

Use one small representative task across all three tools and compare outcomes at the artifact level:

- relevant context found;
- prohibited context not unnecessarily loaded;
- semantic guardrails respected;
- expected files/tests changed;
- validation run;
- no extra unrequested scope;
- developer can understand the result.

Do not rank tools with a universal 'best agent' score. Compatibility is multidimensional and may change with vendor releases.

## Deliverables

- supported-tool compatibility matrix;
- verification date/version policy;
- tool-neutral onboarding guide;
- one representative cross-tool acceptance exercise;
- documented degraded-mode behavior;
- guidance for adding another coding agent later without redesigning the foundation.

## Acceptance scenarios

ADF-G passes when:

- the same bounded task can be completed through Cursor, Claude Code and Codex without semantic instruction forks;
- tool-specific native features improve ergonomics but are not required for correctness;
- a developer can switch tools mid-project and use the same canonical repository state;
- personal tool settings cannot silently change team acceptance criteria;
- ordinary non-agent development remains fully viable.
