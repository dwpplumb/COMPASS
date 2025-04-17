"""
COMPASS Axiom-Matrix Modul
Erzeugt eine hierarchische Bewertungsmatrix entlang der Axiome und Subaxiome für ein gegebenes Ziel.
"""

from typing import Dict


def evaluate_axiom_matrix(goal: str) -> Dict[str, float]:
    """
    Gibt eine Axiomstruktur mit Bewertungen für ein Zielbegriff zurück.
    Derzeit: statische Regelbasis.
    :param goal: Zielbegriff (z. B. "rebuild")
    :return: Dict mit Bewertungen pro (Sub-)Axiom
    """
    g = goal.lower().strip()

    matrix = {
        # Axiom 1: Existenz durch Unterscheidung
        "A1": 0.4 if g in ["rebuild", "reorganize"] else 0.7,
        "A1.1": 0.5 if g in ["rebuild"] else 0.3,
        "A1.2": 0.6 if g in ["rebuild"] else 0.2,

        # Axiom 2: Zustandsveränderung
        "A2": 0.9 if g in ["rebuild", "transform"] else 0.5,
        "A2.1": 0.7 if g in ["rebuild"] else 0.4,
        "A2.2": 0.6 if g in ["rebuild"] else 0.3,

        # Axiom 3: Zeitliche Bewertung
        "A3": 0.5,
        "A3.1": 0.6,
        "A3.2": 0.4,

        # Axiom 4: Raumbezug / Relation
        "A4": 0.3,
        "A4.1": 0.2,
        "A4.2": 0.4,

        # Axiom 5: Verbindungswert
        "A5": 0.6 if g in ["unify"] else 0.4,
        "A5.1": 0.3,
        "A5.2": 0.5,

        # Axiom 6: Instabilität
        "A6": 0.85 if g in ["rebuild"] else 0.4,
        "A6.1": 0.8,
        "A6.2": 0.45,

        # Axiom 7: Reflexion & Kontextübertrag
        "A7": 0.55,
        "A7.1": 0.4,
        "A7.2": 0.3,
        "A7.3": 0.6,
    }

    return matrix
