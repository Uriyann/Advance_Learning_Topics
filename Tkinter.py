from tkinter import *
import tkinter


main = Tk()
main.title("TEST PROJECT")
main.geometry("500x500")

label_label= StringVar()

label = Label(main, textvariable= label_label, font= ('Times New Roman', 20),
             bg= 'white', width= 24, height= 2)
label.pack()

main.mainloop()