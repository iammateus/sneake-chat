import eventlet 
from flask import Flask, jsonify
from flask_socketio import SocketIO
from flask_pymongo import PyMongo

eventlet.monkey_patch()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config["MONGO_URI"] = "mongodb://root:docker@mongo:27017/todos?authSource=admin"
mongo = PyMongo(app)

socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/healthcheck")
def healthcheck():
    data = {'message': 'The server is running! (sneake-chat)'}
    return jsonify(data)

@socketio.on('message')
def handle_message(message):
    print('received message: ' + str(message))

if __name__ == '__main__':
    socketio.run(app)