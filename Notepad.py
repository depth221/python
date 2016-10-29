from tkinter import *

def save():
    save = open('notepad.txt', 'w')
    print("File Opened")
    
    save.write(txt.get('1.0', END+'-1c'))
    print("File Saved")
    
    save.close()
    print("File Closed")

root = Tk()

txt = Text(root)
txt.grid(row = 0, column = 0)

btn = Button(root, text = "Save", width = 90, command = save)
btn.grid(row = 1, column = 0)

root.mainloop()
