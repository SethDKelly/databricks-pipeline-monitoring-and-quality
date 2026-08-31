# ARCH-467 — Deployment Environment Isolation

**Status:** Accepted

Development/test/staging/production deployments have distinct configuration, credentials, callback identities and canonical data boundaries appropriate to their risk; production control/evidence cannot be mutated through lower-environment credentials.

Test fixtures remain clearly non-production evidence.