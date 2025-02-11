import tkinter as tk
from PIL import Image, ImageTk

# Create the main window
parent = tk.Tk()
parent.title("TEST PROJECT")
parent.geometry("500x500")

# Load and display an image 
image = Image.open(r"C:\Users\M S I\Downloads\6d4fc21ede384265bf089310ab4e8a57.jpeg")
image = ImageTk.PhotoImage(image)

# Create a label to display the image
image_label = tk.Label(parent, image=image)
image_label.pack()

# Start the Tkinter event loop
parent.mainloop()
