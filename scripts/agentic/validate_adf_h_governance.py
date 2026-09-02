#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import json
from pathlib import Path

REQUIRED_TOOLS = {'cursor', 'claude_code', 'codex'}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', default='.')
    args = ap.parse_args()
    repo = Path(args.repo).resolve()
    errors: list[str] = []
    warnings: list[str] = []

    required = {
        'policy': repo / 'docs/agentic_development_foundation/security_trust_lifecycle_policy.md',
        'governance': repo / 'docs/agentic_development_foundation/agentic_change_governance.md',
        'lifecycle': repo / 'docs/agentic_development_foundation/tool_lifecycle_review.json',
        'progression_exception': repo / 'docs/agentic_development_foundation/adf_g_progression_exception.md',
    }
    for label, path in required.items():
        if not path.is_file():
            errors.append(f'missing ADF-H {label}: {path.relative_to(repo)}')

    if required['policy'].is_file():
        text = required['policy'].read_text(encoding='utf-8').lower()
        expected = (
            'never check secrets',
            'tool memory',
            'noncanonical',
            'okf `verified` does not mean dmtz assertion authority',
            'prompt injection',
            'least privilege',
            'human fallback',
        )
        for phrase in expected:
            if phrase not in text:
                errors.append(f'security policy missing required boundary phrase: {phrase!r}')

    if required['governance'].is_file():
        text = required['governance'].read_text(encoding='utf-8')
        for cls in ('G1', 'G2', 'G3', 'G4', 'G5'):
            if cls not in text:
                errors.append(f'change governance missing class {cls}')
        if 'DMTZ semantic / architecture' not in text:
            errors.append('change governance must preserve DMTZ semantic/change-control class')

    if required['progression_exception'].is_file():
        text = required['progression_exception'].read_text(encoding='utf-8')
        for phrase in ('ADF-EX-17', 'DEFERRED VERIFICATION', 'does not convert missing runtime evidence into a PASS'):
            if phrase not in text:
                errors.append(f'ADF-G progression exception missing required limitation: {phrase!r}')

    if required['lifecycle'].is_file():
        try:
            data = json.loads(required['lifecycle'].read_text(encoding='utf-8'))
        except json.JSONDecodeError as exc:
            errors.append(f'tool_lifecycle_review.json invalid JSON: {exc}')
        else:
            today = dt.date.today()
            try:
                reviewed = dt.date.fromisoformat(data.get('reviewed_on', ''))
            except ValueError:
                errors.append('tool lifecycle reviewed_on must be ISO date')
                reviewed = None
            horizons = data.get('default_horizons_days', {})
            for key in ('instruction_and_workflow_compatibility', 'security_privacy_retention', 'runtime_smoke'):
                value = horizons.get(key)
                if not isinstance(value, int) or value <= 0:
                    errors.append(f'invalid positive review horizon: {key}')
            tools = data.get('tools', {})
            missing = REQUIRED_TOOLS - set(tools)
            if missing:
                errors.append(f'tool lifecycle missing providers: {sorted(missing)}')
            security_horizon = horizons.get('security_privacy_retention', 0)
            instruction_horizon = horizons.get('instruction_and_workflow_compatibility', 0)
            for name in REQUIRED_TOOLS & set(tools):
                tool = tools[name]
                for field, horizon in (('security_reviewed_on', security_horizon), ('instruction_reviewed_on', instruction_horizon)):
                    try:
                        date = dt.date.fromisoformat(tool.get(field, ''))
                    except ValueError:
                        errors.append(f'{name}: {field} must be ISO date')
                        continue
                    age = (today - date).days
                    if age < 0:
                        errors.append(f'{name}: {field} is in the future')
                    elif horizon and age > horizon:
                        errors.append(f'{name}: {field} exceeds {horizon}-day review horizon ({age} days old)')
                sources = tool.get('official_sources', [])
                if not sources or any(not str(src).startswith('https://') for src in sources):
                    errors.append(f'{name}: official_sources must contain HTTPS references')
                if not str(tool.get('fallback', '')).strip():
                    errors.append(f'{name}: missing degraded/unverified fallback')
                state = tool.get('runtime_status')
                if state not in {'supported', 'degraded', 'unverified', 'unsupported'}:
                    errors.append(f'{name}: invalid runtime_status {state!r}')
                if state == 'unverified':
                    warnings.append(f'{name}: runtime remains unverified under ADF-G deferred verification')
            if reviewed and (today - reviewed).days < 0:
                errors.append('tool lifecycle reviewed_on cannot be in the future')

    for warning in warnings:
        print(f'WARN {warning}')
    for error in errors:
        print(f'ERROR {error}')
    print(f'ADF-H governance validation: {len(errors)} error(s), {len(warnings)} warning(s)')
    return 1 if errors else 0


if __name__ == '__main__':
    raise SystemExit(main())
