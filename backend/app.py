from flask import Flask, jsonify, request
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from flask_cors import CORS


load_dotenv()


app = Flask(__name__)
CORS(app)


MONGO_URI = os.getenv('MONGO_URI')
client = MongoClient(MONGO_URI)
db = client['automobile_db']
collection = db['automobiles']


@app.route('/api/automobiles', methods=['GET'])
def get_automobiles():
    automobiles = list(collection.find({}, {'_id': 0}))
    return jsonify(automobiles)


@app.route('/api/automobiles/search', methods=['GET'])
def search_automobiles():
    query = request.args.get('query', '')
    min_price = request.args.get('min_price', 0, type=int)
    max_price = request.args.get('max_price', float('inf'), type=float)
    fuel = request.args.get('fuel', '')
    transmission = request.args.get('transmission', '')
    max_power = request.args.get('max_power', float('inf'), type=float)

    filters = {
        "full_name": {"$regex": query, "$options": "i"},
        "price": {"$gte": min_price, "$lte": max_price},
        "power_hp": {"$lte": max_power}
    }

    if fuel:
        filters["fuel"] = fuel
    if transmission:
        filters["transmission"] = transmission

    results = list(collection.find(filters, {'_id': 0}))
    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True)
