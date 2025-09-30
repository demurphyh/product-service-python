from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/products', methods=['GET'])
def home():
    products = [
        { "id": 1, "name": "Dog Food", "price": 19.99 },
        { "id": 2, "name": "Cat Food", "price": 34.99 },
        { "id": 3, "name": "Bird Seeds", "price": 10.99 }
    ]
    return jsonify(products)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=3030,debug=True)