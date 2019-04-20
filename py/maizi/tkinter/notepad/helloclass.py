__author__ = 'Administrator'

from Tkinter import *

class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.button = Button(frame, text = 'Hello class', fg = 'red', command = frame.quit)
        self.button.pack()
        self.hiButton = Button(frame, text='Say Hi', command = self.say_hi)
        self.hiButton.pack()

    def say_hi(self):
        print("hi Sunday, Thanks!")

root = Tk()
app = App(root)
root.mainloop()
