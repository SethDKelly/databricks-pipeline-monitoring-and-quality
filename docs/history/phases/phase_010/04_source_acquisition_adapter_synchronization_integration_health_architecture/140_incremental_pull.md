# ARCH-140 — Incremental Pull

**Status:** Accepted

Incremental pulls use source-supported cursors, sequence fields, timestamps, page tokens or equivalent continuation state with provenance.

A cursor reduces repeated work but does not prove that the source publishes every relevant event or that no gap occurred.
