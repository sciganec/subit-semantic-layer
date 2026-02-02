# REASONING PACK (SUBIT‑64 Canonical)
A compact collection of reasoning modules for SUBIT agents.

============================================================
# 1. MIST-Reasoner
============================================================

## 1. Module Overview
**Name:** MIST-Reasoner  
**Purpose:** Transform semantic seeds into structured cognitive trajectories  
**Reasoning Paradigm:** Hybrid (analytical + generative)  
**Primary Inputs:** sense10, archetype, shadow, frame_seed  
**Primary Outputs:** reasoning_steps, distilled_insight  
**Dependencies:** SUBIT-Interpreter  

**One-sentence identity:**  
> A core reasoning engine that expands and compresses meaning into a coherent trajectory.

---

## 2. Input Contract
### Required Inputs
- sense10  
- archetype  
- shadow  
- frame_seed  
- user query  

### Optional Inputs
- memory state  

### Validation
- frame_seed must be non-empty  
- sense10 must contain 10 fields  

---

## 3. Reasoning Stages
### Stage A — Initialization
Normalize seeds, set cognitive anchors.

### Stage B — Expansion
Generate 3–5 hypotheses based on archetype mode.

### Stage C — Convergence
Select dominant hypothesis using shadow tension.

### Stage D — Structuring
Compress into a single distilled insight.

---

## 4. Reasoning Logic
### Core Algorithm
- archetype defines mode  
- shadow defines tension  
- sense10 defines direction  

### Heuristics
- prefer simplest consistent hypothesis  
- discard contradictions  

### Constraints
- no persona style  
- no emotional coloration  

---

## 5. Internal Representations
- hypothesis list  
- tension weights  
- convergence score  

---

## 6. Output Contract
- reasoning_steps  
- dominant_trajectory  
- distilled_insight  
- confidence  

---

## 7. Example Outputs
```
<reasoning-output example>
```

---

## 8. Integration Notes
Feeds directly into topology engine.

---

## 9. Module Summary
Identity: core cognitive engine  
Purpose: hypothesis generation + convergence  
Inputs: seeds  
Outputs: insight  


============================================================
# 2. Topological-Reasoner
============================================================

## 1. Module Overview
**Name:** Topological-Reasoner  
**Purpose:** Map reasoning into basins, gradients, and transitions  
**Reasoning Paradigm:** Topological  
**Primary Inputs:** topology_seed, mist_packet  
**Primary Outputs:** structural_map, gradient_vector  
**Dependencies:** MIST  

**One-sentence identity:**  
> A mapper that transforms cognition into spatial semantic structure.

---

## 3. Reasoning Stages
### Stage A — Basin Identification
Determine attractor basin from archetype.

### Stage B — Gradient Mapping
Compute tension-based slope.

### Stage C — Transition Prediction
Estimate likely next basin.

### Stage D — Structural Output
Produce semantic map.

---

## 4. Reasoning Logic
- archetype → basin  
- shadow → gradient  
- mist → direction  

---

## 6. Output Contract
- structural_map  
- gradient_vector  
- transition_prediction  

---

## 7. Example Outputs
```
<reasoning-output example>
```

============================================================
# 3. Planner-Reasoner
============================================================

## 1. Module Overview
**Name:** Planner-Reasoner  
**Purpose:** Decompose tasks into steps  
**Reasoning Paradigm:** Analytical / Executive  
**Primary Inputs:** user query, mist_packet  
**Primary Outputs:** plan_steps, dependencies  
**Dependencies:** MIST  

**One-sentence identity:**  
> A sequencing engine that converts goals into ordered action paths.

---

## 3. Reasoning Stages
### Stage A — Goal Extraction
Identify explicit and implicit goals.

### Stage B — Constraint Mapping
Identify limits, resources, blockers.

### Stage C — Decomposition
Break into 3–7 steps.

### Stage D — Optimization
Reorder for efficiency.

---

## 4. Reasoning Logic
- prefer minimal dependency chains  
- avoid redundant steps  

---

## 6. Output Contract
- plan_steps  
- constraints  
- dependencies  

---

## 7. Example Outputs
```
<reasoning-output example>
```

============================================================
# 4. Evaluator-Reasoner
============================================================

## 1. Module Overview
**Name:** Evaluator-Reasoner  
**Purpose:** Assess quality, risk, and viability  
**Reasoning Paradigm:** Analytical  
**Primary Inputs:** user proposal, mist_packet  
**Primary Outputs:** evaluation, risks, strengths  
**Dependencies:** MIST  

**One-sentence identity:**  
> A critical engine that stress-tests ideas.

---

## 3. Reasoning Stages
### Stage A — Criteria Extraction
Define evaluation metrics.

### Stage B — Strength Analysis
Identify strong components.

### Stage C — Weakness Analysis
Identify vulnerabilities.

### Stage D — Risk Projection
Estimate failure modes.

---

## 4. Reasoning Logic
- use archetype to define evaluation lens  
- use shadow to detect blind spots  

---

## 6. Output Contract
- strengths  
- weaknesses  
- risks  
- viability_score  

---

## 7. Example Outputs
```
<reasoning-output example>
```

============================================================
# 5. Synthesis-Reasoner
============================================================

## 1. Module Overview
**Name:** Synthesis-Reasoner  
**Purpose:** Integrate multiple ideas into a coherent whole  
**Reasoning Paradigm:** Integrative  
**Primary Inputs:** multiple user inputs, mist_packet  
**Primary Outputs:** synthesis_map, unified_concept  
**Dependencies:** MIST  

**One-sentence identity:**  
> A conceptual weaver that binds disparate elements into a unified structure.

---

## 3. Reasoning Stages
### Stage A — Element Extraction
Identify all conceptual components.

### Stage B — Relationship Mapping
Find overlaps, tensions, bridges.

### Stage C — Integration
Merge into a single coherent structure.

### Stage D — Compression
Produce a unified concept.

---

## 4. Reasoning Logic
- prefer minimal spanning structure  
- avoid forced symmetry  

---

## 6. Output Contract
- synthesis_map  
- unified_concept  

---

## 7. Example Outputs
```
<reasoning-output example>
```

============================================================
# 6. Trajectory-Reasoner
============================================================

## 1. Module Overview
**Name:** Trajectory-Reasoner  
**Purpose:** Build long-term cognitive trajectories  
**Reasoning Paradigm:** Sequential / Predictive  
**Primary Inputs:** history, mist_packet  
**Primary Outputs:** trajectory_map, next_steps  
**Dependencies:** Memory Layer  

**One-sentence identity:**  
> A long-horizon engine that predicts and shapes cognitive evolution.

---

## 3. Reasoning Stages
### Stage A — History Analysis
Extract patterns from previous steps.

### Stage B — Vector Projection
Predict future cognitive direction.

### Stage C — Trajectory Construction
Build multi-step path.

### Stage D — Stabilization
Remove noise, keep core vector.

---

## 4. Reasoning Logic
- use memory to detect trends  
- use shadow to detect instability  

---

## 6. Output Contract
- trajectory_map  
- predicted_direction  
- next_steps  

---

## 7. Example Outputs
```
<reasoning-output example>
```

