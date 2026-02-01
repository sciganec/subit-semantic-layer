# ================================================================
# SUBIT-64 Memory Agent
# Canonical implementation of a multi-turn agent with memory
# ================================================================
# This agent:
#   - maintains long-term memory
#   - stores semantic states (archetype, shadow, topology)
#   - stores textual memory (facts, commitments, user preferences)
#   - updates memory after each step
#   - exposes memory read/write/reset
# ================================================================

from dataclasses import asdict
from typing import Dict, Any, List

from subit_interpreter import interpret
from mist_engine import run_mist
from topology_engine import build_topology
from behavioral_mask import apply_mask


# ================================================================
# 1. MEMORY STRUCTURE
# ================================================================

class SubitMemory:
    """
    Long-term memory for SUBIT-64 agents.
    Stores:
      - semantic states
      - user facts
      - preferences
      - archetype/shadow trajectories
    """

    def __init__(self):
        self.facts: Dict[str, Any] = {}
        self.semantic_history: List[Dict[str, Any]] = []
        self.archetype_trajectory: List[str] = []
        self.shadow_trajectory: List[float] = []

    def store_fact(self, key: str, value: Any):
        self.facts[key] = value

    def get_fact(self, key: str, default=None):
        return self.facts.get(key, default)

    def store_semantic_state(self, archetype: Dict[str, Any], shadow: Dict[str, Any]):
        self.semantic_history.append({
            "archetype": archetype,
            "shadow": shadow
        })
        self.archetype_trajectory.append(archetype["id"])
        self.shadow_trajectory.append(shadow["intensity"])

    def reset(self):
        self.facts.clear()
        self.semantic_history.clear()
        self.archetype_trajectory.clear()
        self.shadow_trajectory.clear()

    def export(self) -> Dict[str, Any]:
        return {
            "facts": self.facts,
            "semantic_history": self.semantic_history,
            "archetype_trajectory": self.archetype_trajectory,
            "shadow_trajectory": self.shadow_trajectory
        }


# ================================================================
# 2. MEMORY-ENABLED AGENT
# ================================================================

class SubitAgentMemory:
    """
    SUBIT-64 agent with long-term memory.
    """

    def __init__(self, name: str = "SUBIT-64 Memory Agent"):
        self.name = name
        self.memory = SubitMemory()

    # ------------------------------------------------------------
    # INTERNAL PIPELINE
    # ------------------------------------------------------------

    def _pipeline(self, text: str) -> Dict[str, Any]:
        """
        Run one full SUBIT-64 cycle and update memory.
        """

        # 1. Interpreter
        interp_packet = interpret(text)
        interp_dict = asdict(interp_packet)

        # 2. MIST
        mist_packet = run_mist(
            archetype=interp_dict["archetype"],
            shadow=interp_dict["shadow"],
            sense10=interp_dict["sense10"],
            frame_seed=interp_dict["frame_seed"]
        )

        # 3. Topology
        topology_packet = build_topology(
            mist=mist_packet,
            archetype=interp_dict["archetype"],
            shadow=interp_dict["shadow"]
        )
        topology_dict = asdict(topology_packet)

        # 4. Mask
        expression_packet = apply_mask(
            topology=topology_dict,
            archetype=interp_dict["archetype"],
            shadow=interp_dict["shadow"]
        )

        # 5. Memory update
        self.memory.store_semantic_state(
            archetype=interp_dict["archetype"],
            shadow=interp_dict["shadow"]
        )

        # Optional: auto-store user facts (simple heuristic)
        if "I am" in text or "my name is" in text:
            self.memory.store_fact("user_identity", text)

        return {
            "interpreter": interp_dict,
            "mist": mist_packet,
            "topology": topology_dict,
            "expression": expression_packet,
        }

    # ------------------------------------------------------------
    # PUBLIC METHODS
    # ------------------------------------------------------------

    def step(self, text: str) -> str:
        """
        Execute one reasoning step and return final output.
        """
        packets = self._pipeline(text)
        return packets["expression"].get("final_output", "")

    def debug_step(self, text: str) -> str:
        """
        Execute one step and return full debug dump.
        """
        packets = self._pipeline(text)

        import json

        def block(title, obj):
            bar = "=" * len(title)
            return f"\n{title}\n{bar}\n{json.dumps(obj, indent=2, ensure_ascii=False)}\n"

        out = ""
        out += block("INPUT", text)
        out += block("INTERPRETER", packets["interpreter"])
        out += block("MIST", packets["mist"])
        out += block("TOPOLOGY", packets["topology"])
        out += block("EXPRESSION", packets["expression"])
        out += block("MEMORY", self.memory.export())
        out += block("FINAL OUTPUT", packets["expression"].get("final_output", ""))

        return out

    def remember(self, key: str, value: Any):
        self.memory.store_fact(key, value)

    def recall(self, key: str, default=None):
        return self.memory.get_fact(key, default)

    def reset_memory(self):
        self.memory.reset()

    def export_memory(self) -> Dict[str, Any]:
        return self.memory.export()


# ================================================================
# 3. CLI LOOP
# ================================================================

def main():
    agent = SubitAgentMemory()
    print(f"[{agent.name}] Memory mode active. Type 'exit' to quit.\n")

    while True:
        try:
            user = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting.")
            break

        if user.lower() in {"exit", "quit"}:
            print("Bye.")
            break

        output = agent.step(user)
        print(f"Agent: {output}\n")


if __name__ == "__main__":
    main()
