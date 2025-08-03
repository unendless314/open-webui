#!/usr/bin/env python3
"""Validate Run YAML files against a minimal schema."""
from __future__ import annotations
import sys
from pathlib import Path
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = REPO_ROOT / 'ai' / 'Runs' / 'schema.yaml'

with SCHEMA_PATH.open('r', encoding='utf-8') as f:
    SCHEMA = yaml.safe_load(f)

REQUIRED = SCHEMA.get('required', [])
PROPERTIES = SCHEMA.get('properties', {})


import datetime

def type_name(value):
    if isinstance(value, (str, datetime.date)):
        return 'string'
    if isinstance(value, int) and not isinstance(value, bool):
        return 'integer'
    if isinstance(value, float):
        return 'number'
    if isinstance(value, dict):
        return 'object'
    if isinstance(value, list):
        return 'array'
    if value is None:
        return 'null'
    return type(value).__name__


def validate(data: dict, path: Path) -> list[str]:
    errors = []
    for field in REQUIRED:
        if field not in data:
            errors.append(f"{path}: missing required field '{field}'")
    for key, spec in PROPERTIES.items():
        if key not in data:
            continue
        expected = spec.get('type')
        if expected:
            actual = type_name(data[key])
            if actual != expected and not (spec.get('nullable') and data[key] is None):
                errors.append(f"{path}: field '{key}' expected type {expected}, got {actual}")
        if 'enum' in spec and data[key] not in spec['enum']:
            errors.append(f"{path}: field '{key}' invalid value '{data[key]}'")
    return errors


def main(files: list[str]) -> int:
    if not files:
        files = [str(p) for p in (REPO_ROOT / 'ai' / 'Runs').rglob('*.yaml')]
    errors = []
    for fpath in files:
        p = Path(fpath)
        if p.name in {'schema.yaml', 'TEMPLATE.yaml'}:
            continue
        with p.open('r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        errors.extend(validate(data, p))
    if errors:
        print('Run YAML validation failed:', file=sys.stderr)
        for e in errors:
            print(' -', e, file=sys.stderr)
        return 1
    print('All Run YAML files valid.')
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
