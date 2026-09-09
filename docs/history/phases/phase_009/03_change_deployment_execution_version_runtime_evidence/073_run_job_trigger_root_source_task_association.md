# INTG-073 — Run-Job Trigger & Root/Source-Task Association

**Status:** Accepted — Phase 009 Group 03

Where Databricks exposes `source_task_run_id`, `root_task_run_id`, `parent_run_id` or equivalent source-owned identifiers, those fields can support explicit orchestration ancestry between runs/tasks.

Availability is data-vintage/source-surface specific. Older history lacking these fields remains partial rather than reconstructed from time proximity.
