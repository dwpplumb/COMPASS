"""
Adaptive Axiom-Matrix für COMPASS
Verwendet GPU (cupy), falls verfügbar, sonst CPU (numpy).
"""

from modules.language_model.language_grounding_en import mean_vector, similarity, MODEL
from modules.language_model.axiom_vectors import AXIOM_VECTORS
from typing import Dict

# Fallback import
try:
    import cupy as cp # type: ignore
    use_gpu = True
except ImportError:
    import numpy as cp  # fallback auf NumPy-API-kompatibel
    use_gpu = False


def vector_for_term(term: str):
    if term in MODEL:
        return cp.asarray(MODEL[term])
    return None


def cosine_similarity(a, b):
    dot = cp.dot(a, b)
    norm = cp.linalg.norm(a) * cp.linalg.norm(b)
    return float(dot / norm)


def evaluate_axiom_matrix_adaptive(goal: str) -> Dict[str, float]:
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
                sim = cosine_similarity(goal_gpu, ref_vec)
                scores.append(sim)
        result[axiom] = max(scores) if scores else 0.0

    return result
