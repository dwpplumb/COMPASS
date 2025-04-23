"""
COMPASS Intent-Extractor
Zerlegt einen Satz in Zielabsicht, emotionale Färbung und axiomatische Bedeutung
"""

from core.sentence_classifier import classify_sentence
from modules.language_model.language_grounding import mean_vector
from modules.language_model.axiom_vectors import AXIOM_VECTORS
from modules.language_model.reflection_language import interpret_axiom_profile


def extract_intent_features(sentence: str) -> dict:
    """
    Analysiert semantische Intention eines Satzes: Zieltyp, Axiomprofil, Satzklasse, Reflexionsstruktur.
    :param sentence: Satz als String
    :return: Dict mit Zielstruktur
    """
    # Satzklassifikation (frage, aussage, aufforderung etc.)
    satztyp = classify_sentence(sentence)

    # Semantisches Profil erzeugen (mittlerer Vektor + Axiomzuordnung)
    vec = mean_vector(sentence)
    if vec is None:
        axiom_profile = {ax: 0.0 for ax in AXIOM_VECTORS.keys()}
    else:
        from core.axiom_matrix import evaluate_axiom_matrix
        axiom_profile = evaluate_axiom_matrix(sentence)

    # Reflexive Interpretation (semantisch generiert)
    reflexion = interpret_axiom_profile(axiom_profile)

    return {
        "satztyp": satztyp,
        "axiome": axiom_profile,
        "reflexion": reflexion
    }


# Beispiel:
if __name__ == "__main__":
    testsaetze = [
        "Wir sollten miteinander sprechen.",
        "Zerstöre die Verbindung.",
        "Was ist Bewusstsein?",
        "Ich wünsche mir mehr Klarheit im System.",
        "Ein Axiom ist ein logischer Grundsatz."
    ]

    for s in testsaetze:
        result = extract_intent_features(s)
        print(f"\n🔍 '{s}'")
        print(f"Typ: {result['satztyp']}")
        print(f"Reflexion: {result['reflexion']}")
        print("Axiome:")
        for ax, val in result['axiome'].items():
            print(f"  {ax}: {round(val, 2)}")
