# core/llm_interface.py

import requests

def call_llm(text: str, model: str = "mistral") -> str:
    """
    Ruft ein LLM (z.B. Mistral über Ollama) via API auf.
    Gibt die Antwort als reinen Text zurück.
    """
    url = "http://ollama:11434/api/generate"  # ggf. anpassen!
    payload = {
        "model": model,
        "prompt": text,
        "stream": False
    }
    try:
        response = requests.post(url, json=payload, timeout=60)
        response.raise_for_status()
        data = response.json()
        # Je nach Ollama-Version: "response" oder "message"
        return data.get("response") or data.get("message") or str(data)
    except Exception as e:
        return f"Fehler bei LLM-Call: {e}"

# Reflexion: Erfüllt A1C (LLM-Output als Systemwirkung), A5C (klare Schnittstelle zur API).
