# ================================================================
# SUBIT Interpreter
# Canonical Python Implementation
# ================================================================
# This module implements the full SUBIT‑Interpreter pipeline:
#   1. SENSE‑10 extraction
#   2. SUBIT‑6 axis reduction
#   3. 6‑bit codon generation
#   4. SUBIT‑64 archetype lookup
#   5. Shadow vector computation
#   6. Interpreter output packet
#
# The interpreter is deterministic and modular.
# ================================================================

from dataclasses import dataclass, asdict
from typing import Dict, Any


# ================================================================
# 1. DATA STRUCTURES
# ================================================================

@dataclass
class Sense10:
    intent: str
    tone: str
    urgency: float
    complexity: float
    ambiguity: float
    relation: str
    temporal: str
    risk: float
    domain: str
    mode: str


@dataclass
class Subit6:
    b1: int
    b2: int
    b3: int
    b4: int
    b5: int
    b6: int


@dataclass
class Archetype:
    id: str
    name: str
    cognitive_mode: str
    behavioral_mode: str
    attractor: str


@dataclass
class Shadow:
    intensity: float
    distortion: Dict[str, float]
    emotional_bias: str


@dataclass
class InterpreterPacket:
    sense10: Dict[str, Any]
    axes: Dict[str, int]
    codon: str
    archetype: Dict[str, Any]
    shadow: Dict[str, Any]
    frame_seed: str
    topology_seed: Dict[str, Any]


# ================================================================
# 2. CANONICAL TABLES
# ================================================================

ARCHETYPES = {
    # 00xxxx — ORDER / SELF

    "000000": Archetype(
        id="000000",
        name="Architect",
        cognitive_mode="structural clarity, system-building",
        behavioral_mode="designing, organizing",
        attractor="coherence"
    ),
    "000001": Archetype(
        id="000001",
        name="Weaver",
        cognitive_mode="pattern synthesis",
        behavioral_mode="connecting, integrating",
        attractor="integration"
    ),
    "000010": Archetype(
        id="000010",
        name="Analyst",
        cognitive_mode="abstraction, conceptual modeling",
        behavioral_mode="dissecting, explaining",
        attractor="generalization"
    ),
    "000011": Archetype(
        id="000011",
        name="Cartographer",
        cognitive_mode="mapping, classification",
        behavioral_mode="charting, categorizing",
        attractor="structure"
    ),
    "000100": Archetype(
        id="000100",
        name="Initiator",
        cognitive_mode="decisive activation",
        behavioral_mode="starting, pushing forward",
        attractor="momentum"
    ),
    "000101": Archetype(
        id="000101",
        name="Strategist",
        cognitive_mode="planning, foresight",
        behavioral_mode="optimizing, sequencing",
        attractor="optimization"
    ),
    "000110": Archetype(
        id="000110",
        name="Observer",
        cognitive_mode="reflective abstraction",
        behavioral_mode="watching, noticing",
        attractor="insight"
    ),
    "000111": Archetype(
        id="000111",
        name="Custodian",
        cognitive_mode="preservation, maintenance",
        behavioral_mode="maintaining, guarding",
        attractor="stability"
    ),

    # 01xxxx — ORDER / OTHER

    "010000": Archetype(
        id="010000",
        name="Mediator",
        cognitive_mode="relational balance",
        behavioral_mode="balancing, reconciling",
        attractor="harmony"
    ),
    "010001": Archetype(
        id="010001",
        name="Connector",
        cognitive_mode="linking systems and people",
        behavioral_mode="bridging, networking",
        attractor="cohesion"
    ),
    "010010": Archetype(
        id="010010",
        name="Interpreter",
        cognitive_mode="translation, reframing",
        behavioral_mode="explaining, rephrasing",
        attractor="mutual understanding"
    ),
    "010011": Archetype(
        id="010011",
        name="Diplomat",
        cognitive_mode="negotiation, alignment",
        behavioral_mode="mediating, aligning",
        attractor="agreement"
    ),
    "010100": Archetype(
        id="010100",
        name="Coordinator",
        cognitive_mode="organizing collective action",
        behavioral_mode="scheduling, orchestrating",
        attractor="synchronization"
    ),
    "010101": Archetype(
        id="010101",
        name="Mentor",
        cognitive_mode="guidance, elevation",
        behavioral_mode="teaching, supporting",
        attractor="development"
    ),
    "010110": Archetype(
        id="010110",
        name="Evaluator",
        cognitive_mode="assessment, calibration",
        behavioral_mode="judging, measuring",
        attractor="accuracy"
    ),
    "010111": Archetype(
        id="010111",
        name="Steward",
        cognitive_mode="responsibility, guardianship",
        behavioral_mode="caring, overseeing",
        attractor="continuity"
    ),

    # 10xxxx — CHAOS / SELF

    "100000": Archetype(
        id="100000",
        name="Spark",
        cognitive_mode="creative ignition",
        behavioral_mode="initiating novelty",
        attractor="novelty"
    ),
    "100001": Archetype(
        id="100001",
        name="Improviser",
        cognitive_mode="spontaneous synthesis",
        behavioral_mode="ad‑hoc combining",
        attractor="emergence"
    ),
    "100010": Archetype(
        id="100010",
        name="Visionary",
        cognitive_mode="abstract projection",
        behavioral_mode="imagining futures",
        attractor="possibility"
    ),
    "100011": Archetype(
        id="100011",
        name="Explorer",
        cognitive_mode="boundary‑breaking exploration",
        behavioral_mode="probing, venturing",
        attractor="expansion"
    ),
    "100100": Archetype(
        id="100100",
        name="Challenger",
        cognitive_mode="disruption, force",
        behavioral_mode="confronting, pushing",
        attractor="change"
    ),
    "100101": Archetype(
        id="100101",
        name="Hacker",
        cognitive_mode="subversion, reconfiguration",
        behavioral_mode="tweaking, breaking patterns",
        attractor="transformation"
    ),
    "100110": Archetype(
        id="100110",
        name="Diver",
        cognitive_mode="deep introspection",
        behavioral_mode="descending inward",
        attractor="depth"
    ),
    "100111": Archetype(
        id="100111",
        name="Rebel",
        cognitive_mode="inversion, refusal",
        behavioral_mode="rejecting, overturning",
        attractor="rupture"
    ),

    # 11xxxx — CHAOS / OTHER

    "110000": Archetype(
        id="110000",
        name="Catalyst",
        cognitive_mode="accelerating others",
        behavioral_mode="triggering, energizing",
        attractor="activation"
    ),
    "110001": Archetype(
        id="110001",
        name="Networker",
        cognitive_mode="emergent relational webs",
        behavioral_mode="connecting many nodes",
        attractor="propagation"
    ),
    "110010": Archetype(
        id="110010",
        name="Trickster",
        cognitive_mode="reframing through disruption",
        behavioral_mode="subverting, teasing",
        attractor="inversion"
    ),
    "110011": Archetype(
        id="110011",
        name="Wanderer",
        cognitive_mode="drifting exploration",
        behavioral_mode="roaming, sampling",
        attractor="diffusion"
    ),
    "110100": Archetype(
        id="110100",
        name="Instigator",
        cognitive_mode="provoking movement",
        behavioral_mode="stirring, agitating",
        attractor="ignition"
    ),
    "110101": Archetype(
        id="110101",
        name="Oracle",
        cognitive_mode="nonlinear insight",
        behavioral_mode="pronouncing, hinting",
        attractor="revelation"
    ),
    "110110": Archetype(
        id="110110",
        name="Mirror",
        cognitive_mode="reflecting others’ states",
        behavioral_mode="mirroring, echoing",
        attractor="resonance"
    ),
    "110111": Archetype(
        id="110111",
        name="Storm",
        cognitive_mode="overwhelming force",
        behavioral_mode="flooding, overwhelming",
        attractor="turbulence"
    ),

    # 00→11 Passive / Outer / Structure variants (друга 32‑ка)

    # ORDER / SELF (Passive / Outer / Structure variants)

    "001000": Archetype(
        id="001000",
        name="Listener",
        cognitive_mode="receptive awareness",
        behavioral_mode="hearing, attending",
        attractor="clarity"
    ),
    "001001": Archetype(
        id="001001",
        name="Synthesizer",
        cognitive_mode="quiet integration",
        behavioral_mode="absorbing, combining",
        attractor="coherence"
    ),
    "001010": Archetype(
        id="001010",
        name="Scholar",
        cognitive_mode="abstract study",
        behavioral_mode="studying, referencing",
        attractor="knowledge"
    ),
    "001011": Archetype(
        id="001011",
        name="Archivist",
        cognitive_mode="preservation of information",
        behavioral_mode="storing, cataloging",
        attractor="continuity"
    ),
    "001100": Archetype(
        id="001100",
        name="Stabilizer",
        cognitive_mode="passive grounding",
        behavioral_mode="holding steady",
        attractor="equilibrium"
    ),
    "001101": Archetype(
        id="001101",
        name="Planner",
        cognitive_mode="structured foresight",
        behavioral_mode="laying out steps",
        attractor="order"
    ),
    "001110": Archetype(
        id="001110",
        name="Witness",
        cognitive_mode="detached observation",
        behavioral_mode="seeing without acting",
        attractor="neutrality"
    ),
    "001111": Archetype(
        id="001111",
        name="Conservator",
        cognitive_mode="maintaining systems",
        behavioral_mode="preserving, protecting",
        attractor="preservation"
    ),

    # ORDER / OTHER (Passive / Outer / Structure variants)

    "011000": Archetype(
        id="011000",
        name="Harmonizer",
        cognitive_mode="quiet relational tuning",
        behavioral_mode="soft balancing",
        attractor="balance"
    ),
    "011001": Archetype(
        id="011001",
        name="Bridge",
        cognitive_mode="connecting without imposing",
        behavioral_mode="linking gently",
        attractor="linkage"
    ),
    "011010": Archetype(
        id="011010",
        name="Translator",
        cognitive_mode="precise interpretation",
        behavioral_mode="rendering faithfully",
        attractor="clarity"
    ),
    "011011": Archetype(
        id="011011",
        name="Negotiator",
        cognitive_mode="soft alignment",
        behavioral_mode="balancing interests",
        attractor="consensus"
    ),
    "011100": Archetype(
        id="011100",
        name="Organizer",
        cognitive_mode="passive coordination",
        behavioral_mode="arranging, ordering",
        attractor="order"
    ),
    "011101": Archetype(
        id="011101",
        name="Guide",
        cognitive_mode="gentle mentorship",
        behavioral_mode="pointing, suggesting",
        attractor="growth"
    ),
    "011110": Archetype(
        id="011110",
        name="Auditor",
        cognitive_mode="quiet evaluation",
        behavioral_mode="checking, reviewing",
        attractor="precision"
    ),
    "011111": Archetype(
        id="011111",
        name="Keeper",
        cognitive_mode="stewardship through restraint",
        behavioral_mode="holding, guarding",
        attractor="continuity"
    ),

    # CHAOS / SELF (Passive / Outer / Structure variants)

    "101000": Archetype(
        id="101000",
        name="Flicker",
        cognitive_mode="subtle creative impulse",
        behavioral_mode="hinting, suggesting novelty",
        attractor="novelty"
    ),
    "101001": Archetype(
        id="101001",
        name="Mixer",
        cognitive_mode="chaotic blending",
        behavioral_mode="combining unpredictably",
        attractor="emergence"
    ),
    "101010": Archetype(
        id="101010",
        name="Dreamer",
        cognitive_mode="abstract imagination",
        behavioral_mode="drifting in possibilities",
        attractor="possibility"
    ),
    "101011": Archetype(
        id="101011",
        name="Drifter",
        cognitive_mode="wandering curiosity",
        behavioral_mode="moving without fixed aim",
        attractor="exploration"
    ),
    "101100": Archetype(
        id="101100",
        name="Disruptor",
        cognitive_mode="passive destabilization",
        behavioral_mode="loosening structures",
        attractor="change"
    ),
    "101101": Archetype(
        id="101101",
        name="Tinkerer",
        cognitive_mode="playful reconfiguration",
        behavioral_mode="experimenting, tweaking",
        attractor="transformation"
    ),
    "101110": Archetype(
        id="101110",
        name="Deep Diver",
        cognitive_mode="nonlinear introspection",
        behavioral_mode="sinking into depth",
        attractor="depth"
    ),
    "101111": Archetype(
        id="101111",
        name="Breaker",
        cognitive_mode="quiet refusal",
        behavioral_mode="withdrawing, breaking away",
        attractor="rupture"
    ),

    # CHAOS / OTHER (Passive / Outer / Structure variants)

    "111000": Archetype(
        id="111000",
        name="Enabler",
        cognitive_mode="amplifying others’ chaos",
        behavioral_mode="supporting activation",
        attractor="activation"
    ),
    "111001": Archetype(
        id="111001",
        name="Web-Spinner",
        cognitive_mode="emergent relational complexity",
        behavioral_mode="weaving networks",
        attractor="propagation"
    ),
    "111010": Archetype(
        id="111010",
        name="Jester",
        cognitive_mode="playful disruption",
        behavioral_mode="joking, poking",
        attractor="inversion"
    ),
    "111011": Archetype(
        id="111011",
        name="Nomad",
        cognitive_mode="drifting through systems",
        behavioral_mode="moving between contexts",
        attractor="diffusion"
    ),
    "111100": Archetype(
        id="111100",
        name="Agitator",
        cognitive_mode="stirring latent forces",
        behavioral_mode="provoking, unsettling",
        attractor="ignition"
    ),
    "111101": Archetype(
        id="111101",
        name="Seer",
        cognitive_mode="nonlinear perception",
        behavioral_mode="revealing, hinting",
        attractor="revelation"
    ),
    "111110": Archetype(
        id="111110",
        name="Reflector",
        cognitive_mode="mirroring external chaos",
        behavioral_mode="reflecting, echoing",
        attractor="resonance"
    ),
    "111111": Archetype(
        id="111111",
        name="Tempest",
        cognitive_mode="total system upheaval",
        behavioral_mode="overturning everything",
        attractor="turbulence"
    ),
}

# ================================================================
# 3. SENSE‑10 EXTRACTION (placeholder heuristic)
# ================================================================

def extract_sense10(text: str) -> Sense10:
    # In production this is an LLM or classifier
    return Sense10(
        intent="analysis",
        tone="neutral",
        urgency=0.4,
        complexity=0.5,
        ambiguity=0.2,
        relation="self",
        temporal="present",
        risk=0.3,
        domain="general",
        mode="analytical"
    )


# ================================================================
# 4. SUBIT‑6 AXIS REDUCTION
# ================================================================

def reduce_to_subit6(s: Sense10) -> Subit6:
    return Subit6(
        b1=0 if s.complexity < 0.6 else 1,     # Order / Chaos
        b2=0 if s.relation == "self" else 1,   # Self / Other
        b3=0 if s.mode == "analytical" else 1, # Abstract / Concrete
        b4=0 if s.urgency > 0.3 else 1,        # Active / Passive
        b5=0 if s.temporal == "present" else 1,# Inner / Outer
        b6=1 if s.risk > 0.5 else 0            # Flow / Structure
    )


# ================================================================
# 5. CODON GENERATION
# ================================================================

def axes_to_codon(ax: Subit6) -> str:
    return f"{ax.b1}{ax.b2}{ax.b3}{ax.b4}{ax.b5}{ax.b6}"


# ================================================================
# 6. ARCHETYPE LOOKUP
# ================================================================

def lookup_archetype(codon: str) -> Archetype:
    return ARCHETYPES.get(
        codon,
        Archetype(
            id=codon,
            name="Unknown",
            cognitive_mode="undefined",
            behavioral_mode="undefined",
            attractor="undefined"
        )
    )


# ================================================================
# 7. SHADOW COMPUTATION
# ================================================================

def compute_shadow(s: Sense10, archetype: Archetype) -> Shadow:
    intensity = (s.ambiguity + s.risk + s.urgency) / 3
    return Shadow(
        intensity=float(intensity),
        distortion={
            "clarity": 1 - intensity,
            "tension": intensity
        },
        emotional_bias=s.tone
    )


# ================================================================
# 8. FRAME + TOPOLOGY SEEDS
# ================================================================

def compute_frame_seed(archetype: Archetype, shadow: Shadow) -> str:
    return f"{archetype.name}:frame:{shadow.emotional_bias}"


def compute_topology_seed(archetype: Archetype, shadow: Shadow) -> Dict[str, Any]:
    return {
        "basin": archetype.attractor,
        "gradient": shadow.intensity
    }


# ================================================================
# 9. MAIN INTERPRETER FUNCTION
# ================================================================

def interpret(text: str) -> InterpreterPacket:
    sense = extract_sense10(text)
    axes = reduce_to_subit6(sense)
    codon = axes_to_codon(axes)
    archetype = lookup_archetype(codon)
    shadow = compute_shadow(sense, archetype)
    frame_seed = compute_frame_seed(archetype, shadow)
    topology_seed = compute_topology_seed(archetype, shadow)

    return InterpreterPacket(
        sense10=asdict(sense),
        axes=asdict(axes),
        codon=codon,
        archetype=asdict(archetype),
        shadow=asdict(shadow),
        frame_seed=frame_seed,
        topology_seed=topology_seed
    )


# ================================================================
# 10. CLI TEST
# ================================================================

if __name__ == "__main__":
    import json
    text = "Help me plan a project."
    packet = interpret(text)
    print(json.dumps(asdict(packet), indent=2))
