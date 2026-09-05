#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from urllib.parse import urlparse

ID_RE = re.compile(r"^(SYN|REF|AUTH|HLTH|OPS|EXPL|INTG|ARCH)-(\d{3})$")
HEADING_RE = re.compile(r"^#{2,6}\s+((?:SYN|REF|AUTH|HLTH|OPS|EXPL|INTG|ARCH)-\d{3})(?:\s|—|-|:|$)")
TOP_KEY = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*):(?:\s*(.*))?$")
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
STATE_RE = re.compile(r"^- \*\*CKR-([A-K]) — .*?: (.+?)\.\*\*$", re.M)


def scalar(raw: str) -> str:
    raw = raw.strip()
    if len(raw) >= 2 and raw[0] == raw[-1] and raw[0] in {'"', "'"}:
        return raw[1:-1]
    return raw


def frontmatter(path: Path) -> dict[str, str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    data: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        match = TOP_KEY.match(line)
        if match:
            data[match.group(1)] = scalar(match.group(2) or "")
    return data


def local_target(source: Path, target: str, repo: Path) -> Path | None:
    target = target.strip().split("#", 1)[0].strip()
    if not target or target.startswith(("http://", "https://", "mailto:")):
        return None
    if urlparse(target).scheme:
        return None
    return (repo / target.lstrip("/")).resolve() if target.startswith("/") else (source.parent / target).resolve()


def rel(repo: Path, path: Path) -> str:
    return path.resolve().relative_to(repo).as_posix()


def state_map(repo: Path) -> dict[str, str]:
    text = (repo / "docs/canonical_knowledge_retrofit/README.md").read_text(encoding="utf-8")
    return {letter: state for letter, state in STATE_RE.findall(text)}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=".")
    args = ap.parse_args()
    repo = Path(args.repo).resolve()
    errors: list[str] = []

    manifest_path = repo / "docs/canonical_knowledge_retrofit/ckr_j_routing_manifest.json"
    inventory_path = repo / "docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json"
    registry_path = repo / "docs/agentic_development_foundation/stable_id_registry.json"
    fixture_path = repo / "docs/canonical_knowledge_retrofit/fixtures/ckr_j_routing_scenarios.yaml"

    for path, label in (
        (manifest_path, "CKR-J routing manifest"),
        (inventory_path, "CKR ownership inventory"),
        (registry_path, "stable-ID registry"),
        (fixture_path, "CKR-J fixture catalog"),
    ):
        if not path.is_file():
            errors.append(f"missing {label}: {path.relative_to(repo)}")
    if errors:
        for error in errors:
            print("ERROR", error)
        return 1

    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        inventory = json.loads(inventory_path.read_text(encoding="utf-8"))
        registry = json.loads(registry_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"ERROR invalid CKR-J JSON: {exc}")
        return 1

    status = manifest.get("status")
    if manifest.get("schema_version") != "1.0":
        errors.append("CKR-J routing manifest schema_version must be 1.0")
    if status not in {"candidate_ready", "active"}:
        errors.append(f"CKR-J routing manifest status must be candidate_ready or active; found {status!r}")
    if manifest.get("purpose", "").lower().find("does not own dmtz product semantics") < 0:
        errors.append("CKR-J routing manifest must explicitly remain non-semantic routing projection")

    states = state_map(repo)
    if states.get("J") not in {"IN EXECUTION", "COMPLETE / ACCEPTED"}:
        errors.append(f"CKR-J validator may run only while CKR-J is in execution or complete; found {states.get('J')!r}")
    if status == "candidate_ready" and states.get("J") != "IN EXECUTION":
        errors.append("candidate_ready CKR-J routing manifest requires CKR-J IN EXECUTION")
    if states.get("K") not in {"PLANNED", "NEXT / READY"}:
        errors.append(f"CKR-J must not activate CKR-K; found CKR-K={states.get('K')!r}")

    stable = manifest.get("stable_reference", {})
    if stable.get("resolution_mode") != "canonical_target_definition_heading":
        errors.append("CKR-J stable-reference resolution mode drifted")
    if stable.get("canonical_locator_format") != "{owner_path}::{stable_id}":
        errors.append("CKR-J canonical locator format must remain {owner_path}::{stable_id}")
    if stable.get("section_selector") != "stable_id_token":
        errors.append("CKR-J stable selector must be the stable-ID token")
    if stable.get("default_scope") != "canonical_owner_only":
        errors.append("CKR-J default exact-ID scope must be canonical_owner_only")
    if stable.get("history_discovery") != "explicit_separate_on_demand":
        errors.append("historical stable-ID occurrence discovery must remain explicit/separate")
    if stable.get("first_match_canonicality") is not False:
        errors.append("first-match canonicality must remain false")
    if stable.get("line_number_is_identity") is not False or stable.get("renderer_slug_is_identity") is not False:
        errors.append("line numbers and renderer slugs cannot become stable identity")

    families = registry.get("families", {})
    owned_families = inventory.get("stable_families", {})
    if set(families) != set(owned_families):
        errors.append("stable-ID registry and CKR ownership inventory family sets differ")

    expected_total = 0
    resolved: dict[str, tuple[str, int, str]] = {}
    canonical_heading_count = 0

    for family, limits in families.items():
        low = int(limits.get("min", 0))
        high = int(limits.get("max", -1))
        expected_total += max(0, high - low + 1)
        owner = owned_families.get(family, {})
        if owner.get("migration_state") != "canonicalized":
            errors.append(f"{family}: CKR-J requires canonicalized stable-family ownership")
        target_docs = owner.get("target_documents", [])
        if not target_docs:
            errors.append(f"{family}: no canonical target_documents")
            continue

        seen_family: dict[str, list[tuple[str, int, str]]] = {}
        for target in target_docs:
            path = repo / target
            if not path.is_file():
                errors.append(f"{family}: missing canonical target document {target}")
                continue
            text = path.read_text(encoding="utf-8")
            if "**Authority:** CANONICAL CURRENT AUTHORITY" not in text:
                errors.append(f"{family}: canonical target lacks current-authority marker: {target}")
            for line_no, line in enumerate(text.splitlines(), start=1):
                match = HEADING_RE.match(line.strip())
                if not match:
                    continue
                token = match.group(1)
                token_match = ID_RE.match(token)
                if not token_match:
                    continue
                token_family, number_text = token_match.groups()
                if token_family != family:
                    errors.append(f"{family}: target document {target} contains foreign stable definition heading {token}")
                    continue
                number = int(number_text)
                if number < low or number > high:
                    errors.append(f"{family}: out-of-range canonical definition heading {token} in {target}")
                    continue
                seen_family.setdefault(token, []).append((target, line_no, line.strip()))

        for number in range(low, high + 1):
            token = f"{family}-{number:03d}"
            hits = seen_family.get(token, [])
            if len(hits) != 1:
                errors.append(f"{token}: expected exactly one canonical definition heading in inventoried target documents; found {len(hits)}")
                continue
            resolved[token] = hits[0]
            canonical_heading_count += 1

    if expected_total != 1237:
        errors.append(f"accepted stable-ID total changed from 1237 to {expected_total}")
    if stable.get("accepted_total") != expected_total:
        errors.append(f"CKR-J manifest accepted_total must equal registry total {expected_total}")
    if len(resolved) != expected_total:
        errors.append(f"canonical stable-reference coverage is {len(resolved)}/{expected_total}")

    # Candidate manifest routes must point only to real intended current resources.
    semantic_routes = manifest.get("okf_semantic_routes", [])
    route_paths = set()
    for route in semantic_routes:
        route_path = route.get("path")
        primary = route.get("primary_resource")
        if not route_path or route_path in route_paths:
            errors.append(f"invalid/duplicate OKF semantic route path {route_path!r}")
            continue
        route_paths.add(route_path)
        source = repo / route_path
        if not source.is_file():
            errors.append(f"missing OKF semantic route {route_path}")
            continue
        if not primary or not primary.startswith("docs/canonical/") or not (repo / primary).exists():
            errors.append(f"{route_path}: primary_resource must be an existing docs/canonical path")
        for required in route.get("required_canonical_routes", []):
            if not required.startswith("docs/canonical/") or not (repo / required).exists():
                errors.append(f"{route_path}: required canonical route missing or noncanonical: {required}")

        if status == "active":
            meta = frontmatter(source)
            actual_target = local_target(source, meta.get("resource", ""), repo)
            expected_target = (repo / primary).resolve() if primary else None
            if actual_target != expected_target:
                errors.append(f"{route_path}: live OKF resource does not match CKR-J manifest primary_resource")
            text = source.read_text(encoding="utf-8")
            resolved_links = {
                rel(repo, target)
                for raw in LINK_RE.findall(text)
                for target in [local_target(source, raw, repo)]
                if target is not None and target.exists() and target.is_relative_to(repo)
            }
            for required in route.get("required_canonical_routes", []):
                if required not in resolved_links:
                    errors.append(f"{route_path}: required canonical body route not linked: {required}")
            for forbidden in manifest.get("forbidden_current_route_patterns_after_cutover", []):
                if forbidden in text:
                    errors.append(f"{route_path}: stale pre-cutover routing text remains: {forbidden!r}")
            for target in resolved_links:
                if target.startswith("docs/concepts/phase_"):
                    errors.append(f"{route_path}: active current-semantic domain route links Phase history directly: {target}")

    project_routes = manifest.get("project_routes", [])
    for route in project_routes:
        path = repo / route.get("path", "")
        primary = route.get("primary_resource")
        if not primary or not (repo / primary).exists():
            errors.append(f"project route target missing: {primary!r}")
        if status == "active":
            if not path.is_file():
                errors.append(f"missing active project route {route.get('path')}")
                continue
            meta = frontmatter(path)
            actual = local_target(path, meta.get("resource", ""), repo)
            expected = (repo / primary).resolve() if primary else None
            if actual != expected:
                errors.append(f"{route.get('path')}: active resource does not match manifest")

    if status == "active":
        if registry.get("status") != "accepted_canonical_resolution":
            errors.append("stable_id_registry status must be accepted_canonical_resolution after CKR-J cutover")
        resolution = registry.get("resolution", {})
        if resolution.get("mode") != "canonical_target_definition_heading":
            errors.append("stable_id_registry resolution.mode must activate canonical target heading resolution")
        if resolution.get("canonical_locator_format") != "{owner_path}::{stable_id}":
            errors.append("stable_id_registry canonical locator format drifted")
        if resolution.get("history_discovery") != "explicit_separate_on_demand":
            errors.append("stable_id_registry must keep historical discovery separate")

        resolver = repo / "scripts/agentic/resolve_stable_id.py"
        if not resolver.is_file():
            errors.append("missing stable-ID resolver")
        else:
            resolver_text = resolver.read_text(encoding="utf-8")
            for token in ("canonical_target_definition_heading", "canonical_locator", "--history"):
                if token not in resolver_text:
                    errors.append(f"stable-ID resolver missing CKR-J behavior marker {token!r}")

        required_surface_tokens = {
            "AGENTS.md": ("resolve_stable_id.py", "canonical owner"),
            "docs/implementation/agent_reference_index.md": ("resolve_stable_id.py", "stable"),
            ".agents/skills/resolve-context/SKILL.md": ("resolve_stable_id.py", "--history"),
            ".agents/skills/resolve-contract/SKILL.md": ("resolve_stable_id.py", "--history"),
            ".agents/skills/update-traceability/SKILL.md": ("resolve_stable_id.py", "locator"),
            ".cursor/rules/00-implementation-routing.mdc": ("resolve_stable_id.py", "canonical"),
        }
        for surface in manifest.get("agent_routing_surfaces", []):
            path = repo / surface
            if not path.is_file():
                errors.append(f"missing CKR-J agent routing surface {surface}")
                continue
            text = path.read_text(encoding="utf-8")
            for token in required_surface_tokens.get(surface, ()):
                if token not in text:
                    errors.append(f"{surface}: missing CKR-J routing token {token!r}")

        impact = repo / "scripts/agentic/knowledge_impact.py"
        if not impact.is_file() or "BODY-LINK" not in impact.read_text(encoding="utf-8"):
            errors.append("knowledge_impact.py must include CKR-J secondary body-link routing impact support")

    fixture_text = fixture_path.read_text(encoding="utf-8")
    scenario_ids = re.findall(r"^\s*-\s+id:\s+(CKRJ-\d{2})\s*$", fixture_text, re.M)
    if scenario_ids != [f"CKRJ-{i:02d}" for i in range(1, 49)]:
        errors.append("CKR-J fixture catalog must contain CKRJ-01..CKRJ-48 exactly once and in order")

    for error in errors:
        print("ERROR", error)
    print(
        f"CKR-J routing validation: {len(errors)} error(s), "
        f"stable={len(resolved)}/{expected_total}, OKF routes={len(semantic_routes)}, "
        f"state={status}"
    )
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
