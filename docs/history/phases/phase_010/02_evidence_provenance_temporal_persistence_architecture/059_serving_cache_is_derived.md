# ARCH-059 — Serving Cache Is Derived

**Status:** Accepted

Low-latency serving caches/materializations MAY be introduced later, but SHALL preserve source/version/projection identity and remain rebuildable from canonical persistence.

Cache freshness or availability does not rewrite the canonical evidence/history state.
