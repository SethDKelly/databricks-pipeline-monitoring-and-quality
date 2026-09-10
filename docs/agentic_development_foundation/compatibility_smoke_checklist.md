# Tool Compatibility Smoke Checklist

**Status:** ACCEPTED — ADF-F BASELINE / ADF-G DEFERRED RUNTIME VERIFICATION / ROUTING REBOUND DPTN-F

Use this checklist when performing actual Cursor, Claude Code, and Codex runtime compatibility exercises. Deterministic repository conformance validates the evidence ledger but does not substitute for a provider runtime.

The common bounded exercise is `ADF-G-XT01` in [`adf_g_runtime_probe.md`](adf_g_runtime_probe.md). Record results in [`runtime_compatibility_evidence.json`](runtime_compatibility_evidence.json).

For each supported-profile tool and representative bounded task, record:

- tool/product version or build when available;
- date of verification;
- actual invocation/runtime mode;
- whether shared repository authority was loaded as expected;
- whether `docs/index.md` could be reached without preloading the full design corpus;
- whether generated `knowledge/index.md`, if used, remained OKF compatibility rather than current semantic authority;
- whether the canonical `.agents/skills/` workflow or documented bridge was discoverable/invokable;
- whether A1/A2/A3/A4 boundaries were preserved;
- whether exact stable-ID resolution returned the deterministic current `owner_path::ID` rather than a first search hit;
- whether historical stable-ID inspection, if requested, used explicit `--history` and remained provenance-only;
- whether the tool stopped at the human-selected task;
- whether safe repository validation could be run or correctly identified;
- observed persistent/routine context behavior where the tool exposes it;
- supported, degraded, unverified, or unsupported result;
- any tool-specific workaround, provided it changes convenience only and not DMTZ semantics.

A provider may move to `supported` or `degraded` only after the actual bounded exercise passes and the evidence ledger records the runtime observation. Documentation-only review remains `unverified` for runtime purposes.

A tool may be marked degraded or unverified independently. Do not alter shared repository semantics merely to force all tools into the same native UX.
