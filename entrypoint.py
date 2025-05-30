from fastapi import FastAPI
from pydantic import BaseModel
from core.evaluator import evaluate_text
from core.llm_interface import evaluate_with_llm

app = FastAPI()

class InputData(BaseModel):
    text: str

@app.post("/evaluate/")
def evaluate(data: InputData):
    try:
        result = evaluate_text(data.text)
        if isinstance(result, tuple):
            result = result[0]
        # LLM-Call nur, wenn "llm_required" gesetzt ist (optional)
        if isinstance(result, dict) and result.get("llm_required"):
            llm_answer = evaluate_with_llm(data.text)
            result["llm_output"] = llm_answer
        return {"result": result}
    except Exception as e:
        return {"error": str(e)}
