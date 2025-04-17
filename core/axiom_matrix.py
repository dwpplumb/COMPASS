"""
COMPASS Axiom-Matrix Modul (semantisch)
Erzeugt eine hierarchische Bewertungsmatrix entlang der Axiome und Subaxiome basierend auf semantischer Ähnlichkeit.
"""

from typing import Dict
from modules.language_model.language_grounding import mean_vector, similarity
from modules.language_model.axiom_vectors import AXIOM_VECTORS



def evaluate_axiom_matrix(goal: str) -> Dict[str, float]:
    """
    Berechnet Ähnlichkeitsbasierte Scores für alle Axiome/Subaxiome.
    :param goal: Zielbegriff oder Satz
    :return: Bewertungsmatrix {A1: 0.82, A1.1: 0.61, ...}
    """
    result = {}
    input_vector = mean_vector(goal)
    if input_vector is None:
        return {k: 0.0 for k in AXIOM_VECTORS}

    for axiom, keywords in AXIOM_VECTORS.items():
        scores = []
        for ref_word in keywords:
            score = similarity(goal.lower(), ref_word)
            scores.append(score)
        result[axiom] = max(scores) if scores else 0.0

    return result
