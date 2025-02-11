import tkinter as tk
from tkinter import ttk

main = tk.Tk()
main.title("WIDGET TEST")
main.geometry("800x500")

label = tk.Label(master= main, text= "Wala Nang Peraaaa", font=("Times New Roman", 20))
label.pack()

text = tk.Text(master= main)
text.pack()




main.mainloop()