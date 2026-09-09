# INTG-069 — Run-Specific Remote-Git Commit Binding

**Status:** Accepted — Phase 009 Group 03

For Lakeflow Jobs configured with remote Git source, Databricks snapshots the configured branch/tag/commit at run start and the Jobs run representation exposes `git_snapshot.used_commit`.

When present for the exact run, `used_commit` is strong run-specific code-revision evidence. It binds the executed Git source facet, not every other implementation/configuration/input facet and not downstream causal truth.
