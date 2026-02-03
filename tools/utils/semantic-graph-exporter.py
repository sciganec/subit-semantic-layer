#!/usr/bin/env python3
# semantic-graph-exporter.py
# SUBIT‑64 Canonical Semantic Graph Exporter

import json
import sys
from pathlib import Path

def load_json(path: Path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"[ERROR] Cannot load JSON: {e}")
        sys.exit(1)

def validate_graph(data: dict):
    if "nodes" not in data or "edges" not in data:
        print("[ERROR] JSON must contain 'nodes' and 'edges' fields.")
        sys.exit(1)

    if not isinstance(data["nodes"], list):
        print("[ERROR] 'nodes' must be a list.")
        sys.exit(1)

    if not isinstance(data["edges"], list):
        print("[ERROR] 'edges' must be a list.")
        sys.exit(1)

def export_dot(nodes, edges, output_path: Path):
    lines = ["digraph SUBIT64 {"]

    for n in nodes:
        lines.append(f'    "{n}"')

    for e in edges:
        src = e.get("from")
        dst = e.get("to")
        if src and dst:
            lines.append(f'    "{src}" -> "{dst}"')

    lines.append("}")

    try:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        print(f"[GENERATED] DOT graph saved to {output_path}")
    except Exception as e:
        print(f"[ERROR] Cannot write DOT file: {e}")
        sys.exit(1)

def export_adj_list(nodes, edges, output_path: Path):
    adj = {n: [] for n in nodes}

    for e in edges:
        src = e.get("from")
        dst = e.get("to")
        if src and dst:
            adj[src].append(dst)

    try:
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(adj, f, indent=4, ensure_ascii=False)
        print(f"[GENERATED] Adjacency list saved to {output_path}")
    except Exception as e:
        print(f"[ERROR] Cannot write adjacency list: {e}")
        sys.exit(1)

def export_edge_list(edges, output_path: Path):
    lines = ["from,to"]

    for e in edges:
        src = e.get("from")
        dst = e.get("to")
        if src and dst:
            lines.append(f"{src},{dst}")

    try:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        print(f"[GENERATED] Edge list saved to {output_path}")
    except Exception as e:
        print(f"[ERROR] Cannot write edge list: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) < 4:
        print("Usage: semantic-graph-exporter.py <graph.json> <format:dot|adj|edges> <output>")
        sys.exit(1)

    json_path = Path(sys.argv[1])
    fmt = sys.argv[2].lower()
    output_path = Path(sys.argv[3])

    data = load_json(json_path)
    validate_graph(data)

    nodes = data["nodes"]
    edges = data["edges"]

    if fmt == "dot":
        export_dot(nodes, edges, output_path)
    elif fmt == "adj":
        export_adj_list(nodes, edges, output_path)
    elif fmt == "edges":
        export_edge_list(edges, output_path)
    else:
        print(f"[ERROR] Unknown format '{fmt}'. Use: dot | adj | edges")
        sys.exit(1)

if __name__ == "__main__":
    main()
