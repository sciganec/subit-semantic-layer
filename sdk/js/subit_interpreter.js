// ================================================================
// SUBIT-64 Interpreter (JavaScript Version)
// Canonical implementation of the semantic initialization layer
// ================================================================
// Pipeline:
//   1. SENSE-10 extraction
//   2. SUBIT-6 axis reduction
//   3. 6-bit codon generation
//   4. Archetype lookup (imported table)
//   5. Shadow computation
//   6. Frame + topology seeds
//   7. Output packet
// ================================================================

import { ARCHETYPES } from "./archetype_selector.js";

// ---------------------------------------------------------------
// 1. SENSE-10 extraction (placeholder heuristic)
// ---------------------------------------------------------------

function extractSense10(text) {
  return {
    intent: "analysis",
    tone: "neutral",
    urgency: 0.4,
    complexity: 0.5,
    ambiguity: 0.2,
    relation: "self",
    temporal: "present",
    risk: 0.3,
    domain: "general",
    mode: "analytical"
  };
}

// ---------------------------------------------------------------
// 2. SUBIT-6 axis reduction
// ---------------------------------------------------------------

function reduceToSubit6(s) {
  return {
    b1: s.complexity < 0.6 ? 0 : 1,          // Order / Chaos
    b2: s.relation === "self" ? 0 : 1,      // Self / Other
    b3: s.mode === "analytical" ? 0 : 1,    // Abstract / Concrete
    b4: s.urgency > 0.3 ? 0 : 1,            // Active / Passive
    b5: s.temporal === "present" ? 0 : 1,   // Inner / Outer
    b6: s.risk > 0.5 ? 1 : 0                // Flow / Structure
  };
}

// ---------------------------------------------------------------
// 3. Codon generation
// ---------------------------------------------------------------

function axesToCodon(ax) {
  return `${ax.b1}${ax.b2}${ax.b3}${ax.b4}${ax.b5}${ax.b6}`;
}

// ---------------------------------------------------------------
// 4. Archetype lookup
// ---------------------------------------------------------------

function lookupArchetype(codon) {
  return ARCHETYPES[codon] || {
    id: codon,
    name: "Unknown",
    cognitive_mode: "undefined",
    behavioral_mode: "undefined",
    attractor: "undefined"
  };
}

// ---------------------------------------------------------------
// 5. Shadow computation
// ---------------------------------------------------------------

function computeShadow(sense, archetype) {
  const intensity = (sense.ambiguity + sense.risk + sense.urgency) / 3;

  return {
    intensity,
    distortion: {
      clarity: 1 - intensity,
      tension: intensity
    },
    emotional_bias: sense.tone
  };
}

// ---------------------------------------------------------------
// 6. Seeds
// ---------------------------------------------------------------

function computeFrameSeed(archetype, shadow) {
  return `${archetype.name}:frame:${shadow.emotional_bias}`;
}

function computeTopologySeed(archetype, shadow) {
  return {
    basin: archetype.attractor,
    gradient: shadow.intensity
  };
}

// ---------------------------------------------------------------
// 7. MAIN INTERPRETER FUNCTION
// ---------------------------------------------------------------

export function interpret(text) {
  const sense10 = extractSense10(text);
  const axes = reduceToSubit6(sense10);
  const codon = axesToCodon(axes);
  const archetype = lookupArchetype(codon);
  const shadow = computeShadow(sense10, archetype);
  const frame_seed = computeFrameSeed(archetype, shadow);
  const topology_seed = computeTopologySeed(archetype, shadow);

  return {
    sense10,
    axes,
    codon,
    archetype,
    shadow,
    frame_seed,
    topology_seed
  };
}

// ---------------------------------------------------------------
// 8. CLI TEST
// ---------------------------------------------------------------

if (import.meta.main) {
  const result = interpret("Help me plan a project.");
  console.log(JSON.stringify(result, null, 2));
}
