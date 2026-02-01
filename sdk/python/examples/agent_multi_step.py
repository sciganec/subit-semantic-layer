# ================================================================
# SUBIT-64 Multi-Step Agent
# Canonical implementation for multi-turn, multi-step reasoning
# ================================================================
# This agent:
#   - maintains internal SUBIT state across steps
#   - updates archetype, shadow, MIST, topology each turn
#   - supports multi-step task execution
#   - exposes step(), run(), and full debug trace
# ================================================================

from dataclasses import asdict
from typing import Dict, Any, List

from subit_interpreter import interpret
from mist_engine import run_mist
from topology_engine import build_topology
from behavioral_mask import apply_mask


# ================================================================
# 1. MULTI-STEP AGENT
# ================================================================

class SubitAgentMultiStep:
    """
    Multi-step SUBIT-64 agent.
    Maintains internal state across turns.
    """

    def __init__(self, name: str = "SUBIT-64 Multi-Step Agent"):
        self.name = name

        # Persistent internal state
        self.history: List[Dict[str, Any]] = []
        self.last_archetype = None
        self.last_shadow = None
        self.last_topology = None
        self.last_mist = None

    # ------------------------------------------------------------
    # INTERNAL PIPELINE
    # ------------------------------------------------------------

    def _pipeline(self, text: str) -> Dict[str, Any]:
        """
        Run one full SUBIT-64 cycle.
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

        # Update persistent state
        self.last_archetype = interp_dict["archetype"]
        self.last_shadow = interp_dict["shadow"]
        self.last_mist = mist_packet
        self.last_topology = topology_dict

        # Save history
        self.history.append({
            "input": text,
            "interpreter": interp_dict,
            "mist": mist_packet,
            "topology": topology_dict,
            "expression": expression_packet
        })

        return {
            "interpreter": interp_dict,
            "mist": mist_packet,
            "topology": topology_dict,
            "expression": expression_packet
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

    def run(self, steps: List[str]) -> List[str]:
        """
        Execute a sequence of steps.
        Returns list of outputs.
        """
        outputs = []
        for s in steps:
            outputs.append(self.step(s))
        return outputs

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
        out += block("FINAL OUTPUT", packets["expression"].get("final_output", ""))

        return out

    def state(self) -> Dict[str, Any]:
        """
        Return current internal SUBIT state.
        """
        return {
            "archetype": self.last_archetype,
            "shadow": self.last_shadow,
            "mist": self.last_mist,
            "topology": self.last_topology,
            "history_length": len(self.history)
        }


# ================================================================
# 2. CLI LOOP
# ================================================================

def main():
    agent = SubitAgentMultiStep()
    print(f"[{agent.name}] Multi-step mode active. Type 'exit' to quit.\n")

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
