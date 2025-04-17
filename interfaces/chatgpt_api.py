import openai
from config.settings import OPENAI_API_KEY

def run():
    openai.api_key = OPENAI_API_KEY
    prompt = input("Gib deine Anfrage ein: ")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150
    )
    print(response.choices[0].message['content'])
