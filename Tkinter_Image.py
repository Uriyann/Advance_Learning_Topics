from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

main = tk.Tk()
main.title("TEST PROJECT")
main.geometry("500x500")

label = Label(main, text= "MARK DE GUZMEN", font= ('Times New Roman', 20),
             bg= 'white', width= 24, height= 2)
label.pack()

frame = ttk.Frame(main, width= 300, height= 300, borderwidth= 10, 
                  relief= tk.GROOVE)
frame.propagate(False)
frame.pack()

ext_label = ttk.Label(frame, text= "Good mood")
ext_label.pack()

image = Image.open(r"C:\Users\M S I\Downloads\IMG20250211142852.jpg")
image = ImageTk.PhotoImage(image)

image_label = tk.Label(frame, width= 250, height= 250, image=image)
image_label.pack()




main.mainloop()