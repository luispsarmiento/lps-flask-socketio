
import socketio

class ChatService:
    @staticmethod
    def send_message(user_received, msg):
        sio = socketio.Client()
        sio.connect('https://reimagined-space-yodel-jr7rwww4wvp2gr-5000.app.github.dev')  # Adjust the URL as needed
        sio.emit('send_message_to_user', {
            'username': 'User API',
            'message': msg,
            'to': user_received  # Use 'to' or the correct key expected by your server
        })
        sio.sleep(1)  # Wait for 1 second to ensure the message is sent
        sio.disconnect()
