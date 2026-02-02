# Reasoning Template (SUBIT‑64 Canonical)
### Universal Specification for Defining a Reasoning Module

This template defines a complete reasoning engine compatible with the SUBIT‑64 architecture.  
A reasoning module transforms *semantic initialization* into *structured cognitive output*.

---

# 1. Module Overview

**Name:**  
**Purpose:**  
**Reasoning Paradigm:** (analytical / generative / topological / hybrid)  
**Primary Inputs:**  
**Primary Outputs:**  
**Dependencies:** (interpreter, topology, memory, etc.)

**One‑sentence identity:**  
> A concise description of what this reasoning module does.

---

# 2. Input Contract

### 2.1 Required Inputs
- sense10  
- archetype  
- shadow  
- frame_seed  
- topology_seed  
- user query  

### 2.2 Optional Inputs
- memory state  
- previous reasoning steps  
- persona mask  
- external context  

### 2.3 Input Validation Rules
- what must be present  
- what must be normalized  
- what must be rejected  

---

# 3. Reasoning Stages

Describe the internal pipeline of the reasoning module.

### 3.1 Stage A — Initialization
- how the module reads seeds  
- how it sets internal variables  
- how it resolves ambiguity  

### 3.2 Stage B — Expansion
- how it generates hypotheses  
- how it explores the problem space  
- how it handles branching  

### 3.3 Stage C — Convergence
- how it selects the dominant trajectory  
- how it resolves conflicts  
- how it compresses reasoning  

### 3.4 Stage D — Output Structuring
- how the final reasoning packet is formed  
- what fields it contains  
- how it is passed to the next module  

---

# 4. Reasoning Logic

### 4.1 Core Algorithm
Describe the algorithmic logic:
- deterministic rules  
- probabilistic rules  
- topological rules  
- archetypal influences  

### 4.2 Heuristics
List heuristics used for:
- prioritization  
- simplification  
- conflict resolution  
- pattern detection  

### 4.3 Constraints
Define what the module must not do:
- no hallucination  
- no persona‑style output  
- no formatting decisions  

---

# 5. Internal Representations

### 5.1 Data Structures
Define internal structures:
- nodes  
- edges  
- frames  
- gradients  
- vectors  

### 5.2 State Variables
List persistent or temporary variables:
- active trajectory  
- confidence weights  
- semantic anchors  

### 5.3 Transition Rules
Describe how the module moves between states:
- triggers  
- thresholds  
- fallback paths  

---

# 6. Output Contract

### 6.1 Required Fields
- reasoning_steps  
- dominant_trajectory  
- distilled_insight  
- structural_map  
- confidence  

### 6.2 Optional Fields
- alternative paths  
- unresolved tensions  
- meta‑notes  

### 6.3 Output Format
Define the structure:
- JSON‑like packet  
- no persona style  
- no final expression  
- pure reasoning  

---

# 7. Example Outputs

### 7.1 Example (Neutral Query)
```
<reasoning-output example>
```

### 7.2 Example (Ambiguous Query)
```
<reasoning-output example>
```

### 7.3 Example (Complex Multi‑Layer Query)
```
<reasoning-output example>
```

---

# 8. Integration Notes

### 8.1 With SUBIT‑Interpreter
- consumes archetype, shadow, seeds  
- does not modify them  

### 8.2 With Topology Engine
- may generate gradients  
- may request basin information  

### 8.3 With Persona Mask
- persona is applied after reasoning  
- reasoning remains neutral  

### 8.4 With Memory Layer
- may read memory  
- must not write memory  

---

# 9. Module Summary (Canonical)

**Identity:**  
**Purpose:**  
**Inputs:**  
**Outputs:**  
**Stages:**  
**Heuristics:**  
**Constraints:**  
**Integration:**  

This summary is used for quick loading.
