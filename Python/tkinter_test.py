from tkinter import *

class window:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.frame.pack(expand = True, fill = BOTH)
        self.label = Label(self.frame, text='my notepad')
        self.label.pack()
        self.text = Text(self.frame, undo = True, height = 20, width = 70)
        self.text.pack(expand = True, fill = BOTH)
        self.text.get("1.0")
root = Tk()
window = window(root)
root.mainloop()