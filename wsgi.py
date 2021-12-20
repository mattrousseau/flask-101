# pylint: disable=missing-docstring
import itertools

from flask import Flask, jsonify, abort, request

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

START_INDEX = len(PRODUCTS) + 1
IDENTIFIER_GENERATOR = itertools.count(START_INDEX)

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

@app.route(f'{BASE_URL}/products', methods=["POST"])
def create_one_product():
    data = request.get_json()
    name = data.get('name')

    if name is None:
        abort(400)

    if name == '' or not isinstance(name, str):
        abort(422)

    next_id = next(IDENTIFIER_GENERATOR)
    PRODUCTS[next_id] = {'id': next_id, 'name': name}

    return jsonify(PRODUCTS[next_id]), 201
