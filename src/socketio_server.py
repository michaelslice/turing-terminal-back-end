import os
import socketio
import eventlet
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

sio = socketio.Server(async_mode='eventlet', cors_allowed_origins='*')
django_app = get_wsgi_application()
application = socketio.WSGIApp(sio, django_app)
from chat.models import Chats
from userbiography.model import UserAccount

'''
Handle the clients connection, and assign them a sid
sid represents the unique session identifier for the connected user
'''
@sio.event
def connect(sid, environ):
    print('Client connected:', sid)
    all_comments = Chats.objects.all()
    comments_list = [{'user': comment.user.user_name, 'comment': comment.message} for comment in all_comments]
    
    sio.emit('load comments', comments_list)
    
'''
Handle clients disconnecting from the web socket
'''
@sio.event
def disconnect(sid):
    print('Client disconnected:', sid)

'''
Handle the clients comment, and upload to the Chats table
'''
@sio.on('chat message')
def handle_message(sid, msg):
    print('Message from {}: {}'.format(sid, msg))
    
    # {'user': 'michaelslice', 'comment': 'test'}
    user = msg['user']
    comment = msg['comment']
    
    # Query the username, for user_id, and save to Chats table 
    current_user = UserAccount.objects.get(user_name=user)
    data = Chats(user=current_user, message=comment, )
    data.save()
    
    # Emit the msg back to the client
    sio.emit('chat message', {'user': user, 'comment': comment})

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('127.0.0.1', 4000)), application)