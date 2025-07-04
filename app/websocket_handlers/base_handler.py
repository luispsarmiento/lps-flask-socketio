from flask_socketio import emit, disconnect
from flask import request
import logging

def register_handlers(socketio):
    
    @socketio.on('connect')
    def handle_connect(auth):
        print(f'Cliente conectado: {request.sid}')
        emit('status', {'msg': f'Usuario {request.sid} conectado'})
    
    @socketio.on('disconnect')
    def handle_disconnect():
        print(f'Cliente desconectado: {request.sid}')
    
    @socketio.on('ping')
    def handle_ping():
        emit('pong', {'data': 'pong'})