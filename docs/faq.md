# SUBIT‑64 FAQ
### Frequently Asked Questions

This FAQ addresses common questions about the SUBIT‑64 architecture, its components, and its usage.

---

# 1. General

### **What is SUBIT‑64?**
A modular semantic architecture for building interpretable cognitive agents.  
It consists of four layers: Interpreter → Reasoning → Topology → Persona.

### **Why “64”?**
Because the system uses a canonical ontology of **64 archetypes**, each representing a distinct cognitive mode.

### **Is SUBIT‑64 a model?**
No.  
It is an **architecture**, not a model.  
It defines structure, flow, and semantics — independent of any underlying LLM.

---

# 2. Interpreter Layer

### **What does the interpreter do?**
It extracts semantic primitives:
- archetype  
- shadow  
- sense10  
- frame seed  
- topology seed  

It does **not** perform reasoning.

### **How is the archetype selected?**
Through a mapping function defined in `/spec/archetypal-ontology-64.md`.

---

# 3. Reasoning Layer (MIST)

### **What is MIST?**
MIST (Modular Insight Synthesis Tree) is the reasoning engine that:
- expands hypotheses  
- evaluates them  
- converges on a dominant trajectory  
- produces distilled insight  

### **Does persona affect reasoning?**
No.  
Reasoning is always neutral and persona‑independent.

---

# 4. Topology Layer

### **What is a semantic basin?**
A stable cognitive attractor determined by archetype and refined by reasoning.

### **What is a gradient?**
A directional vector derived from shadow tension and reasoning trajectory.

### **Why does SUBIT‑64 use topology?**
To represent cognition as **movement** through structured semantic space.

---

# 5. Persona Layer

### **What is a persona?**
A behavioral mask defining tone, voice, pacing, and expression constraints.

### **Does persona change the meaning of the output?**
No.  
Persona shapes **expression**, not **reasoning** or **topology**.

### **Can I create custom personas?**
Yes — using the template in `/sdk/templates/persona-template.md`.

---

# 6. Agents

### **What is a SUBIT‑agent?**
A composition of:
- interpreter  
- reasoning engine  
- topology engine  
- persona mask  

### **Can SUBIT‑agents work together?**
Yes.  
Multi‑agent coordination is defined in `/agents/multi-agent/`.

---

# 7. SDKs

### **Which languages are supported?**
- Python (`/sdk/python/`)  
- JavaScript (`/sdk/js/`)

### **Do SDKs implement the full architecture?**
They implement:
- interpreter  
- topology engine  
- archetype selector  
- example agents  

Reasoning and persona logic are defined in the spec and templates.

---

# 8. Extensibility

### **Can I add new reasoning modules?**
Yes — using `/sdk/templates/reasoning-template.md`.

### **Can I add new topology modules?**
Yes — using `/sdk/templates/topology-template.md`.

### **Can I add new personas?**
Yes — personas are fully modular.

---

# 9. Theory & Specification

### **Where is the formal definition?**
In `/spec/canonical-definition.md`.

### **Where is the theoretical foundation?**
In `/whitepaper/subit-64-semantic-layer.md`.

### **Where are diagrams?**
In `/whitepaper/diagrams/` and `/docs/diagrams/`.

---

# 10. Usage & Integration

### **Can SUBIT‑64 run on any LLM?**
Yes.  
It is model‑agnostic.

### **Does SUBIT‑64 require memory?**
No.  
Memory is optional and used only in multi‑step or multi‑agent modes.

### **Can I embed SUBIT‑64 in an existing system?**
Yes — via the Python or JS SDK.

---

# 11. Troubleshooting

### **The agent output feels inconsistent. Why?**
Check:
- archetype selection  
- shadow intensity  
- persona constraints  
- topology stability  

### **The persona output feels too strong. Why?**
Ensure the persona mask does not override reasoning content.

### **The topology seems unstable. Why?**
High curvature or strong gradient → natural instability.

---

# 12. Summary

SUBIT‑64 is:
- modular  
- interpretable  
- extensible  
- model‑agnostic  
- grounded in semantic topology  

This FAQ covers the most common questions.  
For deeper detail, see `/spec/` and `/whitepaper/`.

