import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("API_URL")
HF_TOKEN = os.getenv("HUGGINGFACE_API_KEY")

headers = {"Authorization": f"Bearer {HF_TOKEN}"}

def ner(text):
    payload = {"inputs": text}
    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        ner_results = response.json()
        print("From HuggingFace API:", ner_results)
        return ner_results
    else:
        print("Error:", response.status_code, response.text)
        return {"error": "NER API failed"}