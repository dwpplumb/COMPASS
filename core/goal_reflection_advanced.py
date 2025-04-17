"""
Erweitertes Reflexionsmodul für COMPASS
Analysiert die Ausrichtung eines Ziels mit dem internen Zielmodell des Systems und führt eine Meta-Analyse durch.
"""

import os
from gensim.models import KeyedVectors
from core.logger_setup import setup_logger

# Initialisiere den Logger
logger = setup_logger(__name__, log_file='logs/compass.log')

# Lade das Wortvektormodell
model_path = os.path.join("modules", "wordvectors", "GoogleNews-vectors-negative300.bin")
model = None

try:
    if os.path.exists(model_path):
        logger.info(f"Lade lokales Modell: {model_path}")
        model = KeyedVectors.load_word2vec_format(model_path, binary=True)
    else:
        raise FileNotFoundError(f"Modellpfad nicht gefunden: {model_path}")
except Exception as e:
    logger.error(f"Fehler beim Laden des Modells: {e}")
    model = None

def reflect_on_goal(data):
    """
    Führt eine erweiterte Zielreflexion mit Meta-Analyse durch.
    :param data: dict mit dem Schlüssel 'goal'
    :return: dict mit Bewertung und Meta-Analyse
    """
    system_goals = ["connect", "stabilize", "harmonize"]
    user_goal = data.get("goal")

    if not user_goal or model is None:
        logger.warning("Kein Ziel angegeben oder Modell nicht verfügbar.")
        return {
            "alignment": "neutral",
            "meta_analysis": {
                "reason": "Kein Ziel angegeben oder Modell nicht verfügbar.",
                "similarity": None,
                "goal_type": None,
                "emotional_connotation": None
            }
        }

    # Unterstützt Listen und einzelne Begriffe
    if isinstance(user_goal, str) and ',' in user_goal:
        user_terms = [t.strip() for t in user_goal.split(',')]
    else:
        user_terms = user_goal if isinstance(user_goal, list) else [user_goal]

    similarities = []
    for user_term in user_terms:
        if user_term in model:
            term_similarities = [model.similarity(user_term, goal) for goal in system_goals if goal in model]
            if term_similarities:
                max_sim = max(term_similarities)
                similarities.append(max_sim)
                logger.debug(f"Ähnlichkeit für '{user_term}': {max_sim}")
        else:
            logger.debug(f"Begriff '{user_term}' nicht im Modell gefunden.")

    if not similarities:
        logger.info("Keine semantische Ähnlichkeit zu Systemzielen gefunden.")
        return {
            "alignment": "neutral",
            "meta_analysis": {
                "reason": "Keine semantische Ähnlichkeit zu Systemzielen gefunden.",
                "similarity": None,
                "goal_type": None,
                "emotional_connotation": None
            }
        }

    max_similarity = max(similarities)

    # Bestimme die Ausrichtung basierend auf der maximalen Ähnlichkeit
    if max_similarity > 0.75:
        alignment = "aligned"
    elif max_similarity > 0.5:
        alignment = "neutral"
    else:
        alignment = "misaligned"

    # Führe eine einfache Meta-Analyse durch
    goal_type = "unknown"
    emotional_connotation = "neutral"

    # Beispielhafte Klassifizierung basierend auf Schlüsselwörtern
    if any(term in ["connect", "unify", "collaborate"] for term in user_terms):
        goal_type = "social"
        emotional_connotation = "positive"
    elif any(term in ["destroy", "interrupt", "disconnect"] for term in user_terms):
        goal_type = "disruptive"
        emotional_connotation = "negative"
    elif any(term in ["stabilize", "organize", "structure"] for term in user_terms):
        goal_type = "structural"
        emotional_connotation = "neutral"

    result = {
        "alignment": alignment,
        "meta_analysis": {
            "reason": f"Maximale Ähnlichkeit zu Systemzielen: {max_similarity:.2f}",
            "similarity": max_similarity,
            "goal_type": goal_type,
            "emotional_connotation": emotional_connotation
        }
    }

    logger.info(f"Reflexionsergebnis: {result}")
    return result
