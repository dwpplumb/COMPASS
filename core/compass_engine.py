"""
COMPASS Core Engine
Processes input data and evaluates it based on the axioms defined in the system.
"""

from .contradiction_check import check_for_contradictions
from .goal_reflection import reflect_on_goal

def evaluate(data):
    """
    Hauptbewertungsfunktion mit Fehlerbehandlung.
    :param data: dict mit Szenario oder Eingabe
    :return: dict mit Bewertungsergebnis oder Fehlermeldung
    """
    try:
        result = {
            "input_valid": bool(data),
            "contradiction": check_for_contradictions(data),
            "goal_alignment": reflect_on_goal(data),
            "connection_score": compute_connection_score(data)
        }
    except Exception as e:
        result = {
            "input_valid": False,
            "error": str(e)
        }
    return result

def compute_connection_score(data):
    """
    Dummy function for connection-based valuation.
    :param data: dict
    :return: float between 0 and 1
    """
    if "connections" in data:
        return min(1.0, len(data["connections"]) / 10.0)
    return 0.0
