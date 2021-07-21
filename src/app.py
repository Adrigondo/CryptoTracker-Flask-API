from flask import Flask, request, jsonify
from flask_pymongo import PyMongo, ObjectId
from flask_cors import CORS
import os

app = Flask(__name__)
app.config["MONGO_URI"] = os.environ["FLASK_ADRIGONDO_URI"]

mongo = PyMongo(app)

CORS(app)

db = mongo.db.users


@app.route("/users", methods=["POST"])
def createUser():
  user = request.json
  id = db.insert(user)
  # print(request.json)
  return jsonify(str(ObjectId(id)))
  # return "Recibido"


@app.route("/users", methods=["GET"])
def getUsers():
  users = [doc for doc in db.find()]
  for user in users:
    user["_id"] = str(ObjectId(user["_id"]))
  return jsonify(users)


@app.route("/users/<id>", methods=["GET"])
def getUser(id):
  user = db.find_one({"_id": ObjectId(id)})
  user["_id"] = str(ObjectId(user["_id"])),
  return jsonify(user)


@app.route("/users/<id>", methods=["DELETE"])
def deleteUser(id):
  db.delete_one({"_id": ObjectId(id)})
  return jsonify({"msg": "User deleted"})


@app.route("/users/<id>", methods=["PUT"])
def updateUser(id):
  db.update_one({"_id": ObjectId(id)}, {"$set": request.json})
  return jsonify({"msg": "User updated"})


if __name__ == "__main__":
  app.run(debug=True)
