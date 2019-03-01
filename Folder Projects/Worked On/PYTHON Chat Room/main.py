from flask import Flask, render_template
from flask_socketio import SocketIO
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)


@app.route('/')
def sessions():
    return render_template('sessions.html')


@socketio.on('event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    data = json["data"]
    print(data)
    if data == "MESSAGE SENT":
        print("%s: %s" % (json["username"], json["message"]))
    elif data == "USER CONNECTED":
        print("A NEW CONNECTION WAS MADE")
    elif data == "USER DISCONNECTED":
        print("A USER DISCONNECTED")
    socketio.emit('response', json)


if __name__ == '__main__':
    socketio.run(app)