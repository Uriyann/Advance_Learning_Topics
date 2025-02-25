from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

main = tk.Tk()
main.title("TEST PROJECT")
main.geometry("900x900")

label = Label(main, text= "NEKOOO CATTT", font= ('Times New Roman', 20),
             bg= 'white', width= 24, height= 2)
label.pack()

frame = tk.Frame(main, width= 800, height= 800, borderwidth= 10, 
                  relief= tk.GROOVE)
frame.propagate(False)
frame.pack()

ext_label = tk.Label(frame, text= "Good Feeling")
ext_label.pack()

image = Image.open(r"C:\Users\M S I\Downloads\e4140a754afb75b19463aefe149e65ab.webp")
image = ImageTk.PhotoImage(image)

image_label = tk.Label(frame, width= 750, height= 750, image=image)
image_label.pack()




main.mainloop()