import zmq

# Create a ZeroMQ context
context = zmq.Context()

# Create a REP (Reply) socket
socket = context.socket(zmq.REP)

# Bind the socket to a specific address
socket.bind("tcp://localhost:7777")

while True:
    # Wait for a request from the client
    request = socket.recv_string()
    print(f"Received request: {request}")

    if request == "about":
        # Send a response to the client
        socket.send_string("Near-Earth Objects (NEOs) are comets and asteroids that have been nudged by the gravitational attraction of nearby planets into orbits that allow them to enter the Earth's neighborhood.")