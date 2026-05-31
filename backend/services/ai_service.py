import json
import configparser
import os
import requests

credentials_path = "/app/credentials.ini"

_config = configparser.ConfigParser()
_config.read(credentials_path)

API_KEY = _config.get("ai", "API_KEY")
ENDPOINT = _config.get("ai", "ENDPOINT")

def get_recipe_suggestions(ingredients):
    system_prompt = (
        "You are a recipe generator. You MUST respond with valid JSON ONLY. "
        "No explanations, no extra text, no markdown. "
        "Your entire response MUST be a single JSON object in this exact format:\n"
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
        "If the user provides ingredients, generate 3 recipes."
    )

    full_prompt = (
        f"{system_prompt}\n\n"
        f"User ingredients: {', '.join(ingredients)}"
    )

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    body = {
        "model": "gpt-4o-mini",
        "input": full_prompt,
        "temperature": 0.7
    }

    try:
        response = requests.post(ENDPOINT, headers=headers, json=body)
        response.raise_for_status()

        content = response.json()["output"][0]["content"][0]["text"]

        try:
            return json.loads(content)
        except json.JSONDecodeError:
            print("AI returned non‑JSON:", content)
            return {"error": "Invalid JSON from AI"}

    except Exception as e:
        print("AI ERROR:", e)
        if hasattr(e, "response") and e.response is not None:
            print("AI RESPONSE:", e.response.text)
        return {"error": str(e)}