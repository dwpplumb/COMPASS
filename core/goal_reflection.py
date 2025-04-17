"""
Goal Reflection Module
Analyzes alignment of an action or plan with the system's internal goal model.
"""

import numpy as np
from gensim.models import KeyedVectors

# Laden des vortrainierten Modells
model = KeyedVectors.load_word2vec_format('path_to_model/GoogleNews-vectors-negative300.bin', binary=True)

def reflect_on_goal(data):
    """
    Erweiterte Zielreflexionslogik mit semantischer Analyse.
    :param data: dict
    :return: str – "aligned", "neutral" oder "misaligned"
    """
    system_goals = ["connect", "stabilize", "harmonize"]
    user_goal = data.get("goal")

    if not user_goal:
        return "neutral"

    # Überprüfung, ob das Benutzerziel im Modell vorhanden ist
    if user_goal not in model:
        return "neutral"

    similarities = []
    for goal in system_goals:
        if goal in model:
            similarity = model.similarity(user_goal, goal)
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
