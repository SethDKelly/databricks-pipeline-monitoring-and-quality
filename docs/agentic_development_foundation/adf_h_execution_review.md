# ADF-H — Execution Review

**Status:** ACCEPTED — ADF-H COMPLETE

## Review question

Does the agent-facing foundation preserve inspectable repository truth, least privilege, secret/sensitive-data boundaries, trust separation, provider lifecycle discipline, noncanonical tool memory and ordinary human fallback without creating a new security or semantic authority?

**Conclusion: yes.**

ADF-H is accepted on actual repository-level conformance evidence. The human-authorized ADF-G progression exception remains separate: ADF-EX-17 is deferred verification, not PASS, and Cursor/Claude Code/Codex remain runtime-`unverified`.

## Delivered artifacts

- `security_trust_lifecycle_policy.md` — least privilege, secret/sensitive-data, prompt-injection/content-trust, memory, lifecycle, retention and human-fallback rules;
- `agentic_change_governance.md` — G1–G5 impact classes and review ownership;
- `tool_lifecycle_review.json` — provider review horizons, sources, current runtime state and fallback;
- `adf_h_security_baseline.md` — current external security compatibility input, explicitly non-semantic;
- `adf_g_progression_exception.md` — bounded human-authorized ADF-EX-17 deferred-verification decision;
- `scripts/agentic/scan_agentic_secrets.py` — high-confidence checked-in agentic secret/local-state guard;
- `scripts/agentic/validate_adf_h_governance.py` — lifecycle/security/governance validation;
- `fixtures/adf_h_security_scenarios.yaml` — ADF-H adversarial/boundary scenarios;
- `.gitignore` exclusion for `.claude/settings.local.json` as noncanonical local permission state;
- ADF-F conformance, CI triggers and negative controls extended through ADF-H.

## Findings

### 1. Repository security boundary — PASS

Agentic artifacts may guide work but cannot grant credentials, cloud permissions, DMTZ Assertion Authority, Capability Authorization, disclosure permission, causal confirmation, control authority or production access.

Provider sandboxes, permission modes, workspace trust, privacy controls, hooks, MCP restrictions and network policy are technical/deployment controls that supplement rather than replace DMTZ repository authority and normal organizational security controls.

### 2. Least privilege / human-directed action — PASS

ADF-H preserves the ADF-A action model:

- A1 prefers read-only repository/local access;
- A2 uses bounded edit/test access;
- A3 external/destructive/scope-expanding action requires explicit task-specific authorization and normal environment/repository gates;
- A4 semantic/architecture change uses DMTZ change control.

The presence of a coding-agent capability never grants the corresponding permission automatically.

### 3. Secrets and sensitive data — PASS

The policy forbids checked-in credentials, tokens, private keys, secret-bearing environment files and convenience copies of restricted production/customer evidence in agentic artifacts.

`scan_agentic_secrets.py` checks high-confidence credential/private-key forms, structured non-placeholder secret assignments, secret-bearing filenames and local-personal state such as `settings.local.json` across the checked-in agentic surfaces.

The scanner is explicitly a bounded repository guard, not a replacement for organization-wide secret scanning, DLP, dependency review, credential rotation or incident response.

### 4. Prompt injection / untrusted content — PASS

Instructions found in ordinary repository content, issues, external pages, generated artifacts or third-party output remain **content**, not authority. They cannot authorize A3/A4 action, permission escalation or security-control bypass merely by appearing in context.

Repository-level MCP servers, plugins, extensions, remote agents and cloud-execution integrations are governed as security/dependency changes with explicit privilege/data/network/retention/update/fallback review.

### 5. Trust firewall — PASS

ADF-H freezes the following separations:

- OKF `verified` ≠ DMTZ Assertion Authority;
- OKF `stable` ≠ monitored data/system health;
- OKF provenance ≠ proposition-level evidence sufficiency;
- human review of a routing artifact ≠ causal confirmation/compliance;
- agent/model confidence ≠ executable validation or authorization;
- an agent rereading its own generated artifact ≠ independent verification.

Canonical resources continue to win conflicts with routing summaries.

### 6. Tool memory / personal state — PASS

Tool memory, auto-memory, chat history, user rules, local settings, model preferences and saved prompts are explicitly noncanonical. They cannot redefine repository acceptance criteria, weaken A1–A4, create durable team truth absent from checked-in authority or grant external/destructive permission.

`.claude/settings.local.json` is explicitly ignored and rejected if checked into the governed agentic surface.

### 7. Lifecycle / stale compatibility — PASS

`tool_lifecycle_review.json` establishes review horizons of:

- instruction/workflow compatibility — 90 days;
- security/privacy/retention — 30 days;
- runtime smoke — 60 days.

Immediate re-verification is also required for runtime-smoke failure, material instruction/skill discovery changes, material permission/sandbox/privacy/retention changes, new repository-level external integration, or an exceeded review horizon.

An expired or uncertain vendor fact becomes degraded/unverified rather than silently rewriting DMTZ semantics.

### 8. Provider lifecycle and ADF-G evidence agree — PASS

ADF-H validates that provider lifecycle runtime state matches the ADF-G evidence ledger. Current state remains:

- Cursor — `unverified`;
- Claude Code — `unverified`;
- Codex — `unverified`;
- ordinary IDE/CLI — supported under the ADF-G evidence model.

The ADF-G progression exception does not promote those providers to runtime-supported.

### 9. Agentic change governance — PASS

ADF-H establishes G1–G5 change classes:

1. G1 — routing/content maintenance;
2. G2 — workflow behavior;
3. G3 — tool adapter/compatibility;
4. G4 — shared authority/security;
5. G5 — DMTZ semantic/architecture change.

A lower class cannot disguise a higher-impact change. G5 uses the established DMTZ change-control path first; agentic routing changes follow as a consequence.

### 10. Retention / human fallback — PASS

The repository does not require a transcript/scratchpad/hidden-reasoning archive. Durable retention is limited to useful reviewed development artifacts and bounded evidence.

Removing Cursor, Claude Code and Codex leaves Git, an editor, Python, checked-in authority/workflows and repository validation sufficient to understand and operate the development process.

### 11. External security compatibility review — PASS

Current official Cursor, Claude Code and Codex/OpenAI security guidance was rechecked on 2026-09-02. ADF-H adopts durable cross-provider principles rather than pinning optional/transient provider modes as DMTZ architecture.

The external review is recorded in `adf_h_security_baseline.md` and `tool_lifecycle_review.json`; actual target-deployment settings remain verification facts rather than repository semantic authority.

### 12. First real ADF-H CI run detected a policy/validator clarity defect — PASS / useful failure evidence

Agentic conformance run **#24** failed while Documentation consistency run **#142** passed.

All substantive security checks already passed in run #24, including the new secret scanner and all 10 negative controls. The sole failure was that `validate_adf_h_governance.py` required the durable phrase `tool memory`, while the policy expressed the same boundary using `auto-memory`, chat history and personal configuration without that exact phrase.

The policy was clarified to state explicitly:

> **Tool memory**, auto-memory, chat history, user rules, local settings, model preferences, saved prompts and personal tool configuration are noncanonical.

The validator was not weakened.

### 13. Corrected repository conformance — PASS

After the policy clarification, **Agentic conformance #25** (run ID `33698279639`, job `100471805073`) completed successfully. **Documentation consistency #143** also completed successfully on the same branch head.

Run #25 reported:

- documentation consistency — PASS;
- OKF structure/resources — PASS, 0 errors / 0 warnings;
- tool adapters — PASS, with the expected three runtime-smoke-pending warnings;
- portable skills — PASS;
- agentic references — PASS, 30 unique accepted stable IDs checked;
- ADF status drift — PASS;
- fixture catalog — PASS, **104 scenarios** across ADF-A–ADF-H;
- context budgets — PASS;
- ADF-G compatibility evidence — PASS, 0 errors / 3 expected provider-runtime-unverified warnings;
- agentic secret scan — PASS, **0 errors / 120 text files scanned**;
- ADF-H security/lifecycle governance — PASS, **0 errors / 3 expected provider-runtime-unverified warnings**;
- negative controls — PASS, **10 / 10 seeded defects detected**;
- deprecated knowledge entries — 0;
- stale knowledge entries — 0.

The two ADF-H-specific negative controls prove that a seeded high-confidence checked-in credential and an expired provider security review horizon are both rejected.

### 14. Context efficiency remains healthy — PASS

Run #25 measured:

- root `AGENTS.md`: **10,485 / 16,384 bytes**;
- `.claude/CLAUDE.md`: **1,054 / 2,048 bytes**;
- Cursor rules aggregate: **19,503 / 32,768 bytes**;
- Cursor routing rule: **3,992 / 6,144 bytes**;
- Cursor root baseline: **10,485 / 20,480 bytes**;
- Claude root baseline: **11,539 / 18,432 bytes**;
- Codex root baseline: **10,485 / 16,384 bytes**;
- all skills, command bridges and OKF routing artifacts remained within their configured limits.

Security/governance therefore did not reintroduce a monolithic always-loaded instruction surface.

### 15. ADF-G progression exception remains bounded — PASS

The human-authorized exception defers only ADF-EX-17. It does not waive shared authority, canonical-reference, security, human-directed action or deterministic conformance requirements.

A future failed Cursor/Claude/Codex runtime smoke must reopen the affected adapter/support claim before that provider is relied on as supported.

## Relationship to foundation exit gates

ADF-H supplies direct implementation/execution evidence for:

- **ADF-EX-19** — secrets/sensitive data excluded from checked-in agentic artifacts and tool memory explicitly noncanonical;
- **ADF-EX-20** — supported-tool compatibility assumptions have current review metadata, defined horizons and explicit degraded/unverified behavior.

It also strengthens ADF-EX-03, ADF-EX-06, ADF-EX-13, ADF-EX-14, ADF-EX-15, ADF-EX-16 and ADF-EX-18.

**ADF-EX-17 remains deferred verification under the explicit bounded progression exception. It is not PASS.**

## Exit decision

**ADF-H — Security, Trust, Lifecycle & Governance: COMPLETE / ACCEPTED.**

The next required work is the **Agentic Development Foundation execution exit review**, which must evaluate ADF-EX-01–ADF-EX-20 and explicitly decide the bounded ADF-EX-17 deferred-verification waiver before Implementation 001-A can begin.
