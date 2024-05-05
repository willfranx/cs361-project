import tkinter as tk

from tkinter import messagebox

from tkinter import ttk
from ttkthemes import ThemedTk

from image_service import generate_image
from about_service import open_about_window


root = ThemedTk(theme="sun-valley")
root.title("APOD-Randomizer (APOD-R)")

# Set window size
window_width = 800
window_height = 600

# Get screen size
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate position
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)

# Set window size and position
root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")


label = ttk.Label(text="NASA Astronomy Picture of the Day (APOD) Randomizer!")
label.grid(row=0, column=0, columnspan=2)  # position the label in the first row

# Create a label to display the image
image_label = ttk.Label(root)
image_label.grid(row=1, column=0, sticky="nsew")  # position the label in the second row, first column

# Create a frame to contain the buttons
button_frame = ttk.Frame(root)
button_frame.grid(row=1, column=1, sticky="nsew")  # position the frame in the second row, second column


dir_button = ttk.Button(
    button_frame,  # parent widget is the button frame
    text="Generate image",
    command=lambda: generate_image(root, image_label, window_width, window_height)  # function to call when the directory button is clicked
)
dir_button.pack(side="top")  # pack the button into the frame

about_button = ttk.Button(
    button_frame,  # parent widget is the button frame
    text="About",
    command=lambda: open_about_window(root)  # function to call when the About button is clicked
)
about_button.pack(side="top")

def on_close():
    if messagebox.askokcancel("Warning", "You have images in your temp folder that have not been saved yet. Are you sure you want to exit?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_close)

root.grid_columnconfigure(0, weight=1)  # make the first column expandable
root.grid_rowconfigure(1, weight=1)  # make the second row expandable

root.mainloop()