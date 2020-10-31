# Exercise 06-02
'''
Student Name: Ted
ID: 201810701580058
Class: Net 182
'''

from tkinter import *
import tkinter.messagebox as ms
def showName():
    name=Entry.get(entry)
    ms.showinfo('my name',name)
    lb.insert(0,name)
def change_name():
    entry.delete(0,END)
root = Tk()
topframe=Frame(root)
topframe.pack()
mylabel=Label(topframe,text='enter your name:')
mylabel.pack()
entry=Label(topframe,text='enter your name:')
entry=Entry(topframe)
entry.pack()
entry.insert(0,' ')
buttomframe=Frame(root)
buttomframe.pack(side=BOTTOM)
var = StringVar()
lb = Listbox(topframe, listvariable = var)
list_item = []
list_item.append('male')
list_item.append('Female')
for item in list_item:
    lb.insert(END,item)
lb.pack()

showName=Button(topframe,text='show name',fg='red',command=showName)
showName.pack(side=LEFT)
change_name=Button(topframe,text='change name',fg='green',command=change_name)
change_name.pack(side=LEFT)

root.mainloop()