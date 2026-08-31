# Group 08 — Security, Identity & Secrets Architecture

## Identity boundary

Authentication establishes a human/workload identity claim; Group 03 canonical Principal binding and Capability Authorization remain authoritative DMTZ governance layers.

Human-facing deployments should federate to an enterprise identity provider where available. Acquisition, serving, reasoning, archive and active-control workloads use distinct least-privilege service/workload identities where practical.

## Credential posture

Prefer short-lived OAuth/OIDC/federated credentials where verified capabilities support the workload. Long-lived credentials are explicit exceptions with secret-store indirection, rotation/revocation and narrow scope.

Secret values are never canonical evidence. Runtime manifests/logs/traces retain only disclosure-safe references/digests/identity where needed.

## Authorization enforcement

Every material request carries tenant, canonical requester/service identity, purpose/delivery, subject/scope/time and detail/export intent. Runtime authorization is evaluated before protected output/action.

Internal service processing permission never grants requester visibility.

For active control, the authorization decision and applicability horizon are bound to the opportunity. Revocation-sensitive or materially delayed actions revalidate authorization before irreversible enforcement when policy requires it.

## Network and callback trust

Expose only required ingress/egress paths; prefer private/restricted connectivity when deployment capabilities justify it. Webhook/protection/attestation/control callbacks require authenticity/integrity validation and replay/idempotency protection.

## Telemetry minimization

Logs/traces must not leak secrets, raw restricted evidence, hidden basis counts/provenance, or sensitive query text merely for debugging convenience. Security observability follows its own retention/disclosure policy.

## Tenant/residency isolation

Canonical data, indexes, caches and processing remain tenant/residency scoped. Any cross-boundary aggregation is explicitly authorized and data-minimized.