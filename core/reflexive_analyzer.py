from modules.language_model.semantic_vector_engine import get_embedding_vector
from modules.evaluation_model.axiom_scorer import score_axioms

class EvaluationResult:
    def __init__(self, input_text, scores):
        self.input_text = input_text
        self.scores = scores  # Dict: {A1: 0.8, A2: 0.4, ...}

    def format(self):
        result = ""
        for axiom, score in self.scores.items():
            result += f"  {axiom}: {score:.2f}\n"
        return result

    def summary(self):
        active = [k for k, v in self.scores.items() if v >= 0.5]
        if not active:
            return "➤ Evaluation: NEUTRAL\nReason: No strong axiom activation."
        return f"➤ Evaluation: STRUCTURED\nActive Axioms: {', '.join(active)}"


def analyze_input(text):
    vector = get_embedding_vector(text)
    if vector is None:
        return EvaluationResult(text, {f"A{i+1}": 0.0 for i in range(7)})
    scores = score_axioms(vector)
    return EvaluationResult(text, scores)
