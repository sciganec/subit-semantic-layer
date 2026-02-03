#!/usr/bin/env python3
# topology-validator.py
# SUBIT‑64 Canonical Validator

import json
import sys
from pathlib import Path

REQUIRED_FIELDS = [
    "basin",
    "gradient",
    "curvature",
    "transition",
    "stability"
]

def load_topology(path: Path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"[ERROR] Cannot load topology packet: {e}")
        sys.exit(1)

def validate_structure(packet: dict):
    errors = []

    if not isinstance(packet, dict):
        errors.append("Topology packet must be a JSON object.")
        return errors

    for field in REQUIRED_FIELDS:
        if field not in packet:
            errors.append(f"Missing required field '{field}'.")

    return errors

def validate_basin(packet: dict):
    errors = []
    basin = packet.get("basin")

    if basin is None or not isinstance(basin, str) or not basin.strip():
        errors.append("Field 'basin' must be a non-empty string.")

    return errors

def validate_gradient(packet: dict):
    errors = []
    gradient = packet.get("gradient")

    if not isinstance(gradient, (int, float)):
        errors.append("Field 'gradient' must be numeric.")
    elif not (0 <= gradient <= 1):
        errors.append("Field 'gradient' must be between 0 and 1.")

    return errors

def validate_curvature(packet: dict):
    errors = []
    curvature = packet.get("curvature")

    if not isinstance(curvature, (int, float)):
        errors.append("Field 'curvature' must be numeric.")
    elif curvature < 0:
        errors.append("Field 'curvature' must be >= 0.")

    return errors

def validate_transition(packet: dict):
    errors = []
    transition = packet.get("transition")

    if transition is None:
        errors.append("Field 'transition' must not be null.")
    elif not isinstance(transition, str):
        errors.append("Field 'transition' must be a string.")

    return errors

def validate_stability(packet: dict):
    errors = []
    stability = packet.get("stability")

    if not isinstance(stability, (int, float)):
        errors.append("Field 'stability' must be numeric.")
    elif not (0 <= stability <= 1):
        errors.append("Field 'stability' must be between 0 and 1.")

    return errors

def run_all_validations(packet: dict):
    errors = []
    errors += validate_structure(packet)
    errors += validate_basin(packet)
    errors += validate_gradient(packet)
    errors += validate_curvature(packet)
    errors += validate_transition(packet)
    errors += validate_stability(packet)
    return errors

def main():
    if len(sys.argv) < 2:
        print("Usage: topology-validator.py <topology_packet.json>")
        sys.exit(1)

    path = Path(sys.argv[1])
    packet = load_topology(path)
    errors = run_all_validations(packet)

    if errors:
        print("\n[VALIDATION FAILED]")
        for e in errors:
            print(" -", e)
        sys.exit(1)

    print("[VALIDATION PASSED] Topology packet is valid.")

if __name__ == "__main__":
    main()
