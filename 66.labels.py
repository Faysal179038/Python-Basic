from tkinter import *
from PIL import Image, ImageTk

# label = an area widget that holds text and/or an image within a window

window = Tk()
window.geometry("720x720")


# Load the image using PIL
file_path = "D:/learning/python/logo2.jpg"
pil_image = Image.open(file_path)
photo = ImageTk.PhotoImage(pil_image)

label = Label(
    window,
    text="bro, do you even code?",
    font=("Arial", 40, "bold"),
    fg="#00FF00",
    bg="black",
    relief=RAISED,
    bd=10,
    padx=20,
    pady=20,
    image=photo,
    compound="bottom",
)
label.pack()
# label.place(x=0,y=0)

window.mainloop()
