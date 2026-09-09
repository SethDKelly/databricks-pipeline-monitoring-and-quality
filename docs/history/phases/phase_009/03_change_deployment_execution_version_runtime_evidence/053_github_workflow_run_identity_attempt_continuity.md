# INTG-053 — GitHub Workflow Run Identity & Attempt Continuity

**Status:** Accepted — Phase 009 Group 03

A GitHub Actions workflow execution is identified by `run_id`; `run_number` is workflow-scoped display/sequence context, and `run_attempt` distinguishes re-execution attempts of the same workflow run.

Re-running does not create a new repository revision by default. Attempt history must preserve the original workflow-run identity and attempt-specific lifecycle/outcome.
