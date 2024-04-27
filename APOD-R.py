import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
from ttkthemes import ThemedTk

def select_directory():
    directory = filedialog.askdirectory()  # open the directory chooser dialog
    print(f"Selected directory: {directory}")  # print the selected directory

root = ThemedTk(theme="sun-valley")
root.title("APOD-Randomizer (APOD-R)")

label = ttk.Label(text="NASA Astronomy Picture of the Day (APOD) Randomizer!")
label.pack()

dir_button = ttk.Button(
    text="Select directory",
    command=select_directory  # function to call when the directory button is clicked
)
dir_button.pack()

# Load the image (make sure the image is in the same directory as your script)
image = Image.open("image.jpg")
photo = ImageTk.PhotoImage(image)

# Create a label and add the image to it
image_label = ttk.Label(root, image=photo)
image_label.pack()

root.mainloop()