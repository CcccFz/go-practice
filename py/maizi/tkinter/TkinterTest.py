# -- coding: utf-8 --

import os
import time
from functools import partial as pto
import Tkinter
import tkMessageBox


# def resize(ev=None):
#     label.config(font='Helvetica -%d bold' % scale.get())
#
# root = Tkinter.Tk()
# root.geometry('250x150')
#
# label = Tkinter.Label(root, text='Hello', font='Helvetica -12 bold')
# label.pack(fill=Tkinter.Y, expand=1)
#
# scale = Tkinter.Scale(root, from_=10, to=40, orient=Tkinter.HORIZONTAL, command=resize)
# scale.set(12)
# scale.pack(fill=Tkinter.X, expand=1)
#
# # quit = Tkinter.Button(root, text='Quit', command=root.quit, bg='red', fg='white')
# quit = Tkinter.Button(root, text='Quit', command=root.quit, activeforeground='red', activebackground='white')
# quit.pack(fill=Tkinter.X, expand=1)
#
# Tkinter.mainloop()

################################################################

# CRIT = 'crit'
# WARN = 'warn'
# REGU = 'regu'
#
# SIGNS = {
#     'do not enter': CRIT,
#     'railroad crossing': WARN,
#     '55\nspeed limit': REGU,
#     'wrong way': CRIT,
#     'merging traffic': WARN,
#     'one way': REGU
# }
#
# critCb = lambda: tkMessageBox.showerror('Error', 'Error Button Pressed!')
# warnCb = lambda: tkMessageBox.showwarning('Warning', 'Warning Button Pressed!')
# infoCb = lambda: tkMessageBox.showinfo('Info', 'Info Button Pressed!')
#
# root = Tkinter.Tk()
# root.title('Road Signs')
#
# Tkinter.Button(root, text='Quit', command=root.quit, bg='red', fg='white').pack()
#
# ptoButton = pto(Tkinter.Button, root)
# CritButton = pto(ptoButton, command=critCb, fg='red', bg='white')
# WarnButton = pto(ptoButton, command=warnCb, bg='goldenrod1')
# ReguButton = pto(ptoButton, command=infoCb, bg='white')
#
# for k, v in SIGNS.items():
#     cmd = '%sButton(text=%r%s).pack(fill=Tkinter.X, expand=True)' \
#           % (v.title(), k, '.upper()' if v == CRIT else '.title()')
#     eval(cmd)
#
# Tkinter.mainloop()


################################################################

# def changeItems():
#     names.append('java')
#     tnames.set(tuple(names))
#
# root = Tkinter.Tk()
# root.geometry('+400+200')
# root.minsize(400, 200)
# root.title('test')
#
# names = ['python', 'TCL', 'ruby']
# tnames = Tkinter.StringVar()
# tnames.set(tuple(names))
#
# l = Tkinter.Listbox(root, listvariable=tnames, height = 10).grid()
# Tkinter.Button(root, text='submit', command=changeItems).grid()
#
# root.mainloop()


################################################################

class ListDir(object):
    def __init__(self, initDir):
        self.root = Tkinter.Tk()
        self.root.title('Dir Lister v1.1')
        self.cwd = Tkinter.StringVar(self.root)
        self.label = Tkinter.Label(self.root, fg='blue', font=('Helvetica', 12, 'bold'))
        self.label.pack()

        self.listfm = Tkinter.Frame(self.root)
        self.listsb = Tkinter.Scrollbar(self.listfm)
        self.listsb.pack(side=Tkinter.RIGHT, fill=Tkinter.Y)
        self.listbx = Tkinter.Listbox(self.listfm, height=15, width=50, yscrollcommand=self.listsb.set)
        self.listbx.bind('<Double-1>', self.setDirandGo)
        self.listsb.config(command=self.listbx.yview)
        self.listbx.pack(side=Tkinter.LEFT, fill=Tkinter.BOTH)
        self.listfm.pack()

        self.entry = Tkinter.Entry(self.root, width=50, textvariable=self.cwd)
        self.entry.bind('<Return>', self.doLS)
        self.entry.pack(fill=Tkinter.X)

        self.bfm = Tkinter.Frame(self.root)
        ptoButton = pto(Tkinter.Button, self.bfm, activeforeground='white')
        self.Clr = pto(ptoButton, text='Clear', activebackground='green')
        self.Lst = pto(ptoButton, text='List', activebackground='blue')
        self.Quit = pto(ptoButton, text='quit', activebackground='red', command=self.root.quit)
        self.Clr = self.Clr()
        self.Lst = self.Lst()
        self.Quit = self.Quit()
        self.Clr.pack(side=Tkinter.LEFT)
        self.Lst.pack(side=Tkinter.LEFT)
        self.Quit.pack(side=Tkinter.LEFT)
        self.bfm.pack()

        if initDir:
            self.cwd.set(os.curdir)
            self.doLS()

if __name__ == '__main__':
    ListDir(os.getcwd())
    Tkinter.mainloop()
