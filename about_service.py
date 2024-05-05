# about_service.py

import tkinter as tk
from tkinter import ttk

def open_about_window(root):
    about_window = tk.Toplevel(root)
    about_window.title("About this app")

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

    about_label = ttk.Label(about_window, text="This is a random image generator app using NASA's APOD API.")
    about_label.pack()