"""
COMPASS Self-Check Tool
Verifies the structure and readiness of a COMPASS instance based on file presence and structure.
"""

import os
import json

BASE_PATH = "."  # Assumes script is run from root of COMPASS repo

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
    results = {}
    for path in REQUIRED_PATHS:
        full_path = os.path.join(BASE_PATH, path)
        results[path] = os.path.exists(full_path)
    return results

def summarize_results(results):
    print("COMPASS Node Self-Check Summary:\n")
    missing = []
    for path, exists in results.items():
        status = "✅" if exists else "❌"
        print(f"{status} {path}")
        if not exists:
            missing.append(path)
    print(f"\nTotal: {len(results)} files checked")
    print(f"Missing: {len(missing)}")
    return missing

if __name__ == "__main__":
    results = check_files()
    summarize_results(results)
