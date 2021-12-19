# pylint: disable=missing-docstring

from flask import Flask, jsonify, abort
app = Flask(__name__)

BASE_URL = '/api/v1'

PRODUCTS = {
    1: {
        'id': 1,
        'name': 'Skello'
    },
    2: {
        'id': 2,
        'name': 'Socialive.tv'
    },
    3: {
        'id': 3,
        'name': 'Le Wagon'
    },
}

@app.route('/')
def hello():
    return "Hi World!"

@app.route(f'{BASE_URL}/products', methods=['GET'])
def index_products():
    return jsonify(list(PRODUCTS.values()))

@app.route(f'{BASE_URL}/products/<int:product_id>', methods=['GET'])
def show_product(product_id):
    product = PRODUCTS.get(product_id)

    if product is None:
        return "Product not found", 404

    return jsonify(product), 200

@app.route(f'{BASE_URL}/products/<int:product_id>', methods=["DELETE"])
def delete_one_product(product_id):
    product = PRODUCTS.pop(product_id, None)

    if product is None:
        abort(404)

    return '', 204
