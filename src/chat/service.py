import os

import requests
from dotenv import load_dotenv

load_dotenv()


def chat_controller():
    KEY = os.getenv("GPT_KEY")
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {KEY}",
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": "Say this is a test!"}],
        "temperature": 0.7,
    }

    res = requests.post(url, headers=headers, json=data)
    print(res.json())
