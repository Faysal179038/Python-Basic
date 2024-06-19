from tkinter import *
from PIL import Image, ImageTk

# List of food items
food = ["pizza", "hamburger", "hotdog"]


# Function to print the order based on selected radio button
def order():
    if x.get() == 0:
        print("You ordered pizza!")
    elif x.get() == 1:
        print("You ordered a hamburger!")
    elif x.get() == 2:
        print("You ordered a hotdog!")
    else:
        print("huh?")


# Initialize the main window
window = Tk()
window.geometry("720x720")


# Function to load image and handle errors
def load_image(path, size):
    try:
        img = Image.open(path)
        img = img.resize(size, Image.LANCZOS)  # Resize image
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Error loading image {path}: {e}")
        return None


# Desired image size
image_size = (50, 50)  # Change this to the size you want

# Load images for the food items using Pillow
pizzaPhoto = load_image("D:/learning/python/pizza.jpg", image_size)
hamburgerPhoto = load_image("D:/learning/python/hamburger.webp", image_size)
hotdogPhoto = load_image("D:/learning/python/hotdog.jpg", image_size)

# Check if images are loaded successfully
if not pizzaPhoto or not hamburgerPhoto or not hotdogPhoto:
    print("One or more images could not be loaded. Exiting.")
    window.destroy()
else:
    foodImages = [pizzaPhoto, hamburgerPhoto, hotdogPhoto]

    # IntVar to hold the value of the selected radio button
    x = IntVar()

    # Create and pack radio buttons
    for index in range(len(food)):
        radiobutton = Radiobutton(
            window,
            text=food[index],  # Add text to radio buttons
            variable=x,  # Group radiobuttons together if they share the same variable
            value=index,  # Assign each radiobutton a different value
            padx=25,  # Add padding on x-axis
            font=("Impact", 50),
            image=foodImages[index],  # Add image to radiobutton
            compound="left",  # Add image & text (left-side)
            command=order,  # Set command of radiobutton to function
        )
        radiobutton.pack(anchor=W)

    # Run the main loop
    window.mainloop()
