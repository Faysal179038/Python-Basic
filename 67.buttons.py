from tkinter import *
from PIL import Image, ImageTk

# button = you click it, then it does stuff

count = 0


def click():
    global count
    count += 1
    print(count)


window = Tk()

# Load the image using PIL
file_path = "D:/learning/python/logo2.jpg"
pil_image = Image.open(file_path)
photo = ImageTk.PhotoImage(pil_image)

button = Button(
    window,
    text="click me! to pet me",
    command=click,
    font=("Comic Sans", 30),
    fg="#FFFFFF",
    bg="black",
    state=ACTIVE,
    image=photo,
    compound="bottom",
)
button.pack()

window.mainloop()
