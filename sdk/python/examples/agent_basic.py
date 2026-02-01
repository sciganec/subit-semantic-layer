# ================================================================
# SUBIT-64 Basic Agent
# Canonical minimal runtime wiring
# ================================================================
# Pipeline:
#   1. SUBIT Interpreter      (text -> semantic init packet)
#   2. MIST Reasoning Engine  (init -> cognitive packet)
#   3. Topology Engine        (cognitive -> semantic topology)
#   4. Behavioral Mask        (topology -> final expression)
#
# This is the simplest usable SUBIT-64 agent.
# ================================================================

from dataclasses import asdict
from typing import Dict, Any

from subit_interpreter import interpret
from mist_engine import run_mist
from topology_engine import build_topology
from behavioral_mask import apply_mask


# ================================================================
# 1. CORE AGENT
# ================================================================

class SubitAgentBasic:
    """
    Minimal SUBIT-64 agent:
    - deterministic pipeline
    - no external tools
    - single active archetype per turn (from interpreter)
    """

    def __init__(self, name: str = "SUBIT-64 Basic Agent"):
        self.name = name

    def process(self, text: str) -> Dict[str, Any]:
        """
        Run the full SUBIT-64 pipeline and return all internal packets.
        Useful for debugging and inspection.
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

        # 4. Mask / Expression
        expression_packet = apply_mask(
            topology=topology_dict,
            archetype=interp_dict["archetype"],
            shadow=interp_dict["shadow"]
        )

        return {
            "interpreter": interp_dict,
            "mist": mist_packet,
            "topology": topology_dict,
            "expression": expression_packet,
        }

    def reply(self, text: str) -> str:
        """
        User-facing method: returns only the final output string.
        """
        packets = self.process(text)
        expr = packets["expression"]
        # assuming apply_mask returns dict with "final_output"
        return expr.get("final_output", "")


# ================================================================
# 2. CLI LOOP (MANUAL TEST)
# ================================================================

def main():
    agent = SubitAgentBasic()
    print(f"[{agent.name}] ready. Type 'exit' to quit.\n")

    while True:
        try:
            user = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting.")
            break

        if user.lower() in {"exit", "quit"}:
            print("Bye.")
            break

        answer = agent.reply(user)
        print(f"Agent: {answer}\n")


if __name__ == "__main__":
    main()
