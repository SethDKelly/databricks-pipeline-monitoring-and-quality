# ADF-D — Portable Skills & Human-Directed Workflow Contract

**Status:** PLANNED / READY TO EXECUTE

## Objective

Define reusable development procedures once, in a portable form, so Cursor/Claude/Codex users can invoke materially equivalent workflows without repeating long prompt recipes.

## Scope

Skills are **human-directed workflow aids**, not autonomous workers. A human chooses the task and invokes or requests the workflow. Skills may inspect, edit and validate within that task's authorized scope but may not create unrelated follow-on work or delegate implementation to other agents.

## Canonical skill source

Use one repository-owned source tree, proposed as:

```text
agent-skills/
├── resolve-context/SKILL.md
├── implement-group/SKILL.md
├── resolve-contract/SKILL.md
├── run-conformance/SKILL.md
├── review-change/SKILL.md
├── update-traceability/SKILL.md
└── exit-review/SKILL.md
```

The canonical source should use the smallest common portable `SKILL.md` subset that can be adapted to native tool locations. Tool-specific-only frontmatter or dynamic command syntax belongs in adapters, not the portable source, unless all supported tools tolerate it.

## Initial workflow semantics

### `resolve-context`

Given a task or implementation group:

1. identify live implementation status;
2. traverse the OKF knowledge index to the smallest relevant domain/package entry;
3. retrieve the active group plan;
4. search exact stable IDs as needed;
5. return the minimal authoritative context set and unresolved assumptions.

No repository edits.

### `implement-group`

For a human-selected group/task:

1. resolve context;
2. inspect existing code/tests/config;
3. state affected contracts/acceptance gates;
4. implement the smallest compliant change;
5. add/update tests at the lowest appropriate level;
6. run relevant non-destructive validation;
7. update traceability/ADRs when required;
8. report residual gaps/capability assumptions.

It must not automatically start the next group.

### `resolve-contract`

Search a stable contract ID or bounded semantic question and return the exact canonical source plus the narrow surrounding context needed to apply it. Summaries are advisory and must link to exact authority.

### `run-conformance`

Run or instruct the repository's deterministic checks for the current change scope and report failures without rewriting requirements to make tests pass.

### `review-change`

Review a diff against affected contracts, security, historical semantics and test obligations. Focus on substantive defects rather than stylistic preference.

### `update-traceability`

Update the implementation traceability manifest after material behavior is added/changed. It may not mark a contract satisfied without supporting executable evidence.

### `exit-review`

Evaluate one implementation group/package against its documented exit gates and produce a review artifact. It cannot self-approve unresolved mandatory criteria.

## Skill design rules

- workflow steps, not duplicated domain specification;
- refer to OKF index/canonical docs rather than embedding long architecture summaries;
- idempotent where practical;
- safe failure: inability to resolve authority becomes an explicit unresolved state;
- no hidden tool-specific assumptions in portable source;
- no network/external writes unless the human task explicitly requires and authorizes them;
- no autonomous chaining from one skill to another except within the bounded workflow explicitly invoked.

## Tool adapters

ADF execution may place generated/copied/thin adapters in native locations such as `.claude/skills/` or Cursor command/rule surfaces if useful. Adapter generation should be deterministic where possible.

Do not rely on symlinks as the sole cross-platform distribution strategy; Windows/enterprise environments may make them inconvenient. Prefer generation/copy validation when portability matters.

## Deliverables

- canonical portable skill directory and profile;
- first seven human-directed skills above or a justified reduced set;
- tool adapter strategy for Cursor/Claude/Codex;
- skill validation tests;
- documentation for invoking skills manually in each supported tool;
- clear unsupported-feature behavior.

## Acceptance scenarios

ADF-D passes when:

- a developer can invoke `resolve-context` and `implement-group` semantics from each supported tool;
- the portable workflow produces equivalent required steps despite different native invocation UX;
- the implementation skill stops after the requested group/task instead of continuing independently;
- a skill cannot override an unresolved architecture conflict by changing its own instructions;
- supporting detail can be loaded on demand instead of inflating every session's persistent context.
