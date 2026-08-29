# ARCH-296 — Retrieval Authorization Filter

**Status:** Accepted

Retrieval corpus and returned candidates are filtered by tenant, residency, authorization, disclosure, time, and scope before model exposure; post-filtering alone is insufficient where retrieval itself leaks sensitive metadata.

This contract is subordinate to accepted Phase 002–009 semantics and ARCH-001–ARCH-295.