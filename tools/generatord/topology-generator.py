#!/usr/bin/env python3
# topology-generator.py
# SUBIT‑64 Canonical Topology Packet Generator

import json
import sys
from pathlib import Path

TEMPLATE = {
    "basin": None,
    "gradient": None,
    "curvature": None,
    "transition": None,
    "stability": None
}

def load_json(path: Path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"[ERROR] Cannot load JSON: {e}")
        sys.exit(1)

def validate_input(data: dict):
    required = TEMPLATE.keys()
    missing = [k for k in required if k not in data]

    if missing:
        print(f"[ERROR] Missing required fields: {missing}")
        sys.exit(1)

def generate_topology(data: dict):
    packet = TEMPLATE.copy()
    packet.update(data)
    return packet

def save_output(packet: dict, output_path: Path):
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(packet, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"[ERROR] Cannot write output: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) < 3:
        print("Usage: topology-generator.py <input.json> <output.json>")
        sys.exit(1)

    json_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])

    data = load_json(json_path)
    validate_input(data)

    packet = generate_topology(data)
    save_output(packet, output_path)

    print(f"[GENERATED] Topology packet saved to {output_path}")

if __name__ == "__main__":
    main()
