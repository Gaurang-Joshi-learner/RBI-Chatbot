import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "phi3:mini"

def generate_with_ollama(prompt: str) -> str:

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        },
        timeout=600
    )

    if response.status_code != 200:

        print("OLLAMA ERROR:")
        print(response.text)

        return (
            "The language model is currently unavailable."
        )

    text = response.json()["response"]

    try:
        text = json.loads(json.dumps(text))
    except:
        pass

    return text.strip()