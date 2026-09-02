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

## Cursor

Canonical source: current Cursor Rules documentation.

Reverified during ADF-C on **2026-09-02**.

Relevant current behavior:

- root and nested `AGENTS.md` are supported;
- project rules live under `.cursor/rules/*.mdc` and may be relevance-selected or file/glob scoped;
- `alwaysApply: true` includes a rule in every Agent conversation;
- rules consume model context when applied;
- `@filename` references can include repository files;
- Cursor also recognizes a **root** `CLAUDE.md` as persistent project instructions for Claude Code compatibility;
- Cursor rules do not govern every Cursor product surface, so repository tests/CI remain the enforcement layer.

DMTZ policy remains: scoped/relevance-driven `.mdc` project rules, no intentional universal `.mdc` rule unless a measured need is accepted.

Because Cursor also reads root `CLAUDE.md`, DMTZ intentionally places the Claude project adapter at `.claude/CLAUDE.md` instead of repository-root `CLAUDE.md`. This avoids a duplicate always-on Cursor instruction surface.

## Claude Code

Canonical source: current Claude Code documentation.

Reverified during ADF-C on **2026-09-02**.

Relevant current behavior:

- Claude Code reads project `CLAUDE.md` instructions rather than `AGENTS.md` directly;
- project instructions may live at `./CLAUDE.md` **or** `./.claude/CLAUDE.md`;
- a `CLAUDE.md` can import other files with `@path`; relative imports resolve relative to the file containing the import;
- current documentation explicitly recommends importing an existing `AGENTS.md` rather than duplicating its contents;
- `.claude/rules/*.md` supports modular/path-scoped rules;
- project skills use `SKILL.md` under `.claude/skills/<skill-name>/` and follow the open Agent Skills format with Claude-specific extensions;
- detailed procedures are better placed in skills or path-scoped rules than in a large persistent `CLAUDE.md`;
- `/memory`, `/skills`, and `/doctor` provide useful configuration diagnostics;
- auto-memory is contextual memory, not enforced project configuration.

DMTZ therefore uses `.claude/CLAUDE.md` importing `../AGENTS.md`, with only minimal Claude-specific mechanics. No `.claude/rules/` files are required by ADF-C.

Claude subagents/agent teams may exist as native product capabilities, but repository implementation delegation remains outside the accepted human-directed foundation and is not enabled by these compatibility facts.

## Codex / OpenAI

Canonical sources: current OpenAI Codex guidance and the OpenAI Codex repository's AGENTS discovery documentation.

Reverified during ADF-C on **2026-09-02**.

Relevant current behavior/practices:

- repository `AGENTS.md` is a native persistent-context mechanism for Codex workflows;
- Codex discovers `AGENTS.md` along the repository path and supports more-specific nested instruction files when present;
- repository/environment configuration and executable tests materially affect coding-agent reliability;
- current OpenAI guidance recommends using `AGENTS.md` as a concise map into structured repository knowledge rather than a monolithic manual;
- reusable skills/workflows are supported in the OpenAI ecosystem, but ADF-D owns DMTZ's portable workflow realization;
- execution/sandbox/approval behavior is a runtime/environment concern and must not be inferred from repository documentation alone.

DMTZ requires no Codex-specific semantic rulebook. Root `AGENTS.md`, `knowledge/index.md`, canonical docs, and repository validation are the shared surfaces.

The foundation does not depend on a particular Codex model name or version.

## Runtime verification status

ADF-C verifies **documented native mechanisms and repository adapter structure**, not installed developer-tool binaries.

`docs/agentic_development_foundation/tool_compatibility.json` records all three supported tools as `documentation_verified_runtime_smoke_pending`.

ADF-G owns tool-in-the-loop verification using representative bounded tasks. A runtime mismatch must be recorded as degraded/unverified rather than silently changing DMTZ authority.

## Reverification triggers

Reverify a tool/format baseline when:

- a supported tool changes its instruction-loading or skill format;
- an OKF major version is proposed;
- a tool-specific adapter begins relying on a new native capability;
- a compatibility smoke test fails after a tool update;
- a previously avoided instruction surface changes loading behavior;
- documentation is older than the review horizon established during ADF-H.

A compatibility fact becoming stale should mark the tool feature unverified/degraded, not silently invalidate DMTZ product documentation.
