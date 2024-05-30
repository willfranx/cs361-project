import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

from PIL import Image, ImageTk
import io
import urllib.request

import webbrowser

from ttkthemes import ThemedTk

import more_images_client

from image_service import generate_image
from about_client import open_about_window
from neo_client import open_neo_window
from about_neo_client import open_about_neo_window


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
    command=lambda: generate_and_update()  # function to call when the directory button is clicked
)
dir_button.pack(side="top")  # pack the button into the frame

about_button = ttk.Button(
    button_frame,  # parent widget is the button frame
    text="About this app",
    command=lambda: open_about_window(root)  # function to call when the About button is clicked
)
about_button.pack(side="top")

neo_button = ttk.Button(
    button_frame,  # parent widget is the button frame
    text="View this week's Near-Earth Objects (NEOs)",
    command=lambda: open_neo_window(root)  # function to call when the About button is clicked
)
neo_button.pack(side="top")

about_neo_button = ttk.Button(
    button_frame,  # parent widget is the button frame
    text="About Near-Earth Objects (NEOs)",
    command=lambda: open_about_neo_window(root)  # function to call when the About button is clicked
)
about_neo_button.pack(side="top")

# Create a new frame at the bottom of the window
info_frame = tk.Frame(root)
info_frame.grid(sticky='we')

# Create labels for the title, copyright, explanation, and url
title_label = tk.Label(info_frame, text=['title'])
copyright_label = tk.Label(info_frame, text=['copyright'])
explanation_button = tk.Button(info_frame, text="Show explanation")
url_label = tk.Label(info_frame, text=['url'], fg="blue", cursor="hand2")
similar_images_button = tk.Button(info_frame, text="Show more images")


def generate_and_update():
    info = generate_image(root, image_label, window_width, window_height)
    dir_button.config(text="Generate another image")
    title_label.config(text=info['title'])
    copyright_label.config(text=info['copyright'])
    url_label.config(text=info['url'])
    explanation_button.config(command=lambda: messagebox.showinfo("Explanation", info['explanation']))
    more_image_urls = more_images_client.search_for_more_images(info['explanation'])
    similar_images_button.config(command=lambda: display_images(more_image_urls))

def open_url(event):
    webbrowser.open_new(event.widget.cget("text"))
# Bind a click event to the url label
url_label.bind("<Button-1>", open_url)

def display_images(urls):
    # Create a new window
    image_window = tk.Toplevel(root)

    # Load and display each image
    for url in urls:
        try:
            with urllib.request.urlopen(url) as u:
                raw_data = u.read()
        except urllib.error.HTTPError:
            print(f"Failed to fetch image from {url}")
            continue

        im = Image.open(io.BytesIO(raw_data))

        # Resize the image
        max_size = (300, 300)
        im.thumbnail(max_size)

        image = ImageTk.PhotoImage(im)
        label = tk.Label(image_window, image=image)
        label.image = image  # keep a reference to the image to prevent it from being garbage collected
        label.pack()


similar_images_button.pack()
# Pack the labels into the frame
title_label.pack()
copyright_label.pack()
explanation_button.pack()
url_label.pack()

def on_close():
    if messagebox.askokcancel("Warning", "You have images in your temp folder that have not been saved yet. Are you sure you want to exit?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_close)

root.grid_columnconfigure(0, weight=1)  # make the first column expandable
root.grid_rowconfigure(1, weight=1)  # make the second row expandable

root.mainloop()