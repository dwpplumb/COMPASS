import requests

# Hauptfunktion zum Abfragen eines LLM-Modells (z.B. Ollama, Mistral)
def query_ollama(prompt, model="mistral"):
    """
    Sendet einen Prompt an das Ollama-Modell und gibt die Antwort zurück.
    Args:
        prompt (str): Die Benutzereingabe oder Systemanweisung.
        model (str): Der Modellname (Standard: 'mistral').
    Returns:
        str: Die generierte Antwort vom Modell oder eine Fehlermeldung.
    """
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        data = response.json()
        # Je nach Ollama-Version kann das Schlüsselwort "response" oder "message" lauten
        if "response" in data:
            return data["response"]
        elif "message" in data:
            return data["message"]
        else:
            return f"Unerwartete Antwortstruktur: {data}"
    except Exception as e:
        return f"Fehler bei Anfrage: {e}"

# Erweiterbar: Weitere LLM-spezifische Logiken
def evaluate_with_llm(input_text, model="mistral"):
    """
    Bewertet einen Input-Text mithilfe eines LLM und bereitet das Ergebnis auf.
    """
    antwort = query_ollama(input_text, model)
    return antwort

# Beispiel für den direkten Funktionsaufruf:
if __name__ == "__main__":
    prompt = input("Prompt an das LLM: ")
    output = evaluate_with_llm(prompt)
    print(f"Antwort:\n{output}")
