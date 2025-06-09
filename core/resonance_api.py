# resonance_api.py
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Dict
from modules.qstructure.q_factor_engine import q_resonance_factorization

router = APIRouter()

class FactorInput(BaseModel):
    n: int
    axiom_weights: Dict[str, float] = {"prime_density": 0.7}

@router.post("/resonance-factorize")
def factorize(input_data: FactorInput):
    try:
        result = q_resonance_factorization(input_data.n, input_data.axiom_weights)
        if result:
            return {"factors": result, "status": "ok"}
        else:
            return {"error": "No valid factorization found.", "status": "no_match"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}
