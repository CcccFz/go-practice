__author__ = 'Administrator'

from tkinter import *

root = Tk()
label = Label(root, text = 'Hello world')
label.config(cursor='gumby',width=10,height=10,fg='yellow',bg='dark green',font=('times','28','bold'))
label.pack()
root.mainloop()