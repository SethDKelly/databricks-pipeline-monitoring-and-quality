# ARCH-436 — Serving Cache Boundary

**Status:** Accepted

Caches accelerate derived responses only when cache entries retain projection revision, canonical/source watermark, applicability horizon and authorization-sensitive keying.

Cache hit is not evidence freshness and cache state is never canonical truth.