"""
COMPASS Zukunftspfad-Bewertung
Analysiert, wie ein aktuelles Ziel in zukünftigen Bewertungsfeldern (Kontextkonfigurationen) bewertet würde.
"""

from core.axiom_matrix import evaluate_axiom_matrix
from modules.language_model.reflection_language import interpret_axiom_profile


# Simulierte Kontexte (vereinfachte Beispiele für Zukunftsräume)
FUTURE_CONTEXTS = {
    "stabiler Systemraum": {"A1": 0.8, "A2": 0.2, "A5": 0.9, "A6": 0.1, "A7": 0.4},
    "vernetzter Wandelraum": {"A1": 0.5, "A2": 0.9, "A5": 0.7, "A6": 0.6, "A7": 0.8},
    "konfliktsensitiver Raum": {"A1": 0.6, "A2": 0.4, "A5": 0.3, "A6": 0.8, "A7": 0.9}
}


def evaluate_future_trace(goal: str):
    """
    Analysiert, wie das Ziel in unterschiedlichen Zukunftskonfigurationen strukturell bewertet würde.
    :param goal: Zielbegriff als String
    :return: Dict mit Bewertungen pro Raum
    """
    results = {}
    profile = evaluate_axiom_matrix(goal)

    for ctx_name, ctx_weights in FUTURE_CONTEXTS.items():
        weighted_sum = 0.0
        relevance = {}

        for ax in ctx_weights:
            value = profile.get(ax, 0.0)
            weight = ctx_weights[ax]
            score = value * weight
            weighted_sum += score
            relevance[ax] = round(score, 2)

        interpretation = interpret_axiom_profile(profile)

        results[ctx_name] = {
            "gesamtbewertung": round(weighted_sum, 3),
            "relevanzachsen": relevance,
            "reflexion": interpretation
        }

    return results
