import os
from core.goal_reflection import reflect_on_goal

# Definition interner Ziele für Erklärung & Vorschläge
system_goals = ["connect", "stabilize", "harmonize"]
suggestions_for_conflict = ["adapt", "coordinate", "stabilize"]

def explain_goal(goal, result):
    if result == "aligned":
        return f"✅ Das Ziel „{goal}“ ist direkt mit den Kernwerten des Systems verbunden: {', '.join(system_goals)}."
    elif result == "neutral":
        return f"ℹ️ Das Ziel „{goal}“ liegt außerhalb der definierten Kernachsen – es erzeugt keine starke Resonanz."
    elif result == "misaligned":
        return f"⚠️ Das Ziel „{goal}“ widerspricht tendenziell den internen Systemachsen. Es erzeugt negative Resonanz."
    else:
        return "❓ Keine Bewertung möglich."

def offer_suggestions():
    return f"💡 Vorschläge für positiv bewertbare Alternativen: {', '.join(suggestions_for_conflict)}"

def chat_loop():
    print("=== 🧭 COMPASS Ziel-Dialogsystem ===")
    print("Gib ein Ziel ein (z. B. connect, organize, delay) oder 'exit' zum Beenden.\n")

    while True:
        user_input = input("Du: ").strip()
        if user_input.lower() in ['exit', 'quit']:
            print("🛑 Sitzung beendet.")
            break

        data = {"goal": user_input}
        result = reflect_on_goal(data)

        print(f"🧭 Bewertung: {result}")

        # Reflexionsfrage
        follow = input("🧭 Möchtest du eine Erklärung dazu? (j/n): ").strip().lower()
        if follow == 'j':
            print(explain_goal(user_input, result))

        # Vorschläge bei neutral/misaligned
        if result in ["neutral", "misaligned"]:
            suggest = input("🧭 Möchtest du Vorschläge für systemkompatible Alternativen? (j/n): ").strip().lower()
            if suggest == 'j':
                print(offer_suggestions())

        print()

if __name__ == "__main__":
    # Nicht im CI-Modus ausführen
    if os.getenv("GITHUB_ACTIONS", "false") == "true":
        print("🛑 Interaktive Sitzung in GitHub Actions deaktiviert.")
    else:
        chat_loop()
