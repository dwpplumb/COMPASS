from interfaces import reflective_chat, chatgpt_api
from config.settings import MODE
from interfaces.reflective_chat import ReflexiveChat

def select_mode():
    print("Verfügbare Modi: local | api")
    return input("Modus wählen: ").strip()

def select_model():
    print("Verfügbare KI-Modelle:")
    print("1 – GPT-4.1")
    print("2 – GPT-3.5")
    print("3 – Lokale Instanz")
    return input("Modell wählen (Nummer): ").strip()

def main():
    mode = MODE or select_mode()

    if mode == "local":
        chat = ReflexiveChat()
        chat.run()

    elif mode == "api":
        model = select_model()
        if model == "1":
            from interfaces import chatgpt_api
            chatgpt_api.run()
        elif model == "2":
            from interfaces import chatgpt_api_light
            chatgpt_api_light.run()
        else:
            print("Modell nicht implementiert.")

    else:
        print("Ungültiger Modus. Bitte 'local' oder 'api' in settings.py festlegen.")

if __name__ == "__main__":
    main()
