from flask import Flask, request, jsonify
from flask_pymongo import PyMongo, ObjectId
from flask_cors import CORS
import os

app = Flask(__name__)
app.config["MONGO_URI"] = os.environ["FLASK_ADRIGONDO_URI"]

mongo = PyMongo(app)

CORS(app)

db = mongo.db.users

@app.route("/", methods=["GET"])
def menu():
  try:
    return "API Flask - Crypto Tracker"
  except error:
    return (str(error))

@app.route("/users", methods=["POST"])
def createUser():
  user = request.json
  try:
    id = db.insert(user)
    return jsonify(str(ObjectId(id)))
  except error:
    return (str(error))
  # print(request.json)
  # return "Recibido"


@app.route("/users", methods=["GET"])
def getUsers():
  users = [doc for doc in db.find()]
  for user in users:
    user["_id"] = str(ObjectId(user["_id"]))
  return jsonify(users)


@app.route("/users/<username>", methods=["GET"])
def getUser(username):
  user = db.find_one({"username": username})
  user["_id"] = str(ObjectId(user["_id"]))
  return jsonify(user)


@app.route("/users/<id>", methods=["DELETE"])
def deleteUser(id):
  db.delete_one({"_id": ObjectId(id)})
  return jsonify({"msg": "User deleted"})


@app.route("/users/<username>", methods=["PUT"])
def updateUser(username):
  db.update_one({"username": username}, {"$set": request.json})
  return jsonify({"msg": "User updated"})


# if __name__ == "__main__":
#   app.run(debug=True)
