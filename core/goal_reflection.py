"""
Goal Reflection Module
Analyzes alignment of an action or plan with the system's internal goal model.
"""

import numpy as np
import os

try:
    from gensim.models import KeyedVectors

    # Angepasster Pfad zum lokalen Modell
    model_path = os.path.join("modules", "wordvectors", "GoogleNews-vectors-negative300.bin")
    model = None

    if os.path.exists(model_path):
        print(f"🔍 Lade lokales Modell: {model_path}")
        model = KeyedVectors.load_word2vec_format(model_path, binary=True)
    else:
        raise FileNotFoundError

except Exception:
    # Fallback: GloVe-Modell über gensim-downloader laden
    print("⚠️ Lokales Modell nicht verfügbar – Lade GloVe-Fallback-Modell.")
    try:
        from gensim.downloader import load
        model = load("glove-wiki-gigaword-50")
    except Exception as e:
        print(f"❌ GloVe-Fallback konnte nicht geladen werden: {e}")
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

    # Unterstützt Listen und einzelne Begriffe
    if isinstance(user_goal, str) and ',' in user_goal:
        user_terms = [t.strip() for t in user_goal.split(',')]
    else:
        user_terms = user_goal if isinstance(user_goal, list) else [user_goal]

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

    if max_similarity > 0.75:
        return "aligned"
    elif max_similarity > 0.5:
        return "neutral"
    else:
        return "misaligned"
