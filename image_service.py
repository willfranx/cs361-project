from PIL import Image, ImageTk
from tkinter import ttk

def generate_image(root):
    # Load the image (make sure the image is in the same directory as your script)
    image = Image.open("image.jpg")
    photo = ImageTk.PhotoImage(image)

    # Create a label and add the image to it
    image_label = ttk.Label(root, image=photo)
    image_label.image = photo  # keep a reference to the image
    image_label.pack()