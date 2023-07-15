# ui for the summeriser App(takes in the file name)

import tkinter as tk
from tkinter import ttk
import summeriser
from tkinter import messagebox

#function for getting the submit

def submitOpen():
    print(entry1.get())
    return summeriser.fileopener(entry1.get())

def infoDisplay():
    return messagebox.showinfo("App information", "app version 1 made by Lee")


#Frame elements

root = tk.Tk()


ttk.Style(root)


ttk.Label(text="input filepath here", font=8).pack(padx="50",pady="25")
entry1 = ttk.Entry(root)
entry1.pack()
ttk.Button(root,text="submitFile", padding=6, command = submitOpen).pack(padx="25",pady="25")
ttk.Button(root,text="information", padding=6, command = infoDisplay).pack(pady="25")


tk.mainloop()