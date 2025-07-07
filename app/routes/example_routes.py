from flask import Blueprint, request
from app.controllers.example_controller import example_function, send_message

example_bp = Blueprint('example', __name__)

@example_bp.route('/example', methods=['GET'])
def example_route():
    return example_function()

@example_bp.route('/chat/send_message', methods=['POST'])
def new_message_route():
    return send_message(request)