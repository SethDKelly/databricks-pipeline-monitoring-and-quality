# DMTZ Coding-Agent Compatibility Matrix

**Status:** REPOSITORY COMPATIBILITY ESTABLISHED / PROVIDER RUNTIME SMOKES PENDING

**Documentation reviewed:** 2026-09-10

This matrix separates documented capability, checked-in repository compatibility, and actual runtime evidence. A documented vendor feature is not a runtime PASS. The ordinary IDE/CLI path remains the repository-owned fallback when provider-specific agent runtime verification is unavailable.

| Dimension | Cursor | Claude Code | Codex | Ordinary IDE/CLI |
|---|---|---|---|---|
| Shared repository authority | root `AGENTS.md` | `.claude/CLAUDE.md` imports `../AGENTS.md` | root `AGENTS.md` | human reads root `AGENTS.md` |
| Repository-native discovery | `docs/index.md` | `docs/index.md` | `docs/index.md` | `docs/index.md` |
| OKF compatibility | generated `knowledge/index.md` | generated `knowledge/index.md` | generated `knowledge/index.md` | generated `knowledge/index.md` when needed |
| Scoped native instructions | `.cursor/rules/*.mdc`; nested `AGENTS.md` | `.claude/rules/*.md`; nested/on-demand CLAUDE files | nested `AGENTS.md` hierarchy | normal directory/document conventions |
| Canonical DMTZ workflows | `.agents/skills/` natively | `.claude/commands/` thin bridge to `.agents/skills/` | `.agents/skills/` | read `.agents/skills/` directly |
| Exact stable-ID discipline | deterministic repository helper/policy | deterministic repository helper/policy | deterministic repository helper/policy | deterministic repository helper/policy |
| Agentic conformance | repository command | repository command | repository command | repository command |
| Human-directed A1–A4 boundary | shared policy | shared policy | shared policy | shared policy/team process |
| Tool memory canonical? | No | No | No | N/A |
| Provider-specific semantic rulebook required? | No | No | No | No |
| Current documentation state | verified | verified | verified | N/A |
| Current provider runtime evidence | **unverified** | **unverified** | **unverified** | **supported** |

## Current documentation findings

### Cursor

Current Cursor documentation supports root/nested `AGENTS.md`, version-controlled scoped `.cursor/rules/*.mdc`, and project Agent Skills under `.agents/skills/`. DMTZ uses `docs/index.md` for repository-native discovery and keeps generated OKF as compatibility only.

### Claude Code

Claude Code project instructions remain at `.claude/CLAUDE.md`, which imports shared `AGENTS.md`. Existing `.claude/commands/` remain thin bridges to `.agents/skills/`; no duplicate semantic `.claude/skills/` corpus is required. Repository-native discovery is `docs/index.md`.

### Codex

Codex continues to use repository `AGENTS.md` instructions and canonical `.agents/skills/`. Repository-native discovery is `docs/index.md`; model identity remains irrelevant to repository semantics.

## Stable-reference behavior

All tools use `python3 scripts/agentic/resolve_stable_id.py <ID>` for deterministic current `owner_path::ID` resolution. Historical occurrences require explicit `--history` and never compete with current ownership. Search order, generated OKF, redirects, history and tool memory do not establish semantic authority.

## Runtime evidence status

The ADF-G execution environment available on 2026-09-02 did not contain Cursor Agent/CLI, Claude Code, or Codex binaries. No authenticated provider runtime was available for the representative bounded task. Cursor, Claude Code and Codex therefore remain **unverified**, not unsupported. Ordinary IDE/CLI remains supported because repository-owned context and conformance work without an agent product.

The authoritative runtime ledger is `runtime_compatibility_evidence.json`.

## Degraded-mode principle

Native UX differences may degrade convenience but not correctness. A tool may remain usable if a developer must manually open a current owner or canonical workflow rather than relying on native discovery. DMTZ does not add duplicate semantic instructions solely to make feature parity look symmetrical.

## Tool switching

Switching tools must not require a branch conversion, status rewrite or semantic migration. A developer may stop one agent, open another, and continue from the same repository state because shared authority, discovery, workflows and validation live in version-controlled repository files independent of the provider.

## Reverification

Material vendor behavior changes require documentation re-review. Runtime status changes only after the bounded exercise is executed in the corresponding actual runtime and recorded in the evidence ledger. A tool may independently become degraded or unverified without changing another tool's status or DMTZ domain health.
