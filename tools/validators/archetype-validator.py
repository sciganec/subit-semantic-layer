#!/usr/bin/env python3
# archetype-validator.py
# SUBIT‑64 Canonical Validator

import json
import sys
from pathlib import Path

REQUIRED_FIELDS = [
    "code",
    "name",
    "essence",
    "domain",
    "shadow",
]

def load_archetypes(path: Path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"[ERROR] Cannot load archetypes: {e}")
        sys.exit(1)

def validate_structure(archetypes: dict):
    errors = []

    if not isinstance(archetypes, dict):
        errors.append("Root must be a dictionary of archetypes.")
        return errors

    if len(archetypes) != 64:
        errors.append(f"Expected 64 archetypes, found {len(archetypes)}.")

    for key, data in archetypes.items():
        if not isinstance(data, dict):
            errors.append(f"{key}: archetype must be an object.")
            continue

        for field in REQUIRED_FIELDS:
            if field not in data:
                errors.append(f"{key}: missing required field '{field}'.")

        code = data.get("code")
        if code and len(code) != 6:
            errors.append(f"{key}: code must be 6 bits (e.g., '010101').")

    return errors

def validate_uniqueness(archetypes: dict):
    errors = []
    codes = [a.get("code") for a in archetypes.values()]
    duplicates = {c for c in codes if codes.count(c) > 1}

    if duplicates:
        errors.append(f"Duplicate archetype codes: {sorted(list(duplicates))}")

    return errors

def validate_domains(archetypes: dict):
    errors = []
    for key, data in archetypes.items():
        domain = data.get("domain")
        if domain and not isinstance(domain, str):
            errors.append(f"{key}: domain must be a string.")
    return errors

def validate_shadow(archetypes: dict):
    errors = []
    for key, data in archetypes.items():
        shadow = data.get("shadow")
        if shadow is None:
            continue
        if not isinstance(shadow, (int, float)):
            errors.append(f"{key}: shadow must be numeric.")
        elif not (0 <= shadow <= 1):
            errors.append(f"{key}: shadow must be between 0 and 1.")
    return errors

def run_all_validations(archetypes: dict):
    errors = []
    errors += validate_structure(archetypes)
    errors += validate_uniqueness(archetypes)
    errors += validate_domains(archetypes)
    errors += validate_shadow(archetypes)
    return errors

def main():
    if len(sys.argv) < 2:
        print("Usage: archetype-validator.py <archetypes.json>")
        sys.exit(1)

    path = Path(sys.argv[1])
    archetypes = load_archetypes(path)
    errors = run_all_validations(archetypes)

    if errors:
        print("\n[VALIDATION FAILED]")
        for e in errors:
            print(" -", e)
        sys.exit(1)

    print("[VALIDATION PASSED] All archetypes are valid.")

if __name__ == "__main__":
    main()
