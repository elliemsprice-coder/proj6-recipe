from flask import Blueprint, request, jsonify
from bson.objectid import ObjectId
from services.db_service import get_favorites_collection
from models.favorite_model import Favorite

favorites_bp = Blueprint("favorites", __name__)

@favorites_bp.route("/favorites", methods=["GET"])
def list_favorites():
    col = get_favorites_collection()
    docs = list(col.find())
    for d in docs:
        d["_id"] = str(d["_id"])
    return jsonify({"favorites": docs})

@favorites_bp.route("/favorites", methods=["POST"])
def add_favorite():
    data = request.get_json() or {}
    title = data.get("title")
    ingredients = data.get("ingredients", [])
    instructions = data.get("instructions", "")

    if not title:
        return jsonify({"error": "title is required"}), 400

    fav = Favorite(title=title, ingredients=ingredients, instructions=instructions)
    col = get_favorites_collection()
    result = col.insert_one(fav.to_dict())
    return jsonify({"id": str(result.inserted_id)}), 201

@favorites_bp.route("/favorites/<fav_id>", methods=["DELETE"])
def delete_favorite(fav_id):
    col = get_favorites_collection()
    try:
        oid = ObjectId(fav_id)
    except Exception:
        return jsonify({"error": "invalid id"}), 400

    res = col.delete_one({"_id": oid})
    if res.deleted_count == 0:
        return jsonify({"error": "not found"}), 404
    return jsonify({"status": "deleted"})