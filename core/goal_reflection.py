"""
Goal Reflection Module
Analyzes alignment of an action or plan with the system's internal goal model.
"""

import numpy as np
import os

try:
    # Lokaler Modus mit großem Word2Vec-Modell (optional)
    from gensim.models import KeyedVectors
    model_path = 'path_to_model/GoogleNews-vectors-negative300.bin'
    model = None
    if os.path.exists(model_path):
        print(f"🔍 Lade lokales Modell: {model_path}")
        model = KeyedVectors.load_word2vec_format(model_path, binary=True)
    else:
        raise FileNotFoundError

except Exception:
    # Fallback für GitHub Actions oder wenn Modell fehlt
    print("⚠️ Lokales Modell nicht verfügbar – Lade kleines GloVe-Modell als Fallback.")
    from gensim.downloader import load
    try:
        model = load("glove-wiki-gigaword-50")
    except Exception as e:
        print(f"❌ Konnte GloVe-Modell nicht laden: {e}")
        model = None


def reflect_on_goal(data):
    """
    Erweiterte Zielreflexionslogik mit semantischer Analyse.
    :param data: dict
    :return: str – "aligned", "neutral" oder "misaligned"
    """
    system_goals = ["connect", "stabilize", "harmonize"]
    user_goal = data.get("goal")

    if not user_goal or model is None:
        return "neutral"

    # Wenn Liste von Zielen gegeben ist
    if isinstance(user_goal, list):
        user_terms = user_goal
    else:
        user_terms = [user_goal]

    similarities = []
    for user_term in user_terms:
        if user_term in model:
            for goal in system_goals:
                if goal in model:
                    similarity = model.similarity(user_term, goal)
                    similarities.append(similarity)

    if not similarities:
        return "neutral"

    max_similarity = max(similarities)

    if max_similarity > 0.7:
        return "aligned"
    elif max_similarity > 0.4:
        return "neutral"
    else:
        return "misaligned"

