#!/usr/bin/env python3
# state-visualizer.py
# SUBIT‑64 State Heatmap Visualizer

import json
import sys
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

def load_json(path: Path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"[ERROR] Cannot load JSON: {e}")
        sys.exit(1)

def validate_data(data: dict):
    if not isinstance(data, dict):
        print("[ERROR] Input must be a dictionary of state:value pairs.")
        sys.exit(1)

    if len(data) != 64:
        print(f"[ERROR] Expected 64 states, found {len(data)}.")
        sys.exit(1)

    for k, v in data.items():
        if not isinstance(v, (int, float)):
            print(f"[ERROR] State '{k}' must have numeric value.")
            sys.exit(1)

def build_grid(data: dict):
    values = [data[str(i)] for i in range(64)]
    grid = np.array(values).reshape(8, 8)
    return grid

def plot_heatmap(grid: np.ndarray, title: str, output_path: Path):
    plt.figure(figsize=(8, 8))
    plt.imshow(grid, cmap="viridis", interpolation="nearest")
    plt.colorbar(label="Value")
    plt.title(title)
    plt.xlabel("Column")
    plt.ylabel("Row")

    for i in range(8):
        for j in range(8):
            plt.text(j, i, f"{i*8+j}", ha="center", va="center", color="white", fontsize=7)

    try:
        plt.savefig(output_path, dpi=200, bbox_inches="tight")
        print(f"[GENERATED] Heatmap saved to {output_path}")
    except Exception as e:
        print(f"[ERROR] Cannot save heatmap: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) < 3:
        print("Usage: state-visualizer.py <states.json> <output.png>")
        sys.exit(1)

    json_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])

    data = load_json(json_path)
    validate_data(data)

    grid = build_grid(data)
    plot_heatmap(grid, "SUBIT‑64 State Map", output_path)

if __name__ == "__main__":
    main()
