# ARCH-465 — Worker / Orchestration Separation

**Status:** Accepted

Long-running acquisition, normalization, reconciliation, archive, replay and heavy reasoning work is separated from synchronous request handling through a deployment-appropriate orchestration/worker boundary.

No universal queue/workflow product is mandated.