"""
COMPASS Sprachsystem-Modul
Zerlegt Spracheingaben in Bedeutungsbestandteile, liefert semantisch interpretierbare Einheiten zur Axiomverknüpfung.
"""

import os
import logging
from gensim.models import KeyedVectors
from gensim.downloader import load as gensim_load
import re

logger = logging.getLogger(__name__)

# Initialisiere semantisches Modell
MODEL = None
MODEL_PATH = os.path.join("modules", "wordvectors", "GoogleNews-vectors-negative300.bin")

try:
    if os.path.exists(MODEL_PATH):
        logger.info("Lade GoogleNews Word2Vec-Modell lokal")
        MODEL = KeyedVectors.load_word2vec_format(MODEL_PATH, binary=True)
    else:
        logger.warning("Kein lokales Modell gefunden, nutze GloVe 50")
        MODEL = gensim_load("glove-wiki-gigaword-50")
except Exception as e:
    logger.error(f"Fehler beim Laden des Sprachmodells: {e}")


def tokenize(text: str):
    """Einfache Tokenisierung + Normalisierung (ohne externe NLP-Abhängigkeit)."""
    text = text.lower()
    text = re.sub(r"[^a-z0-9äöüß]+", " ", text)
    tokens = text.strip().split()
    return tokens


def get_token_vectors(text: str):
    """Gibt Vektor-Embedding für jedes Token zurück."""
    tokens = tokenize(text)
    vectors = {t: MODEL[t] for t in tokens if t in MODEL}
    return vectors


def mean_vector(text: str):
    """Berechnet den Mittelwert der Vektoren aller erkannten Tokens."""
    vectors = list(get_token_vectors(text).values())
    if not vectors:
        return None
    return sum(vectors) / len(vectors)


def similarity(term1: str, term2: str) -> float:
    """Berechnet die semantische Ähnlichkeit zweier Begriffe."""
    if term1 in MODEL and term2 in MODEL:
        return MODEL.similarity(term1, term2)
    return 0.0
