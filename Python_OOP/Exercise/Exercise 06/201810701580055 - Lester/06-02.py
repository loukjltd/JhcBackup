'''
Name:Lester
Class:Net182
ID:201810701580055
'''
from tkinter import *
import tkinter.messagebox as ms
t = Tk()
f1 = Frame(t)
f2 = Frame(t)
label1 = Label(f1,text='ENTER YOUR NAME:')
label1.pack()
t1 = Entry(f1)
t1.pack()
label2 = Listbox(f1)
label2.pack()
label2.insert('end','Male')
label2.insert('end','Female')
f1.pack(side = 'top')
f2.pack(side = 'bottom')
def showname():
    g = t1.get()
    ms.showinfo('My name',g)
def changename():
    t1.delete(0,END)
    t1.insert(0,'Sam')
b1 = Button(f2,text='showname',fg='red',command=showname)
b1.pack(side='left')
b1 = Button(f2,text='changename',fg='green',command=changename)
b1.pack(side='right')
t.mainloop()
