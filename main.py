from interfaces import reflective_chat, chatgpt_api
from config.settings import MODE
from interfaces.reflective_chat import ReflexiveChat

def main():
    if MODE == "local":
        chat = ReflexiveChat()
        chat.run()
    elif MODE == "api":
        chatgpt_api.run()
    else:
        print("Ungültiger Modus. Bitte 'local' oder 'api' in settings.py festlegen.")

if __name__ == "__main__":
    main()
