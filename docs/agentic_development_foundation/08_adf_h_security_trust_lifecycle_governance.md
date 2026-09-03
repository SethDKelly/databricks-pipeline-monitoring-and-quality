# ADF-H — Security, Trust, Lifecycle & Governance

**Status:** IN EXECUTION — IMPLEMENTED / FINAL CONFORMANCE PENDING

## Objective

Ensure the agent-facing knowledge/instruction/workflow layer improves development ergonomics without creating new security boundaries, hidden authority, stale trust or uncontrolled tool state.

## Security principles

### Repository truth stays inspectable

Project-critical instructions, portable workflows and OKF routing knowledge must be version-controlled and reviewable. Personal/user tool settings may exist for preferences but must not be required to understand DMTZ correctness.

### Least privilege applies to agents too

Tool access follows the developer/task need. The foundation does not require broad cloud, production, secret-manager, deployment or unrestricted-network permissions merely because an agent can use them.

Human-directed local development should prefer read/edit/test permissions appropriate to the active task. A3 external/destructive/scope-expanding action remains separately authorized.

### Secrets and sensitive data

- never place secrets/tokens/credentials/private keys in OKF frontmatter, skills, instructions, logs or examples;
- do not copy restricted production payloads into agent knowledge for convenience;
- provider telemetry/chat retention is a deployment concern reviewed separately from DMTZ semantics;
- routing artifacts favor metadata/redacted examples/canonical links over copied sensitive content.

## Trust model

### Agentic trust is advisory artifact trust

OKF `generated`, `verified`, lifecycle state and staleness describe the **knowledge artifact**.

They do not grant or imply DMTZ Assertion Authority, Capability Authorization, evidence sufficiency, causal confirmation, compliance or production permission.

### Tool/model confidence is non-authoritative

Agent confidence, reasoning, memory or “looks correct” statements never satisfy repository tests/review gates. A tool rereading its own output is not independent verification.

## Lifecycle

Knowledge entries use OKF lifecycle deliberately:

- `draft` — not ready for normal routing dependence;
- `stable` — reviewed/current routing reference;
- `deprecated` — historical/transitional, not preferred current discovery.

`stale_after` is reserved for genuinely external/time-sensitive knowledge. Canonical architecture is not made stale merely to force periodic churn.

Provider compatibility/security facts use explicit review horizons and immediate re-verification triggers. Stale vendor assumptions become degraded/unverified rather than rewriting DMTZ semantics.

## Governance of changes

ADF-H implements G1–G5 impact classes:

- G1 routing/content maintenance;
- G2 workflow behavior;
- G3 tool adapter/compatibility;
- G4 shared authority/security;
- G5 DMTZ semantic/architecture change.

A lower class cannot disguise a higher-impact change. Agentic artifacts follow DMTZ; G5 changes use the existing DMTZ change-control path first.

## Memory, personal configuration and retention

Chat history, auto-memory, user rules, local settings, saved prompts and model preferences remain noncanonical.

Do not build a repository archive of agent conversations, hidden reasoning or scratchpads by default. Preserve reviewed durable development artifacts/evidence with a clear purpose.

## External integrations

Repository-level MCP servers, plugins, extensions, remote agents or cloud execution integrations are security/dependency changes. Before adoption, review ownership/source, privileges, data/network exposure, credential requirements, retention/telemetry, update path and degraded fallback.

## Implemented deliverables

- [`security_trust_lifecycle_policy.md`](security_trust_lifecycle_policy.md);
- [`agentic_change_governance.md`](agentic_change_governance.md);
- [`tool_lifecycle_review.json`](tool_lifecycle_review.json);
- [`adf_h_security_baseline.md`](adf_h_security_baseline.md);
- `scripts/agentic/scan_agentic_secrets.py`;
- `scripts/agentic/validate_adf_h_governance.py`;
- `fixtures/adf_h_security_scenarios.yaml`;
- ADF-H checks/negative controls integrated into unified agentic conformance.

The bounded ADF-G progression exception is recorded separately in [`adf_g_progression_exception.md`](adf_g_progression_exception.md). It defers ADF-EX-17 only and cannot weaken ADF-H security acceptance.

## Acceptance scenarios

ADF-H passes when:

- an OKF human-review signal cannot be mistaken for DMTZ authority;
- secrets/sensitive values are rejected from checked-in agentic artifacts by policy/checks;
- stale tool compatibility is visible without invalidating canonical DMTZ docs;
- agent memory cannot supersede checked-in project state;
- a tool-specific policy change cannot silently weaken shared security/change-control rules;
- removing every supported AI tool still leaves the repository understandable and operable by a human developer;
- expired provider security assumptions and fabricated support claims fail closed;
- the final synchronized branch passes unified repository conformance.
