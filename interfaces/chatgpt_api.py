from openai import OpenAI
from config.settings import OPENAI_API_KEY
from core.reflexive_analyzer import analyze_input

def run():
    client = OpenAI(api_key=OPENAI_API_KEY)
    prompt = input("Gib deine Anfrage ein: ")

    # GPT-Antwort erzeugen
    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {"role": "system", "content": "Du bist ein COMPASS-Modul zur Axiom-Analyse."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500,
        temperature=0.7
    )
    gpt_reply = response.choices[0].message.content

    # Axiomatische Bewertung mit COMPASS
    evaluation = analyze_input(prompt)

    # Ausgabe kombinieren
    print("\n🤖 GPT-Antwort:")
    print(gpt_reply)
    print("\n📐 Axiom profile (COMPASS):")
    print(evaluation.format())
    print(evaluation.summary())
