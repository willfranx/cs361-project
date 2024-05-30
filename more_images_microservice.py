import zmq
import json
import requests

# Set up the ZeroMQ context and socket
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://localhost:5555")

while True:
    message = socket.recv_string()
    print(f"Received request: {message}")

    response = requests.get(f"https://images-api.nasa.gov/search?q={message}&media_type=image&page_size=20")
    data = response.json()

    socket.send_json(data)