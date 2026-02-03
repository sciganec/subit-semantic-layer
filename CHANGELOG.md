# CHANGELOG
All notable changes to this project will be documented in this file.  
This project adheres to semantic versioning.

---

## [1.0.0] — Initial Public Release
### Added
- Full SUBIT‑64 architecture (Interpreter → Reasoning → Topology → Persona)
- Canonical 64‑archetype ontology
- Shadow axis and sense10 vector definitions
- MIST reasoning layer specification
- Content topology specification (basins, gradients, curvature, transitions)
- Persona layer specification and templates
- SUBIT‑agent architecture and example agents
- Python SDK (interpreter, topology engine, archetype selector)
- JavaScript SDK (interpreter, example agents)
- Tools:
  - archetype-validator
  - topology-validator
  - persona-generator
  - topology-generator
  - state-visualizer
  - semantic-graph-exporter
- Documentation:
  - overview.md
  - architecture.md
  - glossary.md
  - faq.md
  - narrative.md
  - presentation-deck-outline.md
- Branding materials (pitch narrative, deck outline)

### Changed
- Consolidated specification into `/spec/` directory
- Unified persona template across SDKs
- Updated directory structure for clarity and modularity

### Fixed
- Minor inconsistencies in archetype codes
- Topology packet schema alignment across SDKs
- Persona mask formatting issues

---

## [0.9.0] — Pre‑Release (Internal)
### Added
- Early interpreter prototype
- Initial MIST reasoning draft
- First version of topology engine
- Early personas (Strategist, Analyst, Mentor)
- Internal diagrams and whitepaper drafts

### Changed
- Refined archetype ontology from 32 → 64 modes
- Reworked shadow axis to continuous 0–1 scale

### Fixed
- Stability computation errors in early topology engine

---

## [0.1.0] — Prototype
### Added
- First conceptual sketches of SUBIT‑64
- Early notes on archetypes and semantic basins

