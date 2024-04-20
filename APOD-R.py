import tkinter as tk
from tkinter import messagebox, filedialog

def show_info_dialog():
    messagebox.showinfo("Information", "This is an informational dialog!")

def select_directory():
    directory = filedialog.askdirectory()  # open the directory chooser dialog
    print(f"Selected directory: {directory}")  # print the selected directory

window = tk.Tk()
label = tk.Label(text="NASA Astronomy Picture of the Day (APOD) Randomizer!")
label.pack()

info_button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    command=show_info_dialog  # function to call when the info button is clicked
)
info_button.pack()

dir_button = tk.Button(
    text="Select directory",
    width=25,
    height=5,
    command=select_directory  # function to call when the directory button is clicked
)
dir_button.pack()

show_info_dialog()  # call the function here to show the dialog on startup

window.mainloop()