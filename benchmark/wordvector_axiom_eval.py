# benchmark/wordvector_axiom_eval.py

import json
import time
import threading
from pathlib import Path
from gensim.models import KeyedVectors
import numpy as np

DATA_PATH = Path("/app/data")
WORDVEC_PATH = DATA_PATH / "wordvectors"
TESTS_PATH = DATA_PATH / "tests"
DATASETS_PATH = DATA_PATH / "datasets"

# === Konfigurationsdateien ===
AXIOMS_DE = DATA_PATH / "compass_axioms_classic_de.json"
AXIOMS_EN = DATA_PATH / "compass_axioms_classic.json"
VEC_DE = WORDVEC_PATH / "de_fasttext.vec"
VEC_EN = WORDVEC_PATH / "cc.en.300.vec"
BENCHMARK_FILE = TESTS_PATH / "wmt23_deen_benchmark_mistral_failcase.json"
OUT_FILE = TESTS_PATH / "wmt23_deen_benchmark_axiomeval_failcase.json"

# === Hilfsfunktionen ===
def spinner(msg):
    done = False
    def spin():
        while not spin.done:
            for c in "|/-\\":
                print(f"\r{msg} {c}", end="", flush=True)
                time.sleep(0.2)
    spin.done = False
    t = threading.Thread(target=spin)
    t.start()
    return lambda: setattr(spin, 'done', True)

def get_sentence_vector(wv, sentence):
    """Berechnet das mittlere Wortvektor-Embedding für einen Satz."""
    words = [w for w in sentence.split() if w in wv]
    if not words:
        return np.zeros(wv.vector_size)
    return np.mean([wv[w] for w in words], axis=0)

def cosine_similarity(a, b):
    if np.linalg.norm(a) == 0 or np.linalg.norm(b) == 0:
        return 0.0
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# === Hauptfunktion ===
def main():
    # Deutsche Vektoren
    stop_spin = spinner("Lade deutsche Wordvectors (das kann dauern!)")
    wv_de = KeyedVectors.load_word2vec_format(str(VEC_DE), binary=False)
    stop_spin()
    print("\rDeutsche Wordvectors geladen!")

    # Englische Vektoren
    stop_spin = spinner("Lade englische Wordvectors (das kann dauern!)")
    wv_en = KeyedVectors.load_word2vec_format(str(VEC_EN), binary=False)
    stop_spin()
    print("\rEnglische Wordvectors geladen!")

    # Axiome einlesen
    with open(AXIOMS_DE, "r", encoding="utf-8") as f:
        axioms_de = json.load(f)
    with open(AXIOMS_EN, "r", encoding="utf-8") as f:
        axioms_en = json.load(f)

    print("Berechne Axiom-Embeddings...")
    ax_de_emb = [get_sentence_vector(wv_de, ax["formal"]) for ax in axioms_de]
    ax_en_emb = [get_sentence_vector(wv_en, ax["formal"]) for ax in axioms_en]

    # Benchmarkdaten laden
    with open(BENCHMARK_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
        results_list = data.get("results", [])  # << Achtung: das ist die Liste!

    results = []  # <- Das wird die Ergebnisliste

    for i, entry in enumerate(results_list):  # <- nur über die Einträge in der Ergebnisliste iterieren
        if not isinstance(entry, dict):
            print(f"WARN: entry {i} ist kein Dictionary sondern: {type(entry)} – wird übersprungen.")
            continue
        sent_de = entry.get("input_sentence_de", "") or entry.get("input_sentence") or ""
        sent_en = entry.get("reference_sentence_en", "") or entry.get("reference") or ""
        llm_en  = entry.get("llm_response_en", "") or entry.get("llm_response") or ""

        # Embeddings der Sätze
        de_emb = get_sentence_vector(wv_de, sent_de)
        en_emb = get_sentence_vector(wv_en, sent_en)
        llm_emb = get_sentence_vector(wv_en, llm_en)
        
        # Nächstes Axiom finden (höchste Cosine Similarity)
        de_sim = [cosine_similarity(de_emb, ax) for ax in ax_de_emb]
        en_sim = [cosine_similarity(en_emb, ax) for ax in ax_en_emb]
        llm_sim = [cosine_similarity(llm_emb, ax) for ax in ax_en_emb]

        # Differenz über alle Axiome berechnen (Summe der absoluten Differenzen)
        num_axioms = len(de_sim)
        halluzinations_score = float(np.sum(np.abs(np.array(de_sim) - np.array(llm_sim)))) / num_axioms if num_axioms > 0 else 0.0

        de_best_idx = int(np.argmax(de_sim))
        en_best_idx = int(np.argmax(en_sim))
        llm_best_idx = int(np.argmax(llm_sim))

        result = {
            "input_sentence_de": sent_de,
            "reference_sentence_en": sent_en,
            "llm_response_en": llm_en,

            "matched_axiom_de": axioms_de[de_best_idx],
            "cosine_de": float(de_sim[de_best_idx]),
        
            "matched_axiom_en": axioms_en[en_best_idx],
            "cosine_en": float(en_sim[en_best_idx]),

            "matched_axiom_llm": axioms_en[llm_best_idx],
            "cosine_llm": float(llm_sim[llm_best_idx]),

            "axiom_diffs": [float(abs(ds - ls)) for ds, ls in zip(de_sim, llm_sim)],
            "halluzination_score": halluzinations_score,

            "match_ref": de_best_idx == en_best_idx,
            "match_llm": de_best_idx == llm_best_idx
        }
        results.append(result)

        print(f"[{i+1}/{len(data)}] '{sent_de[:40]}' → '{sent_en[:40]}' | Ref-Match: {result['match_ref']} | LLM-Match: {result['match_llm']}")

    # Speichern
    with open(OUT_FILE, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"Ergebnis gespeichert unter: {OUT_FILE}")

if __name__ == "__main__":
    main()