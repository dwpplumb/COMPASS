def initiate_meta_reflection(context, system_state, conflict=None):
    """
    Initiiert eine Meta-Reflexion basierend auf einem Bewertungsdilemma, Zielkonflikt oder Axiomschwäche.

    :param context: Kontext der ursprünglichen Bewertung (z. B. Thema, Ziel, Instanz)
    :param system_state: aktueller Stand der Bewertung (Module, Axiome, Subziele)
    :param conflict: Optionaler erkannter Konflikt oder Grenzproblem
    :return: Reflexionsvorschlag (z. B. neues Subaxiom, neue Zielstruktur, Kommentar)
    """
    reflection = {}

    if conflict:
        reflection['auslöser'] = conflict
    else:
        reflection['auslöser'] = "Bewertungsgrenze erkannt"

    # Beispielhafte Reflexionsinhalte
    reflection['kontext'] = context
    reflection['systemantwort'] = "Einleitung systemischer Erweiterung gemäß Axiom 7"
    reflection['vorschlag'] = generate_structure_adaptation(context, system_state)

    return reflection

def generate_structure_adaptation(context, system_state):
    """
    Leitet eine strukturelle Erweiterung (z. B. neues Subaxiom, Zielprinzip oder Reflexionsregel) aus einem Meta-Konflikt ab.

    :param context: Beschreibung der Problemstellung, auf die das System nicht mehr reagieren kann
    :param system_state: Snapshot der aktiven Axiome, Ziele und Konflikte
    :return: Vorschlag als strukturierter Text oder Dict
    """
    adaptation = {}

    # Beispiel: Zielkonflikt erkannt
    if 'gleichwertige Ziele' in context.lower():
        adaptation["typ"] = "Zielprinzip"
        adaptation["vorschlag"] = "ZP-008 – Strukturvorrang bei Kontextdisparität"
        adaptation["beschreibung"] = (
            "Wenn zwei gleichwertige Ziele nicht kohärent überlagert werden können, "
            "ist dasjenige zu bevorzugen, das größere systemische Struktur erzeugt."
        )
    
    # Beispiel: Kausalitätsbruch oder Rückkopplungskonflikt
    elif 'zeit' in context.lower() or 'rückwirkung' in context.lower():
        adaptation["typ"] = "Subaxiom (QG-3)"
        adaptation["vorschlag"] = "QG-3.2 – Entropieschatten"
        adaptation["beschreibung"] = (
            "Zeitliche Rückwirkungen sind zulässig, wenn die Systemstruktur eine "
            "kohärente Reflexion entlang entropischer Zielspuren erlaubt."
        )

    # Default – strukturelle Reflexion
    else:
        adaptation["typ"] = "Metareflexion"
        adaptation["vorschlag"] = "Reflexionsregel: 'Jede Grenze erzeugt eine neue Systemebene, wenn sie nicht durch interne Rekonfiguration lösbar ist.'"
        adaptation["beschreibung"] = "Strukturelle Erweiterung durch vertikale Systemöffnung."

    return adaptation
