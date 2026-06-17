import os
import httpx
from dotenv import load_dotenv

load_dotenv("vacation-agent/.env")
key = os.getenv("GEMINI_API_KEY")

url = f"https://generativelanguage.googleapis.com/v1beta/models?key={key}"
res = httpx.get(url, timeout=10)

if res.status_code == 200:
    data = res.json()
    models = [m['name'] for m in data.get('models', []) if "generateContent" in m.get('supportedGenerationMethods', [])]
    print("Modelos disponibles que soportan generación:")
    for m in models:
        print(" -", m)
else:
    print(f"Error {res.status_code}: {res.text}")
