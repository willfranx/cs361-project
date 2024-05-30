# about_service.py

import tkinter as tk
from tkinter import ttk

import zmq

# Set up the ZeroMQ context and socket
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:7777")

def open_about_neo_window(root):
    about_window = tk.Toplevel(root)
    about_window.title("About Near-Earth Objects (NEOs)")

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

    socket.send_string("about")
    response = socket.recv_string()
    print(response)

    # Create a Text widget
    about_text = tk.Text(about_window, wrap=tk.WORD)
    about_text.insert(tk.END, response)
    about_text.pack()

    # Disable editing
    about_text.config(state=tk.DISABLED)