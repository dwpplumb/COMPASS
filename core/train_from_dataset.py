"""
train_from_dataset.py

Dieses Modul analysiert strukturierte COMPASS-Trainingsdaten im JSONL-Format
und berechnet aus Axiom-Aktivierungen und Erfolgseinschätzungen
gewichtete Profile für die Reaktionslogik des Metacortex-Systems.
"""

import json
from collections import defaultdict
from pathlib import Path

# Pfade
DATA_PATH = Path("/mnt/data/training_data.jsonl")
OUTPUT_PATH = Path("/mnt/data/axiom_weights.json")

# Initialisierung
axiom_counts = defaultdict(int)
axiom_scores = defaultdict(float)

# Trainingsdaten einlesen
with DATA_PATH.open("r", encoding="utf-8") as f:
    for line in f:
        try:
            entry = json.loads(line)
            axiome = entry.get("erkannte_axiome", [])
            bewertung = float(entry.get("bewertung", 0.0))
            for ax in axiome:
                axiom_counts[ax] += 1
                axiom_scores[ax] += bewertung
        except json.JSONDecodeError:
            print("Fehlerhafte Zeile übersprungen:", line[:80])

# Gewichtung berechnen
axiom_weights = {
    ax: round(axiom_scores[ax] / axiom_counts[ax], 3)
    for ax in axiom_counts
}

# Ergebnisse speichern
with OUTPUT_PATH.open("w", encoding="utf-8") as f:
    json.dump(axiom_weights, f, indent=2, ensure_ascii=False)

print("Axiomgewichtung abgeschlossen. Gespeichert unter:", OUTPUT_PATH)
