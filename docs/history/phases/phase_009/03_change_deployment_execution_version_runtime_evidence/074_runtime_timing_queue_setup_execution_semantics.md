# INTG-074 — Runtime Timing, Queue, Setup & Execution Semantics

**Status:** Accepted — Phase 009 Group 03

Run/task start/end/timeline fields support bounded timing and temporal-precedence reasoning. Source-specific queue/setup/execution measures must retain their documented meanings and run/task grain.

Timeline rows may be sliced across clock-hour boundaries and a single run can have multiple rows. Row count therefore does not equal execution count, and duration/ordering calculations must assemble the source representation correctly.
