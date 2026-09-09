# INTG-081 — Multi-Output & Partial Output-Version Set

**Status:** Accepted — Phase 009 Group 03

An execution may write zero, one or many outputs and can commit a subset before failure. Output/version association is therefore per output and may be partial.

A successful run can have unknown output evidence; a failed/partial run can have committed output. Missing evidence for one output does not erase another evidenced commit or prove global no-output.
