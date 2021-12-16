# pylint: disable=missing-docstring

from flask import Flask, jsonify
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
}

@app.route('/')
def hello():
    return "Hi World!"

@app.route('/api/v1/products')
def products():
    return jsonify(PRODUCTS)

