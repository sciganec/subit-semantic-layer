# ================================================================
# SUBIT-64 Debug Agent
# Full introspection of all internal states
# ================================================================
# This agent prints:
#   - Interpreter packet
#   - MIST reasoning packet
#   - Topology packet
#   - Mask/expression packet
#
# It is intended for debugging, demos, and development.
# ================================================================

from dataclasses import asdict
from typing import Dict, Any

from subit_interpreter import interpret
from mist_engine import run_mist
from topology_engine import build_topology
from behavioral_mask import apply_mask


# ================================================================
# 1. FORMATTING UTILITIES
# ================================================================

def header(title: str) -> str:
    bar = "=" * len(title)
    return f"\n{title}\n{bar}\n"

def pretty(obj: Any, indent: int = 2) -> str:
    import json
    return json.dumps(obj, indent=indent, ensure_ascii=False)


# ================================================================
# 2. DEBUG AGENT
# ================================================================

class SubitAgentDebug:
    """
    A fully transparent SUBIT-64 agent.
    Shows every internal packet in the pipeline.
    """

    def __init__(self, name: str = "SUBIT-64 Debug Agent"):
        self.name = name

    def process(self, text: str) -> Dict[str, Any]:
        """
        Run the full pipeline and return all packets.
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

        return {
            "interpreter": interp_dict,
            "mist": mist_packet,
            "topology": topology_dict,
            "expression": expression_packet,
        }

    def debug(self, text: str) -> str:
        """
        Return a human-readable debug dump of all internal states.
        """
        packets = self.process(text)

        out = []
        out.append(header("INPUT"))
        out.append(text)

        out.append(header("INTERPRETER PACKET"))
        out.append(pretty(packets["interpreter"]))

        out.append(header("MIST PACKET"))
        out.append(pretty(packets["mist"]))

        out.append(header("TOPOLOGY PACKET"))
        out.append(pretty(packets["topology"]))

        out.append(header("EXPRESSION PACKET"))
        out.append(pretty(packets["expression"]))

        out.append(header("FINAL OUTPUT"))
        out.append(packets["expression"].get("final_output", ""))

        return "\n".join(out)

    def reply(self, text: str) -> str:
        """
        User-facing method: returns only the final output.
        """
        packets = self.process(text)
        return packets["expression"].get("final_output", "")


# ================================================================
# 3. CLI LOOP
# ================================================================

def main():
    agent = SubitAgentDebug()
    print(f"[{agent.name}] Debug mode active. Type 'exit' to quit.\n")

    while True:
        try:
            user = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting.")
            break

        if user.lower() in {"exit", "quit"}:
            print("Bye.")
            break

        dump = agent.debug(user)
        print(dump)
        print("\n" + "-" * 60 + "\n")


if __name__ == "__main__":
    main()
