# ARCH-062 — Migration Without Historical Rewrite

**Status:** Accepted

Storage/schema migrations SHALL preserve durable evidence identity, provenance links and semantic history even when physical layout changes.

A migration may supersede a representation, but it cannot rewrite what source material was collected or what was known at an earlier cutoff.
