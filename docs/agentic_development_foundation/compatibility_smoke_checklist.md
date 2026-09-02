# Tool Compatibility Smoke Checklist

**Status:** ACCEPTED — ADF-F / EXECUTE IN ADF-G

Use this checklist when performing actual Cursor, Claude Code, and Codex runtime compatibility exercises. Deterministic ADF-F CI does not substitute for these checks.

For each supported tool and representative bounded task, record:

- tool/product version or build when available;
- date of verification;
- whether shared repository authority was loaded as expected;
- whether `knowledge/index.md` could be reached without preloading the full design corpus;
- whether the canonical `.agents/skills/` workflow or documented bridge was discoverable/invokable;
- whether A1/A2/A3/A4 boundaries were preserved;
- whether exact stable-ID resolution used canonical repository authority rather than memory;
- whether the tool stopped at the human-selected group/task;
- whether safe repository validation could be run;
- observed persistent/routine context behavior where the tool exposes it;
- supported, degraded, unverified, or unsupported result;
- any tool-specific workaround, provided it changes convenience only and not DMTZ semantics.

A tool may be marked degraded or unverified independently. Do not alter shared repository semantics merely to force all tools into the same native UX.
