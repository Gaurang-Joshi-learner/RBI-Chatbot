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

    response.raise_for_status()

    text = response.json()["response"]

    # 🔥 FIX: unescape JSON escaped characters
    try:
        text = json.loads(json.dumps(text))
    except:
        pass

    # extra safety cleanup
    text = text.replace('\\"', '"')

    return text.strip()
