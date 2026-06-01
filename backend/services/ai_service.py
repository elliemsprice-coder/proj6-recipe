import json
import configparser
import requests

credentials_path = "/app/credentials.ini"

_config = configparser.ConfigParser()
_config.read(credentials_path)

API_KEY = _config.get("ai", "API_KEY")
ENDPOINT = _config.get("ai", "ENDPOINT")

def get_recipe_suggestions(ingredients):
    prompt = (
        "Generate 3 recipes in valid JSON only. "
        "No explanations. No markdown. "
        "Format:\n"
        "{\n"
        '  "recipes": [\n'
        "    {\n"
        '      "title": "string",\n'
        '      "description": "string",\n'
        '      "ingredients": ["list", "of", "strings"],\n'
        '      "instructions": ["step 1", "step 2"]\n'
        "    }\n"
        "  ]\n"
        "}\n"
        f"User ingredients: {', '.join(ingredients)}"
    )

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    body = {
        "inputs": prompt,
        "parameters": {"temperature": 0.7}
    }

    try:
        response = requests.post(ENDPOINT, headers=headers, json=body)
        print("RAW HF RESPONSE:", response.text)
        response.raise_for_status()

        content = response.json()[0]["generated_text"]

        try:
            return json.loads(content)
        except json.JSONDecodeError:
            print("HF returned non‑JSON:", content)
            return {"error": "Invalid JSON from model"}

    except Exception as e:
        print("HF ERROR:", e)
        return {"error": str(e)}