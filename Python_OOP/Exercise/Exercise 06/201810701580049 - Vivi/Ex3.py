#Exercise 06-03
'''
class net182
id 2018100701580049
name vivi
'''

from tkinter import *  # get everything in tkinter module


def calcF():
    w = Entry.get(text)
    new_temp = (float(w) * 1.8) + 32
    myLabel.config(text=str(new_temp))

def calcC():
    w = Entry.get(text)
    new_temp = (float(w) -32) /1.8
    myLabel.config(text=str(new_temp))




root = Tk()

topFrame = Frame(root)
topFrame.pack()

text = Entry(topFrame)
text.pack()

myLabel = Label(topFrame, text="")
myLabel.pack()

button1 = Button(topFrame,text="Celsius",fg="red",command = calcC)
button2 = Button(topFrame,text="Fahrenheit",fg="blue",command = calcF)
button1.pack(side="left")
button2.pack(side="left")

root.mainloop()
