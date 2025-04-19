# modules/response_language/natural_response_model.py

from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import os

# Modellname kann angepasst werden (hier kleines Modell für Testzwecke)
MODEL_NAME = os.getenv("COMPASS_NLP_MODEL", "tiiuae/falcon-rw-1b")

# Initialisiere Modell (nur einmal laden)
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
model.eval()


def generate_natural_response(user_input: str, analysis: str, max_tokens: int = 150) -> str:
    """
    Erzeugt eine semantisch passende Antwort auf Grundlage des Nutzereingabe + Analysekommentars.
    """
    prompt = (
        f"You are a reflective AI system. The user said: \"{user_input}\".\n"
        f"Your internal evaluation is: {analysis}\n"
        f"Now respond with a natural, helpful statement to the user:"
    )

    inputs = tokenizer(prompt, return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_tokens,
            do_sample=True,
            temperature=0.7,
            top_k=50,
            top_p=0.95
        )
    decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Nur neuen Antwortteil extrahieren
    if prompt in decoded:
        return decoded.split(prompt)[-1].strip()
    return decoded.strip()
