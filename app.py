import eventlet 
from flask import Flask, jsonify
from flask_socketio import SocketIO, join_room, leave_room
from flask_pymongo import PyMongo

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
def handleMessage(data):
    room = data['room']
    socketio.emit('messaged', data, room=room)

@socketio.on('join')
def handleJoin(data):
    who = data['who']
    room = data['room']
    join_room(room)
    socketio.emit('joined', who + ' joined the room', room=room)

if __name__ == '__main__':
    socketio.run(app)