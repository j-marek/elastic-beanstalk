from flask import Flask, render_template, jsonify
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Flask application
application = Flask(__name__)


# Routes
@application.route("/")
def home():
    # Get environment information
    env_info = {
        "FLASK_ENV": os.environ.get("FLASK_ENV", "not set"),
    }

    return render_template(
        "index.html",
        db_status="Not Required",
        db_info="Database connection removed",
        env_info=env_info,
    )


@application.route("/health")
def health():
    # Simple health check
    return jsonify(status="healthy")


@application.route("/api/info")
def info():
    return jsonify(
        {
            "service": "Dockerized Flask App",
            "version": "1.0.0",
            "environment": os.environ.get("FLASK_ENV", "development"),
        }
    )


# Run the application
if __name__ == "__main__":
    # For local development only
    application.run(host="0.0.0.0", port=5000, debug=True)
