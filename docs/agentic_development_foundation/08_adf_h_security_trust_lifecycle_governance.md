# ADF-H — Security, Trust, Lifecycle & Governance

**Status:** PLANNED / READY TO EXECUTE

## Objective

Ensure the agent-facing knowledge/instruction/workflow layer improves development ergonomics without creating new security boundaries, hidden authority, stale trust or uncontrolled tool state.

## Security principles

### Repository truth stays inspectable

Project-critical instructions, portable workflows and OKF routing knowledge must be version-controlled and reviewable. Personal/user tool settings may exist for preferences but must not be required to understand DMTZ correctness.

### Least privilege applies to agents too

Tool access should follow the developer/task need. The foundation does not require broad cloud, production, secret-manager or deployment permissions merely because an agent can use them.

Human-directed local development should prefer read/edit/test permissions appropriate to the active task.

### Secrets and sensitive data

- never place secrets/tokens/credentials in OKF frontmatter, skills, instructions, logs or examples;
- do not copy restricted production payloads into agent knowledge for convenience;
- tool telemetry/chat retention policies are enterprise/deployment concerns and must be reviewed separately from repository semantics;
- knowledge/index artifacts should favor metadata and canonical links over copied sensitive content.

## Trust model

### OKF trust is advisory knowledge trust

OKF v0.2 `generated`, `verified`, trust tier, `status` and `stale_after` describe the **knowledge artifact**.

They do not grant or imply DMTZ Assertion Authority, Capability Authorization, evidence sufficiency, causal confirmation or compliance.

### Tool/model confidence is non-authoritative

Agent self-reported confidence, reasoning, memory or 'looks correct' statements never satisfy repository tests/review gates.

### Verification ownership

ADF execution should identify who/what may mark knowledge entries verified:

- humans may verify authored/routing entries against canonical sources;
- deterministic generation/validation processes may record process verification where appropriate;
- an agent that generated an entry should not be treated as independent human verification merely because it reread its output.

## Lifecycle

Knowledge entries should use OKF lifecycle deliberately:

- `draft` — not ready to be depended upon for routing;
- `stable` — reviewed/current routing reference;
- `deprecated` — retained for links/history, not current discovery.

`stale_after` is appropriate only when the content truly has an external/time-based review horizon, such as tool compatibility assumptions. It should not be placed on stable architectural routing entries simply to force periodic churn.

## Vendor/tool lifecycle

Cursor, Claude and Codex capabilities evolve independently. Maintain a compatibility verification record containing:

- tool/product name;
- relevant native feature(s);
- version/date last verified;
- official source/reference;
- current support state: verified / degraded / unverified;
- repository fallback when unavailable.

Do not encode transient vendor behavior as a permanent DMTZ architecture decision.

## Governance of changes

Changes to the agentic foundation should be reviewed by impact class:

- **routing/content maintenance** — update OKF index/links/descriptions;
- **workflow change** — update portable skill and affected adapters/tests;
- **tool-adapter change** — update only the specific adapter plus compatibility verification;
- **shared authority change** — review root `AGENTS.md` and all adapters for consistency;
- **DMTZ semantic/architecture change** — use existing DMTZ change-control, then refresh agentic routing as a consequence.

Agentic artifacts follow DMTZ; they do not initiate semantic authority changes by themselves.

## Retention

Do not build a repository archive of chat transcripts or agent scratchpads by default. Preserve only durable artifacts useful to future development:

- canonical code/docs/tests;
- reviewed ADRs;
- implementation traceability;
- OKF routing/history where useful;
- workflow definitions;
- compatibility verification evidence.

## Deliverables

- security/trust policy for agentic artifacts;
- OKF verification/lifecycle conventions;
- supported-tool compatibility lifecycle policy;
- rules for handling tool memory/personal configuration;
- review ownership and change classes;
- security/adversarial test fixtures for agentic conformance.

## Acceptance scenarios

ADF-H passes when:

- an OKF human-review signal cannot be mistaken for DMTZ authority;
- secrets/sensitive values are rejected from checked-in agentic artifacts by policy/checks;
- stale tool compatibility is visible without invalidating canonical DMTZ docs;
- agent memory cannot supersede checked-in project state;
- a tool-specific policy change cannot silently weaken shared security/change-control rules;
- removing every supported AI tool would still leave the repository understandable and buildable by a human developer.
