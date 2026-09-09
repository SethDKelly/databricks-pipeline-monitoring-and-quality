# INTG-055 — GitHub Re-run Revision, Actor & Privilege Semantics

**Status:** Accepted — Phase 009 Group 03

GitHub documents that re-runs use the same `GITHUB_SHA` and `GITHUB_REF` as the original triggering event while `run_attempt` increments. `github.triggering_actor` may differ from the actor whose privileges govern the re-run.

Re-run, retry and a newly triggered workflow execution are therefore distinct operational propositions even when they execute equivalent source.
