# INTG-052 — GitHub Event & Workflow-Trigger Revision Semantics

**Status:** Accepted — Phase 009 Group 03

GitHub Actions `GITHUB_SHA` / `github.sha` is event-dependent triggering revision evidence. The exact event/ref semantics must be retained rather than treating the field as universally meaning `main` HEAD or merged revision.

`github.workflow_sha` identifies the commit containing the workflow file and can differ in meaning from the triggering revision. Trigger revision and workflow-definition revision therefore remain separate facets.
