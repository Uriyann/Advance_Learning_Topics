from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

main = tk.Tk()
main.title("TEST PROJECT")
main.geometry("900x900")

label = Label(main, text= "ROCKY ROALD", font= ('Times New Roman', 20),
             bg= 'white', width= 24, height= 2)
label.pack()

frame = ttk.Frame(main, width= 750, height= 750, borderwidth= 10, 
                  relief= tk.GROOVE)
frame.propagate(False)
frame.pack()

ext_label = ttk.Label(frame, text= "Good mood")
ext_label.pack()

image = Image.open(r"C:\Users\M S I\Downloads\b7e451f4-a649-4c8b-a46e-64c0cd3d6e32.jpg")
image = ImageTk.PhotoImage(image)

image_label = tk.Label(frame, width= 700, height= 700, image=image)
image_label.pack()




main.mainloop()