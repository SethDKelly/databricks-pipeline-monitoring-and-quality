# ARCH-317 — Replay Projection Rebuild

**Status:** Accepted

Historical replay uses canonical bitemporal journals rather than Delta transaction-log time travel, graph-index history, or current-state back-projection.

This contract is subordinate to accepted Phase 002–009 semantics and ARCH-001–ARCH-316.