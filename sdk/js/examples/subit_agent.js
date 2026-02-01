// ================================================================
// SUBIT-64 Basic Agent (JavaScript Version)
// Canonical minimal runtime wiring
// ================================================================
// Pipeline:
//   1. SUBIT Interpreter      (text -> semantic init packet)
//   2. MIST Reasoning Engine  (init -> cognitive packet)
//   3. Topology Engine        (cognitive -> semantic topology)
//   4. Behavioral Mask        (topology -> final expression)
// ================================================================

import { interpret } from "./subit_interpreter.js";
import { runMIST } from "./mist_engine.js";
import { buildTopology } from "./topology_engine.js";
import { applyMask } from "./behavioral_mask.js";

// ---------------------------------------------------------------
// 1. AGENT CLASS
// ---------------------------------------------------------------

export class SubitAgent {
  constructor(name = "SUBIT-64 JS Agent") {
    this.name = name;
  }

  // Full pipeline with introspection
  process(text) {
    // 1. Interpreter
    const interp = interpret(text);

    // 2. MIST
    const mist = runMIST({
      archetype: interp.archetype,
      shadow: interp.shadow,
      sense10: interp.sense10,
      frame_seed: interp.frame_seed
    });

    // 3. Topology
    const topology = buildTopology({
      mist,
      archetype: interp.archetype,
      shadow: interp.shadow
    });

    // 4. Mask
    const expression = applyMask({
      topology,
      archetype: interp.archetype,
      shadow: interp.shadow
    });

    return {
      interpreter: interp,
      mist,
      topology,
      expression
    };
  }

  // User-facing method
  reply(text) {
    const packets = this.process(text);
    return packets.expression.final_output || "";
  }
}

// ---------------------------------------------------------------
// 2. CLI MODE
// ---------------------------------------------------------------

if (import.meta.main) {
  const agent = new SubitAgent();
  console.log(`[${agent.name}] ready. Type "exit" to quit.\n`);

  const readline = await import("node:readline/promises");
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
  });

  while (true) {
    const user = await rl.question("You: ");

    if (user.trim().toLowerCase() === "exit") {
      console.log("Bye.");
      process.exit(0);
    }

    const answer = agent.reply(user);
    console.log(`Agent: ${answer}\n`);
  }
}
