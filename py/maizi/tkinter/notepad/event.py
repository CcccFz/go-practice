__author__ = 'Administrator'

from tkinter import *
import tkinter.messagebox
root = Tk()

#def button1Click():
#    print("button clicked")

#button = Button(text='hello',command=button1Click)  #label无法用command绑定事件
#button.pack()
#button.mainloop()

def callback(event):
    frame.focus_set()
    print("clicked at:", event.x, event.y)

def key(event):
    print("pressed", repr(event.char))

def closeWindow():
    if tkinter.messagebox.askokcancel('Quit','Do you want to exit'):
        root.destroy()

frame = Frame(root, width=100,height=100)
frame.bind('<Button-1>',callback)
frame.bind('<Key>',key)

root.protocol('WM_DELETE_WINDOW',closeWindow)

frame.pack()
frame.mainloop()

