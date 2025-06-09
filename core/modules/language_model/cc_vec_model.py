# modules/language_model/cc_vec_model.py

import os
import gensim
from gensim.models import KeyedVectors
import numpy as np

MODEL_PATH = "models/cc.de.300.vec"  # Passe ggf. an

# Nur 1x laden
_fasttext_model = None

def load_fasttext_model():
    global _fasttext_model
    if _fasttext_model is None:
        print("⏳ Lade cc.de.300.vec ...")
        _fasttext_model = KeyedVectors.load_word2vec_format(MODEL_PATH, binary=False)
        print("✅ Modell geladen")
    return _fasttext_model

def embed_cc_text(text: str):
    """
    Platzhalterfunktion für kontextbasierte Text-Embeddings (CC-Modell).
    Gibt ein zufälliges Vektor-Array zurück (Simulation).
    """
    np.random.seed(len(text))  # deterministisch für gleiche Eingaben
    return np.random.rand(300)  # Beispiel: 300-dimensionale Vektoren

def text_to_vector(text, model):
    words = [w for w in text.lower().split() if w in model]
    if not words:
        return np.zeros(model.vector_size)
    return np.mean([model[w] for w in words], axis=0)


def analyze_cc_vector_semantics(text):
    model = load_fasttext_model()

    # Vorbereitete Intent-Zentren (dummy-Vektoren zur Demo)
    intent_vectors = {
        "frage": text_to_vector("wie warum wann", model),
        "wunsch": text_to_vector("möchte würde gerne", model),
        "definition": text_to_vector("ist bedeutet meint", model),
        "reflexion": text_to_vector("ich denke glaube verstehe", model),
        "aussage": text_to_vector("ist hat tut", model)
    }

    input_vec = text_to_vector(text, model)
    if np.linalg.norm(input_vec) == 0:
        return {"intent": "unbekannt", "rohtext": text}

    # Ähnlichster Intent
    best_intent = max(intent_vectors.items(), key=lambda item: cosine_similarity(input_vec, item[1]))[0]
    return {"intent": best_intent, "rohtext": text}


def cosine_similarity(vec1, vec2):
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)
    if norm1 == 0 or norm2 == 0:
        return 0.0
    return np.dot(vec1, vec2) / (norm1 * norm2)
