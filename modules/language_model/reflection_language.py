"""
Sprachliche Interpretation von Axiommustern im COMPASS-System
"""

def interpret_axiom_profile(axioms: dict) -> str:
    if not axioms:
        return "⚠️ Kein Axiomprofil verfügbar."

    hints = []

    # Schwellwerte
    low = 0.2
    high = 0.6

    if axioms.get("A5", 0.0) < low:
        hints.append("geringe Verbindungsresonanz")
    elif axioms.get("A5", 0.0) > high:
        hints.append("starke Systemverbindung")

    if axioms.get("A6", 0.0) > high:
        hints.append("hohes Restrukturierungspotenzial")
    elif axioms.get("A6", 0.0) < low:
        hints.append("niedrige Destabilisierungswirkung")

    if axioms.get("A7", 0.0) > high:
        hints.append("reflexiv anschlussfähig")
    elif axioms.get("A7", 0.0) < low:
        hints.append("kaum kontextuell rückführbar")

    if axioms.get("A2", 0.0) > high:
        hints.append("transformationsstark")

    if axioms.get("A1", 0.0) < low:
        hints.append("schwach identifizierbar")

    if not hints:
        return "📘 Das Axiomprofil zeigt keine auffällige Struktur."

    return "🧠 Reflexion: " + ", ".join(hints) + "."
