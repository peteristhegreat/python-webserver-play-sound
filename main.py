from flask import Flask, request
from playsound import playsound
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    # Getting the user's IP
    user_ip = request.remote_addr

    # Getting the current date and time
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Playing the .mp3 file
    playsound('tada.wav')

    print(f"Date and Time: {current_datetime}, IP: {user_ip}")

    return "Sound played."


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
