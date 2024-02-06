from flask import Flask


def create_app():
    """Factory pattern for Flask application"""

    app = Flask(__name__)

    return app