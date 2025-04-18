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
