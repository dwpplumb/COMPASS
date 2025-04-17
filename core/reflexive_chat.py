"""
Reflexives Dialogmodul für COMPASS
Führt einen interaktiven Dialog mit kontinuierlicher Selbstreflexion über Ziele, Aussagen und Bewertungen.
"""

from core.goal_reflection_advanced import reflect_on_goal
from core.compass_engine import evaluate
from core.logger_setup import setup_logger

logger = setup_logger(__name__, log_file='logs/compass.log')

class ReflexiveChat:
    def __init__(self):
        self.history = []
        logger.info("Reflexiver Chat initialisiert.")

    def receive_input(self, user_input):
        logger.info(f"Nutzerinput empfangen: {user_input}")
        reflection = reflect_on_goal({"goal": user_input})
        full_eval = evaluate({"goal": user_input})

        response = {
            "antwort": self._generate_response(reflection, full_eval),
            "bewertung": reflection,
            "evaluation": full_eval
        }

        self.history.append({
            "user_input": user_input,
            "response": response
        })

        logger.info(f"Reflexion abgeschlossen: {response}")
        return response

    def _generate_response(self, reflection, evaluation):
        align = reflection.get("alignment")
        meta = reflection.get("meta_analysis", {})
        msg = f"➤ Zielbewertung: {align.upper()}\n"
        if meta:
            msg += f"Grund: {meta.get('reason')}\n"
            msg += f"Typ: {meta.get('goal_type')}, Stimmung: {meta.get('emotional_connotation')}\n"
        if "connection_score" in evaluation:
            msg += f"Verbindungspunktzahl: {evaluation['connection_score']:.2f}"
        return msg

    def show_history(self):
        return self.history
