"""
COMPASS Sprachsystem-Modul
Zerlegt Spracheingaben in Bedeutungsbestandteile, liefert semantisch interpretierbare Einheiten zur Axiomverknüpfung.
"""

import os
import logging
from gensim.models import KeyedVectors
from gensim.downloader import load as gensim_load
import re
import numpy as np
import requests
from sklearn.metrics.pairwise import cosine_similarity
from modules.language_model.language_mistral_interface import extract_embeddings

logger = logging.getLogger(__name__)

# Initialisiere semantisches Modell
MODEL = None
MODEL_PATH_DE_TXT = os.path.join("modules", "wordvectors", "de_fasttext.vec")
MODEL_PATH_DE_BIN = os.path.join("modules", "wordvectors", "de_fasttext.kv")

try:
    if os.path.exists(MODEL_PATH_DE_BIN):
        logger.info("Lade deutsches Modell (binär)")
        MODEL = KeyedVectors.load(MODEL_PATH_DE_BIN)
    elif os.path.exists(MODEL_PATH_DE_TXT):
        logger.info("Lade deutsches Modell (Text) – kann dauern...")
        MODEL = KeyedVectors.load_word2vec_format(MODEL_PATH_DE_TXT)
        logger.info("Speichere Modell für schnelleren Zugriff")
        MODEL.save(MODEL_PATH_DE_BIN)
    else:
        logger.warning("Kein deutsches Modell gefunden – lade Fallback GloVe")
        MODEL = gensim_load("glove-wiki-gigaword-50")
except Exception as e:
    logger.error(f"Fehler beim Laden des Sprachmodells: {e}")

def semantic_distance(vec1, vec2):
    if vec1 is None or vec2 is None:
        return 1.0
    vec1 = np.array(vec1).reshape(1, -1)
    vec2 = np.array(vec2).reshape(1, -1)
    similarity = cosine_similarity(vec1, vec2)[0][0]
    return 1.0 - similarity

def generate_semantic_variants(term: str, topn: int = 5):
    if term in MODEL:
        return [w for w, _ in MODEL.most_similar(term, topn=topn)]
    return []

def tokenize(text: str):
    text = text.lower()
    text = re.sub(r"[^a-z0-9äöüß]+", " ", text)
    tokens = text.strip().split()
    return tokens

def mistral_embed_request(text: str):
    url = "http://localhost:11434/api/embeddings"
    payload = {"model": "mistral-embed", "prompt": text}
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        logger.error(f"Fehler bei Mistral-Embedding-Request: {e}")
        return {"embedding": []}

def get_token_vectors(text: str) -> dict:
    response = mistral_embed_request(text)
    return extract_embeddings(response)

def mean_vector(text: str):
    vectors = list(get_token_vectors(text).values())
    for v in vectors:
        if not isinstance(v, (list, np.ndarray)):
            print(f"Unerwartetes Vektorformat: {v}")
    if not vectors:
        return None
    return sum(vectors) / len(vectors)

def similarity(term1: str, term2: str) -> float:
    if term1 in MODEL and term2 in MODEL:
        return MODEL.similarity(term1, term2)
    return 0.0

def get_embedding_vector(text: str):
    return mean_vector(text)

def tokenize_input(text: str) -> list[str]:
    return re.findall(r'\b\w+\b', text.lower())

generate_semantic_vector = mean_vector
