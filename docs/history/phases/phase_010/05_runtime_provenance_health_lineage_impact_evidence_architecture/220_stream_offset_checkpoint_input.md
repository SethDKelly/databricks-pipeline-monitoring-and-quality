# ARCH-220 — Stream Offset / Checkpoint Input

**Status:** Accepted

Streaming consumption records bind source/topic/table identity to evidenced offset/version ranges, watermarks/checkpoint state and processing interval where the source/runtime exposes them.

Configured subscription does not prove which events were consumed.