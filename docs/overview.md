# SUBIT‑64 Overview
### A Semantic Architecture for Structured Cognitive Agents

SUBIT‑64 is a modular semantic architecture designed to transform raw user input into structured reasoning, topological mapping, and persona‑aligned expression.  
It provides a unified framework for building interpretable, multi‑layer cognitive agents.

---

# 1. What SUBIT‑64 Is

SUBIT‑64 is a **four‑layer cognitive stack**:

1. **Interpreter Layer**  
   Extracts semantic primitives, selects archetype and shadow, initializes seeds.

2. **Reasoning Layer**  
   Generates hypotheses, converges on a trajectory, produces distilled insight.

3. **Topology Layer**  
   Maps reasoning into basins, gradients, curvature, and transitions.

4. **Persona Layer**  
   Applies tone, voice, and behavioral constraints to produce final expression.

Each layer is independent, composable, and fully documented in the `/spec/` directory.

---

# 2. Core Principles

### 2.1 Modularity  
Each layer is a standalone module with a clear input/output contract.

### 2.2 Interpretability  
Every transformation is explicit: seeds → reasoning → topology → persona.

### 2.3 Archetypal Semantics  
The system uses a 64‑element archetypal ontology to shape cognitive modes.

### 2.4 Topological Reasoning  
Cognition is represented as movement through semantic basins and gradients.

### 2.5 Persona Separation  
Reasoning is neutral; persona affects only expression, not cognition.

---

# 3. High‑Level Data Flow

```
User Input
   ↓
Interpreter Layer
   ↓
Reasoning Layer
   ↓
Topology Layer
   ↓
Persona Layer
   ↓
Agent Output
```

Each stage enriches the cognitive state without overwriting previous layers.

---

# 4. Components of the Architecture

### 4.1 Interpreter  
Located in `/interpreter/`.  
Responsible for:
- archetype selection  
- shadow computation  
- sense10 vector  
- frame and topology seeds  

### 4.2 Reasoning  
Located in `/spec/mist-layer.md` and `/sdk/python/`.  
Implements:
- hypothesis expansion  
- convergence  
- distilled insight  

### 4.3 Topology  
Located in `/spec/content-topology.md` and `/sdk/python/`.  
Provides:
- basin mapping  
- gradient computation  
- curvature analysis  
- transition prediction  

### 4.4 Personas  
Located in `/agents/personas/`.  
Define:
- tone  
- voice  
- behavioral constraints  
- expression rules  

---

# 5. Agent Model

A SUBIT‑agent is a composition of:

- interpreter  
- reasoning engine  
- topology engine  
- persona mask  

Agents can operate in:
- single‑turn mode  
- multi‑step mode  
- multi‑agent mode  

Examples are in `/agents/examples/`.

---

# 6. SDKs

SUBIT‑64 provides two SDKs:

### Python SDK (`/sdk/python/`)
- interpreter  
- topology engine  
- archetype selector  
- example agents  

### JavaScript SDK (`/sdk/js/`)
- interpreter  
- example agents  

Both SDKs follow the same architecture and data contracts.

---

# 7. Specification and Theory

The `/spec/` directory contains the canonical definitions:

- archetypal ontology  
- shadow axes  
- MIST reasoning layer  
- content topology  
- behavioral masks  
- integration principles  

The `/whitepaper/` directory provides the theoretical foundation and diagrams.

---

# 8. Tools and Utilities

Located in `/tools/`:

- validators (archetype, topology)  
- generators (persona, topology)  
- visualization utilities  
- semantic graph exporter  

These tools support development, debugging, and analysis.

---

# 9. Intended Use Cases

SUBIT‑64 is designed for:

- cognitive agents  
- multi‑agent systems  
- assistants and copilots  
- simulations and reasoning engines  
- research in semantic architectures  

It is not tied to any specific model or platform.

---

# 10. Summary

SUBIT‑64 provides:

- a clear semantic foundation  
- a modular cognitive pipeline  
- interpretable reasoning  
- topological mapping  
- persona‑aligned expression  

It is a complete architecture for building structured, transparent, and extensible cognitive agents.

