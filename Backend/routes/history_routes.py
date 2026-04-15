from flask import Blueprint, jsonify

history_bp = Blueprint("history", __name__)

@history_bp.route("/api/history", methods=["GET"])
def get_history():
    # Dummy for now
    return jsonify([
        {"location": "NY", "listing": "Sample listing"}
    ])