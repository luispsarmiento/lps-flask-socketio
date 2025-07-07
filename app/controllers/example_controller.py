def example_function():
    return {"message": "Hello from the controller!"}

def send_message(req):
    user_received = req.get_json().get("user_received", "default_user")
    from app.services.chat_service import ChatService
    ChatService.send_message(user_received, "This is a new message from the controller!")
    return {"message": "New message sended!"}