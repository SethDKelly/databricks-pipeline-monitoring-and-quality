#!/usr/bin/env python3
"""Run a completed CKR validator against a temporary legacy-source path projection.

DPTN-B physically relocates history while accepted CKR validators intentionally retain
original provenance-path assumptions. This wrapper reconstructs only those old history
paths as ephemeral symlinks for the duration of one legacy CKR check. It does not alter
Git state, semantic ownership, canonical routing, or stable-ID resolution.
"""
from __future__ import annotations

import argparse, os, subprocess, sys
from pathlib import Path

PROJECTION = {
    "docs/concepts": "history/phases",
    "docs/reference": "history/reference-legacy",
    "docs/foundation": "history/foundation",
    "docs/planning": "history/planning",
    "docs/decisions": "history/decisions",
    "docs/design_history": "history/design-history",
}


def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument("script"); ap.add_argument("args",nargs=argparse.REMAINDER); ap.add_argument("--repo",default=None)
    # --repo belongs to wrapped args in normal use; derive repository from this wrapper location.
    ns=ap.parse_args(); repo=Path(__file__).resolve().parents[2]; created=[]
    try:
        if (repo/"docs/history/README.md").is_file():
            for rel,target in PROJECTION.items():
                p=repo/rel
                if p.exists() or p.is_symlink(): continue
                p.parent.mkdir(parents=True,exist_ok=True)
                os.symlink(target,p,target_is_directory=True); created.append(p)
        cmd=[sys.executable,str(repo/ns.script),*ns.args]
        return subprocess.run(cmd,cwd=repo).returncode
    finally:
        for p in reversed(created):
            try: p.unlink()
            except FileNotFoundError: pass

if __name__=="__main__": raise SystemExit(main())
