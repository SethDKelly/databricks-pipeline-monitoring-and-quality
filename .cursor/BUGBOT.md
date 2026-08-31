# DMTZ Bugbot Review Policy

Review changed code for correctness, security, historical/evidence integrity, and violations of the frozen DMTZ contracts. Prefer concrete defects over stylistic commentary.

## High-priority findings

Flag changes that:

- turn missing/failed/unauthorized/partial acquisition into a negative domain fact;
- infer canonical identity from a name/path/source-local ID without accepted binding evidence;
- collapse event/effective time, source availability, framework knowledge/recorded time, or later correction in a way that rewrites historical/as-known state;
- overwrite/collapse corrections or supersessions that must retain prior state;
- equate execution success with freshness/data quality/health;
- conflate Expectation with Baseline or Observation with Assessment;
- infer deployment/run/version association from timestamp proximity or names alone;
- treat Lineage/reachability as exposure, Impact, or causality;
- promote localization/correlation/leading hypothesis to confirmed cause without the required evidence/authority gate;
- collapse authentication, Capability Authorization, Assertion Authority, or disclosure permission;
- expose secrets, sensitive raw payloads, hidden basis, cross-tenant data, or authorization-sensitive cache results;
- let model/search/vector output create canonical truth, causal confirmation, authority, Impact, or control decisions;
- advance acquisition checkpoints across incomplete pagination/coverage;
- make derived graph/search/cache/UI state canonical truth;
- use Delta time travel as the sole historical knowledge-cut semantics;
- weaken a frozen contract silently instead of using the documented change-control process;
- omit an executable test for a material accepted contract when the change introduces/changes that behavior.

## Active control, when present

Flag collapse of:

- readiness → Gate decision → issuance/delivery → enforcement → execution;
- Safeguard proposal/authorization/request/attempt/effective enforcement → prevention → release/recovery;
- prevention claims without opportunity + enforcement + alternate-path coverage;
- control authorization that is stale at enforcement where revalidation is required;
- unauthenticated/replayable control callbacks/commands.

## References

Use `docs/implementation/agent_reference_index.md` to locate the smallest authoritative contract set. The root `AGENTS.md`, `docs/implementation/AGENTS.md`, and active implementation package define current engineering scope.
