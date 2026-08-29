# ARCH-204 — Bundle Deployment Revision Manifest

**Status:** Accepted

Bundle/workspace deployments SHOULD emit a durable deployment manifest containing source revision, bundle/artifact digest, deployment configuration revision, target workspace/resource IDs, deploy attempt and correlation ID.

The manifest proves intended/deployed artifact identity only within its attested scope.