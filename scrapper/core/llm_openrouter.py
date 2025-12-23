import os
import requests

# OpenRouter configuration
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
if not OPENROUTER_API_KEY:
    raise RuntimeError("OPENROUTER_API_KEY not set")

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

# Stable, fast, Jarvis-friendly
MODEL = "meta-llama/llama-3-8b-instruct"


def ask_llm(system_prompt: str, user_text: str) -> str:
    """
    Sends a prompt to OpenRouter and returns
    a calm, concise, Jarvis-style response.
    """

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",
        "X-Title": "Jarvis"
    }

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_text}
        ],
        # Jarvis tuning
        "temperature": 0.2,     # calm, controlled
        "top_p": 0.9,
        "max_tokens": 100        # prevents rambling
    }

    try:
        response = requests.post(
            OPENROUTER_URL,
            headers=headers,
            json=payload,
            timeout=20
        )
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"].strip()

    except requests.exceptions.Timeout:
        return "I’m experiencing a delay. Please try again."
    except requests.exceptions.RequestException:
        return "I’m unable to connect at the moment."
