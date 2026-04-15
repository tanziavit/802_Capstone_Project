from flask import Blueprint, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
from models.db import get_db_connection

auth_bp = Blueprint("auth", __name__)

# -------------------------
# SIGNUP
# -------------------------
@auth_bp.route("/api/signup", methods=["POST"])
def signup():
    try:
        data = request.get_json()

        name = data.get("name")
        email = data.get("email")
        password = data.get("password")

        if not name or not email or not password:
            return jsonify({"error": "All fields are required"}), 400

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        # Check if user exists
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        existing_user = cursor.fetchone()

        if existing_user:
            cursor.close()
            conn.close()
            return jsonify({"error": "User already exists"}), 400

        # Hash password
        hashed_password = generate_password_hash(password)

        # Insert user
        cursor.execute(
            "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
            (name, email, hashed_password)
        )

        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({"message": "Signup successful"}), 201

    except Exception as e:
        print("Signup Error:", str(e))
        return jsonify({"error": "Internal server error"}), 500


# -------------------------
# LOGIN
# -------------------------
@auth_bp.route("/api/login", methods=["POST"])
def login():
    try:
        data = request.get_json()

        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            return jsonify({"error": "Email and password required"}), 400

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        # Fetch user
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()

        cursor.close()
        conn.close()

        if not user or not check_password_hash(user["password"], password):
            return jsonify({"error": "Invalid credentials"}), 401

        # Store session
        session["user_id"] = user["id"]

        return jsonify({
            "message": "Login successful",
            "user": {
                "id": user["id"],
                "name": user["name"],
                "email": user["email"]
            }
        }), 200

    except Exception as e:
        print("Login Error:", str(e))
        return jsonify({"error": "Internal server error"}), 500


# -------------------------
# LOGOUT
# -------------------------
@auth_bp.route("/api/logout", methods=["POST"])
def logout():
    try:
        session.pop("user_id", None)
        return jsonify({"message": "Logged out successfully"}), 200

    except Exception as e:
        print("Logout Error:", str(e))
        return jsonify({"error": "Internal server error"}), 500


# -------------------------
# CHECK SESSION
# -------------------------
@auth_bp.route("/api/check-auth", methods=["GET"])
def check_auth():
    try:
        user_id = session.get("user_id")

        if not user_id:
            return jsonify({"authenticated": False}), 401

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT id, name, email FROM users WHERE id = %s", (user_id,))
        user = cursor.fetchone()

        cursor.close()
        conn.close()

        if not user:
            return jsonify({"authenticated": False}), 401

        return jsonify({
            "authenticated": True,
            "user": user
        }), 200

    except Exception as e:
        print("Check Auth Error:", str(e))
        return jsonify({"error": "Internal server error"}), 500