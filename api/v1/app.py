#!/usr/bin/python3

#!/usr/bin/python3
"""
Flask server (variable app)
"""

from flask import Flask, jsonify
from models import storage
from os import getenv
from api.v1.views import app_views
from flask_cors import CORS  # Import the CORS class

app = Flask(__name__)
CORS(app, resources={r"/api/v1/*": {"origins": "0.0.0.0"}})  # Configure CORS for /*

app.register_blueprint(app_views)
app.url_map.strict_slashes = False

# ... (rest of your code)

if __name__ == "__main__":
    host = getenv('HBNB_API_HOST')
    port = getenv('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)

