#
'''
class:net182
name:lenny
ID:201810701580045
'''
from tkinter import *
import tkinter.messagebox
root = Tk()

topFrame = Frame(root)
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

myLabel = Label(topFrame, text="Enter your name:")
myLabel.pack()

entryEnter = Entry(topFrame)
entryEnter.pack()


myEntry = Entry(topFrame)
myEntry.pack()

myListbox1 = Listbox(topFrame)
myListbox1.insert(0,'Male','Female')
myListbox1.pack()

def showName():
    name = Entry.get(myEntry)
    tkinter.messagebox.showinfo("my name", str(name))

def changeName():
    entryEnter.delete(0,END)
    entryEnter.insert(0,'sam')

button1 = Button(bottomFrame, text="Show name", fg="red",command = showName)
button2 = Button(bottomFrame, text="change name", fg="green",command = changeName)
button1.pack()
button2.pack()

root.mainloop()