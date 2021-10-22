import tkinter as tk
from tkinter import *
from tkinter import ttk # why?

class Fate_Realm(Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.pack()
        self.master.title("Fate's Realm")
        self.button1 = Button(self, text="Done", width = 25, command= self.get_group_window)
        self.button1.grid(row=0, column=1, columnspan=2, sticky=W+E+N+S)

    def get_group_window(self):
        self.newWindow = Fate_Group()

class Fate_Group(Frame):
    def __init__(self):
        group_window = tk.Frame.__init__(self)
        group_window = Toplevel(self) # Why?
        group_window.title("Fate")
        group_window.button = tk.Button(text="Understood", width= 25, command=self.close_window)
        group_window.button.pack() # I dont get this

    def close_window(self):
        self.destroy()

def main():
    Fate_Realm().mainloop()

if __name__ == "__main__":
    main()