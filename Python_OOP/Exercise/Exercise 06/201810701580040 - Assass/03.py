#Exercise 06-03
'''
Name:Assass
Class:Net182
ID:201810701580040
'''
from tkinter import *
import tkinter.messagebox as ms
t= Tk()
f1=Frame(t)
f1.pack(side='bottom')
t1=Entry(t)
t1.pack()
l1=Label(t)
l1.pack()
def calcC():
    g=float(t1.get())
    l1.config(text=str(5/9*(g-32)))
def calcF():
    g=float(t1.get())
    l1.config(text=str((9/5)*g+32))
b1=Button(f1,text='Celsius',fg='red',command=calcC)
b1.pack(side='left')
b2=Button(f1,text='Fahrenheit',fg='green',command=calcF)
b2.pack(side='right')

t.mainloop()