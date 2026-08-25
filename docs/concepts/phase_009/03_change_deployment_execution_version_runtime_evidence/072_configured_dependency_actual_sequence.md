# INTG-072 — Configured Dependency vs Actual Sequence

**Status:** Accepted — Phase 009 Group 03

Databricks task configuration such as `depends_on_keys` is evidence of configured dependency/expected order. Task/run timelines provide actual execution timing/precedence evidence.

Configured dependency ≠ actual precedence. Actual precedence ≠ waiting/hold. Neither automatically proves data/version consumption.
