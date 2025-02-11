import tkinter as tk

main = tk.Tk()
main.title("WIDGET TEST")
main.geometry("800x500")

text = tk.Text(master= main)
text.pack()

main.mainloop()