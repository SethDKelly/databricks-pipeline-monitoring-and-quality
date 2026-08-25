# INTG-078 — Delta Output Table Commit / Version Evidence

**Status:** Accepted — Phase 009 Group 03

Delta table history exposes table version, commit timestamp, operation and supporting provenance fields including job/notebook context for qualifying writes. When an exact execution-to-commit association is explicitly available, it can bind that output table version to the execution.

Support is conditional on workload/task/source fields and retained table history. Run success never substitutes for output-commit evidence.
