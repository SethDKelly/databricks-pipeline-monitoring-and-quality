# ARCH-063 — Physical Compaction ≠ Semantic Compaction

**Status:** Accepted

File compaction, clustering, checkpointing and storage optimization MAY rewrite physical files while preserving the exact logical record set and identifiers.

Lossy aggregation/downsampling is a separate governed lifecycle action and cannot be hidden inside storage maintenance.
