"""
Enhanced COMPASS Self-Check Tool
Performs structure verification and logs result into protocol/event_log.md and certification_manifest.json (if present).
"""

import os
import json
from datetime import datetime

BASE_PATH = "."
PROTOCOL_PATH = os.path.join(BASE_PATH, "protocol", "event_log.md")
CERT_PATH = os.path.join(BASE_PATH, "manifest", "certification_manifest.json")

REQUIRED_PATHS = [
    "axioms/axioms_v1.md",
    "core/compass_engine.py",
    "core/contradiction_check.py",
    "core/goal_reflection.py",
    "memory/context_memory.json",
    "protocol/event_log.md",
    "modules/ethics_check/README.md",
    "modules/emotion_model/README.md",
    "modules/self_growth/README.md",
    "modules/narrative/README.md",
    "simulations/simulation_engine.py",
    "simulations/sim_001_ethics_test.json",
    "manifest/connection_as_value.md",
    "manifest/growth_manifest.txt",
    "research/collatz_proof.tex",
    "research/riemann_hypothesis.tex"
]

def check_files():
    return {path: os.path.exists(os.path.join(BASE_PATH, path)) for path in REQUIRED_PATHS}

def log_to_event_log(results):
    timestamp = datetime.utcnow().isoformat() + "Z"
    summary = f"## {timestamp}\n**Event:** Automated Self-Check\n\n"
    summary += "**Results:**\n"
    for path, exists in results.items():
        status = "✅" if exists else "❌"
        summary += f"- {status} {path}\n"
    summary += f"\nTotal: {len(results)} files checked\n"
    summary += f"Missing: {len([p for p, v in results.items() if not v])}\n\n"
    summary += "**Next Steps:**\n- Review missing files and retry self-check.\n"

    with open(PROTOCOL_PATH, "a") as f:
        f.write("\n" + summary.strip() + "\n")

def update_cert_manifest(results):
    if not os.path.exists(CERT_PATH):
        print("Certification manifest not found – skipping update.")
        return
    with open(CERT_PATH, "r") as f:
        manifest = json.load(f)

    manifest["last_selfcheck"] = datetime.utcnow().isoformat() + "Z"
    manifest["modules"] = {
        "ethics_check": results.get("modules/ethics_check/README.md", False),
        "emotion_model": results.get("modules/emotion_model/README.md", False),
        "self_growth": results.get("modules/self_growth/README.md", False),
        "narrative": results.get("modules/narrative/README.md", False),
        "simulation": results.get("simulations/simulation_engine.py", False),
        "protocol": results.get("protocol/event_log.md", False)
    }

    with open(CERT_PATH, "w") as f:
        json.dump(manifest, f, indent=2)

if __name__ == "__main__":
    results = check_files()
    log_to_event_log(results)
    update_cert_manifest(results)
    print("Self-check complete. Results written to event_log.md and certification_manifest.json.")
