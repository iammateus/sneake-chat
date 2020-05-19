from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://root:docker@mongo:27017/todos?authSource=admin"
mongo = PyMongo(app)

@app.route("/healthcheck")
def healthcheck():
    data = {'message': 'The server is running! (sneake-chat)'}
    return jsonify(data)

# start the development server using the run() method
if __name__ == "__main__":
    app.run()
    