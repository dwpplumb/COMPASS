# entrypoint.py

from fastapi import FastAPI
from pydantic import BaseModel
from core.llm_interface import call_llm
from core.compass_benchmark import load_compass_axioms, compass_analyse_text

app = FastAPI()

# Lade die Axiome beim Start
AXIOM_MAP = load_compass_axioms("data/compass_axioms_classic_de.json")

class InputData(BaseModel):
    text: str

@app.post("/benchmark_evaluate")
def benchmark_evaluate(data: InputData):
    try:
        # 1. LLM-Antwort holen
        llm_output = call_llm(data.text)

        # 2. COMPASS-Analyse der LLM-Antwort
        analysis = compass_analyse_text(llm_output, AXIOM_MAP)

        return {
            "llm_response": llm_output,
            "compass_analysis": analysis
        }
    except Exception as e:
        return {"error": str(e)}

# Reflexion: Klarer Schnittpunkt von API, LLM und COMPASS-Analyse (A5C, A3C, A1C).
