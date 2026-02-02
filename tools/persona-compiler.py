# ================================================================
# SUBIT-64 Persona Compiler
# Canonical minimal tool for converting persona markdown files
# into JSON persona masks for agents.
# ================================================================
# Usage:
#   python persona-compiler.py persona-pack.md output_dir/
#
# Output:
#   - Each persona becomes output_dir/<persona-name>.json
#   - Clean, minimal JSON masks ready for agent loading
# ================================================================

import os
import sys
import json
import re


# ---------------------------------------------------------------
# 1. MARKDOWN PARSER (MINIMAL, STRUCTURAL)
# ---------------------------------------------------------------

SECTION_HEADERS = [
    "1. Persona Overview",
    "2. Behavioral Mask",
    "3. Expression Constraints",
    "4. Semantic Alignment",
    "5. Interaction Model",
    "6. Output Format Rules",
    "7. Example Outputs",
    "8. Integration Notes",
    "9. Persona Summary"
]


def split_personas(md_text):
    """Split persona-pack.md into individual persona blocks."""
    blocks = re.split(r"^={20,}.*$", md_text, flags=re.MULTILINE)
    personas = [b.strip() for b in blocks if b.strip()]
    return personas


def extract_name(block):
    """Extract persona name from the block."""
    m = re.search(r"\*\*Name:\*\*\s*(.+)", block)
    return m.group(1).strip() if m else "UnnamedPersona"


def extract_sections(block):
    """Extract sections by header."""
    sections = {}
    for i, header in enumerate(SECTION_HEADERS):
        pattern = rf"##\s*{re.escape(header)}(.*?)(?=##\s*\d+\.|\Z)"
        m = re.search(pattern, block, flags=re.DOTALL)
        if m:
            sections[header] = m.group(1).strip()
        else:
            sections[header] = ""
    return sections


def compile_persona(block):
    """Convert a persona markdown block into a JSON-ready dict."""
    name = extract_name(block)
    sections = extract_sections(block)

    return {
        "name": name,
        "overview": sections["1. Persona Overview"],
        "behavioral_mask": sections["2. Behavioral Mask"],
        "expression_constraints": sections["3. Expression Constraints"],
        "semantic_alignment": sections["4. Semantic Alignment"],
        "interaction_model": sections["5. Interaction Model"],
        "output_format": sections["6. Output Format Rules"],
        "examples": sections["7. Example Outputs"],
        "integration": sections["8. Integration Notes"],
        "summary": sections["9. Persona Summary"]
    }


# ---------------------------------------------------------------
# 2. MAIN COMPILER
# ---------------------------------------------------------------

def compile_file(input_path, output_dir):
    with open(input_path, "r", encoding="utf-8") as f:
        text = f.read()

    personas = split_personas(text)

    os.makedirs(output_dir, exist_ok=True)

    compiled = []

    for block in personas:
        persona = compile_persona(block)
        name = persona["name"].replace(" ", "_")
        out_path = os.path.join(output_dir, f"{name}.json")

        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(persona, f, indent=2, ensure_ascii=False)

        compiled.append(out_path)

    return compiled


# ---------------------------------------------------------------
# 3. CLI
# ---------------------------------------------------------------

def main():
    if len(sys.argv) < 3:
        print("Usage: python persona-compiler.py <input.md> <output_dir>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_dir = sys.argv[2]

    outputs = compile_file(input_path, output_dir)

    print("Compiled personas:")
    for o in outputs:
        print(" -", o)


if __name__ == "__main__":
    main()
