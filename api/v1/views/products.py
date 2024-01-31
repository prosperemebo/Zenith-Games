#!/usr/bin/python3
""" objects that handle all default RestFul API actions for States """
from models.product import Product
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/products', methods=['GET'], strict_slashes=False)
def get_states():
    """
    Retrieves the list of all Products
    """
    all_states = storage.all(State).values()
    list_states = []
    for state in all_states:
        list_states.append(state.to_dict())
    return jsonify(list_states)