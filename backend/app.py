from flask import Flask, send_from_directory
from flask_cors import CORS
from routes.recipes import recipes_bp
from routes.favorites import favorites_bp
import os

def create_app():
    app = Flask(__name__, static_folder=None)
    CORS(app)

    app.register_blueprint(recipes_bp, url_prefix="/api")
    app.register_blueprint(favorites_bp, url_prefix="/api")

    frontend_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "frontend")

    @app.route("/")
    def index():
        return send_from_directory(frontend_dir, "index.html")

    @app.route("/<path:path>")
    def static_proxy(path):
        return send_from_directory(frontend_dir, path)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)