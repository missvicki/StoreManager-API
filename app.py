import json
from flask import Flask, jsonify, request
from models.products import products, product

app = Flask(__name__)

@app.route("/")
def index_page():
    return "Welcome to Storemanager"

@app.route('/products/', methods=["GET", "POST"])
def get_products():
    if request.method == "GET":
        return jsonify({"products": products})
    
    elif request.method == "POST":
        products.append(product)
        return jsonify({"products": products})

@app.route("/products/<int:id>", methods=["GET"])
def get_product(id):
    if request.method == "GET":
        result = {}

        for product in products:
            if int(product["id"]) == id:
                result = jsonify({"product": product})
        return result

@app.route("/products/<int:id>", methods=["DELETE"])
def delete_product(id):
    if request.method == "DELETE":
        for product in products:
            if product["id"] == id:
                products.remove(product)
                result = jsonify({"products": products, 'message': 'product successfully deleted'})
        return result

if __name__ == "__main__":
    app.run('localhost:5000')
