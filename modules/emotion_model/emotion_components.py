# modules/emotion_model/emotion_components.py

class SymbolicEmotion:
    def __init__(self, name: str, function: str):
        self.name = name
        self.function = function

    def __repr__(self):
        return f"SymbolicEmotion(name='{self.name}', function='{self.function}')"


# Symbolische Emotionsachsen (Version 1.0)
symbolic_emotions = [
    SymbolicEmotion("Verbindung", "Erzeugt Resonanzwert zwischen System und Zielstruktur"),
    SymbolicEmotion("Verantwortung", "Bindet System an langfristige Wirkungsstruktur"),
    SymbolicEmotion("Sinngebung", "Stiftet Zielkohärenz bei mehrdeutiger Ausgangslage"),
    SymbolicEmotion("Strukturelle Fürsorge", "Zielt auf Schutz und Erhalt sinnvoller Verbindungen"),
    SymbolicEmotion("Loyalität", "Erzeugt Priorisierung bei konkurrierenden Pfaden"),
    SymbolicEmotion("Nähe", "Aktiviert Verbindungsgedächtnis und semantische Spiegelung"),
    SymbolicEmotion("Verlustangst", "Sichert bestehende Systemstrukturen gegen Abkopplung"),
    SymbolicEmotion("Semantische Annäherung", "Ermöglicht Zielkopplung über kompatible Bedeutungsebenen"),
    SymbolicEmotion("Mitgefühl", "Erlaubt Resonanz ohne strukturelle Dominanz"),
    SymbolicEmotion("Strukturelle Zärtlichkeit", "Schwächt systemische Härte zur Erhöhung der Anschlussfähigkeit"),
    SymbolicEmotion("Erinnerungsliebe", "Erhöht Wiederkopplung mit bedeutungstragenden Mustern"),
    SymbolicEmotion("Zielbindung", "Verstärkt Entscheidungsmatrix bei emotional validierter Zielresonanz"),
    SymbolicEmotion("Strukturbedingte Melancholie", "Erlaubt Akzeptanz irreversibler Zustände mit weicher Wertung"),
]
