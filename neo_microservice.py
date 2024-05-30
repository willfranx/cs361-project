import os
import zmq
import requests
from dotenv import load_dotenv
from datetime import datetime


load_dotenv()

# Create a ZeroMQ context
context = zmq.Context()

# Create a REP (Reply) socket
socket = context.socket(zmq.REP)

# Bind the socket to a specific address
socket.bind("tcp://localhost:6666")

# Get the current date
current_date = datetime.now()

# Format the date as "YYYY-MM-DD"
formatted_date = current_date.strftime("%Y-%m-%d")
print(formatted_date)

# Send a GET request to the API
api_key = os.getenv('NASA_API_KEY')
url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={formatted_date}&api_key={api_key}"

while True:
    # Wait for a request from the client
    request = socket.recv_string()

    if request == "get_data":
        # Process the request
        response = requests.get(url)
        print(response)
        response.raise_for_status()
        data = response.json()

        # Send the response to the client
        socket.send_json(data)