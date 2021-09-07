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

@app.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    if request.method == "GET":
        result = {}

        for prod in products:
            if int(prod["product_id"]) == product_id:
                result = jsonify({"product": prod})
        return result

@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    if request.method == "DELETE":
        for prod in products:
            if int(prod["product_id"]) == product_id:
                products.remove(prod)
                result = jsonify({"products": products, 'message': 'product successfully deleted'})
        return result

if __name__ == "__main__":
    app.run('localhost:5000')
