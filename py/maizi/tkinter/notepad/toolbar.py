__author__ = 'Administrator'

from tkinter import *


def callback():
    print("called the tool bar button")

root = Tk()
toolbar = Frame(root)
b = Button(toolbar,text='new',width=6,command=callback)
b.pack(side=LEFT,padx=2,pady=2)

c = Button(toolbar,text='new',width=6,command=callback)
c.pack(side=LEFT,padx=2,pady=2)

toolbar.pack(side=TOP,fill=X)
root.mainloop()