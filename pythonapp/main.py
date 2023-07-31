import tkinter as tk
from tkinter.messagebox import showinfo

root = tk.Tk()

def show_msg():
    showinfo("Some Titke", "Hello World")

btn = tk.Button(root, text="Click Me!", command=show_msg)
btn.pack()

root.mainloop()
