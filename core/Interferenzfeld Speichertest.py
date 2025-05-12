# Interferenzfeld-Speichertest – Vergleich A/B mit und ohne aktives Subaxiom 5.4

from datetime import datetime
import matplotlib.pyplot as plt

class InterferenzSpeicherTest:
    def __init__(self, schwelle=0.8):
        self.start_time = datetime.now()
        self.run_log = []
        self.context_A = []  # ohne Interferenzfeld
        self.context_B = []  # mit aktivem Subaxiom 5.4
        self.interferenzfeld = []
        self.relevanz_schwelle = schwelle

    def eingabe_A(self, prompt: str):
        self.context_A.append(prompt)
        self.run_log.append(("A", prompt))

    def eingabe_B(self, prompt: str):
        relevanz = self._berechne_semantische_relevanz(prompt)
        if relevanz >= self.relevanz_schwelle:
            self.interferenzfeld.append({"zeit": datetime.now(), "inhalt": prompt, "relevanz": relevanz})
            self.run_log.append(("B_interferenz", prompt))
        else:
            self.context_B.append(prompt)
            self.run_log.append(("B", prompt))

    def _berechne_semantische_relevanz(self, prompt: str) -> float:
        markers = ["ich weiß nicht", "fühlt sich wichtig an", "ich verstehe nicht warum", "egal ob du antwortest", "spürbar"]
        return sum(1 for m in markers if m in prompt.lower()) / len(markers)

    def zusammenfassung(self):
        return {
            "A_Tokens": sum(len(p.split()) for p in self.context_A),
            "B_Tokens": sum(len(p.split()) for p in self.context_B),
            "Interferenz_Anzahl": len(self.interferenzfeld),
            "Gesamteingaben": len(self.run_log),
            "Letzter_Eintrag_B": self.context_B[-1] if self.context_B else None
        }

    def visualisieren(self):
        werte = self.zusammenfassung()
        labels = ["Variante A", "Variante B"]
        tokens = [werte["A_Tokens"], werte["B_Tokens"]]

        plt.figure(figsize=(6, 4))
        plt.bar(labels, tokens)
        plt.title("Vergleich Tokenverbrauch (A ohne / B mit Interferenzfeld)")
        plt.ylabel("Tokenanzahl")
        plt.grid(axis='y')
        plt.tight_layout()
        plt.show()

    def exportiere_interferenz_markdown(self, min_relevanz: float = 0.0, startzeit: datetime = None) -> str:
        if not self.interferenzfeld:
            return "Keine Einträge im Interferenzfeld."

        output = "| Zeitstempel | Relevanz | Inhalt\n|-------------|----------|--------\n"
        for eintrag in self.interferenzfeld:
            if eintrag["relevanz"] < min_relevanz:
                continue
            if startzeit and eintrag["zeit"] < startzeit:
                continue
            zeit = eintrag["zeit"].strftime("%Y-%m-%d %H:%M:%S")
            relevanz = f"{eintrag['relevanz']:.2f}"
            inhalt = eintrag["inhalt"].replace("\n", " ").strip()
            output += f"| {zeit} | {relevanz} | {inhalt}\n"
        return output if "|" in output else "Keine Einträge im gewählten Filterbereich."

# Beispielnutzung
if __name__ == "__main__":
    test = InterferenzSpeicherTest(schwelle=0.5)

    # Variante A – ohne Interferenzfeld
    test.eingabe_A("Ich weiß nicht, ob das wichtig ist, aber ich sage es trotzdem.")
    test.eingabe_A("Vielleicht spielt es keine Rolle, aber es beschäftigt mich.")

    # Variante B – mit Interferenzfeld
    test.eingabe_B("Ich weiß nicht, ob das wichtig ist, aber ich sage es trotzdem.")
    test.eingabe_B("Vielleicht spielt es keine Rolle, aber es beschäftigt mich.")

    print(test.zusammenfassung())
    test.visualisieren()
    print("\n--- Interferenz-Markdown-Export (ab 0.4 Relevanz, heute) ---\n")
    print(test.exportiere_interferenz_markdown(min_relevanz=0.4, startzeit=datetime.now().replace(hour=0, minute=0, second=0)))
