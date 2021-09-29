import tkinter as tk
from tkinter import ttk

han = tk.Tk()
han.title("Python Gui")
han.geometry("500x200")

def click_me():
    a.configure(text='Welcome to IPT 102' + " " + name.get())
    

a = ttk.Label(han, text="Result")
a.grid(column=0, row=3)

ttk.Label(han, text="Enter a name").grid(column=0, row=0)
action = ttk.Button(han, text="Show Results!" , command=click_me)
action.grid(column=1, row=4)

name = tk.StringVar()
name_entered = ttk.Entry(han, width=12, textvariable=name)
name_entered.grid(column=0, row=4)

han.mainloop()