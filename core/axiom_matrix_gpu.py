"""
GPU-gestütztes Axiom-Matrix-Modul für COMPASS
Verwendet CuPy zur parallelen Berechnung semantischer Ähnlichkeit.
"""

import cupy as cp # type: ignore
from COMPASS.modules.language_model.language_grounding_en import mean_vector
from modules.language_model.axiom_vectors import AXIOM_VECTORS
from gensim.models.keyedvectors import KeyedVectors
from typing import Dict

# Zugriff auf das Modell (aus Sprachsystem)
from COMPASS.modules.language_model.language_grounding_en import MODEL


def vector_for_term(term: str):
    if term in MODEL:
        return cp.asarray(MODEL[term])
    return None


def cosine_similarity_gpu(vec_a, vec_b):
    dot = cp.dot(vec_a, vec_b)
    norm = cp.linalg.norm(vec_a) * cp.linalg.norm(vec_b)
    return float(dot / norm)


def evaluate_axiom_matrix_gpu(goal: str) -> Dict[str, float]:
    goal_vec = mean_vector(goal)
    if goal_vec is None:
        return {k: 0.0 for k in AXIOM_VECTORS}

    goal_gpu = cp.asarray(goal_vec)
    result = {}

    for axiom, keywords in AXIOM_VECTORS.items():
        scores = []
        for ref_word in keywords:
            ref_vec = vector_for_term(ref_word)
            if ref_vec is not None:
                sim = cosine_similarity_gpu(goal_gpu, ref_vec)
                scores.append(sim)
        result[axiom] = max(scores) if scores else 0.0

    return result
