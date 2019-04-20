__author__ = 'Administrator'

from Tkinter import *
import Tkinter.messagebox

def callback():
    if Tkinter.messagebox.showerror('Sundy', 'Hi sundy'):
        print('clicked Yes')
    else:
        print('clicked No')

root = Tk()
button = Button(root,text='Button1',command=callback)
button.pack()
root.mainloop()
