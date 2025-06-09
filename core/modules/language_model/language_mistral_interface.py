# modules/language_model/language_mistral_interface.py

from ollama import Client
import json, re
import asyncio
import httpx

client = Client(host="http://ollama:11434")  # Standard-Ollama-Port

def mistral_semantic(text, temperature=0.3):
    """
    Führt eine semantische Analyse des Textes mit Mistral durch.
    Gibt intent und Rohanalyse zurück.
    """
    try:
        prompt = (
            f"Bestimme die semantische Funktion dieses Satzes: {text}\n"
            f"Antwortformat: {{\"intent\": \"frage|aussage|wunsch|definition|reflexion\", \"rohtext\": \"...\"}}"
        )

        response = client.generate(
            model="mistral",
            prompt=prompt,
            options={"temperature": temperature}
        )

        raw_output = response.get("response", "").strip()
        match = re.search(r"\{.*\}", raw_output, re.DOTALL)
        if match:
            return json.loads(match.group())
        else:
            return {"intent": "unbestimmt", "rohtext": raw_output}

    except Exception as e:
        print(f"[Mistral Error] {e}")
        return {"intent": "fehler", "rohtext": str(e)}

async def mistral_embedding_async(text: str) -> list:
    url = "http://localhost:11434/api/embeddings"
    payload = {
        "model": "mistral",
        "prompt": text
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload)
        response.raise_for_status()
        data = response.json()
        return data.get("embedding", [])

async def mistral_semantic_async(text, temperature=0.3):
    """
    Async-Version von mistral_semantic.
    Führt semantische Analyse im Hintergrundthread aus.
    """
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, mistral_semantic, text, temperature)

def get_embedding_vector(text):
    try:
        response = client.embeddings(
            model="mistral-embed",
            prompt=text
        )
        return response["data"][0]["embedding"]
    except Exception as e:
        print(f"[Embedding Error] {e}")
        return None
    
def extract_embeddings(response_json):
    """
    Extrahiert die tatsächlichen Embedding-Vektoren aus der Mistral-API-Antwort.
    """
    if not response_json or "data" not in response_json:
        return {}
    data = response_json["data"]
    if isinstance(data, list):
        return {f"token_{i}": item["embedding"] for i, item in enumerate(data) if "embedding" in item}
    return {}