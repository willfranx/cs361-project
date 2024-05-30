import zmq

import tkinter as tk
from tkinter import ttk

import webbrowser
from hyperlink import URL

# Create a ZeroMQ context
context = zmq.Context()

# Create a REQ (Request) socket
socket = context.socket(zmq.REQ)

# Connect the socket to the server's address
socket.connect("tcp://localhost:6666")

def open_neo_window(root):
    about_window = tk.Toplevel(root)
    about_window.title("2024 Near-Earth Objects (NEOs)")

    # Set window size
    window_width = 400
    window_height = 300

    # Get screen size
    screen_width = about_window.winfo_screenwidth()
    screen_height = about_window.winfo_screenheight()

    # Calculate position
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)

    # Set window size and position
    about_window.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    socket.send_string("get_data")

    # Receive the response from the server
    data = socket.recv_json()

    for date in data['near_earth_objects']:
        print(date)

    def format_data(data, indent=0):
        if isinstance(data, dict):
            return "\n".join(f"{' '*indent}{k}:\n{format_data(v, indent+2)}" if isinstance(v, (dict, list)) and k not in keys_to_skip else f"{' '*indent}{k}: {v}" for k, v in data.items() if k not in keys_to_skip)
        elif isinstance(data, list):
            return "\n".join(f"{' '*indent}{i}" if isinstance(i, str) else f"{' '*indent}\n{format_data(i, indent+2)}" for i in data)
        else:
            return f"{' '*indent}{data}"

    keys_to_skip = ['next', 'previous', 'self', 'links']

    # Create a Text widget with a monospace font
    text_widget = tk.Text(about_window, font=("Courier", 12))
    text_widget.pack(side="left", fill="both", expand=True)

    # Create a Scrollbar and associate it with the Text widget
    scrollbar = tk.Scrollbar(about_window, command=text_widget.yview)
    scrollbar.pack(side="right", fill="y")
    text_widget.config(yscrollcommand=scrollbar.set)

    # Sort the keys in descending order
    sorted_keys = sorted(data.keys(), reverse=True)

    for key in sorted_keys:
        formatted_data = format_data(data[key])
        text_widget.insert('end', formatted_data)
