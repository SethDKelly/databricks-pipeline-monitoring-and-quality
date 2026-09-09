# ARCH-167 — Transactional Checkpoint Advancement

**Status:** Accepted

A checkpoint advances only after the corresponding source material and required provenance have been durably committed.

Crash-after-fetch cannot move progress past evidence that was never persisted.
