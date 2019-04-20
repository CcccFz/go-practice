# -*- coding: utf-8 -*-
__author__ = 'Duome'

""" 成都房产信息搜索界面
    label
    工具栏grid搜索最低价位，最高价位，确定
"""

from Tkinter import Tk, Frame, Entry, Label, Button
from tkMessageBox import showerror, showinfo

from xlsx_filter.filter import Filter
from xlsx_filter.xlsx import Xlsx


class Interface(object):
    """ 搜索界面 """

    def __init__(self):
        self.root = Tk()
        self.xlsx = Xlsx(r'anjuke.xlsx')   # 将xlsx功能与界面绑定
        self.filter = Filter(self.xlsx.get_data())     # 获取excel中的原始数据后，将filter功能与界面绑定
        self.set_layout()


    def set_layout(self):
        self.root.config(bg='#F8F8FF')
        self.root.title(u'成都房产信息搜索')
        self.root.geometry('500x100')

        frame = Frame(self.root, width=10000, height=10000, bg='#F8F8FF')
        frame.pack()

        entry_min_price = Entry(frame, width=10, cursor='xterm')
        entry_min_price.insert(0, u'每平最低价')
        entry_min_price.config(bg='#F5F5F5', font=('Arial', '15'))
        entry_min_price.grid(row=0, column=1, padx=20)

        label_line = Label(frame, text=u'————', width=8)
        label_line.config(fg='#00008B', bg='#F8F8FF')
        label_line.grid(row=0, column=2, padx=5)

        entry_max_price = Entry(frame, width=10, cursor='xterm')
        entry_max_price.insert(0, u'每平最高价')
        entry_max_price.config(bg='#F5F5F5', font=('Arial', '15'))
        entry_max_price.grid(row=0, column=3, padx=20)

        def start_search():
            flag = True
            self.filter.rules = []

            ############################# rule 1 #####################################
            try:
                lprice = int(entry_min_price.get())
                hprice = int(entry_max_price.get())
            except (UnicodeEncodeError, ValueError):
                flag = False
                showerror('错误输入', u'输入无法识别，请重新输入')
            else:
                if lprice < 0 or hprice < 0 and lprice > hprice:
                    showerror('错误输入', u'输入不正确，请重新输入')
                    flag = False
                else:
                    cnt = self.xlsx.head.index(u'参考单价')
                    rule = lambda x: True if lprice <= x[cnt] < hprice or lprice == x[cnt] == hprice else False
                    self.filter.rules.append(rule)
            ############################# rule 1 end #####################################

            if flag:
                result_data = self.filter.get_result()
                self.xlsx.save_data(result_data, r'result.xlsx')
                showinfo('过滤成功', u'过滤结果已存入本地result.xlsx中')

        button = Button(frame, text=u'搜索', width=10)
        button.config(font=('Arial', '10', 'bold'), fg='#191970', bg='#00BFFF', command=start_search)
        button.grid(row=0, column=4, padx=10)


    def start(self):
        self.root.mainloop()
