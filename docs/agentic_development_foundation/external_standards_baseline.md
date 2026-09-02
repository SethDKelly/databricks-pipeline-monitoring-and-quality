# Agentic External Standards Baseline

**Reviewed:** 2026-09-02

This document records the external tool/format assumptions used by the Agentic Development Foundation. These are compatibility facts, not DMTZ semantic authority, and must be reverified when the corresponding foundation group is executed or when vendor behavior changes materially.

## Open Knowledge Format

Canonical source: GoogleCloudPlatform `knowledge-catalog/okf/SPEC.md`.

Reverified during ADF-B on **2026-09-02** against the upstream specification. Current targeted specification: **OKF v0.2**.

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

Assumed capabilities:

- root and nested `AGENTS.md` support;
- project rules under `.cursor/rules/*.mdc`;
- rules can be always-applied, relevance-selected or glob/file scoped;
- rules consume model context when applied;
- `@filename` references may include other files;
- project rules do not govern every Cursor product surface, so repository tests/CI remain the enforcement layer.

DMTZ current policy remains: scoped/relevance-driven project rules, no intentional universal `.mdc` rule unless a measured need is accepted.

## Claude Code

Canonical source: current Claude Code documentation.

Assumed capabilities:

- project `CLAUDE.md` files provide persistent instructions;
- Claude Code reads `CLAUDE.md`, not `AGENTS.md` directly;
- `CLAUDE.md` can import another file using `@path`, including a repository `AGENTS.md`;
- `.claude/rules/` supports modular and path-scoped rules;
- project skills use `SKILL.md` under `.claude/skills/<skill-name>/`;
- detailed procedures are better placed in skills or path-scoped rules than a large persistent `CLAUDE.md`;
- auto-memory is contextual memory, not enforced project configuration.

The foundation should use a thin `CLAUDE.md` importing shared authority rather than copying it.

## Codex / OpenAI

Canonical sources: current OpenAI Codex/developer guidance.

Assumed capabilities/practices:

- repository `AGENTS.md` is an established persistent-context mechanism for Codex workflows;
- OpenAI supports reusable Skills as a platform capability;
- current model guidance favors lean prompts, relevant tools/context, and explicit action/autonomy boundaries;
- repository/environment configuration and tests materially affect coding-agent reliability.

The foundation must not depend on a specific Codex model name. Model selection is an implementation/runtime choice and may change independently of repository semantics.

## Reverification triggers

Reverify a tool/format baseline when:

- a supported tool changes its instruction-loading or skill format;
- an OKF major version is proposed;
- a tool-specific adapter begins relying on a new native capability;
- a compatibility smoke test fails after a tool update;
- documentation is older than the review horizon established during ADF-H.

A compatibility fact becoming stale should mark the tool feature unverified/degraded, not silently invalidate DMTZ product documentation.
