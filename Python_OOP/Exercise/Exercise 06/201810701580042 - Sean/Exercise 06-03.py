# Exercise 06-03
'''
Student Name: Sean
ID: 201810701580042
Class: Network 182
'''

from tkinter import *

root = Tk()

topFrame = Frame(root)
topFrame.pack(side=TOP)
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

entryEnter = Entry(topFrame)
entryEnter.pack()

displayLabel = Label(topFrame, text='')
displayLabel.pack()


def calcC():
    tempC = float(Entry.get(entryEnter))
    tempF = tempC * 1.8 + 32
    displayLabel.config(text=str(tempF))


def calcF():
    tempF = float(Entry.get(entryEnter))
    tempC = (tempF - 32) / 1.8
    displayLabel.config(text=str(tempC))


buttonC = Button(bottomFrame, text='Celsius', fg='red', command=calcC)
buttonC.pack(side=LEFT)
buttonF = Button(bottomFrame, text='Fahrenheit', fg='green', command=calcF)
buttonF.pack(side=RIGHT)

root.mainloop()
