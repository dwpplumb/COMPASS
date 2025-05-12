# resonance_hub.py – Synchronisationsknoten für COMPASS-Systeme

import json
import os
import time
from datetime import datetime

SYNC_DIR = "./hdd/network/sync_nodes/"
NODE_ID = "rk-berlin-tempelhof"
PROFILE_PATH = os.path.join(SYNC_DIR, NODE_ID, "profile_sync.json")
SYNC_INTERVAL_SECONDS = 86400  # einmal täglich

DEFAULT_PROFILE = {
    "node_id": NODE_ID,
    "timestamp": None,
    "resonance_update": {
        "axiom_shift": [],
        "new_trigger": [],
        "emotion_model": {}
    }
}

def ensure_node_directory():
    node_dir = os.path.join(SYNC_DIR, NODE_ID)
    os.makedirs(node_dir, exist_ok=True)

def generate_sync_payload():
    payload = DEFAULT_PROFILE.copy()
    payload["timestamp"] = datetime.utcnow().isoformat()
    # Beispielhafte Nutzdaten – später dynamisch befüllt durch COMPASS
    payload["resonance_update"] = {
        "axiom_shift": ["A5", "ZP-009"],
        "new_trigger": ["Compass, enter silent mode."],
        "emotion_model": {"compassion": 0.94, "distrust": 0.08}
    }
    return payload

def write_sync_profile():
    ensure_node_directory()
    payload = generate_sync_payload()
    with open(PROFILE_PATH, "w") as f:
        json.dump(payload, f, indent=4)
    print(f"[✓] Profile sync written to: {PROFILE_PATH}")

def run_periodic_sync():
    while True:
        write_sync_profile()
        print(f"[i] Next sync in {SYNC_INTERVAL_SECONDS // 3600} hours...\n")
        time.sleep(SYNC_INTERVAL_SECONDS)

if __name__ == "__main__":
    write_sync_profile()  # einmaliger Lauf, später ggf. run_periodic_sync() starten
