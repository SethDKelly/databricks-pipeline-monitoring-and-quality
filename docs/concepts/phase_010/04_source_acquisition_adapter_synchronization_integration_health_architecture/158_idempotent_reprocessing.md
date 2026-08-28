# ARCH-158 — Idempotent Reprocessing

**Status:** Accepted

Adapters and normalizers must safely reprocess overlapping pages, redelivered webhooks, retries and restored files without multiplying one source occurrence into multiple logical events.

Physical duplicate ingestion remains traceable where operationally useful.
