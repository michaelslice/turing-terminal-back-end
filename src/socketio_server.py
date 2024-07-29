import os
import socketio
import eventlet
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

sio = socketio.Server(async_mode='eventlet', cors_allowed_origins='*')
django_app = get_wsgi_application()
application = socketio.WSGIApp(sio, django_app)

@sio.event
def connect(sid, environ):
    print('Client connected:', sid)

@sio.event
def disconnect(sid):
    print('Client disconnected:', sid)

@sio.on('chat message')
def handle_message(sid, msg):
    print('Message from {}: {}'.format(sid, msg))
    sio.emit('chat message', msg)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('127.0.0.1', 4000)), application)
