#Exercise 06-02
'''
Name:Assass
Class:Net182
ID:201810701580040
'''
from tkinter import *
import tkinter.messagebox as ms
t= Tk()
f1=Frame(t)
f2=Frame(t)
l1=Label(f1,text='Enter your name:')
l1.pack()
t1=Entry(f1)
t1.pack()
l2=Listbox(f1)
l2.pack()
l2.insert('end','Male')
l2.insert('end','Female')
f1.pack(side='top')
f2.pack(side='bottom')
def showname():
    g=t1.get()
    ms.showinfo('My name',g)
def changename():
    t1.delete(0,END)
    t1.insert(0,'Sam')
b1=Button(f2,text='show name',fg='red',command=showname)
b1.pack(side='left')
b1=Button(f2,text='change name',fg='green',command=changename)
b1.pack(side='right')

t.mainloop()