# ================================================================
# SUBIT-64 Topology Engine
# Canonical Python Implementation
# ================================================================
# This module implements the semantic topology layer:
#   1. Node construction
#   2. Edge construction
#   3. Gradient assignment
#   4. Basin placement
#   5. Transition potentials
#
# Input:  MIST packet + archetype + shadow
# Output: Semantic topology packet
# ================================================================

from dataclasses import dataclass, asdict
from typing import List, Dict, Any


# ================================================================
# 1. DATA STRUCTURES
# ================================================================

@dataclass
class Node:
    id: str
    type: str
    salience: float
    shadow_bias: float


@dataclass
class Edge:
    source: str
    target: str
    relation: str
    weight: float


@dataclass
class Gradients:
    relevance: float
    urgency: float
    emotional_charge: float
    risk: float
    ambiguity: float
    archetypal_pull: float


@dataclass
class TopologyPacket:
    nodes: List[Dict[str, Any]]
    edges: List[Dict[str, Any]]
    gradients: Dict[str, Any]
    basin: str
    transitions: Dict[str, Any]
    map: Dict[str, Any]


# ================================================================
# 2. NODE CONSTRUCTION
# ================================================================

def build_nodes(mist: Dict[str, Any], shadow: Dict[str, Any]) -> List[Node]:
    nodes = []
    extracted = mist.get("extracted", [])

    for i, item in enumerate(extracted):
        nodes.append(
            Node(
                id=f"n{i}",
                type=item.get("type", "concept"),
                salience=1.0,
                shadow_bias=shadow["intensity"]
            )
        )

    return nodes


# ================================================================
# 3. EDGE CONSTRUCTION
# ================================================================

def build_edges(mist: Dict[str, Any], nodes: List[Node]) -> List[Edge]:
    edges = []
    structure = mist.get("structure", {})

    # Example: causal chains, hierarchical links, etc.
    relations = structure.get("relations", [])

    for rel in relations:
        edges.append(
            Edge(
                source=f"n{rel['from']}",
                target=f"n{rel['to']}",
                relation=rel.get("type", "related"),
                weight=1.0
            )
        )

    return edges


# ================================================================
# 4. GRADIENT ASSIGNMENT
# ================================================================

def compute_gradients(mist: Dict[str, Any], shadow: Dict[str, Any]) -> Gradients:
    projections = mist.get("projections", [])
    emotional = mist.get("frame", "")

    return Gradients(
        relevance=len(projections) / 3,
        urgency=shadow["intensity"],
        emotional_charge=1.0 if "emotion" in emotional else 0.3,
        risk=shadow["distortion"].get("tension", 0.5),
        ambiguity=shadow["distortion"].get("clarity", 0.5),
        archetypal_pull=1.0 - shadow["intensity"]
    )


# ================================================================
# 5. BASIN PLACEMENT
# ================================================================

def determine_basin(archetype: Dict[str, Any], gradients: Gradients) -> str:
    # Basin = attractor region of archetype
    return archetype.get("attractor", "undefined")


# ================================================================
# 6. TRANSITION POTENTIALS
# ================================================================

def compute_transitions(archetype: Dict[str, Any], gradients: Gradients) -> Dict[str, Any]:
    # Simple model: high urgency or ambiguity increases transition probability
    return {
        "drift": gradients.ambiguity * 0.5,
        "shift": gradients.urgency * 0.7,
        "reform": gradients.risk * 0.9
    }


# ================================================================
# 7. FINAL TOPOLOGY MAP
# ================================================================

def build_map(nodes: List[Node], edges: List[Edge], gradients: Gradients) -> Dict[str, Any]:
    return {
        "node_count": len(nodes),
        "edge_count": len(edges),
        "gradient_strength": gradients.relevance + gradients.urgency,
        "structure_density": len(edges) / max(1, len(nodes))
    }


# ================================================================
# 8. MAIN ENGINE FUNCTION
# ================================================================

def build_topology(mist: Dict[str, Any], archetype: Dict[str, Any], shadow: Dict[str, Any]) -> TopologyPacket:
    nodes = build_nodes(mist, shadow)
    edges = build_edges(mist, nodes)
    gradients = compute_gradients(mist, shadow)
    basin = determine_basin(archetype, gradients)
    transitions = compute_transitions(archetype, gradients)
    topology_map = build_map(nodes, edges, gradients)

    return TopologyPacket(
        nodes=[asdict(n) for n in nodes],
        edges=[asdict(e) for e in edges],
        gradients=asdict(gradients),
        basin=basin,
        transitions=transitions,
        map=topology_map
    )


# ================================================================
# 9. CLI TEST
# ================================================================

if __name__ == "__main__":
    import json

    mist = {
        "frame": "analysis",
        "extracted": [{"type": "goal"}, {"type": "constraint"}],
        "structure": {"relations": [{"from": 0, "to": 1, "type": "causal"}]},
        "projections": ["path1", "path2"]
    }

    archetype = {
        "id": "000101",
        "name": "Strategist",
        "attractor": "optimization"
    }

    shadow = {
        "intensity": 0.3,
        "distortion": {"clarity": 0.7, "tension": 0.3},
        "emotional_bias": "neutral"
    }

    packet = build_topology(mist, archetype, shadow)
    print(json.dumps(asdict(packet), indent=2))
