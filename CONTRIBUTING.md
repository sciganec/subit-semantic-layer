# Contributing to SUBIT‑64
Thank you for your interest in contributing to SUBIT‑64.  
This project follows a strict architectural and stylistic canon to ensure clarity, modularity, and long‑term stability.

This document outlines the guidelines for contributing code, documentation, personas, tools, and specifications.

---

# 1. Core Principles

### 1.1 Canonical Consistency
All contributions must align with the SUBIT‑64 architecture:
- Interpreter → Reasoning → Topology → Persona
- 64‑archetype ontology
- Shadow axis and sense10 semantics
- Topology packet schema
- Persona separation (expression ≠ reasoning)

### 1.2 Minimalism
Code and documentation must be:
- clean  
- modular  
- explicit  
- free of unnecessary abstractions  

### 1.3 Deterministic Structure
Every module must have:
- clear input/output contracts  
- predictable behavior  
- no hidden side effects  

---

# 2. Repository Structure

Contributions must follow the existing directory layout:

```
/spec/              — canonical definitions
/docs/              — documentation
/sdk/python/        — Python SDK
/sdk/js/            — JavaScript SDK
/agents/            — personas, examples, multi‑agent
/tools/             — validators, generators, visualizers
/whitepaper/        — theoretical foundation
```

Do not introduce new top‑level directories without discussion.

---

# 3. How to Contribute

### 3.1 Reporting Issues
Use GitHub Issues for:
- bugs  
- inconsistencies  
- unclear documentation  
- feature requests  

Include:
- reproduction steps  
- expected vs actual behavior  
- relevant files or snippets  

### 3.2 Submitting Pull Requests
All PRs must:
- target the `main` branch  
- include a clear description  
- reference related issues  
- pass all validators and tests  
- follow canonical formatting  

PRs that modify architecture or spec require discussion before submission.

---

# 4. Coding Guidelines

### 4.1 Python
- PEP8 compliant  
- no external dependencies unless essential  
- functions must be pure unless explicitly documented  
- validators and generators must be minimal and explicit  

### 4.2 JavaScript
- ES modules  
- no bundlers  
- no heavy dependencies  
- match Python SDK structure where possible  

### 4.3 Tests
- place tests in `/tests/`  
- cover core logic, not stylistic behavior  

---

# 5. Documentation Guidelines

### 5.1 Style
Documentation must be:
- concise  
- structural  
- canonical  
- free of marketing language  

### 5.2 Required Sections
Each new document must include:
- purpose  
- scope  
- canonical definitions  
- examples (if applicable)  

### 5.3 Persona Documentation
Personas must follow the template in:
```
/sdk/templates/persona-template.md
```

---

# 6. Adding New Modules

### 6.1 New Personas
Must include:
- persona file  
- JSON definition (if used with generators)  
- example outputs  
- alignment with archetype + shadow  

### 6.2 New Reasoning Modules
Must:
- follow MIST structure  
- define hypothesis expansion + convergence  
- not modify topology or persona layers  

### 6.3 New Topology Modules
Must:
- follow topology packet schema  
- define basin/gradient/curvature logic  
- remain deterministic  

---

# 7. Tools & Utilities

All tools must:
- be standalone  
- require no external services  
- follow the minimal CLI pattern  
- output clean JSON, Markdown, or PNG  

Examples:
- validators  
- generators  
- visualizers  
- exporters  

---

# 8. Architectural Changes

Changes to `/spec/` or `/whitepaper/` require:
- proposal via GitHub Issue  
- discussion with maintainers  
- architectural justification  
- updated diagrams if needed  

These changes are rare and must preserve canonical integrity.

---

# 9. Code of Conduct

Contributors are expected to:
- be respectful  
- collaborate constructively  
- maintain architectural clarity  
- avoid unnecessary complexity  

---

# 10. Summary

To contribute effectively:
- follow the architecture  
- keep everything minimal and explicit  
- respect canonical definitions  
- document clearly  
- test thoroughly  

SUBIT‑64 grows through clarity, structure, and shared semantic discipline.

