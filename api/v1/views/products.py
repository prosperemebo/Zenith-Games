import random

#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Products """
from models.product import Product
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from slugify import slugify


@app_views.route('/products', methods=['GET'], strict_slashes=False)
def get_products():
    """
    Retrieves the list of all Products
    """
    products = storage.all(Product).values()
    products_list = []

    for product in products:
        products_list.append(product.to_dict())

    return jsonify(products_list)


@app_views.route('/products/<product_id>', methods=['GET'], strict_slashes=False)
def get_product(product_id):
    """ Retrieves a specific Product """
    product = storage.get(Product, product_id)

    if not product:
        abort(404)

    return jsonify(product.to_dict())


@app_views.route('/products', methods=['POST'], strict_slashes=False)
def post_product():
    """ Create new Product """
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

    instance = Product(**data)
    instance.save()

    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/products/<product_id>', methods=['PUT'], strict_slashes=False)
def put_product(product_id):
    """ Update product """
    product = storage.get(Product, product_id)
    data = request.get_json()

    if not product:
        abort(404)

    if not data:
        abort(400, description="Invalid data sent!")

    excluded_fields = ['id', 'created_at', 'updated_at']

    for key, value in data.items():
        if key not in excluded_fields:
            setattr(product, key, value)

    storage.save()
    return make_response(jsonify(product.to_dict()), 200)


@app_views.route('/products/<product_id>', methods=['DELETE'], strict_slashes=False)
def delete_product(product_id):
    """ Deletes product"""
    product = storage.get(Product, product_id)

    if not product:
        abort(404)

    storage.delete(product)
    storage.save()

    return make_response(jsonify({}), 200)

@app_views.route('/products/recommended', methods=['GET'], strict_slashes=False)
def get_random_products():
    """ Retrieves 10 random products for the home page """
    products = list(storage.all(Product).values())

    if len(products) <= 20:
        random_products = [product.to_dict() for product in products]
    else:
        random_products = random.sample(products, 20)
        random_products = [product.to_dict() for product in random_products]

    return jsonify(random_products)
