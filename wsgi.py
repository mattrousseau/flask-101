# pylint: disable=missing-docstring

from flask import Flask, jsonify, abort
app = Flask(__name__)

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

@app.route('/api/v1/products')
def index_products():
    return jsonify(list(PRODUCTS.values()))

@app.route('/api/v1/products/<int:product_id>')
def show_product(product_id):
    product = PRODUCTS.get(product_id)

    if product is None:
        # abort(404)
        return "Product not found", 404

    return jsonify(product), 200
