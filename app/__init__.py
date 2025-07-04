from flask import Flask
from flask_socketio import SocketIO

from app.websocket_handlers import register_handlers

socketio = SocketIO()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.configs.development')  # Default to development config

    app.config['SECRET_KEY'] = 'secret!'
    socketio.init_app(app, cors_allowed_origins="*")

    # Import and register blueprints here
    from app.routes.example_routes import example_bp
    from app.routes.web.index_routes import main_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(example_bp)


    register_handlers(socketio)

    return app