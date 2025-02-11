from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

main = Tk()
main.title("TEST PROJECT")
main.geometry("500x500")

label = Label(main, text= "MARK DE GUZMEN", font= ('Times New Roman', 20),
             bg= 'white', width= 24, height= 2)
label.pack()


image = Image.open(r"C:\Users\M S I\Downloads\IMG20250211142852.jpg")
image = ImageTk.PhotoImage(image)

image_label = tk.Label(main, image=image)
image_label.pack()




main.mainloop()