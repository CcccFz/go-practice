__author__ = 'Administrator'

#未实现：1.文本查找  2.status显示光标所在位置  3.打开文件后全选就无效 4.快捷键未实现

from tkinter.messagebox import *
from tkinter.scrolledtext import *
from tkinter.filedialog import *

editList = []
editRoot = None
fileName = None

def notePadNewEdit():
    global editRoot
    editList.append(NotePadExit(editRoot))

class NotePadExit:
    def __init__(self, root):
        if None == root:
            self.root = Tk()
        else:
            self.root = Toplevel(root)

        self.root.geometry('800x500+100+100')
        self.root.title('New TkNotePad')
        self.menu = Menu(self.root)
        self.root.config(menu = self.menu)

        self.fileMenu = Menu(self.menu)
        self.helpMenu = Menu(self.menu)
        self.editMenu = Menu(self.menu)
        self.menu.add_cascade(label = '文件', menu = self.fileMenu)
        self.menu.add_cascade(label = '编辑', menu = self.editMenu)
        self.menu.add_cascade(label = '帮助', menu = self.helpMenu)

        self.fileMenu.add_command(label = '新建', accelerator = 'Ctrl + N', command = notePadNewEdit)
        self.fileMenu.add_command(label = '打开..', accelerator = 'Ctrl + O', command = self.editOpenFile)
        self.fileMenu.add_command(label = '保存', accelerator = 'Ctrl + S', command = self.editSaveFile)
        self.fileMenu.add_command(label = '另存为..', accelerator = 'Ctrl + Shift + S', command = self.editSaveAsFile)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label = '关闭', accelerator = 'Ctrl + N', command = self.editClose)
        self.fileMenu.add_command(label = '退出', accelerator = 'Ctrl + N', command = self.notePadExit)

        self.editMenu.add_command(label = '撤销', accelerator = 'Ctrl + Z', command = self.editUndo)
        self.editMenu.add_command(label = '重做', accelerator = 'Ctrl + Y', command = self.editRedo)
        self.editMenu.add_separator()
        self.editMenu.add_command(label = '剪切', accelerator = 'Ctrl + X', command = self.editCut)
        self.editMenu.add_command(label = '复制', accelerator = 'Ctrl + C', command = self.editCopy)
        self.editMenu.add_command(label = '粘贴', accelerator = 'Ctrl + V', command = self.editPaste)
        self.editMenu.add_separator()
        self.editMenu.add_command(label = '全选', accelerator = 'Ctrl + A', command = self.editSelectAll)
        self.editMenu.add_command(label = '查找..', accelerator = 'Ctrl + F', command = self.editSearch)

        self.helpMenu.add_command(label = '关于', command = self.notePadAbout)

        self.frame = Frame(self.root, width = 512)
        self.frame.pack(expand = 1, fill = BOTH)
        self.editNumLine = Label(self.frame, width =2, bg = 'antique white')
        self.editNumLine.pack(side = LEFT, fill = Y)
        self.edit = ScrolledText(self.frame, background = "white")
        self.edit.pack(expand = 1, side = LEFT, fill = BOTH)

        self.editStatus = Label(self.root, text = 'Ln20', bd = 1, relief = SUNKEN, anchor = W)
        self.editStatus.pack(side = BOTTOM, fill = X)

    def editOpenFile(self):
        global fileName
        fileName = askopenfilename(defaultextension = '.txt', filetypes = [("Python file", "*.*")])
        if fileName == '':
            openFile = None
        else:
            self.root.title(os.path.basename(fileName))
            self.edit.delete(1.0, END)
            fop = open(fileName, 'r')
            self.edit.insert(1.0, fop.read())
            fop.close()
            #for line in input(fileName):
            #    self.edit.insert(END, line)

    def editSaveFile(self):
        global fileName
        try:
            fop = open(fileName, "w")
            fop.write(self.edit.get(1.0, END))
            fop.flush()
            fop.close()
        except:
            self.editSaveAsFile()

    def editSaveAsFile(self):
        global fileName
        fileName = asksaveasfilename(initialfile = '未命名.txt', defaultextension = '.txt')
        if fileName:
            self.root.title(os.path.basename(fileName))
            fop = open(fileName, "w")
            fop.write(self.edit.get(1.0, END))
            fop.flush()
            fop.close()
        else:
            fileName = None

    def editClose(self):
        self.root.destroy()

    def notePadExit(self):
        sys.exit(0)

    def editUndo(self):
        self.edit.event_generate('<<Undo>>')
        #self.edit.edit_undo()

    def editRedo(self):
        self.edit.event_generate('<<Redo>>')
        #self.edit.edit_redo()

    def editCut(self):
        self.edit.event_generate('<<Cut>>')

    def editCopy(self):
        self.edit.event_generate('<<Copy>>')

    def editPaste(self):
        self.edit.event_generate('<<Paste>>')

    def editSelectAll(self):
        self.edit.tag_add('sel', '1.0', END)

    def editSearch(self):

        def editGetSearch():
            findStr = entry.get()
            start = 1.0
            while True:
                cur = self.edit.search(findStr, start, END)
                if not cur:
                    break
                else:
                    self.edit.tag_add('sel', start, END)
                    start = cur + "+1c"

        topsearch = Toplevel(self.root)
        topsearch.geometry('300x30+200+250')

        label = Label(topsearch, text = 'Find:')
        label.grid(row = 0, column = 0, padx = 5)

        entry = Entry(topsearch, width = 20)
        entry.grid(row = 0, column = 1, padx = 5)

        button = Button(topsearch, text = '查找', width = 10, command = editGetSearch)
        button.grid(row = 0, column = 2, padx = 10)

    def callback(self, event):
        self.edit.focus_set()
        print("clicked at:", event.x, event.y)

    def notePadAbout(self):
        showinfo("TkText","V1.0\n"
            "written in 2015\n"
            "writer : CcccFz")

if __name__ == '__main__':
    editList.append(NotePadExit(editRoot))
    mainloop()





