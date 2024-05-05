# image_service.py

import io
import requests
import json
from PIL import Image, ImageTk
from tkinter import ttk

def generate_image(root, image_label, window_width, window_height):
    url = "https://api.nasa.gov/planetary/apod?count=1&api_key=6dtniaxOZcCirD2tJ2UlG8hUxSYxlI5GwxCFlCcH"
    response = requests.get(url)
    response.raise_for_status()
    data = json.loads(response.text)[0]  # get the first item from the JSON response

    # Fetch the image
    image_url = data['url']
    image_response = requests.get(image_url, stream=True)
    image_response.raise_for_status()
    image_data = image_response.content
    image = Image.open(io.BytesIO(image_data))

    # Calculate the aspect ratio of the image
    image_ratio = image.width / image.height

    # Calculate the new width and height of the image based on its aspect ratio and the size of the window
    new_width = window_width
    new_height = int(window_width / image_ratio)

    # If the new height is greater than the height of the window, adjust the new width and height
    if new_height > window_height:
        new_height = window_height
        new_width = int(window_height * image_ratio)

    # Resize the image
    image = image.resize((new_width, new_height))

    photo = ImageTk.PhotoImage(image)

    # Update the image of the label
    image_label.config(image=photo)
    image_label.image = photo # keep a reference to the image