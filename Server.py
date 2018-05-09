import socketio
import eventlet
from flask import Flask
import threading

sio = socketio.Server(logger=True)
app = Flask(__name__)


@sio.on('connect')
def connect(sid, environ):
    print('client_connect', sid)
    sio.emit(
        'connected_to_server',
        {'message': 'Connected', 'count': 'not needed yet'},
        room=sid
    )


@sio.on('freq_change')
def freq_change(sid, data):
    print(data)
    sio.emit('freq', data)

app = socketio.Middleware(sio, app)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('localhost', 9876)), app)
