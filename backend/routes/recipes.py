from flask import Blueprint, request, jsonify
from services.ai_service import get_recipe_suggestions

recipes_bp = Blueprint("recipes", __name__)

@recipes_bp.route("/recipes", methods=["POST"])
def generate_recipes():
    data = request.get_json() or {}
    ingredients = data.get("ingredients", [])
    if not isinstance(ingredients, list):
        return jsonify({"error": "ingredients must be a list"}), 400

    recipes = get_recipe_suggestions(ingredients)
    return jsonify({"recipes": recipes})