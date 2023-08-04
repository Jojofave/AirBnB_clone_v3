#!/usr/bin/python3
from flask import Flask, Blueprint, jsonify, abort, make_response, request
from models import storage, User

app = Flask(__name__)
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    """Retrieve the list of all User objects."""
    # Implement the code to get all users from the storage
    users = storage.all(User).values()
    return jsonify([user.to_dict() for user in users])


# Implement the remaining views for GET, DELETE, POST, and PUT for individual users
# GET /api/v1/users/:user_id
# DELETE /api/v1/users/:user_id
# POST /api/v1/users
# PUT /api/v1/users/:user_id


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

