from flask import Flask, render_template
from flask_socketio import SocketIO, emit
    
app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('my event')
def test_message(message):
    print(message["data"])
    emit('my response', {'data': 'Sever: I received the following message - ' + message["data"]})

print("Starting app")
socketio.run(app)