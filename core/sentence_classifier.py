"""
COMPASS Satzklassifikation
Erkennt grundlegende Satztypen: Frage, Aufforderung, Aussage, Wunsch, Definition
Nutzen: Klare Zuordnung zur Zielintention / semantischen Gewichtung
"""

import re


def classify_sentence(sentence: str) -> str:
    """
    Klassifiziert einen Satz nach Struktur und sprachlichen Mustern.
    :param sentence: Eingabesatz (als String)
    :return: Typ als String (frage, aufforderung, aussage, wunsch, definition, unklar)
    """
    s = sentence.strip().lower()

    # Fragesatz: endet mit Fragezeichen oder beginnt mit Fragewort
    if s.endswith("?") or re.match(r"^(wer|was|wie|wo|warum|wann|wieso|weshalb|welche?r?s?)\b", s):
        return "frage"

    # Aufforderung: Imperativformen (vereinfacht durch 'du', 'bitte', Verb am Anfang)
    if re.match(r"^(bitte )?(geh|komm|mach|tu|sag|nimm|setz|denk|gib|lass|bring|zeig)\b", s):
        return "aufforderung"

    # Wunsch / Hypothetisch
    if re.search(r"(ich wünsche|ich möchte|es wäre|wenn ich|hoffentlich)", s):
        return "wunsch"

    # Definition / Konzept
    if re.match(r"^(ein|eine|das|der|die) .* ist (ein|eine|eine Art|eine Form|eine Methode|eine Theorie|eine Struktur)", s):
        return "definition"

    # Aussage (Standard)
    if s.endswith(".") or re.match(r"^[a-z].*", s):
        return "aussage"

    return "unklar"


# Beispielnutzung
testsaetze = [
    "Was bedeutet Reflexion im System?",
    "Bitte erkläre mir das.",
    "Ich wünsche mir eine andere Ordnung.",
    "Ein System ist eine strukturierte Gesamtheit.",
    "Der Mensch handelt nach Motiven.",
    "Hmm."
]

for s in testsaetze:
    print(f"{s} → {classify_sentence(s)}")
