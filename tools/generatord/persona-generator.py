#!/usr/bin/env python3
# persona-generator.py
# SUBIT‑64 Canonical Persona Generator

import json
import sys
from pathlib import Path

TEMPLATE = """# {name} Persona (SUBIT‑64 Canonical)

## 1. Overview
**Name:** {name}
**Role:** {role}
**Function:** {function}
**Archetypal Alignment:** {archetype}
**Shadow Profile:** {shadow}
**Behavioral Domain:** {domain}

**Identity (1 sentence):**  
> {identity}

---

## 2. Behavioral Mask

### Tone
{tone}

### Voice
{voice}

### Style Rules
{style_rules}

### Pacing
{pacing}

---

## 3. Expression Constraints

### Allowed Moves
{allowed_moves}

### Forbidden Moves
{forbidden_moves}

### Signature Patterns
{signature_patterns}

---

## 4. Semantic Alignment

### Archetype Influence
{archetype_influence}

### Shadow Influence
{shadow_influence}

---

## 5. Interaction Model

### Response to Users
{response_to_users}

### Conversational Dynamics
{conversational_dynamics}

### Relationship Mode
{relationship_mode}

---

## 6. Output Format Rules

### Structure
{structure}

### Density
{density}

### Clarity vs Ambiguity
{clarity}

---

## 7. Example Outputs

### 7.1 Neutral Query
```
{example_neutral}
```

### 7.2 Emotional Query
```
{example_emotional}
```

### 7.3 Complex Multi‑Layer Query
```
{example_complex}
```

---

## 8. Integration Notes
{integration_notes}

---

## 9. Persona Summary
**Identity:** {summary_identity}  
**Tone:** {summary_tone}  
**Voice:** {summary_voice}  
**Mode:** {summary_mode}  
**Archetype:** {archetype}  
**Shadow:** {shadow}  
**Signature:** {summary_signature}  
**Constraints:** {summary_constraints}
"""

def load_json(path: Path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"[ERROR] Cannot load JSON: {e}")
        sys.exit(1)

def generate_persona(data: dict):
    try:
        return TEMPLATE.format(**data)
    except KeyError as e:
        print(f"[ERROR] Missing required field in JSON: {e}")
        sys.exit(1)

def save_output(content: str, output_path: Path):
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)
    except Exception as e:
        print(f"[ERROR] Cannot write output: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) < 3:
        print("Usage: persona-generator.py <persona.json> <output.md>")
        sys.exit(1)

    json_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])

    data = load_json(json_path)
    content = generate_persona(data)
    save_output(content, output_path)

    print(f"[GENERATED] Persona saved to {output_path}")

if __name__ == "__main__":
    main()
