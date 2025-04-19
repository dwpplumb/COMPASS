"""
Reflexives Dialogmodul für COMPASS
Führt einen interaktiven Dialog mit kontinuierlicher Selbstreflexion über Ziele, Aussagen und Bewertungen.
"""

from core.axiom_matrix_adaptive import evaluate_axiom_matrix_adaptive as evaluate_axiom_matrix
from core.goal_reflection_advanced import reflect_on_goal
from core.compass_engine import evaluate
from core.logger_setup import setup_logger
from modules.response_language.response_language import generate_response_text
from modules.response_language.natural_response_model import generate_natural_response

logger = setup_logger(__name__, log_file='logs/compass.log')


class ReflexiveChat:
    def __init__(self):
        self.system_goals = [
            "connect",         # Verbindung
            "stabilize",       # Stabilität
            "harmonize",       # Ausgleich
            "structure",       # Ordnung / Gliederung
            "integration",     # Einbindung
            "resilience",      # Anpassungsfähigkeit bei Erhalt
            "ethics",          # systemische Bewertung
            "awareness",       # Kontextbewusstsein
            "balance",         # Gleichgewicht
            "reflection"       # Selbstbezug / Metabewertung
        ]
        self.history = []
        logger.info("Reflexiver Chat initialisiert.")

    def run(self):
        if hasattr(self, "_intro_shown") and self._intro_shown:
            return
        self._intro_shown = True  # nur beim ersten Aufruf zeigen

        print("🤖 I am COMPASS – a structured, axiom-based reflective dialogue system.")
        print("My purpose is to analyze your input along fundamental evaluation axes.")
        print("You can enter a goal, statement or idea – and I will reflect with you.\n")

        while True:
            prompt = input("Please enter your local enquiry: ")
            if prompt.lower() == 'exit':
                break
            response = self.receive_input(prompt)
            print(response["antwort"])

    def receive_input(self, user_input):
        logger.info(f"Nutzerinput empfangen: {user_input}")
        reflection = reflect_on_goal({"goal": user_input})
        full_eval = evaluate({"goal": user_input})
        axiom_matrix = evaluate_axiom_matrix(user_input)

        response = {
            "antwort": self._generate_response(user_input, reflection, full_eval, axiom_matrix),
            "bewertung": reflection,
            "evaluation": full_eval,
            "axiom_matrix": axiom_matrix
        }

        self.history.append({
            "user_input": user_input,
            "response": response
        })

        logger.info(f"Reflexion abgeschlossen: {response}")
        return response

    def _generate_response(self, user_input, reflection, evaluation, axiom_matrix):
        align = reflection.get("alignment")
        meta = reflection.get("meta_analysis", {})
        msg = f"➤ Evaluation: {align.upper()}\n"
        if meta:
            msg += f"Reason: {meta.get('reason')}\n"
            msg += f"Type: {meta.get('goal_type')}, Mood: {meta.get('emotional_connotation')}\n"
        if "connection_score" in evaluation:
            msg += f"Connection score: {evaluation['connection_score']:.2f}\n"

        msg += "\n📐 Axiom profile:\n"
        for ax in sorted(axiom_matrix):
            if '.' not in ax:
                msg += f"  {ax}: {round(axiom_matrix[ax], 2)}\n"

        # Sprachliche Reflexion + natürliche Antwort
        from modules.language_model.reflection_language import interpret_axiom_profile
        from modules.response_language.response_language import generate_response_text

        axiom_comment = interpret_axiom_profile(axiom_matrix)
        response = generate_response_text(user_input, align, axiom_comment)

        msg += "\n" + response
        return msg

    def show_history(self):
        return self.history
