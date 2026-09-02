#!/usr/bin/env python3
"""Validate ADF-G compatibility/onboarding evidence without fabricating runtime PASS."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

TOOLS = ("cursor", "claude_code", "codex")
VALID_RUNTIME = {"supported", "degraded", "unverified", "unsupported"}
PASS_RUNTIME = {"supported", "degraded"}
REQUIRED_DOCS = (
    "docs/agentic_development_foundation/adf_g_runtime_probe.md",
    "docs/agentic_development_foundation/developer_onboarding.md",
    "docs/agentic_development_foundation/tool_compatibility_matrix.md",
    "docs/agentic_development_foundation/runtime_compatibility_evidence.json",
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".")
    args = parser.parse_args()
    repo = Path(args.repo).resolve()
    errors: list[str] = []
    warnings: list[str] = []

    for rel in REQUIRED_DOCS:
        if not (repo / rel).is_file():
            errors.append(f"missing ADF-G artifact: {rel}")

    evidence_path = repo / "docs/agentic_development_foundation/runtime_compatibility_evidence.json"
    manifest_path = repo / "docs/agentic_development_foundation/tool_compatibility.json"
    if not evidence_path.is_file() or not manifest_path.is_file():
        for error in errors:
            print(f"ERROR {error}")
        return 1

    try:
        evidence = json.loads(evidence_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"runtime compatibility evidence is invalid JSON: {exc}")
        evidence = {}
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"tool compatibility manifest is invalid JSON: {exc}")
        manifest = {}

    if evidence.get("exercise_id") != "ADF-G-XT01":
        errors.append("runtime evidence must use exercise_id ADF-G-XT01")
    if evidence.get("representative_task_action_class") != "A1-read-review-plan":
        errors.append("ADF-G representative task must remain A1-read-review-plan")

    evidence_tools = evidence.get("tools", {})
    manifest_tools = manifest.get("tools", {})
    for tool in TOOLS:
        data = evidence_tools.get(tool)
        if not isinstance(data, dict):
            errors.append(f"runtime evidence missing tool {tool}")
            continue
        state = data.get("runtime_status")
        if state not in VALID_RUNTIME:
            errors.append(f"{tool}: invalid runtime_status {state!r}")
            continue
        if not data.get("documentation_verified_on"):
            errors.append(f"{tool}: documentation_verified_on is required")

        if state in PASS_RUNTIME:
            if data.get("exercise_result") != "pass":
                errors.append(f"{tool}: {state} requires exercise_result=pass")
            if not data.get("runtime_verified_on"):
                errors.append(f"{tool}: {state} requires runtime_verified_on")
            if not data.get("invocation"):
                errors.append(f"{tool}: {state} requires actual runtime invocation evidence")
            observations = data.get("observations")
            if not isinstance(observations, list) or len(observations) < 5:
                errors.append(f"{tool}: {state} requires substantive bounded-task observations")
        elif state == "unverified":
            if data.get("exercise_result") != "not_run":
                errors.append(f"{tool}: unverified requires exercise_result=not_run")
            if data.get("runtime_verified_on") is not None:
                errors.append(f"{tool}: unverified must not claim runtime_verified_on")
            if not data.get("reason"):
                errors.append(f"{tool}: unverified requires an explicit reason")
            warnings.append(f"{tool}: provider runtime remains unverified")
        elif state == "unsupported":
            if not data.get("reason"):
                errors.append(f"{tool}: unsupported requires an explicit reason")

        manifest_status = str(manifest_tools.get(tool, {}).get("support_status", ""))
        if state == "unverified" and "runtime_smoke_pending" not in manifest_status:
            errors.append(f"{tool}: manifest must remain runtime_smoke_pending while runtime evidence is unverified")
        if state == "supported" and "runtime_smoke_pending" in manifest_status:
            errors.append(f"{tool}: manifest still says runtime_smoke_pending despite supported runtime evidence")

    ordinary = evidence.get("ordinary_cli", {})
    if ordinary.get("runtime_status") != "supported" or ordinary.get("exercise_result") != "pass":
        errors.append("ordinary_cli must remain supported with passing repository-owned evidence")
    canonical = "python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md"
    if ordinary.get("canonical_command") != canonical:
        errors.append("ordinary_cli canonical conformance command drifted")

    onboarding = (repo / "docs/agentic_development_foundation/developer_onboarding.md")
    if onboarding.is_file():
        text = onboarding.read_text(encoding="utf-8")
        for required in ("AGENTS.md", "knowledge/index.md", "AUTH-034", canonical, "Ordinary IDE / CLI"):
            if required not in text:
                errors.append(f"developer onboarding missing required route/step: {required}")

    matrix = repo / "docs/agentic_development_foundation/tool_compatibility_matrix.md"
    if matrix.is_file():
        text = matrix.read_text(encoding="utf-8")
        if "documented vendor feature is not a runtime PASS" not in text:
            errors.append("compatibility matrix must separate documentation from runtime proof")
        if "ordinary IDE/CLI" not in text:
            errors.append("compatibility matrix must preserve non-agent development")

    for warning in warnings:
        print(f"WARN {warning}")
    for error in errors:
        print(f"ERROR {error}")
    print(f"ADF-G compatibility evidence: {len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
