# Agentic External Standards Baseline

**Reviewed:** 2026-09-02

This document records external tool/format assumptions used by the Agentic Development Foundation. These are compatibility facts, not DMTZ semantic authority, and must be reverified when a corresponding foundation group is executed or vendor behavior changes materially.

## Open Knowledge Format

Canonical source: upstream GoogleCloudPlatform `knowledge-catalog/okf/SPEC.md`.

Reverified during ADF-B on **2026-09-02**. Current targeted specification: **OKF v0.2**.

Relevant properties used by this foundation:

- Markdown concept documents with YAML frontmatter;
- `type` is the only universally required concept key under the base spec;
- producer-defined concept types are allowed and unknown types must be tolerated;
- optional `index.md` supports progressive disclosure;
- optional `log.md` supports update history;
- v0.2 adds `sources`, `generated`, `verified`, lifecycle `status`, and `stale_after`;
- lifecycle status values are `draft`, `stable`, `deprecated`;
- a root `index.md` may declare `okf_version: "0.2"`;
- OKF does not replace domain-specific schemas or prescribe a runtime.

DMTZ intentionally does not adopt OKF Attested Computation runtime behavior in this foundation.

## Open Agent Skills / portable workflow baseline

Reverified during ADF-D on **2026-09-02** using current Cursor, Claude Code and OpenAI/Codex documentation.

Common facts relied on by DMTZ:

- Agent Skills are Markdown workflow packages centered on `SKILL.md`;
- `name` and `description` are the common required metadata used by the supported tools/standard;
- skill bodies are loaded on demand/progressively rather than as permanent repository instructions;
- a host may support explicit invocation and/or description-based implicit selection;
- skill selection is a tool/runtime convenience and does not create repository authority or permission.

DMTZ canonical workflows therefore use only `name` and `description` frontmatter plus provider-neutral Markdown instructions under `.agents/skills/`.

## Cursor

Canonical source: current Cursor Rules and Agent Skills documentation.

Reverified for instruction behavior during ADF-C and for skills during ADF-D on **2026-09-02**.

Relevant current behavior:

- root and nested `AGENTS.md` are supported;
- project rules live under `.cursor/rules/*.mdc` and may be relevance-selected or file/glob scoped;
- `alwaysApply: true` includes a rule in every Agent conversation;
- rules consume model context when applied;
- Cursor also recognizes a root `CLAUDE.md` as persistent project instructions for Claude Code compatibility;
- Cursor natively discovers project Agent Skills from `.agents/skills/` and `.cursor/skills/`;
- Cursor also discovers compatible skills from `.claude/skills/` and `.codex/skills/`;
- skills may be explicitly invoked with `/skill-name` and may be selected automatically when relevant;
- skills use progressive/on-demand loading and may include support resources/scripts, though DMTZ ADF-D skills are instruction-only.

DMTZ policy remains: scoped/relevance-driven `.mdc` project rules, no intentional universal `.mdc` rule without a measured accepted need, and one canonical DMTZ workflow source under `.agents/skills/`.

Because Cursor also reads root `CLAUDE.md`, DMTZ uses `.claude/CLAUDE.md`. Because Cursor also discovers `.claude/skills/`, DMTZ does not copy the same workflow names into both `.agents/skills/` and `.claude/skills/`.

## Claude Code

Canonical source: current Claude Code documentation.

Reverified for instructions during ADF-C and skills/commands during ADF-D on **2026-09-02**.

Relevant current behavior:

- project instructions may live at `./CLAUDE.md` or `./.claude/CLAUDE.md`;
- a `CLAUDE.md` can import other files with `@path`; relative imports resolve relative to the containing file;
- `.claude/rules/*.md` supports modular/path-scoped rules;
- Claude Code skills follow the open Agent Skills standard and project skills normally live at `.claude/skills/<skill-name>/SKILL.md`;
- skill bodies load only when used and skills may be invoked directly with `/skill-name` or selected when relevant;
- existing `.claude/commands/*.md` custom commands continue to work and create slash-invoked workflows, although native skills are preferred for richer packaging;
- auto-memory is contextual memory, not enforced project configuration.

DMTZ uses `.claude/CLAUDE.md` importing `../AGENTS.md` and thin `.claude/commands/<name>.md` bridges that direct Claude to the canonical `.agents/skills/<name>/SKILL.md` workflow. This avoids maintaining duplicated DMTZ workflow semantics in `.claude/skills/` while retaining native slash invocation.

Claude subagents/agent teams remain outside the accepted human-directed foundation even though they exist as native product capabilities.

## Codex / OpenAI

Canonical sources: current OpenAI Codex/ChatGPT skills documentation and Codex AGENTS guidance.

Reverified for instructions during ADF-C and skills during ADF-D on **2026-09-02**.

Relevant current behavior/practices:

- repository `AGENTS.md` is a native persistent-context mechanism;
- Codex scans repository `.agents/skills` locations from the working directory toward the repository root;
- a skill requires `SKILL.md` with `name` and `description` and may include optional supporting resources;
- Codex supports explicit skill selection by typing `$` to mention a skill and `/skills` to inspect skills;
- Codex may also select a skill implicitly when the task matches its description;
- Codex skills use progressive disclosure, with the full `SKILL.md` loaded when selected;
- repository/environment configuration and executable tests materially affect coding-agent reliability;
- execution/sandbox/approval behavior is runtime/environment state and is not inferred from repository docs alone.

DMTZ therefore uses root `AGENTS.md`, `knowledge/index.md`, and `.agents/skills/` directly for Codex with no separate Codex semantic rulebook.

The foundation does not depend on a particular Codex model name or version.

## Runtime verification status

ADF-C/D verify **documented native mechanisms and repository adapter/workflow structure**, not installed developer-tool binaries.

`docs/agentic_development_foundation/tool_compatibility.json` records supported tools as `documentation_verified_runtime_smoke_pending`.

ADF-G owns tool-in-the-loop verification using representative bounded tasks. A runtime mismatch must be recorded as degraded/unverified rather than silently changing DMTZ authority or workflow semantics.

## Reverification triggers

Reverify a tool/format baseline when:

- a supported tool changes instruction-loading, skill discovery, invocation, or command behavior;
- the Agent Skills standard introduces a materially incompatible required field/behavior;
- an OKF major version is proposed;
- a tool-specific adapter begins relying on a new native capability;
- a compatibility smoke test fails after a tool update;
- a previously avoided instruction/skill surface changes loading behavior;
- documentation is older than the review horizon established during ADF-H.

A compatibility fact becoming stale should mark the tool feature unverified/degraded, not silently invalidate DMTZ product documentation.
