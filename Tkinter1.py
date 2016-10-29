from tkinter import *
from tkinter import messagebox

def onclick():
    name = txt.get()
    messagebox.showinfo("이름", name)

root = Tk()

lbl = Label(root, text = "이름")
lbl.grid(row = 0, column = 0)

txt = Entry(root)
txt.grid(row = 0, column = 1)

btn = Button(root, text = "OK", command = onclick)
btn.grid(row = 1, column = 1)

root.mainloop()
