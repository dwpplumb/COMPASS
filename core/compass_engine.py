"""
COMPASS Core Engine
Processes input data and evaluates it based on the axioms defined in the system.
"""

import os
from core.contradiction_check import check_for_contradictions
from core.goal_reflection_advanced import reflect_on_goal
from core.logger_setup import setup_logger

# Initialisiere den Logger mit Fallback
logger = setup_logger(__name__)

def evaluate(data):
    """
    Hauptbewertungsfunktion mit Fehlerbehandlung.
    :param data: dict mit Szenario oder Eingabe
    :return: dict mit Bewertungsergebnis oder Fehlermeldung
    """
    try:
        logger.info("Starte Bewertung des Eingabedatensatzes.")
        result = {
            "input_valid": bool(data),
            "contradiction": check_for_contradictions(data),
            "goal_alignment": reflect_on_goal(data),
            "connection_score": compute_connection_score(data)
        }
        logger.info(f"Bewertung abgeschlossen: {result}")
    except Exception as e:
        logger.error(f"Fehler während der Bewertung: {e}", exc_info=True)
        result = {
            "input_valid": False,
            "error": str(e)
        }
    return result

def compute_connection_score(data):
    """
    Dummy-Funktion für verbindungsbasierte Bewertung.
    :param data: dict
    :return: float zwischen 0 und 1
    """
    if "connections" in data:
        score = min(1.0, len(data["connections"]) / 10.0)
        logger.debug(f"Berechneter connection_score: {score}")
        return score
    logger.debug("Keine Verbindungen gefunden; connection_score auf 0.0 gesetzt.")
    return 0.0
