from flask_socketio import emit, join_room, leave_room
from flask import request
from datetime import datetime

def register_handlers(socketio):
    
    @socketio.on('join_chat')
    def handle_join_chat(data):
        username = data.get('username', 'Usuario')
        room = data.get('room', 'general')
        
        join_room(room)
        
        # Notificar a la sala que alguien se unió
        emit('user_joined', {
            'username': username,
            'message': f'{username} se unió a la sala {room}',
            'timestamp': datetime.now().strftime('%H:%M:%S')
        }, room=room)
        
        # Confirmar al usuario que se unió
        emit('joined_room', {
            'room': room,
            'message': f'Te uniste a la sala {room}'
        })
    
    @socketio.on('leave_chat')
    def handle_leave_chat(data):
        username = data.get('username', 'Usuario')
        room = data.get('room', 'general')
        
        leave_room(room)
        
        # Notificar a la sala que alguien se fue
        emit('user_left', {
            'username': username,
            'message': f'{username} dejó la sala {room}',
            'timestamp': datetime.now().strftime('%H:%M:%S')
        }, room=room)
    
    @socketio.on('send_message')
    def handle_send_message(data):
        username = data.get('username', 'Usuario')
        message = data.get('message', '')
        room = data.get('room', 'general')
        
        if message.strip():
            # Enviar mensaje a todos en la sala
            emit('receive_message', {
                'username': username,
                'message': message,
                'timestamp': datetime.now().strftime('%H:%M:%S')
            }, room=room)
    
    @socketio.on('typing')
    def handle_typing(data):
        username = data.get('username', 'Usuario')
        room = data.get('room', 'general')
        is_typing = data.get('typing', False)
        
        # Notificar a otros usuarios que alguien está escribiendo
        emit('user_typing', {
            'username': username,
            'typing': is_typing
        }, room=room, include_self=False)