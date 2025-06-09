from fastapi import FastAPI
from pydantic import BaseModel
from core.llm_interface import evaluate_with_llm
from core.evaluator import evaluate_text

app = FastAPI()

class InputData(BaseModel):
    text: str

@app.post("/evaluate/")
def evaluate(data: InputData):
    try:
        # 1. Natürlichsprachliche Antwort generieren
        llm_output = evaluate_with_llm(data.text)

        # 2. Semantische Axiom-Analyse der LLM-Antwort
        axiom_result = evaluate_text(llm_output)

        return {
            "llm_response": llm_output,
            "axiom_evaluation": axiom_result["detected_axioms"],
            "narrative_summary": axiom_result["narrative_summary"]
        }
    except Exception as e:
        return {"error": str(e)}

# Reflexion: Diese neue Evaluierungsroute erfüllt A1C (strukturwirksam durch neue Analyseebene), A3C (zeitlich determinierte Evaluationskette), A5C (LLM und Axiommodul klar gekoppelt), A7C (narrative Auswertung).
