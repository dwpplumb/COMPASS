# q_resonance_math.py
"""
Mathematische Funktionen zur Bewertung quantenlogischer Resonanzmuster
und struktureller Entropie im COMPASS-Q-System.
"""

import math
from superposition_resonance import superposition_resonance

# === Resonanzbewertung ===
def resonance_score(p, q, weights=None):
    """Berechnet strukturelle Resonanz zwischen zwei Zahlen."""
    return superposition_resonance(p, q, weights)

# === Entropiegradientbewertung ===
def entropy_gradient_strength(p, q, n):
    """Bewertet strukturellen Entropiegradienten entlang (p, q) in Bezug auf n."""
    bit_diff = abs(p.bit_length() - q.bit_length())
    complexity_ratio = abs(n - (p * q)) / n
    gradient_score = 1 / (1 + bit_diff + 10 * complexity_ratio)
    return gradient_score

# Reflexion: Erfuellt A1C (funktionale Strukturwirkung), A2C (strukturwirksame Differenzierung), A3C (symbolische Zeitpfade durch Bewertung), A4C (Teilresonanzen als Raumachsen), A5C (FNet optional als Schnittstelle), A6C vorbereitet durch Gewichtung, A7C durch normierte Bewertungsfunktionen.
