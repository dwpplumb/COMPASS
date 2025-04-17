import os
from core.goal_reflection import reflect_on_goal

def main():
    print("=== COMPASS Zielbewertung ===")
    while True:
        user_input = input("Gib ein Ziel ein (oder 'exit'): ").strip()
        if user_input.lower() == 'exit':
            break
        data = {"goal": user_input}
        result = reflect_on_goal(data)
        print(f"➤ Bewertung: {result}\n")

if __name__ == "__main__":
    # Schutz: nicht ausführen, wenn in GitHub Actions (CI-Umgebung)
    if os.getenv("GITHUB_ACTIONS", "false") == "true":
        print("🛑 Interaktive Eingabe in GitHub Actions deaktiviert.")
    else:
        main()
