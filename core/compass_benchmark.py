# core/compass_benchmark.py

import json
import re
import string
from typing import Dict, Any

def load_compass_axioms(path: str = "data/compass_axioms_classic.json") -> Dict[str, Any]:
    """
    Lädt die COMPASS-Axiome aus einer JSON-Datei.
    Gibt ein Mapping {Axiom-ID: Axiom-Objekt} zurück.
    """
    with open(path, "r", encoding="utf-8") as f:
        axioms = json.load(f)
    axiom_map = {ax["id"]: ax for ax in axioms if ax.get("active", True)}
    return axiom_map

def compass_analyse_text(text: str, axiom_map: Dict[str, Any], min_score: float = 0.01) -> Dict[str, Any]:
    """
    Analysiert einen Text bezüglich der semantic_vectors aller Axiome.
    Gibt Scores, Top-Axiome, Formulierungen und Zusammenfassung zurück.
    """
    cleaned_text = text.lower().translate(str.maketrans("", "", string.punctuation))
    scores = {}
    for ax_id, ax in axiom_map.items():
        count = sum(
            1
            for word in ax["semantic_vector"]
            if re.search(rf"\b{re.escape(word.lower())}\b", cleaned_text)
        )
        norm_score = count / max(1, len(ax["semantic_vector"]))
        if norm_score > min_score:
            scores[ax_id] = norm_score

    if scores:
        ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        top_ids = [ax_id for ax_id, _ in ranked[:2]]
        summary = f"Die Antwort bezieht sich vor allem auf: {', '.join(axiom_map[a]['title'] for a in top_ids)}."
        formals = [axiom_map[a]['formal'] for a in top_ids]
    else:
        summary = "Keine Axiome wurden zuverlässig erkannt."
        top_ids = []
        formals = []

    return {
        "axiom_scores": scores,
        "top_axioms": top_ids,
        "axiom_formals": formals,
        "summary": summary
    }

# Reflexion: Erfüllt A1C (wirksame semantische Struktur), A2C (funktionale Veränderung),
# A5C (Kopplung API<->Analyse), A7C (Selbstauskunft zur Erkennung von Zielabweichungen).
