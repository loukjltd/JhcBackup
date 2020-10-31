#Exercise 06-03
'''
student name :Vicky
ID:201810701580032
class:Net182
'''

from tkinter import *
import tkinter.messagebox as ms

root=Tk()
tx1=Entry(root)
tx1.pack()
tx1.insert(0,'')
MyLabel=Label(root)
MyLabel.pack()
def calcC():
    c=float(Entry.get(tx1))
    f=c*9/5+32
    MyLabel.config(text=str(f))
def calcF():
    f = float(Entry.get(tx1))
    c=(f-32)*5/9
    MyLabel.config(text=str(c))

topFrame = Frame(root)
topFrame.pack()
bottomFrame=Frame(root)
bottomFrame.pack(side=BOTTOM)
Celsius=Button(bottomFrame,text='Celsius',fg='red',command=calcC)
Fahrenheit=Button(bottomFrame,text='Fahrenheit',fg='green',command=calcF)
Celsius.pack(side=LEFT)
Fahrenheit.pack(side=LEFT)
root.mainloop()