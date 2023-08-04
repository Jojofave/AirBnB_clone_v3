#!/usr/bin/python3

from flask import Flask, Blueprint, jsonify, abort, make_response, request
from models import storage, City, Place

app = Flask(__name__)
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')


@app_views.route('/cities/<city_id>/places', methods=['GET'], strict_slashes=False)
def get_places(city_id):
    """Retrieve the list of all Place objects in a city."""
    # Implement the code to get all places from the specified city
    city = storage.get(City, city_id)
    if city is None:
        abort(404)

    places = city.places
    return jsonify([place.to_dict() for place in places])


# Implement the remaining views for GET, DELETE, POST, and PUT for individual places
# GET /api/v1/places/:place_id
# DELETE /api/v1/places/:place_id
# POST /api/v1/cities/:city_id/places
# PUT /api/v1/places/:place_id


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

