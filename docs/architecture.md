# SUBIT‑64 Architecture
### Canonical Technical Overview of the Semantic Cognitive Stack

SUBIT‑64 is a modular semantic architecture for building interpretable cognitive agents.  
It defines a four‑layer processing pipeline — Interpreter → Reasoning → Topology → Persona — each with explicit contracts, seeds, and transformation rules.

This document describes the architecture at the system level.

---

# 1. Architectural Summary

SUBIT‑64 is built on four independent but composable layers:

1. **Interpreter Layer**  
   Extracts semantic primitives, selects archetype and shadow, initializes seeds.

2. **Reasoning Layer (MIST)**  
   Generates hypotheses, converges on a trajectory, produces distilled insight.

3. **Topology Layer**  
   Maps reasoning into basins, gradients, curvature, and transitions.

4. **Persona Layer**  
   Applies tone, voice, and behavioral constraints to produce final expression.

Each layer receives a structured packet and outputs a new one, forming a deterministic cognitive chain.

---

# 2. High‑Level Data Flow

```
User Input
   ↓
Interpreter Layer
   ↓
Reasoning Layer (MIST)
   ↓
Topology Layer
   ↓
Persona Layer
   ↓
Agent Output
```

Each stage enriches the cognitive state without overwriting previous layers.

---

# 3. Layer 1 — Interpreter

### Purpose
Transform raw text into structured semantic seeds.

### Responsibilities
- Archetype selection (64‑ontology)
- Shadow computation (tension axis)
- Sense10 vector generation
- Frame seed initialization
- Topology seed initialization

### Output Packet
```
{
  archetype,
  shadow,
  sense10,
  frame_seed,
  topology_seed
}
```

### Notes
The interpreter does not perform reasoning — it prepares the substrate for reasoning.

---

# 4. Layer 2 — Reasoning (MIST)

### Purpose
Generate structured cognitive insight from seeds.

### Responsibilities
- Hypothesis expansion
- Consistency evaluation
- Trajectory convergence
- Distilled insight generation

### Output Packet
```
{
  reasoning_steps,
  dominant_trajectory,
  distilled_insight,
  confidence
}
```

### Notes
Reasoning is **neutral** — no persona influence, no stylistic decisions.

---

# 5. Layer 3 — Topology

### Purpose
Map reasoning into spatial semantic structure.

### Responsibilities
- Basin identification
- Gradient computation (from shadow)
- Curvature analysis
- Transition prediction
- Stability evaluation

### Output Packet
```
{
  basin,
  gradient,
  curvature,
  transition,
  stability
}
```

### Notes
Topology provides a geometric representation of cognition.

---

# 6. Layer 4 — Persona

### Purpose
Transform neutral reasoning into expressive output.

### Responsibilities
- Tone, voice, pacing
- Behavioral constraints
- Expression formatting
- Style enforcement

### Output Packet
```
{
  final_message
}
```

### Notes
Persona **never** modifies reasoning or topology — only expression.

---

# 7. Cross‑Layer Principles

### 7.1 Modularity
Each layer is replaceable and independently testable.

### 7.2 Deterministic Contracts
Every layer has a strict input/output schema.

### 7.3 Archetypal Semantics
Archetype + shadow define cognitive mode and tension.

### 7.4 Topological Continuity
Reasoning trajectories map to basins and gradients.

### 7.5 Persona Separation
Expression is decoupled from cognition.

---

# 8. System Components

### 8.1 Interpreter Engine  
Located in `/interpreter/`.

### 8.2 Reasoning Engines  
Located in `/spec/mist-layer.md` and `/sdk/python/`.

### 8.3 Topology Engines  
Located in `/spec/content-topology.md` and `/sdk/python/`.

### 8.4 Personas  
Located in `/agents/personas/`.

### 8.5 Tools  
Located in `/tools/` (validators, generators, visualizers).

---

# 9. Multi‑Agent Architecture

SUBIT‑64 supports multi‑agent systems:

- Each agent has its own archetype + persona  
- Agents coordinate through topology alignment  
- Negotiation and role systems are defined in `/agents/multi-agent/`

Multi‑agent dynamics rely on **basin compatibility** and **trajectory alignment**.

---

# 10. Implementation Notes

### Language‑Agnostic
The architecture is defined in `/spec/` and implemented in:

- Python SDK (`/sdk/python/`)
- JavaScript SDK (`/sdk/js/`)

### Extensibility
Developers can add:
- new personas  
- new reasoning modules  
- new topology modules  
- custom interpreters  

### Testing
Unit tests live in `/tests/`.

---

# 11. Summary

SUBIT‑64 provides:

- a modular cognitive pipeline  
- interpretable reasoning  
- topological mapping  
- persona‑aligned expression  
- multi‑agent extensibility  

It is a complete architecture for building structured, transparent, and extensible cognitive agents.

