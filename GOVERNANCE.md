# GOVERNANCE
### SUBIT‑64 Project Governance Model

SUBIT‑64 is an architecture‑driven project that prioritizes clarity, modularity, and canonical consistency.  
This document defines how decisions are made, how changes are approved, and how the long‑term integrity of the architecture is maintained.

---

# 1. Governance Principles

### 1.1 Canonical Integrity
All decisions must preserve:
- the four‑layer architecture  
- the 64‑archetype ontology  
- the topology model  
- persona separation  
- deterministic input/output contracts  

No change may compromise these foundations.

### 1.2 Minimalism
Governance favors:
- fewer rules  
- explicit structures  
- minimal abstractions  
- clarity over complexity  

### 1.3 Transparency
All architectural decisions, discussions, and proposals must be public and documented.

### 1.4 Stability
The architecture evolves deliberately.  
Rapid or unreviewed changes are not permitted.

---

# 2. Roles

### 2.1 Maintainers
Responsible for:
- reviewing and merging PRs  
- enforcing canonical consistency  
- approving architectural changes  
- curating roadmap direction  

Maintainers have final authority on architectural decisions.

### 2.2 Contributors
Anyone submitting:
- code  
- documentation  
- personas  
- tools  
- tests  
- proposals  

Contributors must follow `CONTRIBUTING.md` and respect canonical definitions.

### 2.3 Reviewers
Community members who:
- review PRs  
- provide feedback  
- identify inconsistencies  

Reviewers do not have merge rights unless they are maintainers.

---

# 3. Decision‑Making Process

### 3.1 Routine Changes
Examples:
- documentation updates  
- minor SDK improvements  
- new personas  
- new tools  

Process:
1. Contributor submits PR  
2. Reviewer feedback (optional)  
3. Maintainer approval  
4. Merge  

### 3.2 Architectural Changes
Examples:
- modifications to `/spec/`  
- changes to archetype ontology  
- topology model updates  
- reasoning layer redesign  

Process:
1. Open an issue labeled **architecture‑proposal**  
2. Provide justification, diagrams, and impact analysis  
3. Discussion with maintainers  
4. Maintainer consensus required  
5. Approved changes must update:
   - `/spec/`  
   - diagrams  
   - validators  
   - SDKs (if applicable)  

Architectural changes are rare and must preserve canonical integrity.

### 3.3 Roadmap Changes
Changes to `ROADMAP.md` require maintainer approval.

---

# 4. Release Management

### 4.1 Versioning
SUBIT‑64 uses semantic versioning:
- MAJOR — breaking architectural changes  
- MINOR — new features, personas, tools  
- PATCH — fixes and refinements  

### 4.2 Release Process
1. All tests and validators must pass  
2. Documentation updated  
3. CHANGELOG updated  
4. Maintainer signs off  
5. Release tagged  

---

# 5. Conflict Resolution

### 5.1 Technical Disagreements
Resolved through:
- reference to canonical definitions  
- architectural principles  
- maintainers’ final decision  

### 5.2 Contributor Conflicts
Handled privately by maintainers with focus on:
- respect  
- clarity  
- constructive collaboration  

---

# 6. Adding New Maintainers

Criteria:
- consistent high‑quality contributions  
- deep understanding of SUBIT‑64 architecture  
- demonstrated alignment with canonical principles  
- positive collaboration history  

New maintainers are added by consensus of existing maintainers.

---

# 7. Removing Maintainers

A maintainer may be removed if they:
- repeatedly violate canonical principles  
- introduce instability  
- become inactive for extended periods  
- engage in harmful behavior  

Removal requires consensus of remaining maintainers.

---

# 8. Governance Changes

Any modification to this document requires:
- an issue labeled **governance‑proposal**  
- discussion  
- maintainer consensus  

Governance evolves slowly and deliberately.

---

# 9. Summary

The SUBIT‑64 governance model ensures:
- architectural stability  
- transparent decision‑making  
- minimalistic structure  
- long‑term coherence  
- high‑quality contributions  

Governance protects the canon so the architecture can grow with clarity and purpose.

