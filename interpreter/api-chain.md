# SUBIT‑64 API Chain  
### Canonical Specification of the Modular Semantic Pipeline  
### (Machine‑Readable Integration Layer)

The SUBIT‑64 API Chain defines the **machine‑level interface** for executing the full semantic pipeline.  
Each layer is a deterministic module with a defined input and output schema.  
Together they form a **semantic transformation chain**.

---

# 1. Purpose of the API Chain

The API Chain provides:

- modular integration  
- deterministic execution  
- machine‑readable interfaces  
- predictable semantic transformations  
- compatibility with any LLM or symbolic engine  
- clean separation of cognition and expression  

It is the **operational backbone** of SUBIT‑64.

---

# 2. Canonical Pipeline Overview

The API Chain consists of **eight modules**, executed in strict order:

```
1. SENSE‑10
2. SUBIT‑6
3. Codon Generator (6‑bit)
4. SUBIT‑64 Archetype Selector
5. Shadow Modulator
6. MIST Reasoning Engine
7. Topology Mapper
8. Behavioral Mask
```

Each module receives a JSON packet and returns a JSON packet.

---

# 3. Module 1 — SENSE‑10 Encoder

### **Input**
```
{
  "text": "<user_input>"
}
```

### **Output**
```
{
  "sense10": {
    "intent": ...,
    "tone": ...,
    "urgency": ...,
    "complexity": ...,
    "ambiguity": ...,
    "relation": ...,
    "temporal": ...,
    "risk": ...,
    "domain": ...,
    "mode": ...
  }
}
```

SENSE‑10 is the **subjective signature** of the input.

---

# 4. Module 2 — SUBIT‑6 Axis Reducer

### **Input**
```
{
  "sense10": {...}
}
```

### **Output**
```
{
  "axes": {
    "b1": 0|1,
    "b2": 0|1,
    "b3": 0|1,
    "b4": 0|1,
    "b5": 0|1,
    "b6": 0|1
  }
}
```

SUBIT‑6 reduces SENSE‑10 to six binary semantic axes.

---

# 5. Module 3 — Codon Generator (6‑bit)

### **Input**
```
{
  "axes": {...}
}
```

### **Output**
```
{
  "codon": "b1b2b3b4b5b6"
}
```

The codon uniquely identifies one of the 64 archetypes.

---

# 6. Module 4 — SUBIT‑64 Archetype Selector

### **Input**
```
{
  "codon": "000101"
}
```

### **Output**
```
{
  "archetype": {
    "id": "000101",
    "name": "Strategist",
    "cognitive_mode": "...",
    "behavioral_mode": "...",
    "attractor": "..."
  }
}
```

This module assigns the **semantic identity** of the input.

---

# 7. Module 5 — Shadow Modulator

### **Input**
```
{
  "archetype": {...},
  "sense10": {...}
}
```

### **Output**
```
{
  "shadow": {
    "intensity": 0–1,
    "distortion": {...},
    "emotional_bias": ...
  }
}
```

Shadow introduces depth, tension, and asymmetry.

---

# 8. Module 6 — MIST Reasoning Engine

### **Input**
```
{
  "archetype": {...},
  "shadow": {...},
  "sense10": {...}
}
```

### **Output**
```
{
  "mist": {
    "frame": "...",
    "extracted": [...],
    "structure": {...},
    "interpretation": "...",
    "projections": [...],
    "consolidated": {...}
  }
}
```

MIST produces structured cognition.

---

# 9. Module 7 — Topology Mapper

### **Input**
```
{
  "mist": {...},
  "archetype": {...},
  "shadow": {...}
}
```

### **Output**
```
{
  "topology": {
    "nodes": [...],
    "edges": [...],
    "gradients": {...},
    "basin": "...",
    "transitions": {...},
    "map": {...}
  }
}
```

The mapper spatializes meaning into the semantic manifold.

---

# 10. Module 8 — Behavioral Mask

### **Input**
```
{
  "topology": {...},
  "archetype": {...},
  "shadow": {...}
}
```

### **Output**
```
{
  "expression": {
    "persona": "...",
    "tone": "...",
    "constraints": [...],
    "style": "...",
    "final_output": "<text>"
  }
}
```

Masks shape expression, not cognition.

---

# 11. Full API Chain Example

```
Input: "Help me plan a project."

1. SENSE‑10 → analytical, medium urgency
2. SUBIT‑6 → 000101
3. Codon → 000101
4. Archetype → Strategist
5. Shadow → low
6. MIST → dependency graph + 3 trajectories
7. Topology → planning basin, optimization gradient
8. Mask → Mentor (supportive strategist)

Output:
"Here is a structured plan with three viable paths..."
```

---

# 12. Canonical Summary

The SUBIT‑64 API Chain defines the **machine‑readable pipeline** for semantic cognition.  
Each module is deterministic, modular, and interoperable.  
Together they form a complete semantic transformation chain from raw input to final expression.

