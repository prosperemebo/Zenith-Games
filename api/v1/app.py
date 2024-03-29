#!/usr/bin/python3
""" Flask Application """
from models import storage
from api.v1.views import app_views
from os import environ, getenv
from dotenv import load_dotenv
from flask import Flask, render_template, make_response, jsonify
from flask_cors import CORS

app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True
app.register_blueprint(app_views)
# cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
# cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


allowed_origins = [
    "http://localhost:3000",
    "http://prosperhack.tech",
    "https://prosperhack.tech",
    "http://www.prosperhack.tech",
    "https://www.prosperhack.tech",
    "http://api.prosperhack.tech",
    "http://www.api.prosperhack.tech",
    "https://api.prosperhack.tech",
    "https://www.api.prosperhack.tech",
]

cors = CORS(app, resources={r"/*": {"origins": allowed_origins}})

load_dotenv()


@app.teardown_appcontext
def close_db(error):
    """Close Storage"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """404 Error
    ---
    responses:
      404:
        description: a resource was not found
    """
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    """Main Function"""
    host = environ.get("API_HOST")
    port = environ.get("API_PORT")
    if not host:
        host = "0.0.0.0"
    if not port:
        port = "5000"
    app.run(host=host, port=port, threaded=True, debug=True)
