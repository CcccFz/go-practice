__author__ = 'Administrator'

from tkinter import *

button = Button(text='SundyButton',padx=10,pady=10)
button.config(cursor='gumby',bd=8,relief=RAISED,bg='green',fg='yellow')
button.config(font=('Helvetica',10,'bold italic'))
button.pack()
mainloop()