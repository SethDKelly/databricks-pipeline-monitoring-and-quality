# ADF-H External Security Compatibility Baseline

**Reviewed:** 2026-09-02

**Status:** CURRENT COMPATIBILITY INPUT — NOT DMTZ SEMANTIC AUTHORITY

This file records the external security/privacy/runtime assumptions used by ADF-H. Vendor behavior is reverified under `tool_lifecycle_review.json` and may become degraded/unverified without changing canonical DMTZ semantics.

## Cursor

Official sources reviewed:

- `https://prod.cursor.com/docs/enterprise/security-hardening`
- `https://prod.cursor.com/docs/enterprise/privacy-and-data-governance`
- `https://prod.cursor.com/docs/agent/security`

Current relevant controls include privacy/data-governance settings, agent sandbox/run-mode controls, explicit approval for sensitive actions, `.cursorignore`/repository restrictions, network/plugin/MCP governance and enterprise retention/audit controls.

DMTZ does not assume any one optional Cursor enterprise feature is universally present. Target deployments must verify their actual policy/profile.

## Claude Code

Official sources reviewed:

- `https://code.claude.com/docs/en/security`
- `https://code.claude.com/docs/en/permissions`
- `https://code.claude.com/docs/en/memory`

Current relevant controls include permission modes, sandboxing, working-directory boundaries, workspace trust, fail-closed approval behavior, network/MCP controls and secure credential handling. Claude memory/project instructions remain contextual development state, not DMTZ authority.

DMTZ does not infer the active permission mode or sandbox from repository configuration alone.

## Codex / OpenAI

Official sources reviewed:

- `https://openai.com/index/running-codex-safely/`
- `https://help.openai.com/en/articles/11369540`

Current relevant controls include sandbox boundaries, approval policy, managed configuration, network policy and audit/telemetry. Runtime approval/configuration names may change between versions; repository semantics therefore do not pin a transient Codex permission mode.

DMTZ does not infer Codex runtime support from this documentation review; ADF-G runtime state remains independently recorded.

## Common ADF-H interpretation

Across providers:

- repository instructions steer behavior but do not replace technical permission boundaries;
- provider privacy/retention depends on actual plan, model, policy and deployment configuration;
- network/external tool access should be least privilege;
- external integrations and code/content can introduce prompt-injection or supply-chain risk;
- provider memory/transcripts are not canonical DMTZ knowledge;
- a provider feature becoming stale or unavailable degrades compatibility rather than rewriting DMTZ semantics.
