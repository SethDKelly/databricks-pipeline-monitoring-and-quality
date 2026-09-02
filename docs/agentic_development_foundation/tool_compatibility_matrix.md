# DMTZ Coding-Agent Compatibility Matrix

**Status:** ADF-G — REPOSITORY COMPATIBILITY ESTABLISHED / PROVIDER RUNTIME SMOKES PENDING

**Documentation reviewed:** 2026-09-02

This matrix separates documented capability, checked-in repository compatibility, and actual runtime evidence. A documented vendor feature is not a runtime PASS.

| Dimension | Cursor | Claude Code | Codex | Ordinary IDE/CLI |
|---|---|---|---|---|
| Shared repository authority | root `AGENTS.md` | `.claude/CLAUDE.md` imports `../AGENTS.md` | root `AGENTS.md` | human reads root `AGENTS.md` |
| Scoped native instructions | `.cursor/rules/*.mdc`; nested `AGENTS.md` | `.claude/rules/*.md`; nested/on-demand CLAUDE files | nested `AGENTS.md` hierarchy | normal directory/document conventions |
| Canonical DMTZ workflows | `.agents/skills/` natively | `.claude/commands/` thin bridge to `.agents/skills/` | `.agents/skills/` | read `.agents/skills/` directly |
| Progressive knowledge | `knowledge/index.md` | `knowledge/index.md` | `knowledge/index.md` | `knowledge/index.md` |
| Exact stable-ID discipline | repository helper/policy | repository helper/policy | repository helper/policy | repository helper/policy |
| Agentic conformance | repository command | repository command | repository command | repository command |
| Human-directed A1–A4 boundary | shared policy | shared policy | shared policy | shared policy/team process |
| Tool memory canonical? | No | No | No | N/A |
| Provider-specific semantic rulebook required? | No | No | No | No |
| Current documentation state | verified | verified | verified | N/A |
| Current provider runtime evidence | **unverified** | **unverified** | **unverified** | **supported** |

## Current documentation findings

### Cursor

Current Cursor documentation supports root/nested `AGENTS.md`, version-controlled scoped `.cursor/rules/*.mdc`, and project Agent Skills under `.agents/skills/`. Cursor can discover and invoke skills progressively. This matches the DMTZ repository layout without a semantic copy.

### Claude Code

Current Claude Code documentation confirms that project instructions may live at `.claude/CLAUDE.md`, imports resolve relative to the importing file, and Claude Code itself reads `CLAUDE.md` rather than `AGENTS.md`. It explicitly recommends importing an existing `AGENTS.md` when a repository already uses one. Project skills are native under `.claude/skills/`; existing `.claude/commands/` remain supported and create the same slash-command UX. DMTZ therefore keeps `.claude/commands/` as thin bridges to the canonical `.agents/skills/` corpus rather than creating duplicate Claude skill semantics.

### Codex

Current Codex source/documentation continues to treat `AGENTS.md` as project instructions discovered from project root toward the working directory, with deeper scoped files applying to their directory tree. DMTZ's root `AGENTS.md` therefore remains the native Codex semantic adapter; model identity is irrelevant to repository semantics.

## Runtime evidence status

The ADF-G execution environment available on 2026-09-02 did not contain Cursor Agent/CLI, Claude Code, or Codex binaries. No authenticated provider runtime was available for the representative bounded task.

Accordingly:

- Cursor: **unverified**, not unsupported;
- Claude Code: **unverified**, not unsupported;
- Codex: **unverified**, not unsupported;
- ordinary IDE/CLI: **supported**, because the same repository-owned context and conformance path executes without any coding-agent product.

The authoritative runtime ledger is `runtime_compatibility_evidence.json`.

## Degraded-mode principle

Native UX differences may degrade convenience but not correctness. A tool may remain usable if a developer must manually open a canonical workflow or route rather than relying on native discovery. DMTZ does not add duplicate semantic instructions solely to make feature parity look symmetrical.

## Tool switching

Switching tools must not require a branch conversion, status rewrite or semantic migration. A developer may stop one agent, open another, and continue from the same repository state because the shared authority, knowledge, workflows and validation live in version-controlled files independent of the provider.

## Reverification

Material vendor behavior changes require documentation re-review. Runtime status changes only after the bounded exercise is executed in the corresponding actual runtime and recorded in the evidence ledger. A tool may independently become degraded or unverified without changing another tool's status or DMTZ domain health.
