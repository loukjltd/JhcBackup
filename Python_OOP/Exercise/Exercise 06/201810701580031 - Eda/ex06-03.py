# exercise 06-03
'''
student name: Eda
ID: 201810701580031
class: network182
'''

from tkinter import *
import tkinter.messagebox as ms

root = Tk()

myEntry = Entry(root)
myEntry.pack()
myEntry.insert(0, '')
myLabel = Label(root, text='')
myLabel.pack()


def calcC():
    a = float(myLabel)
    c = (myEntry * 1.8) + 32
    myLabel.config(text=str(a))

def calcF():
    b = float(myLabel)
    d = (myEntry * 1.8) + 32

myLabel.config(text=str(b))
button1 = Button(root, text='Fahrenheit', fg='red', command=calcC)
button2 = Button(root, text='', fg='green', command=calcF)

button1.pack(side=LEFT)
button2.pack(side=RIGHT)
root.mainloop()