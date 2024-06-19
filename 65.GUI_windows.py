from tkinter import *
from PIL import Image, ImageTk

# Create the main window
window = Tk()  # instantiate an instance of a window
window.geometry("720x720")
window.title("CodeForgeGrowth first GUI program")

# Load the image using Pillow
image = Image.open("D:/learning/python/logo.jpg")
# # Convert the image to a format tkinter can use
icon = ImageTk.PhotoImage(file="D:/learning/python/logo.jpg")
window.iconphoto(True, icon)
# window.config(background="#5cfcff")

# Create a label and set the image
label = Label(window, image=icon)
label.pack()

window.mainloop()  # place window on computer screen, listen for events
