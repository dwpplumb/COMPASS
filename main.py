import time
import threading
from config.settings import MODE
from interfaces.reflective_chat import ReflexiveChat
from logger_setup import setup_logger

logger = setup_logger()

DEFAULT_MODE = "api"
TIMEOUT_SECONDS = 5


def input_with_timeout(prompt, timeout):
    user_input = [None]

    def get_input():
        user_input[0] = input(prompt)

    thread = threading.Thread(target=get_input)
    thread.start()
    thread.join(timeout)
    if thread.is_alive():
        print(f"\n⏱️ Keine Eingabe erkannt – starte automatisch mit '{DEFAULT_MODE}'")
        thread.join()
    return user_input[0] or DEFAULT_MODE


def try_api_chat(model, max_retries=3):
    for attempt in range(max_retries):
        try:
            if model == "1":
                from interfaces import chatgpt_api
                chatgpt_api.run()
                return True
            elif model == "2":
                from interfaces import chatgpt_api_light
                chatgpt_api_light.run()
                return True
        except Exception as e:
            logger.warning(f"API-Verbindungsfehler (Versuch {attempt + 1}): {e}")
            time.sleep(1)

    logger.error("API nicht erreichbar – Fallback auf lokalen Modus aktiviert")
    logger.info("Aktiviere Fallback gemäß A6 (temporäre Destabilisierung zugelassen für Effizienzgewinn)")
    return False


def main():
    logger.info("COMPASS gestartet")
    print("🤖 COMPASS gestartet")
    print("Wähle Modus: [local] oder [api] – automatisch in {} Sekunden...".format(TIMEOUT_SECONDS))
    mode = input_with_timeout("Modus eingeben (local/api): ", TIMEOUT_SECONDS).strip()

    if mode == "api":
        print("Verfügbare KI-Modelle:\n1 – GPT-4.1\n2 – GPT-3.5")
        model = input("Modell wählen (Nummer): ").strip() or "1"
        if try_api_chat(model):
            return

    logger.info("Starte lokale Instanz gemäß A7 (Reflexion) und A1 (strukturwirksame Existenz)")
    print("🔄 Starte lokale Instanz...")
    chat = ReflexiveChat()
    chat.run()


if __name__ == "__main__":
    main()
