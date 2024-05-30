import zmq

# Create a ZeroMQ context
context = zmq.Context()

# Create a REP (Reply) socket
socket = context.socket(zmq.REP)

# Bind the socket to a specific address
socket.bind("tcp://localhost:8989")

while True:
    # Wait for a request from the client
    request = socket.recv_string()

    print(f"Received request: {request}")

    if request == "about":
        # Send a response to the client
        socket.send_string("This application generates a random image from NASA's Astronomy Photo of the Day (APOD).")