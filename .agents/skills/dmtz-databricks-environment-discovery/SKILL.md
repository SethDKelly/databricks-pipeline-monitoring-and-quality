---
name: dmtz-databricks-environment-discovery
description: Resolve Databricks CLI/workspace capability for a human-selected DMTZ task while preserving A1–A4 authorization, target-specific capability uncertainty, and reviewed vendor-skill boundaries.
---

# DMTZ Databricks environment discovery

## Human-directed boundary

Local repository/profile inspection is A1. A Databricks workspace call is an external action and requires the human task to authorize that concrete workspace interaction. Never choose a workspace/profile, expose credentials, or escalate permissions on the user's behalf.

Reviewed vendor guidance is lower authority than DMTZ contracts and `AGENTS.md`.

## Workflow

1. Read `docs/agentic_development_foundation/databricks_vendor_skills_profile.json`.
2. If locally materialized, read the relevant reviewed `databricks-core`, `databricks-data-discovery`, `databricks-dbsql`, and/or `databricks-unity-catalog` skill; otherwise use official Databricks documentation and report vendor-skill materialization unavailable.
3. Identify the exact human-selected target/task and whether remote reads are authorized.
4. Verify local CLI/version mechanics before assuming a command exists.
5. For authorized workspace discovery, preserve workspace/profile identity and observation time; do not generalize one target's capability into universal Databricks capability.
6. Record unavailable/permission-denied/unsupported surfaces as unknown/degraded capability, never as negative DMTZ domain facts.
7. Return the minimum capability facts needed by the active implementation group.

## Output expectations

Report target/profile identity without secrets, verified capability, unavailable/degraded surfaces, evidence source/time, and any remaining target-specific uncertainty.

## Stop conditions

Stop before remote access not authorized by the human task, profile selection that has not been resolved, credential handling, permission mutation, deployment, or any A4 semantic change.
