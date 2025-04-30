
def deep_reflect(prompt: str) -> str:
    """
    Führt eine strukturierte Reflexion über die Anfrage durch,
    um Mehrdeutigkeiten, unklare Räume oder falsche Erwartungsebenen zu erkennen.

    :param prompt: Eingabetext des Nutzers
    :return: Geklärter oder zurückgeführter Prompt
    """

    # 1. Einfache Schlüsselwortprüfung (ersetzbar durch NLP später)
    if "Phasenverschiebung" in prompt and "Raum" not in prompt:
        return (
            "Was ist mit 'Phasenverschiebung' gemeint? "
            "Könnte es sich um elektrotechnische, quantenphysikalische oder klassische Raumkonzepte handeln? "
            "Bitte präzisiere z. B.: 'Was ist eine Phasenverschiebung im klassischen Raum aus Sicht des Standardmodells?'"
        )

    # 2. Platzhalter für weitere semantische Prüfungen
    # TODO: Erweiterung durch Begriffsräume und Bewertungsachsen

    # Standardfall: keine Rückmeldung nötig
    return prompt
