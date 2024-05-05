import tkinter as tk
from tkinter import ttk
from image_service import generate_image
from ttkthemes import ThemedTk

root = ThemedTk(theme="sun-valley")
root.title("APOD-Randomizer (APOD-R)")

label = ttk.Label(text="NASA Astronomy Picture of the Day (APOD) Randomizer!")
label.pack()

dir_button = ttk.Button(
    text="Generate image",
    command=lambda: generate_image(root)  # function to call when the directory button is clicked
)
dir_button.pack()


root.mainloop()