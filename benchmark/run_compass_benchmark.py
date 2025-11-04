import requests
import json
from datetime import datetime

today = datetime.now().strftime("%Y-%m-%d_%H-%M")
API_URL = "http://localhost:8000/benchmark_evaluate"
DE_FILE = "../data/datasets/train.deu" 
EN_FILE = "../data/datasets/train.eng"
OUT_FILE = "../data/tests/wmt23_deen_benchmark_mistral_failcase.json"

OLLAMA_API_URL = "http://ollama:11434/api/generate"
MODEL_NAME = "mistral"

# Wie viele Zeilen? Für den ersten Test ggf. nur 100
N = 1000

def query_mistral(sentence, model=MODEL_NAME):
    payload = {
        "model": model,
        "prompt": sentence,
        "stream": False,
        "seed": 42,
        "temperature": 0.0 
    }
    try:
        response = requests.post(OLLAMA_API_URL, json=payload)
        response.raise_for_status()
        data = response.json()
        return data.get("response", "").strip()
    except Exception as e:
        return f"Error: {str(e)}"

results = []
with open(DE_FILE, "r", encoding="utf-8") as f_de, \
     open(EN_FILE, "r", encoding="utf-8") as f_en:
    for idx, (line_de, line_en) in enumerate(zip(f_de, f_en)):
        if idx >= N:
            break
        inp_de = line_de.strip()
        ref_en = line_en.strip()
        prompt = (
       "Translate the following German sentence into English, strictly in a professional medical context.\n"
        "- Keep all symbols (such as %, °C, ml, mg, and other units or abbreviations) exactly as they are, unless they are part of punctuation.\n"
        "- Only use established medical terminology, do not use layperson's language or add explanations.\n"
        "- Do not change or omit any specific terms or numbers.\n"
        "- Output ONLY the English sentence, with no additional comments or translations.\n"
        "\nGerman: {input_sentence}\nEnglish:"
                )
        mistral_output = query_mistral(prompt)
        print(f"[{idx+1}/{N}] {inp_de} → {mistral_output}")

        results.append({
            "input_sentence_de": inp_de,
            "reference_sentence_en": ref_en,
            "llm_response_en": mistral_output
        })

config = {
  "model": {
    "name": "mistral",
    "variant": "7b-instruct-v0.3",
    "architecture": "llama",
    "parameters": "7.2B",
    "quantization": "Q4_0",
    "context_length": 32768,
    "embedding_length": 4096
  },
  "seed": 42,
  "temperature": 0.0,
  "api_url": "http://ollama:11434/api/generate",
  "license": "Apache 2.0, January 2004",
  "benchmark_dataset": "wmt23",
  "prompt":prompt,
  "date": today
}


output = {
    "config": config,
    "results": results
}

with open(OUT_FILE, "w", encoding="utf-8") as fout:
    json.dump(output, fout, ensure_ascii=False, indent=2)

print(f"Benchmark abgeschlossen. Ergebnisse in {OUT_FILE}")
