# holodeck_scenarios.py

def generate_scene(description: str) -> str:
    """
    Dynamisch erzeugt eine Holodeck-Szene auf Basis einer freien Beschreibung.
    """
    intro = """
[HOLODECK ONLINE]
> Szene geladen: \"{description}\"
    """.strip().format(description=description.capitalize())

    prompt = f"""
🏞️ Umgebung wird aufgebaut: {description}.

🎬 Die Szene beginnt...

🧠 Charaktere reagieren auf dich. Atmosphäre passt sich deiner Stimmung an.

> Sag „Ende Holoprogramm“, um zu beenden.
"""
    return f"{intro}\n\n{prompt}"


# Beispielhafte Ausführung (zum Testen)
if __name__ == "__main__":
    user_input = "verrauchte Eckkneipe mit Stand-up Comedian"
    print(generate_scene(user_input))
