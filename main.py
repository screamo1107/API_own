from flask import Flask
from flask_restful import Api, Resource, reqparse
import random
from data import dataMoney

app = Flask(__name__)
api = Api(app)

class Money(Resource):
    def get(self, id=0):
        if id == 0:
            return random.choice(dataMoney), 200
        for record in dataMoney:
            if record["id"] == id:
                return record, 200
        return "Record not found", 404

    def post(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("type")
        parser.add_argument("name")
        parser.add_argument("price")
        params = parser.parse_args()
        for quote in dataMoney:
            if id == quote["id"]:
                return f"Record with id {id} already exists", 400
        record = {
            "id": int(id),
            "type": params["type"],
            "name": params["name"],
            "price": params["price"]
        }
        dataMoney.append(record)
        return record, 201

    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("type")
        parser.add_argument("name")
        parser.add_argument("price")
        params = parser.parse_args()
        for record in dataMoney:
            if (id == record["id"]):
                record["type"] = params["type"]
                record["name"] = params["name"]
                record["price"] = params["price"]
                return record, 200

        record = {
            "id": id,
            "type": params["type"],
            "name": params["name"],
            "price": params["price"]
        }

        dataMoney.append(record)
        return record, 201

    def delete(self, id):
        global dataMoney
        dataMoney = [record for record in dataMoney if record["id"] != id]
        return f"Record with id {id} is deleted.", 200


api.add_resource(Money, "/money", "/money/", "/money/<int:id>")
if __name__ == '__main__':
    app.run(debug=True)