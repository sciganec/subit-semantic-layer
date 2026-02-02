# REASONING PACK PRO (SUBIT‑64 Canonical)
High‑fidelity reasoning modules with real reasoning outputs.

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

### 7.1 Neutral Query
```
reasoning_steps:
  - identified core intent: "optimize workflow"
  - generated hypotheses: {reduce switching, batch tasks, clarify priorities}
  - evaluated tension: low ambiguity, medium urgency
  - selected dominant hypothesis: "reduce switching"
distilled_insight: "workflow inefficiency is primarily caused by context switching"
confidence: 0.82
```

### 7.2 Ambiguous Query
```
reasoning_steps:
  - detected ambiguity in user intent
  - generated hypotheses: {seeking clarity, seeking validation, exploring options}
  - shadow tension elevated → ambiguity weighting increased
  - selected dominant hypothesis: "seeking clarity"
distilled_insight: "the query lacks explicit direction and requires clarification"
confidence: 0.61
```

### 7.3 Complex Multi-Layer Query
```
reasoning_steps:
  - decomposed query into layers: strategic, emotional, operational
  - generated hypotheses for each layer
  - cross-evaluated for consistency
  - selected dominant trajectory: "strategic restructuring"
distilled_insight: "the core issue is misalignment between goals and constraints"
confidence: 0.77
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

### 7.1 Neutral Query
```
structural_map:
  basin: "strategic-order"
  gradient: 0.34
  direction: "toward optimization"
transition_prediction: "remains in same basin unless urgency increases"
```

### 7.2 Ambiguous Query
```
structural_map:
  basin: "uncertainty"
  gradient: 0.58
  direction: "toward clarification"
transition_prediction: "likely shift to analytical basin after disambiguation"
```

### 7.3 Complex Multi-Layer Query
```
structural_map:
  basin: "mixed"
  gradient: 0.71
  direction: "toward restructuring"
transition_prediction: "high probability of transition to strategic basin"
```

============================================================
# 3. Planner-Reasoner
============================================================

## 7. Example Outputs

### 7.1 Neutral Query
```
plan_steps:
  - extract goal: "launch project"
  - identify constraints: time, resources
  - decompose into phases: planning, execution, review
dependencies: {execution depends on planning}
```

### 7.2 Ambiguous Query
```
plan_steps:
  - detected unclear goal
  - generated provisional steps: clarify → define → plan
dependencies: {planning blocked until goal clarified}
```

### 7.3 Complex Multi-Layer Query
```
plan_steps:
  - extracted multi-layer goal: strategic + operational
  - decomposed into 7 steps
  - optimized sequence to reduce bottlenecks
dependencies: {steps 4–7 depend on step 3}
```

============================================================
# 4. Evaluator-Reasoner
============================================================

## 7. Example Outputs

### 7.1 Neutral Query
```
strengths: {clear objective, feasible scope}
weaknesses: {missing timeline}
risks: {resource shortage}
viability_score: 0.74
```

### 7.2 Ambiguous Query
```
strengths: {flexibility}
weaknesses: {undefined success criteria}
risks: {misalignment}
viability_score: 0.42
```

### 7.3 Complex Multi-Layer Query
```
strengths: {strategic coherence}
weaknesses: {operational overload}
risks: {timeline compression}
viability_score: 0.63
```

============================================================
# 5. Synthesis-Reasoner
============================================================

## 7. Example Outputs

### 7.1 Neutral Query
```
synthesis_map:
  elements: {idea A, idea B}
  relationship: "complementary"
unified_concept: "combined model with shared constraints"
```

### 7.2 Ambiguous Query
```
synthesis_map:
  elements: {fragmented inputs}
  relationship: "unclear"
unified_concept: "requires clarification before integration"
```

### 7.3 Complex Multi-Layer Query
```
synthesis_map:
  elements: {strategic, emotional, operational}
  relationship: "layered"
unified_concept: "multi-axis integration model"
```

============================================================
# 6. Trajectory-Reasoner
============================================================

## 7. Example Outputs

### 7.1 Neutral Query
```
trajectory_map:
  history_pattern: "stable analytical mode"
  projected_direction: "toward optimization"
next_steps: {refine constraints, increase clarity}
```

### 7.2 Ambiguous Query
```
trajectory_map:
  history_pattern: "oscillation between modes"
  projected_direction: "toward stabilization"
next_steps: {clarify intent, reduce ambiguity}
```

### 7.3 Complex Multi-Layer Query
```
trajectory_map:
  history_pattern: "multi-vector drift"
  projected_direction: "toward strategic consolidation"
next_steps: {align goals, reduce noise, reinforce core vector}
```

