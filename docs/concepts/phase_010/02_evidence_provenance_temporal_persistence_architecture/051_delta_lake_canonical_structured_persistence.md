# ARCH-051 — Delta Lake Canonical Structured Persistence

**Status:** Accepted

The reference architecture SHALL use framework-owned Delta Lake tables as the canonical durable structured persistence substrate for evidence manifests, normalized journals, temporal/provenance links and retention metadata.

This choice does not make Delta table history/time travel the product historical-replay contract.
