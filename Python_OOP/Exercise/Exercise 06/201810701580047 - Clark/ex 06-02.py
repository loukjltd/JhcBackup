# Exercise 06-02
'''
name:Clark
class:net182
I  D:201810701580047
'''
from tkinter import *
from tkinter import messagebox
root = Tk()
root.title('ex 06-02')
# 框架
lf = Frame(root)
lf.pack()
interF = Frame(root)
interF.pack()
bf = Frame(root)
bf.pack()
# 头
title = Label(lf, text='Enter you name:')
title.pack()
# 输入显示
text = Text(interF)
text.pack()
lnsert = Entry(text)
lnsert.pack()
lst = Listbox(interF)
lst.pack()
# 函数


def show_name():
    messagebox.showinfo('your name', Entry.get(lnsert))


def change_name():
    lst.insert(0, Entry.get(lnsert))
    lnsert.delete(0, END)


# 按钮
sn = Button(bf, text='Show name', fg='red', command=show_name)
sn.pack(side=LEFT)
cn = Button(bf, text='Change name', fg='green', command=change_name)
cn.pack(side=LEFT)
root.mainloop()
