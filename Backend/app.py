from flask import Flask, render_template, session, redirect, url_for
from flask_cors import CORS
from config import Config

# Import Blueprints
from routes.auth_routes import auth_bp
from routes.generate_routes import generate_bp
from routes.history_routes import history_bp

app = Flask(__name__)
app.config.from_object(Config)

CORS(app)

# Register Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(generate_bp)
app.register_blueprint(history_bp)

# -----------------------
# Page Routes
# -----------------------

@app.route("/")
def home():
    if "user_id" in session:
        return redirect(url_for("dashboard"))
    return redirect(url_for("login"))

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect(url_for("login"))
    return render_template("dashboard.html")

@app.route("/generate")
def generate():
    if "user_id" not in session:
        return redirect(url_for("login"))
    return render_template("generate.html")

@app.route("/history")
def history():
    if "user_id" not in session:
        return redirect(url_for("login"))
    return render_template("history.html")

if __name__ == "__main__":
    app.run(debug=True)