#Exercise 06-02
'''
name: Jax
idnumber: 201810701580041
class: net182
'''

from tkinter import *
import tkinter.messagebox as ms
t= Tk()
f1=Frame(t)
f2=Frame(t)
la1=Label(f1,text='Enter your name:')
la1.pack()
te1=Entry(f1)
te1.pack()
la2=Listbox(f1)
la2.pack()
la2.insert('end','Male')
la2.insert('end','Female')
f1.pack(side='top')
f2.pack(side='bottom')
def showname():
    g=te1.get()
    ms.showinfo('My name',g)
def changename():
    te1.delete(0,END)
    te1.insert(0,'Sam')
b1=Button(f2,text='Show name',fg='red',command=showname)
b1.pack(side='left')
b1=Button(f2,text='Change name',fg='green',command=changename)
b1.pack(side='right')
t.mainloop()
