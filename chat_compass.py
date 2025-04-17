import os
from core.reflexive_chat import ReflexiveChat

def chat_loop():
    print("=== 🧭 COMPASS Reflexiver Ziel-Dialog ===")
    print("Gib ein Ziel ein (z. B. connect, organize, delay) oder 'exit' zum Beenden.\n")

    chat = ReflexiveChat()

    while True:
        user_input = input("Du: ").strip()
        if user_input.lower() in ['exit', 'quit']:
            print("🛑 Sitzung beendet.")
            break

        response = chat.receive_input(user_input)
        print(response["antwort"])
        print()

if __name__ == "__main__":
    if os.getenv("GITHUB_ACTIONS", "false") == "true":
        print("🛑 Interaktive Sitzung in GitHub Actions deaktiviert.")
    else:
        chat_loop()
