import tkinter as tk
from tkinter import ttk

main = tk.Tk()
main.title("WIDGET TEST")
main.geometry("900x900")

label = tk.Label(master= main, text= "Wala Nang Peraaaa", font=("Times New Roman", 20))
label.pack()

text = tk.Text(master= main)
text.pack()

entry = ttk.Entry(master= main)
entry.pack()

another_label = tk.Label(master= main, text= "my label", font=("Times New Roman", 20))
another_label.pack()

button = ttk.Button(master= main, text= "A Button", command= main.destroy)
button.pack()

another_button = ttk.Button(master= main, text= "Hello Button", command= lambda: print("hello"))
another_button.pack()

main.mainloop()