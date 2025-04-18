from openai import OpenAI
from config.settings import OPENAI_API_KEY

def run():
    client = OpenAI(api_key=OPENAI_API_KEY)
    prompt = input("Gib deine Anfrage ein: ")
    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {"role": "system", "content": "Du bist ein COMPASS-Modul zur Axiom-Analyse."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500,
        temperature=0.7
    )
    print(response.choices[0].message.content)

