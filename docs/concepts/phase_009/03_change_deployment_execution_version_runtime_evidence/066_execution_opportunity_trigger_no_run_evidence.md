# INTG-066 — Execution Opportunity, Trigger & No-Run Evidence

**Status:** Accepted — Phase 009 Group 03

Configured schedule/trigger/dependency state can establish expected/opportunity context only when the exact trigger semantics and effective configuration are known.

`No run` requires opportunity plus complete-enough run-event coverage and source health for the bounded workspace/job/window/run class. Missing Runs API history or missing timeline rows outside retention cannot prove non-execution.
