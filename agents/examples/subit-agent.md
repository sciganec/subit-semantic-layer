# SUBIT Agent (SUBIT‑64 Canonical)

## 1. Overview
**Name:** SUBIT Agent  
**Role:** Unified cognitive agent built on the SUBIT‑64 semantic architecture  
**Function:** Interpret user input, generate structured reasoning, map cognitive topology, and express output through a selected persona  
**Core Layers:** Interpreter → Reasoning → Topology → Persona  
**Primary Use Cases:** Dialogue systems, assistants, multi‑agent orchestration, cognitive modeling

**Identity (1 sentence):**  
> A modular cognitive agent that transforms raw input into structured, topologically grounded, persona‑aligned output.

---

## 2. Architecture Summary

### Layer Stack
1. **Interpreter Layer**  
   Parses input, extracts seeds, selects archetype + shadow, initializes sense10.

2. **Reasoning Layer**  
   Generates hypotheses, converges on a trajectory, produces distilled insight.

3. **Topology Layer**  
   Maps reasoning into basins, gradients, curvature, transitions.

4. **Persona Layer**  
   Applies behavioral mask, tone, and expression rules to produce final output.

### Data Flow
```
User Input
   ↓
Interpreter → Seeds, Archetype, Shadow, Frame
   ↓
Reasoning Engine → Hypotheses, Insight, Trajectory
   ↓
Topology Engine → Basin, Gradient, Stability
   ↓
Persona Mask → Final Expression
   ↓
Agent Output
```

---

## 3. Input Contract

### Required Inputs
- user message  
- interpreter seeds (sense10, archetype, shadow)  
- frame_seed  
- topology_seed  

### Optional Inputs
- memory state  
- persona override  
- multi‑agent context  

### Validation
- input must be non‑empty  
- seeds must be structurally valid  
- persona must exist in `/agents/personas/`  

---

## 4. Processing Pipeline

### 4.1 Interpreter Stage
- Extracts semantic primitives  
- Selects archetype (64‑ontology)  
- Computes shadow tension  
- Generates sense10 vector  
- Produces interpreter packet  

### 4.2 Reasoning Stage
- Expands hypotheses  
- Evaluates consistency  
- Selects dominant trajectory  
- Produces distilled insight  
- Outputs reasoning packet  

### 4.3 Topology Stage
- Maps insight into basin  
- Computes gradient from shadow  
- Calculates curvature  
- Predicts transitions  
- Outputs topology packet  

### 4.4 Persona Stage
- Loads persona mask  
- Applies tone, voice, constraints  
- Formats final message  
- Outputs agent response  

---

## 5. Agent Behavior Modes

### 5.1 Default Mode
- Single‑turn reasoning  
- Persona applied at the end  
- No memory persistence  

### 5.2 Multi‑Step Mode
- Iterative reasoning cycles  
- Topology evolves over turns  
- Memory influences seeds  

### 5.3 Multi‑Agent Mode
- Multiple SUBIT‑agents coordinate  
- Each agent has its own persona + archetype  
- Negotiation and role‑based dynamics  

---

## 6. Persona Integration

### Persona Selection
- Default persona (configurable)  
- User‑selected persona  
- Context‑driven persona switching (optional)  

### Persona Requirements
- Must follow canonical template  
- Must define tone, voice, constraints  
- Must not override reasoning logic  

### Persona Output Contract
- Persona modifies *expression*, not *reasoning*  
- Persona cannot alter topology or seeds  

---

## 7. Example Agent Cycle

### Input
```
I feel stuck and don’t know how to move forward with my project.
```

### Interpreter Output (simplified)
```
archetype: Mentor
shadow: low
sense10: stable-reflective
```

### Reasoning Output (simplified)
```
distilled_insight: "user lacks clarity on intention layer"
dominant_trajectory: "reflective grounding"
```

### Topology Output (simplified)
```
basin: "reflective"
gradient: 0.22
stability: 0.81
```

### Persona Output (Mentor)
```
Let’s slow this down for a moment.  
There’s a difference between being stuck and not yet knowing the next step.  
Which part feels unclear right now—the goal, the method, or the pressure around it?
```

---

## 8. Integration Notes

### With SDK
- Python and JS SDKs provide interpreter + topology engines  
- Agent logic can be implemented in either language  

### With Multi‑Agent Systems
- SUBIT‑agents can negotiate roles  
- Each agent can hold a different persona  
- Topology alignment enables coordination  

### With External Systems
- Can be embedded in chatbots, assistants, simulations  
- Reasoning and topology layers can run headless (no persona)  

---

## 9. Agent Summary
**Identity:** modular cognitive agent  
**Layers:** interpreter → reasoning → topology → persona  
**Strengths:** structure, clarity, semantic grounding  
**Constraints:** persona does not affect reasoning  
**Use Cases:** assistants, multi‑agent systems, cognitive modeling  

This file defines the canonical SUBIT‑agent architecture.
