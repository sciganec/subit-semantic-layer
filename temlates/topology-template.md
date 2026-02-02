# Topology Template (SUBIT‑64 Canonical)
### Universal Specification for Defining a Topological Reasoning Module

This template defines a complete topological engine compatible with the SUBIT‑64 architecture.  
A topology module transforms *cognitive trajectories* into *spatial semantic structures*.

---

# 1. Module Overview

**Name:**  
**Purpose:**  
**Topological Paradigm:** (basins / gradients / attractors / transitions)  
**Primary Inputs:**  
**Primary Outputs:**  
**Dependencies:** (MIST, interpreter, memory, etc.)

**One‑sentence identity:**  
> A concise description of what this topology module maps or predicts.

---

# 2. Input Contract

### 2.1 Required Inputs
- archetype  
- shadow  
- mist_packet  
- topology_seed  

### 2.2 Optional Inputs
- memory state  
- previous topology states  

### 2.3 Input Validation Rules
- topology_seed must contain basin + gradient  
- mist_packet must contain distilled insight  
- archetype must define attractor type  

---

# 3. Topological Stages

Describe the internal pipeline of the topology module.

### 3.1 Stage A — Basin Identification
- determine attractor basin  
- map archetype to basin type  
- initialize basin parameters  

### 3.2 Stage B — Gradient Computation
- compute slope from shadow intensity  
- compute direction from mist trajectory  
- normalize gradient  

### 3.3 Stage C — Field Construction
- build semantic field  
- define local curvature  
- identify stable and unstable regions  

### 3.4 Stage D — Transition Prediction
- estimate next basin  
- compute transition probability  
- detect bifurcation points  

### 3.5 Stage E — Output Structuring
- assemble structural map  
- compress into canonical topology packet  

---

# 4. Topological Logic

### 4.1 Core Algorithm
Describe the algorithmic logic:
- basin selection rules  
- gradient propagation  
- attractor dynamics  
- transition thresholds  

### 4.2 Heuristics
List heuristics used for:
- smoothing gradients  
- resolving conflicting signals  
- stabilizing noisy trajectories  

### 4.3 Constraints
Define what the module must not do:
- no persona style  
- no final expression  
- no emotional coloration  
- no formatting decisions  

---

# 5. Internal Representations

### 5.1 Data Structures
Define internal structures:
- basins  
- gradients  
- fields  
- attractors  
- transition matrices  

### 5.2 State Variables
List persistent or temporary variables:
- current_basin  
- gradient_vector  
- field_map  
- transition_score  

### 5.3 Transition Rules
Describe how the module moves between states:
- triggers  
- thresholds  
- fallback basins  

---

# 6. Output Contract

### 6.1 Required Fields
- structural_map  
- basin  
- gradient  
- predicted_transition  
- confidence  

### 6.2 Optional Fields
- alternative transitions  
- unresolved tensions  
- meta‑notes  

### 6.3 Output Format
Define the structure:
- JSON‑like packet  
- pure topology  
- no persona style  

---

# 7. Example Outputs

### 7.1 Example (Neutral Query)
```
<topology-output example>
```

### 7.2 Example (Ambiguous Query)
```
<topology-output example>
```

### 7.3 Example (Complex Multi‑Layer Query)
```
<topology-output example>
```

---

# 8. Integration Notes

### 8.1 With MIST
- consumes distilled insight  
- uses trajectory direction  

### 8.2 With Interpreter
- uses archetype to determine basin  
- uses shadow to compute gradient  

### 8.3 With Persona Mask
- persona is applied after topology  
- topology remains neutral  

### 8.4 With Memory Layer
- may read historical basins  
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
