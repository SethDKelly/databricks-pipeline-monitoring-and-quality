#!/usr/bin/env python3
from __future__ import annotations

import argparse, json, re, subprocess, sys
from pathlib import Path

ROOT = "docs/documentation_topology_normalization"
STATE_RE = re.compile(r"^- \*\*DPTN-([A-G]) — .*?: (.+?)\.\*\*$", re.M)
FIXTURE_RE = re.compile(r"^\s*-\s+id:\s+(DPTNB-\d{2})\s*$", re.M)
HISTORY_MARKER = "**Authority:** HISTORY / PROVENANCE ONLY — NOT CURRENT SEMANTIC AUTHORITY"
ORIGINAL_INVENTORY_BLOB = "c9a5e3bd6508bc56a706790ddf248b55d232852e"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def git_object(repo: Path, spec: str) -> str | None:
    p = subprocess.run(["git", "rev-parse", spec], cwd=repo, text=True, capture_output=True)
    return p.stdout.strip() if p.returncode == 0 else None


def main() -> int:
    ap = argparse.ArgumentParser(); ap.add_argument("--repo", default=".")
    repo = Path(ap.parse_args().repo).resolve(); errors: list[str] = []
    readme = repo / ROOT / "README.md"
    manifest_path = repo / ROOT / "dptn_b_relocation_manifest.json"
    fixture_path = repo / ROOT / "fixtures/dptn_b_history_scenarios.yaml"
    review_path = repo / ROOT / "dptn_b_execution_review.md"
    collision_path = repo / ROOT / "collision_register.md"
    history = repo / "docs/history/README.md"
    for p, label in ((readme,"DPTN authority"),(manifest_path,"DPTN-B relocation manifest"),(fixture_path,"DPTN-B fixtures"),(review_path,"DPTN-B execution review"),(collision_path,"DPTN collision register"),(history,"history authority index")):
        if not p.is_file(): errors.append(f"missing {label}: {p.relative_to(repo)}")
    if errors:
        for e in errors: print("ERROR", e)
        return 1

    states = {k:v for k,v in STATE_RE.findall(readme.read_text(encoding="utf-8"))}
    b_state = states.get("B")
    later_active = any(states.get(c) in {"IN EXECUTION","COMPLETE / ACCEPTED"} for c in "CDEFG")
    if states.get("A") != "COMPLETE / ACCEPTED" or b_state not in {"IN EXECUTION","COMPLETE / ACCEPTED"}:
        errors.append(f"DPTN-B validator requires A complete and B in execution/complete; A={states.get('A')!r}, B={b_state!r}")
    manifest = load_json(manifest_path)
    expected_status = "accepted" if b_state == "COMPLETE / ACCEPTED" else "candidate_ready"
    if manifest.get("status") != expected_status: errors.append(f"manifest status must be {expected_status!r}; found {manifest.get('status')!r}")
    if manifest.get("phase") != "DPTN-B" or manifest.get("schema_version") != "1.0": errors.append("DPTN-B manifest schema/phase drifted")
    if "does not own dmtz product semantics" not in manifest.get("purpose","").lower(): errors.append("DPTN-B manifest must remain explicitly non-semantic")
    if manifest.get("history_root") != "docs/history" or manifest.get("current_semantic_root_during_dptn_b") != "docs/canonical": errors.append("DPTN-B history/current root contract drifted")
    if manifest.get("authorized_move_ids") != [f"MOVE-{i:03d}" for i in range(1,7)]: errors.append("DPTN-B may authorize MOVE-001..MOVE-006 only")
    counts = manifest.get("expected_counts", {})
    if counts != {"moves":6,"closed_dptn_b_collisions":5,"concepts":24,"stable_ids":1237,"stable_families":8,"architecture_ids":500,"scenarios":24,"negative_controls":12}: errors.append(f"DPTN-B accepted counts drifted: {counts}")

    if b_state == "COMPLETE / ACCEPTED":
        collision_text = collision_path.read_text(encoding="utf-8")
        for i in range(1,6):
            token = f"COL-{i:03d} — RESOLVED BY DPTN-B"
            if token not in collision_text: errors.append(f"accepted DPTN-B missing collision resolution marker {token!r}")
        if "vacancy does not assign current authority" not in collision_text.lower(): errors.append("DPTN-B collision closure must preserve vacancy != authority")

    ht = history.read_text(encoding="utf-8")
    for token in (HISTORY_MARKER,"Current-truth rule","Preservation rule","vacant/unassigned","Implementation 001-A remains blocked"):
        if token not in ht: errors.append(f"history index missing role/boundary token {token!r}")
    if "**Authority:** CANONICAL CURRENT AUTHORITY" in ht: errors.append("history index may not claim canonical current authority")

    moves = manifest.get("moves", [])
    if [m.get("id") for m in moves] != [f"MOVE-{i:03d}" for i in range(1,7)]: errors.append("DPTN-B move evidence must contain MOVE-001..MOVE-006 exactly once and in order")
    for m in moves:
        target, expected = m.get("target"), m.get("source_tree_sha")
        if m.get("authority_change") is not False or m.get("preservation") != "exact_git_tree_reuse": errors.append(f"{m.get('id')}: history relocation must remain exact-tree/non-authority")
        if not target or not target.startswith("docs/history/") or not (repo/target).is_dir(): errors.append(f"{m.get('id')}: missing history target {target!r}")
        if expected and (repo/".git").exists():
            actual = git_object(repo, f"HEAD:{target}")
            if actual != expected: errors.append(f"{m.get('id')}: target tree differs from accepted source tree; expected {expected}, found {actual}")

    if not later_active:
        for src in ("docs/concepts","docs/reference","docs/foundation","docs/planning","docs/decisions","docs/design_history"):
            if (repo/src).exists(): errors.append(f"DPTN-B source collision was not cleared: {src}")
        canonical_sha = git_object(repo, "HEAD:docs/canonical") if (repo/".git").exists() else None
        if canonical_sha and canonical_sha != manifest.get("canonical_tree_baseline_sha"): errors.append(f"docs/canonical changed during DPTN-B; expected {manifest.get('canonical_tree_baseline_sha')}, found {canonical_sha}")
        inventory_sha = git_object(repo, "HEAD:docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json") if (repo/".git").exists() else None
        if inventory_sha and inventory_sha != ORIGINAL_INVENTORY_BLOB: errors.append("CKR ownership inventory changed during history-only DPTN-B")

    for rel in ("docs/agentic_development_foundation","docs/canonical_knowledge_retrofit"):
        if not (repo/rel).is_dir(): errors.append(f"mixed-lifecycle directory moved prematurely: {rel}")
    registry = load_json(repo/"docs/agentic_development_foundation/stable_id_registry.json")
    total = sum(int(x["max"])-int(x["min"])+1 for x in registry.get("families",{}).values())
    if total != 1237 or len(registry.get("families",{})) != 8: errors.append(f"stable-ID baseline changed: families={len(registry.get('families',{}))}, ids={total}")
    inventory = load_json(repo/"docs/canonical_knowledge_retrofit/canonical_ownership_inventory.json")
    if inventory.get("concept_count") != 24 or inventory.get("canonical_root") not in {"docs/canonical","docs"}: errors.append("concept/canonical-root baseline changed outside recognized DPTN progression")
    if inventory.get("canonical_root")=="docs" and inventory.get("canonical_layout")!="first_class_dptn_c": errors.append("normalized canonical root requires DPTN-C first-class layout marker")
    arch = inventory.get("stable_families",{}).get("ARCH",{})
    if arch.get("accepted_range") != "ARCH-001..ARCH-500": errors.append("ARCH range changed")

    ids = FIXTURE_RE.findall(fixture_path.read_text(encoding="utf-8"))
    if ids != [f"DPTNB-{i:02d}" for i in range(1,25)]: errors.append("DPTN-B fixtures must contain DPTNB-01..DPTNB-24 exactly once and in order")
    fixture_status = re.search(r"^status:\s+(\S+)", fixture_path.read_text(encoding="utf-8"), re.M)
    expected_fixture_status = "accepted" if b_state == "COMPLETE / ACCEPTED" else "candidate_ready"
    if not fixture_status or fixture_status.group(1) != expected_fixture_status: errors.append(f"DPTN-B fixture status must be {expected_fixture_status}")
    review = review_path.read_text(encoding="utf-8")
    expected_review = "**Status:** ACCEPTED — DPTN-B COMPLETE" if b_state == "COMPLETE / ACCEPTED" else "**Status:** IN EXECUTION"
    if expected_review not in review: errors.append(f"DPTN-B execution review missing state marker {expected_review!r}")
    impl = (repo/"docs/implementation/README.md").read_text(encoding="utf-8")
    if "Implementation 001-A — BLOCKED / NOT STARTED" not in impl: errors.append("Implementation 001-A gate was released during DPTN-B")

    if not later_active:
        for token in ("SYN-001","AUTH-034","OPS-123","ARCH-500"):
            p = subprocess.run([sys.executable,str(repo/"scripts/agentic/resolve_stable_id.py"),token,"--repo",str(repo),"--json"],cwd=repo,text=True,capture_output=True)
            if p.returncode != 0:
                errors.append(f"{token}: canonical stable-ID resolution failed during DPTN-B")
                continue
            payload = json.loads(p.stdout)
            if not payload.get("canonical_owner",{}).get("path","").startswith("docs/canonical/"): errors.append(f"{token}: default resolution escaped canonical current owners")

    for e in errors: print("ERROR", e)
    print(f"DPTN-B history validation: {len(errors)} error(s), moves={len(moves)}/6, scenarios={len(ids)}/24, stable_ids={total}, state={b_state}")
    return 1 if errors else 0

if __name__ == "__main__": raise SystemExit(main())
