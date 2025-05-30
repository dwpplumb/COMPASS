AXIOMS = [
    "Existenz", "Veränderung", "Zeit", "Raum", "Verbindung", "Rekonfiguration", "Reflexion"
]

def evaluate_text(text):
    matches = [axiom for axiom in AXIOMS if axiom.lower() in text.lower()]
    if matches:
        return True, f"Begriffe erkannt: {', '.join(matches)}"
    else:
        return False, "Keine axiomatischen Begriffe erkannt"
