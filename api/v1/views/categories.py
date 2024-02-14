#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Categories """
from models.category import Category
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from slugify import slugify


@app_views.route('/categories', methods=['GET'], strict_slashes=False)
def get_categories():
    """ Retrieves the list of all Categories """
    valid_filters = ['parent_id', 'source_id', 'status', 'slug']
    
    filters = {key: request.args.get(key) for key in valid_filters if key in request.args}
    categories = storage.all(Category, **filters).values()
    categories_list = []

    for category in categories:
        categories_list.append(category.to_dict())

    return jsonify(categories_list)


@app_views.route('/categories/parent', methods=['GET'], strict_slashes=False)
def get_parent_categories():
    """ Retrieves the list of all Parent Categories """
    valid_filters = ['parent_id', 'source_id', 'status', 'slug']
    
    filters = { key: request.args.get(key) for key in valid_filters if key in request.args }
    
    if 'parent_id' not in filters:
        filters['parent_id'] = None
    
    categories = storage.all(Category, **filters).values()
    categories_list = []

    for category in categories:
        categories_list.append(category.to_dict())

    return jsonify(categories_list)


@app_views.route('/categories/<category_id>', methods=['GET'], strict_slashes=False)
def get_category(category_id):
    """ Retrieves a specific Category """
    category = storage.get(Category, category_id)

    if not category:
        abort(404)

    return jsonify(category.to_dict())


@app_views.route('/categories', methods=['POST'], strict_slashes=False)
def post_category():
    """ Create new Category """
    if not request.get_json():
        abort(400, description="Not a JSON")

    data = request.get_json()

    if 'label' not in data:
        abort(400, description="label cannot be null!")

    if 'source_id' not in data:
        abort(400, description="source_id cannot be null!")

    if 'slug' not in data:
        label = data.get('label')
        data['slug'] = slugify(label)

    instance = Category(**data)
    instance.save()

    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/categories/<category_id>', methods=['PUT'], strict_slashes=False)
def put_category(category_id):
    """ Update Category """
    category = storage.get(Category, category_id)
    data = request.get_json()

    if not category:
        abort(404)

    if not data:
        abort(400, description="Invalid data sent!")

    excluded_fields = ['id', 'created_at', 'updated_at']

    for key, value in data.items():
        if key not in excluded_fields:
            setattr(category, key, value)

    storage.save()
    return make_response(jsonify(category.to_dict()), 200)


@app_views.route('/categories/<category_id>', methods=['DELETE'], strict_slashes=False)
def delete_category(category_id):
    """ Deletes product"""
    product = storage.get(Category, category_id)

    if not product:
        abort(404)

    storage.delete(product)
    storage.save()

    return make_response(jsonify({}), 200)
