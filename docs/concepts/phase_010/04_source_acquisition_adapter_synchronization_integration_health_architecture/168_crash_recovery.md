# ARCH-168 — Crash Recovery

**Status:** Accepted

After worker/process failure, acquisition resumes from durable checkpoint state with overlap/idempotency as required by the source.

Recovery favors duplicate-safe replay over silently skipping uncertain intervals.
