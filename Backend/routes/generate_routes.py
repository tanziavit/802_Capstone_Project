from flask import Blueprint, request, jsonify
from services.openai_service import generate_text

generate_bp = Blueprint("generate", __name__)

@generate_bp.route("/api/generate", methods=["POST"])
def generate():
    data = request.json

    prompt = f"""
    Create real estate content in {data['tone']} tone.
    Location: {data['location']}
    Size: {data['size']}
    Price: {data['price']}
    Features: {data['features']}

    Generate:
    1. Listing
    2. Social media post
    3. Email
    4. Video script
    """

    result = generate_text(prompt)

    return jsonify({"result": result})