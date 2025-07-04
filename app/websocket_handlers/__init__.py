from app.websocket_handlers import base_handler, chat_handler

def register_handlers(socketio):
    
    base_handler.register_handlers(socketio)
    chat_handler.register_handlers(socketio)