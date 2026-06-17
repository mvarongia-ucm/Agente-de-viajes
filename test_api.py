import os, httpx, json
key = os.getenv("GEMINI_API_KEY")
url = f"https://generativelanguage.googleapis.com/v1beta/models?key={key}"
r = httpx.get(url)
print("Status:", r.status_code)
if r.status_code == 200:
    data = r.json()
    models = [m['name'] for m in data.get('models', [])]
    print("Models:", models)
else:
    print("Error:", r.text)
