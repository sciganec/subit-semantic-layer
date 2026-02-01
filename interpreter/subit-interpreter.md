# SUBIT Interpreter  
### Canonical Specification of the SUBIT‑64 Semantic Interpreter

The SUBIT Interpreter is the component that transforms raw user input into a complete SUBIT‑64 semantic configuration.  
It is the **entry point** of the SUBIT‑64 architecture and the **semantic decoder** for all downstream layers.

The interpreter converts natural language into:

- SENSE‑10 vector  
- SUBIT‑6 axis configuration  
- 6‑bit codon  
- SUBIT‑64 archetype  
- shadow vector  
- MIST frame seed  
- topological initialization packet  

---

# 1. Purpose of the Interpreter

The SUBIT Interpreter provides:

- deterministic semantic decoding  
- stable archetype selection  
- consistent axis reduction  
- contextual shadow modulation  
- initialization of reasoning and topology  
- a unified interface for all SUBIT‑64 layers  

It is the **semantic front‑end** of the system.

---

# 2. Interpreter Pipeline

The interpreter performs a six‑stage transformation:

```
Input → SENSE‑10 → SUBIT‑6 → 6‑bit Codon → SUBIT‑64 → Shadow → Interpreter Output
```

Each stage is deterministic and modular.

---

# 3. Stage 1 — SENSE‑10 Encoding

The interpreter extracts a **10‑dimensional subjective vector**:

1. intent  
2. emotional tone  
3. urgency  
4. complexity  
5. ambiguity  
6. relational stance  
7. temporal orientation  
8. risk level  
9. domain specificity  
10. cognitive mode  

SENSE‑10 is the **subjective signature** of the input.

---

# 4. Stage 2 — SUBIT‑6 Axis Reduction

SENSE‑10 is reduced to six binary axes:

| Axis | 0‑Pole | 1‑Pole |
|------|--------|--------|
| Order / Chaos | Order | Chaos |
| Self / Other | Self | Other |
| Abstract / Concrete | Abstract | Concrete |
| Active / Passive | Active | Passive |
| Inner / Outer | Inner | Outer |
| Flow / Structure | Flow | Structure |

The result is a **6‑bit semantic codon**.

---

# 5. Stage 3 — 6‑bit Codon Generation

The interpreter computes:

```
Codon = b1 b2 b3 b4 b5 b6
```

Each bit is derived from axis polarity.  
This codon uniquely identifies one of the **64 archetypes**.

---

# 6. Stage 4 — SUBIT‑64 Archetype Selection

The codon maps to a canonical archetype:

- cognitive stance  
- behavioral mode  
- attractor pattern  
- reasoning constraints  

The archetype defines the **semantic identity** of the input.

---

# 7. Stage 5 — Shadow Vector Computation

Shadow modulation introduces:

- depth  
- tension  
- asymmetry  
- emotional resonance  
- contextual distortion  

Shadow is computed from:

- SENSE‑10  
- ambiguity  
- emotional tone  
- relational stance  
- risk  
- cognitive load  

Shadow does **not** change the archetype — it modulates it.

---

# 8. Stage 6 — Interpreter Output Packet

The interpreter outputs a **semantic initialization packet**:

```
{
  archetype: <SUBIT‑64 state>,
  codon: <6‑bit>,
  axes: <SUBIT‑6>,
  sense: <SENSE‑10>,
  shadow: <shadow vector>,
  frame_seed: <MIST initialization>,
  topology_seed: <basin + gradient initialization>
}
```

This packet is consumed by:

- MIST  
- Topology  
- Mask  

---

# 9. Interpreter Guarantees

The SUBIT Interpreter guarantees:

### **9.1 Determinism**
Same input → same semantic configuration.

### **9.2 Stability**
Archetype selection is stable across turns unless context changes.

### **9.3 Transparency**
All internal states are inspectable.

### **9.4 Modularity**
Interpreter output is compatible with any downstream module.

### **9.5 Safety**
Shadow modulation is bounded and cannot override archetype constraints.

---

# 10. Interpreter–MIST Interface

The interpreter provides MIST with:

- frame seed  
- extracted tensions  
- initial semantic primitives  
- archetype constraints  
- shadow modulation parameters  

MIST then performs structured reasoning.

---

# 11. Interpreter–Topology Interface

The interpreter provides topology with:

- initial basin placement  
- gradient seeds  
- node prototypes  
- relational hints  

Topology then constructs the semantic manifold.

---

# 12. Interpreter–Mask Interface

Masks receive:

- archetype  
- shadow  
- stance  
- relational cues  

Masks shape **expression**, not cognition.

---

# 13. Canonical Example

```
Input: "I need help deciding between two options."

SENSE‑10:
  intent: decision
  tone: neutral
  urgency: medium
  complexity: moderate
  ambiguity: low
  relational: self
  temporal: present
  risk: medium
  domain: general
  mode: analytical

SUBIT‑6:
  Order, Self, Abstract, Active, Inner, Structure
  → 000100

Codon: 000100  
Archetype: The Initiator  
Shadow: low  
Frame Seed: activation under constraint  
Topology Seed: decision basin, branching gradient
```

---

# 14. Canonical Summary

The SUBIT Interpreter is the semantic decoder of SUBIT‑64.  
It transforms raw input into a complete semantic configuration, enabling structured reasoning, stable topology, and consistent expression.  
It is the **gateway** to the entire SUBIT‑64 architecture.

